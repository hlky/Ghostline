# Sacrum Profanum

Journal: `quests/minor_quest/mq032_sacrum` · `MinorQuest` · hash `1306283341`.

Journal premise: You know, you could deal with our problems first, 'stead of helping every gonk that comes your way. But, well, since you're so hell-bent on saving that monk in distress, delta your ass over to the warehouse. Maybe you can still save him before they slice him. Kinda curious how you'll do it, actually. Gonna go all tree-hugging pacifist, or you gonna just get the job done?

**Coverage: journal-linked.** 22 exact journal-linked nodes in 4 resources; 7 resources in the inspected dependency context.

Resource roles in that context: 7 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: `base\open_world\mini_world_stories\watson\mws_thenerves\mws_thenerves.quest`. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| You know, you could deal with our problems first, 'stead of helping every gonk that comes your way. But, well, since you're so hell-bent on saving that monk in distress, delta your ass over to the warehouse. Maybe you can still save him before they slice him. Kinda curious how you'll do it, actually. Gonna go all tree-hugging pacifist, or you gonna just get the job done? (Primary) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook` |
| Defeat the gangoons. (Primary) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/02_maelstrom` |
| Talk to the monk. (Primary) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk` |
| Take Maelstrom's gear. (Primary) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/04_loot` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `watson_mini_world_stories.questphase / h0 / 108` (PauseCondition) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk`; `quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk`; `quests/minor_quest/mq032_sacrum/mq032_sacrum` | 78:Out → 108:In; 82:Out → 108:In; 108:Out → 98:In |
| `watson_mini_world_stories.questphase / h0 / 113` (PauseCondition) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk`; `quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk`; `quests/minor_quest/mq032_sacrum/mq032_sacrum` | 103:Out → 113:In; 113:Out → 114:In |
| `mq032_01_hook.questphase / h0 / 4` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook` | 23:Out → 4:Active; 22:False → 4:Active; 4:Out → 24:In |
| `mq032_01_hook.questphase / h0 / 10` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook/description` | 24:False → 10:Active; 10:Out → 15:In |
| `mq032_01_hook.questphase / h0 / 19` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook/description_johnny` | 19:Out → 15:In; 24:True → 19:Active |
| `mq032_01_hook.questphase / h0 / 23` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_alternative_title` | 23:Out → 4:Active; 22:True → 23:Active |
| `mq032_02_maelstrom.questphase / h0 / 9` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook` | 13:True → 9:Inactive; 9:Out → 12:Active; 9:Out → 127:In |
| `mq032_02_maelstrom.questphase / h0 / 12` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/02_maelstrom` | 9:Out → 12:Active; 72:Out → 12:Active; 12:Out → 43:In1; 12:Out → 80:In |
| `mq032_02_maelstrom.questphase / h0 / 14` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/02_maelstrom` | 27:Out → 14:Succeeded; 14:Out → 17:Active |
| `mq032_02_maelstrom.questphase / h0 / 17` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk` | 14:Out → 17:Active; 17:Out → 59:In |
| `mq032_02_maelstrom.questphase / h0 / 31` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook` | 36:Out1 → 31:Failed; 31:Out → 32:Failed |
| `mq032_02_maelstrom.questphase / h0 / 32` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/02_maelstrom` | 31:Out → 32:Failed; 32:Out → 33:Failed |
| `mq032_02_maelstrom.questphase / h0 / 33` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk` | 32:Out → 33:Failed; 33:Out → 40:Failed |
| `mq032_02_maelstrom.questphase / h0 / 40` (Journal) | `quests/minor_quest/mq032_sacrum` | 40:Out → 24:In; 33:Out → 40:Failed; 40:Out → 97:In |
| `mq032_02_maelstrom.questphase / h0 / 72` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook` | 72:Out → 12:Active; 83:Out → 72:Inactive; 81:Out → 72:Inactive; 72:Out → 127:In |
| `mq032_02_maelstrom.questphase / h0 / 81` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook/description` | 81:Out → 72:Inactive; 82:False → 81:Active |
| `mq032_02_maelstrom.questphase / h0 / 83` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook/description_johnny` | 83:Out → 72:Inactive; 107:Out → 83:Active |
| `mq032_02_maelstrom.questphase / h0 / 107` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_alternative_title` | 82:True → 107:Active; 107:Out → 83:Active |
| `mq032_02_maelstrom.questphase / h0 / 128` (Journal) | `quests/minor_quest/mq032_sacrum/description_johnny` | 127:True → 128:Active |
| `mq032_02_maelstrom.questphase / h0 / 131` (Journal) | `quests/minor_quest/mq032_sacrum/description` | 127:False → 131:Active |
| `mq032_02_maelstrom.scene / scene / 235` (Journal) | `quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk` | 51:0:0 → 235:0:3; 54:0:0 → 235:0:3; 57:0:0 → 235:0:3; 85:0:1 → 235:0:3; 235:0:0 → 236:0:3; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |
| `mq032_02_maelstrom.scene / scene / 236` (Journal) | `quests/minor_quest/mq032_sacrum` | 235:0:0 → 236:0:3; 236:0:0 → 463:0:1; input mappings: 0:0=CutDestination, 0:1=Active, 0:2=Inactive, 0:3=Succeeded, 0:4=Failed |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `mq032_01_hook.questphase / h0 / 3` | `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene`; `#mq032_01_sm_hook` | 2:Out → 3:mq032_01_hook_in; 3:mq032_01_hook_out → 32:In; 3:Cleanup → 17:In |
| `mq032_02_maelstrom.questphase / h0 / 4` | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene`; `#mq032_02_sm_maelstrom` | 6:CutSource → 4:CutDestination; 92:Out1 → 4:mq032_02_maelstrom_in; 4:mq032_02_maelstrom_out → 53:In2 |
| `mq032_02_maelstrom.questphase / h0 / 5` | `base\quest\minor_quests\mq032\phases\mq032_combat.questphase` | 0:Out → 5:In1; 5:stopscene → 6:In |
| `mq032_02_maelstrom.questphase / h0 / 7` | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene`; `#mq032_02_sm_maelstrom` | 6:Out → 7:mq032_02_maelstrom_attack_in |
| `mq032_02_maelstrom.questphase / h0 / 18` | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene`; `#mq032_02_sm_maelstrom` | 70:CutSource → 18:CutDestination; 125:Out → 18:mq032_02_saved_in; 18:mq032_02_saved_out → 78:In; 18:mq032_02_saved_out → 91:In; 18:mq032_02_saved_out → 126:In |
| `mq032_02_maelstrom.questphase / h0 / 29` | `base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene`; `#mq032_03_sm_epilogue` | 21:Out → 29:mq032_03_monk_cyberware_in; 70:CutSource → 29:CutDestination; 104:CutSource → 29:CutDestination |
| `mq032_02_maelstrom.questphase / h0 / 44` | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene`; `#mq032_02_sm_maelstrom` | 44:mq032_02_killed_out → 36:In2; 69:Out → 44:mq032_02_killed_in |
| `mq032_02_maelstrom.questphase / h0 / 62` | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene`; `#mq032_02_sm_maelstrom` | 6:CutSource → 62:CutDestination; 96:Out1 → 62:mq032_02_maelstrom_fluff_in |
| `mq032_02_maelstrom.questphase / h0 / 67` | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene`; `#mq032_02_sm_maelstrom` | 92:Out1 → 67:mq032_monk_animations_in |
| `mq032_02_maelstrom.questphase / h0 / 105` | `base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene`; `#mq032_03_sm_epilogue` | 70:CutSource → 105:CutDestination; 104:Out → 105:mq032_03_monk_cyberware_in |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\mini_world_stories\ow_mini_world_stories.questphase` / h0 / 7 | `watson_mini_world_stories.questphase` | 13: LogicalHub; 13:Out1 → 7:In1 |
| `base\quest\minor_quests\mq032\mq032_sacrum.questphase` / h0 / 32 | `mq032_01_hook.questphase` | 40: PauseCondition: #mq032_tr_leave; 40:Out → 32:In1; 32:Out1 → 33:hook_done |
| `base\quest\minor_quests\mq032\mq032_sacrum.questphase` / h0 / 33 | `mq032_02_maelstrom.questphase` | 32: Phase: mq032_01_hook.questphase; 40: PauseCondition: #mq032_tr_leave; 32:Out1 → 33:hook_done; 33:Success → 34:Success; 40:Out → 33:In1; 33:Fail → 34:Fail |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 5 | `mq032_combat.questphase` | 0: Input; 0:Out → 5:In1; 5:stopscene → 6:In |
| `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` / h0 / 3 | `mq032_01_hook.scene` | 2: PauseCondition: #mq032_tr_hook; 2:Out → 3:mq032_01_hook_in; 3:mq032_01_hook_out → 32:In; 3:Cleanup → 17:In |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 4 | `mq032_02_maelstrom.scene` | 6: CutControl; 92: LogicalXor; 6:CutSource → 4:CutDestination; 92:Out1 → 4:mq032_02_maelstrom_in; 4:mq032_02_maelstrom_out → 53:In2 |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 7 | `mq032_02_maelstrom.scene` | 6: CutControl; 6:Out → 7:mq032_02_maelstrom_attack_in |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 18 | `mq032_02_maelstrom.scene` | 70: CutControl; 125: Audio; 70:CutSource → 18:CutDestination; 125:Out → 18:mq032_02_saved_in; 18:mq032_02_saved_out → 78:In; 18:mq032_02_saved_out → 91:In; 18:mq032_02_saved_out → 126:In |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 44 | `mq032_02_maelstrom.scene` | 69: SceneManager; 44:mq032_02_killed_out → 36:In2; 69:Out → 44:mq032_02_killed_in |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 62 | `mq032_02_maelstrom.scene` | 6: CutControl; 96: LogicalXor; 6:CutSource → 62:CutDestination; 96:Out1 → 62:mq032_02_maelstrom_fluff_in |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 67 | `mq032_02_maelstrom.scene` | 92: LogicalXor; 92:Out1 → 67:mq032_monk_animations_in |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 29 | `mq032_03_epilogue.scene` | 21: Input; 70: CutControl; 104: CutControl; 21:Out → 29:mq032_03_monk_cyberware_in; 70:CutSource → 29:CutDestination; 104:CutSource → 29:CutDestination |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 105 | `mq032_03_epilogue.scene` | 70: CutControl; 104: CutControl; 70:CutSource → 105:CutDestination; 104:Out → 105:mq032_03_monk_cyberware_in |
| `base\quest\minor_quests\mq032\phases\mq032_03_epilogue.questphase` / h0 / 9 | `mq032_03_epilogue.scene` | 8: PauseCondition: #mq032_tr_hook; 35: CutControl; 8:Out → 9:mq032_03_dead_in; 35:CutSource → 9:CutDestination; 9:mq032_03_dead_out → 10:In |
| `base\quest\minor_quests\mq032\phases\mq032_03_epilogue.questphase` / h0 / 13 | `mq032_03_epilogue.scene` | 7: PauseCondition: #mq032_tr_monk_epilogue; 7:Out → 13:mq032_03_fail_in; 13:mq032_03_fail_out → 20:In |
| `base\quest\minor_quests\mq032\phases\mq032_03_epilogue.questphase` / h0 / 15 | `mq032_03_epilogue.scene` | 14: PauseCondition: #mq032_tr_monk_epilogue; 14:Out → 15:mq032_03_success_in; 15:mq032_03_success_out → 19:In |
| `base\open_world\phases\open_world_content.questphase` / h0 / 93 | `ow_mini_world_stories.questphase` | 92: DeletionMarker; 92:Out → 93:In1; 93:SignalPickup → 101:In |
| `base\quest\minor_quests\minorquests.questphase` / h0 / 4 | `mq032_sacrum.questphase` | 84: LogicalHub; 84:Out1 → 4:In1 |
| `base\quest\minor_quests\mq032\mq032_sacrum.quest` / h0 / 7 | `mq032_sacrum.questphase` | 18: RenderFxManager; 17: RenderFxManager; 19: RenderFxManager; 7:Out1 → 1:In; 18:Out → 7:nonlethal; 17:Out → 7:In1; 19:Out → 7:lethal |
| `base\quest\minor_quests\mq032\mq032_sacrum.questphase` / h0 / 34 | `mq032_03_epilogue.questphase` | 33: Phase: mq032_02_maelstrom.questphase; 33: Phase: mq032_02_maelstrom.questphase; 43: Input; 44: Input; 34:Out1 → 1:In; 33:Success → 34:Success; 33:Fail → 34:Fail; 43:Out → 34:Success; 44:Out → 34:Fail |
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
| `base\quest\cyberpunk2077.questphase` / h520 / 6 | `minorquests.questphase` | 4: Phase: bugfixing.questphase; 7: LogicalHub; 8: PauseCondition: chicken_test_enable_sidecontent; 21: FactsDBManager: ep1_standalone_bugfix_start; 4:to_mq025 → 6:to_mq025; 7:Out1 → 6:In1; 8:Out → 6:In1; 21:Out → 6:EP1_Standalone |
| `base\quest\demos\handson_2020\handson_2020_kabuki.quest` / h0 / 8 | `minorquests.questphase` | 0: Start; 0:Out → 8:In1 |
| `base\quest\demos\handson_2020\handson_2020_little_china.quest` / h0 / 7 | `minorquests.questphase` | 1: Start; 1:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_northside_industrial_district.quest` / h0 / 7 | `minorquests.questphase` | 0: Start; 0:Out → 7:In1 |
| `base\quest\demos\handson_2020\handson_2020_scavengers.quest` / h0 / 32 | `minorquests.questphase` | 25: LogicalHub; 25:Out1 → 32:In1 |
| `base\quest\demos\handson_2020\handson_2020_speed_test.quest` / h0 / 5 | `minorquests.questphase` | 0: Start; 0:Out → 5:In1 |
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
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `mq032_01_hook.scene` | mq032_01_hook_in, mq032_fuck_test_in → Cleanup, mq032_01_hook_out | Cyberware_Monk; Johnny; V; 78 nodes / 88 edges |
| `mq032_02_maelstrom.scene` | mq032_02_maelstrom_in, mq032_02_maelstrom_attack_in, mq032_02_saved_in, Start 8, mq032_02_killed_in, mq032_02_maelstrom_fluff_in, mq032_monk_animations_in, Start 9, mq032_02_lethal_01_CLONE_in, Start 10 → mq032_02_maelstrom_out, mq032_02_maelstrom_attack_out, mq032_02_saved_out, mq032_02_killed_out, mq032_02_maelstrom_fluff_end, mq032_02_lethal_01_CLONE_out, mq032_02_cleanup_out | Brother; Maelstrom_01; Maelstrom_02; Maelstrom_08; Johnny; V; 111 nodes / 139 edges |
| `mq032_03_epilogue.scene` | mq032_03_success_in, mq032_03_monk_cyberware_in, mq032_03_dead_in, mq032_03_fail_in, Start 4 → mq032_03_monk_cyberware_out, mq032_03_success_out, mq032_03_dead_out, mq032_03_fail_out | Monk_Cyberware; Monk_Brother; Johnny; V; 43 nodes / 47 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `mq032_01_hook.scene / n6 / 0` | What happened? (`What`) | No option-level predicate stored | 0:0 → 8:0:0 |
| `mq032_01_hook.scene / n6 / 1` | A monk with implants? (`Option`) | No option-level predicate stored | 0:1 → 46:0:0 |
| `mq032_01_hook.scene / n10 / 0` | Where's your brother now? (`Brother`) | No option-level predicate stored | 0:0 → 15:0:0 |
| `mq032_01_hook.scene / n10 / 1` | Why'd they do it? (`Why`) | No option-level predicate stored | 0:1 → 12:0:0 |
| `mq032_01_hook.scene / n17 / 0` | I'm here to help. (`Help`) | No option-level predicate stored | 0:0 → 30:0:0 |
| `mq032_01_hook.scene / n17 / 1` | Gonna kill those assholes. (`Option_01`) | No option-level predicate stored | 0:1 → 53:0:0 |
| `mq032_01_hook.scene / n17 / 2` | I'd rather not get involved. (`Sorry`) | No option-level predicate stored | 0:2 → 22:0:0 |
| `mq032_01_hook.scene / n17 / 3` | What's in it for me? (`Reward`) | {"bluelineCondition": {"$type": "questStatsCondition", "type": {"$type": "questBuild_ConditionType", "entityRef": {"$type": "questUniversalRef"}, "scriptCondition": {"$type": "Build_ScriptConditionType", "questAssignment": "127566586744", "buildId": "74910219395", "difficulty": "EASY", "comparisonType": "CO_GreaterEq"}}}} | 0:3 → 19:0:0 |
| `mq032_01_hook.scene / n26 / 0` | All right, I'll help. (`Help`) | No option-level predicate stored | 0:0 → 28:0:0 |
| `mq032_01_hook.scene / n134 / 0` | [Show middle finger] (`Fuck`) | No option-level predicate stored | 0:0 → 136:0:0 |
| `mq032_02_maelstrom.scene / n24 / 0` | Heard you call out for help. (``) | {"questCondition": {"$type": "questLogicalCondition", "conditions": [{"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq032_help", "comparisonType": "Equal"}}, {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq032_no_help", "comparisonType": "Equal"}}]}} | 0:0 → 26:0:0 |
| `mq032_02_maelstrom.scene / n24 / 1` | Your brother sent me. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq032_help"}}} | 0:1 → 28:0:0 |
| `mq032_02_maelstrom.scene / n24 / 2` | You can thank your brother. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq032_no_help"}}} | 0:2 → 30:0:0 |
| `mq032_02_maelstrom.scene / n24 / 3` | First, I wanna make sure you're OK. (``) | No option-level predicate stored | 0:3 → 102:0:0 |
| `mq032_02_maelstrom.scene / n39 / 0` | Your brother's waiting for you. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq032_help"}}} | 0:0 → 51:0:0 |
| `mq032_02_maelstrom.scene / n39 / 1` | Don't I get a "Thank you?" (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq032_nonlethal", "comparisonType": "Equal"}}} | 0:1 → 54:0:0 |
| `mq032_02_maelstrom.scene / n39 / 2` | I didn't really have a choice. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq032_nonlethal", "comparisonType": "Equal"}}} | 0:2 → 57:0:0 |
| `mq032_02_maelstrom.scene / n39 / 3` | How did you get taken by Maelstrom? (``) | No option-level predicate stored | 0:3 → 94:0:0 |
| `mq032_02_maelstrom.scene / n219 / 0` | It's OK, you're safe. (``) | No option-level predicate stored | 0:0 → 18:0:0 |
| `mq032_02_maelstrom.scene / n293 / 0` | Your brother's waiting. (``) | No option-level predicate stored | 0:0 → 296:0:0 |
| `mq032_02_maelstrom.scene / n320 / 0` | What was I supposed to do? (``) | No option-level predicate stored | 0:0 → 297:0:0 |
| `mq032_03_epilogue.scene / n7 / 0` | He's safe and sound. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq032_saved"}}} | 0:0 → 9:0:0 |
| `mq032_03_epilogue.scene / n7 / 1` | Not yet. (``) | {"questCondition": {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq032_saved", "comparisonType": "Equal"}}} | 0:1 → 20:0:0 |
| `mq032_03_epilogue.scene / n27 / 0` | He's dead. (``) | No option-level predicate stored | 0:0 → 29:0:0 |
| `mq032_03_epilogue.scene / n27 / 1` | I accidentally killed him. (``) | No option-level predicate stored | 0:1 → 30:0:0 |
| `mq032_03_epilogue.scene / n54 / 0` | Thoughts on constructs? (``) | No option-level predicate stored | 0:0 → 56:0:0 |
| `mq032_03_epilogue.scene / n54 / 1` | Good luck. (``) | No option-level predicate stored | 0:1 → 58:0:0 |
| `mq032_03_epilogue.scene / n61 / 0` | Thanks. (``) | No option-level predicate stored | 0:0 → 74:0:0 |
| `mq032_03_epilogue.scene / n61 / 1` | Is a copy of a person still a person? (``) | No option-level predicate stored | 0:1 → 63:0:0 |
| `mq032_03_epilogue.scene / n61 / 2` | Digitization of people – that sit right with you? (``) | No option-level predicate stored | 0:2 → 65:0:0 |
| `mq032_03_epilogue.scene / n61 / 3` | What's your take, Johnny? (``) | {"questCondition": {"$type": "questLogicalCondition", "conditions": [{"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq032_03_02_Human", "value": 1, "comparisonType": "GreaterOrEqual"}}, {"$type": "questFactsDBCondition", "type": {"$type": "questVarComparison_ConditionType", "factName": "mq032_03_01_Copy", "value": 1, "comparisonType": "GreaterOrEqual"}}]}} | 0:3 → 77:0:0 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `cutfornow` | Producer outside selected context | mq032_02_maelstrom.scene / scene / 304 |
| `mq032_01_whatIgnorance` | mq032_01_hook.scene / scene / 56 | mq032_02_maelstrom.scene / scene / 105 |
| `mq032_03_01_Copy` | mq032_03_epilogue.scene / scene / 79 | mq032_03_epilogue.scene / scene / 61 |
| `mq032_03_02_Human` | mq032_03_epilogue.scene / scene / 82 | mq032_03_epilogue.scene / scene / 61 |
| `mq032_dead` | mq032_02_maelstrom.questphase / h0 / 37 | mq032_02_maelstrom.scene / scene / 471 |
| `mq032_help` | mq032_01_hook.questphase / h0 / 5 | mq032_02_maelstrom.questphase / h0 / 13; mq032_02_maelstrom.scene / scene / 24; mq032_02_maelstrom.scene / scene / 39; mq032_02_maelstrom.scene / scene / 6; mq032_02_maelstrom.scene / scene / 85 |
| `mq032_monk1_met` | mq032_01_hook.scene / scene / 62 | mq032_01_hook.questphase / h221 / 6; mq032_02_maelstrom.scene / scene / 114 |
| `mq032_monk_get_up` | mq032_02_maelstrom.scene / scene / 191 | mq032_02_maelstrom.scene / scene / 197 |
| `mq032_no_help` | mq032_01_hook.scene / scene / 36; mq032_01_hook.scene / scene / 39 | mq032_02_maelstrom.scene / scene / 24 |
| `mq032_nonlethal` | mq032_02_maelstrom.questphase / h0 / 16; mq032_02_maelstrom.questphase / h0 / 65 | mq032_02_maelstrom.scene / scene / 20; mq032_02_maelstrom.scene / scene / 298; mq032_02_maelstrom.scene / scene / 39; mq032_02_maelstrom.scene / scene / 73; mq032_02_maelstrom.scene / scene / 86; mq032_03_epilogue.scene / scene / 48 |
| `mq032_saved` | mq032_02_maelstrom.questphase / h0 / 27 | mq032_03_epilogue.scene / scene / 7 |
| `mq032_stop_idle_gestures` | mq032_01_hook.scene / scene / 208 | mq032_01_hook.scene / scene / 327; mq032_01_hook.scene / scene / 330; mq032_01_hook.scene / scene / 335; mq032_01_hook.scene / scene / 339; mq032_01_hook.scene / scene / 345; mq032_01_hook.scene / scene / 349; mq032_01_hook.scene / scene / 353; mq032_01_hook.scene / scene / 357; mq032_01_hook.scene / scene / 365; mq032_01_hook.scene / scene / 369; mq032_01_hook.scene / scene / 389 |
| `mq032_test_def` | Producer outside selected context | mq032_02_maelstrom.questphase / h0 / 78 |
| `playerHasGone` | mq032_02_maelstrom.scene / scene / 511 | No reader in selected context |
| `q101_enable_side_content` | Producer outside selected context | mq032_01_hook.questphase / h0 / 22; mq032_01_hook.questphase / h0 / 24; mq032_01_hook.scene / scene / 229; mq032_01_hook.scene / scene / 82; mq032_02_maelstrom.questphase / h0 / 127; mq032_02_maelstrom.questphase / h0 / 82; mq032_02_maelstrom.scene / scene / 144 |
| `q306_active` | Producer outside selected context | watson_mini_world_stories.questphase / h0 / 114 |

## Exact gates, joins and cancellation

<details><summary>129 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `watson_mini_world_stories.questphase / h0 / 82` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":5}}}` | 76:Out1_test → 82:In; 82:Out → 108:In |
| `watson_mini_world_stories.questphase / h0 / 98` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mws_thenerves_questtrigger"}}` | 108:Out → 98:In; 98:Out → 103:In |
| `watson_mini_world_stories.questphase / h0 / 103` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","conditions":[{"$type":"questTriggerCondition","triggerAreaRef":"#mws_thenerves_questtrigger"},{"$type":"questTimeCondition","type":{"$type":"questTimePeriod_ConditionType","begin":{"$type":"GameTime","seconds":72000},"end":{"$type":"GameTime","seconds":18000}}}]}}` | 98:Out → 103:In; 103:Out → 113:In |
| `watson_mini_world_stories.questphase / h0 / 108` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Failed"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq032_sacrum/mq032_sacrum","fileEntryIndex":2,"className":"gameJournalQuestPhase"},"state":"Inactive"}}]}}` | 78:Out → 108:In; 82:Out → 108:In; 108:Out → 98:In |
| `watson_mini_world_stories.questphase / h0 / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questLogicalCondition","operation":"OR","conditions":[{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Succeeded"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk","fileEntryIndex":2,"className":"gameJournalQuestObjective"},"state":"Failed"}},{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/minor_quest/mq032_sacrum/mq032_sacrum","fileEntryIndex":2,"className":"gameJournalQuestPhase"},"state":"Inactive"}}]}}` | 103:Out → 113:In; 113:Out → 114:In |
| `watson_mini_world_stories.questphase / h0 / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q306_active","value":1,"comparisonType":"NotEqual"}}}` | 114:Out → 76:In1_test; 113:Out → 114:In |
| `mq032_01_hook.questphase / h0 / 1` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_monk_cyberware"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 0:Out → 1:In; 1:Out → 2:In |
| `mq032_01_hook.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq032_tr_hook"}}` | 1:Out → 2:In; 2:Out → 3:mq032_01_hook_in; 2:Out → 25:In; 2:Out → 37:In1 |
| `mq032_01_hook.questphase / h0 / 8` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq032_tr_maelstrom"}}` | 6:Out → 8:In; 8:Out → 13:Inactive |
| `mq032_01_hook.questphase / h0 / 22` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content"}}}` | 22:False → 4:Active; 5:Out → 22:In; 22:True → 23:Active |
| `mq032_01_hook.questphase / h0 / 24` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content"}}}` | 4:Out → 24:In; 24:False → 10:Active; 24:True → 19:Active |
| `mq032_01_hook.questphase / h0 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq032_tr_hook"}}` | 27:Out → 26:In; 32:CutSource → 27:CutDestination; 29:Out → 27:In |
| `mq032_01_hook.questphase / h0 / 28` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq032_tr_hook"}}` | 26:Out → 28:In; 32:CutSource → 28:CutDestination; 28:Out → 31:In |
| `mq032_01_hook.questphase / h0 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 25:Out → 29:In; 29:Out → 27:In; 32:CutSource → 29:CutDestination |
| `mq032_01_hook.questphase / h0 / 31` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 31:Out → 25:In; 28:Out → 31:In; 32:CutSource → 31:CutDestination |
| `mq032_01_hook.questphase / h0 / 32` | `questCutControlNodeDefinition` `{"permanent":true}` | 3:mq032_01_hook_out → 32:In; 32:CutSource → 27:CutDestination; 32:CutSource → 28:CutDestination; 32:CutSource → 29:CutDestination; 32:CutSource → 31:CutDestination; 32:Out → 33:In |
| `mq032_01_hook.questphase / h221 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq032_com_monk_cyberware","names":["monk"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0},"comparisonType":"LessOrEqual"}}}` | 0:Out → 2:In; 7:CutSource → 2:CutDestination; 29:Out → 2:In; 2:Out → 4:In |
| `mq032_01_hook.questphase / h221 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq032_com_monk_cyberware","names":["monk"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0}}}}` | 7:CutSource → 3:CutDestination; 27:Out → 3:In; 3:Out → 5:In |
| `mq032_01_hook.questphase / h221 / 6` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_monk1_met"}}}` | 0:Out → 6:In; 6:Out → 7:In |
| `mq032_01_hook.questphase / h221 / 7` | `questCutControlNodeDefinition` `{"permanent":true}` | 7:CutSource → 2:CutDestination; 7:CutSource → 3:CutDestination; 7:CutSource → 4:CutDestination; 7:CutSource → 5:CutDestination; 6:Out → 7:In; 7:Out → 33:In; 7:CutSource → 27:CutDestination; 7:CutSource → 29:CutDestination |
| `mq032_01_hook.questphase / h221 / 27` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 27:Out → 3:In; 4:Out → 27:In; 7:CutSource → 27:CutDestination |
| `mq032_01_hook.questphase / h221 / 29` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 29:Out → 2:In; 5:Out → 29:In; 7:CutSource → 29:CutDestination |
| `mq032_01_hook.questphase / h221 / 33` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq032_com_monk_cyberware","names":["monk"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":30.0}}}}` | 7:Out → 33:In; 33:Out → 32:In |
| `mq032_02_maelstrom.questphase / h0 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq032_tr_maelstrom"}}` | 3:Out1 → 2:In; 2:Out → 92:In1 |
| `mq032_02_maelstrom.questphase / h0 / 6` | `questCutControlNodeDefinition` `{"permanent":true}` | 6:CutSource → 4:CutDestination; 5:stopscene → 6:In; 6:Out → 53:In1; 6:Out → 7:mq032_02_maelstrom_attack_in; 6:CutSource → 62:CutDestination |
| `mq032_02_maelstrom.questphase / h0 / 13` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_help"}}}` | 13:True → 9:Inactive; 53:Out1 → 13:In; 13:False → 82:In |
| `mq032_02_maelstrom.questphase / h0 / 20` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq032_tr_leave"}}` | 23:CutSource → 20:CutDestination; 22:Out1 → 20:In; 20:Out → 36:In1 |
| `mq032_02_maelstrom.questphase / h0 / 22` | `questLogicalXorNodeDefinition` `{}` | 22:Out1 → 20:In; 21:Out → 22:In2; 92:Out1 → 22:In1; 22:Out1 → 35:In |
| `mq032_02_maelstrom.questphase / h0 / 23` | `questCutControlNodeDefinition` `{"permanent":true}` | 23:CutSource → 20:CutDestination; 43:Out1 → 23:In |
| `mq032_02_maelstrom.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq032_tr_leave"}}` | 101:Out → 26:In; 26:Out → 76:In1 |
| `mq032_02_maelstrom.questphase / h0 / 35` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_monk_brother"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 22:Out1 → 35:In; 35:Out → 37:In |
| `mq032_02_maelstrom.questphase / h0 / 36` | `questLogicalXorNodeDefinition` `{}` | 20:Out → 36:In1; 36:Out1 → 31:Failed; 44:mq032_02_killed_out → 36:In2 |
| `mq032_02_maelstrom.questphase / h0 / 53` | `questLogicalXorNodeDefinition` `{}` | 4:mq032_02_maelstrom_out → 53:In2; 6:Out → 53:In1; 53:Out1 → 13:In |
| `mq032_02_maelstrom.questphase / h0 / 58` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq032_tr_maelstrom_fluff"}}` | 3:Out1 → 58:In; 58:Out → 96:In2; 58:Out → 99:In |
| `mq032_02_maelstrom.questphase / h0 / 59` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq032_tr_saved"}}` | 17:Out → 59:In; 59:Out → 104:In; 59:Out → 110:In |
| `mq032_02_maelstrom.questphase / h0 / 68` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"count":1,"comparisonType":"GreaterOrEqual"},"unconscious":false,"defeated":false}}}` | 16:Out → 68:In; 68:Out → 65:In; 91:CutSource → 68:CutDestination |
| `mq032_02_maelstrom.questphase / h0 / 70` | `questCutControlNodeDefinition` `{"permanent":true}` | 70:CutSource → 18:CutDestination; 70:CutSource → 29:CutDestination; 37:Out → 70:In; 70:CutSource → 43:CutDestination; 70:Out → 69:In; 70:CutSource → 105:CutDestination |
| `mq032_02_maelstrom.questphase / h0 / 76` | `questLogicalAndNodeDefinition` `{}` | 26:Out → 76:In1; 76:Out1 → 38:In; 79:Out1 → 76:In2 |
| `mq032_02_maelstrom.questphase / h0 / 77` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questGameTimeDelay_ConditionType","days":1}}}` | 78:False → 77:In; 77:Out → 79:In2 |
| `mq032_02_maelstrom.questphase / h0 / 78` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_test_def"}}}` | 18:mq032_02_saved_out → 78:In; 78:False → 77:In; 78:True → 79:In1 |
| `mq032_02_maelstrom.questphase / h0 / 79` | `questLogicalXorNodeDefinition` `{}` | 79:Out1 → 76:In2; 77:Out → 79:In2; 78:True → 79:In1 |
| `mq032_02_maelstrom.questphase / h0 / 82` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content"}}}` | 13:False → 82:In; 82:False → 81:Active; 82:True → 107:Active |
| `mq032_02_maelstrom.questphase / h0 / 91` | `questCutControlNodeDefinition` `{"permanent":true}` | 18:mq032_02_saved_out → 91:In; 91:CutSource → 68:CutDestination; 91:Out → 117:In; 91:CutSource → 115:CutDestination; 91:CutSource → 113:CutDestination; 91:CutSource → 114:CutDestination; 91:CutSource → 112:CutDestination |
| `mq032_02_maelstrom.questphase / h0 / 92` | `questLogicalXorNodeDefinition` `{}` | 2:Out → 92:In1; 92:Out1 → 4:mq032_02_maelstrom_in; 92:Out1 → 22:In1; 92:Out1 → 67:mq032_monk_animations_in; 93:Out → 92:In2 |
| `mq032_02_maelstrom.questphase / h0 / 93` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_monk_brother"},"onScreenTest":true}}}` | 3:Out1 → 93:In; 93:Out → 92:In2 |
| `mq032_02_maelstrom.questphase / h0 / 95` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_monk_brother"},"onScreenTest":true}}}` | 3:Out1 → 95:In; 95:Out → 96:In1 |
| `mq032_02_maelstrom.questphase / h0 / 96` | `questLogicalXorNodeDefinition` `{}` | 58:Out → 96:In2; 96:Out1 → 62:mq032_02_maelstrom_fluff_in; 95:Out → 96:In1 |
| `mq032_02_maelstrom.questphase / h0 / 97` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq032_tr_leave"}}` | 97:Out → 39:In; 40:Out → 97:In |
| `mq032_02_maelstrom.questphase / h0 / 104` | `questCutControlNodeDefinition` `{"permanent":true}` | 104:CutSource → 29:CutDestination; 59:Out → 104:In; 104:Out → 125:In; 104:Out → 105:mq032_03_monk_cyberware_in; 104:CutSource → 124:CutDestination; 104:CutSource → 123:CutDestination; 104:CutSource → 121:CutDestination; 104:CutSource → 122:CutDestination; 104:CutSource → 118:CutDestination |
| `mq032_02_maelstrom.questphase / h0 / 112` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq032_tr_saved"}}` | 91:CutSource → 112:CutDestination; 112:Out → 111:In; 114:Out → 112:In |
| `mq032_02_maelstrom.questphase / h0 / 113` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq032_tr_saved"}}` | 91:CutSource → 113:CutDestination; 111:Out → 113:In; 113:Out → 115:In |
| `mq032_02_maelstrom.questphase / h0 / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 91:CutSource → 114:CutDestination; 110:Out → 114:In; 114:Out → 112:In |
| `mq032_02_maelstrom.questphase / h0 / 115` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 91:CutSource → 115:CutDestination; 115:Out → 110:In; 113:Out → 115:In |
| `mq032_02_maelstrom.questphase / h0 / 118` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq032_tr_maelstrom_signpost"}}` | 3:Out1 → 118:In; 104:CutSource → 118:CutDestination; 118:Out → 119:In |
| `mq032_02_maelstrom.questphase / h0 / 121` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq032_tr_maelstrom_signpost"}}` | 104:CutSource → 121:CutDestination; 121:Out → 120:In; 123:Out → 121:In |
| `mq032_02_maelstrom.questphase / h0 / 122` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq032_tr_maelstrom_signpost"}}` | 104:CutSource → 122:CutDestination; 120:Out → 122:In; 122:Out → 124:In |
| `mq032_02_maelstrom.questphase / h0 / 123` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 104:CutSource → 123:CutDestination; 119:Out → 123:In; 123:Out → 121:In |
| `mq032_02_maelstrom.questphase / h0 / 124` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":100}}}` | 104:CutSource → 124:CutDestination; 124:Out → 119:In; 122:Out → 124:In |
| `mq032_02_maelstrom.questphase / h0 / 127` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content"}}}` | 9:Out → 127:In; 72:Out → 127:In; 127:True → 128:Active; 127:False → 131:Active |
| `mq032_02_maelstrom.questphase / h31 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_monk_brother"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 2:Out → 3:In; 3:Out → 7:In |
| `mq032_02_maelstrom.questphase / h424 / 61` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq032_dvc_security_system_001","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 61:In; 61:Out → 67:In |
| `mq032_02_maelstrom.questphase / h424 / 62` | `questLogicalXorNodeDefinition` `{}` | 62:Out1 → 45:In; 65:Out → 62:In1; 66:Out1 → 62:In2 |
| `mq032_02_maelstrom.questphase / h424 / 65` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 65:Out → 62:In1; 67:Out → 65:In; 66:Out2 → 65:In |
| `mq032_02_maelstrom.questphase / h424 / 67` | `questCutControlNodeDefinition` `{}` | 61:Out → 67:In; 67:Out → 65:In; 67:CutSource → 66:CutDestination |
| `mq032_02_maelstrom.questphase / h477 / 2` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom","names":["maelstrom_01"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 0:Out → 2:In; 2:Out → 7:In1 |
| `mq032_02_maelstrom.questphase / h477 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom","names":["maelstrom_03"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 0:Out → 3:In; 3:Out → 7:In3 |
| `mq032_02_maelstrom.questphase / h477 / 4` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom","names":["maelstrom_02"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 0:Out → 4:In; 4:Out → 7:In2 |
| `mq032_02_maelstrom.questphase / h477 / 5` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom","names":["maelstrom_08"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 0:Out → 5:In; 5:Out → 7:In4 |
| `mq032_02_maelstrom.questphase / h477 / 7` | `questLogicalAndNodeDefinition` `{"inputSocketCount":4}` | 2:Out → 7:In1; 3:Out → 7:In3; 4:Out → 7:In2; 5:Out → 7:In4; 7:Out1 → 10:In |
| `mq032_02_maelstrom.questphase / h477 / 9` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq032_dvc_security_system_001","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 9:In; 9:Out → 8:In |
| `mq032_02_maelstrom.questphase / h477 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterKilled_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom","names":["maelstrom_12"]},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 10:Out → 1:In; 7:Out1 → 10:In |
| `mq032_combat.questphase / h12 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 3:Out → 1:In; 2:Out → 3:In |
| `mq032_combat.questphase / h43 / 3` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq032_dvc_dang_area","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemAlerted"}}}` | 0:Out → 3:In; 3:Out → 8:In1 |
| `mq032_combat.questphase / h43 / 7` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questObjectCondition","type":{"$type":"questDevice_ConditionType","objectRef":"#mq032_dvc_dang_area","deviceControllerClass":"SecuritySystemControllerPS","deviceConditionFunction":"IsSystemInCombat"}}}` | 0:Out → 7:In; 7:Out → 8:In2 |
| `mq032_combat.questphase / h43 / 8` | `questLogicalXorNodeDefinition` `{"inputSocketCount":7}` | 3:Out → 8:In1; 8:Out1 → 4:In; 8:Out1 → 5:In; 7:Out → 8:In2; 10:Out → 8:In3; 12:Out → 8:In4; 13:Out → 8:In5; 14:Out → 8:In6; 15:Out → 8:In7 |
| `mq032_combat.questphase / h43 / 10` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom","names":["maelstrom_01"]},"isPlayer":false}}}` | 0:Out → 10:In; 10:Out → 8:In3 |
| `mq032_combat.questphase / h43 / 12` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom","names":["maelstrom_02"]},"isPlayer":false}}}` | 0:Out → 12:In; 12:Out → 8:In4 |
| `mq032_combat.questphase / h43 / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom","names":["maelstrom_03"]},"isPlayer":false}}}` | 0:Out → 13:In; 13:Out → 8:In5 |
| `mq032_combat.questphase / h43 / 14` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom","names":["maelstrom_08"]},"isPlayer":false}}}` | 0:Out → 14:In; 14:Out → 8:In6 |
| `mq032_combat.questphase / h43 / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterCombat_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#mq032_com_maelstrom","names":["maelstrom_12"]},"isPlayer":false}}}` | 0:Out → 15:In; 15:Out → 8:In7 |
| `mq032_01_hook.scene / scene / 24` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":3}}}` | 24:0:0 → 26:0:0; 36:0:0 → 24:0:1 |
| `mq032_01_hook.scene / scene / 75` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq032_01_hook_Johnny"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 75:0:0 → 244:0:1; 82:0:0 → 75:0:1; 143:0:0 → 75:0:1 |
| `mq032_01_hook.scene / scene / 82` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content"}}}` | 62:0:0 → 82:0:1; 82:0:0 → 75:0:1; 82:0:0 → 103:0:1; 82:0:1 → 103:0:1 |
| `mq032_01_hook.scene / scene / 129` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 6:1:0 → 129:0:1; 129:0:0 → 71:0:0 |
| `mq032_01_hook.scene / scene / 183` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq032_com_monk_cyberware","names":["monk"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0}}}}` | 103:0:0 → 183:0:1; 183:0:0 → 185:0:0 |
| `mq032_01_hook.scene / scene / 218` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":2}}}` | 188:0:0 → 218:0:1; 218:0:0 → 6:0:0 |
| `mq032_01_hook.scene / scene / 229` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content"}}}` | 1:0:0 → 229:0:1; 229:0:0 → 231:0:1 |
| `mq032_01_hook.scene / scene / 231` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq032_01_hook_Johnny"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 229:0:0 → 231:0:1; 231:0:0 → 240:0:1 |
| `mq032_01_hook.scene / scene / 248` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":300}}}` | 244:0:0 → 248:0:1; 248:0:0 → 65:0:0 |
| `mq032_01_hook.scene / scene / 312` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq032_01_hook_Johnny"},"onScreenTest":true,"inverted":true}}}` | 65:0:0 → 312:0:1; 134:4:0 → 312:0:1; 136:2:1 → 312:0:1; 312:0:0 → 197:0:1 |
| `mq032_01_hook.scene / scene / 327` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_stop_idle_gestures","value":1,"comparisonType":"Less"}}}` | 4:2:0 → 327:0:1; 327:0:0 → 328:0:0 |
| `mq032_01_hook.scene / scene / 330` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_stop_idle_gestures","value":1,"comparisonType":"Less"}}}` | 4:2:1 → 330:0:1; 330:0:0 → 332:0:0 |
| `mq032_01_hook.scene / scene / 335` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_stop_idle_gestures","value":1,"comparisonType":"Less"}}}` | 4:2:3 → 335:0:1; 335:0:0 → 337:0:0 |
| `mq032_01_hook.scene / scene / 339` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_stop_idle_gestures","value":1,"comparisonType":"Less"}}}` | 4:2:4 → 339:0:1; 339:0:0 → 341:0:0 |
| `mq032_01_hook.scene / scene / 345` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_stop_idle_gestures","value":1,"comparisonType":"Less"}}}` | 4:2:5 → 345:0:1; 345:0:0 → 347:0:0 |
| `mq032_01_hook.scene / scene / 349` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_stop_idle_gestures","value":1,"comparisonType":"Less"}}}` | 4:2:6 → 349:0:1; 349:0:0 → 351:0:0 |
| `mq032_01_hook.scene / scene / 353` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_stop_idle_gestures","value":1,"comparisonType":"Less"}}}` | 4:2:7 → 353:0:1; 353:0:0 → 355:0:0 |
| `mq032_01_hook.scene / scene / 357` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_stop_idle_gestures","value":1,"comparisonType":"Less"}}}` | 4:2:8 → 357:0:1; 357:0:0 → 359:0:0 |
| `mq032_01_hook.scene / scene / 365` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_stop_idle_gestures","value":1,"comparisonType":"Less"}}}` | 4:2:9 → 365:0:1; 365:0:0 → 367:0:0 |
| `mq032_01_hook.scene / scene / 369` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_stop_idle_gestures","value":1,"comparisonType":"Less"}}}` | 4:2:10 → 369:0:1; 369:0:0 → 371:0:0 |
| `mq032_01_hook.scene / scene / 389` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_stop_idle_gestures","value":1,"comparisonType":"Less"}}}` | 4:2:2 → 389:0:1; 389:0:0 → 391:0:0; 395:0:0 → 389:0:1 |
| `mq032_01_hook.scene / scene / 402` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","anyParent":true,"childIsPlayer":true}}}` | 65:2:0 → 402:0:1; 402:0:1 → 134:0:0 |
| `mq032_02_maelstrom.scene / scene / 6` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_help"}}}` | 6:0:0 → 9:0:0; 6:0:1 → 2:0:0; 70:0:0 → 6:0:1 |
| `mq032_02_maelstrom.scene / scene / 20` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_nonlethal"}}}` | 20:0:0 → 35:0:0; 20:0:1 → 37:0:0; 26:0:0 → 20:0:1; 28:2:1 → 20:0:1; 30:0:0 → 20:0:1 |
| `mq032_02_maelstrom.scene / scene / 73` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_nonlethal"}}}` | 73:0:0 → 74:0:0; 73:0:1 → 75:0:0; 120:0:0 → 73:0:1 |
| `mq032_02_maelstrom.scene / scene / 85` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_help"}}}` | 85:0:0 → 39:0:0; 85:0:1 → 235:0:3; 86:0:0 → 85:0:1 |
| `mq032_02_maelstrom.scene / scene / 86` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_nonlethal"}}}` | 86:0:0 → 85:0:1; 86:0:1 → 39:0:0; 105:0:1 → 86:0:1; 106:0:0 → 86:0:1; 111:0:0 → 86:0:1; 114:0:1 → 86:0:1 |
| `mq032_02_maelstrom.scene / scene / 105` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_01_whatIgnorance","value":1,"comparisonType":"GreaterOrEqual"}}}` | 35:0:0 → 105:0:1; 105:0:0 → 106:0:0; 105:0:1 → 86:0:1 |
| `mq032_02_maelstrom.scene / scene / 114` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_monk1_met","value":1,"comparisonType":"GreaterOrEqual"}}}` | 37:0:0 → 114:0:1; 114:0:0 → 111:0:0; 114:0:1 → 86:0:1 |
| `mq032_02_maelstrom.scene / scene / 120` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq032_02_maelstrom_Johnny"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 120:0:0 → 73:0:1; 120:0:0 → 323:0:1; 144:0:0 → 120:0:1 |
| `mq032_02_maelstrom.scene / scene / 144` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"q101_enable_side_content"}}}` | 144:0:0 → 120:0:1; 144:0:1 → 231:0:1; 463:0:0 → 144:0:1 |
| `mq032_02_maelstrom.scene / scene / 197` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_monk_get_up"}}}` | 17:0:0 → 197:0:1; 193:0:0 → 197:0:1; 197:0:0 → 166:0:0 |
| `mq032_02_maelstrom.scene / scene / 207` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq032_02_maelstrom_Johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"angleTolerance":92.0,"inverted":true}}}` | 74:0:0 → 207:0:1; 75:0:0 → 207:0:1; 207:0:0 → 231:0:1; 207:0:0 → 327:0:1 |
| `mq032_02_maelstrom.scene / scene / 275` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 275:0:0 → 270:0:0; 335:0:0 → 275:0:1 |
| `mq032_02_maelstrom.scene / scene / 298` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_nonlethal"}}}` | 298:0:0 → 293:0:0; 298:0:1 → 320:0:0; 304:0:0 → 298:0:1 |
| `mq032_02_maelstrom.scene / scene / 304` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"cutfornow"}}}` | 273:3:0 → 304:0:1; 273:3:1 → 304:0:1; 304:0:0 → 298:0:1 |
| `mq032_02_maelstrom.scene / scene / 335` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq032_com_monk_brother","names":["brother"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0}}}}` | 332:0:0 → 335:0:1; 335:0:0 → 273:0:0; 335:0:0 → 275:0:1; 335:0:0 → 511:0:1; 335:0:0 → 585:0:1 |
| `mq032_02_maelstrom.scene / scene / 342` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq032_02_maelstrom_Johnny"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 17:0:0 → 342:0:1; 342:0:0 → 349:0:1 |
| `mq032_02_maelstrom.scene / scene / 454` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq032_com_monk_brother","names":["brother"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":50.0}}}}` | 351:0:0 → 454:0:1; 454:0:0 → 457:0:1 |
| `mq032_02_maelstrom.scene / scene / 457` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":1}}}` | 454:0:0 → 457:0:1; 457:0:0 → 456:0:0 |
| `mq032_02_maelstrom.scene / scene / 471` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_dead","comparisonType":"Equal"}}}` | 158:0:0 → 471:0:1; 471:0:0 → 159:0:0 |
| `mq032_02_maelstrom.scene / scene / 595` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq032_com_monk_brother","names":["brother"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":10.0}}}}` | 589:0:0 → 595:0:1; 595:0:0 → 597:0:0 |
| `mq032_02_maelstrom.scene / scene / 602` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questDistanceCondition","type":{"$type":"questDistanceComparison_ConditionType","distanceDefinition1":{"$type":"questObjectDistance","entityRef":{"$type":"questUniversalRef"},"nodeRef2":{"$type":"gameEntityReference","reference":"#mq032_com_monk_brother","names":["brother"]}},"distanceDefinition2":{"$type":"questValueDistance","distanceValue":5.0},"comparisonType":"Less"}}}` | 597:0:0 → 602:0:1; 602:0:0 → 589:0:0 |
| `mq032_03_epilogue.scene / scene / 11` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","minutes":1}}}` | 11:0:0 → 13:0:1; 15:0:0 → 11:0:1 |
| `mq032_03_epilogue.scene / scene / 13` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","triggerAreaRef":"#mq032_tr_hook"}}` | 11:0:0 → 13:0:1; 13:0:0 → 5:0:0 |
| `mq032_03_epilogue.scene / scene / 15` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTriggerCondition","type":"IsOutside","triggerAreaRef":"#mq032_tr_hook"}}` | 1:0:0 → 15:0:1; 15:0:0 → 11:0:1; 20:0:0 → 15:0:1 |
| `mq032_03_epilogue.scene / scene / 48` | `questConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mq032_nonlethal"}}}` | 43:0:0 → 48:0:1; 48:0:0 → 104:0:1; 48:0:1 → 51:0:0; 162:0:0 → 48:0:1 |
| `mq032_03_epilogue.scene / scene / 96` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq032_03_epilogue_Johnny"},"timeInterval":0.10000000149011612,"onScreenTest":true,"angleTolerance":92.0,"inverted":true}}}` | 92:0:0 → 96:0:1; 96:0:0 → 119:0:1 |
| `mq032_03_epilogue.scene / scene / 114` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","dynamicEntityUniqueName":"a_mq032_03_epilogue_Johnny"},"comparisonParams":{"$type":"questComparisonParam","entireCommunity":false,"comparisonType":"Greater"}}}}` | 77:2:0 → 114:0:1; 114:0:0 → 92:0:1; 114:0:0 → 117:0:1 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | mq032_01_hook.questphase / h0 / 1; mq032_01_hook.scene / scene / 231; mq032_01_hook.scene / scene / 75; mq032_02_maelstrom.questphase / h31 / 3; +4 locations in catalogue.json | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `actor_route` | mq032_02_maelstrom.scene / scene / 284 | actor + authored route/spline + movement policy → movement output. World navigation is a dependency; test blockage, combat and departure recovery. |
| `checkpoint` | mq032_01_hook.questphase / h0 / 20; mq032_02_maelstrom.questphase / h0 / 100; mq032_02_maelstrom.questphase / h0 / 101; mq032_02_maelstrom.questphase / h0 / 99 | checkpoint scope + save eligibility + debug identity → checkpoint request. Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone. |
| `choice_gate` | mq032_01_hook.scene / scene / 10; mq032_01_hook.scene / scene / 134; mq032_01_hook.scene / scene / 17; mq032_01_hook.scene / scene / 26; +10 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `community_lifecycle` | mq032_01_hook.questphase / h0 / 0; mq032_02_maelstrom.questphase / h0 / 126; mq032_02_maelstrom.questphase / h0 / 38; mq032_02_maelstrom.questphase / h0 / 39; +3 locations in catalogue.json | community + named entries/phases + ownership → activated/reactivated/deactivated entries. Spawn, readiness and safe departure cleanup are separate steps. |
| `conditional_route` | mq032_01_hook.questphase / h0 / 22; mq032_01_hook.questphase / h0 / 24; mq032_01_hook.questphase / h221 / 6; mq032_01_hook.scene / scene / 229; +34 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `content_scope` | mq032_01_hook.questphase / h221 / 32; mq032_01_hook.questphase / h221 / 4; mq032_01_hook.questphase / h221 / 5; mq032_02_maelstrom.questphase / h0 / 60 | owned token source + block/unblock/spawn operation → scope acquired/released. Avoid copying broad UnblockAll behavior without an explicit ownership policy. |
| `controller_event` | mq032_02_maelstrom.scene / scene / 349; mq032_02_maelstrom.scene / scene / 351 | entity + controller/PS class + typed event → event dispatched. Resolve controller ownership and its completion predicate; an event send is not operation success. |
| `device_action` | mq032_02_maelstrom.questphase / h424 / 45; mq032_02_maelstrom.questphase / h424 / 47 | controller class + object + action → action dispatched. Bind the matching device completion predicate; dispatch alone is not success. |
| `device_state` | mq032_02_maelstrom.questphase / h424 / 61; mq032_02_maelstrom.questphase / h477 / 9; mq032_combat.questphase / h43 / 3; mq032_combat.questphase / h43 / 7 | controller class + object + condition function → device predicate. Check already-satisfied state and controller persistence across save/load. |
| `elapsed_time` | mq032_02_maelstrom.questphase / h0 / 77; watson_mini_world_stories.questphase / h0 / 82 | clock domain + duration + start/reset condition → elapsed signal. Compose objective/contact behavior separately; test time skip and save/load. |
| `journal_transition` | mq032_01_hook.questphase / h0 / 10; mq032_01_hook.questphase / h0 / 11; mq032_01_hook.questphase / h0 / 12; mq032_01_hook.questphase / h0 / 13; +19 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | mq032_01_hook.scene / scene / 402 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | mq032_02_maelstrom.questphase / h0 / 76; mq032_02_maelstrom.questphase / h477 / 7 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | mq032_01_hook.questphase / h0 / 5; mq032_01_hook.scene / scene / 208; mq032_01_hook.scene / scene / 36; mq032_01_hook.scene / scene / 39; +10 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `race_resolution` | mq032_02_maelstrom.questphase / h0 / 22; mq032_02_maelstrom.questphase / h0 / 36; mq032_02_maelstrom.questphase / h0 / 53; mq032_02_maelstrom.questphase / h0 / 79; +4 locations in catalogue.json | competing outcome signals + retirement policy → converged signal. Review actual graph wiring; an XOR class alone does not prove loser cancellation. |
| `realtime_delay` | mq032_01_hook.questphase / h0 / 29; mq032_01_hook.questphase / h0 / 31; mq032_01_hook.questphase / h221 / 27; mq032_01_hook.questphase / h221 / 29; +11 locations in catalogue.json | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `retire_branch` | mq032_01_hook.questphase / h0 / 32; mq032_01_hook.questphase / h221 / 7; mq032_02_maelstrom.questphase / h0 / 104; mq032_02_maelstrom.questphase / h0 / 23; +4 locations in catalogue.json | owned target branch(es) + permanent/reset policy → branch retired. Trace every CutSource destination; cancellation must not commit success. |
| `reward_commit` | mq032_02_maelstrom.scene / scene / 463 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | mq032_01_hook.questphase / h0 / 3; mq032_02_maelstrom.questphase / h0 / 105; mq032_02_maelstrom.questphase / h0 / 18; mq032_02_maelstrom.questphase / h0 / 29; +5 locations in catalogue.json | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `spatial_gate` | mq032_01_hook.questphase / h0 / 2; mq032_01_hook.questphase / h0 / 27; mq032_01_hook.questphase / h0 / 28; mq032_01_hook.questphase / h0 / 8; +15 locations in catalogue.json | trigger + activator + exact inside/outside event → spatial predicate. Resolve the registered NodeRef and test starting inside, exiting, actor activation and return. |
| `target_resolution` | mq032_02_maelstrom.questphase / h0 / 35; mq032_02_maelstrom.questphase / h0 / 68; mq032_02_maelstrom.questphase / h424 / 65; mq032_02_maelstrom.questphase / h477 / 10; +4 locations in catalogue.json | target set + lethal/unconscious/defeated policy → target resolved. Review RED defaults, early defeat and per-target deduplication before counter joins. |
| `vehicle_control` | mq032_02_maelstrom.scene / scene / 585 | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `workspot_performance` | mq032_01_hook.scene / scene / 113; mq032_01_hook.scene / scene / 114; mq032_01_hook.scene / scene / 115; mq032_01_hook.scene / scene / 116; +21 locations in catalogue.json | actor + workspot + entry/exit policy → work started/success/failure. Wait for actor/spot readiness and restore AI ownership on interruption. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\mini_world_stories\watson\watson_mini_world_stories.questphase` | content candidate; journal anchor | `base-shared` |
| `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` | content candidate; journal anchor | `base-mq032` |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` | content candidate; journal anchor | `base-mq032` |
| `base\quest\minor_quests\mq032\phases\mq032_combat.questphase` | content candidate; forward dependency | `base-mq032` |
| `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` | content candidate; forward dependency | `base-mq032` |
| `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene` | content candidate; journal anchor | `base-mq032` |
| `base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene` | content candidate; forward dependency | `base-mq032` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

