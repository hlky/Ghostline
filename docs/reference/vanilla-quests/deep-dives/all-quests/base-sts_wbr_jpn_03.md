# Gig: A Shrine Defiled

Journal: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03` · `StreetStory` · hash `1105932277`.

Journal premise: Gig type: Agent Saboteur\nObjective: Place a wiretap in a Tyger Claw-controlled shrine\nLocation: Shinto shrine at Milagro Terrace\nDetails:\n\nThe person should not stray from the road and the tiger should not leave his mountain steppes. Or misfortune will find them both.\n\nTyger Claw boss Taki Kazo thinks he's smart. He thinks I won't find out about his agreement at the shinto shrine on Milagro Terrace. He thinks I don't know he's using the shrine's honden for secret meetings. He thinks he can rule Japantown without my influence. He will be wrong.\n\nI'll give you a wiretap to place right at the shintai in the most sacred of shinto spaces. Don't make a noise. And don't disappoint me.

**Coverage: journal-linked.** 34 exact journal-linked nodes in 3 resources; 5 resources in the inspected dependency context.

Resource roles in that context: 4 content candidate, 1 repair. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\district_definitions\open_world_kabuki.quest`; `base\open_world\open_world_test.quest`; `base\open_world\police_system\police_system_test.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Get out of the shrine complex. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/escape_shrone` |
| Get to the honden. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/find_way_in` |
| Remain undetected. (Optional) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/stealth` |
| Collect your bonus from the Drop Point. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/get_special_reward` |
| Place the wiretap inside the shrine's main hall. (Primary) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/plant_bug_in_honden` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `sts_wbr_japantown.questphase / h11912 / 4` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/find_way_in` | 39:True → 4:Active; 4:Out → 17:In; 4:Out → 15:Active |
| `sts_wbr_japantown.questphase / h11912 / 5` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/escape_shrone` | 10:Out → 5:Active; 5:Out → 6:In |
| `sts_wbr_japantown.questphase / h11912 / 7` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/escape_shrone` | 6:Out → 7:Succeeded; 7:Out → 29:In |
| `sts_wbr_japantown.questphase / h11912 / 10` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/plant_bug_in_honden` | 10:Out → 5:Active; 46:Out → 10:Succeeded; 10:Out → 54:In |
| `sts_wbr_japantown.questphase / h11912 / 13` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03` | 63:Out → 13:Succeeded; 13:Out → 91:In |
| `sts_wbr_japantown.questphase / h11912 / 15` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/stealth` | 4:Out → 15:Active; 40:Out → 15:Active; 15:Out → 20:In |
| `sts_wbr_japantown.questphase / h11912 / 18` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/find_way_in` | 17:Out → 18:Succeeded; 18:Out → 62:Active |
| `sts_wbr_japantown.questphase / h11912 / 21` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/stealth` | 20:Out → 21:Failed |
| `sts_wbr_japantown.questphase / h11912 / 27` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/stealth` | 29:False → 27:Succeeded; 27:Out → 83:In |
| `sts_wbr_japantown.questphase / h11912 / 40` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/find_way_in` | 40:Out → 15:Active; 40:Out → 17:In; 39:False → 40:Active |
| `sts_wbr_japantown.questphase / h11912 / 48` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/get_special_reward` | 70:Out → 48:Active; 48:Out → 51:In |
| `sts_wbr_japantown.questphase / h11912 / 49` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03` | 82:Out → 49:Succeeded; 49:Out → 93:In |
| `sts_wbr_japantown.questphase / h11912 / 62` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/plant_bug_in_honden` | 62:Out → 3:In; 18:Out → 62:Active |
| `sts_wbr_japantown.questphase / h11912 / 63` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/stealth` | 63:Out → 13:Succeeded; 72:Out → 63:Failed |
| `sts_wbr_japantown.questphase / h11912 / 75` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03_brief` | 0:Out → 75:Active |
| `sts_wbr_japantown.questphase / h11912 / 82` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/get_special_reward` | 82:Out → 49:Succeeded; 52:Out → 82:Succeeded |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 4` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/find_way_in` | 39:True → 4:Active; 4:Out → 17:In; 4:Out → 15:Active |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 5` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/escape_shrone` | 10:Out → 5:Active; 5:Out → 6:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 7` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/escape_shrone` | 6:Out → 7:Succeeded; 7:Out → 29:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 10` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/plant_bug_in_honden` | 10:Out → 5:Active; 46:Out → 10:Succeeded; 10:Out → 54:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 13` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03` | 63:Out → 13:Succeeded; 13:Out → 91:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 15` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/stealth` | 4:Out → 15:Active; 40:Out → 15:Active; 15:Out → 20:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 18` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/find_way_in` | 17:Out → 18:Succeeded; 18:Out → 62:Active |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 21` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/stealth` | 20:Out → 21:Failed |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 27` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/stealth` | 29:False → 27:Succeeded; 27:Out → 83:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 40` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/find_way_in` | 40:Out → 15:Active; 40:Out → 17:In; 39:False → 40:Active |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 48` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/get_special_reward` | 70:Out → 48:Active; 48:Out → 51:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 49` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03` | 82:Out → 49:Succeeded; 49:Out → 93:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 62` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/plant_bug_in_honden` | 62:Out → 3:In; 18:Out → 62:Active |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 63` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/stealth` | 63:Out → 13:Succeeded; 72:Out → 63:Failed |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 75` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03_brief` | 0:Out → 75:Active |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 82` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03/sts_wbr_jpn_03/get_special_reward` | 82:Out → 49:Succeeded; 52:Out → 82:Succeeded |
| `open_world_bugfixing.questphase / h674 / 14` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03` | 13:True → 14:Succeeded |
| `open_world_bugfixing.questphase / h1792 / 14` (Journal) | `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03` | 13:True → 14:Succeeded |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 64` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene`; `#sts_sm_wbr_jpn_03_holocall_prebrief` | 64:End 0 → 41:Active; 64:rejected_out → 41:Active; 74:True → 64:Start 0; 64:Holocall INT → 77:In; 64:Holocall RET → 76:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 65` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene`; `#sts_sm_wbr_jpn_03_holocall_debrief` | 102:False → 65:Start 0; 65:End 0 → 68:In; 65:rejected_out → 101:Active; 65:Holocall INT → 79:In; 65:Holocall RET → 78:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 66` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene`; `#sts_sm_wbr_jpn_03_holocall_debrief` | 100:False → 66:Start 0; 66:End 0 → 67:In; 66:rejected_out → 99:Active; 66:Holocall INT → 81:In; 66:Holocall RET → 80:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\sts_westbrook.questphase` / h0 / 3 | `sts_wbr_japantown.questphase` | 0: Input; 0:Out → 3:In1 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h11737 / 13 | `sts_wbr_jpn_03_streetstory.questphase` | 0: Input; 0:Out → 13:In1; 13:Success → 1:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_phase.questphase` / h0 / 13 | `sts_wbr_jpn_03_streetstory.questphase` | 0: Input; 0:Out → 13:In1; 13:Success → 1:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h11912 / 65 | `sts_wbr_jpn_03_holocall_debrief.scene` | 102: Condition; 102:False → 65:Start 0; 65:End 0 → 68:In; 65:rejected_out → 101:Active; 65:Holocall INT → 79:In; 65:Holocall RET → 78:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h11912 / 66 | `sts_wbr_jpn_03_holocall_debrief.scene` | 100: Condition; 100:False → 66:Start 0; 66:End 0 → 67:In; 66:rejected_out → 99:Active; 66:Holocall INT → 81:In; 66:Holocall RET → 80:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h158 / 65 | `sts_wbr_jpn_03_holocall_debrief.scene` | 102: Condition; 102:False → 65:Start 0; 65:End 0 → 68:In; 65:rejected_out → 101:Active; 65:Holocall INT → 79:In; 65:Holocall RET → 78:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h158 / 66 | `sts_wbr_jpn_03_holocall_debrief.scene` | 100: Condition; 100:False → 66:Start 0; 66:End 0 → 67:In; 66:rejected_out → 99:Active; 66:Holocall INT → 81:In; 66:Holocall RET → 80:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h11912 / 64 | `sts_wbr_jpn_03_holocall_prebrief.scene` | 74: Condition; 64:End 0 → 41:Active; 64:rejected_out → 41:Active; 74:True → 64:Start 0; 64:Holocall INT → 77:In; 64:Holocall RET → 76:In |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h158 / 64 | `sts_wbr_jpn_03_holocall_prebrief.scene` | 74: Condition; 64:End 0 → 41:Active; 64:rejected_out → 41:Active; 74:True → 64:Start 0; 64:Holocall INT → 77:In; 64:Holocall RET → 76:In |
| `base\quest\bugfixing.questphase` / h0 / 11 | `open_world_bugfixing.questphase` | 16: DeletionMarker; 16:Out → 11:In1 |
| `base\open_world\street_stories\street_stories.questphase` / h0 / 8 | `sts_westbrook.questphase` | 0: Input; 0:Out → 8:In1 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h0 / 8 | `sts_wbr_jpn_03_phase.questphase` | 29: Journal; 55: Journal; 29:Out → 8:IN; 55:Out → 8:IN |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\sts_wbr_jpn_03.quest` / h0 / 2 | `sts_wbr_jpn_03_phase.questphase` | 5: FactsDBManager: jpb_03_testdef; 2:OUT → 1:In; 5:Out → 2:IN |
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
| `sts_wbr_jpn_03_holocall_debrief.scene` | Start 0 → End 0, rejected_out | fixer; 25 nodes / 33 edges |
| `sts_wbr_jpn_03_holocall_prebrief.scene` | Start 0 → End 0, rejected_out | fixer; 22 nodes / 25 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `holo_active_call_interrupted` | Producer outside selected context | sts_wbr_jpn_03_holocall_prebrief.scene / scene / 279 |
| `holo_setup_active` | Producer outside selected context | sts_wbr_jpn_03_holocall_debrief.scene / scene / 254; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 279 |
| `holo_setup_started` | Producer outside selected context | sts_wbr_jpn_03_holocall_debrief.scene / scene / 254; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 279 |
| `holo_wakako_calls_v_end_activate` | sts_wbr_jpn_03_holocall_debrief.scene / scene / 76; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 71; sts_wbr_jpn_03_streetstory.questphase / h158 / 77; sts_wbr_jpn_03_streetstory.questphase / h158 / 79; sts_wbr_jpn_03_streetstory.questphase / h158 / 81 | No reader in selected context |
| `holo_wakako_calls_v_end_done` | sts_wbr_jpn_03_holocall_debrief.scene / scene / 72; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 69 | sts_wbr_jpn_03_holocall_debrief.scene / scene / 71; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 68 |
| `holo_wakako_calls_v_rejectable` | sts_wbr_jpn_03_holocall_debrief.scene / scene / 279; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 254; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 285 | No reader in selected context |
| `holo_wakako_calls_v_rejected` | sts_wbr_jpn_03_holocall_debrief.scene / scene / 281; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 256 | sts_wbr_jpn_03_holocall_debrief.scene / scene / 283; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 258 |
| `holo_wakako_calls_v_start_activate` | sts_wbr_jpn_03_holocall_debrief.scene / scene / 260; sts_wbr_jpn_03_holocall_debrief.scene / scene / 75; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 283; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 62; sts_wbr_jpn_03_streetstory.questphase / h158 / 76; sts_wbr_jpn_03_streetstory.questphase / h158 / 78; sts_wbr_jpn_03_streetstory.questphase / h158 / 80 | sts_wbr_jpn_03_holocall_debrief.scene / scene / 254 |
| `holo_wakako_calls_v_start_done` | sts_wbr_jpn_03_holocall_debrief.scene / scene / 70; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 60 | sts_wbr_jpn_03_holocall_debrief.scene / scene / 249; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 267 |
| `jpb_03_testdef` | Producer outside selected context | sts_wbr_japantown.questphase / h11912 / 39; sts_wbr_jpn_03_streetstory.questphase / h158 / 39 |
| `jpn_03_finished` | sts_wbr_jpn_03_streetstory.questphase / h687 / 14 | open_world_bugfixing.questphase / h1792 / 13; open_world_bugfixing.questphase / h674 / 13 |
| `jpn_03_start` | sts_wbr_jpn_03_streetstory.questphase / h7 / 7 | No reader in selected context |
| `jpn_03_stealth_fail` | Producer outside selected context | sts_wbr_japantown.questphase / h11912 / 20; sts_wbr_japantown.questphase / h11912 / 29; sts_wbr_jpn_03_holocall_debrief.scene / scene / 31; sts_wbr_jpn_03_streetstory.questphase / h158 / 20; sts_wbr_jpn_03_streetstory.questphase / h158 / 29 |
| `wbr_achievement` | sts_wbr_jpn_03_streetstory.questphase / h687 / 12 | sts_wbr_jpn_03_streetstory.questphase / h687 / 29 |

## Exact gates, joins and cancellation

<details><summary>45 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `sts_wbr_japantown.questphase / h11912 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#jpn_03_go_shintai","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 62:Out → 3:In; 3:Out → 61:In |
| `sts_wbr_japantown.questphase / h11912 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#jpn_03_tr_get_out_001"}}` | 5:Out → 6:In; 6:Out → 7:Succeeded |
| `sts_wbr_japantown.questphase / h11912 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_03_tr_honden_001"}}` | 4:Out → 17:In; 40:Out → 17:In; 17:Out → 18:Succeeded; 17:Out → 53:In |
| `sts_wbr_japantown.questphase / h11912 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_03_stealth_fail","value":1,"comparisonType":"Equal"}}}` | 15:Out → 20:In; 20:Out → 21:Failed |
| `sts_wbr_japantown.questphase / h11912 / 29` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_03_stealth_fail","value":1,"comparisonType":"Equal"}}}` | 7:Out → 29:In; 29:False → 27:Succeeded; 29:True → 72:In |
| `sts_wbr_japantown.questphase / h11912 / 39` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpb_03_testdef","comparisonType":"Equal"}}}` | 0:Out → 39:In; 39:True → 4:Active; 39:False → 40:Active |
| `sts_wbr_japantown.questphase / h11912 / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/c_westbrook/japan_town/japan_town_drop_points_prefab7T6EPDI/drop_point_004_prefabOAR44JI","deviceControllerClass":"DropPointControllerPS","deviceConditionFunction":"IsRewardCollected"}}}` | 51:Out → 52:In; 52:Out → 82:Succeeded |
| `sts_wbr_japantown.questphase / h11912 / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 49:Out → 93:In; 68:Out → 93:In; 93:Out → 92:In |
| `sts_wbr_jpn_03_streetstory.questphase / h7 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_03_tr_sts_area_trigger_001"},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Driving"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterState_ConditionType","subType":{"$type":"questCharacterState_PlayerSubType","vehicleComparisonType":"NotEqual","vehicleState":"Passenger"}}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleScene","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFpp","inverted":true}},{"$type":"questCharacterCondition","type":{"$type":"questCharacterStatusEffect_CondtionType","isPlayer":true,"statusEffectID":"GameplayRestriction.VehicleSceneFppOnlyForward","inverted":true}}]}}` | 29:Out → 8:In; 30:Out → 29:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#jpn_03_go_shintai","deviceControllerClass":"ScriptableDeviceComponentPS","deviceConditionFunction":"IsPersonalLinkConnected"}}}` | 62:Out → 3:In; 3:Out → 61:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#jpn_03_tr_get_out_001"}}` | 5:Out → 6:In; 6:Out → 7:Succeeded |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 17` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_03_tr_honden_001"}}` | 4:Out → 17:In; 40:Out → 17:In; 17:Out → 18:Succeeded; 17:Out → 53:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_03_stealth_fail","value":1,"comparisonType":"Equal"}}}` | 15:Out → 20:In; 20:Out → 21:Failed |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 29` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_03_stealth_fail","value":1,"comparisonType":"Equal"}}}` | 7:Out → 29:In; 29:False → 27:Succeeded; 29:True → 72:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 39` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpb_03_testdef","comparisonType":"Equal"}}}` | 0:Out → 39:In; 39:True → 4:Active; 39:False → 40:Active |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 52` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"$/03_night_city/c_westbrook/japan_town/japan_town_drop_points_prefab7T6EPDI/drop_point_004_prefabOAR44JI","deviceControllerClass":"DropPointControllerPS","deviceConditionFunction":"IsRewardCollected"}}}` | 51:Out → 52:In; 52:Out → 82:Succeeded |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#jpn_03_tr_sts_area_trigger_001"}}` | 41:Out → 56:In; 59:Out → 56:In; 56:Out → 58:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 57` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#jpn_03_tr_sts_area_trigger_001"}}` | 58:Out → 57:In; 57:Out → 59:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 71` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 71:Out → 70:Active; 73:Out → 71:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 74` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 74:False → 41:Active; 74:True → 64:Start 0; 98:False → 74:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 87` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 95:Out → 87:In; 87:Out → 100:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 90` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 94:Out → 90:In; 90:Out → 102:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 92` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\japantown\\sts_wbr_jpn_03\\scenes\\sts_wbr_jpn_03_holocall_debrief.scene","Flags":"Soft"},"type":"IsOutside"}},{"$type":"questSceneCondition","type":{"$type":"questSceneNode_ConditionType","sceneFile":{"DepotPath":"base\\open_world\\street_stories\\westbrook\\japantown\\sts_wbr_jpn_03\\scenes\\sts_wbr_jpn_03_holocall_prebrief.scene","Flags":"Soft"},"type":"IsOutside"}}]}}` | 92:Out → 69:In; 93:Out → 92:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 49:Out → 93:In; 68:Out → 93:In; 93:Out → 92:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 98` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 0:Out → 98:In; 98:True → 41:Active; 98:False → 74:In |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 100` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 100:False → 66:Start 0; 87:Out → 100:In; 100:True → 99:Active |
| `sts_wbr_jpn_03_streetstory.questphase / h158 / 102` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questPhoneMuted_ConditionType","groupName":"fixer_briefs_and_debriefs"}}}` | 102:False → 65:Start 0; 90:Out → 102:In; 102:True → 101:Active |
| `sts_wbr_jpn_03_streetstory.questphase / h687 / 25` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#jpn_03_tr_sts_area_trigger_001"}}` | 25:Out → 17:In; 26:Out → 25:In |
| `sts_wbr_jpn_03_streetstory.questphase / h687 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","hours":3}}}` | 26:Out → 25:In; 28:Out → 26:In |
| `sts_wbr_jpn_03_holocall_debrief.scene / scene / 31` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_03_stealth_fail"}}}` | 31:0:0 → 28:0:0; 31:0:1 → 27:0:0; 73:0:0 → 31:0:1 |
| `sts_wbr_jpn_03_holocall_debrief.scene / scene / 71` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_end_done"}}}` | 71:0:0 → 72:0:1; 76:0:0 → 71:0:1 |
| `sts_wbr_jpn_03_holocall_debrief.scene / scene / 249` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_done"}}}` | 69:666:0 → 249:0:1; 249:0:0 → 271:0:0 |
| `sts_wbr_jpn_03_holocall_debrief.scene / scene / 252` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":200}}}` | 69:666:0 → 252:0:1; 252:0:0 → 254:0:1; 262:0:0 → 252:0:1; 271:1:0 → 252:0:0; 271:1:0 → 252:1026:0 |
| `sts_wbr_jpn_03_holocall_debrief.scene / scene / 254` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_activate","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 252:0:0 → 254:0:1; 254:0:0 → 256:0:1; 271:1:0 → 254:0:0; 271:1:0 → 254:1026:0 |
| `sts_wbr_jpn_03_holocall_debrief.scene / scene / 256` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2,"miliseconds":200}}}` | 254:0:0 → 256:0:1; 256:0:0 → 258:0:1; 271:1:0 → 256:0:0; 271:1:0 → 256:1026:0 |
| `sts_wbr_jpn_03_holocall_debrief.scene / scene / 258` | `questConditionNodeDefinition` `{"condition":{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}}` | 256:0:0 → 258:0:1; 258:0:0 → 260:0:1; 258:0:1 → 262:0:0 |
| `sts_wbr_jpn_03_holocall_debrief.scene / scene / 283` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_rejected"}}}` | 1:0:0 → 283:0:1; 283:0:0 → 281:0:1 |
| `sts_wbr_jpn_03_holocall_prebrief.scene / scene / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_end_done"}}}` | 68:0:0 → 69:0:1; 71:0:0 → 68:0:1 |
| `sts_wbr_jpn_03_holocall_prebrief.scene / scene / 258` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_rejected"}}}` | 62:0:0 → 258:0:1; 258:0:0 → 256:0:1 |
| `sts_wbr_jpn_03_holocall_prebrief.scene / scene / 267` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_wakako_calls_v_start_done"}}}` | 59:666:0 → 267:0:1; 267:0:0 → 269:0:0 |
| `sts_wbr_jpn_03_holocall_prebrief.scene / scene / 273` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":30}}}` | 59:666:0 → 273:0:1; 269:1:0 → 273:0:0; 273:0:0 → 279:0:1 |
| `sts_wbr_jpn_03_holocall_prebrief.scene / scene / 279` | `questConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_active","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_setup_started","value":1,"comparisonType":"Less"}},{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"holo_active_call_interrupted","value":1,"comparisonType":"Less"}},{"$type":"questContentCondition","type":{"$type":"questContentLock_ConditionType"}}]}}` | 273:0:0 → 279:0:1; 279:0:0 → 285:0:1; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `sts_wbr_jpn_03_holocall_prebrief.scene / scene / 281` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":5}}}` | 269:1:0 → 281:0:0; 279:0:1 → 281:0:1; 281:0:0 → 279:0:1 |
| `open_world_bugfixing.questphase / h674 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_03_finished"}}}` | 0:Out → 13:In; 13:True → 14:Succeeded |
| `open_world_bugfixing.questphase / h1792 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"jpn_03_finished"}}}` | 0:Out → 13:In; 13:True → 14:Succeeded |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `checkpoint` | sts_wbr_jpn_03_streetstory.questphase / h687 / 15; sts_wbr_jpn_03_streetstory.questphase / h7 / 8 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `community_lifecycle` | sts_wbr_jpn_03_streetstory.questphase / h687 / 2; sts_wbr_jpn_03_streetstory.questphase / h687 / 7; sts_wbr_jpn_03_streetstory.questphase / h7 / 4 | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | open_world_bugfixing.questphase / h1792 / 13; open_world_bugfixing.questphase / h674 / 13; sts_wbr_japantown.questphase / h11912 / 20; sts_wbr_japantown.questphase / h11912 / 29; +13 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | sts_wbr_japantown.questphase / h11912 / 72; sts_wbr_japantown.questphase / h11912 / 83; sts_wbr_jpn_03_streetstory.questphase / h158 / 58; sts_wbr_jpn_03_streetstory.questphase / h158 / 59; +5 locations in catalogue.json | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | sts_wbr_japantown.questphase / h11912 / 51; sts_wbr_japantown.questphase / h11912 / 54; sts_wbr_jpn_03_streetstory.questphase / h158 / 51; sts_wbr_jpn_03_streetstory.questphase / h158 / 53; +14 locations in catalogue.json | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | sts_wbr_japantown.questphase / h11912 / 46; sts_wbr_jpn_03_streetstory.questphase / h158 / 45; sts_wbr_jpn_03_streetstory.questphase / h158 / 46; sts_wbr_jpn_03_streetstory.questphase / h687 / 10; +14 locations in catalogue.json | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | sts_wbr_japantown.questphase / h11912 / 3; sts_wbr_japantown.questphase / h11912 / 52; sts_wbr_jpn_03_streetstory.questphase / h158 / 3; sts_wbr_jpn_03_streetstory.questphase / h158 / 52 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | sts_wbr_jpn_03_streetstory.questphase / h687 / 26 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | open_world_bugfixing.questphase / h1792 / 14; open_world_bugfixing.questphase / h674 / 14; sts_wbr_japantown.questphase / h11912 / 10; sts_wbr_japantown.questphase / h11912 / 13; +37 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `persistent_decision` | sts_wbr_jpn_03_holocall_debrief.scene / scene / 260; sts_wbr_jpn_03_holocall_debrief.scene / scene / 279; sts_wbr_jpn_03_holocall_debrief.scene / scene / 281; sts_wbr_jpn_03_holocall_debrief.scene / scene / 70; +20 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | sts_wbr_japantown.questphase / h11912 / 93; sts_wbr_jpn_03_holocall_debrief.scene / scene / 252; sts_wbr_jpn_03_holocall_debrief.scene / scene / 256; sts_wbr_jpn_03_holocall_prebrief.scene / scene / 273; +5 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | sts_wbr_jpn_03_streetstory.questphase / h158 / 67; sts_wbr_jpn_03_streetstory.questphase / h158 / 68 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | sts_wbr_jpn_03_streetstory.questphase / h158 / 64; sts_wbr_jpn_03_streetstory.questphase / h158 / 65; sts_wbr_jpn_03_streetstory.questphase / h158 / 66 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | sts_wbr_japantown.questphase / h11912 / 17; sts_wbr_japantown.questphase / h11912 / 6; sts_wbr_jpn_03_streetstory.questphase / h158 / 17; sts_wbr_jpn_03_streetstory.questphase / h158 / 56; +4 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `world_variant` | sts_wbr_jpn_03_streetstory.questphase / h7 / 11 | prefab + variant + desired state + restore policy → world presentation changed. Resolve world ownership and restore only this quest's overrides. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` | content candidate; journal anchor | `base-sts-wbr-jpn-03` |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` | content candidate; forward dependency | `base-sts-wbr-jpn-03` |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene` | content candidate; forward dependency | `base-sts-wbr-jpn-03` |
| `base\quest\bugfixing\open_world_bugfixing.questphase` | repair; journal anchor | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-sts-wbr-jpn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-wbr-jpn-03.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

