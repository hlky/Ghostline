# Gig: Lousy Kleppers

Journal: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06` · `StreetStory` · hash `4132951293`.

Journal premise: Gig type: Thievery\nObjective: Steal the databank with the transport route data from Malorian Ltd.\nLocation: Warehouse, Offshore St.\nDetails:\n\nV, big news going around town. A Malorian van was stolen on Sir Francis Drake avenue. Maelstrom claimed responsibility.\n\nIt just so happens that one of my informants saw the whole thing, and he was smart enough to tail them using a drone.\n\nHard part's over – we already know where they've stashed the van. I'd say we got lucky, but the truth is my people know how to get shit done. OK, OK, I'll quit flattering myself.\n\nGo to the chop shop and find a databank in the van that has Malorian's transport route data. The gangers have no idea it's worth more than the all the cargo they're sitting on.

**Coverage: journal-linked.** 33 exact journal-linked nodes in 4 resources; 6 resources in the inspected dependency context.

Resource roles in that context: 4 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`; `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest`; `base\quest\demos\handson_2020\handson_2020_speed_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Deposit the databank in the Drop Point. (Primary) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/deliver_files` |
| Leave the area. (Primary) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/escape_abandoned_warehouse` |
| Get inside the Maelstrom warehouse. (Primary) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/get_inside` |
| Find the databank from the Malorian van. (Primary) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/locate_data_drive` |
| Steal the databank. (Primary) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/take` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_wat_nid_06_openworld.questphase / h126 / 3` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/take` | 73:Out → 3:Active; 3:Out → 107:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 4` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/get_inside` | 80:True → 4:Active; 4:Out → 60:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 8` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/get_inside` | 60:Out → 8:Succeeded; 8:Out → 69:Active |
| `sts_wat_nid_06_openworld.questphase / h126 / 9` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/take` | 107:Out → 9:Succeeded; 9:Out → 14:Active; 9:Out → 118:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 14` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/escape_abandoned_warehouse` | 14:Out → 7:In; 9:Out → 14:Active |
| `sts_wat_nid_06_openworld.questphase / h126 / 15` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/escape_abandoned_warehouse` | 7:Out → 15:Succeeded; 15:Out → 21:Active |
| `sts_wat_nid_06_openworld.questphase / h126 / 21` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/deliver_files` | 15:Out → 21:Active; 21:Out → 133:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 23` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/deliver_files` | 133:Out → 23:Succeeded; 23:Out → 26:Succeeded |
| `sts_wat_nid_06_openworld.questphase / h126 / 26` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06` | 23:Out → 26:Succeeded; 26:Out → 121:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 64` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/brief` | 86:Out → 64:Active |
| `sts_wat_nid_06_openworld.questphase / h126 / 67` (MappinManager) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/locate_data_drive/area_shard` | 76:Out1 → 67:Inactive; 67:Out → 68:Active |
| `sts_wat_nid_06_openworld.questphase / h126 / 68` (MappinManager) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/take/take_mp` | 67:Out → 68:Active; 68:Out → 73:Succeeded |
| `sts_wat_nid_06_openworld.questphase / h126 / 69` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/locate_data_drive` | 8:Out → 69:Active; 69:Out → 70:In; 69:Out → 75:In; 69:Out → 132:In1 |
| `sts_wat_nid_06_openworld.questphase / h126 / 73` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/locate_data_drive` | 73:Out → 3:Active; 68:Out → 73:Succeeded; 130:Out → 73:Succeeded |
| `sts_wat_nid_06_openworld.questphase / h126 / 81` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/get_inside` | 81:Out → 60:In; 80:False → 81:Active |
| `sts_wat_northside_industrial_district.questphase / h12972 / 3` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/take` | 73:Out → 3:Active; 3:Out → 107:In |
| `sts_wat_northside_industrial_district.questphase / h12972 / 4` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/get_inside` | 80:True → 4:Active; 4:Out → 60:In |
| `sts_wat_northside_industrial_district.questphase / h12972 / 8` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/get_inside` | 60:Out → 8:Succeeded; 8:Out → 69:Active |
| `sts_wat_northside_industrial_district.questphase / h12972 / 9` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/take` | 107:Out → 9:Succeeded; 9:Out → 14:Active; 9:Out → 118:In |
| `sts_wat_northside_industrial_district.questphase / h12972 / 14` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/escape_abandoned_warehouse` | 14:Out → 7:In; 9:Out → 14:Active |
| `sts_wat_northside_industrial_district.questphase / h12972 / 15` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/escape_abandoned_warehouse` | 7:Out → 15:Succeeded; 15:Out → 21:Active |
| `sts_wat_northside_industrial_district.questphase / h12972 / 21` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/deliver_files` | 15:Out → 21:Active; 21:Out → 133:In |
| `sts_wat_northside_industrial_district.questphase / h12972 / 23` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/deliver_files` | 133:Out → 23:Succeeded; 23:Out → 26:Succeeded |
| `sts_wat_northside_industrial_district.questphase / h12972 / 26` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06` | 23:Out → 26:Succeeded; 26:Out → 121:In |
| `sts_wat_northside_industrial_district.questphase / h12972 / 64` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/brief` | 86:Out → 64:Active |
| `sts_wat_northside_industrial_district.questphase / h12972 / 67` (MappinManager) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/locate_data_drive/area_shard` | 76:Out1 → 67:Inactive; 67:Out → 68:Active |
| `sts_wat_northside_industrial_district.questphase / h12972 / 68` (MappinManager) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/take/take_mp` | 67:Out → 68:Active; 68:Out → 73:Succeeded |
| `sts_wat_northside_industrial_district.questphase / h12972 / 69` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/locate_data_drive` | 8:Out → 69:Active; 69:Out → 70:In; 69:Out → 75:In; 69:Out → 132:In1 |
| `sts_wat_northside_industrial_district.questphase / h12972 / 73` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/locate_data_drive` | 73:Out → 3:Active; 68:Out → 73:Succeeded; 130:Out → 73:Succeeded |
| `sts_wat_northside_industrial_district.questphase / h12972 / 81` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/get_inside` | 81:Out → 60:In; 80:False → 81:Active |
| `mq036_quest_bugfixes.questphase / h870 / 259` (Condition) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/deliver_files` | 259:False → 246:In; 253:False → 259:In; 257:Out → 259:In; 259:True → 260:In |
| `open_world_bugfixing.questphase / h116 / 91` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06` | 47:True → 91:Succeeded |
| `open_world_bugfixing.questphase / h2878 / 91` (Journal) | `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06` | 47:True → 91:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_wat_nid_06_openworld.questphase / h126 / 119` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_prebrief.scene`; `#sts_sm_wat_nid_06_holocall_prebrief` | 119:End 0 → 93:Active; 119:rejected_out → 93:Active; 124:True → 119:Start 0; 119:Holocall INT → 126:In; 119:Holocall RET → 125:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 120` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene`; `#sts_sm_wat_nid_06_holocall_debrief` | 120:End 0 → 91:In; 142:False → 120:Start 0; 120:rejected_out → 141:Active; 120:Holocall INT → 128:In; 120:Holocall RET → 127:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_phase.questphase` / h0 / 16 | `sts_wat_nid_06_openworld.questphase` | 9: Input; 9:Out → 16:In1; 16:Out1 → 22:In |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_northside_industrial_district.questphase` / h6330 / 16 | `sts_wat_nid_06_openworld.questphase` | 9: Input; 9:Out → 16:In1; 16:Out1 → 22:In |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` / h126 / 120 | `sts_wat_nid_06_holocall_debrief.scene` | 142: Condition; 120:End 0 → 91:In; 142:False → 120:Start 0; 120:rejected_out → 141:Active; 120:Holocall INT → 128:In; 120:Holocall RET → 127:In |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_northside_industrial_district.questphase` / h12972 / 120 | `sts_wat_nid_06_holocall_debrief.scene` | 142: Condition; 120:End 0 → 91:In; 142:False → 120:Start 0; 120:rejected_out → 141:Active; 120:Holocall INT → 128:In; 120:Holocall RET → 127:In |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` / h126 / 119 | `sts_wat_nid_06_holocall_prebrief.scene` | 124: Condition; 119:End 0 → 93:Active; 119:rejected_out → 93:Active; 124:True → 119:Start 0; 119:Holocall INT → 126:In; 119:Holocall RET → 125:In |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_northside_industrial_district.questphase` / h12972 / 119 | `sts_wat_nid_06_holocall_prebrief.scene` | 124: Condition; 119:End 0 → 93:Active; 119:rejected_out → 93:Active; 124:True → 119:Start 0; 119:Holocall INT → 126:In; 119:Holocall RET → 125:In |
| `base\open_world\street_stories\watson\sts_watson.questphase` / h0 / 4 | `sts_wat_northside_industrial_district.questphase` | 0: Input; 0:Out → 4:In1 |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest` / h0 / 3 | `sts_wat_northside_industrial_district.questphase` | 0: Start; 0:Out → 3:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h397 / 4 | `sts_wat_northside_industrial_district.questphase` | 0: Input; 0:Out → 4:In1 |
| `base\quest\bugfixing\quest_bugfixing.questphase` / h233 / 54 | `mq036_quest_bugfixes.questphase` | 20: LogicalHub; 20:Out1 → 54:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\sts_wat_nid_06_quest.quest` / h0 / 12 | `sts_wat_nid_06_phase.questphase` | 13: FactsDBManager: nid_06_testdef; 12:Out1 → 1:In; 13:Out → 12:In1 |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_northside_industrial_district.questphase` / h0 / 11 | `sts_wat_nid_06_phase.questphase` | 28: Journal; 70: Journal; 28:Out → 11:In1; 70:Out → 11:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 7 | `sts_watson.questphase` | 0: Input; 0:Out → 7:In1 |
| `base\quest\bugfixing.questphase` / h0 / 9 | `quest_bugfixing.questphase` | 16: DeletionMarker; 9:Out_res_act1 → 20:In; 16:Out → 9:In1; 9:to_mq025 → 55:In |
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
| `base\open_world\community\heywood\wellsprings\hey_spr_quest.quest` / h0 / 4 | `street_stories.questphase` | 1: Start; 1:Out → 4:In1 |
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.quest` / h0 / 21 | `street_stories.questphase` | 0: Start; 0:Out → 21:In1 |
| `base\open_world\phases\open_world_content.questphase` / h0 / 2 | `street_stories.questphase` | 33: PauseCondition: sts_loop_start; 122: Input; 33:Out → 2:In1; 122:Out → 2:In1 |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
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
| `sts_wat_nid_06_holocall_debrief.scene` | Start 0 → End 0, rejected_out | fixer; Player; 23 nodes / 30 edges |
| `sts_wat_nid_06_holocall_prebrief.scene` | Start 0 → End 0, rejected_out | fixer; Player; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `holo_active_call_interrupted` | Producer outside selected context | sts_wat_nid_06_holocall_prebrief.scene / scene / 279 |
| `holo_reggie_calls_v_end_activate` | sts_wat_nid_06_holocall_debrief.scene / scene / 69; sts_wat_nid_06_holocall_prebrief.scene / scene / 69; sts_wat_nid_06_openworld.questphase / h126 / 126; sts_wat_nid_06_openworld.questphase / h126 / 128 | No reader in selected context |
| `holo_reggie_calls_v_end_done` | sts_wat_nid_06_holocall_debrief.scene / scene / 65; sts_wat_nid_06_holocall_prebrief.scene / scene / 65 | sts_wat_nid_06_holocall_debrief.scene / scene / 64; sts_wat_nid_06_holocall_prebrief.scene / scene / 64 |
| `holo_reggie_calls_v_rejectable` | sts_wat_nid_06_holocall_debrief.scene / scene / 279; sts_wat_nid_06_holocall_prebrief.scene / scene / 254; sts_wat_nid_06_holocall_prebrief.scene / scene / 285 | No reader in selected context |
| `holo_reggie_calls_v_rejected` | sts_wat_nid_06_holocall_debrief.scene / scene / 281; sts_wat_nid_06_holocall_prebrief.scene / scene / 256 | sts_wat_nid_06_holocall_debrief.scene / scene / 283; sts_wat_nid_06_holocall_prebrief.scene / scene / 258 |
| `holo_reggie_calls_v_start_activate` | sts_wat_nid_06_holocall_debrief.scene / scene / 261; sts_wat_nid_06_holocall_debrief.scene / scene / 68; sts_wat_nid_06_holocall_prebrief.scene / scene / 283; sts_wat_nid_06_holocall_prebrief.scene / scene / 68; sts_wat_nid_06_openworld.questphase / h126 / 125; sts_wat_nid_06_openworld.questphase / h126 / 127 | sts_wat_nid_06_holocall_debrief.scene / scene / 251 |
| `holo_reggie_calls_v_start_done` | sts_wat_nid_06_holocall_debrief.scene / scene / 63; sts_wat_nid_06_holocall_prebrief.scene / scene / 63 | sts_wat_nid_06_holocall_debrief.scene / scene / 267; sts_wat_nid_06_holocall_prebrief.scene / scene / 267 |
| `holo_setup_active` | Producer outside selected context | sts_wat_nid_06_holocall_debrief.scene / scene / 251; sts_wat_nid_06_holocall_prebrief.scene / scene / 279 |
| `holo_setup_started` | Producer outside selected context | sts_wat_nid_06_holocall_debrief.scene / scene / 251; sts_wat_nid_06_holocall_prebrief.scene / scene / 279 |
| `nid_06_finished` | sts_wat_nid_06_openworld.questphase / h126 / 91 | open_world_bugfixing.questphase / h116 / 47; open_world_bugfixing.questphase / h2878 / 47 |
| `nid_06_start` | sts_wat_nid_06_openworld.questphase / h126 / 86; sts_wat_northside_industrial_district.questphase / h12972 / 86 | No reader in selected context |
| `nid_06_testdef` | Producer outside selected context | sts_wat_nid_06_openworld.questphase / h126 / 80; sts_wat_northside_industrial_district.questphase / h12972 / 80 |
| `sts_wat_nid_06_data_drive` | Producer outside selected context | sts_wat_nid_06_openworld.questphase / h126 / 133; sts_wat_northside_industrial_district.questphase / h12972 / 133 |
| `wat_achievement` | sts_wat_nid_06_openworld.questphase / h573 / 34 | sts_wat_nid_06_openworld.questphase / h573 / 35 |

