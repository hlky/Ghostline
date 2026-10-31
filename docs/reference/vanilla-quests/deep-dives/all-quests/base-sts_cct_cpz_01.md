# Gig: Serial Suicide

Journal: `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01` · `StreetStory` · hash `2457764693`.

Journal premise: Gig type: Thievery\nObjective: Steal CCTV footage\nLocation: Memorial Park Station\nDetails:\n\nSomething's rotten in the City of Dreams. A series of suicides, a rash of self-destruction. The contagion mostly targets politicians, corpos, journalists and police officers.\n\nThe latest victim was Zoli Barnes, a journalist who "fell" onto the tracks at Memorial Park station. Her death was officially ruled a suicide, but Barnes' parents say that she went to meet one her informants at the station and that she never would've taken her own life (I know, I know, that's what all parents say). Seems like the jury's still out – nobody really knows what happened because every last shred of CCTV footage was wiped clean. Her parents tracked down the witnesses, but they didn't want to talk and what's more – Militech took a keen interest in the whole thing.\n\nIt's our turn to make heads or tails of this. Head to the station, breach the servers and download any CCTV-related files. I'll have my code monkeys try to recover the deleted footage.\nP.S. Oh and by the way, at the time Zoli was working on a piece about Brad Noorwood – a Militech fanboy in the Night City Council.\n\nAnyway, looks that piece is never getting published.\nP.P.S. Transferring you Militech authorization that'll get you into the station.

**Coverage: journal-linked.** 28 exact journal-linked nodes in 4 resources; 7 resources in the inspected dependency context.