144 repeated typed/socket path signatures in this selected graph context; 29 distinct direct resource identities; 3 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 76 -> 71 -> 72 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `fee3756653cd083fb28e` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h687 / 28 -> 26 -> 25 | questDeletionMarkerNodeDefinition -> questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `1d933adb5a617880c93e` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 74 -> 76 -> 71 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `d6b7c21f5d2d0ab76fc6` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 283 -> 281 -> 285 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `26762f051e7728f090ca` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene` / scene / 60 -> 61 -> 26 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `101b60945ddf6f25f378` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 27 -> 74 -> 76 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |
| `9e5e28ecb38ea2a53a15` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene` / scene / 254 -> 62 -> 258 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `2beeeaa3b4da5300c035` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 1 -> 279 -> 75 | scnStartNode[scnNodeId] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:1; 0:0 -> 0:1 |
| `4e9253a72e6b0134b8dd` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase` / h11912 / 17 -> 18 -> 62 | questPauseConditionNodeDefinition[questTriggerCondition] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Succeeded; Out -> Active |
| `bbf9efd740881cf31a37` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` / scene / 249 -> 271 -> 252 | questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnCutControlNode[scnNodeId] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; 0:0 -> 0:0; 1:0 -> 0:0 |
| `d5cbf4acf851cb8612b3` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene` / scene / 285 -> 283 -> 260 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `fe9d2c1bdd2cebf30eb2` | `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene` / scene / 61 -> 26 -> 70 | scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]; 0:0 -> 0:0; 0:0 -> 0:0 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h0 / 2 | `h7` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h0 / 3 | `h158` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":69,"socketName":"Out1"}] |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` / h0 / 11 | `h687` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |

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
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02_test.gamedef` | content candidate | base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\sts_hey_rey_02.quest |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\sts_wbr_jpn_03_gamedef.gamedef` | content candidate | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\sts_wbr_jpn_03.quest |
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
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\phases\sts_hey_rey_09_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01b_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_01\phases\sts_wbr_jpn_01b_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_02\phases\sts_wbr_jpn_02_streetstory.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_streetstory.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\lipsync\en\sts_wbr_jpn_03_holocall_debrief\wakako_okada.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\lipsync\en\sts_wbr_jpn_03_holocall_prebrief\wakako_okada.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\phases\sts_wbr_jpn_05_gameplay.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\phases\sts_wbr_jpn_05_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\phases\sts_wbr_jpn_05_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_main_phase.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12a.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\phases\sts_wbr_jpn_12b_openworld.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `holo_active_call_interrupted` | base\quest\holocalls\holocall_interrupts.questphase / h0 / 100; base\quest\holocalls\holocall_interrupts.questphase / h0 / 104; base\quest\holocalls\holocall_interrupts.questphase / h0 / 115; base\quest\holocalls\holocall_interrupts.questphase / h0 / 118; 4 total source locations in compressed evidence |
| `holo_setup_active` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 135; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 138; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 45; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 46; 972 total source locations in compressed evidence |
| `holo_setup_started` | base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 136; base\quest\minor_quests\mq018\phases\mq018_01_msgs.questphase / h0 / 139; base\quest\bugfixing\part1\q112\q112_quest_bugfixes.questphase / h566 / 8; base\cinematics\scene_blocks\sb_holocall_initializer.scene / scene / 56; 469 total source locations in compressed evidence |
| `holo_wakako_calls_v_end_activate` | base\open_world\fixers\wakako\phases\wakako.questphase / h0 / 63; base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 903; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h1654 / 199; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h2858 / 27; 60 total source locations in compressed evidence |
| `holo_wakako_calls_v_end_done` | base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 895; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 293; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 42; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 528; 26 total source locations in compressed evidence |
| `holo_wakako_calls_v_rejectable` | base\quest\holocalls\wakako\wakako_holocall.scene / scene / 629; base\quest\side_quests\sq023\scenes\sq023_03_call.scene / scene / 1206; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_debriefs.scene / scene / 288; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_prebrief.scene / scene / 254; 25 total source locations in compressed evidence |
| `holo_wakako_calls_v_rejected` | base\quest\holocalls\wakako\wakako_holocall.scene / scene / 637; base\quest\side_quests\sq023\scenes\sq023_03_call.scene / scene / 1214; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_debriefs.scene / scene / 290; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_09\scenes\sts_hey_rey_09_holocall_prebrief.scene / scene / 256; 17 total source locations in compressed evidence |
| `holo_wakako_calls_v_start_activate` | base\open_world\fixers\wakako\phases\wakako.questphase / h0 / 62; base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 901; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h1654 / 198; base\open_world\street_stories\heywood\vista_del_rey\sts_hey_vista_del_rey.questphase / h2858 / 26; 74 total source locations in compressed evidence |
| `holo_wakako_calls_v_start_done` | base\open_world\fixers\wakako\scenes\wakako_okada_default.scene / scene / 891; base\quest\bugfixing\additional_content\holocall_bugfixing.questphase / h121 / 292; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 41; base\quest\holocalls\wakako\wakako_holocall.scene / scene / 575; 25 total source locations in compressed evidence |
| `jpb_03_testdef` | base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\sts_wbr_jpn_03.quest / h0 / 5; 1 total source locations in compressed evidence |
| `jpn_03_finished` | base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase / h12441 / 14; 1 total source locations in compressed evidence |
| `jpn_03_start` | base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase / h11761 / 7; 1 total source locations in compressed evidence |
| `jpn_03_stealth_fail` | base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase / h4999 / 11; base\open_world\street_stories\westbrook\japantown\sts_wbr_japantown.questphase / h5228 / 5; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_combat.questphase / h43 / 11; base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\phase\sts_wbr_jpn_03_combat.questphase / h272 / 5; 4 total source locations in compressed evidence |
| `wbr_achievement` | base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_01\ma_wbr_hil_01.questphase / h0 / 40; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_02\ma_wbr_hil_02_phase.questphase / h0 / 68; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_03\ma_wbr_hil_03_phase.questphase / h0 / 51; base\open_world\minor_activities\westbrook\charter_hill\ma_wbr_hil_04\ma_wbr_hil_04_phase.questphase / h0 / 60; 39 total source locations in compressed evidence |

NodeRef uses: 78; TweakDB binding uses: 5. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene` | 2 / 4 | scnDialogLineEvent: 4 |
| `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene` | 1 / 1 | scnDialogLineEvent: 1 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