## Exact gates, joins and cancellation

<details><summary>54 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_wat_nid_06_openworld.questphase / h12 / 23` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 7:Out → 23:In3; 10:Out → 23:In2; 13:Out → 23:In4; 14:Out → 23:In1; 23:Out1 → 21:In |
| `sts_wat_nid_06_openworld.questphase / h12 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#nid_06_tr_start"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 31:Out → 24:In; 32:Out → 31:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Exited","triggerAreaRef":"#wat_nid_tr_escape"}}` | 14:Out → 7:In; 7:Out → 15:Succeeded; 7:Out → 117:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"XOR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#wat_nid_tr_inside_maelstrom_leader_chat_003"},{"$type":"questTriggerCondition","triggerAreaRef":"#wat_nid_tr_inside_maelstrom_004_001"},{"$type":"questTriggerCondition","triggerAreaRef":"#wat_nid_tr_inside_maelstrom_003_001"},{"$type":"questTriggerCondition","triggerAreaRef":"#wat_nid_tr_inside_maelstrom_005"}]}}` | 4:Out → 60:In; 60:Out → 8:Succeeded; 81:Out → 60:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#nid_06_dvc_objective"},"eventType":"Finished"}}}` | 69:Out → 70:In; 70:Out → 76:In1 |
| `sts_wat_nid_06_openworld.questphase / h126 / 75` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#nid_06_dvc_objective"},"timeInterval":2.0,"angleTolerance":20.0}}}` | 69:Out → 75:In; 75:Out → 76:In2 |
| `sts_wat_nid_06_openworld.questphase / h126 / 76` | `questLogicalXorNodeDefinition` `{}` | 76:Out1 → 67:Inactive; 70:Out → 76:In1; 75:Out → 76:In2 |
| `sts_wat_nid_06_openworld.questphase / h126 / 80` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"nid_06_testdef","value":1,"comparisonType":"GreaterOrEqual"}}}` | 80:True → 4:Active; 86:Out → 80:In; 80:False → 81:Active |
| `sts_wat_nid_06_openworld.questphase / h126 / 97` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sts_wat_nid_06_enemies_outside"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 86:Out → 97:In; 97:Out → 101:In2 |
| `sts_wat_nid_06_openworld.questphase / h126 / 98` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#sts_wat_nid_06_enemies_inside_ground_floor"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 86:Out → 98:In; 98:Out → 101:In1 |
| `sts_wat_nid_06_openworld.questphase / h126 / 101` | `questLogicalAndNodeDefinition` `{}` | 101:Out1 → 95:In; 101:Out1 → 96:In; 97:Out → 101:In2; 98:Out → 101:In1 |
| `sts_wat_nid_06_openworld.questphase / h126 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"130317604731","comparisonType":"Greater"}}}` | 3:Out → 107:In; 107:Out → 9:Succeeded; 107:Out → 122:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#wat_nid_tr_escape"}}` | 93:Out → 113:In; 113:Out → 112:In; 115:Out → 113:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#wat_nid_tr_escape"}}` | 112:Out → 114:In; 114:Out → 115:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 121` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 26:Out → 121:In; 121:Out → 137:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 124` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 124:False → 93:Active; 124:True → 119:Start 0; 139:False → 124:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 130` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"130317604731","comparisonType":"Greater"}}}` | 130:Out → 73:Succeeded; 132:Out1 → 130:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wat_nid_06_data_drive"}}}` | 21:Out → 133:In; 133:Out → 23:Succeeded |
| `sts_wat_nid_06_openworld.questphase / h126 / 136` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\watson\\northside_industrial_district\\sts_wat_nid_06\\scenes\\sts_wat_nid_06_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 136:Out → 1:In; 91:Out → 136:In |
| `sts_wat_nid_06_openworld.questphase / h126 / 139` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 86:Out → 139:In; 139:False → 124:In; 139:True → 140:In1 |
| `sts_wat_nid_06_openworld.questphase / h126 / 142` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 142:False → 120:Start 0; 137:Out → 142:In; 142:True → 143:In1 |
| `sts_wat_nid_06_openworld.questphase / h573 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#sts_nid_06_tr_cleanup"}}` | 37:Out → 5:In; 5:Out → 38:In |
| `sts_wat_nid_06_openworld.questphase / h573 / 20` | `questLogicalAndNodeDefinition` `{"inputSocketCount":9}` | 20:Out1 → 1:In; 6:Out → 20:In5; 7:Out → 20:In6; 8:Out → 20:In4; 9:Out → 20:In3; 15:Out → 20:In7; 16:Out → 20:In8; 27:Out → 20:In1; 23:Out → 20:In2; 25:Out → 20:In9 |
| `sts_wat_nid_06_openworld.questphase / h573 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 12:Out → 28:In; 28:Out → 34:In |
| `sts_wat_nid_06_openworld.questphase / h573 / 37` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 37:Out → 5:In; 32:Out → 37:In |
| `sts_wat_nid_06_holocall_debrief.scene / scene / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 64:0:0 → 65:0:1; 69:0:0 → 64:0:1 |
| `sts_wat_nid_06_holocall_debrief.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3,"miliseconds":600}}}` | 62:666:0 → 249:0:1; 249:0:0 → 251:0:1; 257:0:0 → 249:0:1; 259:1:0 → 249:0:0; 259:1:0 → 249:1026:0 |
| `sts_wat_nid_06_holocall_debrief.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 249:0:0 → 251:0:1; 251:0:0 → 253:0:1; 259:1:0 → 251:0:0; 259:1:0 → 251:1026:0 |
| `sts_wat_nid_06_holocall_debrief.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3,"miliseconds":600}}}` | 251:0:0 → 253:0:1; 253:0:0 → 255:0:1; 259:1:0 → 253:0:0; 259:1:0 → 253:1026:0 |
| `sts_wat_nid_06_holocall_debrief.scene / scene / 255` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 253:0:0 → 255:0:1; 255:0:0 → 261:0:1; 255:0:1 → 257:0:0 |
| `sts_wat_nid_06_holocall_debrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 62:666:0 → 267:0:1; 267:0:0 → 259:0:0 |
| `sts_wat_nid_06_holocall_debrief.scene / scene / 283` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_rejected"}}}` | 62:666:0 → 283:0:1; 283:0:0 → 281:0:1 |
| `sts_wat_nid_06_holocall_prebrief.scene / scene / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_end_done"}}}` | 64:0:0 → 65:0:1; 69:0:0 → 64:0:1 |
| `sts_wat_nid_06_holocall_prebrief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_rejected"}}}` | 254:0:0 → 258:0:1; 258:0:0 → 256:0:1 |
| `sts_wat_nid_06_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_reggie_calls_v_start_done"}}}` | 62:666:0 → 267:0:1; 267:0:0 → 269:0:0 |
| `sts_wat_nid_06_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 62:666:0 → 273:0:1; 269:1:0 → 273:0:0; 273:0:0 → 279:0:1 |
| `sts_wat_nid_06_holocall_prebrief.scene / scene / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 279:0:1; 279:0:0 → 285:0:1; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_wat_nid_06_holocall_prebrief.scene / scene / 281` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 269:1:0 → 281:0:0; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_wat_northside_industrial_district.questphase / h12972 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"Exited","triggerAreaRef":"#wat_nid_tr_escape"}}` | 14:Out → 7:In; 7:Out → 15:Succeeded; 7:Out → 117:In |
| `sts_wat_northside_industrial_district.questphase / h12972 / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"XOR","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#wat_nid_tr_inside_maelstrom_leader_chat_003"},{"$type":"questTriggerCondition","triggerAreaRef":"#wat_nid_tr_inside_maelstrom_004_001"},{"$type":"questTriggerCondition","triggerAreaRef":"#wat_nid_tr_inside_maelstrom_003_001"},{"$type":"questTriggerCondition","triggerAreaRef":"#wat_nid_tr_inside_maelstrom_005"}]}}` | 4:Out → 60:In; 60:Out → 8:Succeeded; 81:Out → 60:In |
| `sts_wat_northside_industrial_district.questphase / h12972 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questScan_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#nid_06_dvc_objective"},"eventType":"Finished"}}}` | 69:Out → 70:In; 70:Out → 76:In1 |
| `sts_wat_northside_industrial_district.questphase / h12972 / 75` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#nid_06_dvc_objective"},"timeInterval":2.0,"angleTolerance":20.0}}}` | 69:Out → 75:In; 75:Out → 76:In2 |
| `sts_wat_northside_industrial_district.questphase / h12972 / 76` | `questLogicalXorNodeDefinition` `{}` | 76:Out1 → 67:Inactive; 70:Out → 76:In1; 75:Out → 76:In2 |
| `sts_wat_northside_industrial_district.questphase / h12972 / 80` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"nid_06_testdef","value":1,"comparisonType":"GreaterOrEqual"}}}` | 80:True → 4:Active; 86:Out → 80:In; 80:False → 81:Active |
| `sts_wat_northside_industrial_district.questphase / h12972 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"130317604731","comparisonType":"Greater"}}}` | 3:Out → 107:In; 107:Out → 9:Succeeded; 107:Out → 122:In |
| `sts_wat_northside_industrial_district.questphase / h12972 / 121` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 26:Out → 121:In; 121:Out → 137:In |
| `sts_wat_northside_industrial_district.questphase / h12972 / 130` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"130317604731","comparisonType":"Greater"}}}` | 130:Out → 73:Succeeded; 132:Out1 → 130:In |
| `sts_wat_northside_industrial_district.questphase / h12972 / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_wat_nid_06_data_drive"}}}` | 21:Out → 133:In; 133:Out → 23:Succeeded |
| `mq036_quest_bugfixes.questphase / h870 / 246` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/deliver_chip","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 246:False → 201:In1; 259:False → 246:In; 258:Out → 246:In; 246:True → 247:In |
| `mq036_quest_bugfixes.questphase / h870 / 253` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/get_to_droppoint","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 240:False → 253:In; 245:Out → 253:In; 253:True → 254:In; 253:False → 259:In |
| `mq036_quest_bugfixes.questphase / h870 / 259` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/deliver_files","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Active"}}}` | 259:False → 246:In; 253:False → 259:In; 257:Out → 259:In; 259:True → 260:In |
| `mq036_quest_bugfixes.questphase / h870 / 260` | `questConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questInventory_ConditionType","itemID":"130317604731","quantity":1,"comparisonType":"GreaterOrEqual"}}}` | 260:True → 258:In; 259:True → 260:In; 260:False → 261:In |
| `open_world_bugfixing.questphase / h116 / 47` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"nid_06_finished"}}}` | 0:Out → 47:In; 47:True → 91:Succeeded |
| `open_world_bugfixing.questphase / h2878 / 47` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"nid_06_finished"}}}` | 0:Out → 47:In; 47:True → 91:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `checkpoint` | sts_wat_nid_06_openworld.questphase / h12 / 20; sts_wat_nid_06_openworld.questphase / h573 / 29 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `community_lifecycle` | sts_wat_nid_06_openworld.questphase / h12 / 21; sts_wat_nid_06_openworld.questphase / h573 / 6; sts_wat_nid_06_openworld.questphase / h573 / 7 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h116 / 47; open_world_bugfixing.questphase / h2878 / 47; sts_wat_nid_06_holocall_debrief.scene / scene / 251; sts_wat_nid_06_holocall_debrief.scene / scene / 267; +10 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_wat_nid_06_openworld.questphase / h126 / 112; sts_wat_nid_06_openworld.questphase / h126 / 115; sts_wat_nid_06_openworld.questphase / h573 / 12; sts_wat_nid_06_openworld.questphase / h573 / 30 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq036_quest_bugfixes.questphase / h870 / 257; sts_wat_nid_06_openworld.questphase / h12 / 10; sts_wat_nid_06_openworld.questphase / h12 / 7; sts_wat_nid_06_openworld.questphase / h126 / 122; +4 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_wat_nid_06_openworld.questphase / h12 / 14; sts_wat_nid_06_openworld.questphase / h573 / 26; sts_wat_nid_06_openworld.questphase / h573 / 27 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `elapsed_time` | sts_wat_nid_06_openworld.questphase / h573 / 37 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `item_state` | mq036_quest_bugfixes.questphase / h870 / 260; sts_wat_nid_06_openworld.questphase / h126 / 107; sts_wat_nid_06_openworld.questphase / h126 / 130; sts_wat_northside_industrial_district.questphase / h12972 / 107; +1 locations in catalogue.json | item ID + entity + quantity/comparison → ownership predicate. Ownership alone does not prove reading, device interaction or reward delivery. |
| `journal_transition` | open_world_bugfixing.questphase / h116 / 91; open_world_bugfixing.questphase / h2878 / 91; sts_wat_nid_06_openworld.questphase / h12 / 4; sts_wat_nid_06_openworld.questphase / h126 / 117; +28 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | sts_wat_nid_06_openworld.questphase / h12 / 23; sts_wat_nid_06_openworld.questphase / h126 / 101; sts_wat_nid_06_openworld.questphase / h573 / 20 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_wat_nid_06_holocall_debrief.scene / scene / 261; sts_wat_nid_06_holocall_debrief.scene / scene / 279; sts_wat_nid_06_holocall_debrief.scene / scene / 281; sts_wat_nid_06_holocall_debrief.scene / scene / 63; +19 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_wat_nid_06_openworld.questphase / h126 / 76; sts_wat_northside_industrial_district.questphase / h12972 / 76 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_wat_nid_06_holocall_debrief.scene / scene / 249; sts_wat_nid_06_holocall_debrief.scene / scene / 253; sts_wat_nid_06_holocall_prebrief.scene / scene / 273; sts_wat_nid_06_holocall_prebrief.scene / scene / 281; +3 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | sts_wat_nid_06_openworld.questphase / h573 / 2 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scan_evidence` | sts_wat_nid_06_openworld.questphase / h126 / 70; sts_wat_northside_industrial_district.questphase / h12972 / 70 | clue reference + exact scan event + required-set policy → clue observed. Preserve Started versus Finished, ordering, bypass and reaction joins. |
| `scene_interface` | sts_wat_nid_06_openworld.questphase / h126 / 119; sts_wat_nid_06_openworld.questphase / h126 / 120 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_wat_nid_06_openworld.questphase / h12 / 31; sts_wat_nid_06_openworld.questphase / h126 / 113; sts_wat_nid_06_openworld.questphase / h126 / 114; sts_wat_nid_06_openworld.questphase / h126 / 60; +4 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_wat_nid_06_openworld.questphase / h126 / 97; sts_wat_nid_06_openworld.questphase / h126 / 98 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `world_variant` | sts_wat_nid_06_openworld.questphase / h12 / 13; sts_wat_nid_06_openworld.questphase / h573 / 16; sts_wat_nid_06_openworld.questphase / h573 / 23 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` | content candidate; journal anchor | `base-sts-wat-nid-06` |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` | content candidate; forward dependency | `base-sts-wat-nid-06` |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-wat-nid-06` |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_northside_industrial_district.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` | repair; journal anchor | `base-mq036` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq036](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq036.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-sts-wat-nid-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-wat-nid-06.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

162 repeated typed/socket path signatures in this selected graph context; 34 distinct direct resource identities; 3 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 69 -> 64 -> 65 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `fee3756653cd083fb28e` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` / h573 / 32 -> 37 -> 5 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 67 -> 69 -> 64 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 283 -> 281 -> 285 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 63 -> 66 -> 17 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 17 -> 67 -> 69 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `c8705a8da51824b73252` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` / h126 / 0 -> 86 -> 80 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_prebrief.scene` / scene / 68 -> 254 -> 258 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 1 -> 68 -> 279 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` / h126 / 7 -> 15 -> 21 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 267 -> 259 -> 249 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `d5cbf4acf851cb8612b3` | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_prebrief.scene` / scene / 285 -> 283 -> 260 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` / h0 / 4 | `h126` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` / h0 / 5 | `h573` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\community\westbrook\charter_hill\wbr_hil_com_test_03_02.gamedef` | content candidate | base\open_world\community\westbrook\charter_hill\wbr_hil_com_test.quest |
| `base\open_world\district_definitions\open_world_kabuki.gamedef` | content candidate | base\open_world\district_definitions\open_world_kabuki.quest |
| `base\open_world\open_world_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\police_system\police_system_test.gamedef` | content candidate | base\open_world\police_system\police_system_test.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
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
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02_test.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\sts_wat_nid_06_definition.gamedef` | content candidate | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\sts_wat_nid_06_quest.quest |
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
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_01\phases\sts_wat_nid_01_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_03\phases\sts_wat_nid_03.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_03\phases\sts_wat_nid_03_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_03\phases\sts_wat_nid_03_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_04\phases\sts_wat_nid_04_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\phase\sts_wat_nid_05_streetstory.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\lipsync\en\sts_wat_nid_06_holocall_debrief\regina_reggie_jones.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\lipsync\en\sts_wat_nid_06_holocall_debrief\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\lipsync\en\sts_wat_nid_06_holocall_prebrief\regina_reggie_jones.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\lipsync\en\sts_wat_nid_06_holocall_prebrief\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\phases\sts_wat_nid_07.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\phases\sts_wat_nid_07_aaron.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\phases\sts_wat_nid_07_aaron_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\phases\sts_wat_nid_07_aaron_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\phases\sts_wat_nid_07_warehouse.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\phases\sts_wat_nid_07_warehouse_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\phases\sts_wat_nid_07_warehouse_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_12\phases\sts_wat_nid_12.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_12\phases\sts_wat_nid_12_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_12\phases\sts_wat_nid_12_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 212; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 125; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 186; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 379; 194 total source locations in compressed evidence |
| `holo_reggie_calls_v_end_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\ma_bls_ina_se1_07_phase.questphase / h0 / 211; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 121; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 375; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase / h0 / 305; 74 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejectable` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 249; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 266; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 395; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 412; 102 total source locations in compressed evidence |
| `holo_reggie_calls_v_rejected` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 251; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 403; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 256; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 256; 63 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_activate` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 124; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 264; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\ma_bls_ina_se1_08_phase.questphase / h0 / 185; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 378; 253 total source locations in compressed evidence |
| `holo_reggie_calls_v_start_done` | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene / scene / 119; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene / scene / 373; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene / scene / 58; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene / scene / 55; 69 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `nid_06_finished` | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_northside_industrial_district.questphase / h12972 / 91; 1 total source locations in compressed evidence |
| `nid_06_testdef` | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\sts_wat_nid_06_quest.quest / h0 / 13; 1 total source locations in compressed evidence |
| `wat_achievement` | base\open_world\minor_activities\watson\northside\ma_wat_nid_01\ma_wat_nid_01_phase.questphase / h0 / 81; base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase / h0 / 89; base\open_world\minor_activities\watson\northside\ma_wat_nid_04\ma_wat_nid_04_phase.questphase / h0 / 50; base\open_world\minor_activities\watson\northside\ma_wat_nid_06\ma_wat_nid_06_phase.questphase / h0 / 66; 67 total source locations in compressed evidence |

NodeRef uses: 87; TweakDB binding uses: 13. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` | 1 / 1 | scnDialogLineEvent: 1 |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_prebrief.scene` | 1 / 2 | scnDialogLineEvent: 2 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
