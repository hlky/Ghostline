# Gig: Fifth Column

Journal: `quests/street_stories/heywood/glen/sts_hey_gle_04` · `StreetStory` · hash `1009463697`.

Journal premise: Gig type: Thievery\nObjective: Steal data on Javier Alvarado's embezzlement activity\nLocation: El Pinche Pollo Restaurant\nDetails:\n\nIt's election season so everyone's got a political stick up their ass. Can't say I like it but it is good for biz.\n\nYoung woman came up to me, claims to be a media. She must be a wizard with words because I've never seen a mediajock like her burn so much cash.\n\nShe's fishing for dirt on the mayor's adviser, Javier Alvarado. Says Alvarado is bezzling public money, padding the Valentinos' pockets.\n\nProof? Apparently found in the office of El Pinche Pollo, some Valentino-run restaurant. Have a look there. This media seemed confident of her sources.\n\nAnd you know how this rolls. She fronts the eddies, we don't ask who she "writes" for.

**Coverage: journal-linked.** 32 exact journal-linked nodes in 4 resources; 7 resources in the inspected dependency context.

Resource roles in that context: 5 content candidate, 2 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Enter the restaurant. (Primary) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in` |
| Get inside the office. (Primary) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in_inner` |
| Leave the restaurant. (Primary) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/leave_the_area` |
| Steal the incriminating data. (Primary) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/main_objective` |
| Find incriminating evidence on the mayor's advisor. (Primary) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/steal_evidence` |
| Drink to Jackie with the bouncer. (Optional) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/have_a_drink` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_hey_gle_04_bugfixing.questphase / h14 / 12` (Condition) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04` | 12:False → 1:In; 7:True → 12:In; 12:True → 8:In; 12:True → 9:In; 12:True → 15:In |
| `sts_hey_gle_04_bugfixing.questphase / h106 / 20` (Condition) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/leave_the_area` | 20:False → 1:In; 5:Out → 20:In; 20:True → 40:In |
| `sts_hey_gle_04_ow.questphase / h67 / 3` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in` | 38:False → 3:Active; 3:Out → 11:In |
| `sts_hey_gle_04_ow.questphase / h67 / 5` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in` | 11:Out → 5:Succeeded; 5:Out → 6:Active; 5:Out → 51:In |
| `sts_hey_gle_04_ow.questphase / h67 / 6` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in_inner` | 5:Out → 6:Active; 6:Out → 13:In |
| `sts_hey_gle_04_ow.questphase / h67 / 7` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in_inner` | 13:Out → 7:Succeeded; 51:Out → 7:Succeeded; 7:Out → 102:Active |
| `sts_hey_gle_04_ow.questphase / h67 / 10` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04` | 84:Out → 10:Succeeded; 10:Out → 109:In |
| `sts_hey_gle_04_ow.questphase / h67 / 40` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in` | 40:Out → 11:In; 38:True → 40:Active |
| `sts_hey_gle_04_ow.questphase / h67 / 41` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/brief` | 41:Out → 38:In; 45:Out → 41:Active |
| `sts_hey_gle_04_ow.questphase / h67 / 102` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/steal_evidence` | 7:Out → 102:Active |
| `sts_hey_gle_04_ow.questphase / h67 / 104` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/steal_evidence` | 92:Out → 104:Succeeded; 104:Out → 112:Active |
| `sts_hey_gle_04_ow.questphase / h67 / 112` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/leave_the_area` | 104:Out → 112:Active; 112:Out → 110:Active |
| `sts_hey_gle_04_ow.questphase / h67 / 114` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/leave_the_area` | 113:Out → 114:Succeeded; 114:Out → 147:In |
| `sts_hey_gle_04_ow.questphase / h67 / 125` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/have_a_drink` | 127:Out → 125:Active; 125:Out → 134:In; 125:Out → 133:In |
| `sts_hey_gle_04_ow.questphase / h67 / 128` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/have_a_drink` | 133:Out → 128:Failed |
| `sts_hey_gle_04_ow.questphase / h67 / 129` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/have_a_drink` | 134:Out → 129:Succeeded |
| `sts_hey_glenn.questphase / h479 / 3` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in` | 38:False → 3:Active; 3:Out → 11:In |
| `sts_hey_glenn.questphase / h479 / 5` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in` | 11:Out → 5:Succeeded; 5:Out → 6:Active; 5:Out → 51:In |
| `sts_hey_glenn.questphase / h479 / 6` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in_inner` | 5:Out → 6:Active; 6:Out → 13:In |
| `sts_hey_glenn.questphase / h479 / 7` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in_inner` | 13:Out → 7:Succeeded; 51:Out → 7:Succeeded; 7:Out → 102:Active |
| `sts_hey_glenn.questphase / h479 / 10` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04` | 84:Out → 10:Succeeded; 10:Out → 109:In |
| `sts_hey_glenn.questphase / h479 / 40` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/get_in` | 40:Out → 11:In; 38:True → 40:Active |
| `sts_hey_glenn.questphase / h479 / 41` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/brief` | 41:Out → 38:In; 45:Out → 41:Active |
| `sts_hey_glenn.questphase / h479 / 102` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/steal_evidence` | 7:Out → 102:Active |
| `sts_hey_glenn.questphase / h479 / 104` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/steal_evidence` | 92:Out → 104:Succeeded; 104:Out → 112:Active |
| `sts_hey_glenn.questphase / h479 / 112` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/leave_the_area` | 104:Out → 112:Active; 112:Out → 110:Active |
| `sts_hey_glenn.questphase / h479 / 114` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/leave_the_area` | 113:Out → 114:Succeeded; 114:Out → 147:In |
| `sts_hey_glenn.questphase / h479 / 125` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/have_a_drink` | 127:Out → 125:Active; 125:Out → 134:In; 125:Out → 133:In |
| `sts_hey_glenn.questphase / h479 / 128` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/have_a_drink` | 133:Out → 128:Failed |
| `sts_hey_glenn.questphase / h479 / 129` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/have_a_drink` | 134:Out → 129:Succeeded |
| `open_world_bugfixing.questphase / h1127 / 3` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04` | 2:True → 3:Succeeded |
| `open_world_bugfixing.questphase / h2262 / 3` (Journal) | `quests/street_stories/heywood/glen/sts_hey_gle_04` | 2:True → 3:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_hey_gle_04_ow.questphase / h67 / 138` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_prebrief.scene`; `#sts_sm_hey_gle_04_holocall_prebrief` | 138:End 0 → 99:Active; 138:rejected_out → 99:Active; 140:True → 138:Start 0; 138:Holocall INT → 146:In; 138:Holocall RET → 141:In |
| `sts_hey_gle_04_ow.questphase / h67 / 139` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene`; `#sts_sm_hey_gle_04_holocall_debriefs` | 156:Out → 139:Start 0; 139:End 0 → 155:In; 139:rejected_out → 162:Active; 139:Holocall INT → 145:In; 139:Holocall RET → 143:In |
| `sts_hey_gle_04_ow.questphase / h745 / 15` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_johnny.scene`; `#sts_sm_hey_gle_04_johnny` | 15:End 0 → 1:In; 4:Out → 15:Start 0 |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\bugfixing\sts\sts_glen_bugfixing.questphase` / h0 / 6 | `sts_hey_gle_04_bugfixing.questphase` | 5: DeletionMarker; 5:Out → 6:In1 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04.questphase` / h0 / 8 | `sts_hey_gle_04_ow.questphase` | 12: Checkpoint; 12:Out → 8:In1; 8:Out1 → 10:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h4727 / 8 | `sts_hey_gle_04_ow.questphase` | 12: Checkpoint; 12:Out → 8:In1; 8:Out1 → 10:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` / h67 / 139 | `sts_hey_gle_04_holocall_debriefs.scene` | 156: PauseCondition: {"seconds": 2}; 156:Out → 139:Start 0; 139:End 0 → 155:In; 139:rejected_out → 162:Active; 139:Holocall INT → 145:In; 139:Holocall RET → 143:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h479 / 139 | `sts_hey_gle_04_holocall_debriefs.scene` | 156: PauseCondition: {"seconds": 2}; 156:Out → 139:Start 0; 139:End 0 → 155:In; 139:rejected_out → 162:Active; 139:Holocall INT → 145:In; 139:Holocall RET → 143:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` / h67 / 138 | `sts_hey_gle_04_holocall_prebrief.scene` | 140: Condition; 138:End 0 → 99:Active; 138:rejected_out → 99:Active; 140:True → 138:Start 0; 138:Holocall INT → 146:In; 138:Holocall RET → 141:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h479 / 138 | `sts_hey_gle_04_holocall_prebrief.scene` | 140: Condition; 138:End 0 → 99:Active; 138:rejected_out → 99:Active; 140:True → 138:Start 0; 138:Holocall INT → 146:In; 138:Holocall RET → 141:In |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` / h745 / 15 | `sts_hey_gle_04_johnny.scene` | 4: FactsDBManager: gle_04_got_evidence; 15:End 0 → 1:In; 4:Out → 15:Start 0 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h1157 / 15 | `sts_hey_gle_04_johnny.scene` | 4: FactsDBManager: gle_04_got_evidence; 15:End 0 → 1:In; 4:Out → 15:Start 0 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn_test.quest` / h0 / 0 | `sts_hey_glenn.questphase` | 2: FactsDBManager: debug_sts_start; 2:Out → 0:In1 |
| `base\open_world\street_stories\heywood\sts_heywood.questphase` / h0 / 2 | `sts_hey_glenn.questphase` | 0: Input; 0:Out → 2:In1 |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\quest\bugfixing\open_world_bugfixing.questphase` / h11 / 42 | `sts_glen_bugfixing.questphase` | 9: DeletionMarker; 9:Out → 42:In1 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\sts_hey_gle_04.quest` / h0 / 15 | `sts_hey_gle_04.questphase` | 19: FactsDBManager: gle_04_testdef; 15:Out1 → 1:In; 19:Out → 15:In1 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` / h0 / 2 | `sts_hey_gle_04.questphase` | 67: Journal; 67:Out → 2:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 4 | `sts_heywood.questphase` | 0: Input; 21: Input; 0:Out → 4:In1; 21:Out → 4:sts_hey_rey_02_bugfixing |
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
| `sts_hey_gle_04_holocall_debriefs.scene` | Start 0 → End 0, rejected_out | padre; 23 nodes / 30 edges |
| `sts_hey_gle_04_holocall_prebrief.scene` | Start 0 → End 0, rejected_out | padre; 22 nodes / 25 edges |
| `sts_hey_gle_04_johnny.scene` | Start 0 → End 0 | Johnny; Player; 8 nodes / 7 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `CYB-592653` | sts_hey_gle_04_bugfixing.questphase / h14 / 5 | sts_hey_gle_04_bugfixing.questphase / h14 / 6 |
| `CYB-598628` | sts_hey_gle_04_bugfixing.questphase / h106 / 5 | sts_hey_gle_04_bugfixing.questphase / h106 / 6 |
| `CYB-620886` | sts_hey_gle_04_bugfixing.questphase / h224 / 2 | sts_hey_gle_04_bugfixing.questphase / h224 / 3 |
| `gle_04_data_is_stolen` | sts_hey_gle_04_ow.questphase / h67 / 52 | sts_hey_gle_04_ow.questphase / h745 / 17 |
| `gle_04_drink_with_bouncer` | Producer outside selected context | sts_hey_gle_04_ow.questphase / h67 / 127; sts_hey_gle_04_ow.questphase / h67 / 133; sts_hey_gle_04_ow.questphase / h67 / 134; sts_hey_glenn.questphase / h479 / 127; sts_hey_glenn.questphase / h479 / 133; sts_hey_glenn.questphase / h479 / 134 |
| `gle_04_finished` | sts_hey_gle_04_ow.questphase / h67 / 84; sts_hey_glenn.questphase / h479 / 84 | open_world_bugfixing.questphase / h1127 / 2; open_world_bugfixing.questphase / h2262 / 2; sts_hey_gle_04_bugfixing.questphase / h224 / 8 |
| `gle_04_gang_chase` | sts_hey_gle_04_ow.questphase / h520 / 67 | No reader in selected context |
| `gle_04_gang_retaliation` | Producer outside selected context | sts_hey_gle_04_ow.questphase / h520 / 64 |
| `gle_04_got_evidence` | sts_hey_gle_04_ow.questphase / h745 / 4 | No reader in selected context |
| `gle_04_high_level_netrunner_hacked` | Producer outside selected context | sts_hey_gle_04_ow.questphase / h67 / 51; sts_hey_glenn.questphase / h479 / 51 |
| `gle_04_start` | sts_hey_gle_04_ow.questphase / h12 / 15 | sts_hey_gle_04_bugfixing.questphase / h224 / 5 |
| `gle_04_testdef` | Producer outside selected context | sts_hey_gle_04_ow.questphase / h67 / 38; sts_hey_glenn.questphase / h479 / 38 |
| `glossary_valentinos` | sts_hey_gle_04_ow.questphase / h67 / 45; sts_hey_glenn.questphase / h479 / 45 | No reader in selected context |
| `hey_achievement` | sts_hey_gle_04_ow.questphase / h520 / 13 | sts_hey_gle_04_ow.questphase / h520 / 60 |
| `holo_active_call_interrupted` | Producer outside selected context | sts_hey_gle_04_holocall_prebrief.scene / scene / 282 |
| `holo_padre_calls_v_end_activate` | sts_hey_gle_04_holocall_debriefs.scene / scene / 66; sts_hey_gle_04_holocall_prebrief.scene / scene / 66; sts_hey_gle_04_ow.questphase / h67 / 145; sts_hey_gle_04_ow.questphase / h67 / 146 | No reader in selected context |
| `holo_padre_calls_v_end_done` | sts_hey_gle_04_holocall_debriefs.scene / scene / 62; sts_hey_gle_04_holocall_prebrief.scene / scene / 62 | sts_hey_gle_04_holocall_debriefs.scene / scene / 61; sts_hey_gle_04_holocall_prebrief.scene / scene / 61 |
| `holo_padre_calls_v_rejectable` | sts_hey_gle_04_holocall_debriefs.scene / scene / 285; sts_hey_gle_04_holocall_prebrief.scene / scene / 256; sts_hey_gle_04_holocall_prebrief.scene / scene / 288 | No reader in selected context |
| `holo_padre_calls_v_rejected` | sts_hey_gle_04_holocall_debriefs.scene / scene / 289; sts_hey_gle_04_holocall_prebrief.scene / scene / 260 | sts_hey_gle_04_holocall_debriefs.scene / scene / 287; sts_hey_gle_04_holocall_prebrief.scene / scene / 258 |
| `holo_padre_calls_v_start_activate` | sts_hey_gle_04_holocall_debriefs.scene / scene / 257; sts_hey_gle_04_holocall_debriefs.scene / scene / 65; sts_hey_gle_04_holocall_prebrief.scene / scene / 286; sts_hey_gle_04_holocall_prebrief.scene / scene / 65; sts_hey_gle_04_ow.questphase / h67 / 141; sts_hey_gle_04_ow.questphase / h67 / 143 | sts_hey_gle_04_holocall_debriefs.scene / scene / 251 |
| `holo_padre_calls_v_start_done` | sts_hey_gle_04_holocall_debriefs.scene / scene / 60; sts_hey_gle_04_holocall_prebrief.scene / scene / 60 | sts_hey_gle_04_holocall_debriefs.scene / scene / 273; sts_hey_gle_04_holocall_prebrief.scene / scene / 269 |
| `holo_setup_active` | Producer outside selected context | sts_hey_gle_04_holocall_debriefs.scene / scene / 251; sts_hey_gle_04_holocall_prebrief.scene / scene / 282 |
| `holo_setup_started` | Producer outside selected context | sts_hey_gle_04_holocall_debriefs.scene / scene / 251; sts_hey_gle_04_holocall_prebrief.scene / scene / 282 |
| `sts_hey_gle_04_window_second_ws` | Producer outside selected context | sts_hey_gle_04_bugfixing.questphase / h14 / 7 |
| `sts_valentinos_retaliation` | sts_hey_gle_04_ow.questphase / h520 / 65 | No reader in selected context |
| `travelling_merchant_lives` | Producer outside selected context | sts_hey_gle_04_bugfixing.questphase / h0 / 14 |

## Exact gates, joins and cancellation

<details><summary>67 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_hey_gle_04_bugfixing.questphase / h0 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"travelling_merchant_lives","value":9999,"comparisonType":"GreaterOrEqual"}}}` | 15:Out → 14:In |
| `sts_hey_gle_04_bugfixing.questphase / h14 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":45}}}` | 10:Out1 → 4:In; 4:Out → 16:In |
| `sts_hey_gle_04_bugfixing.questphase / h14 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-592653"}}}` | 0:Out → 6:In; 6:False → 5:In |
| `sts_hey_gle_04_bugfixing.questphase / h14 / 7` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"sts_hey_gle_04_window_second_ws","comparisonType":"Equal"}}}` | 7:False → 1:In; 5:Out → 7:In; 7:True → 12:In |
| `sts_hey_gle_04_bugfixing.questphase / h14 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_04_tr_phone_scene_01"}}` | 12:True → 8:In; 8:Out → 10:In1 |
| `sts_hey_gle_04_bugfixing.questphase / h14 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_04_tr_phone_scene_02"}}` | 12:True → 9:In; 9:Out → 10:In2 |
| `sts_hey_gle_04_bugfixing.questphase / h14 / 10` | `questLogicalXorNodeDefinition` `{}` | 10:Out1 → 4:In; 8:Out → 10:In1; 9:Out → 10:In2 |
| `sts_hey_gle_04_bugfixing.questphase / h14 / 12` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04","fileEntryIndex":4,"className":"gameJournalQuestPhase"},"state":"Active"}}}` | 12:False → 1:In; 7:True → 12:In; 12:True → 8:In; 12:True → 9:In; 12:True → 15:In |
| `sts_hey_gle_04_bugfixing.questphase / h14 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_04_com","names":["gle_04_window"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false}}}}` | 15:Out → 1:In; 12:True → 15:In |
| `sts_hey_gle_04_bugfixing.questphase / h106 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-598628"}}}` | 0:Out → 6:In; 6:False → 5:In |
| `sts_hey_gle_04_bugfixing.questphase / h106 / 20` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/street_stories/heywood/glen/sts_hey_gle_04/sts_hey_gle_04/leave_the_area","fileEntryIndex":4,"className":"gameJournalQuestObjective"},"state":"Succeeded"}}}` | 20:False → 1:In; 5:Out → 20:In; 20:True → 40:In |
| `sts_hey_gle_04_bugfixing.questphase / h106 / 28` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 28:Out1 → 1:In; 21:Out → 28:In1; 25:Out → 28:In3; 26:Out → 28:In4; 27:Out → 28:In2 |
| `sts_hey_gle_04_bugfixing.questphase / h106 / 34` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#gle_04_tr_CP"}}` | 34:Out → 21:In; 34:Out → 22:In; 34:Out → 23:In; 34:Out → 24:In; 39:Out → 34:In |
| `sts_hey_gle_04_bugfixing.questphase / h106 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 39:Out → 34:In; 40:Out → 39:In |
| `sts_hey_gle_04_bugfixing.questphase / h224 / 3` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"CYB-620886"}}}` | 0:Out → 3:In; 3:False → 2:In |
| `sts_hey_gle_04_bugfixing.questphase / h224 / 5` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_start"}}}` | 2:Out → 5:In; 5:True → 8:In |
| `sts_hey_gle_04_bugfixing.questphase / h224 / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_04_com","names":["gle_04_window"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false}}}}` | 8:True → 6:In; 6:True → 7:In |
| `sts_hey_gle_04_bugfixing.questphase / h224 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#gle_04_com","names":["gle_04_window"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1}}}}` | 7:Out → 4:In; 6:True → 7:In |
| `sts_hey_gle_04_bugfixing.questphase / h224 / 8` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_finished","comparisonType":"Equal"}}}` | 5:True → 8:In; 8:True → 6:In |
| `sts_hey_gle_04_ow.questphase / h67 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_04_tr_inside"}}` | 3:Out → 11:In; 11:Out → 5:Succeeded; 40:Out → 11:In; 11:Out → 151:In |
| `sts_hey_gle_04_ow.questphase / h67 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_04_tr_office"}}` | 6:Out → 13:In; 13:Out → 7:Succeeded; 92:CutSource → 13:CutDestination |
| `sts_hey_gle_04_ow.questphase / h67 / 38` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_testdef"}}}` | 38:False → 3:Active; 41:Out → 38:In; 38:True → 40:Active |
| `sts_hey_gle_04_ow.questphase / h67 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_high_level_netrunner_hacked","value":1,"comparisonType":"GreaterOrEqual"}}}` | 5:Out → 51:In; 51:Out → 7:Succeeded; 51:Out → 59:In |
| `sts_hey_gle_04_ow.questphase / h67 / 92` | `questCutControlNodeDefinition` `{"permanent":true}` | 92:CutSource → 13:CutDestination; 137:Out → 92:In; 92:Out → 104:Succeeded |
| `sts_hey_gle_04_ow.questphase / h67 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_04_tr_inside"}}` | 99:Out → 107:In; 107:Out → 105:In; 106:Out → 107:In |
| `sts_hey_gle_04_ow.questphase / h67 / 108` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#gle_04_tr_inside"}}` | 105:Out → 108:In; 108:Out → 106:In |
| `sts_hey_gle_04_ow.questphase / h67 / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#gle_04_tr_inside"}}` | 110:Out → 113:In; 113:Out → 114:Succeeded |
| `sts_hey_gle_04_ow.questphase / h67 / 127` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_drink_with_bouncer","value":1,"comparisonType":"Equal"}}}` | 0:Out → 127:In; 127:Out → 125:Active |
| `sts_hey_gle_04_ow.questphase / h67 / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_drink_with_bouncer","value":2,"comparisonType":"Equal"}}}` | 125:Out → 133:In; 133:Out → 128:Failed |
| `sts_hey_gle_04_ow.questphase / h67 / 134` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_drink_with_bouncer","value":3,"comparisonType":"Equal"}}}` | 125:Out → 134:In; 134:Out → 129:Succeeded |
| `sts_hey_gle_04_ow.questphase / h67 / 140` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 140:False → 99:Active; 140:True → 138:Start 0; 159:False → 140:In |
| `sts_hey_gle_04_ow.questphase / h67 / 150` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#gle_04_dvc_office_computer","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 150:Out → 47:In; 149:Out → 150:In |
| `sts_hey_gle_04_ow.questphase / h67 / 154` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\glenn\\sts_hey_gle_04\\scenes\\sts_hey_gle_04_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}},{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\heywood\\glenn\\sts_hey_gle_04\\scenes\\sts_hey_gle_04_holocall_debriefs.scene","Flags":"Soft"},"type":"IsOutside"}}]}}` | 154:Out → 84:In; 155:Out → 154:In; 162:Out → 154:In |
| `sts_hey_gle_04_ow.questphase / h67 / 155` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 139:End 0 → 155:In; 155:Out → 154:In |
| `sts_hey_gle_04_ow.questphase / h67 / 156` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 156:Out → 139:Start 0; 161:False → 156:In |
| `sts_hey_gle_04_ow.questphase / h67 / 159` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 0:Out → 159:In; 159:True → 99:Active; 159:False → 140:In |
| `sts_hey_gle_04_ow.questphase / h67 / 161` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 161:False → 156:In; 158:Out → 161:In; 161:True → 162:Active |
| `sts_hey_gle_04_ow.questphase / h520 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#gle_04_tr_CP"}}` | 57:Out → 28:In; 57:Out → 30:In; 57:Out → 31:In; 57:Out → 32:In; 58:Out → 57:In |
| `sts_hey_gle_04_ow.questphase / h520 / 59` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 59:Out1 → 25:In; 28:Out → 59:In1; 33:Out → 59:In2; 34:Out → 59:In4; 35:Out → 59:In3 |
| `sts_hey_gle_04_ow.questphase / h520 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":1}}}` | 61:Out → 58:In; 62:Out → 61:In |
| `sts_hey_gle_04_ow.questphase / h520 / 64` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_gang_retaliation","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 64:In; 64:False → 63:In; 64:True → 67:In |
| `sts_hey_gle_04_ow.questphase / h745 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_data_is_stolen","value":1,"comparisonType":"GreaterOrEqual"}}}` | 0:Out → 17:In; 17:Out → 4:In |
| `sts_hey_gle_04_holocall_debriefs.scene / scene / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_end_done"}}}` | 61:0:0 → 62:0:1; 66:0:0 → 61:0:1 |
| `sts_hey_gle_04_holocall_debriefs.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 59:666:0 → 249:0:1; 249:0:0 → 251:0:1; 259:0:0 → 249:0:1; 261:1:0 → 249:0:0; 261:1:0 → 249:1026:0 |
| `sts_hey_gle_04_holocall_debriefs.scene / scene / 251` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 249:0:0 → 251:0:1; 251:0:0 → 253:0:1; 261:1:0 → 251:0:0; 261:1:0 → 251:1026:0 |
| `sts_hey_gle_04_holocall_debriefs.scene / scene / 253` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 251:0:0 → 253:0:1; 253:0:0 → 255:0:1; 261:1:0 → 253:0:0; 261:1:0 → 253:1026:0 |
| `sts_hey_gle_04_holocall_debriefs.scene / scene / 255` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 253:0:0 → 255:0:1; 255:0:0 → 257:0:1; 255:0:1 → 259:0:0 |
| `sts_hey_gle_04_holocall_debriefs.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_done"}}}` | 59:666:0 → 273:0:1; 273:0:0 → 261:0:0 |
| `sts_hey_gle_04_holocall_debriefs.scene / scene / 287` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_rejected"}}}` | 65:0:0 → 287:0:1; 287:0:0 → 289:0:1 |
| `sts_hey_gle_04_holocall_prebrief.scene / scene / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_end_done"}}}` | 61:0:0 → 62:0:1; 66:0:0 → 61:0:1 |
| `sts_hey_gle_04_holocall_prebrief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_rejected"}}}` | 65:0:0 → 258:0:1; 258:0:0 → 260:0:1 |
| `sts_hey_gle_04_holocall_prebrief.scene / scene / 269` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_padre_calls_v_start_done"}}}` | 59:666:0 → 269:0:1; 269:0:0 → 272:0:0 |
| `sts_hey_gle_04_holocall_prebrief.scene / scene / 275` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 59:666:0 → 275:0:1; 272:1:0 → 275:0:0; 275:0:0 → 282:0:1 |
| `sts_hey_gle_04_holocall_prebrief.scene / scene / 282` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 275:0:0 → 282:0:1; 282:0:0 → 288:0:1; 282:0:1 → 284:0:1; 284:0:0 → 282:0:1 |
| `sts_hey_gle_04_holocall_prebrief.scene / scene / 284` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 272:1:0 → 284:0:0; 282:0:1 → 284:0:1; 284:0:0 → 282:0:1 |
| `sts_hey_gle_04_johnny.scene / scene / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_sts_hey_gle_04_johnny_Johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"angleTolerance":92.0,"inverted":true}}}` | 4:0:0 → 13:0:1; 13:0:0 → 8:0:1 |
| `sts_hey_glenn.questphase / h479 / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_04_tr_inside"}}` | 3:Out → 11:In; 11:Out → 5:Succeeded; 40:Out → 11:In; 11:Out → 151:In |
| `sts_hey_glenn.questphase / h479 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#gle_04_tr_office"}}` | 6:Out → 13:In; 13:Out → 7:Succeeded; 92:CutSource → 13:CutDestination |
| `sts_hey_glenn.questphase / h479 / 38` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_testdef"}}}` | 38:False → 3:Active; 41:Out → 38:In; 38:True → 40:Active |
| `sts_hey_glenn.questphase / h479 / 51` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_high_level_netrunner_hacked","value":1,"comparisonType":"GreaterOrEqual"}}}` | 5:Out → 51:In; 51:Out → 7:Succeeded; 51:Out → 59:In |
| `sts_hey_glenn.questphase / h479 / 92` | `questCutControlNodeDefinition` `{"permanent":true}` | 92:CutSource → 13:CutDestination; 137:Out → 92:In; 92:Out → 104:Succeeded |
| `sts_hey_glenn.questphase / h479 / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#gle_04_tr_inside"}}` | 110:Out → 113:In; 113:Out → 114:Succeeded |
| `sts_hey_glenn.questphase / h479 / 127` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_drink_with_bouncer","value":1,"comparisonType":"Equal"}}}` | 0:Out → 127:In; 127:Out → 125:Active |
| `sts_hey_glenn.questphase / h479 / 133` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_drink_with_bouncer","value":2,"comparisonType":"Equal"}}}` | 125:Out → 133:In; 133:Out → 128:Failed |
| `sts_hey_glenn.questphase / h479 / 134` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_drink_with_bouncer","value":3,"comparisonType":"Equal"}}}` | 125:Out → 134:In; 134:Out → 129:Succeeded |
| `open_world_bugfixing.questphase / h1127 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_finished"}}}` | 0:Out → 2:In; 2:True → 3:Succeeded |
| `open_world_bugfixing.questphase / h2262 / 2` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"gle_04_finished"}}}` | 0:Out → 2:In; 2:True → 3:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | sts_hey_gle_04_bugfixing.questphase / h14 / 15; sts_hey_gle_04_bugfixing.questphase / h224 / 7 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `checkpoint` | sts_hey_gle_04_ow.questphase / h520 / 11 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `community_lifecycle` | sts_hey_gle_04_bugfixing.questphase / h14 / 16; sts_hey_gle_04_ow.questphase / h520 / 24; sts_hey_gle_04_ow.questphase / h520 / 49; sts_hey_gle_04_ow.questphase / h520 / 52 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1127 / 2; open_world_bugfixing.questphase / h2262 / 2; sts_hey_gle_04_bugfixing.questphase / h0 / 14; sts_hey_gle_04_bugfixing.questphase / h106 / 6; +25 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_hey_gle_04_ow.questphase / h520 / 12; sts_hey_gle_04_ow.questphase / h520 / 63; sts_hey_gle_04_ow.questphase / h67 / 105; sts_hey_gle_04_ow.questphase / h67 / 106; +4 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sts_hey_gle_04_bugfixing.questphase / h106 / 21; sts_hey_gle_04_bugfixing.questphase / h106 / 22; sts_hey_gle_04_bugfixing.questphase / h106 / 23; sts_hey_gle_04_bugfixing.questphase / h106 / 24; +13 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_hey_gle_04_ow.questphase / h12 / 22; sts_hey_gle_04_ow.questphase / h520 / 25; sts_hey_gle_04_ow.questphase / h520 / 44; sts_hey_gle_04_ow.questphase / h520 / 45; +5 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_hey_gle_04_ow.questphase / h67 / 150 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_hey_gle_04_bugfixing.questphase / h106 / 39; sts_hey_gle_04_ow.questphase / h520 / 61 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | open_world_bugfixing.questphase / h1127 / 3; open_world_bugfixing.questphase / h2262 / 3; sts_hey_gle_04_ow.questphase / h0 / 10; sts_hey_gle_04_ow.questphase / h12 / 14; +32 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `parallel_join` | sts_hey_gle_04_bugfixing.questphase / h106 / 28; sts_hey_gle_04_ow.questphase / h520 / 59 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | sts_hey_gle_04_bugfixing.questphase / h106 / 5; sts_hey_gle_04_bugfixing.questphase / h14 / 5; sts_hey_gle_04_bugfixing.questphase / h224 / 2; sts_hey_gle_04_holocall_debriefs.scene / scene / 257; +28 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | sts_hey_gle_04_bugfixing.questphase / h14 / 10 | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | sts_hey_gle_04_bugfixing.questphase / h14 / 4; sts_hey_gle_04_holocall_debriefs.scene / scene / 249; sts_hey_gle_04_holocall_debriefs.scene / scene / 253; sts_hey_gle_04_holocall_prebrief.scene / scene / 275; +3 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | sts_hey_gle_04_ow.questphase / h67 / 92; sts_hey_glenn.questphase / h479 / 92 | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | sts_hey_gle_04_ow.questphase / h520 / 8 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sts_hey_gle_04_ow.questphase / h67 / 138; sts_hey_gle_04_ow.questphase / h67 / 139; sts_hey_gle_04_ow.questphase / h745 / 15 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_hey_gle_04_bugfixing.questphase / h106 / 34; sts_hey_gle_04_bugfixing.questphase / h14 / 8; sts_hey_gle_04_bugfixing.questphase / h14 / 9; sts_hey_gle_04_ow.questphase / h520 / 57; +8 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | sts_hey_gle_04_bugfixing.questphase / h224 / 6 | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `workspot_performance` | sts_hey_gle_04_johnny.scene / scene / 28; sts_hey_gle_04_johnny.scene / scene / 30; sts_hey_gle_04_johnny.scene / scene / 7; sts_hey_gle_04_johnny.scene / scene / 8 | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |
| `world_variant` | sts_hey_gle_04_ow.questphase / h12 / 30; sts_hey_gle_04_ow.questphase / h520 / 53; sts_hey_gle_04_ow.questphase / h520 / 55 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_bugfixing.questphase` | repair; journal anchor | `base-sts-hey-gle-04` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` | content candidate; journal anchor | `base-sts-hey-gle-04` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene` | content candidate; forward dependency | `base-sts-hey-gle-04` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-hey-gle-04` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_johnny.scene` | content candidate; forward dependency | `base-sts-hey-gle-04` |
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-gle-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-gle-04.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

