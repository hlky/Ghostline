# A Cool Metal Fire

Journal: `quests/side_quest/sq031_smack_my_bitch_up` · `SideQuest` · hash `653340120`.

**Coverage: journal-linked.** 42 exact journal-linked nodes in 7 resources; 9 resources in the inspected dependency context.

Resource roles in that context: 8 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../corpus-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Now, I don't ask you for much, but I gotta zero Smasher myself. That motherfucker thinks he's invincible. Worse, so does Rogue. All these years, Arasaka Tower's been haunting her. Enough's enough. I'm taking control this one time, I'm finding him, I'm wiping Adam Smasher off the face of the earth. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/01_afterlife/01_bug_drags` |
| Talk to Cassius. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/02_smack_tattoo/01_get_tattoo` |
| Watch Ruby dance. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease` |
| Talk to Ruby. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease2` |
| Talk to Ruby. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease3` |
| Talk to Ruby. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease4` |
| Buy champagne at the bar. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/02_buy_champagne` |
| Drink with Ruby. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne` |
| Drink with the others in the club. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne1` |
| Choose a pill. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne2` |
| Take a pill to keep control over V's body. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne3` |
| Go to the bathroom. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/04_find_toilet` |
| Talk to the bouncers. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/05_talk_to_patrons` |
| Take Ruby back to your place. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/08_drive_streapper` |
| Wait for Ruby to leave the club. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/09_wait_for_streapper` |
| Have fun. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/13_enjoy_evening` |
| Talk to Rogue. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/04_smack_motel/01_talk_to_stranger1` |
| Talk to Johnny. (Primary) | `quests/side_quest/sq031_smack_my_bitch_up/04_smack_motel/03_talk_to_johnny` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sq031_cinematic_bugfixes.questphase / h37 / 3` (Condition) | `quests/side_quest/sq031_smack_my_bitch_up` | 3:False → 1:In; 2:Out → 3:In; 3:True → 4:In |
| `sq031_afterlife.questphase / h0 / 124` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/01_afterlife/01_bug_drags` | 122:sq031_00_johnny_out → 124:Active; 124:Out → 192:Active |
| `sq031_afterlife.questphase / h0 / 192` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/01_afterlife/01_bug_drags/description` | 124:Out → 192:Active |
| `sq031_brawl.questphase / h0 / 33` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/05_talk_to_patrons` | 58:Out1 → 33:Succeeded; 33:Out → 34:Active |
| `sq031_brawl.questphase / h0 / 34` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/06_beat_patrons` | 33:Out → 34:Active |
| `sq031_brawl.questphase / h0 / 35` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/06_beat_patrons` | 15:Out → 35:Succeeded; 35:Out → 56:In |
| `sq031_motel.questphase / h66 / 9` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease` | 0:Out → 9:Succeeded; 9:Out → 5:In |
| `sq031_01b_smack_tatto.scene / scene / 244` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/02_smack_tattoo/01_get_tattoo` | 411:0:0 → 244:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01b_smack_tatto.scene / scene / 336` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/01_afterlife` | 336:0:0 → 459:0:1; 706:0:0 → 336:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01b_smack_tatto.scene / scene / 339` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/02_smack_tattoo/01_get_tattoo` | 339:0:0 → 579:0:3; 535:0:0 → 339:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01b_smack_tatto.scene / scene / 579` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/02_smack_tattoo` | 339:0:0 → 579:0:3; 579:0:0 → 645:0:1; 579:0:0 → 699:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 313` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease` | 925:0:0 → 313:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 315` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease` | 227:0:0 → 315:0:3; 315:0:0 → 351:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 351` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/02_buy_champagne` | 315:0:0 → 351:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 480` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease3` | 3109:0:0 → 480:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 482` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease3` | 482:0:0 → 484:0:1; 2067:0:0 → 482:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 484` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/08_drive_streapper` | 482:0:0 → 484:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 514` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/08_drive_streapper` | 514:0:0 → 516:0:1; 2266:0:0 → 514:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 516` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease4` | 514:0:0 → 516:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 731` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/05_talk_to_patrons` | 1582:0:0 → 731:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 918` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease4` | 918:0:0 → 920:0:1; 2084:0:0 → 918:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 920` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/13_enjoy_evening` | 918:0:0 → 920:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 922` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/13_enjoy_evening` | 557:0:0 → 922:0:3; 922:0:0 → 2474:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1151` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/02_buy_champagne` | 323:0:0 → 1151:0:3; 1151:0:0 → 1153:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1153` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne` | 1151:0:0 → 1153:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1561` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne1` | 2608:0:0 → 1561:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1563` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne1` | 1563:0:0 → 1565:0:1; 3126:0:0 → 1563:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1565` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne2` | 1563:0:0 → 1565:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1568` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne2` | 1568:0:0 → 1574:0:1; 1699:0:0 → 1568:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1574` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease2` | 1568:0:0 → 1574:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1577` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/01_watch_streaptease2` | 1128:2:2 → 1577:0:3; 1577:0:0 → 1578:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1578` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/04_find_toilet` | 1577:0:0 → 1578:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1582` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/04_find_toilet` | 260:0:0 → 1582:0:3; 1582:0:0 → 731:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1585` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/05_talk_to_patrons` | 1536:0:0 → 1585:0:3; 1585:0:0 → 1586:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 1586` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/09_wait_for_streapper` | 1585:0:0 → 1586:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 2608` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/03_pour_champagne` | 1714:0:0 → 2608:0:1; 2608:0:0 → 1561:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01c_smack_striptease.scene / scene / 3109` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/03_smack_streaptease/05_talk_to_patrons` | 1493:0:0 → 3109:0:3; 3109:0:0 → 480:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01d_smack_rogue.scene / scene / 465` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/04_smack_motel/01_talk_to_stranger1` | 305:0:0 → 465:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01d_smack_rogue.scene / scene / 541` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/04_smack_motel/01_talk_to_stranger1` | 541:0:0 → 549:0:1; 752:2:0 → 541:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01d_smack_rogue.scene / scene / 549` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/04_smack_motel/03_talk_to_johnny` | 541:0:0 → 549:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01d_smack_rogue.scene / scene / 553` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up/04_smack_motel/03_talk_to_johnny` | 380:0:0 → 553:0:3; 553:0:0 → 593:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `sq031_01d_smack_rogue.scene / scene / 593` (Journal) | `quests/side_quest/sq031_smack_my_bitch_up` | 553:0:0 → 593:0:3; 593:0:0 → 810:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sq031_afterlife.questphase / h0 / 122` | `base\quest\side_quests\sq031\scenes\sq031_00_johnny.scene`; `#sq031_00_sm_johnny` | 172:Out → 122:sq031_00_johnny_in; 122:sq031_00_johnny_out → 191:In; 122:sq031_00_johnny_out → 124:Active; 122:sq031_00_johnny_out → 210:In; 122:sq031_00_johnny_out → 143:sq031_01_afterlife_bartender_in |
| `sq031_afterlife.questphase / h0 / 143` | `base\quest\side_quests\sq031\scenes\sq031_01a_smack_afterlife.scene`; `#sq031_01a_sm_smack_afterlife` | 122:sq031_00_johnny_out → 143:sq031_01_afterlife_bartender_in; 143:sq031_01_afterlife_bartender_out → 203:In1; 143:sq031_01_afterlife_bartender_out → 223:In |
| `sq031_brawl.questphase / h0 / 51` | `base\quest\side_quests\sq031\scenes\sq031_01c_smack_striptease.scene`; `#sq031_01c_sm_smack_striptease` | 46:Out → 51:sq031_01a_brawler_taunt_in |
| `sq031_motel.questphase / h0 / 256` | `base\quest\side_quests\sq031\scenes\sq031_01d_smack_rogue.scene`; `#sq031_01d_sm_smack_rogue` | 292:Out → 256:sq031_01_motel_arrived_in; 256:sq031_01_motel_room_out → 275:In |
| `sq031_motel.questphase / h0 / 271` | `base\quest\side_quests\sq031\scenes\sq031_01d_smack_rogue.scene`; `#sq031_01d_sm_smack_rogue` | 288:Out → 271:sq031_01_motel_fluff_1_in; 271:sq031_01_motel_fluff_out → 287:In |
| `sq031_motel.questphase / h0 / 290` | `base\quest\side_quests\sq031\scenes\sq031_01d_smack_rogue.scene`; `#sq031_01d_sm_smack_rogue` | 290:sq031_01_motel_fluff_out → 287:In; 289:Out → 290:sq031_01_motel_fluff_2_in |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\side_quests\sq031\sq031.questphase` / h0 / 58 | `sq031_afterlife.questphase` | 63: Phase; 63:Out1 → 58:In1; 58:Out1 → 59:In1 |
| `base\quest\side_quests\sq031\sq031.questphase` / h0 / 61 | `sq031_motel.questphase` | 60: Phase: sq031_striptease.questphase; 73: Phase; 61:Out1 → 53:In1; 60:Out1 → 61:In1; 73:Out1 → 61:In1 |
| `base\quest\side_quests\sq031\phases\sq031_afterlife.questphase` / h0 / 122 | `sq031_00_johnny.scene` | 172: Checkpoint; 172:Out → 122:sq031_00_johnny_in; 122:sq031_00_johnny_out → 191:In; 122:sq031_00_johnny_out → 124:Active; 122:sq031_00_johnny_out → 210:In; 122:sq031_00_johnny_out → 143:sq031_01_afterlife_bartender_in |
| `base\quest\side_quests\sq031\phases\sq031_afterlife.questphase` / h0 / 143 | `sq031_01a_smack_afterlife.scene` | 122: Scene: sq031_00_johnny.scene; 122:sq031_00_johnny_out → 143:sq031_01_afterlife_bartender_in; 143:sq031_01_afterlife_bartender_out → 203:In1; 143:sq031_01_afterlife_bartender_out → 223:In |
| `base\quest\side_quests\sq031\phases\sq031_tattoo.questphase` / h0 / 132 | `sq031_01b_smack_tatto.scene` | 146: GameManager; 132:sq031_01_tattoo_out → 126:In; 146:Out → 132:sq031_01_tattoo_in; 132:cleaning_aftelife → 141:In1 |
| `base\quest\side_quests\sq031\phases\sq031_brawl.questphase` / h0 / 51 | `sq031_01c_smack_striptease.scene` | 46: PauseCondition: {"seconds": 3}; 46:Out → 51:sq031_01a_brawler_taunt_in |
| `base\quest\side_quests\sq031\phases\sq031_striptease.questphase` / h0 / 199 | `sq031_01c_smack_striptease.scene` | 254: GameManager; 247: Input; 254:Out → 199:sq031_01_streapptease_in; 247:Out → 199:sq031_01_brawl_in; 199:sq031_01_smbu_ends_out → 250:In2; 199:sq031_01_smbu_ends_out → 253:In |
| `base\quest\side_quests\sq031\phases\sq031_motel.questphase` / h0 / 256 | `sq031_01d_smack_rogue.scene` | 292: GameManager; 292:Out → 256:sq031_01_motel_arrived_in; 256:sq031_01_motel_room_out → 275:In |
| `base\quest\side_quests\sq031\phases\sq031_motel.questphase` / h0 / 271 | `sq031_01d_smack_rogue.scene` | 288: PauseCondition: #sq031_tr_rogue_left_motel_room; 288:Out → 271:sq031_01_motel_fluff_1_in; 271:sq031_01_motel_fluff_out → 287:In |
| `base\quest\side_quests\sq031\phases\sq031_motel.questphase` / h0 / 290 | `sq031_01d_smack_rogue.scene` | 289: PauseCondition: #sq031_tr_motel_exit_johnny; 290:sq031_01_motel_fluff_out → 287:In; 289:Out → 290:sq031_01_motel_fluff_2_in |
| `base\quest\side_quests\sidequests.questphase` / h0 / 38 | `sq031.questphase` | 94: Phase: sq032.questphase; 94:Out1 → 38:In1; 38:Out1 → 39:In1 |
| `base\quest\side_quests\sq031\sq031.questphase` / h0 / 59 | `sq031_tattoo.questphase` | 58: Phase: sq031_afterlife.questphase; 65: Phase; 58:Out1 → 59:In1; 65:Out1 → 59:In1; 59:Out1 → 60:In1 |
| `base\quest\side_quests\sq031\sq031.questphase` / h0 / 60 | `sq031_striptease.questphase` | 59: Phase: sq031_tattoo.questphase; 67: Phase; 101: Phase; 59:Out1 → 60:In1; 67:Out1 → 60:In1; 60:Out1 → 61:In1; 101:Out1 → 60:In2 |
| `base\quest\cyberpunk2077.questphase` / h520 / 5 | `sidequests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:sq026_02_signal → 5:sq026_02_signal; 7:Out1 → 5:In1; 8:Out → 5:In1; 21:Out → 5:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `sq031_00_johnny.scene` | sq031_00_johnny_in → sq031_00_johnny_out, sq031_00_kill_signal | Johnny; Emmerick; Claire; Player; V_Posessed; 72 nodes / 97 edges |
| `sq031_01a_smack_afterlife.scene` | sq031_01_afterlife_bartender_in, sq031_01a_not_leave_out, Start 5 → sq031_01_afterlife_bartender_out | Johnny; Rogue; Clair; Emmerick; bar_guest; V_Posessed; 90 nodes / 117 edges |
| `sq031_01b_smack_tatto.scene` | sq031_01_tattoo_in → sq031_01_tattoo_out, cleaning_aftelife | Johnny; Cassious; Pandora; Player; 67 nodes / 86 edges |
| `sq031_01c_smack_striptease.scene` | preview, preview_02, sq031_01_streapptease_in, sq031_01_brawl_in → sq031_01_smbu_ends_out | Johnny; Ruby; Barkeeper; Brawler1; Brawler2; Guard; Simone; Drunk_Guy; Drunk_Girl; Cybereyes_Guy; Back_Woman; player_tpp_male; player_tpp_female; Ruby_vehicle; Player; 307 nodes / 355 edges |
| `sq031_01d_smack_rogue.scene` | sq031_01_motel_fluff_2_in, sq031_01_motel_fluff_1_in, q115_reuse_johnny, sq031_01_motel_arrived_in → sq031_01_motel_room_out, sq031_01_motel_fluff_out | Johnny; Rogue; Player; 154 nodes / 179 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sq031_00_johnny.scene / n92 / 0` | [Take Misty's pills] Ready. (`let go`) | No option-level predicate stored | 0:0 → 331:0:1 |
| `sq031_00_johnny.scene / n92 / 1` | Just gonna talk to Rogue, right? (`the plan`) | No option-level predicate stored | 0:1 → 299:0:0 |
| `sq031_00_johnny.scene / n92 / 2` | Wanna play off her conscience, feelings of guilt? (`guilty`) | No option-level predicate stored | 0:2 → 308:0:0 |
| `sq031_01a_smack_afterlife.scene / n21 / 0` | Blue Glass. (`blueglass`) | No option-level predicate stored | 0:0 → 397:0:0 |
| `sq031_01a_smack_afterlife.scene / n21 / 1` | Tequila Old Fashioned. (`tequila`) | No option-level predicate stored | 0:1 → 964:0:0 |
| `sq031_01a_smack_afterlife.scene / n946 / 0` | Know what I need now? (`what i need`) | No option-level predicate stored | 0:0 → 902:0:0 |
| `sq031_01a_smack_afterlife.scene / n946 / 1` | Cassius Ryder. Name mean anything to you? (`cassius`) | No option-level predicate stored | 0:1 → 949:0:0 |
| `sq031_01a_smack_afterlife.scene / n1069 / 0` | [Drink] (`Wypij.`) | No option-level predicate stored | 0:0 → 1239:0:1 |
| `sq031_01a_smack_afterlife.scene / n1073 / 0` | Same again. (`order`) | No option-level predicate stored | 0:0 → 658:0:0 |
| `sq031_01a_smack_afterlife.scene / n1076 / 0` | [Drink] (`Wypij`) | No option-level predicate stored | 0:0 → 1245:0:1 |
| `sq031_01b_smack_tatto.scene / n262 / 0` | Billy-goat. (`goat`) | No option-level predicate stored | 0:0 → 265:0:0 |
| `sq031_01b_smack_tatto.scene / n262 / 1` | The other. (`second`) | No option-level predicate stored | 0:1 → 268:0:0 |
| `sq031_01c_smack_striptease.scene / n1074 / 0` | [Drink] (`Option`) | No option-level predicate stored | 0:0 → 1086:0:0 |
| `sq031_01c_smack_striptease.scene / n1076 / 0` | [Drink] (`Option`) | No option-level predicate stored | 0:0 → 1087:0:0 |
| `sq031_01c_smack_striptease.scene / n1077 / 0` | [Drink] (`Option`) | No option-level predicate stored | 0:0 → 1088:0:0 |
| `sq031_01c_smack_striptease.scene / n1103 / 0` | [Right] (`right`) | No option-level predicate stored | 0:0 → 1104:1:0; 0:0 → 1109:0:0 |
| `sq031_01c_smack_striptease.scene / n1104 / 0` | [Left] (`left`) | No option-level predicate stored | 0:0 → 1103:1:0; 0:0 → 1107:0:0 |
| `sq031_01c_smack_striptease.scene / n1134 / 0` | So're you guys. Best get back to work. (`get to work`) | No option-level predicate stored | 0:0 → 1135:0:0 |
| `sq031_01c_smack_striptease.scene / n1134 / 1` | [Punch] Fuck, how I missed this. (`i missed this`) | No option-level predicate stored | 0:1 → 1138:0:0 |
| `sq031_01d_smack_rogue.scene / n724 / 0` | Did we...? You know… (`did we`) | No option-level predicate stored | 0:0 → 725:0:0 |
| `sq031_01d_smack_rogue.scene / n724 / 1` | You don't seem surprised. (`surprised`) | No option-level predicate stored | 0:1 → 727:0:0 |
| `sq031_01d_smack_rogue.scene / n724 / 2` | Feel like shit. (`shit`) | No option-level predicate stored | 0:2 → 729:0:0 |
| `sq031_01d_smack_rogue.scene / n734 / 0` | He tell you about Smasher? (`smasher`) | No option-level predicate stored | 0:0 → 740:0:0 |
| `sq031_01d_smack_rogue.scene / n734 / 1` | Feels weird, this. (`weird`) | No option-level predicate stored | 0:1 → 742:0:0 |
| `sq031_01d_smack_rogue.scene / n744 / 0` | Need some help? (`help`) | No option-level predicate stored | 0:0 → 750:0:0 |
| `sq031_01d_smack_rogue.scene / n744 / 1` | Know what Smasher's been doing all this time? (`before`) | No option-level predicate stored | 0:1 → 747:0:0 |
| `sq031_01d_smack_rogue.scene / n760 / 0` | You tricked me. Were just supposed to talk to Rogue. (`cheated`) | No option-level predicate stored | 0:0 → 767:0:0 |
| `sq031_01d_smack_rogue.scene / n760 / 1` | You oughta be the one puking here. (`it should be you`) | No option-level predicate stored | 0:1 → 765:0:0 |
| `sq031_01d_smack_rogue.scene / n760 / 2` | Fuck, never again. (`all yous fault`) | No option-level predicate stored | 0:2 → 761:0:0 |
| `sq031_01d_smack_rogue.scene / n776 / 0` | Actually, for a moment there I thought... (`for a while`) | No option-level predicate stored | 0:0 → 781:0:0 |
| `sq031_01d_smack_rogue.scene / n776 / 1` | I am happy. Positively glowing. (`im happy`) | No option-level predicate stored | 0:1 → 783:0:0 |
| `sq031_01d_smack_rogue.scene / n779 / 0` | "Ebunike." That's real? (`ebunike`) | No option-level predicate stored | 0:0 → 785:0:0 |
| `sq031_01d_smack_rogue.scene / n779 / 1` | Coulda done it myself. (`myself`) | No option-level predicate stored | 0:1 → 787:0:0 |
| `sq031_01d_smack_rogue.scene / n850 / 0` | [Stand] (`stand up`) | No option-level predicate stored | 0:0 → 916:0:1; 0:0 → 1006:1:0 |
| `sq031_01d_smack_rogue.scene / n949 / 0` | [Stand] (`stand up`) | No option-level predicate stored | 0:0 → 677:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers/conditions in context |
| --- | --- | --- |
| `CP77-55456` | sq031_cinematic_bugfixes.questphase / h78 / 3 | sq031_cinematic_bugfixes.questphase / h78 / 4 |
| `CP77-57328` | sq031_cinematic_bugfixes.questphase / h143 / 4 | No reader in selected context |
| `CP77-57328_executed` | sq031_cinematic_bugfixes.questphase / h143 / 7 | No reader in selected context |
| `CP77-60396` | sq031_cinematic_bugfixes.questphase / h212 / 3 | sq031_cinematic_bugfixes.questphase / h212 / 4 |
| `CYB-12345` | sq031_cinematic_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-644298` | sq031_cinematic_bugfixes.questphase / h37 / 2 | No reader in selected context |
| `air_traffic_off` | sq031_00_johnny.scene / scene / 463; sq031_01d_smack_rogue.scene / scene / 1136; sq031_01d_smack_rogue.scene / scene / 1145 | No reader in selected context |
| `censorship_homosexuality` | Producer outside selected context | sq031_01c_smack_striptease.scene / scene / 2343; sq031_01c_smack_striptease.scene / scene / 2354 |
| `censorship_oversexualized` | Producer outside selected context | sq031_01c_smack_striptease.scene / scene / 2363; sq031_01c_smack_striptease.scene / scene / 2654 |
| `claire_default_on` | sq031_01a_smack_afterlife.scene / scene / 1431; sq031_afterlife.questphase / h0 / 193; sq031_afterlife.questphase / h0 / 204 | No reader in selected context |
| `emphaty_dancefloor_on` | sq031_01c_smack_striptease.scene / scene / 2471; sq031_01c_smack_striptease.scene / scene / 2474 | No reader in selected context |
| `johnny_off` | sq031_01c_smack_striptease.scene / scene / 2611 | No reader in selected context |
| `player_drunk` | sq031_01a_smack_afterlife.scene / scene / 1540 | No reader in selected context |
| `q115_av_sequence_done` | Producer outside selected context | sq031_cinematic_bugfixes.questphase / h212 / 8 |
| `rogue_default_on` | sq031_01d_smack_rogue.scene / scene / 893; sq031_01d_smack_rogue.scene / scene / 899; sq031_cinematic_bugfixes.questphase / h212 / 11 | No reader in selected context |
| `sq031_00_lets_start` | sq031_00_johnny.scene / scene / 524 | sq031_00_johnny.scene / scene / 528 |
| `sq031_01a_blueglass` | sq031_01a_smack_afterlife.scene / scene / 1192 | sq031_01a_smack_afterlife.scene / scene / 1199; sq031_01a_smack_afterlife.scene / scene / 1239; sq031_01a_smack_afterlife.scene / scene / 1245 |
| `sq031_01d_confuse` | sq031_01d_smack_rogue.scene / scene / 796 | No reader in selected context |
| `sq031_01d_sex_nope` | sq031_01d_smack_rogue.scene / scene / 737 | No reader in selected context |
| `sq031_afterlife_sequence_done` | sq031_afterlife.questphase / h0 / 224 | No reader in selected context |
| `sq031_claire_scene_end` | sq031_01a_smack_afterlife.scene / scene / 1031 | No reader in selected context |
| `sq031_cool_metal_fire_start` | sq031_00_johnny.scene / scene / 504 | sq031_00_johnny.scene / scene / 588; sq031_00_johnny.scene / scene / 611 |
| `sq031_done` | Producer outside selected context | sq031_cinematic_bugfixes.questphase / h78 / 6 |
| `sq031_goat_tattoo` | sq031_01b_smack_tatto.scene / scene / 273 | No reader in selected context |
| `sq031_kill_afterlife_phase` | Producer outside selected context | sq031_afterlife.questphase / h0 / 210 |
| `sq031_kill_ebunike` | Producer outside selected context | sq031_cinematic_bugfixes.questphase / h212 / 5 |
| `sq031_property_tattoo` | sq031_01b_smack_tatto.scene / scene / 274 | No reader in selected context |
| `sq031_rogue_met_johnny` | sq031_01d_smack_rogue.scene / scene / 806 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | sq031_cinematic_bugfixes.questphase / h0 / 23 |
| `wat_nid_ripperdoc_01_default_on` | sq031_01b_smack_tatto.scene / scene / 411; sq031_01c_smack_striptease.scene / scene / 956 | No reader in selected context |

