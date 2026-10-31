# Path of Glory

Journal: `quests/main_quest/epilogues/q203_legend` · `MainQuest` · hash `3248564736`.

**Coverage: journal-linked.** 106 exact journal-linked nodes in 15 resources; 16 resources in the inspected dependency context.

Resource roles in that context: 15 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Enter the Afterlife. (Primary) | `quests/main_quest/epilogues/q203_legend/afterlife/enter_afterlife` |
| Meet with the client. (Primary) | `quests/main_quest/epilogues/q203_legend/afterlife/meet_contact` |
| Sit. (Primary) | `quests/main_quest/epilogues/q203_legend/afterlife/sit_with_blue_eye` |
| Talk to Mr. Blue Eyes. (Primary) | `quests/main_quest/epilogues/q203_legend/afterlife/talk_blue_eyes` |
| Talk to Claire. (Optional) | `quests/main_quest/epilogues/q203_legend/afterlife/drink` |
| Talk to Emmerick. (Primary) | `quests/main_quest/epilogues/q203_legend/afterlife/talk_emmerick` |
| Turn on autopilot. (Primary) | `quests/main_quest/epilogues/q203_legend/cosmos/activate_autopilot` |
| Decompress the airlock. (Primary) | `quests/main_quest/epilogues/q203_legend/cosmos/depressurize` |
| Enter the airlock. (Primary) | `quests/main_quest/epilogues/q203_legend/cosmos/enter_airlock` |
| Exit the airlock and soar into the stars. (Primary) | `quests/main_quest/epilogues/q203_legend/cosmos/exit_airlock` |
| Get armed. (Primary) | `quests/main_quest/epilogues/q203_legend/cosmos/get_guns` |
| Put on the helmet. (Primary) | `quests/main_quest/epilogues/q203_legend/cosmos/get_helmet` |
| Leave the cockpit. (Primary) | `quests/main_quest/epilogues/q203_legend/cosmos/leave_cabin` |
| Listen to the client. (Primary) | `quests/main_quest/epilogues/q203_legend/cosmos/listen_to_briefing` |
| Wait for the airlock decompression. (Primary) | `quests/main_quest/epilogues/q203_legend/cosmos/wait_for_depressurization` |
| Walk with Mr. Blue Eyes. (Primary) | `quests/main_quest/epilogues/q203_legend/cosmos/walk_with_blueeyes` |
| Enter the AV. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/enter_delemain` |
| Take your jacket. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/get_dressed` |
| Get a gun. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/get_guns` |
| Get a melee weapon. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/get_katana` |
|  (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` |
| Join River on the balcony. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/join_river_balcony` |
| Join River in the kitchen. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/join_river_kitchen` |
| Check your calendar. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_ai` |
| Talk to Judy. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_judy` |
| Talk to Kerry. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_kerry` |
| Talk to Panam. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_panam` |
| Talk to River. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_sobchak` |
| Take the coffee. (Optional) | `quests/main_quest/epilogues/q203_legend/penthouse/grab_coffee` |
| Go to the Afterlife. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/travel_to_afterlife` |
| Wait for the AV. (Primary) | `quests/main_quest/epilogues/q203_legend/penthouse/wait_for_delamain` |
| Get dressed. (Optional) | `quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mws_wat_02.questphase / h229 / 13` (PauseCondition) | `quests/main_quest/epilogues/q203_legend/penthouse/enter_delemain` | 5:Out → 13:In; 13:Out → 10:In |
| `q203_quest_bugfixes.questphase / h28 / 4` (Condition) | `quests/main_quest/epilogues/q203_legend` | 0:Out → 4:In; 4:True → 2:In; 4:False → 6:In |
| `q203_quest_bugfixes.questphase / h96 / 4` (Condition) | `quests/main_quest/epilogues/q203_legend/cosmos/activate_autopilot`; `quests/main_quest/epilogues/q203_legend` | 0:Out → 4:In; 4:True → 13:In; 4:False → 14:In2 |
| `q203_afterlife.questphase / h0 / 156` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/meet_contact` | 180:Out → 156:Active |
| `q203_afterlife.questphase / h0 / 157` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/drink` | 153:q203_05_claire_drink_out → 157:Succeeded |
| `q203_afterlife.questphase / h0 / 180` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/enter_afterlife` | 149:Out → 180:Succeeded; 180:Out → 156:Active |
| `q203_afterlife.questphase / h0 / 181` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/enter_afterlife` | 161:Out → 181:Active |
| `q203_afterlife.questphase / h351 / 3` (MappinManager) | `quests/main_quest/epilogues/q203_legend/afterlife/enter_afterlife/mappin_elevator` | 2:Out → 3:Inactive; 3:Out → 4:Active |
| `q203_afterlife.questphase / h351 / 4` (MappinManager) | `quests/main_quest/epilogues/q203_legend/afterlife/enter_afterlife/mappin_elevator_panel` | 3:Out → 4:Active; 4:Out → 12:In |
| `q203_afterlife.questphase / h351 / 7` (MappinManager) | `quests/main_quest/epilogues/q203_legend/afterlife/enter_afterlife/mappin_elevator_panel` | 12:Out → 7:Inactive; 7:Out → 8:Active |
| `q203_afterlife.questphase / h351 / 8` (MappinManager) | `quests/main_quest/epilogues/q203_legend/afterlife/enter_afterlife/mappin_elevator_door_bottom` | 7:Out → 8:Active; 8:Out → 9:In |
| `q203_afterlife.questphase / h351 / 10` (MappinManager) | `quests/main_quest/epilogues/q203_legend/afterlife/enter_afterlife/mappin_elevator_door_bottom` | 9:Out → 10:Inactive; 10:Out → 11:Active |
| `q203_afterlife.questphase / h351 / 11` (MappinManager) | `quests/main_quest/epilogues/q203_legend/afterlife/enter_afterlife/mappin_door` | 10:Out → 11:Active |
| `q203_av_ride.questphase / h0 / 21` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/enter_afterlife` | 21:Out → 20:In; 22:Out → 21:Active |
| `q203_av_ride.questphase / h0 / 22` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/travel_to_afterlife` | 22:Out → 21:Active; 26:Out → 22:Succeeded |
| `q203_cosmos.questphase / h0 / 22` (Journal) | `quests/main_quest/epilogues/q203_legend` | 67:Out → 22:Succeeded; 22:Out → 60:In |
| `q203_cosmos.questphase / h0 / 65` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/activate_autopilot` | 70:Out1 → 65:Active |
| `q203_cosmos.questphase / h115 / 2` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/talk_rogue` | 0:Out → 2:Succeeded; 2:Out → 3:Succeeded |
| `q203_cosmos.questphase / h115 / 3` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/afterlife` | 2:Out → 3:Succeeded; 3:Out → 10:In |
| `q203_delamain.questphase / h0 / 33` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/wait_for_delamain` | 30:Out1 → 33:Succeeded |
| `q203_delamain.questphase / h0 / 49` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/enter_delemain` | 55:Out → 49:Active; 49:Out → 77:In |
| `q203_delamain.questphase / h0 / 55` (PauseCondition) | `quests/main_quest/epilogues/q203_legend/penthouse/get_dressed` | 55:Out → 49:Active; 80:Out1 → 55:In |
| `q203_delamain.questphase / h0 / 76` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/wait_for_delamain` | 68:True → 76:Active; 76:Out → 75:In1; 81:Out → 76:Active |
| `q203_penthouse.questphase / h7 / 28` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_dressed` | 115:False → 28:Active; 28:Out → 107:In |
| `q203_penthouse.questphase / h7 / 29` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_dressed` | 146:Out → 29:Succeeded; 29:Out → 78:In |
| `q203_penthouse.questphase / h7 / 135` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_dressed` | 115:True → 135:Active; 135:Out → 134:In |
| `q203_penthouse.questphase / h7 / 136` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_dressed` | 136:Out → 78:In; 134:Out → 136:Succeeded |
| `q203_penthouse.questphase / h620 / 34` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 0:Out → 34:Active; 34:Out → 32:In |
| `q203_penthouse.questphase / h719 / 32` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 0:Out → 32:Active; 32:Out → 26:In |
| `q203_penthouse.questphase / h828 / 22` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 0:Out → 22:Active; 22:Out → 13:In |
| `q203_penthouse.questphase / h941 / 23` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 0:Out → 23:Active; 23:Out → 13:In |
| `q203_penthouse.questphase / h1057 / 15` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 0:Out → 15:Active; 15:Out → 12:In |
| `q203_penthouse.questphase / h1153 / 5` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_sobchak` | 3:Out → 5:Succeeded |
| `q203_penthouse.questphase / h1718 / 3` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes` | 6:Out → 3:Succeeded |
| `q203_penthouse.questphase / h1718 / 12` (PauseCondition) | `quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes` | 14:Out → 12:In; 12:Out → 16:In |
| `q203_02_shower.scene / scene / 302` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 302:0:0 → 494:0:1; 352:0:0 → 302:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02_shower.scene / scene / 305` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 305:0:0 → 492:0:1; 387:0:0 → 305:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02_shower.scene / scene / 338` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_ai` | 441:0:0 → 338:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02_shower.scene / scene / 340` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_ai` | 337:0:0 → 340:0:3; 340:0:0 → 150:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02_shower.scene / scene / 492` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes` | 305:0:0 → 492:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02_shower.scene / scene / 494` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower/description` | 302:0:0 → 494:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `q203_02b_kerry.scene / scene / 163` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_kerry` | 210:0:0 → 163:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02b_kerry.scene / scene / 209` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 209:0:0 → 499:0:1; 262:0:0 → 209:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02b_kerry.scene / scene / 210` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 210:0:0 → 163:0:1; 210:0:0 → 497:0:1; 300:0:0 → 210:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02b_kerry.scene / scene / 495` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_kerry` | 495:0:0 → 665:0:1; 566:0:0 → 495:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02b_kerry.scene / scene / 497` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes` | 210:0:0 → 497:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02b_kerry.scene / scene / 499` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower/description` | 209:0:0 → 499:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `q203_02c_judy.scene / scene / 107` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_judy` | 803:0:0 → 107:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02c_judy.scene / scene / 257` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_judy` | 257:0:0 → 249:0:1; 412:2:1 → 257:0:3; 416:0:0 → 257:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02c_judy.scene / scene / 372` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 372:0:0 → 541:0:0; 372:0:0 → 810:0:1; 517:0:0 → 372:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02c_judy.scene / scene / 803` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 497:3:0 → 803:0:3; 803:0:0 → 107:0:1; 803:0:0 → 808:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02c_judy.scene / scene / 808` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes` | 803:0:0 → 808:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02c_judy.scene / scene / 810` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower/description` | 372:0:0 → 810:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `q203_02d_panam.scene / scene / 71` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 71:0:0 → 528:0:1; 221:0:0 → 71:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02d_panam.scene / scene / 73` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 73:0:0 → 84:0:1; 73:0:0 → 526:0:1; 288:0:0 → 73:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02d_panam.scene / scene / 84` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_panam` | 73:0:0 → 84:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02d_panam.scene / scene / 98` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_panam` | 98:0:0 → 735:0:1; 598:0:0 → 98:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02d_panam.scene / scene / 526` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes` | 73:0:0 → 526:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_02d_panam.scene / scene / 528` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower/description` | 71:0:0 → 528:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `q203_03_sobchak.scene / scene / 151` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/join_river_kitchen` | 151:0:0 → 256:0:1; 511:0:0 → 151:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_03_sobchak.scene / scene / 153` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/join_river_kitchen` | 87:2:0 → 153:0:3; 153:0:0 → 184:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_03_sobchak.scene / scene / 184` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_sobchak` | 153:0:0 → 184:0:1; 184:0:0 → 88:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_03_sobchak.scene / scene / 203` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/join_river_balcony` | 174:0:0 → 203:0:1; 203:0:0 → 909:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_03_sobchak.scene / scene / 208` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/join_river_balcony` | 208:0:0 → 911:0:1; 209:0:0 → 208:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_03_sobchak.scene / scene / 218` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_sobchak` | 218:0:0 → 668:0:1; 352:0:0 → 218:0:3; 582:0:0 → 218:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_03_sobchak.scene / scene / 428` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 428:0:0 → 432:0:0; 428:0:0 → 717:0:1; 475:0:0 → 428:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_03_sobchak.scene / scene / 668` (Condition) | `quests/main_quest/epilogues/q203_legend/penthouse/grab_coffee` | 218:0:0 → 668:0:1; 668:0:0 → 670:0:2; 668:0:1 → 703:0:0; input mappings: 0:0=CutDestination, 0:1=In |
| `q203_03_sobchak.scene / scene / 670` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/grab_coffee` | 668:0:0 → 670:0:2; 670:0:0 → 703:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_03_sobchak.scene / scene / 711` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower` | 511:0:0 → 711:0:3; 711:0:0 → 715:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_03_sobchak.scene / scene / 715` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes` | 711:0:0 → 715:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_03_sobchak.scene / scene / 717` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/get_shower/description` | 428:0:0 → 717:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `q203_03_sobchak.scene / scene / 909` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_sobchak` | 203:0:0 → 909:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_03_sobchak.scene / scene / 911` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/talk_sobchak` | 208:0:0 → 911:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_04_delamain.scene / scene / 178` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/enter_delemain` | 178:0:0 → 179:0:1; 671:0:0 → 178:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_04_delamain.scene / scene / 179` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/travel_to_afterlife` | 178:0:0 → 179:0:1; 179:0:0 → 1081:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_04_delamain.scene / scene / 208` (Condition) | `quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes` | 44:0:0 → 208:0:1; 208:0:0 → 210:0:4; input mappings: 0:0=CutDestination, 0:1=In |
| `q203_04_delamain.scene / scene / 210` (Journal) | `quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes` | 208:0:0 → 210:0:4; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_05_afterlife.scene / scene / 324` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/drink` | 324:0:0 → 228:0:0; 357:0:0 → 324:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_05_afterlife.scene / scene / 335` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/talk_blue_eyes` | 335:0:0 → 337:0:3; 555:0:0 → 335:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_05_afterlife.scene / scene / 337` (Journal) | `quests/main_quest/epilogues/q203_legend` | 335:0:0 → 337:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_05_afterlife.scene / scene / 376` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/drink` | 377:0:0 → 376:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_05_afterlife.scene / scene / 377` (PauseCondition) | `quests/main_quest/epilogues/q203_legend/afterlife/drink` | 369:0:0 → 377:0:1; 377:0:0 → 376:0:2; input mappings: 0:0=CutDestination, 0:1=In |
| `q203_05_afterlife.scene / scene / 380` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/sit_with_blue_eye` | 369:0:0 → 380:0:3; 380:0:0 → 382:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_05_afterlife.scene / scene / 382` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/talk_blue_eyes` | 380:0:0 → 382:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_05_afterlife.scene / scene / 386` (MappinManager) | `quests/main_quest/epilogues/q203_legend/afterlife/drink/drink` | 443:0:0 → 386:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `q203_05_afterlife.scene / scene / 391` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/drink` | 230:1:0 → 391:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_05_afterlife.scene / scene / 443` (MappinManager) | `quests/main_quest/epilogues/q203_legend/afterlife/drink/claire` | 397:2:0 → 443:0:2; 443:0:0 → 386:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `q203_05_afterlife.scene / scene / 533` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/sit_with_blue_eye` | 534:0:0 → 533:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_05_afterlife.scene / scene / 534` (Journal) | `quests/main_quest/epilogues/q203_legend/afterlife/meet_contact` | 484:0:0 → 534:0:3; 534:0:0 → 533:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 112` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/leave_cabin` | 57:2:2 → 112:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 115` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/listen_to_briefing` | 67:0:0 → 115:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 221` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/get_helmet` | 156:0:0 → 221:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 222` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/enter_airlock` | 161:0:0 → 222:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 229` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/get_guns` | 163:0:0 → 229:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 231` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/depressurize` | 174:0:0 → 231:0:3; 231:0:0 → 233:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 233` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/wait_for_depressurization` | 231:0:0 → 233:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 236` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/wait_for_depressurization` | 176:0:0 → 236:0:3; 236:0:0 → 239:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 239` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/exit_airlock` | 236:0:0 → 239:0:1; 239:0:0 → 118:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 241` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/exit_airlock` | 241:0:0 → 407:0:1; 410:0:0 → 241:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 258` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/activate_autopilot` | 218:0:0 → 258:0:3; 258:0:0 → 389:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 389` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/listen_to_briefing` | 258:0:0 → 389:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 539` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/leave_cabin` | 276:0:0 → 539:0:3; 539:0:0 → 540:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 540` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/get_helmet` | 539:0:0 → 540:0:1; 540:0:0 → 541:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 541` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/get_guns` | 540:0:0 → 541:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 557` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/enter_airlock` | 83:0:0 → 557:0:3; 292:0:0 → 557:0:3; 557:0:0 → 558:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `q203_06_cosmos.scene / scene / 558` (Journal) | `quests/main_quest/epilogues/q203_legend/cosmos/depressurize` | 557:0:0 → 558:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mws_wat_02.questphase / h20 / 15` | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene`; `#mws_sm_wat_02` | 30:False → 15:mws_wat_02_in |
| `mws_wat_02.questphase / h20 / 31` | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene`; `#mws_sm_wat_02` | 30:True → 31:mws_wat_02_iguana_cat_in |
| `mws_wat_02.questphase / h229 / 7` | `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene`; `#mws_sm_wat_02_q203_iguana` | 6:Out → 7:mws_wat_02_q203_in |
| `q203_afterlife.questphase / h0 / 135` | `base\quest\main_quests\epilogue\q203\scenes\q203_05_afterlife.scene`; `#q203_05_sm_afterlife` | 135:q203_05_mr_blueeyes_leaving_out → 1:In; 149:Out → 135:q203_05_afterlife_booth_in; 135:q203_05_mr_blueeyes_leaving_out → 203:In; 135:q203_05_mr_blueeyes_leaving_out → 215:In |
| `q203_afterlife.questphase / h0 / 153` | `base\quest\main_quests\epilogue\q203\scenes\q203_05_afterlife.scene`; `#q203_05_sm_afterlife` | 152:Out → 153:q203_05_claire_drink_in; 153:q203_05_claire_drink_out → 157:Succeeded |
| `q203_afterlife.questphase / h0 / 196` | `base\quest\main_quests\epilogue\q203\scenes\q203_05_afterlife.scene`; `#q203_05_sm_afterlife` | 206:True → 196:Weyland_Rogue; 198:True → 196:q203_05_weyland_IN |
| `q203_afterlife.questphase / h0 / 205` | `base\quest\main_quests\epilogue\q203\scenes\q203_05_afterlife.scene`; `#q203_05_sm_afterlife` | 204:True → 205:Rogue_start |
| `q203_afterlife.questphase / h0 / 207` | `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene`; `#q203_04_sm_delamain` | 209:Out → 207:q203_04_delemain_leaves_IN |
| `q203_av_ride.questphase / h0 / 4` | `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene`; `#q203_04_sm_delamain` | 0:Out → 4:q203_04_goodbye_to_nc_in; 4:q203_04_goodbye_to_nc_out → 39:In |
| `q203_cosmos.questphase / h0 / 10` | `base\quest\main_quests\epilogue\q203\scenes\q203_06_cosmos.scene`; `#q203_06_sm_cosmos` | 70:Out1 → 10:q203_06_cosmos_mr_blue_eyes_IN; 10:clean_up → 64:In1; 10:q203_06_cosmos_mr_blue_eyes_OUT → 63:In |
| `q203_cosmos.questphase / h0 / 73` | `base\quest\main_quests\epilogue\q203\scenes\q203_06_cosmos.scene`; `#q203_06_sm_cosmos` | 63:Out → 73:q203_06_helmet_IN; 73:q203_06_final_cutscene_OUT → 82:In |
| `q203_delamain.questphase / h0 / 44` | `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene`; `#q203_04_sm_delamain` | 67:Out → 44:q203_04_delemain_in; 44:q203_04_delemain_to_afterlife_out → 85:In |
| `q203_delamain.questphase / h12 / 35` | `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene`; `#q203_04_sm_delamain` | 0:Out → 35:q203_04_delemain_lands_IN; 35:q203_04_delemain_lands_out → 1:In |
| `q203_penthouse.questphase / h0 / 196` | `base\quest\main_quests\epilogue\q203\phase\q203_delamain.questphase` | 196:Out1 → 188:In1; 197:Out → 196:Debug_IN; 224:Out → 196:In1 |
| `q203_penthouse.questphase / h620 / 4` | `base\quest\main_quests\epilogue\q203\scenes\q203_02_shower.scene`; `#q203_02_sm_shower` | 29:Out → 4:in_shower; 4:out_shower → 21:In |
| `q203_penthouse.questphase / h719 / 5` | `base\quest\main_quests\epilogue\q203\scenes\q203_03_sobchak.scene`; `#q203_03_sm_sobchak` | 5:q205_02_sobchak_out → 1:In; 29:Out → 5:q203_01a_shower_in; 5:q203_03_sobchak_d_arrives_out → 25:q203_04_delemain_lands_IN |
| `q203_penthouse.questphase / h719 / 25` | `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene`; `#q203_04_sm_delamain` | 5:q203_03_sobchak_d_arrives_out → 25:q203_04_delemain_lands_IN |
| `q203_penthouse.questphase / h828 / 5` | `base\quest\main_quests\epilogue\q203\scenes\q203_02c_judy.scene`; `#q203_02c_sm_judy` | 5:q203_02c_judy_out → 1:In; 23:Out → 5:q203_02c_judy_in; 5:q203_02c_judy_d_lands_out → 16:q203_04_delemain_lands_IN |
| `q203_penthouse.questphase / h828 / 16` | `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene`; `#q203_04_sm_delamain` | 5:q203_02c_judy_d_lands_out → 16:q203_04_delemain_lands_IN |
| `q203_penthouse.questphase / h941 / 7` | `base\quest\main_quests\epilogue\q203\scenes\q203_02b_kerry.scene`; `#q203_02b_sm_kerry` | 7:q203_02b_kerry_in_out → 1:In; 20:Out → 7:q203_02b_kerry_in; 7:q203_02b_kerry_d_lands_out → 17:q203_04_delemain_lands_IN |
| `q203_penthouse.questphase / h941 / 17` | `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene`; `#q203_04_sm_delamain` | 7:q203_02b_kerry_d_lands_out → 17:q203_04_delemain_lands_IN |
| `q203_penthouse.questphase / h1057 / 3` | `base\quest\main_quests\epilogue\q203\scenes\q203_02d_panam.scene`; `#q203_02d_sm_panam` | 3:q203_02d_panam_out → 1:In; 9:Out → 3:q203_02d_panam_in; 3:q203_02d_panam_d_lands → 7:q203_04_delemain_lands_IN |
| `q203_penthouse.questphase / h1057 / 7` | `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene`; `#q203_04_sm_delamain` | 3:q203_02d_panam_d_lands → 7:q203_04_delemain_lands_IN |
| `q203_penthouse.questphase / h1220 / 18` | `base\quest\main_quests\epilogue\q203\scenes\q203_02d_panam.scene`; `#q203_02d_sm_panam` | 7:Out → 18:panam_farewell_interaction; 19:Out → 18:panam_farewell_interaction |
| `q203_penthouse.questphase / h1685 / 2` | `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene`; `#q203_04_sm_delamain` | 3:Out → 2:q203_04_emmerick_calls_IN |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.quest` / h0 / 2 | `mws_wat_02.questphase` | 5: FactsDBManager: q101_enable_side_content; 5:Out → 2:In1 |
| `base\open_world\mini_world_stories\watson\watson_mini_world_stories.questphase` / h0 / 8 | `mws_wat_02.questphase` | 15: PauseCondition; 28: PauseCondition; 15:Out → 8:In1; 28:Out → 8:kill |
| `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h20 / 15 | `mws_wat_02.scene` | 30: Condition: mws_wat_02_iguana_cat_together_active GreaterOrEqual 1; 30:False → 15:mws_wat_02_in |
| `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h20 / 31 | `mws_wat_02.scene` | 30: Condition: mws_wat_02_iguana_cat_together_active GreaterOrEqual 1; 30:True → 31:mws_wat_02_iguana_cat_in |
| `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h229 / 7 | `mws_wat_02.scene` | 6: PauseCondition; 6:Out → 7:mws_wat_02_q203_in |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h119 / 4 | `q203_quest_bugfixes.questphase` | 0: Input; 0:Out → 4:In1 |
| `base\quest\main_quests\epilogue\q203\q203_legend.quest` / h0 / 31 | `q203_quest_bugfixes.questphase` | 27: FactsDBManager: q204_var_test_def; 27:Out → 31:In1 |
| `base\quest\main_quests\epilogue\q203\q203_legend.questphase` / h0 / 5 | `q203_afterlife.questphase` | 19: Phase: q203_av_ride.questphase; 16: Input; 5:Out1 → 6:In1; 19:Out1 → 5:In1; 16:Out → 5:debug_in |
| `base\quest\main_quests\epilogue\q203\q203_legend.questphase` / h0 / 19 | `q203_av_ride.questphase` | 2: Phase: q203_penthouse.questphase; 2:Out1 → 19:In1; 19:Out1 → 5:In1 |
| `base\quest\main_quests\epilogue\q203\q203_legend.questphase` / h0 / 6 | `q203_cosmos.questphase` | 5: Phase: q203_afterlife.questphase; 27: PauseCondition: {"seconds": 5}; 5:Out1 → 6:In1; 6:Out1 → 20:In1; 27:Out → 6:debug_in |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 196 | `q203_delamain.questphase` | 197: Input; 224: Checkpoint; 196:Out1 → 188:In1; 197:Out → 196:Debug_IN; 224:Out → 196:In1 |
| `base\quest\main_quests\epilogue\q203\q203_legend.questphase` / h0 / 2 | `q203_penthouse.questphase` | 22: FactsDBManager: claire_default_on write/default comparison 0; 14: Input; 2:Out1 → 19:In1; 22:Out → 2:In1; 14:Out → 2:in_delamain |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h620 / 4 | `q203_02_shower.scene` | 29: Audio; 29:Out → 4:in_shower; 4:out_shower → 21:In |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h941 / 7 | `q203_02b_kerry.scene` | 20: Audio; 7:q203_02b_kerry_in_out → 1:In; 20:Out → 7:q203_02b_kerry_in; 7:q203_02b_kerry_d_lands_out → 17:q203_04_delemain_lands_IN |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h828 / 5 | `q203_02c_judy.scene` | 23: SpawnManager; 5:q203_02c_judy_out → 1:In; 23:Out → 5:q203_02c_judy_in; 5:q203_02c_judy_d_lands_out → 16:q203_04_delemain_lands_IN |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h1057 / 3 | `q203_02d_panam.scene` | 9: Audio; 3:q203_02d_panam_out → 1:In; 9:Out → 3:q203_02d_panam_in; 3:q203_02d_panam_d_lands → 7:q203_04_delemain_lands_IN |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h1220 / 18 | `q203_02d_panam.scene` | 7: FactsDBManager: q203_fact_lover_says_goodbye; 19: PauseCondition: {"seconds": 1}; 7:Out → 18:panam_farewell_interaction; 19:Out → 18:panam_farewell_interaction |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h719 / 5 | `q203_03_sobchak.scene` | 29: Audio; 5:q205_02_sobchak_out → 1:In; 29:Out → 5:q203_01a_shower_in; 5:q203_03_sobchak_d_arrives_out → 25:q203_04_delemain_lands_IN |
| `base\quest\side_quests\sq021\phases\sq021_braindance.questphase` / h1120 / 159 | `q203_03_sobchak.scene` | 158: Scene: sq017_10_us_crack_intro.scene; 158:sq021_we_got_out → 159:sq021_okay_in; 159:sq021_okay_out → 160:sq021_nothing_left_in |
| `base\quest\main_quests\epilogue\q203\phase\q203_afterlife.questphase` / h0 / 207 | `q203_04_delamain.scene` | 209: PauseCondition: #q203_tr_enter_elevator_top; 209:Out → 207:q203_04_delemain_leaves_IN |
| `base\quest\main_quests\epilogue\q203\phase\q203_av_ride.questphase` / h0 / 4 | `q203_04_delamain.scene` | 0: Input; 0:Out → 4:q203_04_goodbye_to_nc_in; 4:q203_04_goodbye_to_nc_out → 39:In |
| `base\quest\main_quests\epilogue\q203\phase\q203_delamain.questphase` / h0 / 44 | `q203_04_delamain.scene` | 67: PauseCondition: #q203_tr_penthouse_garage; 67:Out → 44:q203_04_delemain_in; 44:q203_04_delemain_to_afterlife_out → 85:In |
| `base\quest\main_quests\epilogue\q203\phase\q203_delamain.questphase` / h12 / 35 | `q203_04_delamain.scene` | 0: Input; 0:Out → 35:q203_04_delemain_lands_IN; 35:q203_04_delemain_lands_out → 1:In |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h719 / 25 | `q203_04_delamain.scene` | 5: Scene: q203_03_sobchak.scene; 5:q203_03_sobchak_d_arrives_out → 25:q203_04_delemain_lands_IN |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h828 / 16 | `q203_04_delamain.scene` | 5: Scene: q203_02c_judy.scene; 5:q203_02c_judy_d_lands_out → 16:q203_04_delemain_lands_IN |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h941 / 17 | `q203_04_delamain.scene` | 7: Scene: q203_02b_kerry.scene; 7:q203_02b_kerry_d_lands_out → 17:q203_04_delemain_lands_IN |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h1057 / 7 | `q203_04_delamain.scene` | 3: Scene: q203_02d_panam.scene; 3:q203_02d_panam_d_lands → 7:q203_04_delemain_lands_IN |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h1685 / 2 | `q203_04_delamain.scene` | 3: PauseCondition: {"seconds": 3}; 3:Out → 2:q203_04_emmerick_calls_IN |
| `base\quest\main_quests\epilogue\q203\phase\q203_afterlife.questphase` / h0 / 135 | `q203_05_afterlife.scene` | 149: PauseCondition: #q203_tr_emmerick_talk; 135:q203_05_mr_blueeyes_leaving_out → 1:In; 149:Out → 135:q203_05_afterlife_booth_in; 135:q203_05_mr_blueeyes_leaving_out → 203:In; 135:q203_05_mr_blueeyes_leaving_out → 215:In |
| `base\quest\main_quests\epilogue\q203\phase\q203_afterlife.questphase` / h0 / 153 | `q203_05_afterlife.scene` | 152: PauseCondition: #q203_05_tr_claire_welcome; 152:Out → 153:q203_05_claire_drink_in; 153:q203_05_claire_drink_out → 157:Succeeded |
| `base\quest\main_quests\epilogue\q203\phase\q203_afterlife.questphase` / h0 / 196 | `q203_05_afterlife.scene` | 206: Condition: q115_did_it_solo; 198: Condition: q115_jungle_weyland_saved; 206:True → 196:Weyland_Rogue; 198:True → 196:q203_05_weyland_IN |
| `base\quest\main_quests\epilogue\q203\phase\q203_afterlife.questphase` / h0 / 205 | `q203_05_afterlife.scene` | 204: Condition: q115_did_it_solo; 204:True → 205:Rogue_start |
| `base\quest\main_quests\epilogue\q203\phase\q203_cosmos.questphase` / h0 / 10 | `q203_06_cosmos.scene` | 70: LogicalHub; 70:Out1 → 10:q203_06_cosmos_mr_blue_eyes_IN; 10:clean_up → 64:In1; 10:q203_06_cosmos_mr_blue_eyes_OUT → 63:In |
| `base\quest\main_quests\epilogue\q203\phase\q203_cosmos.questphase` / h0 / 73 | `q203_06_cosmos.scene` | 63: Checkpoint; 63:Out → 73:q203_06_helmet_IN; 73:q203_06_final_cutscene_OUT → 82:In |
| `base\open_world\mini_world_stories\ow_mini_world_stories.questphase` / h0 / 7 | `watson_mini_world_stories.questphase` | 13: LogicalHub; 13:Out1 → 7:In1 |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
| `base\quest\main_quests\epilogue\epilogue.questphase` / h0 / 11 | `q203_legend.questphase` | 19: Input; 19:Out → 11:In1; 11:Out1 → 27:In |
| `base\quest\main_quests\epilogue\q203\q203_legend.quest` / h0 / 22 | `q203_legend.questphase` | 23: Scene: q203_chickentest.scene; 23: Scene: q203_chickentest.scene; 23: Scene: q203_chickentest.scene; 23: Scene: q203_chickentest.scene; 22:Out1 → 1:In; 23:out_penthouse → 22:In1; 23:out_delamain → 22:in_delamain; 23:out_afterlife → 22:in_afterlife; 23:out_cosmos → 22:in_cosmos |
| `base\quest\side_quests\sq021\sq021.questphase` / h0 / 13 | `sq021_braindance.questphase` | 7: Input; 16: Phase: sq021_ride_back.questphase; 64: FactsDBManager: sq021_school_clue_bulletin; 7:Out → 13:In1; 16:Out1 → 13:In1; 13:Out1 → 23:In1; 64:Out → 13:bd_farm_in |
| `base\open_world\phases\open_world_content.questphase` / h0 / 93 | `ow_mini_world_stories.questphase` | 92: DeletionMarker; 92:Out → 93:In1; 93:SignalPickup → 101:In |
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
| `base\quest\cyberpunk2077.questphase` / h0 / 36 | `epilogue.questphase` | 33: Phase: act_1.questphase; 33: Phase: act_1.questphase; 33: Phase: act_1.questphase; 33: Phase: act_1.questphase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 33:Q201 → 36:Q201; 33:Q202 → 36:Q202; 33:Q203 → 36:Q203; 33:Q204 → 36:Q204; 57:Q201 Out → 36:Q201; 36:Q201 Final Board → 56:Q201; 57:Q202 Out → 36:Q202; 36:Q202 Final Board → 56:Q202; 57:Q203 Out → 36:Q203; 36:Q203 Final Board → 56:Q203; 57:Q204 Out → 36:Q204; 36:Q204 Final Board → 56:Q204 |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 127 | `epilogue.questphase` | 73: Phase: q116_mikoshi.questphase; 73: Phase: q116_mikoshi.questphase; 73: Phase: q116_mikoshi.questphase; 113: Phase: q113.questphase; 73:q202_out → 127:Q202; 73:q203_out → 127:Q203; 73:q204_out → 127:Q204; 113:Out1 → 127:Q201; 127:Q201 Final Board → 128:Q201; 127:Q202 Final Board → 128:Q202; 127:Q203 Final Board → 128:Q203; 127:Q204 Final Board → 128:Q204 |
| `base\quest\side_quests\sidequests.questphase` / h0 / 54 | `sq021.questphase` | 111: PauseCondition; 111:Out → 54:In1; 54:Out1 → 185:In |
| `base\quest\side_quests\sq021\sq021.quest` / h0 / 2 | `sq021.questphase` | 19: TeleportPuppet; 22: TeleportPuppet; 54: RenderFxManager; 28: TeleportPuppet; 49: RenderFxManager; 15: Phase; 6: RenderFxManager; 7: RenderFxManager; 14: RenderFxManager; 12: RenderFxManager; 11: RenderFxManager; 10: RenderFxManager; 9: RenderFxManager; 59: RenderFxManager; 60: RenderFxManager; 16: RenderFxManager; 52: RenderFxManager; 2:Out1 → 1:In; 19:Out → 2:In1; 22:Out → 2:meeting_river_in; 54:Out → 2:river_follower; 28:Out → 2:entering_lab; 49:Out → 2:chicken_lab_in; 15:Out1 → 2:ride_in; 6:Out → 2:randys_room_in; 7:Out → 2:investigation_in; 14:Out → 2:bbq_in; 12:Out → 2:ride_back_in; 11:Out → 2:bd_in; 10:Out → 2:bd_farm_in; 9:Out → 2:finale_in; 59:Out → 2:chicken_wrong_in; 60:Out → 2:wrong_fight_in; 16:Out → 2:good_farm_in; 52:Out → 2:the_end_in |
| `base\open_world\district_definitions\open_world_kabuki.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\metro\ue_metro\ue_metro.quest` / h0 / 21 | `open_world_content.questphase` | 0: Start; 0:Out → 21:EP1_Standalone |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.quest` / h0 / 7 | `open_world_content.questphase` | 8: Scene: ma_bls_ina_07_chicken.scene; 8:start → 7:In1 |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.quest` / h0 / 3 | `open_world_content.questphase` | 2: FactsDBManager: sts_std_arr_tier_1; 2:Out → 3:In1 |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest` / h0 / 4 | `open_world_content.questphase` | 3: FactsDBManager: sts_wat_kab_tier_1; 3:Out → 4:In1 |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.quest` / h0 / 3 | `open_world_content.questphase` | 2: FactsDBManager: sts_wat_nid_tier_1; 2:Out → 3:In1 |
| `base\open_world\open_world_test.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\police_system\police_system_test.quest` / h0 / 2 | `open_world_content.questphase` | 4: PauseCondition: {"seconds": 1}; 4:Out → 2:In1 |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest` / h0 / 4 | `open_world_content.questphase` | 0: Start; 0:Out → 4:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 19 | `open_world_content.questphase` | 0: Input; 36: Input; 0:Out → 19:In1; 36:Out → 19:EP1_Standalone |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
| `base\quest\cyberpunk2077.questphase` / h520 / 5 | `sidequests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:sq026_02_signal → 5:sq026_02_signal; 7:Out1 → 5:In1; 8:Out → 5:In1; 21:Out → 5:EP1_Standalone |
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

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mws_wat_02.scene` | mws_wat_02_in, mws_wat_02_iguana_cat_in, johnny_jamming, mws_wat_02_q203_in →  | Iguana; Johnny; IguanaQ203; NibblesPuff; IguanaPuff; Player; 109 nodes / 124 edges |
| `q203_02_shower.scene` | in_shower, Start 12, Start 13, q203_02_assistant_help_IN → out_shower, q203_02_assistant_help_OUT | sobchak; rogue; judy; kerry; assistant; tpp_male; tpp_female; V; 65 nodes / 63 edges |
| `q203_02b_kerry.scene` | q203_02b_kerry_in, test_preview_balcony, preview_bed, Start 7, kerry_proximity → q203_02b_kerry_in_out, q203_02b_kerry_d_lands_out | kerry; q203_02b_female_tpp; q203_02b_male_tpp; delamain_av; v; 208 nodes / 254 edges |
| `q203_02c_judy.scene` | preview_bed, q203_02c_judy_in, in_goodbye, preview_01 → q203_02c_judy_out, q203_02c_judy_d_lands_out | judy; v_female_tpp; v_male_tpp; q203_02c_delamain_av; v; 172 nodes / 223 edges |
| `q203_02d_panam.scene` | q203_02d_panam_in, preview_kitchen, preview_balcony, Start 9, panam_farewell_interaction, Start 8, Start 10 → q203_02d_panam_out, q203_02d_panam_d_lands | panam; q203_02d_tpp_female; q203_02d_tpp_male; q203_02d_delamain_av; Player; 155 nodes / 190 edges |
| `q203_03_sobchak.scene` | Start 9, q203_01a_shower_in, sq021_okay_in, preview_kitchen, preview_balcony → q205_02_sobchak_out, sq021_okay_out, q203_03_sobchak_d_arrives_out | sobchak; tpp_female; tpp_male; q203_03_delamain_av; v; 211 nodes / 253 edges |
| `q203_04_delamain.scene` | q203_04_delemain_in, emmerick_holocall_prev, q203_04_delemain_lands_IN, q203_04_goodbye_to_nc_in, q203_04_delemain_leaves_IN, av_preview, q203_04_emmerick_calls_IN → q203_04_delemain_to_afterlife_out, q203_04_delemain_lands_out, q203_04_delemain_leaves_OUT, q203_04_goodbye_to_nc_out, q203_04_emmerick_calls_OUT | delamain; emmerick; delamain_sad; Delamain_av; v; 151 nodes / 191 edges |
| `q203_05_afterlife.scene` | q203_05_afterlife_booth_in, Start 13, q203_05_weyland_IN, Rogue_start, q203_05_emmerick_greets_in, q203_05_claire_drink_in, Weyland_Rogue → q203_05_mr_blueeyes_leaving_out, q203_05_weyland_OUT, q203_05_claire_drink_out | emmerick; mr_blue_eyes; claire; weyland; rogue; janitor; drunk_at_bar; man_in_booth_01; man_in_booth_02; nibbles; v; 263 nodes / 333 edges |
| `q203_06_cosmos.scene` | Start 6, q203_06_cosmos_mr_blue_eyes_IN, q203_06_helmet_IN, q203_06_see_you_IN, q203_06_final_cutscene_IN → q203_06_cosmos_mr_blue_eyes_OUT, q203_06_helmet_OUT, q203_06_final_cutscene_OUT, clean_up | mrx; q203_female_v_tpp; q203_male_v_tpp; v; 141 nodes / 146 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mws_wat_02.scene / n271 / 0` | Pogłaskaj (`Option`) | {"questCondition": {"$type": "questLogicalCondition", "conditions": [{"$type": "questJournalCondition", "type": {"$type": "questJournalEntryState_ConditionType", "path": {"$type": "gameJournalPath", "realPath": "ep1/quests/main_quest/q305_border_crossing/08_border_crossing/10_talk_to_johnny", "fileEntryIndex": 2, "className": "gameJournalQuestObjective"}, "state": "Active", "inverted": true}}, {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq055_apt_interactions_off", "comparisonType": "Equal"}}]}} | 0:0 → 510:0:0; 0:0 → 684:0:1 |
| `mws_wat_02.scene / n487 / 0` | Połóż jajo iguany (`place`) | {"questCondition": {"$type": "questLogicalCondition", "conditions": [{"$type": "questJournalCondition", "type": {"$type": "questJournalEntryState_ConditionType", "path": {"$type": "gameJournalPath", "realPath": "ep1/quests/main_quest/q305_border_crossing/08_border_crossing/10_talk_to_johnny", "fileEntryIndex": 2, "className": "gameJournalQuestObjective"}, "state": "Active", "inverted": true}}, {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq055_apt_interactions_off", "comparisonType": "Equal"}}]}} | 0:0 → 174:0:1; 0:0 → 633:0:1 |
| `q203_02_shower.scene / n309 / 0` | [Take shower] (``) | No option-level predicate stored | 0:0 → 397:0:0 |
| `q203_02_shower.scene / n313 / 0` | [Make coffee] (``) | No option-level predicate stored | 0:0 → 461:0:0 |
| `q203_02_shower.scene / n317 / 0` | [Drink] (``) | No option-level predicate stored | 0:0 → 513:0:0 |
| `q203_02_shower.scene / n351 / 0` | [Stand] (``) | No option-level predicate stored | 0:0 → 350:0:0 |
| `q203_02_shower.scene / n386 / 0` | [Wash off blood] (``) | No option-level predicate stored | 0:0 → 387:0:0; 0:0 → 4386:0:1 |
| `q203_02_shower.scene / n533 / 0` | [Lean] (``) | No option-level predicate stored | 0:0 → 535:0:0 |
| `q203_02_shower.scene / n540 / 0` | [Step away] (``) | No option-level predicate stored | 0:0 → 542:0:0 |
| `q203_02_shower.scene / n2163 / 0` | [Take amulet] (``) | No option-level predicate stored | 0:0 → 2165:0:0 |
| `q203_02b_kerry.scene / n18 / 0` | Could've been important. (``) | No option-level predicate stored | 0:0 → 20:0:0 |
| `q203_02b_kerry.scene / n18 / 1` | That an ex? (``) | No option-level predicate stored | 0:1 → 22:0:0 |
| `q203_02b_kerry.scene / n27 / 0` | Agonizing about the future's a waste of time, too. (``) | No option-level predicate stored | 0:0 → 29:0:0 |
| `q203_02b_kerry.scene / n27 / 1` | True, that. (``) | No option-level predicate stored | 0:1 → 31:0:0 |
| `q203_02b_kerry.scene / n45 / 0` | Don't worry about me. I'll be fine. (``) | No option-level predicate stored | 0:0 → 47:0:0 |
| `q203_02b_kerry.scene / n45 / 1` | Not feeling well. Gets worse every day. (``) | No option-level predicate stored | 0:1 → 51:0:0 |
| `q203_02b_kerry.scene / n45 / 2` | Just noticed yesterday? (``) | No option-level predicate stored | 0:2 → 56:0:0 |
| `q203_02b_kerry.scene / n58 / 0` | You got no idea what you're talkin' about. (``) | No option-level predicate stored | 0:0 → 60:0:0 |
| `q203_02b_kerry.scene / n58 / 1` | I don't wanna argue. (``) | No option-level predicate stored | 0:1 → 63:0:0 |
| `q203_02b_kerry.scene / n68 / 0` | What now? (``) | No option-level predicate stored | 0:0 → 33:0:0 |
| `q203_02b_kerry.scene / n68 / 1` | Think about him often? (``) | No option-level predicate stored | 0:1 → 75:0:0 |
| `q203_02b_kerry.scene / n139 / 0` | [Make coffee] (``) | No option-level predicate stored | 0:0 → 157:0:1; 0:0 → 438:0:0 |
| `q203_02b_kerry.scene / n142 / 0` | [Drink coffee] (``) | No option-level predicate stored | 0:0 → 454:0:0 |
| `q203_02b_kerry.scene / n178 / 0` | It's not enough. I don't know any other way. (``) | No option-level predicate stored | 0:0 → 180:0:0 |
| `q203_02b_kerry.scene / n178 / 1` | Easy for you to say. You're not dying. (``) | No option-level predicate stored | 0:1 → 183:0:0 |
| `q203_02b_kerry.scene / n178 / 2` | Can't believe my ears. You're worried about me? (``) | No option-level predicate stored | 0:2 → 191:0:0 |
| `q203_02b_kerry.scene / n185 / 0` | Don't wanna lose you, either. (``) | No option-level predicate stored | 0:0 → 194:0:0 |
| `q203_02b_kerry.scene / n185 / 1` | We both know how this ends. (``) | No option-level predicate stored | 0:1 → 197:0:0 |
| `q203_02b_kerry.scene / n213 / 0` | [Take shower] (``) | No option-level predicate stored | 0:0 → 214:0:0; 0:0 → 1000:0:1; 0:0 → 2249:0:1 |
| `q203_02b_kerry.scene / n223 / 0` | [Stand] (``) | No option-level predicate stored | 0:0 → 224:1:0; 0:0 → 262:0:0 |
| `q203_02b_kerry.scene / n224 / 0` | [Kiss] Rise and shine. (``) | No option-level predicate stored | 0:0 → 223:1:0; 0:0 → 267:0:0 |
| `q203_02b_kerry.scene / n233 / 0` | [Hug] Take care of yourself. (``) | No option-level predicate stored | 0:0 → 200:0:0 |
| `q203_02b_kerry.scene / n233 / 1` | [Step away] I gotta go. (``) | No option-level predicate stored | 0:1 → 238:0:0; 0:1 → 881:1:0 |
| `q203_02b_kerry.scene / n252 / 0` | [Turn] (``) | No option-level predicate stored | 0:0 → 254:0:0 |
| `q203_02b_kerry.scene / n302 / 0` | [Wash off blood] Mhmmm... (``) | No option-level predicate stored | 0:0 → 300:0:0; 0:0 → 2204:0:1 |
| `q203_02b_kerry.scene / n319 / 0` | [Lean] (``) | No option-level predicate stored | 0:0 → 320:0:0; 0:0 → 572:0:0; 0:0 → 581:0:1; 0:0 → 871:1:0; 0:0 → 971:0:1 |
| `q203_02b_kerry.scene / n2163 / 0` | [Take amulet] (``) | No option-level predicate stored | 0:0 → 2165:0:0 |
| `q203_02c_judy.scene / n18 / 0` | Special? (`Special`) | No option-level predicate stored | 0:0 → 20:0:0 |
| `q203_02c_judy.scene / n18 / 1` | Lost? (`Stronger`) | No option-level predicate stored | 0:1 → 22:0:0 |
| `q203_02c_judy.scene / n18 / 2` | What? (`How`) | No option-level predicate stored | 0:2 → 24:0:0 |
| `q203_02c_judy.scene / n30 / 0` | You have me... (`WhatAboutMe`) | No option-level predicate stored | 0:0 → 32:0:0 |
| `q203_02c_judy.scene / n30 / 1` | I know what you mean. (`I know`) | No option-level predicate stored | 0:1 → 36:0:0 |
| `q203_02c_judy.scene / n42 / 0` | What phase is this? (`Current`) | No option-level predicate stored | 0:0 → 44:0:0 |
| `q203_02c_judy.scene / n42 / 1` | Things'll be different now. (`Different`) | No option-level predicate stored | 0:1 → 49:0:0 |
| `q203_02c_judy.scene / n42 / 2` | That's life in this city. (`ThatsNC`) | No option-level predicate stored | 0:2 → 52:0:0 |
| `q203_02c_judy.scene / n62 / 0` | Nothing's wrong. For the past few months, nothing... (`Yeah`) | No option-level predicate stored | 0:0 → 64:0:0 |
| `q203_02c_judy.scene / n62 / 1` | Just tired... (`Tired`) | No option-level predicate stored | 0:1 → 66:0:0 |
| `q203_02c_judy.scene / n62 / 2` | You know what's wrong. I'm dying. (`youknow`) | No option-level predicate stored | 0:2 → 68:0:0 |
| `q203_02c_judy.scene / n72 / 0` | Don't worry. (`DontWorry`) | No option-level predicate stored | 0:0 → 76:0:0 |
| `q203_02c_judy.scene / n72 / 1` | Let's talk about something else. (`NoTalk`) | No option-level predicate stored | 0:1 → 78:0:0 |
| `q203_02c_judy.scene / n90 / 0` | You should go. (`Leave`) | No option-level predicate stored | 0:0 → 92:0:0 |
| `q203_02c_judy.scene / n90 / 1` | I need you. (`NeedU`) | No option-level predicate stored | 0:1 → 95:0:0 |
| `q203_02c_judy.scene / n191 / 0` | [Drink coffee] (`take_mug`) | No option-level predicate stored | 0:0 → 698:0:0 |
| `q203_02c_judy.scene / n275 / 0` | Still got somethin' to prove to this city. (`legend`) | No option-level predicate stored | 0:0 → 278:0:0 |
| `q203_02c_judy.scene / n275 / 1` | Don't have much time. It's gotta be now. (`time`) | No option-level predicate stored | 0:1 → 280:0:0 |
| `q203_02c_judy.scene / n275 / 2` | Wherever you go – won't let you forget me. (`fame`) | No option-level predicate stored | 0:2 → 282:0:0 |
| `q203_02c_judy.scene / n361 / 0` | [Stand] Hey... I'ma take a shower. (`Get up`) | No option-level predicate stored | 0:0 → 363:1:0; 0:0 → 399:0:0 |
| `q203_02c_judy.scene / n363 / 0` | [Kiss] Morning. (`kiss get up`) | No option-level predicate stored | 0:0 → 361:1:0; 0:0 → 405:0:0 |
| `q203_02c_judy.scene / n410 / 0` | [Hug] Time I was on my way. (`Hug`) | No option-level predicate stored | 0:0 → 412:0:0 |
| `q203_02c_judy.scene / n410 / 1` | [Step away] Better get goin'. (`Leave`) | No option-level predicate stored | 0:1 → 416:0:0 |
| `q203_02c_judy.scene / n475 / 0` | [Wash off blood] (`wash_blood`) | No option-level predicate stored | 0:0 → 497:0:0 |
| `q203_02c_judy.scene / n509 / 0` | [Turn] (`Turn around`) | No option-level predicate stored | 0:0 → 395:0:0 |
| `q203_02c_judy.scene / n522 / 0` | [Stand] Gonna hop in the shower. (`Get up `) | No option-level predicate stored | 0:0 → 1289:0:0 |
| `q203_02c_judy.scene / n541 / 0` | [Take shower] (`Take Shower`) | No option-level predicate stored | 0:0 → 469:0:0; 0:0 → 582:0:1 |
| `q203_02c_judy.scene / n667 / 0` | [Lean] (`join`) | No option-level predicate stored | 0:0 → 15:0:0; 0:0 → 2170:0:1 |
| `q203_02c_judy.scene / n2105 / 0` | [Take amulet] (`Option_01`) | No option-level predicate stored | 0:0 → 2100:0:0 |
| `q203_02d_panam.scene / n56 / 0` | [Drink coffee] (`Take_coffee`) | No option-level predicate stored | 0:0 → 504:0:0 |
| `q203_02d_panam.scene / n102 / 0` | Night City's my city. Still got something to prove here. (`mycity`) | No option-level predicate stored | 0:0 → 111:0:0 |
| `q203_02d_panam.scene / n102 / 1` | Even if I leave with you, my time's almost up. (`notime`) | No option-level predicate stored | 0:1 → 118:0:0 |
| `q203_02d_panam.scene / n102 / 2` | Why don't you stay here with me? (`youstay`) | No option-level predicate stored | 0:2 → 105:0:0 |
| `q203_02d_panam.scene / n109 / 0` | For Night City. I still have something to prove to it. (`nc`) | No option-level predicate stored | 0:0 → 111:0:0 |
| `q203_02d_panam.scene / n109 / 1` | Even if I run away with you, I'll still be short on time. You know that. (`notime`) | No option-level predicate stored | 0:1 → 118:0:0 |
| `q203_02d_panam.scene / n113 / 0` | Don't wanna lose you. But there's no other way. (`looseyou`) | No option-level predicate stored | 0:0 → 124:0:0 |
| `q203_02d_panam.scene / n113 / 1` | I'm dying. Lemme settle my affairs. (`dying`) | No option-level predicate stored | 0:1 → 126:0:0 |
| `q203_02d_panam.scene / n113 / 2` | So this is goodbye? (`farewell`) | No option-level predicate stored | 0:2 → 116:0:0 |
| `q203_02d_panam.scene / n128 / 0` | See you, Panam. Someday. (`seeya`) | No option-level predicate stored | 0:0 → 135:0:0 |
| `q203_02d_panam.scene / n128 / 1` | We don't have to say goodbye. (`nomad`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "67091901544"}}}} | 0:1 → 140:0:0 |
| `q203_02d_panam.scene / n158 / 0` | [Take shower] Didn't wanna wait for me? (`shower`) | No option-level predicate stored | 0:0 → 718:0:0 |
| `q203_02d_panam.scene / n215 / 0` | [Stand] (`Get up`) | No option-level predicate stored | 0:0 → 213:0:0 |
| `q203_02d_panam.scene / n253 / 0` | Everything all right? (`Talk`) | No option-level predicate stored | 0:0 → 9:0:0 |
| `q203_02d_panam.scene / n253 / 1` | Wanna see the Crystal Palace? (`Talk2`) | No option-level predicate stored | 0:1 → 500:0:0 |
| `q203_02d_panam.scene / n289 / 0` | [Wash off blood] (`Wash Blood`) | No option-level predicate stored | 0:0 → 288:0:0; 0:0 → 2177:0:1 |
| `q203_02d_panam.scene / n315 / 0` | [Lean] (`Join`) | No option-level predicate stored | 0:0 → 312:0:0; 0:0 → 671:0:1; 0:0 → 975:0:1 |
| `q203_02d_panam.scene / n406 / 0` | [Hug] Till next time. (`Hug`) | No option-level predicate stored | 0:0 → 132:0:0 |
| `q203_02d_panam.scene / n406 / 1` | Gotta go – Afterlife awaits. (`Leave`) | No option-level predicate stored | 0:1 → 137:0:0 |
| `q203_02d_panam.scene / n493 / 0` | [Turn] (`Turn`) | No option-level predicate stored | 0:0 → 221:0:0 |
| `q203_02d_panam.scene / n1037 / 0` | [Take amulet] (`Option_01`) | No option-level predicate stored | 0:0 → 1039:0:0 |
| `q203_03_sobchak.scene / n88 / 0` | Nothing. Everything'll be fine soon. (``) | No option-level predicate stored | 0:0 → 90:0:0 |
| `q203_03_sobchak.scene / n88 / 1` | Just tired. (``) | No option-level predicate stored | 0:1 → 99:0:0 |
| `q203_03_sobchak.scene / n88 / 2` | We'll talk later. (``) | No option-level predicate stored | 0:2 → 96:0:0 |
| `q203_03_sobchak.scene / n94 / 0` | You're right, it won't end well. (``) | No option-level predicate stored | 0:0 → 112:0:0 |
| `q203_03_sobchak.scene / n94 / 1` | Give me some time. (``) | No option-level predicate stored | 0:1 → 114:0:0 |
| `q203_03_sobchak.scene / n101 / 0` | Not this time. (``) | No option-level predicate stored | 0:0 → 103:0:0 |
| `q203_03_sobchak.scene / n101 / 1` | You being here's enough. (``) | No option-level predicate stored | 0:1 → 106:0:0 |
| `q203_03_sobchak.scene / n261 / 0` | [Drink coffee] (``) | No option-level predicate stored | 0:0 → 679:0:0 |
| `q203_03_sobchak.scene / n317 / 0` | What do you mean? Thought everything was pretty clear. (``) | No option-level predicate stored | 0:0 → 319:0:0 |
| `q203_03_sobchak.scene / n317 / 1` | River – I'm dying, remember? (``) | No option-level predicate stored | 0:1 → 323:0:0 |
| `q203_03_sobchak.scene / n317 / 2` | Family is important. But my time's running out. (``) | No option-level predicate stored | 0:2 → 325:0:0 |
| `q203_03_sobchak.scene / n321 / 0` | Is this an interrogation? (``) | No option-level predicate stored | 0:0 → 329:0:0 |
| `q203_03_sobchak.scene / n321 / 1` | We're partners. But some things I gotta do on my own. (``) | No option-level predicate stored | 0:1 → 331:0:0 |
| `q203_03_sobchak.scene / n321 / 2` | Our separate lives never bothered you before. (``) | No option-level predicate stored | 0:2 → 336:0:0 |
| `q203_03_sobchak.scene / n333 / 0` | I want Night City to remember me. (``) | No option-level predicate stored | 0:0 → 342:0:0 |
| `q203_03_sobchak.scene / n333 / 1` | One last job's waiting for me at The Afterlife. (``) | No option-level predicate stored | 0:1 → 346:0:0 |
| `q203_03_sobchak.scene / n344 / 0` | [Hug] See you. (``) | No option-level predicate stored | 0:0 → 582:0:0 |
| `q203_03_sobchak.scene / n344 / 1` | [Step away] Afterlife awaits. (``) | No option-level predicate stored | 0:1 → 352:0:0 |
| `q203_03_sobchak.scene / n344 / 2` | What's your plan? Once I'm gone? (``) | No option-level predicate stored | 0:2 → 349:0:0 |
| `q203_03_sobchak.scene / n432 / 0` | [Take shower] (``) | No option-level predicate stored | 0:0 → 433:0:0; 0:0 → 540:0:1 |
| `q203_03_sobchak.scene / n434 / 0` | [Kiss] (``) | No option-level predicate stored | 0:0 → 435:1:0; 0:0 → 451:0:0 |
| `q203_03_sobchak.scene / n435 / 0` | [Stand] (``) | No option-level predicate stored | 0:0 → 434:1:0; 0:0 → 475:0:0 |
| `q203_03_sobchak.scene / n461 / 0` | [Turn] (``) | No option-level predicate stored | 0:0 → 471:0:0 |
| `q203_03_sobchak.scene / n495 / 0` | pl-pl[wyłącz radio] (``) | No option-level predicate stored | 0:0 → 497:0:0; 0:0 → 1065:0:0 |
| `q203_03_sobchak.scene / n509 / 0` | [Wash off blood] (``) | No option-level predicate stored | 0:0 → 511:0:0 |
| `q203_03_sobchak.scene / n573 / 0` | Thanks. (``) | No option-level predicate stored | 0:0 → 688:0:0; 0:0 → 1116:1:0 |
| `q203_03_sobchak.scene / n573 / 1` | How is she? (``) | No option-level predicate stored | 0:1 → 686:0:0; 0:1 → 1116:1:0 |
| `q203_03_sobchak.scene / n719 / 0` | [Lean] (``) | No option-level predicate stored | 0:0 → 721:0:0; 0:0 → 1132:0:1 |
| `q203_03_sobchak.scene / n1339 / 0` | [Take amulet] (``) | No option-level predicate stored | 0:0 → 1341:0:0 |
| `q203_04_delamain.scene / n44 / 0` | [Get in] Take me to the Afterlife. (`afterlife`) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "q203_fact_gear_gathered"}}} | 0:0 → 208:0:1; 0:0 → 671:0:0; 0:0 → 1201:0:1 |
| `q203_04_delamain.scene / n44 / 1` | Hang on. (`stay_here`) | No option-level predicate stored | 0:1 → 52:0:0 |
| `q203_04_delamain.scene / n120 / 0` | Any news about Arasaka? What's the latest in town? (`city`) | No option-level predicate stored | 0:0 → 122:0:0; 0:0 → 503:0:1 |
| `q203_04_delamain.scene / n120 / 1` | Just take me to the Afterlife. Without the talking. (`Afterlife`) | {"questCondition": {"$type": "questGatherTriggerCondition", "type": "IsOutside", "triggerAreaRef": "#q203_tr_av_arrive_afterlife"}} | 0:1 → 127:0:0; 0:1 → 503:0:1 |
| `q203_04_delamain.scene / n120 / 2` | Too late to help. (`toolate`) | No option-level predicate stored | 0:2 → 124:0:0 |
| `q203_04_delamain.scene / n132 / 0` | Fulfillment? (`fulfill`) | No option-level predicate stored | 0:0 → 134:0:0 |
| `q203_04_delamain.scene / n132 / 1` | I'll die. (`die`) | No option-level predicate stored | 0:1 → 136:0:0 |
| `q203_04_delamain.scene / n132 / 2` | Ask me then. (`asklater`) | No option-level predicate stored | 0:2 → 138:0:0 |
| `q203_04_delamain.scene / n229 / 0` | Just get me to the Afterlife, stat. (`Afterlife`) | {"questCondition": {"$type": "questGatherTriggerCondition", "type": "IsOutside", "triggerAreaRef": "#q203_tr_av_arrive_afterlife"}} | 0:0 → 232:0:0; 0:0 → 507:0:1 |
| `q203_04_delamain.scene / n229 / 1` | Any news about Arasaka? (`gossip`) | No option-level predicate stored | 0:1 → 958:0:0 |
| `q203_04_delamain.scene / n229 / 2` | Little too late for medical help. (`toolate`) | No option-level predicate stored | 0:2 → 231:0:0 |
| `q203_04_delamain.scene / n288 / 0` | Could be the last time I do. (`Option_01`) | No option-level predicate stored | 0:0 → 290:0:0 |
| `q203_04_delamain.scene / n288 / 1` | Mhm. Thanks. (`Option_02`) | No option-level predicate stored | 0:1 → 292:0:0 |
| `q203_04_delamain.scene / n437 / 0` | Get me to the Afterlife, stat. (`Afterlife`) | {"questCondition": {"$type": "questGatherTriggerCondition", "type": "IsOutside", "triggerAreaRef": "#q203_tr_av_arrive_afterlife"}} | 0:0 → 439:0:0; 0:0 → 510:0:1 |
| `q203_04_delamain.scene / n437 / 1` | Little too late for medical help. (`toolate`) | No option-level predicate stored | 0:1 → 438:0:0 |
| `q203_04_delamain.scene / n437 / 2` | Any news about Arasaka? (`gossip`) | No option-level predicate stored | 0:2 → 961:0:0 |
| `q203_04_delamain.scene / n440 / 0` | Could be the last time I do. (`Option_01`) | No option-level predicate stored | 0:0 → 441:0:0 |
| `q203_04_delamain.scene / n440 / 1` | Mhm. Thanks. (`Option_02`) | No option-level predicate stored | 0:1 → 442:0:0 |
| `q203_04_delamain.scene / n468 / 0` | [Get out] (`exit`) | No option-level predicate stored | 0:0 → 714:0:0; 0:0 → 761:0:1; 0:0 → 1136:0:1 |
| `q203_05_afterlife.scene / n230 / 0` | Gonna drink to Johnny. (``) | No option-level predicate stored | 0:0 → 232:0:0 |
| `q203_05_afterlife.scene / n230 / 1` | Wanna drink to Jackie. (``) | No option-level predicate stored | 0:1 → 407:0:0 |
| `q203_05_afterlife.scene / n230 / 2` | Rogue, gonna drink to Rogue. (``) | No option-level predicate stored | 0:2 → 410:0:0 |
| `q203_05_afterlife.scene / n230 / 3` | What about my drink? I'll drink to me. (``) | No option-level predicate stored | 0:3 → 413:0:0 |
| `q203_05_afterlife.scene / n369 / 0` | [Sit] Whaddaya got for me? (``) | No option-level predicate stored | 0:0 → 239:0:0; 0:0 → 377:0:1; 0:0 → 380:0:3; 0:0 → 704:1:0; 0:0 → 1057:1:0; 0:0 → 1207:1:0; 0:0 → 1246:0:0 |
| `q203_05_afterlife.scene / n393 / 0` | [Lean in] The usual. (``) | No option-level predicate stored | 0:0 → 395:0:0; 0:0 → 1509:0:1 |
| `q203_05_afterlife.scene / n393 / 1` | [Lean in] No thanks. (``) | No option-level predicate stored | 0:1 → 400:0:0; 0:1 → 1519:0:1 |
| `q203_05_afterlife.scene / n416 / 0` | I'm the best. Won't let you down. (``) | No option-level predicate stored | 0:0 → 418:0:0 |
| `q203_05_afterlife.scene / n416 / 1` | Got doubts? (``) | No option-level predicate stored | 0:1 → 420:0:0 |
| `q203_05_afterlife.scene / n432 / 0` | They'd be all kinds of wrong. (``) | No option-level predicate stored | 0:0 → 437:0:0 |
| `q203_05_afterlife.scene / n432 / 1` | It's why you hired me. (``) | No option-level predicate stored | 0:1 → 434:0:0 |
| `q203_05_afterlife.scene / n440 / 0` | I'm primed for this. (``) | No option-level predicate stored | 0:0 → 555:0:0; 0:0 → 1065:1:0 |
| `q203_05_afterlife.scene / n547 / 0` | Hey. Back at your post already? (``) | No option-level predicate stored | 0:0 → 546:0:0 |
| `q203_05_afterlife.scene / n547 / 1` | Lookin' brand new. (``) | No option-level predicate stored | 0:1 → 559:0:0 |
| `q203_05_afterlife.scene / n631 / 0` | Hey. (``) | No option-level predicate stored | 0:0 → 973:0:1 |
| `q203_05_afterlife.scene / n670 / 0` | [Drink] (``) | No option-level predicate stored | 0:0 → 426:0:0 |
| `q203_05_afterlife.scene / n697 / 0` | [Stand] (``) | No option-level predicate stored | 0:0 → 469:0:0; 0:0 → 1513:0:1 |
| `q203_05_afterlife.scene / n765 / 0` | Hey. What's the sich? (``) | No option-level predicate stored | 0:0 → 763:0:0 |
| `q203_05_afterlife.scene / n765 / 1` | Hey. Client seems settled in. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mr_blue_seen", "value": 1, "comparisonType": "Equal"}}} | 0:1 → 769:0:0 |
| `q203_05_afterlife.scene / n765 / 2` | Hey. Client here yet? (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mr_blue_seen", "comparisonType": "Equal"}}} | 0:2 → 847:0:0 |
| `q203_05_afterlife.scene / n778 / 0` | [Lean in] The usual. (``) | No option-level predicate stored | 0:0 → 779:0:0 |
| `q203_05_afterlife.scene / n778 / 1` | [Lean in] No thanks. (``) | No option-level predicate stored | 0:1 → 833:0:0 |
| `q203_05_afterlife.scene / n796 / 0` | I'll drink to Johnny. (``) | No option-level predicate stored | 0:0 → 798:0:0 |
| `q203_05_afterlife.scene / n796 / 1` | I'll drink to Jackie. (``) | No option-level predicate stored | 0:1 → 802:0:0 |
| `q203_05_afterlife.scene / n796 / 2` | How about mine? Wanna drink to me. (``) | No option-level predicate stored | 0:2 → 806:0:0 |
| `q203_05_afterlife.scene / n810 / 0` | [Drink] (``) | No option-level predicate stored | 0:0 → 814:0:0 |
| `q203_05_afterlife.scene / n819 / 0` | [Stand] Thanks. (``) | No option-level predicate stored | 0:0 → 816:0:0 |
| `q203_05_afterlife.scene / n843 / 0` | Everything chill? (``) | No option-level predicate stored | 0:0 → 844:0:0; 0:0 → 1018:1:0 |
| `q203_06_cosmos.scene / n73 / 0` | [Put on helmet] (``) | No option-level predicate stored | 0:0 → 156:0:0 |
| `q203_06_cosmos.scene / n108 / 0` | [Stand] (``) | No option-level predicate stored | 0:0 → 146:0:0 |
| `q203_06_cosmos.scene / n118 / 0` | [Open] (``) | No option-level predicate stored | 0:0 → 212:0:1; 0:0 → 395:0:1; 0:0 → 559:0:1; 0:0 → 620:0:1; 0:0 → 1219:0:1; 0:0 → 1232:0:1 |
| `q203_06_cosmos.scene / n160 / 0` | [Open] (``) | No option-level predicate stored | 0:0 → 171:0:0 |
| `q203_06_cosmos.scene / n163 / 0` | [Take gun] (``) | No option-level predicate stored | 0:0 → 229:0:3; 0:0 → 1230:0:1; 0:0 → 1250:0:1 |
| `q203_06_cosmos.scene / n174 / 0` | [Start decompression] Here goes nothin'. (``) | No option-level predicate stored | 0:0 → 176:0:0; 0:0 → 214:0:1; 0:0 → 231:0:3 |
| `q203_06_cosmos.scene / n218 / 0` | [Activate autopilot] (``) | No option-level predicate stored | 0:0 → 57:0:0; 0:0 → 258:0:3; 0:0 → 3061:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CP77-55455` | q203_quest_bugfixes.questphase / h157 / 3 | q203_quest_bugfixes.questphase / h157 / 2 |
| `CYB-12345` | q203_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-637926` | q203_quest_bugfixes.questphase / h28 / 5 | No reader in selected context |
| `air_traffic_off` | q203_afterlife.questphase / h674 / 2 | No reader in selected context |
| `glossary_crystal_palace` | q203_penthouse.questphase / h1423 / 6 | No reader in selected context |
| `holo_emmerick_calls_v_end_activate` | q203_04_delamain.scene / scene / 1054 | No reader in selected context |
| `holo_emmerick_calls_v_end_done` | q203_04_delamain.scene / scene / 1050 | q203_04_delamain.scene / scene / 1049 |
| `holo_emmerick_calls_v_start_activate` | q203_04_delamain.scene / scene / 1053 | No reader in selected context |
| `holo_emmerick_calls_v_start_done` | q203_04_delamain.scene / scene / 1048 | q203_04_delamain.scene / scene / 1047 |
| `iguana_johnny_default_despawn` | mws_wat_02.scene / scene / 684; mws_wat_02.scene / scene / 687 | No reader in selected context |
| `johnny_default_on` | mws_wat_02.questphase / h20 / 37; mws_wat_02.scene / scene / 633; mws_wat_02.scene / scene / 635; mws_wat_02.scene / scene / 638; mws_wat_02.scene / scene / 643; mws_wat_02.scene / scene / 663 | No reader in selected context |
| `mq001_done` | Producer outside selected context | q203_penthouse.questphase / h374 / 14 |
| `mq003_done` | Producer outside selected context | q203_penthouse.questphase / h374 / 24 |
| `mq014_altar_looted` | Producer outside selected context | q203_penthouse.questphase / h374 / 18 |
| `mq019_done` | Producer outside selected context | q203_penthouse.questphase / h374 / 22 |
| `mq033_done` | Producer outside selected context | q203_penthouse.questphase / h374 / 9 |
| `mq055_apt_interactions_off` | Producer outside selected context | mws_wat_02.scene / scene / 271; mws_wat_02.scene / scene / 487 |
| `mr_blue_seen` | q203_05_afterlife.scene / scene / 1007 | q203_05_afterlife.scene / scene / 765 |
| `mws_wat_02_egg_placed` | mws_wat_02.scene / scene / 45 | mws_wat_02.questphase / h0 / 35; mws_wat_02.scene / scene / 57 |
| `mws_wat_02_iguana_cat_together` | mws_wat_02.questphase / h20 / 24; mws_wat_02.scene / scene / 602 | mws_wat_02.questphase / h20 / 27 |
| `mws_wat_02_iguana_cat_together_active` | mws_wat_02.questphase / h20 / 29; mws_wat_02.scene / scene / 601 | mws_wat_02.questphase / h20 / 30 |
| `mws_wat_02_iguana_cat_together_done` | mws_wat_02.scene / scene / 607 | No reader in selected context |
| `mws_wat_02_iguana_hatched` | mws_wat_02.questphase / h0 / 33 | mws_wat_02.questphase / h20 / 17; mws_wat_02.scene / scene / 231; mws_wat_02.scene / scene / 61 |
| `mws_wat_02_iguana_petted` | mws_wat_02.scene / scene / 551 | mws_wat_02.scene / scene / 553 |
| `mws_wat_02_iguana_reaction` | mws_wat_02.scene / scene / 98 | mws_wat_02.scene / scene / 101 |
| `mws_wat_02_johnny_plays` | mws_wat_02.questphase / h20 / 18; mws_wat_02.scene / scene / 437 | mws_wat_02.scene / scene / 444 |
| `mws_wat_02_started` | mws_wat_02.questphase / h20 / 7 | No reader in selected context |
| `nibbles_unlocked` | Producer outside selected context | q203_05_afterlife.scene / scene / 1525 |
| `q101_done` | Producer outside selected context | mws_wat_02.questphase / h0 / 56 |
| `q115_did_it_solo` | Producer outside selected context | q203_afterlife.questphase / h0 / 204; q203_afterlife.questphase / h0 / 206; q203_afterlife.questphase / h16 / 44 |
| `q115_judy_romance_chosen` | Producer outside selected context | q203_penthouse.questphase / h1261 / 22; q203_penthouse.questphase / h1359 / 12 |
| `q115_jungle_weyland_saved` | Producer outside selected context | q203_afterlife.questphase / h0 / 198; q203_afterlife.questphase / h16 / 40 |
| `q115_kerry_romance_chosen` | Producer outside selected context | q203_penthouse.questphase / h1261 / 23; q203_penthouse.questphase / h1359 / 9 |
| `q115_panam_romance_chosen` | Producer outside selected context | q203_penthouse.questphase / h1261 / 24; q203_penthouse.questphase / h1359 / 10 |
| `q115_river_romance_chosen` | Producer outside selected context | q203_penthouse.questphase / h1261 / 21; q203_penthouse.questphase / h1359 / 7 |
| `q203_05_cancel_lokat` | q203_05_afterlife.scene / scene / 1489 | q203_05_afterlife.scene / scene / 1488 |
| `q203_active` | q203_penthouse.questphase / h244 / 36 | mws_wat_02.questphase / h0 / 38; mws_wat_02.questphase / h20 / 19; q203_quest_bugfixes.questphase / h157 / 4 |
| `q203_coffee_empty` | q203_02b_kerry.scene / scene / 127 | No reader in selected context |
| `q203_coffee_made` | q203_02c_judy.scene / scene / 171; q203_03_sobchak.scene / scene / 254 | No reader in selected context |
| `q203_fact_afterlife_entered` | q203_afterlife.questphase / h0 / 218 | No reader in selected context |
| `q203_fact_alone` | q203_penthouse.questphase / h1261 / 20; q203_penthouse.questphase / h1359 / 11 | q203_04_delamain.scene / scene / 547; q203_delamain.questphase / h0 / 68; q203_penthouse.questphase / h7 / 83; q203_quest_bugfixes.questphase / h157 / 4 |
| `q203_fact_begin_emmerick_texting` | q203_04_delamain.scene / scene / 461 | q203_av_ride.questphase / h106 / 2 |
| `q203_fact_cosmos_begun` | q203_cosmos.questphase / h0 / 75 | No reader in selected context |
| `q203_fact_delamain_already_arrived` | q203_03_sobchak.scene / scene / 774 | No reader in selected context |
| `q203_fact_delamain_departs` | q203_delamain.questphase / h0 / 84 | No reader in selected context |
| `q203_fact_gear_gathered` | q203_delamain.questphase / h0 / 77 | q203_04_delamain.scene / scene / 199; q203_04_delamain.scene / scene / 202; q203_04_delamain.scene / scene / 44 |
| `q203_fact_lonely_shower` | q203_penthouse.questphase / h620 / 26 | q203_penthouse.questphase / h7 / 85 |
| `q203_fact_lover_says_goodbye` | q203_02c_judy.scene / scene / 249; q203_penthouse.questphase / h0 / 237; q203_penthouse.questphase / h1153 / 3; q203_penthouse.questphase / h1182 / 6; q203_penthouse.questphase / h1201 / 4; q203_penthouse.questphase / h1220 / 7 | q203_delamain.questphase / h0 / 57 |
| `q203_fact_open_inner_airlock` | q203_06_cosmos.scene / scene / 254 | q203_06_cosmos.scene / scene / 246 |
| `q203_fact_relationship_dialogue_over` | q203_02b_kerry.scene / scene / 665; q203_02d_panam.scene / scene / 735; q203_penthouse.questphase / h0 / 223 | q203_penthouse.questphase / h7 / 80 |
| `q203_fact_start_stanley` | q203_02_shower.scene / scene / 326; q203_02b_kerry.scene / scene / 231; q203_02c_judy.scene / scene / 393; q203_02d_panam.scene / scene / 982; q203_03_sobchak.scene / scene / 449; q203_03_sobchak.scene / scene / 520 | q203_penthouse.questphase / h1423 / 3; q203_penthouse.questphase / h1423 / 4 |
| `q203_prep_done` | q203_penthouse.questphase / h7 / 84 | q203_delamain.questphase / h152 / 2 |
| `q203_shower_done` | q203_02_shower.scene / scene / 441; q203_02c_judy.scene / scene / 503; q203_02d_panam.scene / scene / 324; q203_03_sobchak.scene / scene / 608 | No reader in selected context |
| `q203_started` | q203_penthouse.questphase / h244 / 37 | No reader in selected context |
| `q203_v_departs_with_delamain` | q203_04_delamain.scene / scene / 1201 | q203_delamain.questphase / h0 / 93; q203_delamain.questphase / h12 / 46 |
| `q305_johnny_scene_active` | Producer outside selected context | mws_wat_02.scene / scene / 672; mws_wat_02.scene / scene / 675 |
| `question_asked` | q203_04_delamain.scene / scene / 503; q203_04_delamain.scene / scene / 507; q203_04_delamain.scene / scene / 510 | q203_04_delamain.scene / scene / 512 |
| `radio_on` | q203_penthouse.questphase / h244 / 42 | No reader in selected context |
| `sq012_done` | Producer outside selected context | q203_penthouse.questphase / h374 / 11 |
| `sq024_claire_dead` | Producer outside selected context | q203_afterlife.questphase / h0 / 179; q203_afterlife.questphase / h16 / 36 |
| `sq024_claire_pissed` | Producer outside selected context | q203_afterlife.questphase / h0 / 183; q203_afterlife.questphase / h16 / 37 |
| `sq025_delamain_fate` | Producer outside selected context | q203_04_delamain.scene / scene / 1136; q203_04_delamain.scene / scene / 1138; q203_04_delamain.scene / scene / 1140; q203_04_delamain.scene / scene / 1142; q203_04_delamain.scene / scene / 212; q203_04_delamain.scene / scene / 213; q203_04_delamain.scene / scene / 217; q203_04_delamain.scene / scene / 251; q203_04_delamain.scene / scene / 252; q203_04_delamain.scene / scene / 263; q203_04_delamain.scene / scene / 264; q203_04_delamain.scene / scene / 373; q203_04_delamain.scene / scene / 374; q203_04_delamain.scene / scene / 422; q203_04_delamain.scene / scene / 423; q203_04_delamain.scene / scene / 622; q203_04_delamain.scene / scene / 627; q203_04_delamain.scene / scene / 628; q203_04_delamain.scene / scene / 633; q203_04_delamain.scene / scene / 634; q203_04_delamain.scene / scene / 639; q203_04_delamain.scene / scene / 640; q203_04_delamain.scene / scene / 645; q203_04_delamain.scene / scene / 646 |
| `sq026_done` | Producer outside selected context | q203_penthouse.questphase / h374 / 20 |
| `sq029_done` | Producer outside selected context | q203_penthouse.questphase / h374 / 16 |
| `sq031_rogue_met_johnny` | Producer outside selected context | q203_05_afterlife.scene / scene / 824 |
| `sq032_done` | Producer outside selected context | mws_wat_02.questphase / h20 / 38; mws_wat_02.scene / scene / 651; mws_wat_02.scene / scene / 654 |
| `travelling_merchant_lives` | Producer outside selected context | q203_quest_bugfixes.questphase / h0 / 20 |

## Exact gates, joins and cancellation

<details><summary>301 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mws_wat_02.questphase / h0 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mws_wat_02_tr_interior_v_room"}}` | 23:Out1 → 17:In; 56:Out → 17:In; 17:Out → 35:In; 17:Out → 20:In1 |
| `mws_wat_02.questphase / h0 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"93782953671","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 31:In; 31:Out → 56:In |
| `mws_wat_02.questphase / h0 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":90}}}` | 34:Out → 33:In; 35:Out → 34:In |
| `mws_wat_02.questphase / h0 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_02_egg_placed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 17:Out → 35:In; 35:Out → 34:In |
| `mws_wat_02.questphase / h0 / 38` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_active","value":1,"comparisonType":"GreaterOrEqual"}}}` | 33:Out → 38:In; 38:Out → 41:In |
| `mws_wat_02.questphase / h0 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_done"}}}` | 56:Out → 17:In; 31:Out → 56:In |
| `mws_wat_02.questphase / h20 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mws_wat_02_tr_interior_v_room"}}` | 12:Out → 10:In; 10:Out → 18:In |
| `mws_wat_02.questphase / h20 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 7:Out → 12:In; 12:Out → 10:In |
| `mws_wat_02.questphase / h20 / 17` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_02_iguana_hatched","value":1,"comparisonType":"GreaterOrEqual"}}}` | 17:False → 11:In; 17:True → 16:In; 38:False → 17:In; 37:Out → 17:In |
| `mws_wat_02.questphase / h20 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_active","value":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 19:In; 19:Out → 22:In |
| `mws_wat_02.questphase / h20 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_02_iguana_cat_together","value":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 27:In; 27:Out → 24:In |
| `mws_wat_02.questphase / h20 / 30` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_02_iguana_cat_together_active","value":1,"comparisonType":"GreaterOrEqual"}}}` | 7:Out → 30:In; 30:False → 15:mws_wat_02_in; 30:True → 31:mws_wat_02_iguana_cat_in |
| `mws_wat_02.questphase / h20 / 38` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_done"}}}` | 38:False → 17:In; 18:Out → 38:In; 38:True → 37:In |
| `mws_wat_02.questphase / h229 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_wat_02_q203_iguana"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 5:Out → 6:In; 6:Out → 7:mws_wat_02_q203_in |
| `mws_wat_02.questphase / h229 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/epilogues/q203_legend/penthouse/enter_delemain","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 5:Out → 13:In; 13:Out → 10:In |
| `mws_wat_02.scene / scene / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_wat_02_iguana"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 9:0:0 → 12:0:1; 12:0:0 → 101:0:1; 12:0:0 → 371:0:1; 12:0:0 → 537:0:0 |
| `mws_wat_02.scene / scene / 22` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 22:0:0 → 21:0:1; 174:0:0 → 22:0:1 |
| `mws_wat_02.scene / scene / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mws_wat_02_tr_interior_v_room"}}` | 35:0:0 → 38:0:1; 231:0:0 → 35:0:1 |
| `mws_wat_02.scene / scene / 57` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_02_egg_placed","value":1,"comparisonType":"GreaterOrEqual"}}}` | 57:0:0 → 231:0:1; 57:0:1 → 226:0:1; 61:0:1 → 57:0:1 |
| `mws_wat_02.scene / scene / 61` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_02_iguana_hatched","value":1,"comparisonType":"GreaterOrEqual"}}}` | 1:0:0 → 61:0:1; 61:0:0 → 38:0:1; 61:0:1 → 57:0:1 |
| `mws_wat_02.scene / scene / 101` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_02_iguana_reaction","value":1,"comparisonType":"GreaterOrEqual"}}}` | 12:0:0 → 101:0:1; 101:0:0 → 518:0:0; 101:0:1 → 194:0:1 |
| `mws_wat_02.scene / scene / 139` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 131:2:0 → 139:0:1; 139:0:0 → 109:0:1 |
| `mws_wat_02.scene / scene / 146` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mws_wat_02_Johnny"},"onScreenTest":true,"inverted":true}}}` | 146:0:0 → 163:0:1; 146:0:0 → 651:0:1; 258:0:0 → 146:0:1; 396:1:0 → 146:0:0 |
| `mws_wat_02.scene / scene / 147` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 111:0:0 → 147:0:1; 147:0:0 → 242:0:1; 147:0:0 → 263:0:0 |
| `mws_wat_02.scene / scene / 165` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mws_wat_02_Johnny"},"onScreenTest":true,"inverted":true}}}` | 165:0:0 → 169:0:1; 165:0:0 → 654:0:1; 167:0:0 → 165:0:1; 391:1:0 → 165:0:0 |
| `mws_wat_02.scene / scene / 167` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 98:0:0 → 167:0:1; 167:0:0 → 165:0:1; 167:0:0 → 518:0:0 |
| `mws_wat_02.scene / scene / 194` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mws_wat_02_iguana"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"LessOrEqual"}}}` | 101:0:1 → 194:0:1; 194:0:0 → 396:0:0; 194:0:0 → 638:0:1; 678:0:0 → 194:0:1 |
| `mws_wat_02.scene / scene / 231` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_02_iguana_hatched","value":1,"comparisonType":"GreaterOrEqual"}}}` | 45:0:0 → 231:0:1; 57:0:0 → 231:0:1; 231:0:0 → 35:0:1 |
| `mws_wat_02.scene / scene / 247` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 242:0:0 → 247:0:1; 247:0:0 → 256:0:1 |
| `mws_wat_02.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":500}}}` | 109:0:0 → 251:0:1; 251:0:0 → 244:0:1 |
| `mws_wat_02.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 256:0:0 → 258:0:1; 258:0:0 → 146:0:1 |
| `mws_wat_02.scene / scene / 284` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 284:0:0 → 271:0:0; 510:0:0 → 284:0:1 |
| `mws_wat_02.scene / scene / 426` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 426:0:0 → 405:0:0; 426:0:0 → 432:0:1; 448:0:0 → 426:0:1 |
| `mws_wat_02.scene / scene / 432` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 426:0:0 → 432:0:1; 432:0:0 → 430:0:1 |
| `mws_wat_02.scene / scene / 444` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_02_johnny_plays","value":1,"comparisonType":"GreaterOrEqual"}}}` | 391:0:0 → 444:0:1; 444:0:1 → 437:0:1 |
| `mws_wat_02.scene / scene / 451` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 437:0:0 → 451:0:1; 451:0:0 → 448:0:1 |
| `mws_wat_02.scene / scene / 553` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mws_wat_02_iguana_petted","value":1,"comparisonType":"GreaterOrEqual"}}}` | 553:0:0 → 341:0:0; 553:0:1 → 551:0:1; 663:0:0 → 553:0:1 |
| `mws_wat_02.scene / scene / 563` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_wat_02_iguana_puff"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 561:0:0 → 563:0:1; 563:0:0 → 566:0:1; 563:0:0 → 584:0:0 |
| `mws_wat_02.scene / scene / 574` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q003_nibbles","names":["Nibbles"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 573:0:0 → 574:0:1; 574:0:0 → 578:0:1; 574:0:0 → 584:0:1 |
| `mws_wat_02.scene / scene / 604` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mws_wat_02_iguana_puff"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}},{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q003_nibbles","names":["Nibbles"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}]}}` | 584:0:0 → 604:0:1; 604:0:0 → 601:0:1 |
| `mws_wat_02.scene / scene / 612` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mws_wat_02_iguana_puff"},"onScreenTest":true}}}` | 607:0:0 → 612:0:1; 612:0:0 → 614:0:0 |
| `mws_wat_02.scene / scene / 617` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q003_nibbles","names":["Nibbles"]},"onScreenTest":true}}}` | 607:0:0 → 617:0:1; 617:0:0 → 614:0:1 |
| `mws_wat_02.scene / scene / 651` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_done"}}}` | 146:0:0 → 651:0:1; 651:0:0 → 635:0:1 |
| `mws_wat_02.scene / scene / 654` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq032_done"}}}` | 165:0:0 → 654:0:1; 654:0:0 → 643:0:1 |
| `mws_wat_02.scene / scene / 672` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q305_johnny_scene_active","comparisonType":"Equal"}}}` | 396:0:0 → 672:0:1; 672:0:0 → 131:0:0; 672:0:1 → 675:0:1 |
| `mws_wat_02.scene / scene / 675` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q305_johnny_scene_active","comparisonType":"Equal"}}}` | 672:0:1 → 675:0:1; 675:0:0 → 678:0:1 |
| `mws_wat_02.scene / scene / 678` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 675:0:0 → 678:0:1; 678:0:0 → 194:0:1 |
| `q203_quest_bugfixes.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 22:Out1 → 20:In |
| `q203_quest_bugfixes.questphase / h28 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/epilogues/q203_legend","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}}` | 0:Out → 4:In; 4:True → 2:In; 4:False → 6:In |
| `q203_quest_bugfixes.questphase / h96 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/epilogues/q203_legend/cosmos/activate_autopilot","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/epilogues/q203_legend","fileEntryIndex":3,"className":"gameJournalQuest"},"state":"Active"}}]}}` | 0:Out → 4:In; 4:True → 13:In; 4:False → 14:In2 |
| `q203_quest_bugfixes.questphase / h157 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CP77-55455","value":1,"comparisonType":"Less"}}}` | 0:Out → 2:In; 2:True → 3:In |
| `q203_quest_bugfixes.questphase / h157 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_active"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_alone"}}]}}` | 3:Out → 4:In; 4:Out → 11:In; 4:Out → 12:In; 4:Out → 13:In; 4:Out → 14:In; 4:Out → 16:In |
| `q203_quest_bugfixes.questphase / h157 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q005_com_afterlife_community","names":["merc_01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 4:Out → 11:In; 11:Out → 6:In |
| `q203_quest_bugfixes.questphase / h157 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q005_com_afterlife_community","names":["merc_02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 4:Out → 12:In; 12:Out → 8:In |
| `q203_quest_bugfixes.questphase / h157 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q005_com_afterlife_community","names":["merc_03"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 4:Out → 13:In; 13:Out → 9:In |
| `q203_quest_bugfixes.questphase / h157 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q005_com_afterlife_community","names":["merc_04"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 4:Out → 14:In; 14:Out → 10:In |
| `q203_quest_bugfixes.questphase / h157 / 16` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q005_com_afterlife_community","names":["walker_03"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 4:Out → 16:In; 16:Out → 15:In |
| `q203_afterlife.questphase / h0 / 148` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_afterlife_entrance"}}` | 7:Out1 → 148:In; 148:Out → 133:In; 148:Out → 199:In; 148:Out → 206:In; 148:Out → 213:In1; 148:Out → 216:In |
| `q203_afterlife.questphase / h0 / 149` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_emmerick_talk"}}` | 18:Out → 149:In; 149:Out → 135:q203_05_afterlife_booth_in; 149:Out → 180:Succeeded; 149:Out → 192:In; 149:Out → 200:In; 149:Out → 204:In; 149:Out → 211:In; 149:Out → 218:In |
| `q203_afterlife.questphase / h0 / 152` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_05_tr_claire_welcome"}}` | 183:False → 152:In; 152:Out → 153:q203_05_claire_drink_in |
| `q203_afterlife.questphase / h0 / 163` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 163:Out → 161:In; 217:Out → 163:In |
| `q203_afterlife.questphase / h0 / 179` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq024_claire_dead"}}}` | 204:False → 179:In; 179:False → 183:In |
| `q203_afterlife.questphase / h0 / 182` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 161:Out → 182:In; 182:Out → 173:In |
| `q203_afterlife.questphase / h0 / 183` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq024_claire_pissed"}}}` | 183:False → 152:In; 179:False → 183:In |
| `q203_afterlife.questphase / h0 / 198` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_jungle_weyland_saved"}}}` | 198:True → 196:q203_05_weyland_IN; 206:False → 198:In |
| `q203_afterlife.questphase / h0 / 201` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 201:Out → 151:In; 200:Out → 201:In |
| `q203_afterlife.questphase / h0 / 204` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_did_it_solo"}}}` | 149:Out → 204:In; 204:False → 179:In; 204:True → 205:Rogue_start |
| `q203_afterlife.questphase / h0 / 206` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_did_it_solo"}}}` | 148:Out → 206:In; 206:True → 196:Weyland_Rogue; 206:False → 198:In |
| `q203_afterlife.questphase / h0 / 209` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_enter_elevator_top"}}` | 7:Out1 → 209:In; 209:Out → 207:q203_04_delemain_leaves_IN |
| `q203_afterlife.questphase / h16 / 36` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq024_claire_dead"}}}` | 0:Out → 36:In; 36:False → 37:In |
| `q203_afterlife.questphase / h16 / 37` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq024_claire_pissed"}}}` | 37:False → 31:In; 36:False → 37:In |
| `q203_afterlife.questphase / h16 / 40` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_jungle_weyland_saved"}}}` | 0:Out → 40:In; 40:True → 41:In |
| `q203_afterlife.questphase / h16 / 44` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_did_it_solo"}}}` | 0:Out → 44:In; 44:True → 45:In |
| `q203_afterlife.questphase / h351 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_enter_elevator_top"}}` | 0:Out → 2:In; 2:Out → 3:Inactive |
| `q203_afterlife.questphase / h351 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_emmerick_talk"}}` | 8:Out → 9:In; 9:Out → 10:Inactive |
| `q203_afterlife.questphase / h351 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q115_afterlife_lift","deviceControllerClass":"LiftControllerPS","deviceConditionFunction":"IsFloorSelected","functionParameters":[{"$type":"questDevice_ConditionFunctionParameter","name":"floor","value":{"$type":"Variant","$rawData":"ZAAIAAAAAAAAAA=="}}]}}}` | 4:Out → 12:In; 12:Out → 7:Inactive; 12:Out → 14:In |
| `q203_afterlife.questphase / h424 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"#q103_dvc_door_afterlife_main"}}` | 0:Out → 3:In; 3:Out → 4:In |
| `q203_afterlife.questphase / h424 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 5:Out → 2:In; 4:Out → 5:In |
| `q203_afterlife.questphase / h424 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"#q115_dvc_door_afterlife_front"}}` | 0:Out → 7:In; 7:Out → 8:In |
| `q203_afterlife.questphase / h424 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 9:Out → 6:In; 8:Out → 9:In |
| `q203_afterlife.questphase / h424 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"#q103_dvc_door_afterlife_bar_right"}}` | 0:Out → 11:In; 11:Out → 10:In |
| `q203_afterlife.questphase / h424 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 10:Out → 13:In; 13:Out → 12:In |
| `q203_afterlife.questphase / h424 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"#q103_dvc_door_afterlife_bar_left"}}` | 0:Out → 15:In; 15:Out → 14:In |
| `q203_afterlife.questphase / h424 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 14:Out → 17:In; 17:Out → 16:In |
| `q203_afterlife.questphase / h424 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questNodeLoadingCondition","objectRef":"#q103_dvc_door_afterlife_bar_double"}}` | 0:Out → 19:In; 19:Out → 18:In |
| `q203_afterlife.questphase / h424 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 18:Out → 21:In; 21:Out → 20:In |
| `q203_av_ride.questphase / h0 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_afterlife_landing_pad"}}` | 41:Out → 12:In; 12:Out → 15:In; 12:Out → 35:In |
| `q203_av_ride.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#delamain_vehicle","names":["delamain_av"]},"childIsPlayer":true,"condition":"OnUnmount"}}}` | 21:Out → 20:In; 20:Out → 23:In |
| `q203_av_ride.questphase / h0 / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 23:Out → 19:In; 20:Out → 23:In |
| `q203_av_ride.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 15:Out → 27:In; 27:Out → 26:In |
| `q203_av_ride.questphase / h106 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_begin_emmerick_texting"}}}` | 0:Out → 2:In; 2:Out → 3:Active |
| `q203_av_ride.questphase / h106 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 3:Out → 4:In; 4:Out → 5:Active |
| `q203_av_ride.questphase / h106 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 5:Out → 6:In; 6:Out → 7:Active |
| `q203_av_ride.questphase / h106 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/emmerick/q203_taxi_ride/03_ch_delamain_ride/03a_ch_delamain_ride","fileEntryIndex":1,"className":"gameJournalPhoneChoiceEntry"},"state":"Succeeded"}}}` | 8:Out → 9:In; 9:Out → 11:In |
| `q203_av_ride.questphase / h106 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 9:Out → 11:In; 11:Out → 10:Active |
| `q203_cosmos.questphase / h0 / 83` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 89:Out → 83:In; 83:Out → 85:In; 83:Out → 87:In |
| `q203_cosmos.questphase / h0 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3,"miliseconds":500}}}` | 83:Out → 87:In; 87:Out → 91:In |
| `q203_cosmos.questphase / h51 / 21` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"156398579661","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 12:Out → 21:In; 21:Out → 15:In |
| `q203_delamain.questphase / h0 / 55` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/epilogues/q203_legend/penthouse/get_dressed","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 55:Out → 49:Active; 80:Out1 → 55:In |
| `q203_delamain.questphase / h0 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_lover_says_goodbye"}}}` | 68:False → 57:In; 57:Out → 80:In1; 57:Out → 92:In |
| `q203_delamain.questphase / h0 / 67` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_penthouse_garage"}}` | 67:Out → 44:q203_04_delemain_in; 80:Out1 → 67:In; 67:Out → 84:In |
| `q203_delamain.questphase / h0 / 68` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_alone"}}}` | 0:Out → 68:In; 68:False → 57:In; 68:True → 76:Active |
| `q203_delamain.questphase / h0 / 89` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_delamain_squash","activatorRef":{"$type":"gameEntityReference","reference":"#delamain_vehicle"},"isPlayerActivator":false}}` | 94:CutSource → 89:CutDestination; 92:Out → 89:In; 89:Out → 90:In |
| `q203_delamain.questphase / h0 / 90` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_delamain_squash"}}` | 89:Out → 90:In; 94:CutSource → 90:CutDestination; 90:True → 91:In |
| `q203_delamain.questphase / h0 / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_v_departs_with_delamain"}}}` | 92:Out → 93:In; 93:Out → 94:In |
| `q203_delamain.questphase / h0 / 94` | `questCutControlNodeDefinition` `{"permanent":true}` | 94:CutSource → 89:CutDestination; 94:CutSource → 90:CutDestination; 94:CutSource → 91:CutDestination; 93:Out → 94:In |
| `q203_delamain.questphase / h12 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_delamain_squash","activatorRef":{"$type":"gameEntityReference","reference":"#delamain_vehicle"},"isPlayerActivator":false}}` | 47:CutSource → 42:CutDestination; 45:Out → 42:In; 42:Out → 43:In |
| `q203_delamain.questphase / h12 / 43` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_delamain_squash"}}` | 42:Out → 43:In; 47:CutSource → 43:CutDestination; 43:True → 44:In |
| `q203_delamain.questphase / h12 / 46` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_v_departs_with_delamain"}}}` | 45:Out → 46:In; 46:Out → 47:In |
| `q203_delamain.questphase / h12 / 47` | `questCutControlNodeDefinition` `{"permanent":true}` | 47:CutSource → 42:CutDestination; 47:CutSource → 43:CutDestination; 47:CutSource → 44:CutDestination; 46:Out → 47:In |
| `q203_delamain.questphase / h152 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_prep_done"}}}` | 0:Out → 2:In; 2:Out → 1:In |
| `q203_penthouse.questphase / h0 / 195` | `questLogicalXorNodeDefinition` `{"inputSocketCount":5}` | 220:Out1 → 195:In1; 221:Out1 → 195:In2; 222:Out1 → 195:In3; 227:Out1 → 195:In4; 219:Out1 → 195:In5; 195:Out1 → 224:In |
| `q203_penthouse.questphase / h7 / 80` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_relationship_dialogue_over"}}}` | 0:Out → 80:In; 80:Out → 105:In2 |
| `q203_penthouse.questphase / h7 / 83` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_alone"}}}` | 0:Out → 83:In; 83:Out → 85:In |
| `q203_penthouse.questphase / h7 / 85` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_lonely_shower"}}}` | 83:Out → 85:In; 85:Out → 105:In1 |
| `q203_penthouse.questphase / h7 / 105` | `questLogicalXorNodeDefinition` `{}` | 80:Out → 105:In2; 85:Out → 105:In1; 105:Out1 → 115:In |
| `q203_penthouse.questphase / h7 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"112185654454","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 28:Out → 107:In; 107:Out → 146:In |
| `q203_penthouse.questphase / h7 / 115` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"115569420103","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 115:False → 28:Active; 105:Out1 → 115:In; 115:True → 135:Active |
| `q203_penthouse.questphase / h7 / 134` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 135:Out → 134:In; 134:Out → 136:Succeeded |
| `q203_penthouse.questphase / h244 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 56:Out → 21:In1; 25:Out → 56:In |
| `q203_penthouse.questphase / h374 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterLifePath_ConditionType","lifePathID":"83635443133"}}}` | 0:Out → 2:In; 2:True → 3:In; 2:False → 4:In |
| `q203_penthouse.questphase / h374 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterLifePath_ConditionType","lifePathID":"67091901544"}}}` | 2:False → 4:In; 4:True → 5:In; 4:False → 6:In |
| `q203_penthouse.questphase / h374 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterLifePath_ConditionType","lifePathID":"83574632792"}}}` | 4:False → 6:In; 6:True → 7:In; 6:False → 8:In1 |
| `q203_penthouse.questphase / h374 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq033_done"}}}` | 24:False → 9:In; 25:Out → 9:In; 9:True → 10:In; 9:False → 11:In |
| `q203_penthouse.questphase / h374 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq012_done"}}}` | 9:False → 11:In; 10:Out → 11:In; 11:True → 12:In; 11:False → 14:In |
| `q203_penthouse.questphase / h374 / 14` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq001_done"}}}` | 11:False → 14:In; 12:Out → 14:In; 14:True → 15:In; 14:False → 16:In |
| `q203_penthouse.questphase / h374 / 16` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq029_done"}}}` | 14:False → 16:In; 15:Out → 16:In; 16:True → 17:In; 16:False → 18:In |
| `q203_penthouse.questphase / h374 / 18` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq014_altar_looted"}}}` | 16:False → 18:In; 17:Out → 18:In; 18:True → 19:In; 18:False → 20:In |
| `q203_penthouse.questphase / h374 / 20` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq026_done"}}}` | 18:False → 20:In; 19:Out → 20:In; 20:True → 21:In; 20:False → 22:In |
| `q203_penthouse.questphase / h374 / 22` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq019_done"}}}` | 22:False → 13:In1; 20:False → 22:In; 21:Out → 22:In; 22:True → 23:In |
| `q203_penthouse.questphase / h374 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq003_done"}}}` | 8:Out1 → 24:In; 24:False → 9:In; 24:True → 25:In |
| `q203_penthouse.questphase / h719 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sobchak"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 18:Out → 19:In; 19:Out → 24:In |
| `q203_penthouse.questphase / h828 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#judy"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 11:Out → 12:In; 12:Out → 15:In |
| `q203_penthouse.questphase / h941 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 11:Out → 12:In; 12:Out → 16:In |
| `q203_penthouse.questphase / h1153 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 0:Out → 4:In; 4:Out → 3:In |
| `q203_penthouse.questphase / h1182 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 0:Out → 7:In; 7:Out → 6:In |
| `q203_penthouse.questphase / h1201 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 0:Out → 5:In; 5:Out → 4:In |
| `q203_penthouse.questphase / h1220 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 0:Out → 6:In; 6:Out → 7:In |
| `q203_penthouse.questphase / h1220 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 19:Out → 18:panam_farewell_interaction |
| `q203_penthouse.questphase / h1261 / 21` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_river_romance_chosen"}}}` | 21:True → 15:In; 19:Out → 21:In; 21:False → 22:In |
| `q203_penthouse.questphase / h1261 / 22` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_judy_romance_chosen"}}}` | 22:True → 16:In; 21:False → 22:In; 22:False → 23:In |
| `q203_penthouse.questphase / h1261 / 23` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_kerry_romance_chosen"}}}` | 23:True → 17:In; 22:False → 23:In; 23:False → 24:In |
| `q203_penthouse.questphase / h1261 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_panam_romance_chosen"}}}` | 24:True → 18:In; 24:False → 20:In; 23:False → 24:In |
| `q203_penthouse.questphase / h1359 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_river_romance_chosen"}}}` | 0:Out → 7:In; 7:True → 1:In; 7:False → 12:In |
| `q203_penthouse.questphase / h1359 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_kerry_romance_chosen"}}}` | 9:True → 3:In; 12:False → 9:In; 9:False → 10:In |
| `q203_penthouse.questphase / h1359 / 10` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_panam_romance_chosen"}}}` | 10:True → 4:In; 9:False → 10:In; 10:False → 11:In |
| `q203_penthouse.questphase / h1359 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q115_judy_romance_chosen"}}}` | 12:True → 2:In; 7:False → 12:In; 12:False → 9:In |
| `q203_penthouse.questphase / h1423 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_start_stanley"}}}` | 0:Out → 3:In; 3:Out → 4:In; 3:Out → 6:In; 3:Out → 16:In |
| `q203_penthouse.questphase / h1423 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_start_stanley","comparisonType":"Equal"}}}` | 3:Out → 4:In; 4:Out → 19:In |
| `q203_penthouse.questphase / h1423 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 17:Out → 12:In; 52:Out → 17:In; 17:Out → 40:In1 |
| `q203_penthouse.questphase / h1423 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 40:Out1 → 42:In; 42:Out → 41:In1 |
| `q203_penthouse.questphase / h1423 / 43` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":50}}}` | 43:Out → 40:In1; 41:Out1 → 43:In |
| `q203_penthouse.questphase / h1423 / 54` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 23:Out → 54:In; 54:Out → 51:In |
| `q203_penthouse.questphase / h1509 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q203_dvc_bedside_radio","deviceControllerClass":"RadioControllerPS","deviceConditionFunction":"IsOFF"}}}` | 0:Out → 2:In; 2:Out → 5:In1 |
| `q203_penthouse.questphase / h1509 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q203_dvc_shower_radio","deviceControllerClass":"RadioControllerPS","deviceConditionFunction":"IsOFF"}}}` | 0:Out → 3:In; 3:Out → 5:In2 |
| `q203_penthouse.questphase / h1509 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q203_dvc_kitchen_radio","deviceControllerClass":"RadioControllerPS","deviceConditionFunction":"IsOFF"}}}` | 0:Out → 4:In; 4:Out → 5:In3 |
| `q203_penthouse.questphase / h1509 / 5` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 2:Out → 5:In1; 3:Out → 5:In2; 4:Out → 5:In3; 5:Out1 → 6:In |
| `q203_penthouse.questphase / h1573 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q203_dvc_bedside_radio","deviceControllerClass":"RadioControllerPS","deviceConditionFunction":"IsON"}}}` | 0:Out → 2:In; 2:Out → 5:In1 |
| `q203_penthouse.questphase / h1573 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q203_dvc_shower_radio","deviceControllerClass":"RadioControllerPS","deviceConditionFunction":"IsON"}}}` | 0:Out → 3:In; 3:Out → 5:In2 |
| `q203_penthouse.questphase / h1573 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q203_dvc_kitchen_radio","deviceControllerClass":"RadioControllerPS","deviceConditionFunction":"IsON"}}}` | 0:Out → 4:In; 4:Out → 5:In3 |
| `q203_penthouse.questphase / h1573 / 5` | `questLogicalXorNodeDefinition` `{"inputSocketCount":3}` | 2:Out → 5:In1; 3:Out → 5:In2; 4:Out → 5:In3; 5:Out1 → 6:In |
| `q203_penthouse.questphase / h1685 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 0:Out → 3:In; 3:Out → 2:q203_04_emmerick_calls_IN |
| `q203_penthouse.questphase / h1718 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInteraction_ConditionType","objectRef":"#q203_clothes_container","eventType":"Executed"}}}` | 4:Out → 9:In; 9:Out → 6:In |
| `q203_penthouse.questphase / h1718 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 14:Out → 12:In; 12:Out → 16:In |
| `q203_02_shower.scene / scene / 379` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_shower_radio"}}` | 350:0:0 → 379:0:1; 379:0:0 → 309:0:0 |
| `q203_02_shower.scene / scene / 449` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 397:0:0 → 449:0:1; 449:0:0 → 385:0:0 |
| `q203_02_shower.scene / scene / 4413` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 4411:0:0 → 4413:0:1; 4413:0:0 → 4415:0:1 |
| `q203_02b_kerry.scene / scene / 95` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_penthouse_balcony"}}` | 95:0:0 → 319:0:0; 95:0:0 → 572:0:1; 576:0:0 → 95:0:1 |
| `q203_02b_kerry.scene / scene / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_terrace"}}` | 96:0:0 → 10:0:0; 454:0:0 → 96:0:1 |
| `q203_02b_kerry.scene / scene / 215` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 214:0:0 → 215:0:1; 215:0:0 → 297:0:0 |
| `q203_02b_kerry.scene / scene / 290` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_shower_radio"}}` | 290:0:0 → 213:0:0; 828:0:0 → 290:0:1 |
| `q203_02b_kerry.scene / scene / 345` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#delamain_vehicle","names":["delamain_av"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 343:0:0 → 345:0:1; 345:0:0 → 544:0:1; 345:0:0 → 570:0:0 |
| `q203_02b_kerry.scene / scene / 451` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_kerry_kitchen"}}` | 451:0:0 → 44:0:0; 684:0:0 → 451:0:1 |
| `q203_02b_kerry.scene / scene / 475` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 467:0:0 → 475:0:1; 475:0:0 → 469:0:1 |
| `q203_02b_kerry.scene / scene / 478` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 469:0:0 → 478:0:1; 478:0:0 → 470:0:1 |
| `q203_02b_kerry.scene / scene / 481` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 470:0:0 → 481:0:1; 481:0:0 → 471:0:1 |
| `q203_02b_kerry.scene / scene / 581` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 319:0:0 → 581:0:1; 581:0:0 → 467:0:1 |
| `q203_02b_kerry.scene / scene / 632` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"onScreenTest":true}}}` | 320:2:0 → 632:0:1; 632:0:0 → 631:0:0; 635:0:0 → 632:0:1; 648:1:0 → 632:0:0; 648:1:0 → 632:1026:0 |
| `q203_02b_kerry.scene / scene / 633` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"onScreenTest":true,"inverted":true}}}` | 631:0:0 → 633:0:1; 633:0:0 → 634:0:0; 648:1:0 → 633:0:0; 648:1:0 → 633:1026:0 |
| `q203_02b_kerry.scene / scene / 839` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_kerry_notice"}}` | 300:0:0 → 839:0:1; 839:0:0 → 684:0:0 |
| `q203_02b_kerry.scene / scene / 925` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 925:0:0 → 920:0:0; 926:0:0 → 925:0:1 |
| `q203_02b_kerry.scene / scene / 926` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6}}}` | 40:0:0 → 926:0:1; 200:0:0 → 926:0:1; 680:0:0 → 926:0:1; 682:0:0 → 926:0:1; 926:0:0 → 925:0:1 |
| `q203_02b_kerry.scene / scene / 2231` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":56}}}` | 2228:0:0 → 2231:0:1; 2231:0:0 → 2233:0:1 |
| `q203_02b_kerry.scene / scene / 2243` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 420:0:0 → 2243:0:1; 2243:0:0 → 2241:0:1 |
| `q203_02b_kerry.scene / scene / 2249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#kerry","names":["kerry"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 213:0:0 → 2249:0:1; 2249:0:0 → 2247:0:1 |
| `q203_02c_judy.scene / scene / 128` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_terrace"}}` | 128:0:0 → 667:0:0; 350:0:0 → 128:0:1 |
| `q203_02c_judy.scene / scene / 313` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_penthouse_kitchen"}}` | 313:0:0 → 303:0:0; 329:0:0 → 313:0:1 |
| `q203_02c_judy.scene / scene / 477` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 469:0:0 → 477:0:1; 477:0:0 → 468:0:0 |
| `q203_02c_judy.scene / scene / 678` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_judy_coffe"}}` | 497:0:0 → 678:0:1; 678:0:0 → 329:0:0 |
| `q203_02c_judy.scene / scene / 738` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 736:0:0 → 738:0:1; 738:0:0 → 870:0:1; 738:0:0 → 914:0:0 |
| `q203_02c_judy.scene / scene / 894` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 113:0:0 → 894:0:1; 894:0:0 → 1318:0:1 |
| `q203_02c_judy.scene / scene / 932` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#judy","names":["judy"]},"timeInterval":0.30000001192092896,"onScreenTest":true}}}` | 15:2:0 → 932:0:1; 932:0:0 → 930:0:0; 940:0:0 → 932:0:1; 1251:1:0 → 932:0:0; 1251:1:0 → 932:1026:0 |
| `q203_02c_judy.scene / scene / 935` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#judy","names":["judy"]},"timeInterval":0.30000001192092896,"onScreenTest":true,"inverted":true}}}` | 930:0:0 → 935:0:1; 935:0:0 → 938:0:0; 1251:1:0 → 935:0:0; 1251:1:0 → 935:1026:0 |
| `q203_02c_judy.scene / scene / 1240` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":6}}}` | 964:0:0 → 1240:0:1; 1240:0:0 → 1241:0:1 |
| `q203_02c_judy.scene / scene / 1241` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#judy","names":["judy"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"LessOrEqual"}}}` | 1240:0:0 → 1241:0:1; 1241:0:0 → 1236:0:0 |
| `q203_02c_judy.scene / scene / 1318` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#judy","names":["judy"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 894:0:0 → 1318:0:1; 1318:0:0 → 461:0:1 |
| `q203_02d_panam.scene / scene / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_enter_shower"}}` | 17:0:0 → 185:0:0; 17:0:0 → 652:0:1; 213:0:0 → 17:0:1 |
| `q203_02d_panam.scene / scene / 53` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_penthouse_kitchen"}}` | 53:0:0 → 253:0:0; 256:0:0 → 53:0:1 |
| `q203_02d_panam.scene / scene / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_terrace","activatorRef":{"$type":"gameEntityReference","reference":"#panam","names":["panam"]}}}` | 61:0:0 → 315:0:0; 263:0:0 → 61:0:1 |
| `q203_02d_panam.scene / scene / 232` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 221:0:0 → 232:0:1; 232:0:0 → 215:0:0 |
| `q203_02d_panam.scene / scene / 309` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_judy_coffe"}}` | 288:0:0 → 309:0:1; 309:0:0 → 256:0:0 |
| `q203_02d_panam.scene / scene / 326` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 199:0:0 → 326:0:1; 326:0:0 → 287:0:0 |
| `q203_02d_panam.scene / scene / 442` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 440:0:0 → 442:0:1; 442:0:0 → 611:0:0 |
| `q203_02d_panam.scene / scene / 471` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#panam","names":["panam"]},"comparisonParams":{"$type":"questComparisonParam"}}}}` | 469:0:0 → 471:0:1; 471:0:0 → 464:0:1 |
| `q203_02d_panam.scene / scene / 652` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_02d_tr_panam_shower"}}` | 17:0:0 → 652:0:1; 652:0:0 → 2221:0:0; 718:1:0 → 652:0:0 |
| `q203_02d_panam.scene / scene / 671` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 315:0:0 → 671:0:1; 671:0:0 → 50:0:0 |
| `q203_02d_panam.scene / scene / 696` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#panam","names":["panam"]},"onScreenTest":true}}}` | 312:2:0 → 696:0:1; 696:0:0 → 695:0:0; 699:0:0 → 696:0:1; 706:1:0 → 696:0:0; 706:1:0 → 696:1026:0 |
| `q203_02d_panam.scene / scene / 697` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#panam","names":["panam"]},"onScreenTest":true,"inverted":true}}}` | 695:0:0 → 697:0:1; 697:0:0 → 698:0:0; 706:1:0 → 697:0:0; 706:1:0 → 697:1026:0 |
| `q203_02d_panam.scene / scene / 914` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":13}}}` | 132:0:0 → 914:0:1; 137:0:0 → 914:0:1; 914:0:0 → 915:0:1 |
| `q203_02d_panam.scene / scene / 915` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#panam","names":["panam"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"LessOrEqual"}}}` | 914:0:0 → 915:0:1; 915:0:0 → 751:0:0 |
| `q203_03_sobchak.scene / scene / 209` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_terrace"}}` | 209:0:0 → 208:0:3; 209:0:0 → 276:0:0; 209:0:0 → 719:0:0; 569:0:0 → 209:0:1 |
| `q203_03_sobchak.scene / scene / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_03_tr_river_coffe_start"}}` | 151:0:0 → 256:0:1; 256:0:0 → 150:0:0 |
| `q203_03_sobchak.scene / scene / 499` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 433:0:0 → 499:0:1; 499:0:0 → 495:1:0; 499:0:0 → 501:0:0; 1065:1:0 → 499:0:0 |
| `q203_03_sobchak.scene / scene / 618` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#delamain_vehicle","names":["delamain_av"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 618:0:0 → 774:0:1; 618:0:0 → 776:0:1; 619:0:0 → 618:0:1 |
| `q203_03_sobchak.scene / scene / 668` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/epilogues/q203_legend/penthouse/grab_coffee","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 218:0:0 → 668:0:1; 668:0:0 → 670:0:2; 668:0:1 → 703:0:0 |
| `q203_03_sobchak.scene / scene / 871` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sobchak"},"timeInterval":0.25,"onScreenTest":true}}}` | 721:2:0 → 871:0:1; 871:0:0 → 870:0:0; 874:0:0 → 871:0:1 |
| `q203_03_sobchak.scene / scene / 872` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sobchak"},"timeInterval":0.25,"onScreenTest":true,"inverted":true}}}` | 870:0:0 → 872:0:1; 872:0:0 → 873:0:0 |
| `q203_03_sobchak.scene / scene / 900` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 501:0:0 → 900:0:1; 900:0:0 → 492:0:0 |
| `q203_03_sobchak.scene / scene / 1162` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_kerry_kitchen"}}` | 1157:0:0 → 1162:0:1; 1162:0:0 → 87:0:0 |
| `q203_03_sobchak.scene / scene / 1241` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":15}}}` | 782:0:0 → 1241:0:1; 1241:0:0 → 1242:0:1 |
| `q203_03_sobchak.scene / scene / 1242` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#sobchak"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"LessOrEqual"}}}` | 1241:0:0 → 1242:0:1; 1242:0:0 → 1240:0:0 |
| `q203_04_delamain.scene / scene / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_av_arrive_afterlife"}}` | 81:0:0 → 103:0:1; 103:0:0 → 485:1:0; 103:0:0 → 665:0:1; 103:0:0 → 1179:0:1 |
| `q203_04_delamain.scene / scene / 199` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_gear_gathered"}}}` | 199:0:0 → 44:0:0; 202:0:1 → 199:0:1 |
| `q203_04_delamain.scene / scene / 202` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_gear_gathered"}}}` | 202:0:0 → 205:0:1; 202:0:1 → 199:0:1; 420:0:0 → 202:0:1; 421:0:0 → 202:0:1; 425:0:0 → 202:0:1 |
| `q203_04_delamain.scene / scene / 205` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 202:0:0 → 205:0:1; 205:0:0 → 44:0:0 |
| `q203_04_delamain.scene / scene / 208` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/epilogues/q203_legend/penthouse/put_on_clothes","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 44:0:0 → 208:0:1; 208:0:0 → 210:0:4 |
| `q203_04_delamain.scene / scene / 212` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","comparisonType":"Equal"}}}` | 81:0:0 → 212:0:1; 212:0:0 → 87:0:0; 212:0:1 → 213:0:1 |
| `q203_04_delamain.scene / scene / 213` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":1,"comparisonType":"Equal"}}}` | 212:0:1 → 213:0:1; 213:0:0 → 146:0:0; 213:0:1 → 622:0:1 |
| `q203_04_delamain.scene / scene / 217` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":3,"comparisonType":"Equal"}}}` | 217:0:0 → 146:0:0; 622:0:1 → 217:0:1 |
| `q203_04_delamain.scene / scene / 251` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","comparisonType":"Equal"}}}` | 251:0:0 → 105:0:0; 251:0:1 → 252:0:1; 512:0:1 → 251:0:1 |
| `q203_04_delamain.scene / scene / 252` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":1,"comparisonType":"Equal"}}}` | 251:0:1 → 252:0:1; 252:0:0 → 152:0:0; 252:0:1 → 628:0:1 |
| `q203_04_delamain.scene / scene / 263` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","comparisonType":"Equal"}}}` | 263:0:0 → 37:0:0; 263:0:1 → 264:0:1; 696:0:0 → 263:0:1 |
| `q203_04_delamain.scene / scene / 264` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":1,"comparisonType":"Equal"}}}` | 263:0:1 → 264:0:1; 264:0:0 → 158:0:0; 264:0:1 → 640:0:1 |
| `q203_04_delamain.scene / scene / 373` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","comparisonType":"Equal"}}}` | 77:0:0 → 373:0:1; 373:0:0 → 371:0:0; 373:0:1 → 374:0:1 |
| `q203_04_delamain.scene / scene / 374` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":1,"comparisonType":"Equal"}}}` | 373:0:1 → 374:0:1; 374:0:0 → 372:0:0; 374:0:1 → 646:0:1 |
| `q203_04_delamain.scene / scene / 422` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","comparisonType":"Equal"}}}` | 52:0:0 → 422:0:1; 422:0:0 → 420:0:0; 422:0:1 → 423:0:1 |
| `q203_04_delamain.scene / scene / 423` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":1,"comparisonType":"Equal"}}}` | 422:0:1 → 423:0:1; 423:0:0 → 421:0:0; 423:0:1 → 634:0:1 |
| `q203_04_delamain.scene / scene / 512` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"question_asked","value":1,"comparisonType":"Equal"}}}` | 512:0:0 → 534:0:0; 512:0:1 → 251:0:1; 1179:0:0 → 512:0:1 |
| `q203_04_delamain.scene / scene / 541` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 127:0:0 → 541:0:1; 134:0:0 → 541:0:1; 136:0:0 → 541:0:1; 138:0:0 → 541:0:1; 290:0:0 → 541:0:1; 292:0:0 → 541:0:1; 441:0:0 → 541:0:1; 442:0:0 → 541:0:1; 541:0:0 → 547:0:1 |
| `q203_04_delamain.scene / scene / 547` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_alone"}}}` | 541:0:0 → 547:0:1; 547:0:1 → 461:0:1 |
| `q203_04_delamain.scene / scene / 622` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":2,"comparisonType":"Equal"}}}` | 213:0:1 → 622:0:1; 622:0:0 → 435:0:0; 622:0:1 → 217:0:1 |
| `q203_04_delamain.scene / scene / 627` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":3,"comparisonType":"Equal"}}}` | 627:0:0 → 152:0:0; 628:0:1 → 627:0:1 |
| `q203_04_delamain.scene / scene / 628` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":2,"comparisonType":"Equal"}}}` | 252:0:1 → 628:0:1; 628:0:0 → 359:0:0; 628:0:1 → 627:0:1 |
| `q203_04_delamain.scene / scene / 633` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":3,"comparisonType":"Equal"}}}` | 633:0:0 → 421:0:0; 634:0:1 → 633:0:1 |
| `q203_04_delamain.scene / scene / 634` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":2,"comparisonType":"Equal"}}}` | 423:0:1 → 634:0:1; 634:0:0 → 425:0:0; 634:0:1 → 633:0:1 |
| `q203_04_delamain.scene / scene / 639` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":3,"comparisonType":"Equal"}}}` | 639:0:0 → 158:0:0; 640:0:1 → 639:0:1 |
| `q203_04_delamain.scene / scene / 640` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":2,"comparisonType":"Equal"}}}` | 264:0:1 → 640:0:1; 640:0:0 → 413:0:0; 640:0:1 → 639:0:1 |
| `q203_04_delamain.scene / scene / 645` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":3,"comparisonType":"Equal"}}}` | 645:0:0 → 372:0:0; 646:0:1 → 645:0:1 |
| `q203_04_delamain.scene / scene / 646` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":2,"comparisonType":"Equal"}}}` | 374:0:1 → 646:0:1; 646:0:0 → 416:0:0; 646:0:1 → 645:0:1 |
| `q203_04_delamain.scene / scene / 681` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#delamain_vehicle","names":["delamain_av"]},"comparisonParams":{"$type":"questComparisonParam"}}}}` | 681:0:0 → 683:0:1; 681:0:0 → 687:0:0; 684:0:0 → 681:0:1 |
| `q203_04_delamain.scene / scene / 683` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 681:0:0 → 683:0:1; 683:0:0 → 685:0:1 |
| `q203_04_delamain.scene / scene / 773` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_av_arrive_afterlife"}}` | 134:0:0 → 773:0:1; 136:0:0 → 773:0:1; 138:0:0 → 773:0:1; 773:0:1 → 485:0:0 |
| `q203_04_delamain.scene / scene / 1047` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_emmerick_calls_v_start_done"}}}` | 1047:0:0 → 1048:0:1; 1053:0:0 → 1047:0:1 |
| `q203_04_delamain.scene / scene / 1049` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_emmerick_calls_v_end_done"}}}` | 1049:0:0 → 1050:0:1; 1054:0:0 → 1049:0:1 |
| `q203_04_delamain.scene / scene / 1136` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","comparisonType":"Equal"}}}` | 468:0:0 → 1136:0:1; 1136:0:0 → 1145:0:0; 1136:0:1 → 1138:0:1 |
| `q203_04_delamain.scene / scene / 1138` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":1,"comparisonType":"Equal"}}}` | 1136:0:1 → 1138:0:1; 1138:0:0 → 1149:0:0; 1138:0:1 → 1142:0:1 |
| `q203_04_delamain.scene / scene / 1140` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":3,"comparisonType":"Equal"}}}` | 1140:0:0 → 1149:0:0; 1142:0:1 → 1140:0:1 |
| `q203_04_delamain.scene / scene / 1142` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq025_delamain_fate","value":2,"comparisonType":"Equal"}}}` | 1138:0:1 → 1142:0:1; 1142:0:0 → 1156:0:0; 1142:0:1 → 1140:0:1 |
| `q203_05_afterlife.scene / scene / 377` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/main_quest/epilogues/q203_legend/afterlife/drink","fileEntryIndex":3,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 369:0:0 → 377:0:1; 377:0:0 → 376:0:2 |
| `q203_05_afterlife.scene / scene / 487` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#q203_tr_mr_blue"}}` | 227:0:0 → 487:0:1; 487:0:0 → 484:0:0 |
| `q203_05_afterlife.scene / scene / 621` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 544:0:0 → 621:0:1; 621:0:0 → 619:0:1 |
| `q203_05_afterlife.scene / scene / 710` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_05_tr_blue_turn"}}` | 484:0:0 → 710:0:1; 710:0:0 → 704:0:0; 1199:0:0 → 710:0:1; 1246:1:0 → 710:0:0 |
| `q203_05_afterlife.scene / scene / 742` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 740:0:0 → 742:0:1; 742:0:0 → 744:0:1 |
| `q203_05_afterlife.scene / scene / 824` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sq031_rogue_met_johnny"}}}` | 806:2:0 → 824:0:1; 824:0:0 → 826:0:0; 824:0:1 → 828:0:0 |
| `q203_05_afterlife.scene / scene / 1005` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q203_com_mr_x","names":["mr_blue_eyes"]},"onScreenTest":true}}}` | 762:0:0 → 1005:0:1; 1005:0:0 → 1007:0:1 |
| `q203_05_afterlife.scene / scene / 1024` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#rogue","names":["rogue"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 762:0:0 → 1024:0:1; 1024:0:0 → 765:0:0; 1024:0:0 → 1291:0:1; 1024:0:0 → 1295:0:0 |
| `q203_05_afterlife.scene / scene / 1125` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#weyland","names":["weyland"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 604:0:0 → 1125:0:1; 1125:0:0 → 1262:0:1 |
| `q203_05_afterlife.scene / scene / 1198` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_mr_blue"}}` | 1198:0:0 → 1207:0:0; 1204:0:0 → 1198:0:1; 1246:1:0 → 1198:0:0 |
| `q203_05_afterlife.scene / scene / 1202` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q203_05_tr_blue_turn"}}` | 704:0:0 → 1202:0:1; 1202:0:0 → 1204:0:1; 1246:1:0 → 1202:0:0 |
| `q203_05_afterlife.scene / scene / 1204` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 1202:0:0 → 1204:0:1; 1204:0:0 → 1198:0:1; 1246:1:0 → 1204:0:0 |
| `q203_05_afterlife.scene / scene / 1216` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_05_tr_player_sit"}}` | 393:1:0 → 1216:0:1; 1216:0:0 → 459:0:0; 1216:0:1 → 1218:0:0 |
| `q203_05_afterlife.scene / scene / 1231` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_05_tr_player_sit"}}` | 778:1:0 → 1231:0:1; 1231:0:0 → 1228:0:0; 1231:0:1 → 1232:0:0 |
| `q203_05_afterlife.scene / scene / 1260` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#weyland","names":["weyland"]},"onScreenTest":true}}}` | 604:0:0 → 1260:0:1; 1260:0:0 → 1262:0:0 |
| `q203_05_afterlife.scene / scene / 1318` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1316:0:0 → 1318:0:1; 1318:0:0 → 1320:0:1 |
| `q203_05_afterlife.scene / scene / 1382` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 1382:0:0 → 1393:0:0; 1383:0:0 → 1382:0:1; 1419:0:0 → 1382:0:0 |
| `q203_05_afterlife.scene / scene / 1386` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 1383:0:1 → 1386:0:1; 1386:0:0 → 1393:0:0; 1419:0:0 → 1386:0:0 |
| `q203_05_afterlife.scene / scene / 1388` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":7}}}` | 1383:0:2 → 1388:0:1; 1388:0:0 → 1393:0:0; 1419:0:0 → 1388:0:0 |
| `q203_05_afterlife.scene / scene / 1434` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 1419:0:0 → 1434:0:0; 1434:0:0 → 1442:0:0; 1436:0:0 → 1434:0:1 |
| `q203_05_afterlife.scene / scene / 1438` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 1419:0:0 → 1438:0:0; 1436:0:1 → 1438:0:1; 1438:0:0 → 1442:0:0 |
| `q203_05_afterlife.scene / scene / 1440` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":7}}}` | 1419:0:0 → 1440:0:0; 1436:0:2 → 1440:0:1; 1440:0:0 → 1442:0:0 |
| `q203_05_afterlife.scene / scene / 1488` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_05_cancel_lokat"}}}` | 1027:0:0 → 1488:0:1; 1488:0:1 → 1410:0:1 |
| `q203_05_afterlife.scene / scene / 1525` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"nibbles_unlocked"}}}` | 227:0:0 → 1525:0:1; 1525:0:0 → 1526:0:1 |
| `q203_05_afterlife.scene / scene / 1529` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q203_05_afterlife_nibbles"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 1526:0:0 → 1529:0:1; 1529:0:0 → 1532:0:0 |
| `q203_06_cosmos.scene / scene / 246` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q203_fact_open_inner_airlock"}}}` | 171:2:0 → 246:0:1; 246:0:0 → 252:0:1; 246:0:0 → 3052:0:1 |
| `q203_06_cosmos.scene / scene / 362` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 55:0:0 → 362:0:1; 362:0:0 → 361:0:0 |
| `q203_06_cosmos.scene / scene / 400` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterGender_CondtionType","isPlayer":true,"gender":"Male"}}}` | 545:0:0 → 400:0:1 |
| `q203_06_cosmos.scene / scene / 535` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_leaving_cabin"}}` | 70:0:0 → 535:0:1; 535:0:0 → 73:0:0; 535:0:0 → 163:0:0 |
| `q203_06_cosmos.scene / scene / 545` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q203_tr_enter_airlock"}}` | 83:0:0 → 545:0:1; 292:0:0 → 545:0:1; 545:0:0 → 174:0:0; 545:0:0 → 400:0:1; 545:0:0 → 549:0:1; 545:0:0 → 552:0:1 |
| `q203_06_cosmos.scene / scene / 550` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 549:0:0 → 550:0:1; 550:0:0 → 551:0:1 |
| `q203_06_cosmos.scene / scene / 620` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterBodyType_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#player"}}}}` | 118:0:0 → 620:0:1; 620:0:0 → 404:0:1; 620:0:1 → 402:0:1 |
| `q203_06_cosmos.scene / scene / 1189` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterBodyType_CondtionType","objectRef":{"$type":"gameEntityReference","reference":"#player"}}}}` | 407:0:0 → 1189:0:1; 1189:0:0 → 1191:0:0; 1189:0:1 → 198:0:0 |
| `q203_06_cosmos.scene / scene / 1203` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q203_06_cosmos_q203_female_v_tpp"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 404:0:0 → 1203:0:1; 1203:0:0 → 609:0:1 |
| `q203_06_cosmos.scene / scene / 1205` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q203_06_cosmos_q203_male_v_tpp"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 402:0:0 → 1205:0:1; 1205:0:0 → 624:0:1 |
| `q203_06_cosmos.scene / scene / 1224` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 609:0:0 → 1224:0:1; 1224:0:0 → 614:0:1 |
| `q203_06_cosmos.scene / scene / 1227` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 624:0:0 → 1227:0:1; 1227:0:0 → 627:0:1 |
| `q203_06_cosmos.scene / scene / 1255` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 1248:0:0 → 1255:0:1; 1255:0:0 → 280:0:1 |
| `q203_06_cosmos.scene / scene / 2971` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 55:0:0 → 2971:0:1; 2971:0:0 → 2974:0:1; 2971:0:0 → 2982:0:1; 2971:0:0 → 3056:0:1; 2971:0:0 → 3059:0:1 |
| `q203_06_cosmos.scene / scene / 2974` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":600}}}` | 2971:0:0 → 2974:0:1; 2974:0:0 → 2978:0:1 |
| `q203_06_cosmos.scene / scene / 3002` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#q203_shuttle_cabin_door","deviceControllerClass":"DoorControllerPS","deviceConditionFunction":"IsOpen"}}}` | 70:0:0 → 3002:0:1; 3002:0:0 → 3039:0:1 |
| `q203_06_cosmos.scene / scene / 3010` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 3007:0:0 → 3010:0:1; 3010:0:0 → 3047:0:1 |
| `q203_06_cosmos.scene / scene / 3077` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 386:0:0 → 3077:0:1; 3077:0:0 → 84:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mws_wat_02.questphase / h229 / 6; mws_wat_02.scene / scene / 12; mws_wat_02.scene / scene / 563; mws_wat_02.scene / scene / 574; +18 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | q203_02b_kerry.scene / scene / 124; q203_02c_judy.scene / scene / 155; q203_02d_panam.scene / scene / 37; q203_03_sobchak.scene / scene / 200; +1 locations in catalogue.json | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `call_lifecycle` | q203_06_cosmos.scene / scene / 3032; q203_06_cosmos.scene / scene / 3056 | contact + call operation + scene ownership → connection/end state. Audio filtering is not call connection; test busy, interrupted and ended calls. |
| `checkpoint` | q203_afterlife.questphase / h0 / 133; q203_av_ride.questphase / h0 / 15; q203_cosmos.questphase / h0 / 60; q203_cosmos.questphase / h0 / 63; +8 locations in catalogue.json | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mws_wat_02.scene / scene / 271; mws_wat_02.scene / scene / 487; q203_02_shower.scene / scene / 2163; q203_02_shower.scene / scene / 309; +101 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | mws_wat_02.questphase / h20 / 25; mws_wat_02.scene / scene / 573; q203_afterlife.questphase / h16 / 38; q203_afterlife.questphase / h16 / 46; +6 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mws_wat_02.questphase / h0 / 35; mws_wat_02.questphase / h0 / 38; mws_wat_02.questphase / h0 / 56; mws_wat_02.questphase / h20 / 17; +91 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `controller_event` | mws_wat_02.scene / scene / 371; mws_wat_02.scene / scene / 566; mws_wat_02.scene / scene / 578; q203_02_shower.scene / scene / 4420; +14 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | q203_02b_kerry.scene / scene / 2186; q203_02c_judy.scene / scene / 2168; q203_02d_panam.scene / scene / 2165; q203_03_sobchak.scene / scene / 2165; +52 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | q203_06_cosmos.scene / scene / 3002; q203_afterlife.questphase / h351 / 12; q203_penthouse.questphase / h1509 / 2; q203_penthouse.questphase / h1509 / 3; +4 locations in catalogue.json | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | mws_wat_02.questphase / h0 / 34 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mws_wat_02.questphase / h0 / 31; q203_cosmos.questphase / h51 / 21; q203_penthouse.questphase / h7 / 107; q203_penthouse.questphase / h7 / 115 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | q203_02_shower.scene / scene / 302; q203_02_shower.scene / scene / 305; q203_02_shower.scene / scene / 338; q203_02_shower.scene / scene / 340; +91 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | q203_av_ride.questphase / h0 / 20 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `persistent_decision` | mws_wat_02.questphase / h0 / 33; mws_wat_02.questphase / h20 / 18; mws_wat_02.questphase / h20 / 24; mws_wat_02.questphase / h20 / 29; +67 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | q203_penthouse.questphase / h0 / 195; q203_penthouse.questphase / h1509 / 5; q203_penthouse.questphase / h1573 / 5; q203_penthouse.questphase / h7 / 105 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mws_wat_02.questphase / h20 / 12; mws_wat_02.scene / scene / 139; mws_wat_02.scene / scene / 147; mws_wat_02.scene / scene / 167; +79 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | q203_delamain.questphase / h0 / 94; q203_delamain.questphase / h12 / 47 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `scene_interface` | mws_wat_02.questphase / h20 / 15; mws_wat_02.questphase / h20 / 31; mws_wat_02.questphase / h229 / 7; q203_afterlife.questphase / h0 / 135; +20 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mws_wat_02.questphase / h0 / 17; mws_wat_02.questphase / h20 / 10; mws_wat_02.scene / scene / 35; q203_02_shower.scene / scene / 379; +37 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `vehicle_control` | q203_02b_kerry.scene / scene / 544; q203_02c_judy.scene / scene / 870; q203_03_sobchak.scene / scene / 776; q203_04_delamain.scene / scene / 1159; +3 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `weather_scope` | q203_cosmos.questphase / h51 / 20; q203_penthouse.questphase / h244 / 39 | weather operation + named source + reset policy → weather request/reset dispatched. Completion follows the caller's full restoration sequence, not an early cleanup fact. |
| `workspot_performance` | mws_wat_02.scene / scene / 120; mws_wat_02.scene / scene / 135; mws_wat_02.scene / scene / 163; mws_wat_02.scene / scene / 169; +270 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | mws_wat_02.questphase / h0 / 61; mws_wat_02.questphase / h20 / 22; mws_wat_02.scene / scene / 226; q203_04_delamain.scene / scene / 666; +49 locations in catalogue.json | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` | content candidate; journal anchor | `base-mws-wat-02` |
| `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` | content candidate; forward dependency | `base-mws-wat-02` |
| `base\quest\bugfixing\epilogue\q203\q203_quest_bugfixes.questphase` | repair; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\phase\q203_afterlife.questphase` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\phase\q203_av_ride.questphase` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\phase\q203_cosmos.questphase` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\phase\q203_delamain.questphase` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02_shower.scene` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02b_kerry.scene` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02c_judy.scene` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02d_panam.scene` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\scenes\q203_03_sobchak.scene` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\scenes\q203_05_afterlife.scene` | content candidate; journal anchor | `base-q203` |
| `base\quest\main_quests\epilogue\q203\scenes\q203_06_cosmos.scene` | content candidate; journal anchor | `base-q203` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-02.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

1019 repeated typed/socket path signatures in this selected graph context; 217 distinct direct resource identities; 40 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h244 / 37 -> 36 -> 42 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `598920ee48558917ab4e` | `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 224 -> 223 -> 237 | questCheckpointNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene` / scene / 1053 -> 1047 -> 1048 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene` / scene / 1049 -> 1050 -> 465 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `a909c836470d2b0e7fbc` | `base\quest\main_quests\epilogue\q203\phase\q203_delamain.questphase` / h152 / 0 -> 2 -> 1 | questInputNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questOutputNodeDefinition; Out -> In; Out -> In |
| `8cd3b647ae3f592ad947` | `base\quest\main_quests\epilogue\q203\scenes\q203_03_sobchak.scene` / scene / 812 -> 807 -> 813 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `c8705a8da51824b73252` | `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h20 / 0 -> 7 -> 30 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `6497920d6ce0ac894daa` | `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h20 / 18 -> 38 -> 37 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; True -> In |
| `4e9253a72e6b0134b8dd` | `base\quest\main_quests\epilogue\q203\phase\q203_afterlife.questphase` / h0 / 149 -> 180 -> 156 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `40aa0dddb5f517500320` | `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h20 / 18 -> 38 -> 17 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; False -> In |
| `87eb1c34e9bd01e08a31` | `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h1261 / 23 -> 24 -> 20 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; False -> In; False -> In |
| `9c634ff27b9a7aa77918` | `base\quest\main_quests\epilogue\q203\phase\q203_delamain.questphase` / h12 / 0 -> 45 -> 46 | questInputNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h0 / 20 | `h20` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":11,"socketName":"Unload"},{"$type":"questOutputNodeDefinition","id":20,"socketName":"Kill"},{"$type":"questOutputNodeDefinition","id":28,"socketName":"Reset"}] |
| `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.questphase` / h0 / 46 | `h229` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":9,"socketName":"Kill"},{"$type":"questInputNodeDefinition","id":15,"socketName":"kill"}] |
| `base\quest\bugfixing\epilogue\q203\q203_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\epilogue\q203\q203_quest_bugfixes.questphase` / h0 / 12 | `h28` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\epilogue\q203\q203_quest_bugfixes.questphase` / h0 / 18 | `h96` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\epilogue\q203\q203_quest_bugfixes.questphase` / h0 / 23 | `h157` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_afterlife.questphase` / h0 / 7 | `h16` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_afterlife.questphase` / h0 / 185 | `h351` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_afterlife.questphase` / h0 / 189 | `h424` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_afterlife.questphase` / h0 / 213 | `h674` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_av_ride.questphase` / h0 / 5 | `h43` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_av_ride.questphase` / h0 / 28 | `h106` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_cosmos.questphase` / h0 / 23 | `h51` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_cosmos.questphase` / h0 / 64 | `h115` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_delamain.questphase` / h0 / 30 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_delamain.questphase` / h0 / 75 | `h152` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 35 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 188 | `h152` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h152 / 23 | `h164` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 214 | `h244` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":31,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h244 / 21 | `h251` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h244 / 44 | `h341` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h244 / 47 | `h374` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 219 | `h620` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 220 | `h719` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 221 | `h828` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 222 | `h941` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 227 | `h1057` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1","type":"NonTerminating"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 228 | `h1153` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 229 | `h1182` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 230 | `h1201` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 231 | `h1220` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 232 | `h1261` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"kerry","type":"NonTerminating"},{"$type":"questOutputNodeDefinition","id":10,"socketName":"judy","type":"NonTerminating"},{"$type":"questOutputNodeDefinition","id":11,"socketName":"river","type":"NonTerminating"},{"$type":"questOutputNodeDefinition","id":12,"socketName":"panam","type":"NonTerminating"},{"$type":"questOutputNodeDefinition","id":14,"socketName":"alone","type":"NonTerminating"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 234 | `h1359` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Sobchak"},{"$type":"questOutputNodeDefinition","id":2,"socketName":"Judy"},{"$type":"questOutputNodeDefinition","id":3,"socketName":"Kerry"},{"$type":"questOutputNodeDefinition","id":4,"socketName":"Panam"},{"$type":"questOutputNodeDefinition","id":5,"socketName":"Alone"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 235 | `h1423` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h1423 / 40 | `h1509` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h1423 / 41 | `h1573` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 238 | `h1685` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 239 | `h1718` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\main_quests\epilogue\q203\phase\q203_penthouse.questphase` / h0 / 246 | `h1784` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07.quest |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08.quest |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.gamedef` | content candidate | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.quest |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.gamedef` | content candidate | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\ma_cct_dtn_07.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_04\ma_hey_spr_04.quest |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.gamedef` | content candidate | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.gamedef` | content candidate | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.gamedef` | content candidate | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\ma_std_arr_06.quest |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.gamedef` | content candidate | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_02\ma_wat_kab_02_quest.quest |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_def.gamedef` | content candidate | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_quest.quest |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.gamedef` | content candidate | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\ma_wat_lch_06.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.gamedef` | content candidate | base\open_world\minor_activities\watson\northside\ma_wat_nid_22\ma_wat_nid_22.quest |
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
| `base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.gamedef` | content candidate | base\open_world\mini_world_stories\watson\mws_wat_02\mws_wat_02.quest |
| `base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.gamedef` | content candidate | base\open_world\mini_world_stories\watson\mws_wat_08\mws_wat_08.quest |
| `base\quest\main_quests\prologue\q000\q000.gamedef` | content candidate | base\quest\main_quests\prologue\q000\q000.quest |
| `base\quest\main_quests\prologue\q001\q001.gamedef` | content candidate | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\main_quests\prologue\q001\test\q001_miss0_mark_world.gamedef` | test/debug | base\quest\main_quests\prologue\q001\q001.quest |
| `base\quest\main_quests\prologue\q003\q003.gamedef` | content candidate | base\quest\main_quests\prologue\q003\q003.quest |
| `base\quest\main_quests\prologue\q005\q005_heist.gamedef` | content candidate | base\quest\main_quests\prologue\q005\q005_heist.quest |
| `base\quest\main_quests\part1\q101\q101.gamedef` | content candidate | base\quest\main_quests\part1\q101\q101.quest |
| `base\quest\main_quests\part1\q103\q103.gamedef` | content candidate | base\quest\main_quests\part1\q103\q103.quest |
| `base\quest\main_quests\part1\q105\q105_main.gamedef` | content candidate | base\quest\main_quests\part1\q105\q105_main.quest |
| `base\quest\main_quests\part1\q110\q110.gamedef` | content candidate | base\quest\main_quests\part1\q110\q110.quest |
| `base\quest\main_quests\part1\q112\q112_abduction.gamedef` | content candidate | base\quest\main_quests\part1\q112\q112_abduction.quest |
| `base\quest\main_quests\part1\q113\q113.gamedef` | content candidate | base\quest\main_quests\part1\q113\q113.quest |
| `base\quest\main_quests\part1\q114\q114_nomads.gamedef` | content candidate | base\quest\main_quests\part1\q114\q114_nomads.quest |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\main_quests\epilogue\q201\q201_heir.gamedef` | content candidate | base\quest\main_quests\epilogue\q201\q201_heir.quest |
| `base\quest\main_quests\epilogue\q202\q202.gamedef` | content candidate | base\quest\main_quests\epilogue\q202\q202.quest |
| `base\quest\main_quests\epilogue\q203\q203_legend.gamedef` | content candidate | base\quest\main_quests\epilogue\q203\q203_legend.quest |
| `base\quest\main_quests\epilogue\q204\q204_reborn.gamedef` | content candidate | base\quest\main_quests\epilogue\q204\q204_reborn.quest |
| `base\open_world\community\heywood\glen\hey_gle_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\heywood\wellsprings\hey_spr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\heywood\wellsprings\hey_spr_testdef.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\pacifica\west_wind_estate\pac_wwd_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\santo_domingo\arroyo\std_arr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\santo_domingo\rancho_coronado\std_rcr_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\kabuki\wat_kab_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\kabuki\wat_kab_testdef.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\little_china\wat_lch_prolog_ow_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\watson\northside\wat_nid_def.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\district_definitions\open_world_kabuki.gamedef` | content candidate | base\open_world\district_definitions\open_world_kabuki.quest |
| `base\open_world\open_world_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\police_system\police_system_test.gamedef` | content candidate | base\open_world\police_system\police_system_test.quest |
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
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02_test.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\metro\ue_metro\ue_metro.gamedef` | content candidate | base\open_world\metro\ue_metro\ue_metro.quest |
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
| `base\animations\facial\generic\interactive_scene\generic_facial_additives.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\items\environment\animal\cybercat.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_stand_2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_average_female_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_bar_lean0__2h_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_rail_lean0__2h_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_rail_lean270__arms_crossed__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_rail_lean270__lh_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_table_lean0__2h_on_table__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_wall_lean180__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\open_world\generic_female_average_work__stand__lh_glass_rh_rag__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__lie_bed_0__sleep__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_bench_lean180__lh_on_bench_back__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean0__2h_guitar__no_pick_fingers__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean0__2h_guitar__no_pick_ponpon__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean0__2h_guitar__pick__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean0__2h_guitar__pick_beast__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair_lean0__2h_guitar__pick_chippin__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_back__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_rail_lean0__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_rail_lean270__lh_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_rail_lean270__lh_on_rail_rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_table_lean180__rh_cigarette_lh_table__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_big_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__sit_barstool_bar_lean0__2h_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__sit_barstool_bar_lean270__lh_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__stand__2h_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__stand_rail_lean0__2h_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__stand_rail_lean270__lh_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big__stand_table_lean0__2h_on_table__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\interactive_scene\generic_male_big_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\open_world\generic_male_big__stand_rail_lean315__rh_can_lh_phone__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\open_world\generic_male_big__stand_table_lean180__rh_can__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\open_world\generic_male_big__work_transitions__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_big\open_world\generic_male_big_work__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\claire\interactive_scene\claire__stand__lh_glass_rh_rag__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\claire\interactive_scene\claire__stand_bar_lean0__2h_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\claire\interactive_scene\claire__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__lie_table_lean270__rh_on_belly__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_bench_lean0__lh_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\female\body\player_locomotion_johnny_guitar.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__sit_barstool_bar_lean0__2h_on_bar.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__sit_bench_lean180__rh_on_backrest__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__stand_rail_lean0__2h_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__sit_barstool_bar_lean0__2h_on_bar.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__sit_bench_lean180__rh_on_backrest__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__stand_rail_lean0__2h_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__stand_rail_lean90__rh_on_rail__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\male\body\player_locomotion_sick.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01_wakeup\body\q203_01_wakeup__excalibur.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01_wakeup\body\q203_01_wakeup__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01_wakeup\body\q203_01_wakeup__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01_wakeup\synced\synced__q203_01_wakeup__necklace.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01_wakeup\synced\synced__q203_01_wakeup__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01_wakeup\synced\synced__q203_01_wakeup__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01a_wakeup_sobchak\body\q203_01a_wakeup_sobchak__male_big.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01a_wakeup_sobchak\rid\synced__river_joins_v_in_shower__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01a_wakeup_sobchak\rid\synced__v_river_final_goodbye_hug__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01a_wakeup_sobchak\rid\synced__v_wakes_river__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01a_wakeup_sobchak\synced\synced__q203_01a_wakeup_sobchak__male_big.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01a_wakeup_sobchak\synced\synced__q203_01a_wakeup_sobchak__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01b_wakeup_judy\body\q203_01b_wakeup_judy__female_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01b_wakeup_judy\rid\synced__judy_and_v_in_shower__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01b_wakeup_judy\rid\synced__v_judy_final_goodbye_hug__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01b_wakeup_judy\rid\synced__v_judy_final_goodbye_no_hug__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01b_wakeup_judy\rid\synced__v_wakes_judy__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01b_wakeup_judy\synced\synced__q203_01b_wakeup_judy__female_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01b_wakeup_judy\synced\synced__q203_01b_wakeup_judy__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01c_wakeup_kerry\body\q203_01c_wakeup_kerry__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01c_wakeup_kerry\rid\synced__kerry_joins_v_in_shower__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01c_wakeup_kerry\rid\synced__v_kerry_final_goodbye_hug__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01c_wakeup_kerry\rid\synced__v_kerry_final_goodbye_no_hug__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01c_wakeup_kerry\synced\synced__q203_01c_wakeup_kerry__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_01c_wakeup_kerry\synced\synced__q203_01c_wakeup_kerry__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_02d_panam\body\q203_02d_panam__female_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_02d_panam\rid\synced__v_panam_final_goodbye_hug__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_02d_panam\rid\synced__v_panam_final_goodbye_no_hug__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_02d_panam\rid\synced__v_tries_joining_panam_in_shower__01.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_02d_panam\synced\synced__q203_02d_panam__female_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_02d_panam\synced\synced__q203_02d_panam__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_05_afterlife\body\q203_05_afterlife__excalibur.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_05_afterlife\body\q203_05_afterlife__female_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_05_afterlife\body\q203_05_afterlife__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_05_afterlife\body\q203_05_afterlife__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_05_afterlife\synced\synced__q203_05_afterlife__leaflet.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_05_afterlife\synced\synced__q203_05_afterlife__male_average.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_05_afterlife\synced\synced__q203_05_afterlife__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_05_afterlife\synced\synced__q203_05_afterlife__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_06_cosmos\body\q203_06_cosmos__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_06_cosmos\body\q203_06_cosmos__shuttle_a_gate_control_lever.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_06_cosmos\body\q203_06_cosmos__space_shuttle_single_sliding_door.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_06_cosmos\q203_3_legend_cosmos.scenerid` | asset binding .scenerid | content/basegame_4_gamedata.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_06_cosmos\synced\synced__q203_06_cosmos__leaflet.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_06_cosmos\synced\synced__q203_06_cosmos__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_06_cosmos\synced\synced__q203_06_cosmos__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_06_cosmos\synced\synced__q203_06_cosmos__shuttle_a_airlock_door_b.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_06_cosmos\synced\synced__q203_06_cosmos__shuttle_a_gate_control_lever.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\epilogue\q203\q203_06_cosmos\synced\synced__q203_06_cosmos__space_shuttle_single_sliding_door.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q113\q113_05_av_flight\body\q113_05_av_flight__player_female.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q113\q113_05_av_flight\body\q113_05_av_flight__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q113\q113_05_av_flight\vehicles\q113_05_av_flight__av_rayfield_excalibur.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q115\q115_03_rogue\body\q115_03_rogue__wa_rogue.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\part1\q116\q116_05_mikoshi\synced\synced__q116_05_mikoshi__necklace.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q000\q000_corpo_03b_fly_to_lizzies\body\q000_corpo_03b_fly_to_lizzies__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q000\q000_corpo_03b_fly_to_lizzies\vehicle\q000_corpo_03b_fly_to_lizzies__excalibur.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\main_quests\prologue\q005\q005_07_vip_apartament\q005_07_vip_apartament__iguana_animation.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\fx\quest\q203\cosmos\q203_character_lights.effect` | asset binding .effect | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\fx\quest\q203\cosmos\q203_jetpack_steam.effect` | asset binding .effect | content/basegame_4_gamedata.archive; index evidence only |
| `base\fx\quest\q203\cosmos\q203_space_dust.effect` | asset binding .effect | content/basegame_4_gamedata.archive; index evidence only |
| `base\fx\quest\q203\q203_blood_driping_hand.effect` | asset binding .effect | content/basegame_4_gamedata.archive; index evidence only |
| `base\fx\quest\q203\q203_camera_vfx.effect` | asset binding .effect | content/basegame_4_gamedata.archive; index evidence only |
| `base\fx\quest\q203\v_av_rayfield_dust_kickup.effect` | asset binding .effect | content/basegame_4_gamedata.archive; index evidence only |
| `base\gameplay\gui\global_tv\overlays\ch01_n54_news\ch01_n54_commercial_overlay.inkwidget` | UI | content/basegame_4_gamedata.archive; index evidence only |
| `base\media\quests\scenes\q203_01_crystal_palace_info.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\movies\fullscreen\q203\intro.bk2` | asset binding .bk2 | content/basegame_5_video.archive; index evidence only |
| `base\movies\fullscreen\q203\low_pressure_begining.bk2` | asset binding .bk2 | content/basegame_5_video.archive; index evidence only |
| `base\movies\fullscreen\q203\low_pressure_ending.bk2` | asset binding .bk2 | content/basegame_5_video.archive; index evidence only |
| `base\movies\fullscreen\q203\low_pressure_middle_part.bk2` | asset binding .bk2 | content/basegame_5_video.archive; index evidence only |
| `base\movies\fullscreen\q203\middle.bk2` | asset binding .bk2 | content/basegame_5_video.archive; index evidence only |
| `base\movies\tv\quest\tv_q203_01_crystal_palace_info.bk2` | asset binding .bk2 | content/basegame_5_video.archive; index evidence only |
| `base\open_world\mini_world_stories\watson\mws_wat_02\qest_custom\iguana.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\mini_world_stories\watson\mws_wat_02\qest_custom\synced__mws_wat_02__cybercat.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\mini_world_stories\watson\mws_wat_02\qest_custom\synced__mws_wat_02__iguana.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\mini_world_stories\watson\mws_wat_02\qest_custom\synced__mws_wat_02__player_male.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\lipsync\en\mws_wat_02\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\lipsync\en\mws_wat_02\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\lipsync\en\mws_wat_02\votest_olivia.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\lipsync\en\mws_wat_02\votest_sophie.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\main_quests\epilogue\q203\phase\q203_delamain.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02_shower\arasaka_ai.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02_shower\judy.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02_shower\kerry.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02_shower\rogue.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02_shower\sobchak.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02_shower\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02b_kerry\kerry.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02b_kerry\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02c_judy\judy.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02c_judy\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02d_panam\panam.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_02d_panam\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_03_sobchak\sobchak.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_03_sobchak\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_04_delamain\delamain.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_04_delamain\delamain_sad.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_04_delamain\emmerick.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_04_delamain\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_05_afterlife\civ_high_m_07_enus_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_05_afterlife\claire.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_05_afterlife\emmerick.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_05_afterlife\rogue.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_05_afterlife\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_05_afterlife\weyland.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_06_cosmos\civ_high_m_07_enus_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\lipsync\en\q203_06_cosmos\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\epilogue\q203\scenes\q203_01_wakeup.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02_shower.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02b_kerry.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02c_judy.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02d_panam.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\main_quests\epilogue\q203\scenes\q203_03_sobchak.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\main_quests\epilogue\q203\scenes\q203_05_afterlife.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\main_quests\epilogue\q203\scenes\q203_06_cosmos.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\animals\cat\cat__lie__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\archetype\dirt\common\ground\dirt__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\bar\ground\generic__stand_glass__clean__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\bar\generic__stand_bar_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\bed\generic__lie_double_bed__sleep__04.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\bench\generic__sit_bench_lean_back_l_hand_on_back__talk__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\bench\player__sit_bench_lean_back_r_hand_on_back__talk__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\common\chair\generic__sit_chair_lean_front_guitar__play__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__05.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_front_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_left__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_left__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_left_back_cell_can__talk__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_left_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\generic__stand_rail_lean_right__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\rail\player__stand_rail_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\table\big__stand_table_lean_back_can__drink__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\table\generic__stand_table_lean_back_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\table\generic__stand_table_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\generic__stand_wall_lean_back__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\claire\claire__stand_bar_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\jackie\jackie__sit_barstool_bar_lean_front__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__lie_table_lean_left__lie_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_bench__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\rogue\bar\rogue__stand_bar_lean_front__talk__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\main_characters\rogue\bar\rogue__stand_bar_lean_right__talk__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\player\bar\player__sit_barstool_bar_lean_front__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\player\rail\player__stand_rail_lean_left___01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_01_wakeup\player__lie_bed_lean_left__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_01_wakeup\player__lie_bed_lean_right__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_01_wakeup\player__stand_wall_lean_front_shower__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_01_wakeup\player__stand_wall_lean_front_shower_blood__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_01_wakeup\player__stand_wall_lean_front_shower_hide_blood__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_01a_wakeup_sobchak\river__lie_bed__sleep__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_01b_wakeup_judy\judy__lie_bed_lean_left__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_02d_panam\panam__stand_shower_lean_front__wash__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_05_afterlife\player_sit_bench_leaflet__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\epilogue\q203\q203_06_cosmos\player__sit_netrunner_chair_lean_back__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\part1\q113\q113_05_av_flight\player__sit_av_excalibur__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\prologue\q001\q001_03a_meet_jackie_downstairs\q001_03a_meet_jackie_downstairs__sit_barstool_bar_lean270__lh_on_bar__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\quest\main_quests\prologue\q005\q005_01a_slice_of_afterlife\q005_01a_slice_of_afterlife__claire_cleaning_glass.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\side_quests\sq031\sq031_01a_smack_afterlife\sq031__claire__stand_bar_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `air_traffic_off` | base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene / scene / 1440; base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene / scene / 1442; base\quest\minor_quests\mq014\mq014.questphase / h215 / 83; base\quest\minor_quests\mq014\mq014.questphase / h643 / 50; 172 total source locations in compressed evidence |
| `holo_emmerick_calls_v_end_activate` | base\quest\holocalls\emmerick\emmerick_holocall.questphase / h0 / 11; 1 total source locations in compressed evidence |
| `holo_emmerick_calls_v_end_done` | base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 107; base\quest\holocalls\emmerick\emmerick_holocall.scene / scene / 42; base\quest\holocalls\emmerick\emmerick_holocall.scene / scene / 552; 3 total source locations in compressed evidence |
| `holo_emmerick_calls_v_start_activate` | base\quest\holocalls\emmerick\emmerick_holocall.questphase / h0 / 10; 1 total source locations in compressed evidence |
| `holo_emmerick_calls_v_start_done` | base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 106; base\quest\holocalls\emmerick\emmerick_holocall.scene / scene / 41; base\quest\holocalls\emmerick\emmerick_holocall.scene / scene / 585; 3 total source locations in compressed evidence |
| `johnny_default_on` | base\quest\minor_quests\mq033\mq033_tarot.questphase / h197 / 226; base\quest\minor_quests\mq033\mq033_tarot.questphase / h197 / 227; base\quest\minor_quests\mq033\mq033_tarot.questphase / h197 / 228; base\quest\minor_quests\mq033\mq033_tarot.questphase / h197 / 229; 24 total source locations in compressed evidence |
| `mq001_done` | base\quest\minor_quests\mq001\mq001.questphase / h517 / 11; base\quest\minor_quests\mq001\phases\mq001_cleanup.questphase / h0 / 59; base\quest\minor_quests\mq001\scenes\test\mq001_chicken_test.scene / scene / 88; base\quest\main_quests\epilogue\q203\q203_legend.quest / h43 / 5; 4 total source locations in compressed evidence |
| `mq003_done` | base\quest\minor_quests\mq003\mq003_orbitals.questphase / h0 / 12; base\quest\main_quests\epilogue\q203\q203_legend.quest / h43 / 9; 2 total source locations in compressed evidence |
| `mq014_altar_looted` | base\quest\minor_quests\mq014\phases\mq014_altar.questphase / h0 / 2; base\quest\main_quests\epilogue\q203\q203_legend.quest / h43 / 6; 2 total source locations in compressed evidence |
| `mq019_done` | base\quest\minor_quests\mq019\phases\mq019_06_finale.questphase / h0 / 40; base\quest\main_quests\epilogue\q203\q203_legend.quest / h43 / 8; ep1\quest\main_quests\q303\test\q303_00_chickentest.scene / scene / 315; ep1\quest\main_quests\q303\test\q303_00_chickentest.scene / scene / 368; 7 total source locations in compressed evidence |
| `mq033_done` | base\quest\minor_quests\mq033\mq033_tarot.questphase / h0 / 89; base\quest\main_quests\epilogue\q203\q203_legend.quest / h43 / 3; 2 total source locations in compressed evidence |
| `mq055_apt_interactions_off` | base\quest\minor_quests\mq055\scenes\mq055_01_megabuilding.scene / scene / 6874; base\quest\minor_quests\mq055\scenes\mq055_01_megabuilding.scene / scene / 6876; base\quest\minor_quests\mq055\scenes\mq055_01_megabuilding.scene / scene / 6879; base\quest\minor_quests\mq055\scenes\mq055_01_megabuilding.scene / scene / 6883; 10 total source locations in compressed evidence |
| `mws_wat_02_iguana_cat_together` | base\quest\main_quests\prologue\q003\phases\q003_stout.questphase / h575 / 95; 1 total source locations in compressed evidence |
| `mws_wat_02_iguana_cat_together_done` | base\quest\main_quests\prologue\q003\phases\q003_stout.questphase / h575 / 98; 1 total source locations in compressed evidence |
| `nibbles_unlocked` | base\quest\bugfixing\minor_quests\mq000\mq000_quest_bugfixes.questphase / h258 / 7; base\quest\main_quests\prologue\q003\phases\q003_stout.questphase / h575 / 38; ep1\quest\main_quests\q306\test\q306_00_chickentest.scene / scene / 1150; 3 total source locations in compressed evidence |
| `q101_done` | base\open_world\minor_activities\watson\little_china\ma_wat_lch_06\test\ma_wat_lch_06_chicken_test.scene / scene / 6; base\open_world\minor_activities\watson\northside\ma_wat_nid_15\ma_wat_nid_15.quest / h0 / 24; base\quest\minor_quests\mq010\mq010.quest / h0 / 12; base\quest\minor_quests\mq018\phases\mq018_00_chickentest.questphase / h0 / 27; 51 total source locations in compressed evidence |
| `q115_did_it_solo` | base\quest\main_quests\part1\q115\phases\q115_solo_the_mikoshi.questphase / h0 / 12; base\quest\main_quests\part1\q116\test\q116_00_chicken_test.scene / scene / 348; base\quest\main_quests\epilogue\q203\tests\q203_chickentest.scene / scene / 248; 3 total source locations in compressed evidence |
| `q115_judy_romance_chosen` | base\quest\main_quests\part1\q115\scenes\q115_02b_ripperdoc_roof.scene / scene / 949; base\quest\main_quests\epilogue\q202\test\q202_chicken_test.scene / scene / 29; base\quest\main_quests\epilogue\q203\tests\q203_chickentest.scene / scene / 15; base\quest\main_quests\epilogue\q204\test\q204_00_chicken_test.scene / scene / 18; 5 total source locations in compressed evidence |
| `q115_jungle_weyland_saved` | base\quest\main_quests\part1\q115\phases\q115_05_jungle.questphase / h1320 / 34; base\quest\main_quests\part1\q115\phases\q115_05_jungle_weyland.questphase / h7 / 10; base\quest\main_quests\part1\q115\phases\q115_05_jungle_weyland.questphase / h624 / 10; base\quest\main_quests\part1\q115\test\q115_00_chickentest.scene / scene / 680; 8 total source locations in compressed evidence |
| `q115_kerry_romance_chosen` | base\quest\main_quests\part1\q115\scenes\q115_02b_ripperdoc_roof.scene / scene / 946; base\quest\main_quests\epilogue\q202\test\q202_chicken_test.scene / scene / 33; base\quest\main_quests\epilogue\q203\tests\q203_chickentest.scene / scene / 17; base\quest\main_quests\epilogue\q204\test\q204_00_chicken_test.scene / scene / 19; 5 total source locations in compressed evidence |
| `q115_panam_romance_chosen` | base\quest\bugfixing\part1\q114\q114_cinematic_bugfixes.questphase / h7 / 13; base\quest\main_quests\part1\q114\scenes\test\q114_00_setup.scene / scene / 1044; base\quest\main_quests\part1\q114\scenes\test\q114_00_setup.scene / scene / 1045; base\quest\main_quests\part1\q115\scenes\q115_02b_ripperdoc_roof.scene / scene / 952; 8 total source locations in compressed evidence |
| `q115_river_romance_chosen` | base\quest\main_quests\part1\q115\scenes\q115_02b_ripperdoc_roof.scene / scene / 943; base\quest\main_quests\epilogue\q202\test\q202_chicken_test.scene / scene / 35; base\quest\main_quests\epilogue\q203\tests\q203_chickentest.scene / scene / 13; base\quest\main_quests\epilogue\q204\test\q204_00_chicken_test.scene / scene / 21; 5 total source locations in compressed evidence |
| `q305_johnny_scene_active` | ep1\quest\main_quests\q305\phases\q305_08_border_crossing.questphase / h1079 / 69; ep1\quest\main_quests\q305\phases\q305_09_chippin_in.questphase / h0 / 9; ep1\quest\main_quests\q305\phases\q305_09_chippin_in.questphase / h0 / 65; ep1\quest\main_quests\q305\scenes\q305_12_johnny.scene / scene / 2331; 4 total source locations in compressed evidence |
| `radio_on` | base\quest\minor_quests\mq008\mq008.questphase / h577 / 23; base\quest\minor_quests\mq008\mq008.questphase / h1616 / 3; base\quest\minor_quests\mq008\mq008.questphase / h1616 / 5; base\quest\minor_quests\mq008\phases\mq008_cleanup.questphase / h0 / 19; 206 total source locations in compressed evidence |
| `sq012_done` | base\quest\main_quests\epilogue\q201\scenes\q201_00_chicken_test.scene / scene / 149; base\quest\main_quests\epilogue\q201\scenes\q201_00_chicken_test.scene / scene / 158; base\quest\main_quests\epilogue\q201\scenes\q201_00_chicken_test.scene / scene / 165; base\quest\main_quests\epilogue\q201\scenes\q201_00_chicken_test.scene / scene / 175; 11 total source locations in compressed evidence |
| `sq024_claire_pissed` | base\quest\minor_quests\mq058\phases\mq058_quest_setup.questphase / h0 / 109; base\quest\main_quests\part1\q115\test\q115_00_chickentest.scene / scene / 845; base\quest\side_quests\sq024\phases\sq024_02_pacifica_race.questphase / h5370 / 2; base\quest\side_quests\sq024\phases\sq024_03_badlands_race.questphase / h6692 / 2; 13 total source locations in compressed evidence |
| `sq025_delamain_fate` | base\quest\minor_quests\mq055\mq055.quest / h37 / 39; base\quest\main_quests\epilogue\q203\tests\q203_chickentest.scene / scene / 221; base\quest\main_quests\epilogue\q203\tests\q203_chickentest.scene / scene / 224; base\quest\main_quests\epilogue\q203\tests\q203_chickentest.scene / scene / 228; 17 total source locations in compressed evidence |
| `sq026_done` | base\quest\main_quests\epilogue\q203\q203_legend.quest / h43 / 7; base\quest\main_quests\epilogue\q204\test\q204_00_chicken_test.scene / scene / 116; base\quest\side_quests\sq026\phases\sq026_end.questphase / h96 / 20; base\quest\side_quests\sq026\phases\sq026_end.questphase / h225 / 24; 6 total source locations in compressed evidence |
| `sq029_done` | base\quest\main_quests\epilogue\q203\q203_legend.quest / h43 / 4; base\quest\side_quests\sq029\phases\sq029_conclusion.questphase / h286 / 4; 2 total source locations in compressed evidence |
| `sq031_rogue_met_johnny` | base\quest\main_quests\epilogue\q204\test\q204_00_chicken_test.scene / scene / 239; base\quest\side_quests\sq031\scenes\sq031_01d_smack_rogue.scene / scene / 806; ep1\quest\minor_quests\mq301\scenes\test\mq301_chicken_test.scene / scene / 466; ep1\quest\minor_quests\mq301\scenes\test\mq301_chicken_test.scene / scene / 588; 6 total source locations in compressed evidence |
| `sq032_done` | base\quest\side_quests\sq032\sq032.questphase / h0 / 76; 1 total source locations in compressed evidence |

NodeRef uses: 1236; TweakDB binding uses: 302. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene` | 10 / 29 | scnChangeIdleAnimEvent: 4; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnLookAtEvent: 1; scnPlaySkAnimEvent: 7; scnUnmountEvent: 1; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 12 |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02_shower.scene` | 12 / 78 | scnAudioEvent: 12; scnChangeIdleAnimEvent: 3; scnDialogLineEvent: 7; scnGameplayTransitionEvent: 3; scnIKEvent: 6; scnPlaySkAnimEvent: 11; scnUnmountEvent: 3; scneventsAttachPropToPerformer: 2; scneventsAttachPropToWorld: 2; scneventsCameraParamsEvent: 6; scneventsSetAnimFeatureEvent: 3; scneventsSocket: 12; scneventsVFXEvent: 8 |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02b_kerry.scene` | 49 / 490 | scnAudioEvent: 25; scnChangeIdleAnimEvent: 20; scnDialogLineEvent: 115; scnGameplayTransitionEvent: 5; scnIKEvent: 10; scnLookAtEvent: 90; scnPlaySkAnimEvent: 105; scnUnmountEvent: 5; scneventsAttachPropToPerformer: 5; scneventsAttachPropToWorld: 3; scneventsCameraParamsEvent: 15; scneventsSetAnimFeatureEvent: 5; scneventsSocket: 78; scneventsVFXEvent: 9 |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02c_judy.scene` | 54 / 481 | scnAudioEvent: 21; scnChangeIdleAnimEvent: 22; scnDialogLineEvent: 97; scnGameplayTransitionEvent: 7; scnIKEvent: 14; scnLookAtEvent: 83; scnPlaySkAnimEvent: 129; scnUnmountEvent: 7; scneventsAttachPropToPerformer: 1; scneventsAttachPropToWorld: 1; scneventsCameraParamsEvent: 20; scneventsSetAnimFeatureEvent: 7; scneventsSocket: 63; scneventsVFXEvent: 9 |
| `base\quest\main_quests\epilogue\q203\scenes\q203_02d_panam.scene` | 38 / 394 | scnAudioEvent: 20; scnChangeIdleAnimEvent: 25; scnDialogLineEvent: 64; scnGameplayTransitionEvent: 5; scnIKEvent: 10; scnLookAtEvent: 89; scnPlaySkAnimEvent: 99; scnUnmountEvent: 5; scneventsAttachPropToPerformer: 1; scneventsAttachPropToWorld: 1; scneventsCameraParamsEvent: 15; scneventsSetAnimFeatureEvent: 5; scneventsSocket: 49; scneventsVFXEvent: 6 |
| `base\quest\main_quests\epilogue\q203\scenes\q203_03_sobchak.scene` | 53 / 433 | scnAudioEvent: 24; scnChangeIdleAnimEvent: 16; scnDialogLineEvent: 89; scnGameplayTransitionEvent: 5; scnIKEvent: 10; scnLookAtEvent: 57; scnPlaySkAnimEvent: 98; scnUnmountEvent: 5; scneventsAttachPropToPerformer: 3; scneventsAttachPropToWorld: 4; scneventsCameraParamsEvent: 17; scneventsSetAnimFeatureEvent: 5; scneventsSocket: 82; scneventsUnequipItemFromPerformerByItem: 2; scneventsVFXEvent: 16 |
| `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene` | 49 / 203 | scnAudioEvent: 9; scnChangeIdleAnimEvent: 6; scnDialogLineEvent: 157; scnGameplayActionEvent: 2; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnLookAtEvent: 1; scnPlaySkAnimEvent: 7; scnUnmountEvent: 1; scneventsSetAnimFeatureEvent: 2; scneventsSocket: 4; scneventsVFXDurationEvent: 2; scneventsVFXEvent: 9 |
| `base\quest\main_quests\epilogue\q203\scenes\q203_05_afterlife.scene` | 86 / 850 | scnAudioEvent: 19; scnChangeIdleAnimEvent: 17; scnDialogLineEvent: 145; scnGameplayTransitionEvent: 3; scnIKEvent: 6; scnLookAtEvent: 141; scnPlaySkAnimEvent: 355; scnUnmountEvent: 3; scneventsAttachPropToPerformer: 21; scneventsAttachPropToWorld: 20; scneventsCameraParamsEvent: 1; scneventsEquipItemToPerformer: 4; scneventsSetAnimFeatureEvent: 3; scneventsSocket: 95; scneventsUnequipItemFromPerformer: 2; scneventsVFXEvent: 15 |
| `base\quest\main_quests\epilogue\q203\scenes\q203_06_cosmos.scene` | 13 / 223 | scnAudioEvent: 11; scnChangeIdleAnimEvent: 7; scnDialogLineEvent: 15; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnPlayRidAnimEvent: 22; scnPlaySkAnimEvent: 97; scnUnmountEvent: 1; scneventsAttachPropToPerformer: 2; scneventsCameraParamsEvent: 1; scneventsPlayRidCameraAnimEvent: 22; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 15; scneventsVFXDurationEvent: 12; scneventsVFXEvent: 14 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