176 repeated typed/socket path signatures in this selected graph context; 25 distinct direct resource identities; 7 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `20a77143a898bc753a26` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` / h520 / 24 -> 52 -> 49 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]; Out -> In; Out -> In |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene` / scene / 65 -> 287 -> 289 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `fee3756653cd083fb28e` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_bugfixing.questphase` / h106 / 40 -> 39 -> 34 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene` / scene / 64 -> 66 -> 61 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene` / scene / 287 -> 289 -> 283 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene` / scene / 60 -> 63 -> 29 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene` / scene / 29 -> 64 -> 66 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene` / scene / 285 -> 65 -> 287 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene` / scene / 1 -> 285 -> 65 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `eaf5aab427d50e5598b6` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_bugfixing.questphase` / h14 / 0 -> 6 -> 5 | questInputNodeDefinition -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> In; False -> In |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` / h67 / 11 -> 5 -> 6 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene` / scene / 273 -> 261 -> 249 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_bugfixing.questphase` / h0 / 8 | `h14` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_bugfixing.questphase` / h0 / 12 | `h106` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_bugfixing.questphase` / h0 / 16 | `h224` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` / h0 / 2 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` / h0 / 5 | `h67` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` / h0 / 6 | `h520` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` / h0 / 7 | `h745` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\street_stories\heywood\glenn\sts_hey_glenn_test.gamedef` | content candidate | base\open_world\street_stories\heywood\glenn\sts_hey_glenn_test.quest |
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
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\sts_hey_gle_04_gamedef.gamedef` | content candidate | base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\sts_hey_gle_04.quest |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\sts_hey_gle_04_test.gamedef` | content candidate | base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\sts_hey_gle_04.quest |
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
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__rh_on_chin__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\open_world\generic_average_male_stand__rh_on_chin__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\phases\sts_hey_gle_01.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\phases\sts_hey_gle_01_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\phases\sts_hey_gle_01_streetstory.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\phases\sts_hey_gle_03_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_ow.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\lipsync\en\sts_hey_gle_04_holocall_debriefs\sebastian_padre_perez.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\lipsync\en\sts_hey_gle_04_holocall_prebrief\sebastian_padre_perez.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\lipsync\en\sts_hey_gle_04_johnny\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\lipsync\en\sts_hey_gle_04_johnny\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_johnny.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\phases\sts_hey_gle_05_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\phase\sts_hey_gle_06_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\common\ground\generic__stand_ground__think__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `gle_04_data_is_stolen` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 52; 1 total source locations in compressed evidence |
| `gle_04_drink_with_bouncer` | base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_bouncer.scene / scene / 328; base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_bouncer.scene / scene / 330; base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_bouncer.scene / scene / 333; 3 total source locations in compressed evidence |
| `gle_04_gang_chase` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h932 / 67; 1 total source locations in compressed evidence |
| `gle_04_gang_retaliation` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h3163 / 100; base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_combat.questphase / h7 / 100; 2 total source locations in compressed evidence |
| `gle_04_got_evidence` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h1157 / 4; 1 total source locations in compressed evidence |
| `gle_04_start` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h424 / 15; 1 total source locations in compressed evidence |
| `gle_04_testdef` | base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\sts_hey_gle_04.quest / h0 / 19; 1 total source locations in compressed evidence |
| `glossary_valentinos` | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h294 / 69; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h6436 / 74; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h6919 / 161; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h10479 / 71; 12 total source locations in compressed evidence |
| `hey_achievement` | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_02\ma_hey_spr_02_phase.questphase / h0 / 42; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_03\ma_hey_spr_03_phase.questphase / h0 / 34; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_bugfixing.questphase / h89 / 8; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_10\ma_hey_spr_10_phase.questphase / h0 / 40; 32 total source locations in compressed evidence |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_padre_calls_v_end_activate` | base\open_world\fixers\padre\phases\padre.questphase / h0 / 54; base\open_world\fixers\padre\scenes\padre_default.scene / scene / 148; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 145; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 146; 77 total source locations in compressed evidence |
| `holo_padre_calls_v_end_done` | base\open_world\fixers\padre\scenes\padre_default.scene / scene / 144; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 213; base\quest\holocalls\padre\padre_holocall.scene / scene / 42; base\quest\holocalls\padre\padre_holocall.scene / scene / 541; 24 total source locations in compressed evidence |
| `holo_padre_calls_v_rejectable` | base\quest\holocalls\padre\padre_holocall.scene / scene / 664; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_debriefs.scene / scene / 283; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 269; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 308; 30 total source locations in compressed evidence |
| `holo_padre_calls_v_rejected` | base\quest\holocalls\padre\padre_holocall.scene / scene / 672; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_debriefs.scene / scene / 287; base\open_world\street_stories\heywood\glenn\sts_hey_gle_01\scenes\sts_hey_gle_01_holocall_prebrief.scene / scene / 273; base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_debriefs.scene / scene / 289; 20 total source locations in compressed evidence |
| `holo_padre_calls_v_start_activate` | base\open_world\fixers\padre\phases\padre.questphase / h0 / 53; base\open_world\fixers\padre\scenes\padre_default.scene / scene / 147; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 141; base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h479 / 143; 93 total source locations in compressed evidence |
| `holo_padre_calls_v_start_done` | base\open_world\fixers\padre\scenes\padre_default.scene / scene / 142; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 212; base\quest\holocalls\padre\padre_holocall.scene / scene / 41; base\quest\holocalls\padre\padre_holocall.scene / scene / 527; 24 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `sts_hey_gle_04_window_second_ws` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h3195 / 101; base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\phases\sts_hey_gle_04_combat.questphase / h39 / 101; 2 total source locations in compressed evidence |
| `sts_valentinos_retaliation` | base\open_world\street_stories\heywood\glenn\sts_hey_glenn.questphase / h932 / 65; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h6130 / 88; base\open_world\street_stories\street_stories_gang_retaliation.questphase / h1431 / 23; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\phases\sts_hey_rey_02_open_world.questphase / h281 / 88; 4 total source locations in compressed evidence |

NodeRef uses: 85; TweakDB binding uses: 5. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_debriefs.scene` | 1 / 2 | scnDialogLineEvent: 2 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_holocall_prebrief.scene` | 1 / 3 | scnDialogLineEvent: 3 |
| `base\open_world\street_stories\heywood\glenn\sts_hey_gle_04\scenes\sts_hey_gle_04_johnny.scene` | 1 / 10 | scnDialogLineEvent: 3; scnLookAtEvent: 2; scnPlaySkAnimEvent: 3; scneventsSocket: 2 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