309 repeated typed/socket path signatures in this selected graph context; 44 distinct direct resource identities; 6 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h31 / 0 -> 2 -> 3 | questInputNodeDefinition -> questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]; Out -> In; Out -> In |
| `8cd3b647ae3f592ad947` | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene` / scene / 12 -> 13 -> 15 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnEndNode[scnNodeId]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `a53561b4c002bc02b58a` | `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 14 -> 17 -> 59 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> Active; Out -> In |
| `19665e3783f6f51a7337` | `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` / scene / 1 -> 188 -> 323 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `31294c8f4e8aa6c1b8cb` | `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 59 -> 104 -> 124 | questPauseConditionNodeDefinition[questTriggerCondition] -> questCutControlNodeDefinition -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; Out -> In; CutSource -> CutDestination |
| `c1b6601d2f647c8a694d` | `base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene` / scene / 25 -> 27 -> 29 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `016828d499c85128303c` | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene` / scene / 35 -> 105 -> 106 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `84bfca44950402ede644` | `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` / scene / 46 -> 49 -> 123 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]; 0:0 -> 0:0; 2:0 -> 0:1 |
| `1fa539921730278ef7fb` | `base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene` / scene / 27 -> 29 -> 33 | scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `f3a269b6a97862bc211c` | `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` / h0 / 0 -> 1 -> 2 | questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam] -> questPauseConditionNodeDefinition[questTriggerCondition]; Out -> In; Out -> In |
| `2fd99f4299806c136bfa` | `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` / scene / 1 -> 188 -> 4 | scnStartNode[scnNodeId] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]; 0:0 -> 0:0; 0:0 -> 0:0 |
| `7ff0eae411231e617b77` | `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` / scene / 30 -> 32 -> 62 | scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; 0:0 -> 0:0; 0:0 -> 0:1 |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` / h0 / 37 | `h221` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 3 | `h31` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 43 | `h424` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h424 / 66 | `h477` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"},{"$type":"questOutputNodeDefinition","id":8,"socketName":"Out2"}] |
| `base\quest\minor_quests\mq032\phases\mq032_combat.questphase` / h0 / 4 | `h12` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Out1"}] |
| `base\quest\minor_quests\mq032\phases\mq032_combat.questphase` / h0 / 5 | `h43` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"In1"},{"$type":"questOutputNodeDefinition","id":5,"socketName":"stopscene","type":"NonTerminating"}] |

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
| `base\open_world\district_definitions\open_world_kabuki.gamedef` | content candidate | base\open_world\district_definitions\open_world_kabuki.quest |
| `base\open_world\open_world_test.gamedef` | content candidate | base\open_world\open_world_test.quest |
| `base\open_world\police_system\police_system_test.gamedef` | content candidate | base\open_world\police_system\police_system_test.quest |
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
| `base\animations\facial\generic\interactive_scene\generic_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_gestures.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_idle.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\facial\male_average\interactive_scene\generic_average_male_facial_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__sit_chair_lean180__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\dirtboy\interactive_scene\dirtboy__stand_wall_lean180__arms_crossed_front_lf_on_wall__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\monk\open_world\monk_work__sit_ground__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\archetype_characters\monk\open_world\monk_work__transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male__lie_ground_0__2h_on_head__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_stand_sink_low_lean0__2h_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_average_male_transitions.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__sit_chair__2h_on_lap__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_back__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__2h_up__02.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_wall_lean180__2h_on_sides__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\npc\generic_characters\male_average\interactive_scene\generic_male_average__stand_wall_lean180__arms_crossed_front__01.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_female__stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\animations\player\interactive_scene\player_male__stand__2h_on_sides.anims` | asset binding .anims | content/basegame_4_animation.archive; index evidence only |
| `base\quest\minor_quests\mq032\phases\mq032_combat.questphase` | phase flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_01_hook\civ_high_m_22_jap_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_01_hook\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_01_hook\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_02_maelstrom\civ_high_m_19_jap_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_02_maelstrom\gang_mls_m_02_enus_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_02_maelstrom\gang_mls_m_09_enus_40.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_02_maelstrom\gang_mls_m_13_enus_20.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_02_maelstrom\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_02_maelstrom\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_03_epilogue\civ_high_m_19_jap_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_03_epilogue\civ_high_m_22_jap_30.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_03_epilogue\johnny.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\lipsync\en\mq032_03_epilogue\v.anims` | asset binding .anims | No match in inspected vanilla indexes; index evidence only |
| `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |
| `base\workspots\archetype\corpo\corpo__sit_chair_nails__paint__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\archetype\monk\common\ground\monk__sit_ground__meditate__04.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\big__stand_ground__look_at_products__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\big__stand_microwave__use__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\ground\generic__stand_ground__afraid__01.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |
| `base\workspots\common\wall\generic__stand_wall_lean_back__stand_around__02.workspot` | performance binding | content/memoryresident_1_general.archive; ep1/ep1_1_nightcity.archive; index evidence only |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `mq032_nonlethal` | base\quest\minor_quests\mq032\scenes\mq032_00_chicken_test_setup.scene / scene / 13; 1 total source locations in compressed evidence |
| `mq032_saved` | base\quest\minor_quests\mq032\scenes\mq032_00_chicken_test_setup.scene / scene / 27; base\quest\minor_quests\mq032\scenes\mq032_00_chicken_test_setup.scene / scene / 29; 2 total source locations in compressed evidence |
| `mq032_test_def` | base\quest\minor_quests\mq032\mq032_sacrum.quest / h0 / 11; 1 total source locations in compressed evidence |
| `q101_enable_side_content` | base\quest\minor_quests\mq025\mq025_psycho_brawl.quest / h0 / 14; base\quest\minor_quests\mq032\scenes\mq032_00_chicken_test_setup.scene / scene / 6; base\quest\minor_quests\mq048\mq048.questphase / h435 / 6; base\quest\minor_quests\mq049\mq049.quest / h0 / 5; 36 total source locations in compressed evidence |
| `q306_active` | ep1\quest\main_quests\q306\phases\debug\q306_meeting_debug_setup.questphase / h0 / 3; ep1\quest\main_quests\q306\phases\q306_00_setup.questphase / h0 / 3; ep1\quest\main_quests\q306\phases\q306_cleanup.questphase / h0 / 19; ep1\quest\main_quests\q306\q306.quest / h99 / 18; 10 total source locations in compressed evidence |

NodeRef uses: 149; TweakDB binding uses: 27. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` | 27 / 206 | scnChangeIdleAnimEvent: 7; scnDialogLineEvent: 45; scnLookAtEvent: 6; scnPlaySkAnimEvent: 123; scnPoseCorrectionEvent: 1; scneventsSocket: 24 |
| `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene` | 31 / 264 | scnChangeIdleAnimEvent: 6; scnDialogLineEvent: 68; scnGameplayTransitionEvent: 1; scnIKEvent: 2; scnLookAtEvent: 17; scnPlaySkAnimEvent: 122; scnPoseCorrectionEvent: 28; scnUnmountEvent: 1; scneventsSetAnimFeatureEvent: 1; scneventsSocket: 18 |
| `base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene` | 16 / 111 | scnChangeIdleAnimEvent: 1; scnDialogLineEvent: 46; scnLookAtEvent: 24; scnPlaySkAnimEvent: 39; scneventsSocket: 1 |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