## Exact gates, joins and cancellation

<details><summary>86 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sq031_cinematic_bugfixes.questphase / h0 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 24:Out → 23:In |
| `sq031_cinematic_bugfixes.questphase / h37 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq031_smack_my_bitch_up","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded"}}}` | 3:False → 1:In; 2:Out → 3:In; 3:True → 4:In |
| `sq031_cinematic_bugfixes.questphase / h78 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-55456","value":1,"comparisonType":"Less"}}}` | 0:Out → 4:In; 4:True → 5:In |
| `sq031_cinematic_bugfixes.questphase / h78 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq031_rogue/02_afterlife/00_wait_for_rogue_call","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq031_rogue/02_afterlife/00_wait_for_rogue_call","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}]}}` | 4:True → 5:In; 5:True → 7:In1; 5:False → 6:In |
| `sq031_cinematic_bugfixes.questphase / h78 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq031_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 5:False → 6:In; 6:Out → 7:In2 |
| `sq031_cinematic_bugfixes.questphase / h143 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq031_rogue/malorian/08_remove_cloth","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 4:Out → 2:In; 2:True → 5:In; 2:False → 8:In2 |
| `sq031_cinematic_bugfixes.questphase / h143 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleGlobalName":"#sq031_porsche"}}}` | 2:True → 5:In; 5:Out → 6:In |
| `sq031_cinematic_bugfixes.questphase / h212 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-60396","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 4:In; 4:False → 3:In; 4:True → 15:In1 |
| `sq031_cinematic_bugfixes.questphase / h212 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq031_kill_ebunike","value":1,"comparisonType":"GreaterOrEqual"}}}` | 3:Out → 5:In; 5:True → 8:In; 5:False → 15:In1 |
| `sq031_cinematic_bugfixes.questphase / h212 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#rogue"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0},"comparisonType":"LessOrEqual"}}}` | 8:False → 6:In; 6:True → 7:In; 6:False → 14:In1 |
| `sq031_cinematic_bugfixes.questphase / h212 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_av_sequence_done","value":1,"comparisonType":"GreaterOrEqual"}}}` | 5:True → 8:In; 8:False → 6:In; 8:True → 13:In1 |
| `sq031_afterlife.questphase / h0 / 210` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq031_kill_afterlife_phase"}}}` | 122:sq031_00_johnny_out → 210:In; 210:Out → 211:In |
| `sq031_afterlife.questphase / h0 / 215` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#emmerick"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":8.0},"comparisonType":"LessOrEqual"}}}` | 215:Out → 172:In; 204:Out → 215:In |
| `sq031_afterlife.questphase / h0 / 203` | `questLogicalAndNodeDefinition` `{}` | 143:sq031_01_afterlife_bartender_out → 203:In1; 223:Out → 203:In2; 203:Out1 → 224:In |
| `sq031_brawl.questphase / h0 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq031_brawlers","names":["sq031_brawlers_2"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 58:Out1 → 15:In; 15:Out → 35:Succeeded |
| `sq031_brawl.questphase / h0 / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 58:Out1 → 46:In; 46:Out → 51:sq031_01a_brawler_taunt_in |
| `sq031_motel.questphase / h0 / 285` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\side_quests\\sq031\\scenes\\sq031_01d_smack_rogue.scene","Flags":"Soft"},"sectionName":"sq031_01d_c","type":"Entered"}}}` | 0:Out → 285:In; 285:Out → 286:In |
| `sq031_motel.questphase / h0 / 286` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 286:Out → 284:In1; 285:Out → 286:In |
| `sq031_motel.questphase / h0 / 288` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq031_tr_rogue_left_motel_room"}}` | 268:Out → 288:In; 288:Out → 271:sq031_01_motel_fluff_1_in |
| `sq031_motel.questphase / h0 / 289` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq031_tr_motel_exit_johnny"}}` | 268:Out → 289:In; 289:Out → 290:sq031_01_motel_fluff_2_in |
| `sq031_00_johnny.scene / scene / 369` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#johnny","names":["johnny"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 369:0:0 → 528:0:1; 369:0:0 → 563:0:1; 370:0:0 → 369:0:1 |
| `sq031_00_johnny.scene / scene / 391` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#johnny","names":["johnny"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":12.0}}}}` | 391:0:0 → 92:1:0; 391:0:0 → 546:0:0; 393:0:0 → 391:0:1; 400:1:0 → 391:0:0; 400:1:0 → 391:1026:0; 538:0:0 → 391:0:1 |
| `sq031_00_johnny.scene / scene / 393` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#johnny","names":["johnny"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 393:0:0 → 391:0:1; 393:0:1 → 370:0:1; 395:0:0 → 393:0:1 |
| `sq031_00_johnny.scene / scene / 395` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq031_tr_afterlife_johnny_met"}}` | 395:0:0 → 393:0:1; 400:1:0 → 395:0:0; 400:1:0 → 395:1026:0; 408:0:0 → 395:0:1; 559:0:0 → 395:0:1 |
| `sq031_00_johnny.scene / scene / 413` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#emmerick","names":["emmerick"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":4.0},"comparisonType":"LessOrEqual"}}}` | 1:0:0 → 413:0:1; 413:0:0 → 312:0:1 |
| `sq031_00_johnny.scene / scene / 451` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq031_tr_afterlife_johnny_met"}}` | 1:0:0 → 451:0:1; 451:0:0 → 370:0:1; 451:0:0 → 481:0:0 |
| `sq031_00_johnny.scene / scene / 472` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 472:0:0 → 376:0:0; 476:0:0 → 472:0:1 |
| `sq031_00_johnny.scene / scene / 528` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq031_00_lets_start","value":1,"comparisonType":"GreaterOrEqual"}}}` | 369:0:0 → 528:0:1; 528:0:0 → 531:0:0; 528:0:1 → 91:0:0 |
| `sq031_00_johnny.scene / scene / 554` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#afterlife_interior_area_inside"}}` | 554:0:0 → 557:0:1; 554:0:1 → 407:0:2; 588:0:1 → 554:0:1 |
| `sq031_00_johnny.scene / scene / 563` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq031_rogue/afterlife/01_go_to_afterlife","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 369:0:0 → 563:0:1; 563:0:0 → 9:0:3; 563:0:1 → 566:0:1 |
| `sq031_00_johnny.scene / scene / 566` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq031_rogue/afterlife/02_talk_to_johnny","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 9:0:0 → 566:0:1; 563:0:1 → 566:0:1; 566:0:0 → 574:0:1; 566:0:1 → 8:0:1 |
| `sq031_00_johnny.scene / scene / 581` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#afterlife_interior_area_inside"}}` | 400:1:0 → 581:0:0; 400:1:0 → 581:1026:0; 557:0:0 → 581:0:1; 581:0:0 → 611:0:1 |
| `sq031_00_johnny.scene / scene / 588` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq031_cool_metal_fire_start","value":1,"comparisonType":"GreaterOrEqual"}}}` | 405:0:0 → 588:0:1; 588:0:1 → 554:0:1 |
| `sq031_00_johnny.scene / scene / 590` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/side_quest/sq031_rogue/afterlife/02_talk_to_johnny","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 590:0:0 → 584:0:2; 611:0:1 → 590:0:1 |
| `sq031_00_johnny.scene / scene / 611` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq031_cool_metal_fire_start","value":1,"comparisonType":"GreaterOrEqual"}}}` | 581:0:0 → 611:0:1; 611:0:1 → 590:0:1 |
| `sq031_00_johnny.scene / scene / 616` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#afterlife_tr_inside_area"}}` | 400:1:0 → 616:0:0; 400:1:0 → 616:1026:0; 481:0:0 → 616:0:1; 616:0:0 → 483:0:0; 616:0:1 → 619:0:1 |
| `sq031_00_johnny.scene / scene / 622` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#sq031_tr_afterlife_johnny_met"}}` | 400:1:0 → 622:0:0; 400:1:0 → 622:1026:0; 619:0:0 → 622:0:1; 622:0:0 → 481:0:0 |
| `sq031_01a_smack_afterlife.scene / scene / 1199` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq031_01a_blueglass","value":1,"comparisonType":"Equal"}}}` | 658:2:0 → 1199:0:1; 1199:0:0 → 1197:0:0; 1199:0:1 → 1198:0:0 |
| `sq031_01a_smack_afterlife.scene / scene / 1239` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq031_01a_blueglass","value":1,"comparisonType":"Equal"}}}` | 1069:0:0 → 1239:0:1; 1239:0:0 → 1068:0:0; 1239:0:1 → 1241:0:0 |
| `sq031_01a_smack_afterlife.scene / scene / 1245` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq031_01a_blueglass","value":1,"comparisonType":"Equal"}}}` | 1076:0:0 → 1245:0:1; 1245:0:0 → 1083:0:0; 1245:0:1 → 1248:0:0 |
| `sq031_01b_smack_tatto.scene / scene / 346` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#wat_nid_ripperdoc_01","names":["wat_nid_ripperdoc_01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 346:0:0 → 411:0:1; 706:0:0 → 346:0:1 |
| `sq031_01b_smack_tatto.scene / scene / 365` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":7}}}` | 365:0:0 → 366:0:0; 370:1:0 → 365:0:0; 648:0:0 → 365:0:1 |
| `sq031_01b_smack_tatto.scene / scene / 372` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 370:1:0 → 372:0:0; 371:0:0 → 372:0:1; 372:0:0 → 375:0:0 |
| `sq031_01b_smack_tatto.scene / scene / 373` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 370:1:0 → 373:0:0; 371:0:1 → 373:0:1; 373:0:0 → 375:0:0 |
| `sq031_01b_smack_tatto.scene / scene / 374` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":7}}}` | 370:1:0 → 374:0:0; 371:0:2 → 374:0:1; 374:0:0 → 375:0:0 |
| `sq031_01b_smack_tatto.scene / scene / 680` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#player"},"itemID":"80148848893","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 678:0:0 → 680:0:1; 680:0:0 → 683:0:1 |
| `sq031_01b_smack_tatto.scene / scene / 685` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#player"},"itemID":"94842881877","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 679:0:0 → 685:0:1; 685:0:0 → 686:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 491` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#sq031_streapper_car"},"childRef":{"$type":"gameEntityReference","reference":"#sq031_streapper","names":["sq031_streapper"]}}}}` | 491:0:0 → 3210:0:1; 1605:0:0 → 491:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 562` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#sq031_streapper_car"},"childIsPlayer":true,"condition":"OnUnmount"}}}` | 562:0:0 → 2377:0:1; 562:0:0 → 3216:0:1; 2662:0:0 → 562:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 563` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#sq031_streapper_car"},"childRef":{"$type":"gameEntityReference","reference":"#sq031_streapper","names":["sq031_streapper"]},"condition":"OnUnmount"}}}` | 563:0:0 → 571:0:0; 2662:0:0 → 563:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 925` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq031_streapper","names":["sq031_streapper"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 595:0:0 → 925:0:1; 925:0:0 → 313:0:1; 925:0:0 → 2428:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 1216` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq031_simone"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 1214:0:0 → 1216:0:1; 1216:0:0 → 2430:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 1221` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq031_drunk_guy"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 1220:0:0 → 1221:0:1; 1221:0:0 → 2597:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 1227` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq031_drunk_girl"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 1226:0:0 → 1227:0:1; 1227:0:0 → 2598:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 1255` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq031_cybereyes_guy"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 1254:0:0 → 1255:0:1; 1255:0:0 → 2446:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 1264` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq031_back_woman"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 1263:0:0 → 1264:0:1; 1264:0:0 → 2599:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 2340` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterGender_CondtionType","isPlayer":true}}}` | 1901:0:0 → 2340:0:1; 2340:0:0 → 2343:0:1; 2340:0:1 → 1645:0:0 |
| `sq031_01c_smack_striptease.scene / scene / 2343` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_homosexuality"}}}` | 2340:0:0 → 2343:0:1; 2343:0:0 → 2346:0:0; 2343:0:1 → 1645:0:0 |
| `sq031_01c_smack_striptease.scene / scene / 2353` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterGender_CondtionType","isPlayer":true}}}` | 2353:0:0 → 2354:0:1; 2353:0:1 → 286:0:0; 2353:0:1 → 840:0:0; 3054:0:0 → 2353:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 2354` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_homosexuality"}}}` | 2353:0:0 → 2354:0:1; 2354:0:0 → 2358:0:0; 2354:0:1 → 286:0:0 |
| `sq031_01c_smack_striptease.scene / scene / 2363` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_oversexualized"}}}` | 2207:0:0 → 2363:0:1; 2363:0:0 → 3399:0:0; 2363:0:1 → 858:0:0 |
| `sq031_01c_smack_striptease.scene / scene / 2513` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#dtn_03_com","names":["#dtn_03_ws_barman"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 317:0:0 → 2513:0:1; 2513:0:0 → 3025:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 2551` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq031_streapper","names":["sq031_streapper"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 370:0:0 → 2551:0:1; 2551:0:0 → 2677:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 2654` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_oversexualized"}}}` | 2071:0:0 → 2654:0:1; 2654:0:0 → 561:0:1; 2654:0:1 → 2662:0:0 |
| `sq031_01c_smack_striptease.scene / scene / 2964` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterBodyType_CondtionType","isPlayer":true}}}` | 1128:0:0 → 2964:0:1; 2964:0:0 → 2965:0:1; 2964:0:1 → 2966:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 2967` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq031_01c_smack_striptease_player_tpp_female"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 2965:0:0 → 2967:0:1; 2967:0:0 → 2978:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 2968` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sq031_01c_smack_striptease_player_tpp_male"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 2966:0:0 → 2968:0:1; 2968:0:0 → 2978:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 3008` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq031_brawlers","names":["sq031_brawlers_1"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 1910:0:0 → 3008:0:1; 3008:0:0 → 3011:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 3011` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sq031_brawlers","names":["sq031_brawlers_2"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 3008:0:0 → 3011:0:1; 3011:0:0 → 3007:0:1; 3011:0:0 → 3014:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 3178` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 892:0:0 → 3178:0:1; 3178:0:0 → 3181:0:0 |
| `sq031_01c_smack_striptease.scene / scene / 3186` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 1825:0:0 → 3186:0:1; 3186:0:0 → 3188:0:0 |
| `sq031_01c_smack_striptease.scene / scene / 3205` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#sq031_streapper_car"},"childRef":{"$type":"gameEntityReference","reference":"#sq031_streapper","names":["sq031_streapper"]},"childIsPlayer":true}}}` | 2592:0:0 → 3205:0:1; 3205:0:0 → 3210:0:0 |
| `sq031_01c_smack_striptease.scene / scene / 3216` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 562:0:0 → 3216:0:1; 3216:0:0 → 3218:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 3316` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 3311:0:0 → 3316:0:1; 3316:0:0 → 3301:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 3332` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 3330:0:0 → 3332:0:1; 3332:0:0 → 3328:0:1 |
| `sq031_01c_smack_striptease.scene / scene / 3341` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 3339:0:0 → 3341:0:1; 3341:0:0 → 3337:0:1 |
| `sq031_01d_smack_rogue.scene / scene / 375` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#johnny","names":["johnny"]},"onScreenTest":true,"angleTolerance":2.0,"inverted":true}}}` | 375:0:0 → 438:0:1; 790:0:0 → 375:0:1 |
| `sq031_01d_smack_rogue.scene / scene / 403` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#rogue","names":["rogue"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"LessOrEqual"}}}}` | 399:0:0 → 403:0:1; 403:0:0 → 1167:0:1 |
| `sq031_01d_smack_rogue.scene / scene / 693` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#johnny","names":["johnny"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"LessOrEqual"}}}}` | 691:0:0 → 693:0:1; 693:0:0 → 706:0:0 |
| `sq031_01d_smack_rogue.scene / scene / 704` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#johnny","names":["johnny"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"LessOrEqual"}}}}` | 702:0:0 → 704:0:1; 704:0:0 → 695:0:0 |
| `sq031_01d_smack_rogue.scene / scene / 717` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 706:0:0 → 717:0:1; 717:0:0 → 837:0:1 |
| `sq031_01d_smack_rogue.scene / scene / 721` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 695:0:0 → 721:0:1; 721:0:0 → 840:0:1 |
| `sq031_01d_smack_rogue.scene / scene / 837` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#johnny","names":["johnny"]},"inverted":true}}}` | 717:0:0 → 837:0:1; 837:0:0 → 715:0:1 |
| `sq031_01d_smack_rogue.scene / scene / 840` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#johnny","names":["johnny"]},"inverted":true}}}` | 721:0:0 → 840:0:1; 840:0:0 → 720:0:1 |
| `sq031_01d_smack_rogue.scene / scene / 4437` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 910:0:0 → 4437:0:1; 4437:0:0 → 4442:0:1 |
| `sq031_01d_smack_rogue.scene / scene / 4440` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":600}}}` | 4440:0:0 → 394:0:1; 4442:0:0 → 4440:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sq031_00_johnny.scene / scene / 369; sq031_00_johnny.scene / scene / 393; sq031_01b_smack_tatto.scene / scene / 346; sq031_01c_smack_striptease.scene / scene / 1216; +14 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | sq031_01d_smack_rogue.scene / scene / 530 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `choice_gate` | sq031_00_johnny.scene / scene / 92; sq031_01a_smack_afterlife.scene / scene / 1069; sq031_01a_smack_afterlife.scene / scene / 1073; sq031_01a_smack_afterlife.scene / scene / 1076; +17 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | sq031_brawl.questphase / h0 / 50 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | sq031_01b_smack_tatto.scene / scene / 317; sq031_01b_smack_tatto.scene / scene / 319; sq031_01c_smack_striptease.scene / scene / 2184; sq031_01c_smack_striptease.scene / scene / 317; +7 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | sq031_00_johnny.scene / scene / 528; sq031_00_johnny.scene / scene / 588; sq031_00_johnny.scene / scene / 611; sq031_01a_smack_afterlife.scene / scene / 1199; +13 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sq031_00_johnny.scene / scene / 331; sq031_motel.questphase / h0 / 292 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `device_action` | sq031_00_johnny.scene / scene / 312; sq031_00_johnny.scene / scene / 327; sq031_01c_smack_striptease.scene / scene / 2558; sq031_01c_smack_striptease.scene / scene / 2624; +7 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `item_state` | sq031_01b_smack_tatto.scene / scene / 680; sq031_01b_smack_tatto.scene / scene / 685 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `mount_state` | sq031_01c_smack_striptease.scene / scene / 3205; sq031_01c_smack_striptease.scene / scene / 491; sq031_01c_smack_striptease.scene / scene / 562; sq031_01c_smack_striptease.scene / scene / 563 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | sq031_afterlife.questphase / h0 / 203 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sq031_00_johnny.scene / scene / 463; sq031_00_johnny.scene / scene / 504; sq031_00_johnny.scene / scene / 524; sq031_01a_smack_afterlife.scene / scene / 1031; +27 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | sq031_00_johnny.scene / scene / 472; sq031_01b_smack_tatto.scene / scene / 365; sq031_01b_smack_tatto.scene / scene / 372; sq031_01b_smack_tatto.scene / scene / 373; +13 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | sq031_afterlife.questphase / h0 / 191; sq031_motel.questphase / h0 / 274 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sq031_afterlife.questphase / h0 / 122; sq031_afterlife.questphase / h0 / 143; sq031_brawl.questphase / h0 / 51; sq031_motel.questphase / h0 / 256; +2 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `target_resolution` | sq031_brawl.questphase / h0 / 15 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | sq031_01c_smack_striptease.scene / scene / 2592; sq031_01c_smack_striptease.scene / scene / 560; sq031_01c_smack_striptease.scene / scene / 561; sq031_cinematic_bugfixes.questphase / h143 / 6 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | sq031_00_johnny.scene / scene / 321; sq031_00_johnny.scene / scene / 322; sq031_00_johnny.scene / scene / 323; sq031_00_johnny.scene / scene / 341; +136 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sq031_01b_smack_tatto.scene / scene / 726; sq031_01c_smack_striptease.scene / scene / 3256; sq031_01c_smack_striptease.scene / scene / 3258; sq031_01c_smack_striptease.scene / scene / 3267; +1 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\sidequests\sq031\sq031_cinematic_bugfixes.questphase` | repair; journal anchor | `base-sq031` |
| `base\quest\side_quests\sq031\phases\sq031_afterlife.questphase` | content candidate; journal anchor | `base-sq031` |
| `base\quest\side_quests\sq031\phases\sq031_brawl.questphase` | content candidate; journal anchor | `base-sq031` |
| `base\quest\side_quests\sq031\phases\sq031_motel.questphase` | content candidate; journal anchor | `base-sq031` |
| `base\quest\side_quests\sq031\scenes\sq031_00_johnny.scene` | content candidate; forward dependency | `base-sq031` |
| `base\quest\side_quests\sq031\scenes\sq031_01a_smack_afterlife.scene` | content candidate; forward dependency | `base-sq031` |
| `base\quest\side_quests\sq031\scenes\sq031_01b_smack_tatto.scene` | content candidate; journal anchor | `base-sq031` |
| `base\quest\side_quests\sq031\scenes\sq031_01c_smack_striptease.scene` | content candidate; journal anchor | `base-sq031` |
| `base\quest\side_quests\sq031\scenes\sq031_01d_smack_rogue.scene` | content candidate; journal anchor | `base-sq031` |

Evidence shards for this dossier (including parent context): [base-shared](../../../../../reference/quests/deep-dives/catalogue/evidence/base-shared.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/catalogue/evidence/base-sq031.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../expanded-blocks.md). No installed playtest is claimed.