Resource roles in that context: 5 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Steal the CCTV footage. (Primary) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/data` |
| Leave the station. (Primary) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/escape` |
| Sneak into the station. (Primary) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/security_building` |
| Reach the main server room in the station. (Primary) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/server_room` |
| Acquire the data. (Primary) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/steal_recording` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_cct_corpo_plaza.questphase / h228 / 13` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/escape` | 54:Out → 13:Active; 13:Out → 17:In |
| `sts_cct_corpo_plaza.questphase / h228 / 14` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/escape` | 17:Out → 14:Succeeded; 14:Out → 19:Succeeded |
| `sts_cct_corpo_plaza.questphase / h228 / 19` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01` | 14:Out → 19:Succeeded; 19:Out → 29:In |
| `sts_cct_corpo_plaza.questphase / h228 / 33` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/security_building` | 33:Out → 25:In1; 26:True → 33:Active |
| `sts_cct_corpo_plaza.questphase / h228 / 34` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/security_building` | 34:Out → 25:In2; 26:False → 34:Active |
| `sts_cct_corpo_plaza.questphase / h228 / 35` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/security_building` | 36:Out → 35:Succeeded; 35:Out → 48:In1 |
| `sts_cct_corpo_plaza.questphase / h228 / 38` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/brief` | 25:Out1 → 38:Active |
| `sts_cct_corpo_plaza.questphase / h228 / 59` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/steal_recording` | 48:Out1 → 59:Succeeded |
| `sts_cct_corpo_plaza.questphase / h360 / 2` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/data` | 2:Out → 1:In; 15:Out → 2:Succeeded |
| `sts_cct_corpo_plaza.questphase / h360 / 4` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/server_room` | 3:Out → 4:Succeeded; 4:Out → 5:Active |
| `sts_cct_corpo_plaza.questphase / h360 / 5` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/data` | 4:Out → 5:Active; 5:Out → 13:In |
| `sts_cct_corpo_plaza.questphase / h360 / 7` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/server_room` | 0:Out → 7:Active; 7:Out → 3:In |
| `sts_cct_cpz_01_bugfixing.questphase / h0 / 5` (Condition) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01` | 4:True → 5:In; 5:True → 6:Succeeded |
| `sts_cct_cpz_01_bugfixing.questphase / h0 / 6` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01` | 5:True → 6:Succeeded |
| `sts_cct_cpz_01_openworld.questphase / h108 / 13` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/escape` | 54:Out → 13:Active; 13:Out → 17:In |
| `sts_cct_cpz_01_openworld.questphase / h108 / 14` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/escape` | 17:Out → 14:Succeeded; 14:Out → 19:Succeeded |
| `sts_cct_cpz_01_openworld.questphase / h108 / 19` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01` | 14:Out → 19:Succeeded; 19:Out → 29:In |
| `sts_cct_cpz_01_openworld.questphase / h108 / 33` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/security_building` | 33:Out → 25:In1; 26:True → 33:Active |
| `sts_cct_cpz_01_openworld.questphase / h108 / 34` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/security_building` | 34:Out → 25:In2; 26:False → 34:Active |
| `sts_cct_cpz_01_openworld.questphase / h108 / 35` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/security_building` | 36:Out → 35:Succeeded; 35:Out → 48:In1 |
| `sts_cct_cpz_01_openworld.questphase / h108 / 38` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/brief` | 25:Out1 → 38:Active |
| `sts_cct_cpz_01_openworld.questphase / h108 / 59` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/steal_recording` | 48:Out1 → 59:Succeeded |
| `sts_cct_cpz_01_openworld.questphase / h240 / 2` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/data` | 2:Out → 1:In; 15:Out → 2:Succeeded |
| `sts_cct_cpz_01_openworld.questphase / h240 / 4` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/server_room` | 3:Out → 4:Succeeded; 4:Out → 5:Active |
| `sts_cct_cpz_01_openworld.questphase / h240 / 5` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/data` | 4:Out → 5:Active; 5:Out → 13:In |
| `sts_cct_cpz_01_openworld.questphase / h240 / 7` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01/sts_cct_cpz_01/server_room` | 0:Out → 7:Active; 7:Out → 3:In |
| `open_world_bugfixing.questphase / h1425 / 3` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01` | 2:True → 3:Succeeded |
| `open_world_bugfixing.questphase / h2561 / 3` (Journal) | `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01` | 2:True → 3:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_cct_cpz_01_openworld.questphase / h108 / 76` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_prebrief.scene`; `#sts_sm_cct_cpz_01_holocall_prebrief` | 76:End 0 → 75:Active; 76:rejected_out → 75:Active; 83:False → 76:Start 0; 76:Holocall INT → 79:In; 76:Holocall RET → 78:In |
| `sts_cct_cpz_01_openworld.questphase / h484 / 6` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_prisoner_chat.scene`; `#sts_sm_cct_cpz_01_prisoner_chat` | 7:Out → 6:cpz_01_prisoner_chat_start |
| `sts_cct_cpz_01_openworld.questphase / h509 / 59` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene`; `#sts_sm_cct_cpz_01_holocall_debrief` | 59:End 0 → 27:In; 81:False → 59:Start 0; 59:rejected_out → 82:Active; 59:Holocall INT → 68:In; 59:Holocall RET → 67:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\city_center\sts_city_center.questphase` / h0 / 2 | `sts_cct_corpo_plaza.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\open_world\bugfixing\sts\sts_corpo_plaza_bugfixing.questphase` / h0 / 4 | `sts_cct_cpz_01_bugfixing.questphase` | 6: DeletionMarker; 6:Out → 4:In1 |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase` / h865 / 19 | `sts_cct_cpz_01_openworld.questphase` | 0: Input; 0:Out → 19:In1; 19:Out1 → 1:In |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\sts_cct_cpz_01.questphase` / h0 / 19 | `sts_cct_cpz_01_openworld.questphase` | 0: Input; 0:Out → 19:In1; 19:Out1 → 1:In |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase` / h629 / 59 | `sts_cct_cpz_01_holocall_debrief.scene` | 81: Condition; 59:End 0 → 27:In; 81:False → 59:Start 0; 59:rejected_out → 82:Active; 59:Holocall INT → 68:In; 59:Holocall RET → 67:In |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` / h509 / 59 | `sts_cct_cpz_01_holocall_debrief.scene` | 81: Condition; 59:End 0 → 27:In; 81:False → 59:Start 0; 59:rejected_out → 82:Active; 59:Holocall INT → 68:In; 59:Holocall RET → 67:In |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase` / h228 / 76 | `sts_cct_cpz_01_holocall_prebrief.scene` | 83: Condition; 76:End 0 → 75:Active; 76:rejected_out → 75:Active; 83:False → 76:Start 0; 76:Holocall INT → 79:In; 76:Holocall RET → 78:In |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` / h108 / 76 | `sts_cct_cpz_01_holocall_prebrief.scene` | 83: Condition; 76:End 0 → 75:Active; 76:rejected_out → 75:Active; 83:False → 76:Start 0; 76:Holocall INT → 79:In; 76:Holocall RET → 78:In |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase` / h604 / 6 | `sts_cct_cpz_01_prisoner_chat.scene` | 7: PauseCondition: #cpz_01_tr_prisoner; 7:Out → 6:cpz_01_prisoner_chat_start |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` / h484 / 6 | `sts_cct_cpz_01_prisoner_chat.scene` | 7: PauseCondition: #cpz_01_tr_prisoner; 7:Out → 6:cpz_01_prisoner_chat_start |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 3 | `sts_city_center.questphase` | 0: Input; 0:Out → 3:In1 |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h11 / 46 | `sts_corpo_plaza_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 46:In1 |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase` / h0 / 6 | `sts_cct_cpz_01.questphase` | 13: Journal; 15: Journal; 13:Out → 6:In1; 15:Out → 6:In1 |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\sts_cct_cpz_01.quest` / h0 / 2 | `sts_cct_cpz_01.questphase` | 4: PauseCondition: {"seconds": 4}; 2:Out1 → 1:In; 4:Out → 2:In1 |
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
| `sts_cct_cpz_01_holocall_debrief.scene` | Start 0 → End 0, rejected_out | fixer; 23 nodes / 30 edges |
| `sts_cct_cpz_01_holocall_prebrief.scene` | Start 0 → End 0, rejected_out | fixer; Player; 23 nodes / 26 edges |
| `sts_cct_cpz_01_prisoner_chat.scene` | cpz_01_prisoner_chat_start, CineStart02 → Scene interrupted | prisoner_001; guard_004; Player; 60 nodes / 69 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `sts_cct_cpz_01_prisoner_chat.scene / n49 / 0` | How many more are there? (``) | No option-level predicate stored | 0:0 → 54:0:0 |
| `sts_cct_cpz_01_prisoner_chat.scene / n49 / 1` | Why was he beating on you? (``) | No option-level predicate stored | 0:1 → 51:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-688401` | sts_cct_cpz_01_bugfixing.questphase / h0 / 3 | sts_cct_cpz_01_bugfixing.questphase / h0 / 2 |
| `cct_achievement` | sts_cct_cpz_01_openworld.questphase / h509 / 57 | sts_cct_cpz_01_openworld.questphase / h509 / 73 |
| `cpz_01_finished` | sts_cct_corpo_plaza.questphase / h228 / 29; sts_cct_cpz_01_openworld.questphase / h108 / 29 | open_world_bugfixing.questphase / h1425 / 2; open_world_bugfixing.questphase / h2561 / 2 |
| `cpz_01_journal_test` | Producer outside selected context | sts_cct_corpo_plaza.questphase / h228 / 26; sts_cct_cpz_01_openworld.questphase / h108 / 26 |
| `cpz_01_start` | sts_cct_cpz_01_openworld.questphase / h108 / 28 | No reader in selected context |
| `holo_active_call_interrupted` | Producer outside selected context | sts_cct_cpz_01_holocall_prebrief.scene / scene / 288 |
| `holo_dino_calls_v_end_activate` | sts_cct_cpz_01_holocall_debrief.scene / scene / 69; sts_cct_cpz_01_holocall_prebrief.scene / scene / 65; sts_cct_cpz_01_openworld.questphase / h108 / 79; sts_cct_cpz_01_openworld.questphase / h509 / 68 | sts_cct_cpz_01_holocall_prebrief.scene / scene / 60 |
| `holo_dino_calls_v_end_done` | sts_cct_cpz_01_holocall_debrief.scene / scene / 65; sts_cct_cpz_01_holocall_prebrief.scene / scene / 61 | sts_cct_cpz_01_holocall_debrief.scene / scene / 64 |
| `holo_dino_calls_v_rejectable` | sts_cct_cpz_01_holocall_debrief.scene / scene / 280; sts_cct_cpz_01_holocall_prebrief.scene / scene / 262; sts_cct_cpz_01_holocall_prebrief.scene / scene / 304 | No reader in selected context |
| `holo_dino_calls_v_rejected` | sts_cct_cpz_01_holocall_debrief.scene / scene / 282; sts_cct_cpz_01_holocall_prebrief.scene / scene / 264 | sts_cct_cpz_01_holocall_debrief.scene / scene / 284; sts_cct_cpz_01_holocall_prebrief.scene / scene / 266 |
| `holo_dino_calls_v_start_activate` | sts_cct_cpz_01_holocall_debrief.scene / scene / 257; sts_cct_cpz_01_holocall_debrief.scene / scene / 68; sts_cct_cpz_01_holocall_prebrief.scene / scene / 302; sts_cct_cpz_01_holocall_prebrief.scene / scene / 64; sts_cct_cpz_01_openworld.questphase / h108 / 78; sts_cct_cpz_01_openworld.questphase / h509 / 67 | sts_cct_cpz_01_holocall_debrief.scene / scene / 253 |
| `holo_dino_calls_v_start_done` | sts_cct_cpz_01_holocall_debrief.scene / scene / 63; sts_cct_cpz_01_holocall_prebrief.scene / scene / 59 | sts_cct_cpz_01_holocall_debrief.scene / scene / 249; sts_cct_cpz_01_holocall_prebrief.scene / scene / 278 |
| `holo_setup_active` | Producer outside selected context | sts_cct_cpz_01_holocall_debrief.scene / scene / 253; sts_cct_cpz_01_holocall_prebrief.scene / scene / 288 |
| `holo_setup_started` | Producer outside selected context | sts_cct_cpz_01_holocall_debrief.scene / scene / 253; sts_cct_cpz_01_holocall_prebrief.scene / scene / 288 |

## Exact gates, joins and cancellation

<details><summary>56 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_cct_corpo_plaza.questphase / h228 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#cpz_01_tr_end"}}` | 13:Out → 17:In; 17:Out → 14:Succeeded |
| `sts_cct_corpo_plaza.questphase / h228 / 25` | `questLogicalXorNodeDefinition` `{}` | 33:Out → 25:In1; 34:Out → 25:In2; 25:Out1 → 36:In; 25:Out1 → 38:Active |
| `sts_cct_corpo_plaza.questphase / h228 / 26` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"cpz_01_journal_test"}}}` | 28:Out → 26:In; 26:True → 33:Active; 26:False → 34:Active |
| `sts_cct_corpo_plaza.questphase / h228 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#cpz_01_tr_end"}}` | 25:Out1 → 36:In; 36:Out → 35:Succeeded |
| `sts_cct_corpo_plaza.questphase / h360 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#cpz_01_tr_server_room"}}` | 7:Out → 3:In; 3:Out → 4:Succeeded; 3:Out → 12:In |
| `sts_cct_corpo_plaza.questphase / h360 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#cpz_01_dvc_computer_002","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 5:Out → 13:In; 13:Out → 14:In |
| `sts_cct_cpz_01_bugfixing.questphase / h0 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-688401"}}}` | 0:Out → 2:In; 2:False → 3:In |
| `sts_cct_cpz_01_bugfixing.questphase / h0 / 4` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"contacts/dino_dinovic/sts_cct_cpz_01/sts_cct_cpz_01_debrief","fileEntryIndex":1,"className":"gameJournalPhoneMessage"},"state":"Active"}}}` | 3:Out → 4:In; 4:True → 5:In |
| `sts_cct_cpz_01_bugfixing.questphase / h0 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01","fileEntryIndex":4,"className":"gameJournalQuest"},"state":"Active"}}}` | 4:True → 5:In; 5:True → 6:Succeeded |
| `sts_cct_cpz_01_openworld.questphase / h12 / 44` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#cpz_01_tr_initiation"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 44:Out → 20:In; 45:Out → 44:In |
| `sts_cct_cpz_01_openworld.questphase / h108 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#cpz_01_tr_end"}}` | 13:Out → 17:In; 17:Out → 14:Succeeded |
| `sts_cct_cpz_01_openworld.questphase / h108 / 25` | `questLogicalXorNodeDefinition` `{}` | 33:Out → 25:In1; 34:Out → 25:In2; 25:Out1 → 36:In; 25:Out1 → 38:Active |
| `sts_cct_cpz_01_openworld.questphase / h108 / 26` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"cpz_01_journal_test"}}}` | 28:Out → 26:In; 26:True → 33:Active; 26:False → 34:Active |
| `sts_cct_cpz_01_openworld.questphase / h108 / 36` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#cpz_01_tr_end"}}` | 25:Out1 → 36:In; 36:Out → 35:Succeeded |
| `sts_cct_cpz_01_openworld.questphase / h108 / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#cpz_01_tr_end"}}` | 60:Out → 62:In; 62:Out → 63:In |
| `sts_cct_cpz_01_openworld.questphase / h108 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#cpz_01_combat_com","names":["guard_001","guard_002","guard_003","guard_005"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 70:In; 70:Out → 72:In1 |
| `sts_cct_cpz_01_openworld.questphase / h108 / 71` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#cpz_01_combat_com","names":["guard_004"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 0:Out → 71:In; 71:Out → 72:In2 |
| `sts_cct_cpz_01_openworld.questphase / h108 / 72` | `questLogicalAndNodeDefinition` `{}` | 72:Out1 → 66:In; 72:Out1 → 67:In; 72:Out1 → 68:In; 72:Out1 → 69:In; 70:Out → 72:In1; 71:Out → 72:In2 |
| `sts_cct_cpz_01_openworld.questphase / h108 / 77` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 0:Out → 77:In; 77:False → 75:Active; 77:True → 83:In |
| `sts_cct_cpz_01_openworld.questphase / h108 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#cpz_01_tr_end"}}` | 61:Out → 60:In; 63:Out → 61:In; 75:Out → 61:In |
| `sts_cct_cpz_01_openworld.questphase / h108 / 82` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\city_center\\corpo_plaza\\sts_cct_cpz_01\\scenes\\sts_cct_cpz_01_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}}` | 82:Out → 1:In; 29:Out → 82:In |
| `sts_cct_cpz_01_openworld.questphase / h108 / 83` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 83:True → 75:Active; 83:False → 76:Start 0; 77:True → 83:In |
| `sts_cct_cpz_01_openworld.questphase / h240 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#cpz_01_tr_server_room"}}` | 7:Out → 3:In; 3:Out → 4:Succeeded; 3:Out → 12:In |
| `sts_cct_cpz_01_openworld.questphase / h240 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#cpz_01_dvc_computer_002","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 5:Out → 13:In; 13:Out → 14:In |
| `sts_cct_cpz_01_openworld.questphase / h484 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#cpz_01_tr_prisoner"}}` | 0:Out → 7:In; 7:Out → 6:cpz_01_prisoner_chat_start |
| `sts_cct_cpz_01_openworld.questphase / h509 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 27:Out → 25:In; 82:Out → 27:In; 59:End 0 → 27:In |
| `sts_cct_cpz_01_openworld.questphase / h509 / 46` | `questLogicalAndNodeDefinition` `{"inputSocketCount":9}` | 46:Out1 → 1:In; 41:Out → 46:In2; 42:Out → 46:In3; 43:Out → 46:In1; 44:Out → 46:In5; 45:Out → 46:In4; 51:Out → 46:In6; 53:Out → 46:In7; 52:Out → 46:In8; 58:Out → 46:In9 |
| `sts_cct_cpz_01_openworld.questphase / h509 / 70` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#cpz_01_tr_cleanup"}}` | 74:Out → 70:In; 70:Out → 75:In |
| `sts_cct_cpz_01_openworld.questphase / h509 / 74` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 69:Out → 74:In; 74:Out → 70:In |
| `sts_cct_cpz_01_openworld.questphase / h509 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 0:Out → 77:In; 77:Out → 80:In |
| `sts_cct_cpz_01_openworld.questphase / h509 / 81` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 81:False → 59:Start 0; 80:Out → 81:In; 81:True → 82:Active |
| `sts_cct_cpz_01_holocall_debrief.scene / scene / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_end_done"}}}` | 64:0:0 → 65:0:1; 69:0:0 → 64:0:1 |
| `sts_cct_cpz_01_holocall_debrief.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_start_done"}}}` | 62:666:0 → 249:0:1; 249:0:0 → 269:0:0 |
| `sts_cct_cpz_01_holocall_debrief.scene / scene / 252` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":400}}}` | 62:666:0 → 252:0:1; 252:0:0 → 253:0:1; 260:0:0 → 252:0:1; 269:1:0 → 252:0:0; 269:1:0 → 252:1026:0 |
| `sts_cct_cpz_01_holocall_debrief.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 252:0:0 → 253:0:1; 253:0:0 → 254:0:1; 269:1:0 → 253:0:0; 269:1:0 → 253:1026:0 |
| `sts_cct_cpz_01_holocall_debrief.scene / scene / 254` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":400}}}` | 253:0:0 → 254:0:1; 254:0:0 → 256:0:1; 269:1:0 → 254:0:0; 269:1:0 → 254:1026:0 |
| `sts_cct_cpz_01_holocall_debrief.scene / scene / 256` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 254:0:0 → 256:0:1; 256:0:0 → 257:0:1; 256:0:1 → 260:0:0 |
| `sts_cct_cpz_01_holocall_debrief.scene / scene / 284` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_rejected"}}}` | 68:0:0 → 284:0:1; 284:0:0 → 282:0:1 |
| `sts_cct_cpz_01_holocall_prebrief.scene / scene / 60` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_end_activate"}}}` | 60:0:0 → 61:0:1; 65:0:0 → 60:0:1 |
| `sts_cct_cpz_01_holocall_prebrief.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 1:0:0 → 251:0:1; 251:0:0 → 262:0:1 |
| `sts_cct_cpz_01_holocall_prebrief.scene / scene / 266` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_rejected"}}}` | 64:0:0 → 266:0:1; 266:0:0 → 264:0:1 |
| `sts_cct_cpz_01_holocall_prebrief.scene / scene / 276` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 58:666:0 → 276:0:1; 276:0:0 → 288:0:1; 281:1:0 → 276:0:0 |
| `sts_cct_cpz_01_holocall_prebrief.scene / scene / 278` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_dino_calls_v_start_done"}}}` | 58:666:0 → 278:0:1; 278:0:0 → 281:0:0 |
| `sts_cct_cpz_01_holocall_prebrief.scene / scene / 288` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 276:0:0 → 288:0:1; 288:0:0 → 304:0:1; 288:0:1 → 290:0:1; 290:0:0 → 288:0:1 |
| `sts_cct_cpz_01_holocall_prebrief.scene / scene / 290` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 281:1:0 → 290:0:0; 288:0:1 → 290:0:1; 290:0:0 → 288:0:1 |
| `sts_cct_cpz_01_prisoner_chat.scene / scene / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#cpz_01_combat_com","names":["guard_004"]},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 12:0:0 → 3:1:0; 12:0:0 → 117:0:1; 12:0:0 → 144:0:1; 153:0:0 → 12:0:1 |
| `sts_cct_cpz_01_prisoner_chat.scene / scene / 62` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSceneCondition","type":{"$type":"questSceneInterrupt_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\city_center\\corpo_plaza\\sts_cct_cpz_01\\scenes\\sts_cct_cpz_01_prisoner_chat.scene","Flags":"Soft"},"interruptConditions":[{"$type":"scnCheckSpeakerOrAddressDistractedInterruptCondition"}]}}}` | 62:0:0 → 3:1:0; 153:0:0 → 62:0:1 |
| `sts_cct_cpz_01_prisoner_chat.scene / scene / 144` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","inverted":true}},{"$type":"questTriggerCondition","triggerAreaRef":"#cpz_01_tr_prisoner_room"}]}}` | 12:0:0 → 144:0:1; 144:0:0 → 11:0:0 |
| `sts_cct_cpz_01_prisoner_chat.scene / scene / 212` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 189:3:0 → 212:0:1; 212:0:0 → 181:0:0 |
| `sts_cct_cpz_01_prisoner_chat.scene / scene / 215` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#cpz_01_combat_com"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"GreaterOrEqual"}}}}` | 54:0:0 → 215:0:1; 215:0:0 → 189:0:0; 215:0:1 → 220:0:0 |
| `sts_cct_cpz_01_prisoner_chat.scene / scene / 217` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#cpz_01_combat_com"},"comparisonParams":{"$type":"questComparisonParam"}}}}` | 217:0:0 → 229:0:0; 220:0:0 → 217:0:1 |
| `sts_cct_cpz_01_prisoner_chat.scene / scene / 246` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 3:0:0 → 246:0:1; 246:0:0 → 248:0:0 |
| `sts_cct_cpz_01_prisoner_chat.scene / scene / 262` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#cpz_01_combat_com","names":["guard_004"]},"isPlayer":false}}}` | 153:0:0 → 262:0:1; 262:0:0 → 264:0:1 |
| `sts_cct_cpz_01_prisoner_chat.scene / scene / 277` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#cpz_01_dvc_security_system","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 1:0:0 → 277:0:1; 277:0:0 → 64:0:0 |
| `open_world_bugfixing.questphase / h1425 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"cpz_01_finished"}}}` | 0:Out → 2:In; 2:True → 3:Succeeded |
| `open_world_bugfixing.questphase / h2561 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"cpz_01_finished"}}}` | 0:Out → 2:In; 2:True → 3:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_route` | sts_cct_cpz_01_prisoner_chat.scene / scene / 187; sts_cct_cpz_01_prisoner_chat.scene / scene / 237; sts_cct_cpz_01_prisoner_chat.scene / scene / 257 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | sts_cct_cpz_01_openworld.questphase / h12 / 35; sts_cct_cpz_01_openworld.questphase / h509 / 60 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | sts_cct_cpz_01_prisoner_chat.scene / scene / 49 | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `combat_control` | sts_cct_cpz_01_prisoner_chat.scene / scene / 264; sts_cct_cpz_01_prisoner_chat.scene / scene / 266; sts_cct_cpz_01_prisoner_chat.scene / scene / 267 | actor + target + combat operation → command result. Separate hostility, threat injection, encounter completion and target cleanup. |
| `community_lifecycle` | sts_cct_cpz_01_openworld.questphase / h12 / 21; sts_cct_cpz_01_openworld.questphase / h12 / 38; sts_cct_cpz_01_openworld.questphase / h12 / 40; sts_cct_cpz_01_openworld.questphase / h509 / 51; +3 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1425 / 2; open_world_bugfixing.questphase / h2561 / 2; sts_cct_corpo_plaza.questphase / h228 / 26; sts_cct_cpz_01_bugfixing.questphase / h0 / 2; +9 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_cct_cpz_01_openworld.questphase / h0 / 7; sts_cct_cpz_01_openworld.questphase / h108 / 60; sts_cct_cpz_01_openworld.questphase / h108 / 63; sts_cct_cpz_01_openworld.questphase / h509 / 56 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sts_cct_corpo_plaza.questphase / h360 / 12; sts_cct_corpo_plaza.questphase / h360 / 18; sts_cct_corpo_plaza.questphase / h360 / 20; sts_cct_cpz_01_openworld.questphase / h108 / 65; +14 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_cct_corpo_plaza.questphase / h360 / 15; sts_cct_cpz_01_openworld.questphase / h12 / 27; sts_cct_cpz_01_openworld.questphase / h240 / 15; sts_cct_cpz_01_openworld.questphase / h509 / 43 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_cct_corpo_plaza.questphase / h360 / 13; sts_cct_cpz_01_openworld.questphase / h240 / 13; sts_cct_cpz_01_prisoner_chat.scene / scene / 277 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_cct_cpz_01_openworld.questphase / h509 / 74 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | open_world_bugfixing.questphase / h1425 / 3; open_world_bugfixing.questphase / h2561 / 3; sts_cct_corpo_plaza.questphase / h228 / 13; sts_cct_corpo_plaza.questphase / h228 / 14; +29 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | sts_cct_cpz_01_openworld.questphase / h108 / 72; sts_cct_cpz_01_openworld.questphase / h509 / 46 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_cct_corpo_plaza.questphase / h228 / 29; sts_cct_cpz_01_bugfixing.questphase / h0 / 3; sts_cct_cpz_01_holocall_debrief.scene / scene / 257; sts_cct_cpz_01_holocall_debrief.scene / scene / 280; +20 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_cct_corpo_plaza.questphase / h228 / 25; sts_cct_cpz_01_openworld.questphase / h108 / 25 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_cct_cpz_01_holocall_debrief.scene / scene / 252; sts_cct_cpz_01_holocall_debrief.scene / scene / 254; sts_cct_cpz_01_holocall_prebrief.scene / scene / 251; sts_cct_cpz_01_holocall_prebrief.scene / scene / 276; +5 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | sts_cct_cpz_01_openworld.questphase / h509 / 25 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sts_cct_cpz_01_openworld.questphase / h108 / 76; sts_cct_cpz_01_openworld.questphase / h484 / 6; sts_cct_cpz_01_openworld.questphase / h509 / 59 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_cct_corpo_plaza.questphase / h228 / 17; sts_cct_corpo_plaza.questphase / h228 / 36; sts_cct_corpo_plaza.questphase / h360 / 3; sts_cct_cpz_01_openworld.questphase / h108 / 17; +8 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_cct_cpz_01_openworld.questphase / h108 / 70; sts_cct_cpz_01_openworld.questphase / h108 / 71; sts_cct_cpz_01_prisoner_chat.scene / scene / 12; sts_cct_cpz_01_prisoner_chat.scene / scene / 215; +1 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | sts_cct_cpz_01_prisoner_chat.scene / scene / 121; sts_cct_cpz_01_prisoner_chat.scene / scene / 124; sts_cct_cpz_01_prisoner_chat.scene / scene / 130; sts_cct_cpz_01_prisoner_chat.scene / scene / 142; +18 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_bugfixing.questphase` | repair; journal anchor | `base-sts-cct-cpz-01` |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` | content candidate; journal anchor | `base-sts-cct-cpz-01` |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene` | content candidate; forward dependency | `base-sts-cct-cpz-01` |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-cct-cpz-01` |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_prisoner_chat.scene` | content candidate; forward dependency | `base-sts-cct-cpz-01` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-cct-cpz-01](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-cct-cpz-01.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

205 repeated typed/socket path signatures in this selected graph context; 37 distinct direct resource identities; 6 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `20a77143a898bc753a26` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` / h12 / 21 -> 40 -> 38 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene` / scene / 68 -> 284 -> 282 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `fee3756653cd083fb28e` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` / h509 / 69 -> 74 -> 70 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene` / scene / 67 -> 69 -> 64 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene` / scene / 284 -> 282 -> 286 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene` / scene / 63 -> 66 -> 18 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene` / scene / 18 -> 67 -> 69 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `c8705a8da51824b73252` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` / h108 / 0 -> 28 -> 26 | questInputNodeDefinition -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; Out -> In; Out -> In |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene` / scene / 280 -> 68 -> 284 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene` / scene / 1 -> 280 -> 68 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `eaf5aab427d50e5598b6` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_bugfixing.questphase` / h0 / 0 -> 2 -> 3 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase` / h360 / 3 -> 4 -> 5 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase` / h228 / 48 | `h360` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` / h0 / 3 | `h108` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` / h108 / 48 | `h240` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` / h0 / 4 | `h484` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` / h0 / 5 | `h509` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\sts_cct_cpz_01.gamedef` | content candidate | base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\sts_cct_cpz_01.quest |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\sts_cct_cpz_01_test.gamedef` | content candidate | base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\sts_cct_cpz_01.quest |
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
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__kneel__2h_elbow_on_knees_rh_cigarette__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\open_world\dirtboy_work__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\gameplay\man_average\gang\unarmed\ma_gang_unarmed_locomotion_stealth.anims` | asset binding .anims | content/basegame_1_engine.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_ground_lean0__2h_around_legs__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_up__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__rh_up__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\synced\lore\ma_lore.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\phases\sts_cct_cpz_01_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\lipsync\en\sts_cct_cpz_01_holocall_debrief\dino_dyno_dinovic.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\lipsync\en\sts_cct_cpz_01_holocall_prebrief\dino_dyno_dinovic.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\lipsync\en\sts_cct_cpz_01_holocall_prebrief\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\lipsync\en\sts_cct_cpz_01_prisoner_chat\civ_low_m_05_enus_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\lipsync\en\sts_cct_cpz_01_prisoner_chat\sec_mid_m_01_enus_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\lipsync\en\sts_cct_cpz_01_prisoner_chat\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_prisoner_chat.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\sts_cct_cpz_01.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\archetype\dirt\common\ground\dirt__kneel_ground_cigarette__slav_squat__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__sit_ground_lean_front__scared__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__afraid__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__afraid__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__stand_around__06.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\street\ground\generic__stand_ground__demonstrate_negative__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\synced\encounter\synced__ganger__ganger_kick_lying_victim__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_2_gamedata.archive; index evidence only |
| `base\workspots\synced\lore\lore_ganger_street_violence_02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\synced\lore\lore_victim_robbery_02_lying.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\synced\lore\lore_victim_street_violence_02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `cct_achievement` | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase / h0 / 22; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase / h0 / 30; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_09\ma_cct_dtn_09_phase.questphase / h0 / 24; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase / h0 / 44; 16 total source locations in compressed evidence |
| `cpz_01_journal_test` | base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\sts_cct_cpz_01.quest / h0 / 3; 1 total source locations in compressed evidence |
| `cpz_01_start` | base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase / h228 / 28; 1 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_dino_calls_v_end_activate` | base\open_world\fixers\dyno\phases\dyno.questphase / h0 / 44; base\open_world\fixers\dyno\scenes\dyno_default.scene / scene / 220; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase / h228 / 79; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase / h629 / 68; 42 total source locations in compressed evidence |
| `holo_dino_calls_v_end_done` | base\open_world\fixers\dyno\scenes\dyno_default.scene / scene / 216; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 99; base\quest\holocalls\dino\dino_holocall.scene / scene / 42; base\quest\holocalls\dino\dino_holocall.scene / scene / 553; 14 total source locations in compressed evidence |
| `holo_dino_calls_v_rejectable` | base\quest\holocalls\dino\dino_holocall.scene / scene / 636; base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_holocall_debriefs.scene / scene / 283; base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_holocall_prebrief.scene / scene / 254; base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_holocall_prebrief.scene / scene / 285; 14 total source locations in compressed evidence |
| `holo_dino_calls_v_rejected` | base\quest\holocalls\dino\dino_holocall.scene / scene / 644; base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_holocall_debriefs.scene / scene / 285; base\open_world\street_stories\city_center\downtown\sts_cct_dtn_02\scenes\sts_cct_dtn_02_holocall_prebrief.scene / scene / 256; base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\scenes\sts_cct_dtn_03_holocall_debriefs.scene / scene / 293; 10 total source locations in compressed evidence |
| `holo_dino_calls_v_start_activate` | base\open_world\fixers\dyno\phases\dyno.questphase / h0 / 43; base\open_world\fixers\dyno\scenes\dyno_default.scene / scene / 219; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase / h228 / 78; base\open_world\street_stories\city_center\corpo_plaza\sts_cct_corpo_plaza.questphase / h629 / 67; 51 total source locations in compressed evidence |
| `holo_dino_calls_v_start_done` | base\open_world\fixers\dyno\scenes\dyno_default.scene / scene / 214; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 98; base\quest\holocalls\dino\dino_holocall.scene / scene / 41; base\quest\holocalls\dino\dino_holocall.scene / scene / 580; 14 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |

NodeRef uses: 113; TweakDB binding uses: 17. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene` | 1 / 3 | scnDialogLineEvent: 3 |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_prebrief.scene` | 1 / 3 | scnDialogLineEvent: 3 |
| `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_prisoner_chat.scene` | 13 / 114 | scnChangeIdleAnimEvent: 5; scnDialogLineEvent: 20; scnGameplayTransitionEvent: 3; scnIKEvent: 6; scnLookAtEvent: 12; scnPlaySkAnimEvent: 32; scnUnmountEvent: 3; scneventsEquipItemToPerformer: 2; scneventsSetAnimFeatureEvent: 3; scneventsSocket: 27; scneventsUnequipItemFromPerformer: 1 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
