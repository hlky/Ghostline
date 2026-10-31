# The Ballad of Buck Ravers

Journal: `quests/minor_quest/mq023_bootleg` · `MinorQuest` · hash `140985621`.

Journal premise: Don't think I've gone all sentimental or anything. Honestly, I couldn't give a shit if I've got any fans left in this city. If someone hears one of my tracks and they get the itch to take to the streets, then that's fuckin' nova, but those old recordings don't matter anymore. Find 'em, listen to 'em, I don't care. Although, while we're on the subject... Wonder how things are over at Rainbow Cadenza...

**Coverage: journal-linked.** 43 exact journal-linked nodes in 8 resources; 9 resources in the inspected dependency context.

Resource roles in that context: 8 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Talk to Johnny. (Primary) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny` |
| Go to the Rainbow Cadenza club. (Primary) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/02_go_to_venue` |
| Ask the staff about the club. (Primary) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/03_ask_the_staff` |
| Talk to the cook. (Primary) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/03a_talk_with_waiter` |
| Find the vendor selling the tapes. (Primary) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/04_find_street_vendor` |
| Talk to the vendor. (Primary) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/05_talk_with_karim` |
| Persuade the vendor to give you the tapes. (Primary) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/05a_obtain_samurai_recording_from_karim` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `mq023_quest_bugfixes.questphase / h30 / 9` (Condition) | `quests/minor_quest/mq023_bootleg` | 2:Out → 9:In; 9:True → 10:Active; 9:False → 11:In |
| `mq023_quest_bugfixes.questphase / h30 / 10` (Journal) | `quests/minor_quest/mq023_bootleg/description` | 9:True → 10:Active; 10:Out → 16:In1 |
| `mq023_quest_bugfixes.questphase / h30 / 13` (Journal) | `quests/minor_quest/mq023_bootleg` | 13:Out → 1:In; 14:Out → 13:Succeeded |
| `mq023_quest_bugfixes.questphase / h30 / 14` (Journal) | `quests/minor_quest/mq023_bootleg/description` | 11:True → 14:Active; 14:Out → 13:Succeeded |
| `mq023_quest_bugfixes.questphase / h172 / 9` (Condition) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/03_ask_the_staff` | 2:Out → 9:In; 9:True → 20:In; 9:False → 15:In1 |
| `mq023_quest_bugfixes.questphase / h172 / 19` (PauseCondition) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/04_find_street_vendor` | 10:Out → 19:In; 19:Out → 21:In |
| `q105_04_jigjig_street.scene / scene / 1713` (Condition) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny` | 1042:0:0 → 1713:0:1; 1046:0:0 → 1713:0:1; 1713:0:1 → 1714:0:1; input mappings: 0:0=CutDestination, 0:1=In |
| `mq023_bootleg.questphase / h125 / 6` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/02_go_to_venue` | 2:Out → 6:Active; 6:Out → 7:In |
| `mq023_bootleg.questphase / h178 / 6` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/04_find_street_vendor` | 5:Out → 6:Active; 6:Out → 7:In |
| `mq023_bootleg_02_diner.questphase / h0 / 4` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny` | 7:Out → 4:Active; 4:Out → 9:Start 0 |
| `mq023_bootleg_02_diner.questphase / h0 / 7` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/02_go_to_venue` | 2:Out → 7:Succeeded; 7:Out → 4:Active |
| `mq023_bootleg_03_vendor.questphase / h0 / 4` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/04_find_street_vendor` | 3:Out → 4:Succeeded; 4:Out → 5:Active |
| `mq023_bootleg_03_vendor.questphase / h0 / 5` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/05_talk_with_karim` | 4:Out → 5:Active; 5:Out → 7:Start 0 |
| `mq023_bootleg_03_vendor.questphase / h0 / 8` (Journal) | `quests/minor_quest/mq023_bootleg` | 17:Out → 8:Succeeded; 8:Out → 13:In |
| `mq023_01_johnny.scene / scene / 4` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny` | 4:0:0 → 213:0:1; 65:0:0 → 4:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_01_johnny.scene / scene / 19` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny` | 19:0:0 → 119:0:2; 60:2:0 → 19:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_01_johnny.scene / scene / 29` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/02_go_to_venue` | 29:0:0 → 239:0:0; 119:0:0 → 29:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_01_johnny.scene / scene / 119` (MappinManager) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny3` | 19:0:0 → 119:0:2; 119:0:0 → 29:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq023_01_johnny.scene / scene / 199` (MappinManager) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny` | 199:0:0 → 225:0:0; 221:0:0 → 199:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq023_01_johnny.scene / scene / 203` (MappinManager) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny3` | 225:0:0 → 203:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq023_01_johnny.scene / scene / 209` (MappinManager) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny` | 209:0:0 → 11:0:0; 213:0:0 → 209:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq023_01_johnny.scene / scene / 213` (Journal) | `quests/minor_quest/mq023_bootleg/description` | 4:0:0 → 213:0:1; 213:0:0 → 209:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq023_02_dinner.scene / scene / 4` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny` | 4:0:0 → 87:0:2; 5:0:0 → 4:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_02_dinner.scene / scene / 9` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/03_ask_the_staff` | 9:0:0 → 126:0:1; 87:0:0 → 9:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_02_dinner.scene / scene / 16` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/03_ask_the_staff` | 12:0:0 → 16:0:3; 16:0:0 → 30:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_02_dinner.scene / scene / 19` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/04_find_street_vendor` | 19:0:0 → 128:0:1; 33:0:0 → 19:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_02_dinner.scene / scene / 30` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/03a_talk_with_waiter` | 16:0:0 → 30:0:1; 30:0:0 → 213:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_02_dinner.scene / scene / 33` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/03a_talk_with_waiter` | 33:0:0 → 19:0:1; 252:0:1 → 33:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_02_dinner.scene / scene / 87` (MappinManager) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny1` | 4:0:0 → 87:0:2; 87:0:0 → 9:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq023_02_dinner.scene / scene / 121` (MappinManager) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny1` | 163:0:0 → 121:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq023_03_street_vendor.scene / scene / 141` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny` | 141:0:0 → 324:0:1; 142:0:0 → 141:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_03_street_vendor.scene / scene / 142` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/05_talk_with_karim` | 142:0:0 → 141:0:1; 686:0:0 → 142:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_03_street_vendor.scene / scene / 192` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/05a_obtain_samurai_recording_from_karim` | 192:0:0 → 196:0:1; 203:0:0 → 192:0:3; 772:0:0 → 192:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_03_street_vendor.scene / scene / 196` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/05_talk_with_karim` | 192:0:0 → 196:0:1; 196:0:0 → 949:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_03_street_vendor.scene / scene / 324` (MappinManager) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny2` | 141:0:0 → 324:0:1; 324:0:0 → 925:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq023_03_street_vendor.scene / scene / 478` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny` | 478:0:0 → 479:0:1; 480:0:0 → 478:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_03_street_vendor.scene / scene / 479` (MappinManager) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny2` | 478:0:0 → 479:0:1; 479:0:0 → 443:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq023_03_street_vendor.scene / scene / 480` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/05a_obtain_samurai_recording_from_karim` | 480:0:0 → 478:0:1; 869:0:0 → 480:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_03_street_vendor.scene / scene / 486` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny` | 33:0:0 → 486:0:2; 486:0:0 → 487:0:2; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_03_street_vendor.scene / scene / 487` (MappinManager) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny/johnny2` | 486:0:0 → 487:0:2; 487:0:0 → 488:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive |
| `mq023_03_street_vendor.scene / scene / 488` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/05a_obtain_samurai_recording_from_karim` | 487:0:0 → 488:0:1; 488:0:0 → 667:0:0; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_03_street_vendor.scene / scene / 493` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/05a_obtain_samurai_recording_from_karim` | 493:0:0 → 640:0:1; 495:0:0 → 493:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq023_03_street_vendor.scene / scene / 495` (Journal) | `quests/minor_quest/mq023_bootleg/mq023_bootleg/05_talk_with_karim` | 19:0:0 → 495:0:2; 495:0:0 → 493:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq023_quest_bugfixes.questphase / h305 / 12` | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene`; `#mq023_03_sm_street_vendor` | 9:Out → 12:ow_vendor_in |
| `mq023_bootleg.questphase / h0 / 2` | `base\quest\minor_quests\mq023\phases\mq023_bootleg_01_hook.questphase` | 0:Out → 2:In1; 2:Out1 → 3:In1 |
| `mq023_bootleg.questphase / h0 / 3` | `base\quest\minor_quests\mq023\phases\mq023_bootleg_02_diner.questphase` | 2:Out1 → 3:In1; 10:Out1 → 3:In1; 3:Out1 → 4:In1 |
| `mq023_bootleg.questphase / h0 / 4` | `base\quest\minor_quests\mq023\phases\mq023_bootleg_03_vendor.questphase` | 3:Out1 → 4:In1; 11:Out1 → 4:In1; 4:Out1 → 5:In1 |
| `mq023_bootleg_01_hook.questphase / h0 / 4` | `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene`; `#mq023_01_sm_johnny` | 11:Out1 → 4:Start 0; 4:mq023_johnny_out → 26:In |
| `mq023_bootleg_02_diner.questphase / h0 / 9` | `base\quest\minor_quests\mq023\scenes\mq023_02_dinner.scene`; `#mq023_02_sm_dinner` | 4:Out → 9:Start 0; 9:End 0 → 17:In; 9:content_token_control → 16:In1 |
| `mq023_bootleg_03_vendor.questphase / h0 / 7` | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene`; `#mq023_03_sm_street_vendor` | 5:Out → 7:Start 0; 7:End 0 → 20:In; 7:karim_content_manager_start → 18:In1 |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 42 | `mq023_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 42:In1 |
| `base\quest\main_quests\part1\q105\phases\q105_jigjig.questphase` / h0 / 474 | `q105_04_jigjig_street.scene` | 521: PauseCondition: #q105_tr_jigjig_street; 521:Out → 474:in_johnny |
| `base\quest\main_quests\part1\q105\phases\q105_jigjig_persistent.questphase` / h128 / 2 | `q105_04_jigjig_street.scene` | 27: PauseCondition: #q105_tr_04_peep_show; 8: SpawnManager; 30: PauseCondition: #q105_tr_04_stand_chats; 28: SpawnManager; 38: SpawnManager; 42: PauseCondition: #q105_tr_04b_gutter_prostitutes; 3: SpawnManager; 22: PauseCondition: #q105_tr_04b_sex; 11: SpawnManager; 27:Out → 2:in_window; 8:Out → 2:in_wbr_jpn_medicstore_02; 30:Out → 2:in_stand; 28:Out → 2:in_shop_scene; 38:Out → 2:in_scan; 42:Out → 2:in_gutter; 3:Out → 2:in_holograms; 22:Out → 2:in_sex_scene; 11:Out → 2:in_offer_m; 2:out_shop_scene → 31:In; 2:out_stand → 35:In; 2:out_sex_scene → 25:In |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 27 | `mq023_bootleg.questphase` | 70: LogicalHub; 70:Out1 → 27:In1 |
| `base\quest\minor_quests\mq023\mq023_bootleg.quest` / h0 / 2 | `mq023_bootleg.questphase` | 8: Scene: mq023_chicken_test.scene; 8: Scene: mq023_chicken_test.scene; 8: Scene: mq023_chicken_test.scene; 8:Start_Out → 2:In1; 2:Out1 → 3:In; 8:Noodle_Out → 2:Noodle_In; 8:Karim_Out → 2:Karim_In |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` / h0 / 2 | `mq023_bootleg_01_hook.questphase` | 0: Input; 0:Out → 2:In1; 2:Out1 → 3:In1 |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` / h0 / 3 | `mq023_bootleg_02_diner.questphase` | 2: Phase: mq023_bootleg_01_hook.questphase; 10: Phase; 2:Out1 → 3:In1; 10:Out1 → 3:In1; 3:Out1 → 4:In1 |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` / h0 / 4 | `mq023_bootleg_03_vendor.questphase` | 3: Phase: mq023_bootleg_02_diner.questphase; 11: Phase; 3:Out1 → 4:In1; 11:Out1 → 4:In1; 4:Out1 → 5:In1 |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_01_hook.questphase` / h0 / 4 | `mq023_01_johnny.scene` | 11: LogicalHub; 11:Out1 → 4:Start 0; 4:mq023_johnny_out → 26:In |
| `base\quest\minor_quests\mq042\phases\mq042_nomad_02_car.questphase` / h0 / 16 | `mq023_01_johnny.scene` | 16:interrupt_out → 19:In |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_02_diner.questphase` / h0 / 9 | `mq023_02_dinner.scene` | 4: Journal; 4:Out → 9:Start 0; 9:End 0 → 17:In; 9:content_token_control → 16:In1 |
| `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h305 / 12 | `mq023_03_street_vendor.scene` | 9: PauseCondition; 9:Out → 12:ow_vendor_in |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_03_vendor.questphase` / h0 / 7 | `mq023_03_street_vendor.scene` | 5: Journal; 5:Out → 7:Start 0; 7:End 0 → 20:In; 7:karim_content_manager_start → 18:In1 |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
| `base\quest\main_quests\part1\q105\phases\q105_fingers.questphase` / h0 / 277 | `q105_jigjig.questphase` | 284: Phase; 284:Out1 → 277:In1; 277:Out1 → 357:In |
| `base\quest\persistent_content.questphase` / h2760 / 2 | `q105_jigjig_persistent.questphase` | 0: Input; 5: Input; 0:Out → 2:In1; 5:Out → 2:In1 |
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 8 | `minorquests.questphase` | 0: Start; 0:Out → 8:In1 |
| `base\quest\demos\handson_2020\handson_2020_little_china.quest` / h0 / 7 | `minorquests.questphase` | 1: Start; 1:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest` / h0 / 7 | `minorquests.questphase` | 0: Start; 0:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 32 | `minorquests.questphase` | 25: LogicalHub; 25:Out1 → 32:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h0 / 5 | `minorquests.questphase` | 0: Start; 0:Out → 5:In1 |
| `base\quest\minor_quests\mq042\mq042_nomad.questphase` / h0 / 3 | `mq042_nomad_02_car.questphase` | 2: Phase: mq042_nomad_01_hook.questphase; 2:Out1 → 3:In1; 3:Out1 → 4:In1 |
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
| `base\quest\bugfixing\part1\q105\q105_quest_bugfixes.questphase` / h2380 / 14 | `q105_fingers.questphase` | 9: Condition: #q105_tr_fingers_office_operation; 9:True → 14:CYB-635451 |
| `base\quest\main_quests\part1\q105\phases\q105_complete.questphase` / h0 / 5 | `q105_fingers.questphase` | 3: Phase: q105_dollhouse.questphase; 48: Phase; 48: Phase; 3:to_jigjig → 5:In1; 5:Out1 → 72:In1; 48:jigjig → 5:jigjig; 48:fingers_start → 5:fingers_start |
| `base\animations\marketing\gifs\how_you_doing\how_you_doing_gif.quest` / h0 / 10 | `persistent_content.questphase` | 0: Start; 0:Out → 10:In1 |
| `base\quest\additional_game_elements.questphase` / h0 / 17 | `persistent_content.questphase` | 0: Input; 36: Input; 0:Out → 17:In1; 36:Out → 17:EP1_Standalone |
| `base\quest\main_quests\part1\q108\q108_johnny.quest` / h0 / 24 | `persistent_content.questphase` | 0: Start; 0:Out → 24:In1 |
| `base\quest\minor_quests\mq025\batty\batty_quest.quest` / h0 / 3 | `persistent_content.questphase` | 0: Start; 0:Out → 3:In1 |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 24 | `mq042_nomad.questphase` | 90: LogicalHub; 90:Out1 → 24:In1 |
| `base\quest\minor_quests\mq042\mq042_nomad.quest` / h0 / 0 | `mq042_nomad.questphase` | 7: Scene: mq042_chicken_test.scene; 0:Out1 → 2:In; 7:End 0 → 0:In1 |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h61 / 5 | `q105_quest_bugfixes.questphase` | 0: Input; 0:Out → 5:In1 |
| `base\quest\main_quests\part1\act_1.questphase` / h0 / 9 | `q105_complete.questphase` | 37: Input; 158: LogicalHub; 37:Out → 9:In1; 158:Out1 → 9:In1; 9:Start_q110 → 10:In1 |
| `base\quest\main_quests\part1\q105\definitions\q105_braindance.quest` / h0 / 2 | `q105_complete.questphase` | 5: FactsDBManager: q105_testdef; 5:Out → 2:to_studio |
| `base\quest\main_quests\part1\q105\definitions\q105_dollhouse.quest` / h0 / 2 | `q105_complete.questphase` |  |
| `base\quest\main_quests\part1\q105\definitions\q105_fingers.quest` / h0 / 2 | `q105_complete.questphase` |  |
| `base\quest\main_quests\part1\q105\definitions\q105_jigjig.quest` / h0 / 2 | `q105_complete.questphase` |  |
| `base\quest\main_quests\part1\q105\q105_main.quest` / h0 / 2 | `q105_complete.questphase` | 18: RenderFxManager; 20: Scene: q105_chicken.scene; 20: Scene: q105_chicken.scene; 20: Scene: q105_chicken.scene; 20: Scene: q105_chicken.scene; 20: Scene: q105_chicken.scene; 20: Scene: q105_chicken.scene; 2:clear → 1:In; 18:Out → 2:In1; 20:dollhouse → 2:to_dollhouse; 20:fingers → 2:to_fingers; 20:jigjig_end → 2:to_jigjig_end; 20:braindance → 2:to_studio; 20:ending → 2:to_final; 20:text → 2:to_text |
| `base\quest\minor_quests\mq048\mq048.questphase` / h435 / 15 | `q105_complete.questphase` | 7: GameManager; 7:Out → 15:In1 |
| `base\quest\side_quests\sq032\sq032.quest` / h85 / 2 | `q105_complete.questphase` | 3: FactsDBManager: q105_testdef_dollhouse_leave; 3:Out → 2:to_dollhouse |
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
| `base\quest\cyberpunk2077.questphase` / h0 / 33 | `act_1.questphase` | 32: Phase: prologue.questphase; 82: Phase; 57: Phase; 57: Phase; 57: Phase; 98: Condition: ep1_active Less 1; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 102: PauseCondition: ep1_active GreaterOrEqual 1; 32:Out1 → 33:Q101; 82:CYB-656199_Out → 33:CYB-656199_In; 33:Q201 → 36:Q201; 33:Q202 → 36:Q202; 57:Q101 Out → 33:Q101; 33:Q203 → 36:Q203; 57:Q101 Vroom Out → 33:Q101 Vroom; 33:Q204 → 36:Q204; 57:Q103 Out → 33:Q103; 98:True → 33:Q103; 33:Q115 Final Boards → 91:In1; 57:Q104 Out → 33:Q104; 57:Q105 Out → 33:Q105; 57:Q108 Out → 33:Q108; 57:Q110 Out → 33:Q110; 57:Q112 Out → 33:Q112; 57:Q113 Out → 33:Q113; 57:Q114 Out → 33:Q114; 57:Q115 Out → 33:Q115; 57:Q116 Out → 33:Q116; 57:EP1_Standalone → 33:EP1_Standalone; 102:Out → 33:EP1_Standalone |
| `base\quest\bugfixing\additional_content_bugfixing.questphase` / h0 / 21 | `mq048.questphase` | 20: DeletionMarker; 20:Out → 21:In1 |
| `base\quest\minor_quests\mq048\mq048.quest` / h0 / 3 | `mq048.questphase` | 11: Scene: mq048_chickentest.scene; 11: Scene: mq048_chickentest.scene; 11: Scene: mq048_chickentest.scene; 11: Scene: mq048_chickentest.scene; 11:q001_before_vic_out → 3:q001_before_vic; 11:q001_after_vic_out → 3:q001_after_vic; 11:after_q001_out → 3:after_q001; 11:after_Q101 → 3:after_q101 |
| `base\quest\bugfixing.questphase` / h0 / 19 | `additional_content_bugfixing.questphase` | 18: DeletionMarker; 18:Out → 19:In1 |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `q105_04_jigjig_street.scene` | in_wbr_jpn_medicstore_02, in_holograms, in_sex_scene, in_offer_m, in_window, in_stand, in_shop_scene, in_johnny, in_scan, in_gutter, johnny_jig_01 → out_sex_scene, out_offer_m, out_johnny, out_shop_scene, out_stand, out_04_implants | holo_01; holo_02; offer_f; offer_m; Judy; gutter_01; gutter_02; sex_m; sex_f; scan_f_01; scan_f_02; scan_m_01; scan_m_02; Johnny; peep_client_f_01; peep_client_m_01; peep_prostitute_m_01; stand_client_m_01; stand_client_m_02; shop_vendor_m; shop_client_m_01; street_dealer_m_unicorn; shop_client_m_02; peep_client_m_02; Player; 195 nodes / 222 edges |
| `mq023_01_johnny.scene` | Start 0, interrupt_in → End 0, interrupt_out, mq023_johnny_out | johnny; performer; Player; 41 nodes / 43 edges |
| `mq023_02_dinner.scene` | Start 0 → End 0, content_token_control | johnny; waiter; Karim; Player; 48 nodes / 54 edges |
| `mq023_03_street_vendor.scene` | Start 0, ow_vendor_in, cinedebug_start → End 0, karim_content_manager_start | johnny; karim; Player; 221 nodes / 268 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `q105_04_jigjig_street.scene / n886 / 0` | This more to your taste? (``) | No option-level predicate stored | 0:0 → 638:0:0 |
| `q105_04_jigjig_street.scene / n927 / 0` | Lemme see. (``) | No option-level predicate stored | 0:0 → 1024:0:0 |
| `q105_04_jigjig_street.scene / n959 / 0` | Lemme see. (``) | No option-level predicate stored | 0:0 → 1022:0:0 |
| `mq023_01_johnny.scene / n34 / 0` | Weak. Amateur hour. (`Option`) | No option-level predicate stored | 0:0 → 36:0:0 |
| `mq023_01_johnny.scene / n34 / 1` | Not bad. I guess. (`Option_01`) | No option-level predicate stored | 0:1 → 38:0:0 |
| `mq023_01_johnny.scene / n44 / 0` | Success gives you a platform. (`Option_02`) | No option-level predicate stored | 0:0 → 46:0:0 |
| `mq023_01_johnny.scene / n44 / 1` | Losers tend to say that. (`Option_03`) | No option-level predicate stored | 0:1 → 48:0:0 |
| `mq023_01_johnny.scene / n54 / 0` | Old tapes could be worth somethin'... (`Option_04`) | No option-level predicate stored | 0:0 → 56:0:0 |
| `mq023_01_johnny.scene / n54 / 1` | Lemme find those tapes, I'll be your fan. (`Option_05`) | No option-level predicate stored | 0:1 → 58:0:0 |
| `mq023_02_dinner.scene / n12 / 0` | Lookin' for some Samurai tapes. (``) | No option-level predicate stored | 0:0 → 16:0:3 |
| `mq023_02_dinner.scene / n12 / 1` | What happened to Rainbow Cadenza? (``) | No option-level predicate stored | 0:1 → 37:0:0 |
| `mq023_02_dinner.scene / n40 / 0` | What's he sell? (``) | No option-level predicate stored | 0:0 → 42:0:0 |
| `mq023_02_dinner.scene / n40 / 1` | Does his shoppin' there? (``) | No option-level predicate stored | 0:1 → 44:0:0 |
| `mq023_03_street_vendor.scene / n4 / 0` | Lookin' for some good tunes. (`samurai`) | No option-level predicate stored | 0:0 → 7:0:0 |
| `mq023_03_street_vendor.scene / n4 / 1` | You got any lazrpop in there...? (`Option`) | No option-level predicate stored | 0:1 → 374:0:1 |
| `mq023_03_street_vendor.scene / n9 / 0` | I'm looking for some real Samurai relics. (`old_vinyls`) | No option-level predicate stored | 0:0 → 19:0:0 |
| `mq023_03_street_vendor.scene / n9 / 1` | Silverhand's biggest fan, huh? (`fluff`) | No option-level predicate stored | 0:1 → 360:0:1 |
| `mq023_03_street_vendor.scene / n21 / 0` | I know what they say about Johnny at Arasaka. (`corpo`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questLifePath_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "LifePath_ScriptConditionType", "lifePathId": "83635443133"}}}} | 0:0 → 343:0:1 |
| `mq023_03_street_vendor.scene / n21 / 1` | I remember the gigs at Rainbow Cadenza. (`memories`) | No option-level predicate stored | 0:1 → 854:0:1 |
| `mq023_03_street_vendor.scene / n21 / 2` | I know what Johnny's last words to Kerry were. (`Option_03`) | No option-level predicate stored | 0:2 → 85:0:0 |
| `mq023_03_street_vendor.scene / n36 / 0` | Don't remember? Someone doused the blaze with beer. (`riots`) | No option-level predicate stored | 0:0 → 38:0:0 |
| `mq023_03_street_vendor.scene / n36 / 1` | Poor Denny... and her hair. (`fire`) | No option-level predicate stored | 0:1 → 39:0:0 |
| `mq023_03_street_vendor.scene / n75 / 0` | Known "Chippin' In" since I was a kid. (`Option_01`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "128271491759", "buildId": "74910219395", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:0 → 77:0:0 |
| `mq023_03_street_vendor.scene / n75 / 1` | Johnny's always with me. (`Option_02`) | No option-level predicate stored | 0:1 → 79:0:0 |
| `mq023_03_street_vendor.scene / n88 / 0` | Little help, Johnny. (`Option_04`) | No option-level predicate stored | 0:0 → 90:0:0 |
| `mq023_03_street_vendor.scene / n88 / 1` | A little help here, Johnny! (`Option_05`) | No option-level predicate stored | 0:1 → 92:0:0 |
| `mq023_03_street_vendor.scene / n110 / 0` | Something must've changed. (`Option_08`) | No option-level predicate stored | 0:0 → 112:0:0 |
| `mq023_03_street_vendor.scene / n110 / 1` | Can't change people by blowing 'em up... (`Option_09`) | No option-level predicate stored | 0:1 → 114:0:0 |
| `mq023_03_street_vendor.scene / n126 / 0` | Fuck, Johnny! (`Option_10`) | No option-level predicate stored | 0:0 → 129:0:0 |
| `mq023_03_street_vendor.scene / n126 / 1` | Johnny, please. (`Option_11`) | No option-level predicate stored | 0:1 → 131:0:0 |
| `mq023_03_street_vendor.scene / n162 / 0` | Jealous? Yes, it's Silverhand's jacket. (`Option_12`) | No option-level predicate stored | 0:0 → 163:0:0 |
| `mq023_03_street_vendor.scene / n162 / 1` | It's a replica. Bring back memories? (`Option_13`) | No option-level predicate stored | 0:1 → 165:0:0 |
| `mq023_03_street_vendor.scene / n199 / 0` | [Browse memorabilia] (`open_panel`) | No option-level predicate stored | 0:0 → 178:0:1 |
| `mq023_03_street_vendor.scene / n1083 / 0` | [Browse memorabilia] (`open_panel`) | No option-level predicate stored | 0:0 → 1100:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-12345` | mq023_quest_bugfixes.questphase / h7 / 2 | No reader in selected context |
| `CYB-629358` | mq023_quest_bugfixes.questphase / h30 / 2 | mq023_quest_bugfixes.questphase / h30 / 8 |
| `CYB-636803` | mq023_quest_bugfixes.questphase / h172 / 2 | mq023_quest_bugfixes.questphase / h172 / 8 |
| `CYB-644298_mq023` | mq023_quest_bugfixes.questphase / h124 / 2 | mq023_quest_bugfixes.questphase / h124 / 8 |
| `CYB-644863` | mq023_quest_bugfixes.questphase / h265 / 4 | mq023_quest_bugfixes.questphase / h265 / 3 |
| `censorship_drugs` | Producer outside selected context | q105_04_jigjig_street.scene / scene / 878; q105_04_jigjig_street.scene / scene / 882 |
| `censorship_homosexuality` | Producer outside selected context | q105_04_jigjig_street.scene / scene / 870; q105_04_jigjig_street.scene / scene / 874; q105_04_jigjig_street.scene / scene / 912; q105_04_jigjig_street.scene / scene / 918 |
| `mq017_var_interrupt_active` | mq023_bootleg_01_hook.questphase / h109 / 8; mq023_bootleg_01_hook.questphase / h109 / 9 | mq023_bootleg_01_hook.questphase / h0 / 4 |
| `mq023_done` | mq023_bootleg_03_vendor.questphase / h0 / 10 | mq023_quest_bugfixes.questphase / h124 / 9; mq023_quest_bugfixes.questphase / h265 / 12; mq023_quest_bugfixes.questphase / h30 / 11 |
| `mq023_karim_2h_table` | mq023_03_street_vendor.scene / scene / 1010; mq023_03_street_vendor.scene / scene / 776; mq023_03_street_vendor.scene / scene / 782; mq023_03_street_vendor.scene / scene / 854 | mq023_03_street_vendor.scene / scene / 1016; mq023_03_street_vendor.scene / scene / 1028; mq023_03_street_vendor.scene / scene / 1039 |
| `mq023_karim_change_idle` | mq023_03_street_vendor.scene / scene / 1230; mq023_03_street_vendor.scene / scene / 1253; mq023_03_street_vendor.scene / scene / 1257; mq023_03_street_vendor.scene / scene / 1261 | mq023_03_street_vendor.scene / scene / 1267 |
| `mq023_karim_keepalive` | mq023_03_street_vendor.scene / scene / 562; mq023_03_street_vendor.scene / scene / 564; mq023_03_street_vendor.scene / scene / 640; mq023_03_street_vendor.scene / scene / 644; mq023_03_street_vendor.scene / scene / 648; mq023_03_street_vendor.scene / scene / 660; mq023_03_street_vendor.scene / scene / 672; mq023_03_street_vendor.scene / scene / 674; mq023_03_street_vendor.scene / scene / 680; mq023_03_street_vendor.scene / scene / 682; mq023_03_street_vendor.scene / scene / 686; mq023_03_street_vendor.scene / scene / 691; mq023_03_street_vendor.scene / scene / 695; mq023_03_street_vendor.scene / scene / 988; mq023_03_street_vendor.scene / scene / 990 | mq023_03_street_vendor.scene / scene / 560; mq023_03_street_vendor.scene / scene / 566; mq023_03_street_vendor.scene / scene / 620; mq023_03_street_vendor.scene / scene / 711; mq023_03_street_vendor.scene / scene / 733; mq023_03_street_vendor.scene / scene / 803; mq023_03_street_vendor.scene / scene / 805; mq023_03_street_vendor.scene / scene / 808 |
| `mq023_killbodyidles` | mq023_03_street_vendor.scene / scene / 1069 | mq023_03_street_vendor.scene / scene / 1052 |
| `mq023_noodle_talk` | mq023_02_dinner.scene / scene / 137; mq023_quest_bugfixes.questphase / h172 / 23 | mq023_quest_bugfixes.questphase / h172 / 24 |
| `mq023_started` | mq023_bootleg_01_hook.questphase / h0 / 6 | No reader in selected context |
| `mq023_var_corpo_path_chosen` | mq023_03_street_vendor.scene / scene / 343 | No reader in selected context |
| `mq023_var_noodle_interrupt_active` | mq023_bootleg_02_diner.questphase / h69 / 8; mq023_bootleg_02_diner.questphase / h69 / 9 | mq023_bootleg_02_diner.questphase / h0 / 9 |
| `q101_kerry_insult` | Producer outside selected context | mq023_03_street_vendor.scene / scene / 118 |
| `q105_04_intro_done` | q105_04_jigjig_street.scene / scene / 812 | q105_04_jigjig_street.scene / scene / 1578; q105_04_jigjig_street.scene / scene / 1581; q105_04_jigjig_street.scene / scene / 1585; q105_04_jigjig_street.scene / scene / 1589 |
| `q105_04_jigjig_street_gutter_done` | q105_04_jigjig_street.scene / scene / 1409 | No reader in selected context |
| `q105_jigjig_prostitutes_scanned` | q105_04_jigjig_street.scene / scene / 383 | q105_04_jigjig_street.scene / scene / 1578; q105_04_jigjig_street.scene / scene / 1581; q105_04_jigjig_street.scene / scene / 1585; q105_04_jigjig_street.scene / scene / 1589 |
| `travelling_merchant_lives` | Producer outside selected context | mq023_quest_bugfixes.questphase / h0 / 24 |
| `wbr_jpn_cloth_02_default_on` | mq023_bootleg.questphase / h52 / 30; mq023_quest_bugfixes.questphase / h265 / 10 | mq023_quest_bugfixes.questphase / h265 / 11; mq023_quest_bugfixes.questphase / h286 / 11 |
| `wbr_jpn_clothingshop_02_met` | mq023_03_street_vendor.scene / scene / 1099; mq023_03_street_vendor.scene / scene / 1210 | mq023_03_street_vendor.scene / scene / 1100 |
| `wbr_jpn_food_01_default_on` | mq023_02_dinner.scene / scene / 126; mq023_02_dinner.scene / scene / 128; mq023_quest_bugfixes.questphase / h172 / 10; mq023_quest_bugfixes.questphase / h172 / 22 | mq023_quest_bugfixes.questphase / h172 / 20; mq023_quest_bugfixes.questphase / h172 / 21 |

## Exact gates, joins and cancellation

<details><summary>130 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `mq023_quest_bugfixes.questphase / h0 / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 25:Out → 24:In |
| `mq023_quest_bugfixes.questphase / h30 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-629358"}}}` | 0:Out → 8:In; 8:False → 2:In |
| `mq023_quest_bugfixes.questphase / h30 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq023_bootleg","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 2:Out → 9:In; 9:True → 10:Active; 9:False → 11:In |
| `mq023_quest_bugfixes.questphase / h30 / 11` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_done"}}}` | 9:False → 11:In; 11:True → 14:Active; 11:False → 15:In1 |
| `mq023_quest_bugfixes.questphase / h124 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-644298_mq023"}}}` | 0:Out → 8:In; 8:False → 2:In |
| `mq023_quest_bugfixes.questphase / h124 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_done"}}}` | 9:False → 1:In; 2:Out → 9:In; 9:True → 10:In |
| `mq023_quest_bugfixes.questphase / h172 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-636803"}}}` | 0:Out → 8:In; 8:False → 2:In |
| `mq023_quest_bugfixes.questphase / h172 / 9` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq023_bootleg/mq023_bootleg/03_ask_the_staff","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 2:Out → 9:In; 9:True → 20:In; 9:False → 15:In1 |
| `mq023_quest_bugfixes.questphase / h172 / 19` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq023_bootleg/mq023_bootleg/04_find_street_vendor","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 10:Out → 19:In; 19:Out → 21:In |
| `mq023_quest_bugfixes.questphase / h172 / 20` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wbr_jpn_food_01_default_on"}}}` | 9:True → 20:In; 20:True → 10:In; 20:False → 15:In1 |
| `mq023_quest_bugfixes.questphase / h172 / 21` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wbr_jpn_food_01_default_on","comparisonType":"Equal"}}}` | 19:Out → 21:In; 21:True → 22:In; 21:False → 24:In |
| `mq023_quest_bugfixes.questphase / h172 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_noodle_talk"}}}` | 24:False → 1:In; 21:False → 24:In; 22:Out → 24:In; 24:True → 23:In |
| `mq023_quest_bugfixes.questphase / h265 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-644863"}}}` | 0:Out → 3:In; 3:False → 4:In |
| `mq023_quest_bugfixes.questphase / h265 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wbr_jpn_cloth_02_default_on"}}}` | 11:Out → 9:In1; 9:Out1 → 11:In; 10:Out → 11:In |
| `mq023_quest_bugfixes.questphase / h265 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_done"}}}` | 4:Out → 12:In; 12:Out → 10:In |
| `mq023_quest_bugfixes.questphase / h286 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wbr_jpn_cloth_02_default_on","value":1,"comparisonType":"Less"}}}` | 0:Out → 11:In; 11:Out → 12:Inactive |
| `mq023_quest_bugfixes.questphase / h286 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#wbr_jpn_cloth_02_mp"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0},"comparisonType":"Less"}}}` | 7:Out → 14:In; 14:Out → 9:In1; 9:Out1 → 14:In |
| `mq023_quest_bugfixes.questphase / h305 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq023_bootleg_karim"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":20.0},"comparisonType":"Less"}}}` | 16:Out → 9:In; 9:Out → 12:ow_vendor_in |
| `mq023_quest_bugfixes.questphase / h305 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#wbr_jpn_cloth_02_mp"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0}}}}` | 5:Out → 15:In; 15:Out → 14:In |
| `q105_04_jigjig_street.scene / scene / 32` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q105_jigjig_injector"},"eventType":"Finished"}}}` | 32:0:0 → 33:0:0; 32:0:0 → 1612:0:1; 1605:0:0 → 32:0:1 |
| `q105_04_jigjig_street.scene / scene / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["offer_f"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":4.0},"comparisonType":"LessOrEqual"}}}` | 37:0:0 → 882:0:1; 947:0:0 → 37:0:1 |
| `q105_04_jigjig_street.scene / scene / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_f_01"]},"eventType":"Finished"}}}` | 39:0:0 → 1552:0:1; 1490:0:0 → 39:0:1 |
| `q105_04_jigjig_street.scene / scene / 40` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_f_02"]},"eventType":"Finished"}}}` | 40:0:0 → 1554:0:1; 1490:0:0 → 40:0:1 |
| `q105_04_jigjig_street.scene / scene / 41` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_m_01"]},"eventType":"Finished"}}}` | 41:0:0 → 1556:0:1; 1490:0:0 → 41:0:1 |
| `q105_04_jigjig_street.scene / scene / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_m_02"]},"eventType":"Finished"}}}` | 42:0:0 → 1558:0:1; 1490:0:0 → 42:0:1 |
| `q105_04_jigjig_street.scene / scene / 497` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["offer_m"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"LessOrEqual"}}}` | 497:0:0 → 532:0:0; 870:0:1 → 497:0:1 |
| `q105_04_jigjig_street.scene / scene / 660` | `questConditionNodeDefinition` `{"condition":{"$type":"questStatsCondition","type":{"$type":"questBuild_ConditionType","entityRef":{"$type":"questUniversalRef"},"scriptCondition":{"$type":"Build_ScriptConditionType","buildId":"85601791440","difficulty":"EASY"}}}}` | 660:0:0 → 464:0:0; 660:0:1 → 1134:0:1; 1539:0:0 → 660:0:1 |
| `q105_04_jigjig_street.scene / scene / 674` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q105_04_jigjig_street_Johnny"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 674:0:0 → 886:0:0; 674:0:0 → 891:0:1; 674:0:0 → 1082:0:1; 1075:1:0 → 674:0:0; 1075:1:0 → 674:1026:0; 1168:0:0 → 674:0:1; 1811:1:0 → 674:0:0 |
| `q105_04_jigjig_street.scene / scene / 684` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["holo_01"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"LessOrEqual"}}}` | 684:0:0 → 4:0:0; 828:0:0 → 684:0:1; 874:0:1 → 684:0:1 |
| `q105_04_jigjig_street.scene / scene / 706` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q105_04_jigjig_street_Johnny"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 706:0:0 → 1042:0:1; 706:0:0 → 1046:0:1; 1498:0:0 → 706:0:1 |
| `q105_04_jigjig_street.scene / scene / 720` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q105_tr_04b_gutter_prostitutes"}}` | 31:0:0 → 720:0:1; 720:0:0 → 722:0:0; 720:0:0 → 1411:0:1 |
| `q105_04_jigjig_street.scene / scene / 729` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q105_tr_04b_gutter_prostitutes"}}` | 33:0:0 → 729:0:1; 729:0:0 → 1164:0:0 |
| `q105_04_jigjig_street.scene / scene / 828` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["holo_01"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0},"comparisonType":"GreaterOrEqual"}}}` | 4:0:0 → 828:0:1; 828:0:0 → 684:0:1 |
| `q105_04_jigjig_street.scene / scene / 832` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["holo_02"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"LessOrEqual"}}}` | 832:0:0 → 565:0:0; 835:0:0 → 832:0:1; 874:0:1 → 832:0:1 |
| `q105_04_jigjig_street.scene / scene / 835` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["holo_02"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0},"comparisonType":"GreaterOrEqual"}}}` | 565:0:0 → 835:0:1; 835:0:0 → 832:0:1 |
| `q105_04_jigjig_street.scene / scene / 863` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 863:0:0 → 867:0:1; 863:0:0 → 1001:0:1; 1015:0:0 → 863:0:1 |
| `q105_04_jigjig_street.scene / scene / 870` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_homosexuality"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterGender_CondtionType","isPlayer":true,"gender":"Male"}}]}}` | 870:0:0 → 912:0:1; 870:0:1 → 497:0:1; 912:0:0 → 870:0:1; 1425:0:0 → 870:0:1 |
| `q105_04_jigjig_street.scene / scene / 874` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_homosexuality"}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterGender_CondtionType","isPlayer":true}}]}}` | 874:0:0 → 918:0:1; 874:0:1 → 684:0:1; 874:0:1 → 832:0:1; 918:0:0 → 874:0:1; 1419:0:0 → 874:0:1 |
| `q105_04_jigjig_street.scene / scene / 878` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_drugs"}}}` | 878:0:0 → 927:0:0; 878:0:1 → 922:0:0; 943:0:0 → 878:0:1 |
| `q105_04_jigjig_street.scene / scene / 882` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_drugs"}}}` | 37:0:0 → 882:0:1; 882:0:0 → 971:0:1; 882:0:0 → 997:0:0; 882:0:1 → 6:0:0 |
| `q105_04_jigjig_street.scene / scene / 891` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q105_tr_fingers_area"}}` | 674:0:0 → 891:0:1; 891:0:0 → 903:0:1; 1811:1:0 → 891:0:0 |
| `q105_04_jigjig_street.scene / scene / 902` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q105_04_jigjig_street_Johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"angleTolerance":60.0,"inverted":true}}}` | 638:0:0 → 902:0:1; 902:0:0 → 903:0:0 |
| `q105_04_jigjig_street.scene / scene / 912` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_homosexuality","comparisonType":"Equal"}}}` | 870:0:0 → 912:0:1; 912:0:0 → 870:0:1 |
| `q105_04_jigjig_street.scene / scene / 918` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"censorship_homosexuality","comparisonType":"Equal"}}}` | 874:0:0 → 918:0:1; 918:0:0 → 874:0:1 |
| `q105_04_jigjig_street.scene / scene / 980` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["offer_f"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":8.0},"comparisonType":"GreaterOrEqual"}}}` | 954:0:0 → 980:0:1; 980:0:0 → 982:0:1; 980:0:0 → 983:0:1; 983:0:0 → 980:0:1 |
| `q105_04_jigjig_street.scene / scene / 983` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["offer_f"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"LessOrEqual"}}}` | 980:0:0 → 983:0:1; 983:0:0 → 980:0:1; 983:0:0 → 987:0:1 |
| `q105_04_jigjig_street.scene / scene / 1005` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 867:0:0 → 1005:0:1; 1005:0:0 → 1004:0:1 |
| `q105_04_jigjig_street.scene / scene / 1015` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 861:0:0 → 1015:0:1; 1015:0:0 → 863:0:1; 1015:0:0 → 1013:0:1 |
| `q105_04_jigjig_street.scene / scene / 1042` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q105_tr_04_johnny_arrival_01"}}` | 706:0:0 → 1042:0:1; 1042:0:0 → 1177:0:0; 1042:0:0 → 1713:0:1; 1075:1:0 → 1042:0:0; 1075:1:0 → 1042:1026:0; 1207:1:0 → 1042:0:0; 1207:1:0 → 1042:1026:0 |
| `q105_04_jigjig_street.scene / scene / 1046` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q105_tr_04_johnny_arrival_02"}}` | 706:0:0 → 1046:0:1; 1046:0:0 → 1207:0:0; 1046:0:0 → 1713:0:1; 1075:1:0 → 1046:0:0; 1075:1:0 → 1046:1026:0; 1177:1:0 → 1046:0:0; 1177:1:0 → 1046:1026:0 |
| `q105_04_jigjig_street.scene / scene / 1082` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q105_04_jigjig_street_Johnny"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":7.0},"comparisonType":"GreaterOrEqual"}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q105_04_jigjig_street_Johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"inverted":true}}]}}` | 674:0:0 → 1082:0:1; 1075:1:0 → 1082:0:0; 1075:1:0 → 1082:1026:0; 1082:0:0 → 886:1:0; 1082:0:0 → 1087:0:1; 1811:1:0 → 1082:0:0 |
| `q105_04_jigjig_street.scene / scene / 1138` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q105_04_jigjig_street_Johnny"},"onScreenTest":true,"angleTolerance":60.0,"inverted":true}}}` | 1134:0:0 → 1138:0:1; 1138:0:0 → 1139:0:1 |
| `q105_04_jigjig_street.scene / scene / 1152` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q105_04_jigjig_street_Johnny"},"onScreenTest":true,"angleTolerance":60.0,"inverted":true}}}` | 722:0:0 → 1152:0:1; 1152:0:0 → 1153:0:1; 1164:1:0 → 1152:0:0 |
| `q105_04_jigjig_street.scene / scene / 1156` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_q105_04_jigjig_street_Johnny"},"onScreenTest":true,"angleTolerance":60.0,"inverted":true}}}` | 716:0:0 → 1156:0:1; 1156:0:0 → 1157:0:1 |
| `q105_04_jigjig_street.scene / scene / 1405` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":12}}}` | 716:0:0 → 1405:0:1; 1405:0:0 → 1407:0:1 |
| `q105_04_jigjig_street.scene / scene / 1442` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#q105_tr_04_dealer"}}` | 1433:0:0 → 1442:0:1; 1442:0:0 → 554:0:0 |
| `q105_04_jigjig_street.scene / scene / 1578` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q105_04_intro_done"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q105_jigjig_prostitutes_scanned","comparisonType":"Equal"}}]}}` | 1552:0:0 → 1578:0:1; 1578:0:0 → 1108:0:0 |
| `q105_04_jigjig_street.scene / scene / 1581` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q105_04_intro_done"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q105_jigjig_prostitutes_scanned","comparisonType":"Equal"}}]}}` | 1554:0:0 → 1581:0:1; 1581:0:0 → 1115:0:0 |
| `q105_04_jigjig_street.scene / scene / 1585` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q105_04_intro_done"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q105_jigjig_prostitutes_scanned","comparisonType":"Equal"}}]}}` | 1556:0:0 → 1585:0:1; 1585:0:0 → 1117:0:0 |
| `q105_04_jigjig_street.scene / scene / 1589` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q105_04_intro_done"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q105_jigjig_prostitutes_scanned","comparisonType":"Equal"}}]}}` | 1558:0:0 → 1589:0:1; 1589:0:0 → 1118:0:0 |
| `q105_04_jigjig_street.scene / scene / 1595` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["gutter_02"]},"eventType":"Finished"}}}` | 1595:0:0 → 1598:0:1; 1601:0:0 → 1595:0:1 |
| `q105_04_jigjig_street.scene / scene / 1596` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["gutter_01"]},"eventType":"Finished"}}}` | 1596:0:0 → 1597:0:1; 1601:0:0 → 1596:0:1 |
| `q105_04_jigjig_street.scene / scene / 1633` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_f_01"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0},"comparisonType":"GreaterOrEqual"}}}` | 1631:0:0 → 1633:0:1; 1633:0:0 → 1637:0:0 |
| `q105_04_jigjig_street.scene / scene / 1645` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_f_02"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0},"comparisonType":"GreaterOrEqual"}}}` | 1643:0:0 → 1645:0:1; 1645:0:0 → 1647:0:0 |
| `q105_04_jigjig_street.scene / scene / 1655` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_m_01"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0},"comparisonType":"GreaterOrEqual"}}}` | 1653:0:0 → 1655:0:1; 1655:0:0 → 1657:0:0 |
| `q105_04_jigjig_street.scene / scene / 1664` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_m_01"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0},"comparisonType":"GreaterOrEqual"}}}` | 1662:0:0 → 1664:0:1; 1664:0:0 → 1666:0:0 |
| `q105_04_jigjig_street.scene / scene / 1681` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_f_01"]}}}}` | 1490:0:0 → 1681:0:1; 1681:0:0 → 1620:0:1; 1681:0:0 → 1631:0:0 |
| `q105_04_jigjig_street.scene / scene / 1686` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_f_02"]}}}}` | 1490:0:0 → 1686:0:1; 1686:0:0 → 1641:0:1; 1686:0:0 → 1643:0:0 |
| `q105_04_jigjig_street.scene / scene / 1691` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_m_01"]}}}}` | 1490:0:0 → 1691:0:1; 1691:0:0 → 1625:0:1; 1691:0:0 → 1653:0:0 |
| `q105_04_jigjig_street.scene / scene / 1696` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#q105_com_jigjig","names":["scan_m_02"]}}}}` | 1490:0:0 → 1696:0:1; 1696:0:0 → 1628:0:1; 1696:0:0 → 1662:0:0 |
| `q105_04_jigjig_street.scene / scene / 1705` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 861:0:0 → 1705:0:1; 1705:0:0 → 1703:0:1 |
| `q105_04_jigjig_street.scene / scene / 1713` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq023_bootleg/mq023_bootleg/01_talk_with_johnny","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 1042:0:0 → 1713:0:1; 1046:0:0 → 1713:0:1; 1713:0:1 → 1714:0:1 |
| `q105_04_jigjig_street.scene / scene / 1714` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#q105_tr_jigjig_street"}}` | 1713:0:1 → 1714:0:1; 1714:0:0 → 1808:0:1 |
| `mq023_bootleg.questphase / h52 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq023_speaker"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0}}}}` | 0:Out → 2:In; 2:Out → 5:In |
| `mq023_bootleg_01_hook.questphase / h0 / 26` | `questCutControlNodeDefinition` `{}` | 4:mq023_johnny_out → 26:In; 26:Out → 15:In; 26:CutSource → 25:CutDestination |
| `mq023_bootleg_01_hook.questphase / h0 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq023_bootleg_performer"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0},"comparisonType":"LessOrEqual"}},{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq023_bootleg_performer"},"timeInterval":0.5,"angleTolerance":60.0}}]}}` | 3:Out1 → 29:In; 29:Out → 6:In |
| `mq023_bootleg_01_hook.questphase / h109 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq023_tr_content_manager_loop"}}` | 7:Out1 → 3:In; 3:Out → 9:In |
| `mq023_bootleg_01_hook.questphase / h109 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq023_tr_content_manager_loop"}}` | 10:Out → 5:In; 12:Out → 5:In; 5:Out → 8:In |
| `mq023_bootleg_02_diner.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq023_tr_diner_entrance"}}` | 0:Out → 2:In; 2:Out → 7:Succeeded |
| `mq023_bootleg_02_diner.questphase / h0 / 17` | `questCutControlNodeDefinition` `{}` | 9:End 0 → 17:In; 17:CutSource → 16:CutDestination; 17:Out → 19:In |
| `mq023_bootleg_02_diner.questphase / h69 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq023_tr_diner_inside"}}` | 7:Out1 → 3:In; 3:Out → 9:In |
| `mq023_bootleg_02_diner.questphase / h69 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq023_tr_diner_inside"}}` | 0:Out → 5:In; 4:Out → 5:In; 5:Out → 8:In |
| `mq023_bootleg_03_vendor.questphase / h0 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq023_tr_vendor_shop"}}` | 24:Out → 3:In; 3:Out → 4:Succeeded |
| `mq023_bootleg_03_vendor.questphase / h0 / 20` | `questCutControlNodeDefinition` `{}` | 7:End 0 → 20:In; 20:Out → 17:In; 20:CutSource → 18:CutDestination |
| `mq023_bootleg_03_vendor.questphase / h80 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq023_tr_content_manager_loop_stand"}}` | 0:Out → 2:In; 5:Out → 2:In; 2:Out → 6:In1 |
| `mq023_bootleg_03_vendor.questphase / h80 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq023_tr_content_manager_loop_stand"}}` | 4:Out → 3:In; 3:Out → 5:In |
| `mq023_01_johnny.scene / scene / 79` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq023_01_johnny_johnny"},"timeInterval":0.10000000149011612,"angleTolerance":80.0,"inverted":true}}}` | 79:0:0 → 206:0:1; 239:0:0 → 79:0:1 |
| `mq023_01_johnny.scene / scene / 95` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq023_01_johnny_johnny"},"timeInterval":0.10000000149011612,"angleTolerance":80.0,"inverted":true}}}` | 82:0:0 → 95:0:1; 95:0:0 → 94:0:1 |
| `mq023_02_dinner.scene / scene / 23` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq023_02_dinner_johnny"},"timeInterval":0.10000000149011612,"angleTolerance":80.0,"inverted":true}}}` | 23:0:0 → 134:0:1; 185:0:0 → 23:0:1 |
| `mq023_02_dinner.scene / scene / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq023_tr_diner_inside"}}` | 51:0:0 → 12:0:0; 185:0:1 → 51:0:1 |
| `mq023_02_dinner.scene / scene / 145` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 141:0:0 → 145:0:1; 145:0:0 → 158:0:0 |
| `mq023_02_dinner.scene / scene / 148` | `questConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq023_tr_johnnyspawn"}}` | 148:0:0 → 151:0:0; 148:0:1 → 176:0:0; 158:0:1 → 148:0:1 |
| `mq023_02_dinner.scene / scene / 163` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 158:0:0 → 163:0:1; 163:0:0 → 121:0:1 |
| `mq023_02_dinner.scene / scene / 225` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq023_02_dinner_johnny"},"timeInterval":0.10000000149011612,"angleTolerance":80.0,"inverted":true}}}` | 225:0:0 → 227:0:1; 247:0:0 → 225:0:1 |
| `mq023_02_dinner.scene / scene / 234` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 206:0:0 → 234:0:1; 234:0:0 → 230:0:0 |
| `mq023_03_street_vendor.scene / scene / 118` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_kerry_insult","value":1,"comparisonType":"GreaterOrEqual"}}}` | 85:0:0 → 118:0:1; 118:0:0 → 120:0:0; 118:0:1 → 122:0:0 |
| `mq023_03_street_vendor.scene / scene / 149` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterEquippedItem_ConditionType","isPlayer":true,"itemID":"112185654454"}}}` | 7:0:0 → 149:0:1; 149:0:0 → 153:0:0; 149:0:1 → 651:0:1 |
| `mq023_03_street_vendor.scene / scene / 179` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"119498216216","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 178:0:0 → 179:0:1; 179:0:0 → 203:0:0 |
| `mq023_03_street_vendor.scene / scene / 316` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq023_03_street_vendor_johnny"},"timeInterval":0.10000000149011612,"angleTolerance":80.0,"inverted":true}}}` | 316:0:0 → 472:0:1; 700:0:0 → 316:0:1 |
| `mq023_03_street_vendor.scene / scene / 360` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\minor_quests\\mq023\\scenes\\mq023_03_street_vendor.scene","Flags":"Soft"},"sectionName":"mq023_03_fluff","type":"IsOutside"}}}` | 9:0:1 → 360:0:1; 360:0:0 → 10:0:0 |
| `mq023_03_street_vendor.scene / scene / 374` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSectionNode_ConditionType","sceneFile":{"DepotPath":"base\\quest\\minor_quests\\mq023\\scenes\\mq023_03_street_vendor.scene","Flags":"Soft"},"sectionName":"mq023_03_LaserPop","type":"IsOutside"}}}` | 4:0:1 → 374:0:1; 374:0:0 → 71:0:0 |
| `mq023_03_street_vendor.scene / scene / 516` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq023_bootleg_karim","names":["karim"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":6.0},"comparisonType":"Less"}}}` | 516:0:0 → 542:0:0; 560:0:0 → 516:0:1 |
| `mq023_03_street_vendor.scene / scene / 546` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 544:0:0 → 546:0:1; 546:0:0 → 552:0:0 |
| `mq023_03_street_vendor.scene / scene / 548` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 544:0:1 → 548:0:1; 548:0:0 → 552:0:0 |
| `mq023_03_street_vendor.scene / scene / 550` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 544:0:2 → 550:0:1; 550:0:0 → 552:0:0 |
| `mq023_03_street_vendor.scene / scene / 560` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_keepalive","value":1,"comparisonType":"Equal"}}}` | 560:0:0 → 516:0:1; 560:0:1 → 566:0:1; 743:0:0 → 560:0:1 |
| `mq023_03_street_vendor.scene / scene / 566` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_keepalive","value":1,"comparisonType":"Equal"}}}` | 560:0:1 → 566:0:1; 566:0:0 → 622:0:0; 617:0:0 → 566:0:1 |
| `mq023_03_street_vendor.scene / scene / 620` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_keepalive","comparisonType":"Equal"}}}` | 620:0:0 → 617:0:0; 622:0:1 → 620:0:1 |
| `mq023_03_street_vendor.scene / scene / 628` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 617:1:0 → 628:0:0; 622:0:0 → 628:0:1; 628:0:0 → 542:0:0 |
| `mq023_03_street_vendor.scene / scene / 711` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_keepalive","value":1,"comparisonType":"Equal"}}}` | 704:0:1 → 711:0:1; 711:0:0 → 1016:0:1; 736:0:0 → 711:0:1; 1039:0:0 → 711:0:1; 1054:1:0 → 711:0:0 |
| `mq023_03_street_vendor.scene / scene / 733` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_keepalive","comparisonType":"Equal"}}}` | 714:0:0 → 733:0:1; 733:0:0 → 1028:0:1; 1054:1:0 → 733:0:0 |
| `mq023_03_street_vendor.scene / scene / 790` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 222:0:0 → 790:0:1; 790:0:0 → 178:0:1 |
| `mq023_03_street_vendor.scene / scene / 803` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_keepalive","value":1,"comparisonType":"Equal"}}}` | 803:0:0 → 808:0:1; 803:0:1 → 805:0:1; 1039:0:1 → 803:0:1; 1075:0:0 → 803:0:1 |
| `mq023_03_street_vendor.scene / scene / 805` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_keepalive","comparisonType":"Equal"}}}` | 803:0:1 → 805:0:1; 805:0:0 → 1267:0:1; 810:0:0 → 805:0:1; 1054:1:0 → 805:0:0 |
| `mq023_03_street_vendor.scene / scene / 808` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_keepalive","value":1,"comparisonType":"Equal"}}}` | 803:0:0 → 808:0:1; 808:0:0 → 810:0:0; 1054:1:0 → 808:0:0 |
| `mq023_03_street_vendor.scene / scene / 922` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq023_03_street_vendor_johnny"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"LessOrEqual"}}}` | 922:0:0 → 106:0:0; 958:0:0 → 922:0:1 |
| `mq023_03_street_vendor.scene / scene / 949` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 196:0:0 → 949:0:1; 949:0:0 → 1069:0:1 |
| `mq023_03_street_vendor.scene / scene / 976` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq023_bootleg_karim","names":["karim"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.5},"comparisonType":"GreaterOrEqual"}}}` | 958:0:1 → 976:0:1; 976:0:0 → 990:0:1 |
| `mq023_03_street_vendor.scene / scene / 1016` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_2h_table","value":1,"comparisonType":"Equal"}}}` | 711:0:0 → 1016:0:1; 1016:0:0 → 714:0:0; 1016:0:1 → 1075:0:1 |
| `mq023_03_street_vendor.scene / scene / 1028` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_2h_table","value":1,"comparisonType":"Equal"}}}` | 733:0:0 → 1028:0:1; 1028:0:0 → 736:0:0; 1028:0:1 → 1075:0:0 |
| `mq023_03_street_vendor.scene / scene / 1036` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 965:0:0 → 1036:0:1; 1036:0:0 → 988:0:1 |
| `mq023_03_street_vendor.scene / scene / 1039` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_2h_table","value":1,"comparisonType":"Equal"}}}` | 821:0:0 → 1039:0:1; 1039:0:0 → 711:0:1; 1039:0:1 → 803:0:1 |
| `mq023_03_street_vendor.scene / scene / 1052` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_killbodyidles","value":1,"comparisonType":"Equal"}}}` | 704:0:2 → 1052:0:1; 1052:0:0 → 1054:0:0 |
| `mq023_03_street_vendor.scene / scene / 1100` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"wbr_jpn_clothingshop_02_met"}}}` | 1083:0:0 → 1100:0:1; 1100:0:0 → 1085:0:1; 1100:0:1 → 1099:0:1 |
| `mq023_03_street_vendor.scene / scene / 1134` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq023_bootleg_karim"}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":3.0},"comparisonType":"Less"}}}` | 1095:0:0 → 1134:0:1; 1134:0:0 → 1141:0:0 |
| `mq023_03_street_vendor.scene / scene / 1156` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq023_tr_vendor_shop"}}` | 1091:0:0 → 1156:0:1; 1156:0:0 → 1210:0:1; 1163:0:0 → 1156:0:1 |
| `mq023_03_street_vendor.scene / scene / 1159` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questGatherTriggerCondition","triggerAreaRef":"#mq023_tr_vendor_shop"}}` | 1159:0:0 → 1091:0:1; 1159:0:0 → 1163:0:1; 1210:0:0 → 1159:0:1 |
| `mq023_03_street_vendor.scene / scene / 1163` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":500}}}` | 1159:0:0 → 1163:0:1; 1163:0:0 → 1156:0:1 |
| `mq023_03_street_vendor.scene / scene / 1202` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1,"miliseconds":500}}}` | 1189:0:0 → 1202:0:1; 1197:0:0 → 1202:0:1; 1202:0:0 → 1190:0:0 |
| `mq023_03_street_vendor.scene / scene / 1267` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq023_karim_change_idle","comparisonType":"Equal"}}}` | 805:0:0 → 1267:0:1; 1267:0:0 → 819:0:0; 1267:0:1 → 824:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | q105_04_jigjig_street.scene / scene / 706 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | q105_04_jigjig_street.scene / scene / 1000; q105_04_jigjig_street.scene / scene / 1004; q105_04_jigjig_street.scene / scene / 1701; q105_04_jigjig_street.scene / scene / 1703 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | mq023_bootleg.questphase / h52 / 9; mq023_bootleg_01_hook.questphase / h0 / 8; mq023_bootleg_02_diner.questphase / h0 / 12; mq023_bootleg_03_vendor.questphase / h0 / 22 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq023_01_johnny.scene / scene / 34; mq023_01_johnny.scene / scene / 44; mq023_01_johnny.scene / scene / 54; mq023_02_dinner.scene / scene / 12; +15 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | q105_04_jigjig_street.scene / scene / 1407; q105_04_jigjig_street.scene / scene / 861; q105_04_jigjig_street.scene / scene / 867 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq023_03_street_vendor.scene / scene / 1016; mq023_03_street_vendor.scene / scene / 1028; mq023_03_street_vendor.scene / scene / 1039; mq023_03_street_vendor.scene / scene / 1052; +34 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq023_bootleg_01_hook.questphase / h0 / 15; mq023_bootleg_01_hook.questphase / h109 / 2; mq023_bootleg_01_hook.questphase / h109 / 4; mq023_bootleg_02_diner.questphase / h0 / 19; +6 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq023_bootleg_01_hook.questphase / h0 / 30; mq023_bootleg_01_hook.questphase / h109 / 12; mq023_bootleg_03_vendor.questphase / h0 / 24; mq023_bootleg_03_vendor.questphase / h0 / 25; +12 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `elapsed_time` | q105_04_jigjig_street.scene / scene / 1405 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mq023_03_street_vendor.scene / scene / 179 | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | mq023_01_johnny.scene / scene / 19; mq023_01_johnny.scene / scene / 213; mq023_01_johnny.scene / scene / 29; mq023_01_johnny.scene / scene / 4; +32 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | mq023_02_dinner.scene / scene / 126; mq023_02_dinner.scene / scene / 128; mq023_02_dinner.scene / scene / 137; mq023_03_street_vendor.scene / scene / 1010; +45 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | mq023_02_dinner.scene / scene / 145; mq023_02_dinner.scene / scene / 163; mq023_02_dinner.scene / scene / 234; mq023_03_street_vendor.scene / scene / 1036; +12 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq023_bootleg_01_hook.questphase / h0 / 26; mq023_bootleg_02_diner.questphase / h0 / 17; mq023_bootleg_03_vendor.questphase / h0 / 20 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq023_bootleg_03_vendor.questphase / h0 / 13 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | q105_04_jigjig_street.scene / scene / 1595; q105_04_jigjig_street.scene / scene / 1596; q105_04_jigjig_street.scene / scene / 1681; q105_04_jigjig_street.scene / scene / 1686; +7 locations in catalogue.json | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | mq023_bootleg_01_hook.questphase / h0 / 4; mq023_bootleg_02_diner.questphase / h0 / 9; mq023_bootleg_03_vendor.questphase / h0 / 7; mq023_quest_bugfixes.questphase / h305 / 12 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq023_02_dinner.scene / scene / 148; mq023_02_dinner.scene / scene / 51; mq023_bootleg_01_hook.questphase / h109 / 3; mq023_bootleg_01_hook.questphase / h109 / 5; +13 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `vehicle_control` | mq023_bootleg.questphase / h52 / 17 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mq023_01_johnny.scene / scene / 182; mq023_01_johnny.scene / scene / 197; mq023_01_johnny.scene / scene / 206; mq023_01_johnny.scene / scene / 228; +74 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` | repair; journal anchor | `base-mq023` |
| `base\quest\main_quests\part1\q105\scenes\q105_04_jigjig_street.scene` | content candidate; journal anchor | `base-q105` |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` | content candidate; journal anchor | `base-mq023` |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_01_hook.questphase` | content candidate; forward dependency | `base-mq023` |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_02_diner.questphase` | content candidate; journal anchor | `base-mq023` |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_03_vendor.questphase` | content candidate; journal anchor | `base-mq023` |
| `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene` | content candidate; journal anchor | `base-mq023` |
| `base\quest\minor_quests\mq023\scenes\mq023_02_dinner.scene` | content candidate; journal anchor | `base-mq023` |
| `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` | content candidate; journal anchor | `base-mq023` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq042](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq042.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q108](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q108.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

454 repeated typed/socket path signatures in this selected graph context; 80 distinct direct resource identities; 17 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `8cd3b647ae3f592ad947` | `base\quest\main_quests\part1\q105\scenes\q105_04_jigjig_street.scene` / scene / 1421 -> 29 -> 1446 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `6497920d6ce0ac894daa` | `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h172 / 22 -> 24 -> 23 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; True -> In |
| `eaf5aab427d50e5598b6` | `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h30 / 0 -> 8 -> 2 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `f3d4655cd61f691d52d7` | `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h265 / 4 -> 12 -> 10 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; Out -> In |
| `4e9253a72e6b0134b8dd` | `base\quest\minor_quests\mq023\phases\mq023_bootleg_02_diner.questphase` / h0 / 2 -> 7 -> 4 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `bbf9efd740881cf31a37` | `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` / scene / 620 -> 617 -> 628 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `cbae0fd3078e68426197` | `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h0 / 19 -> 25 -> 24 | questDeletionMarkerNodeDefinition -> questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `8a23917edc2bf62cc99e` | `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h172 / 21 -> 24 -> 23 | questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; False -> In; True -> In |
| `3fe0ae98a8cf5496b004` | `base\quest\minor_quests\mq023\phases\mq023_bootleg_03_vendor.questphase` / h80 / 4 -> 3 -> 5 | questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition] -> questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]; Out -> In; Out -> In |
| `eb252b7e42db30cea85d` | `base\quest\minor_quests\mq023\phases\mq023_bootleg_03_vendor.questphase` / h80 / 3 -> 5 -> 2 | questPauseConditionNodeDefinition[questTriggerCondition] -> questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `19665e3783f6f51a7337` | `base\quest\main_quests\part1\q105\scenes\q105_04_jigjig_street.scene` / scene / 1458 -> 506 -> 1367 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `95d4997362b664c5c23b` | `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene` / scene / 50 -> 54 -> 56 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 2:0 -> 0:0; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h0 / 1 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h0 / 12 | `h30` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h0 / 17 | `h124` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h0 / 22 | `h172` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h0 / 23 | `h265` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h265 / 9 | `h286` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":13,"socketName":"Out1"}] |
| `base\quest\bugfixing\minor_quests\mq023\mq023_quest_bugfixes.questphase` / h286 / 9 | `h305` | [{"$type":"questInputNodeDefinition","id":5,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":6,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` / h0 / 3 | `h26` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` / h0 / 4 | `h40` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` / h0 / 5 | `h52` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` / h0 / 10 | `h125` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq023\mq023_bootleg.questphase` / h0 / 11 | `h178` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_01_hook.questphase` / h0 / 3 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_01_hook.questphase` / h0 / 25 | `h109` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_02_diner.questphase` / h0 / 16 | `h69` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_03_vendor.questphase` / h0 / 18 | `h80` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"}] |

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
| `base\quest\minor_quests\mq042\mq042_nomad.gamedef` | content candidate | base\quest\minor_quests\mq042\mq042_nomad.quest |
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
| `base\quest\main_quests\part1\q105\definitions\q105_braindance.gamedef` | content candidate | base\quest\main_quests\part1\q105\definitions\q105_braindance.quest |
| `base\quest\main_quests\part1\q105\definitions\q105_dollhouse.gamedef` | content candidate | base\quest\main_quests\part1\q105\definitions\q105_dollhouse.quest |
| `base\quest\main_quests\part1\q105\definitions\q105_fingers.gamedef` | content candidate | base\quest\main_quests\part1\q105\definitions\q105_fingers.quest |
| `base\quest\main_quests\part1\q105\definitions\q105_jigjig.gamedef` | content candidate | base\quest\main_quests\part1\q105\definitions\q105_jigjig.quest |
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
| `base\quest\demos\handson_2020\handson_2020_kabuki.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_kabuki.quest |
| `base\quest\demos\handson_2020\handson_2020_little_china.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_little_china.quest |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest |
| `base\quest\demos\handson_2020\handson_2020_scavengers.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_scavengers.quest |
| `base\quest\demos\handson_2020\handson_2020_speed_test.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_speed_test.quest |
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
| `base\animations\facial\generic\interactive_scene\generic_facial_additives.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand__rh_on_hip__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\female_average\interactive_scene\generic_female_average__stand_wall_lean180__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_stand__rh_hotdog__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_stand_bar_lean0__2h_on_bar__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_barstool_bar_lean270__lh_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_hip__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_bar_lean0__2h_on_bar__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_wall_lean180__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__sit_ledge_lean0__rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__stand__lh_fries__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_male_average_work__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_bench_lean0__lh_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__sit_chair_lean0__rh_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand__lh_pocket__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__stand_wall_lean180__lh_pocket__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\main_characters\johnny\interactive_scene\johnny__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\quest\side_quests\sq032\sq032_04_fourth_episode\sq032_04_fourth_episode__johnny.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_low_f_100_jap_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_low_m_09_enus_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_low_m_107_bra_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_low_m_10_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_low_m_119_rus_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_mid_m_04_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_mid_m_38_afam_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_prst_f_01_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_prst_f_02_afam_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_prst_f_03_mex_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_prst_f_04_chn_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_prst_f_05_jap_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_prst_m_01_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_prst_m_02_afam_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\civ_prst_m_03_mex_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\judy.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\main_quests\part1\q105\scenes\lipsync\en\q105_04_jigjig_street\votest_andrew.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_01_hook.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_02_diner.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq023\phases\mq023_bootleg_03_vendor.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq023\scenes\lipsync\en\mq023_01_johnny\civ_low_m_15_enus_25.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq023\scenes\lipsync\en\mq023_01_johnny\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq023\scenes\lipsync\en\mq023_01_johnny\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq023\scenes\lipsync\en\mq023_02_dinner\civ_low_m_100_jap_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq023\scenes\lipsync\en\mq023_02_dinner\civ_low_m_123_arb_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq023\scenes\lipsync\en\mq023_02_dinner\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq023\scenes\lipsync\en\mq023_02_dinner\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq023\scenes\lipsync\en\mq023_03_street_vendor\civ_low_m_30_enus_50.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq023\scenes\lipsync\en\mq023_03_street_vendor\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq023\scenes\lipsync\en\mq023_03_street_vendor\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq023\scenes\mq023_02_dinner.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\archetype\corpo\corpo__stand_ground__look_at_products__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\archetype\corpo\corpo__stand_ground_hotdog__eat__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\bar\generic__stand_bar_lean_front__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\bar_and_barstool\generic__sit_barstool_bar_lean_left__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\big__stand_ground__look_at_products__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__look_at_products__03.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__03.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__wait__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground_fries_cone__eat__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ledge\generic__sit_ledge__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\dirt__stand_wall_lean_back_cigarette__smoke__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\generic__stand_wall_lean_back__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_bench__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__sit_chair_lean_front__sit_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_ground__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\main_characters\johnny\johnny__stand_wall_lean_back__think__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\side_quests\sq031\sq031_01a_smack_afterlife\sq031__johnny__stand__wait_nervous__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\quest\side_quests\sq031\sq031_05_grave\sq_031__johnny__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `CYB-12345` | base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_cct_dtn_07\ma_cct_dtn_07_quest_bugfixes.questphase / h7 / 2; base\quest\bugfixing\minor_quests\ma_hey_spr_04\ma_hey_spr_04_quest_bugfixes.questphase / h7 / 2; 182 total source locations in compressed evidence |
| `censorship_homosexuality` | base\quest\side_quests\sq017\test\sq017_chicken_test.scene / scene / 55; base\quest\side_quests\sq026\definitions\sq026_chicken_test.scene / scene / 468; base\quest\side_quests\sq030\definitions\sq030_chicken_test.scene / scene / 155; 3 total source locations in compressed evidence |
| `q101_kerry_insult` | base\quest\main_quests\part1\q101\scenes\q101_06c_memories_backalley_p1.scene / scene / 1152; base\quest\main_quests\part1\q101\scenes\q101_06c_memories_backalley_p1.scene / scene / 1154; 2 total source locations in compressed evidence |
| `wbr_jpn_food_01_default_on` | base\open_world\vendors\westbrook\japantown\japantown_vendors.questphase / h0 / 27; 1 total source locations in compressed evidence |

NodeRef uses: 266; TweakDB binding uses: 57. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\main_quests\part1\q105\scenes\q105_04_jigjig_street.scene` | 36 / 146 | scnChangeIdleAnimEvent: 3; scnDialogLineEvent: 51; scnLookAtEvent: 26; scnPlaySkAnimEvent: 34; scnPoseCorrectionEvent: 2; scneventsSocket: 27; scneventsUnequipItemFromPerformerByItem: 2; scneventsVFXEvent: 1 |
| `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene` | 12 / 105 | scnChangeIdleAnimEvent: 26; scnDialogLineEvent: 30; scnLookAtEvent: 18; scnPlaySkAnimEvent: 20; scneventsSocket: 9; scneventsVFXEvent: 2 |
| `base\quest\minor_quests\mq023\scenes\mq023_02_dinner.scene` | 9 / 79 | scnChangeIdleAnimEvent: 23; scnDialogLineEvent: 21; scnLookAtEvent: 15; scnOverridePhantomParamsEvent: 3; scnPlaySkAnimEvent: 13; scneventsSocket: 4 |
| `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene` | 48 / 336 | scnChangeIdleAnimEvent: 83; scnDialogLineEvent: 81; scnLookAtEvent: 28; scnOverridePhantomParamsEvent: 2; scnPlaySkAnimEvent: 99; scneventsEquipItemToPerformer: 1; scneventsSocket: 40; scneventsVFXEvent: 2 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
