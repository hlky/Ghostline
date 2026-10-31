# Outlaw

Journal: `quests/vehicle_metaquest/herrera_outlaw` · `VehicleQuest` · hash `3496387698`.

Journal premise: So this is kinda last minute, but I got a Herrera Outlaw for sale. Wouldn't wait too long on this – knowing folks around here, thing's a fucking thief-magnet. Probably only 1000 of them left in the world, no more than ten in all of NC, so we're talkin' 'bout a precious commodity. So chop chop, don't dawdle or I guarantee you'll be crying yourself to sleep for weeks to come.

**Coverage: journal-linked.** 7 exact journal-linked nodes in 3 resources; 4 resources in the inspected dependency context.

Resource roles in that context: 4 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| Buy Vehicle: Herrera Outlaw (€$92,000) (Primary) | `quests/vehicle_metaquest/herrera_outlaw/herrera_outlaw/buy` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `vehicle_metaquest_achievement.questphase / h0 / 26` (PauseCondition) | `quests/vehicle_metaquest/herrera_outlaw` | 0:Out → 26:In; 26:Out → 55:In |
| `vehicles_metaquest.questphase / h7188 / 7` (Journal) | `quests/vehicle_metaquest/herrera_outlaw/herrera_outlaw/buy` | 5:Out → 7:Active; 7:Out → 27:Active |
| `vehicles_metaquest.questphase / h7188 / 27` (Journal) | `quests/vehicle_metaquest/herrera_outlaw/description` | 27:Out → 2:herrera_outlaw; 7:Out → 27:Active; 27:Out → 33:In |
| `vehicles_metaquest.questphase / h7195 / 31` (Journal) | `quests/vehicle_metaquest/herrera_outlaw` | 31:Out → 24:In; 55:Out → 31:Succeeded |
| `vehicles_metaquest_new.questphase / h21 / 23` (Condition) | `quests/vehicle_metaquest/herrera_outlaw` | 0:Out → 23:In; 23:True → 50:Inactive |
| `vehicles_metaquest_new.questphase / h21 / 50` (Journal) | `quests/vehicle_metaquest/herrera_outlaw` | 23:True → 50:Inactive; 50:Out → 77:In |
| `vehicles_metaquest_new.questphase / h21 / 167` (Journal) | `quests/vehicle_metaquest/herrera_outlaw/herrera_outlaw/buy` | 77:Out → 167:Inactive; 167:Out → 196:Inactive |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| `vehicles_metaquest.questphase / h7195 / 4` | `base\open_world\vendors\vehicles_metaquest\scenes\vehicle_metaquest_choicehub.scene`; `#vehicle_sm_metaquest_choicehub` | 48:Out → 4:chevalier_emperor; 4:chevalier_emperor_bought → 50:In |
| `vehicles_metaquest.questphase / h7195 / 22` | `base\open_world\vendors\vehicles_metaquest\scenes\vehicle_metaquest_choicehub.scene`; `#vehicle_sm_metaquest_choicehub` | 49:Out → 22:herrera_outlaw; 22:herrera_outlaw_bought → 51:In |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h0 / 9 | `vehicle_metaquest_achievement.questphase` |  |
| `base\open_world\phases\open_world_content.questphase` / h0 / 9 | `vehicles_metaquest.questphase` | 0: Input; 0:Out → 9:In1; 9:Out1 → 121:In1 |
| `base\open_world\vendors\vehicles_metaquest\vehicles_metaquest.quest` / h0 / 2 | `vehicles_metaquest.questphase` | 0: Start; 0:Out → 2:In1; 2:Out1 → 4:In1 |
| `base\open_world\phases\open_world_content.questphase` / h0 / 121 | `vehicles_metaquest_new.questphase` | 9: Phase: vehicles_metaquest.questphase; 122: Input; 9:Out1 → 121:In1; 122:Out → 121:EP1_Standalone |
| `base\open_world\vendors\vehicles_metaquest\vehicles_metaquest.quest` / h0 / 4 | `vehicles_metaquest_new.questphase` | 2: Phase: vehicles_metaquest.questphase; 2:Out1 → 4:In1 |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h75 / 5 | `vehicle_metaquest_choicehub.scene` | 71: Vehicle; 71:Out → 5:archer_quartz; 5:archer_quartz_bought → 69:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h75 / 23 | `vehicle_metaquest_choicehub.scene` | 73: Vehicle; 73:Out → 23:thorton_colby; 23:thorton_colby_bought → 70:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h535 / 51 | `vehicle_metaquest_choicehub.scene` | 52: DeletionMarker; 51:thorton_galena_bought → 39:In; 52:Out → 51:thorton_galena |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h799 / 5 | `vehicle_metaquest_choicehub.scene` | 41: Vehicle; 41:Out → 5:mizutani_shion; 5:mizutani_shion_bought → 38:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h799 / 24 | `vehicle_metaquest_choicehub.scene` | 43: Vehicle; 43:Out → 24:quadra_type66_nomad_ncu; 24:quadra_type66_nomad_ncu_bought → 39:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h1575 / 39 | `vehicle_metaquest_choicehub.scene` | 85: Vehicle; 85:Out → 39:quadra_turbo; 39:quadra_turbo_bought → 77:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h1575 / 63 | `vehicle_metaquest_choicehub.scene` | 84: Vehicle; 84:Out → 63:makigai_maimai; 63:makigai_maimai_bought → 76:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h2033 / 5 | `vehicle_metaquest_choicehub.scene` | 38: Vehicle; 38:Out → 5:yaiba_kusanagi; 5:yaiba_kusanagi_bought → 37:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h2279 / 5 | `vehicle_metaquest_choicehub.scene` | 59: Vehicle; 59:Out → 5:arch; 5:arch_bought → 49:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h2279 / 44 | `vehicle_metaquest_choicehub.scene` | 60: Vehicle; 60:Out → 44:rayfield_aerondight; 44:rayfield_aerondight_bought → 52:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h3071 / 18 | `vehicle_metaquest_choicehub.scene` | 81: CharacterManager; 81:Out → 18:thorton_colby_nomad; 18:thorton_colby_nomad_bought → 73:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h3071 / 22 | `vehicle_metaquest_choicehub.scene` | 82: CharacterManager; 82:Out → 22:mizutani_shion_nomad; 22:mizutani_shion_nomad_bought → 74:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h3071 / 34 | `vehicle_metaquest_choicehub.scene` | 83: CharacterManager; 83:Out → 34:quadra_type66_nomad; 34:quadra_type66_nomad_bought → 75:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h3071 / 158 | `vehicle_metaquest_choicehub.scene` | 160: DeletionMarker; 158:thorton_galena_nomad_bought → 72:In; 160:Out → 158:thorton_galena_nomad |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h3071 / 180 | `vehicle_metaquest_choicehub.scene` | 167: CharacterManager; 167:Out → 180:archer_bandit; 180:archer_bandit_bought → 168:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h4719 / 37 | `vehicle_metaquest_choicehub.scene` | 54: CharacterManager; 54:Out → 37:chevalier_thrax; 37:chevalier_thrax_bought → 50:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h4719 / 40 | `vehicle_metaquest_choicehub.scene` | 58: CharacterManager; 58:Out → 40:villefort_cortes; 40:villefort_cortes_bought → 51:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h5186 / 7 | `vehicle_metaquest_choicehub.scene` | 25: CharacterManager; 25:Out → 7:villefort_alvarado; 7:villefort_alvarado_bought → 23:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h5495 / 2 | `vehicle_metaquest_choicehub.scene` | 23: CharacterManager; 23:Out → 2:brennan_apollo; 2:brennan_apollo_bought → 21:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h5954 / 15 | `vehicle_metaquest_choicehub.scene` | 55: CharacterManager; 55:Out → 15:thorton_mackinaw; 15:thorton_mackinaw_bought → 51:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h5954 / 27 | `vehicle_metaquest_choicehub.scene` | 54: CharacterManager; 54:Out → 27:mahir_supron; 27:mahir_supron_bought → 49:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h6417 / 12 | `vehicle_metaquest_choicehub.scene` | 57: CharacterManager; 57:Out → 12:thorton_colby_pickup; 12:thorton_colby_pickup_bought → 51:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h6417 / 40 | `vehicle_metaquest_choicehub.scene` | 56: CharacterManager; 56:Out → 40:quadra_type66; 40:quadra_type66_bought → 48:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7195 / 4 | `vehicle_metaquest_choicehub.scene` | 48: CharacterManager; 48:Out → 4:chevalier_emperor; 4:chevalier_emperor_bought → 50:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7195 / 22 | `vehicle_metaquest_choicehub.scene` | 49: CharacterManager; 49:Out → 22:herrera_outlaw; 22:herrera_outlaw_bought → 51:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7733 / 2 | `vehicle_metaquest_choicehub.scene` | 45: CharacterManager; 45:Out → 2:quadra_type66_avenger; 2:quadra_type66_avenger_bought → 39:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7733 / 7 | `vehicle_metaquest_choicehub.scene` | 46: CharacterManager; 46:Out → 7:rayfield_caliburn; 7:rayfield_caliburn_bought → 40:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7733 / 26 | `vehicle_metaquest_choicehub.scene` | 47: CharacterManager; 47:Out → 26:villefort_columbus; 26:villefort_columbus_bought → 41:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h2130 / 7 | `vehicle_metaquest_choicehub.scene` | 17: Vehicle; 17:Out → 7:quadra_type66_nomad_ncu; 7:quadra_type66_nomad_ncu_bought → 23:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h2397 / 13 | `vehicle_metaquest_choicehub.scene` | 7: CharacterManager; 7:Out → 13:archer_bandit; 13:archer_bandit_bought → 19:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h3154 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:thorton_galena; 14:thorton_galena_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h3367 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:mahir_supron; 14:mahir_supron_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h3571 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:villefort_columbus; 14:villefort_columbus_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h3775 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:thorton_colby; 14:thorton_colby_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h4050 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:makigai_maimai; 14:makigai_maimai_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h4243 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:thorton_colby_pickup; 14:thorton_colby_pickup_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h4437 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:villefort_cortes; 14:villefort_cortes_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h4724 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:thorton_mackinaw; 14:thorton_mackinaw_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h4921 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:chevalier_thrax; 14:chevalier_thrax_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h5118 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:archer_quartz; 14:archer_quartz_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h5320 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:brennan_apollo; 14:brennan_apollo_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h5555 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:chevalier_emperor; 14:chevalier_emperor_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h5752 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:villefort_alvarado; 14:villefort_alvarado_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h6017 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:thorton_galena_nomad; 14:thorton_galena_nomad_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h6214 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:quadra_type66; 14:quadra_type66_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h6411 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:mizutani_shion; 14:mizutani_shion_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h6600 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:yaiba_kusanagi; 14:yaiba_kusanagi_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h6807 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:thorton_colby_nomad; 14:thorton_colby_nomad_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h7056 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:mizutani_shion_nomad; 14:mizutani_shion_nomad_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h7253 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:arch; 14:arch_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h7560 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:quadra_type66_avenger; 14:quadra_type66_avenger_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h7757 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:herrera_outlaw; 14:herrera_outlaw_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h7954 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:quadra_type66_nomad; 14:quadra_type66_nomad_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h8243 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:rayfield_caliburn; 14:rayfield_caliburn_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h9809 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:mizutani_shion; 14:mizutani_shion_bought → 7:In |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h10179 / 14 | `vehicle_metaquest_choicehub.scene` | 6: CharacterManager; 6:Out → 14:mizutani_shion; 14:mizutani_shion_bought → 7:In |
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
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| `vehicle_metaquest_choicehub.scene` | makigai_maimai, chevalier_emperor, mizutani_shion, thorton_galena, thorton_mackinaw, villefort_alvarado, villefort_columbus, villefort_cortes, yaiba_kusanagi, thorton_colby, quadra_type66_nomad_ncu, archer_quartz, mahir_supron, herrera_outlaw, thorton_colby_pickup, archer_bandit, quadra_type66, arch, quadra_type66_avenger, rayfield_aerondight, brennan_apollo, thorton_galena_nomad, thorton_colby_nomad, rayfield_caliburn, mizutani_shion_nomad, quadra_turbo_r, chevalier_thrax, quadra_type66_nomad, quadra_turbo → makigai_maimai_bought, chevalier_emperor_bought, mizutani_shion_bought, thorton_galena_bought, thorton_mackinaw_bought, villefort_alvarado_bought, villefort_columbus_bought, villefort_cortes_bought, yaiba_kusanagi_bought, thorton_colby_bought, quadra_type66_nomad_ncu_bought, archer_quartz_bought, mahir_supron_bought, herrera_outlaw_bought, archer_bandit_bought, thorton_colby_pickup_bought, quadra_type66_bought, arch_bought, quadra_type66_avenger_bought, rayfield_aerondight_bought, brennan_apollo_bought, rayfield_caliburn_bought, thorton_galena_nomad_bought, thorton_colby_nomad_bought, mizutani_shion_nomad_bought, quadra_turbo_r_bought, chevalier_thrax_bought, quadra_type66_nomad_bought, quadra_turbo_bought | makigai_maimai; chevalier_emperor; villefort_cortes; thorton_mackinaw; villefort_alvarado; villefort_columbus; thorton_galena; yaiba_kusanagi; mizutani_shion; thorton_colby; quadra_turbo; quadra_type66_nomad_ncu; archer_quartz; mahir_supron; herrera_outlaw; thorton_colby_pickup; quadra_type66; chevalier_thrax; arch; rayfield_aerondight; brennan_apollo; rayfield_caliburn; thorton_galena_nomad; thorton_colby_nomad; quadra_type66_nomad; mizutani_shion_nomad; quadra_turbo_r; quadra_type66_avenger; archer_bandit; 145 nodes / 145 edges |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| `vehicle_metaquest_choicehub.scene / n6 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "224913275214", "difficulty": "MEDIUM"}}}} | 0:0 → 623:0:1 |
| `vehicle_metaquest_choicehub.scene / n10 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "238141522672", "difficulty": "MEDIUM"}}}} | 0:0 → 620:0:1 |
| `vehicle_metaquest_choicehub.scene / n15 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "211685270884", "difficulty": "MEDIUM"}}}} | 0:0 → 617:0:1 |
| `vehicle_metaquest_choicehub.scene / n20 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "226648066966", "difficulty": "EASY"}}}} | 0:0 → 535:0:1 |
| `vehicle_metaquest_choicehub.scene / n25 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "232287114639", "difficulty": "EASY"}}}} | 0:0 → 614:0:1 |
| `vehicle_metaquest_choicehub.scene / n30 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "229949616240", "difficulty": "MEDIUM"}}}} | 0:0 → 611:0:1 |
| `vehicle_metaquest_choicehub.scene / n35 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "245298516447", "difficulty": "EASY"}}}} | 0:0 → 608:0:1 |
| `vehicle_metaquest_choicehub.scene / n40 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "233415618274", "difficulty": "MEDIUM"}}}} | 0:0 → 605:0:1 |
| `vehicle_metaquest_choicehub.scene / n45 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "229216640373", "difficulty": "HARD"}}}} | 0:0 → 602:0:1 |
| `vehicle_metaquest_choicehub.scene / n50 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "221718838414", "difficulty": "MEDIUM"}}}} | 0:0 → 599:0:1 |
| `vehicle_metaquest_choicehub.scene / n63 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "250131570963", "difficulty": "MEDIUM"}}}} | 0:0 → 596:0:1 |
| `vehicle_metaquest_choicehub.scene / n69 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "220484392566", "difficulty": "MEDIUM"}}}} | 0:0 → 593:0:1 |
| `vehicle_metaquest_choicehub.scene / n71 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "220105694895", "difficulty": "MEDIUM"}}}} | 0:0 → 590:0:1 |
| `vehicle_metaquest_choicehub.scene / n74 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "213945172398", "difficulty": "HARD"}}}} | 0:0 → 587:0:1 |
| `vehicle_metaquest_choicehub.scene / n77 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "253313111519", "difficulty": "MEDIUM"}}}} | 0:0 → 584:0:1 |
| `vehicle_metaquest_choicehub.scene / n80 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "209308677937", "difficulty": "HARD"}}}} | 0:0 → 581:0:1 |
| `vehicle_metaquest_choicehub.scene / n83 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "187505012669", "difficulty": "HARD"}}}} | 0:0 → 578:0:1 |
| `vehicle_metaquest_choicehub.scene / n86 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "241855836507", "difficulty": "MEDIUM"}}}} | 0:0 → 575:0:1 |
| `vehicle_metaquest_choicehub.scene / n89 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "236044380235", "difficulty": "HARD"}}}} | 0:0 → 572:0:1 |
| `vehicle_metaquest_choicehub.scene / n92 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "228132484378", "difficulty": "EASY"}}}} | 0:0 → 569:0:1 |
| `vehicle_metaquest_choicehub.scene / n94 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "224744148688", "difficulty": "HARD"}}}} | 0:0 → 566:0:1 |
| `vehicle_metaquest_choicehub.scene / n97 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "251901414083", "difficulty": "MEDIUM"}}}} | 0:0 → 563:0:1 |
| `vehicle_metaquest_choicehub.scene / n100 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "249170124842", "difficulty": "MEDIUM"}}}} | 0:0 → 560:0:1 |
| `vehicle_metaquest_choicehub.scene / n128 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "240364847540", "difficulty": "MEDIUM"}}}} | 0:0 → 557:0:1 |
| `vehicle_metaquest_choicehub.scene / n131 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "215820942989", "difficulty": "MEDIUM"}}}} | 0:0 → 554:0:1 |
| `vehicle_metaquest_choicehub.scene / n153 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "231528567959", "difficulty": "MEDIUM"}}}} | 0:0 → 551:0:1 |
| `vehicle_metaquest_choicehub.scene / n156 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "234312714822", "difficulty": "MEDIUM"}}}} | 0:0 → 548:0:1 |
| `vehicle_metaquest_choicehub.scene / n163 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "203257819397", "difficulty": "HARD"}}}} | 0:0 → 545:0:1 |
| `vehicle_metaquest_choicehub.scene / n254 / 0` | [kup pojazd] (``) | {"bluelineCondition": {"$type": "questPaymentCondition", "type": {"$type": "questPaymentBalanced_ConditionType", "scriptCondition": {"$type": "PaymentBalanced_ScriptConditionType", "questAssignment": "221769267356", "difficulty": "HARD"}}}} | 0:0 → 542:0:1 |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| `arch_owned` | vehicle_metaquest_choicehub.scene / scene / 578 | vehicle_metaquest_choicehub.scene / scene / 421 |
| `archer_bandit_owned` | vehicle_metaquest_choicehub.scene / scene / 542 | vehicle_metaquest_choicehub.scene / scene / 501 |
| `archer_quartz_owned` | vehicle_metaquest_choicehub.scene / scene / 593 | vehicle_metaquest_choicehub.scene / scene / 291 |
| `brennan_apollo_owned` | vehicle_metaquest_choicehub.scene / scene / 569 | vehicle_metaquest_choicehub.scene / scene / 442 |
| `car_quest_delay` | vehicles_metaquest.questphase / h7188 / 33 | No reader in selected context |
| `carbought` | vehicles_metaquest.questphase / h7195 / 14; vehicles_metaquest.questphase / h7195 / 24 | No reader in selected context |
| `carbought_money_counter` | vehicle_metaquest_achievement.questphase / h0 / 55 | No reader in selected context |
| `chevalier_emperor_owned` | vehicle_metaquest_choicehub.scene / scene / 620 | vehicle_metaquest_choicehub.scene / scene / 336 |
| `chevalier_thrax_owned` | vehicle_metaquest_choicehub.scene / scene / 551 | vehicle_metaquest_choicehub.scene / scene / 288 |
| `herrera_outlaw_owned` | vehicle_metaquest_choicehub.scene / scene / 587 | vehicle_metaquest_choicehub.scene / scene / 403 |
| `mahir_supron_owned` | vehicle_metaquest_choicehub.scene / scene / 590 | vehicle_metaquest_choicehub.scene / scene / 272 |
| `makigai_maimai_owned` | vehicle_metaquest_choicehub.scene / scene / 623 | vehicle_metaquest_choicehub.scene / scene / 330 |
| `mizutani_shion_nomad_owned` | vehicle_metaquest_choicehub.scene / scene / 557 | vehicle_metaquest_choicehub.scene / scene / 469 |
| `mizutani_shion_owned` | vehicle_metaquest_choicehub.scene / scene / 617 | vehicle_metaquest_choicehub.scene / scene / 344 |
| `quadra_turbo_owned` | vehicle_metaquest_choicehub.scene / scene / 545 | vehicle_metaquest_choicehub.scene / scene / 491 |
| `quadra_turbo_r_owned` | vehicle_metaquest_choicehub.scene / scene / 554 | vehicle_metaquest_choicehub.scene / scene / 476 |
| `quadra_type66_avenger_owned` | vehicle_metaquest_choicehub.scene / scene / 575 | vehicle_metaquest_choicehub.scene / scene / 425 |
| `quadra_type66_nomad_owned` | vehicle_metaquest_choicehub.scene / scene / 548 | vehicle_metaquest_choicehub.scene / scene / 487 |
| `quadra_type66_owned` | vehicle_metaquest_choicehub.scene / scene / 581 | vehicle_metaquest_choicehub.scene / scene / 414 |
| `rayfield_aerondight_owned` | vehicle_metaquest_choicehub.scene / scene / 572 | vehicle_metaquest_choicehub.scene / scene / 435 |
| `rayfield_caliburn_owned` | vehicle_metaquest_choicehub.scene / scene / 566 | vehicle_metaquest_choicehub.scene / scene / 449 |
| `thorton_colby_nomad_owned` | vehicle_metaquest_choicehub.scene / scene / 560 | vehicle_metaquest_choicehub.scene / scene / 295 |
| `thorton_colby_owned` | vehicle_metaquest_choicehub.scene / scene / 599 | vehicle_metaquest_choicehub.scene / scene / 268 |
| `thorton_colby_pickup_owned` | vehicle_metaquest_choicehub.scene / scene / 584 | vehicle_metaquest_choicehub.scene / scene / 280 |
| `thorton_galena_nomad_owned` | vehicle_metaquest_choicehub.scene / scene / 563 | vehicle_metaquest_choicehub.scene / scene / 455 |
| `thorton_galena_owned` | vehicle_metaquest_choicehub.scene / scene / 535 | vehicle_metaquest_choicehub.scene / scene / 349 |
| `thorton_mackinaw_owned` | vehicle_metaquest_choicehub.scene / scene / 614 | vehicle_metaquest_choicehub.scene / scene / 284 |
| `vehicle_metaquest_website_quadra_type66_ncu_bought` | vehicle_metaquest_choicehub.scene / scene / 596 | vehicle_metaquest_choicehub.scene / scene / 388 |
| `vehicle_metaquest_website_thorton_galena_bought` | Producer outside selected context | vehicle_metaquest_choicehub.scene / scene / 20 |
| `villefort_alvarado_owned` | vehicle_metaquest_choicehub.scene / scene / 611 | vehicle_metaquest_choicehub.scene / scene / 303 |
| `villefort_columbus_owned` | vehicle_metaquest_choicehub.scene / scene / 608 | vehicle_metaquest_choicehub.scene / scene / 264 |
| `villefort_cortes_owned` | vehicle_metaquest_choicehub.scene / scene / 605 | vehicle_metaquest_choicehub.scene / scene / 368 |
| `yaiba_kusanagi_owned` | vehicle_metaquest_choicehub.scene / scene / 602 | vehicle_metaquest_choicehub.scene / scene / 377 |

## Exact gates, joins and cancellation

<details><summary>41 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `vehicle_metaquest_achievement.questphase / h0 / 26` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntry_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/vehicle_metaquest/herrera_outlaw","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Succeeded"}}}` | 0:Out → 26:In; 26:Out → 55:In |
| `vehicles_metaquest.questphase / h7195 / 25` | `questLogicalAndNodeDefinition` `{}` | 25:Out1 → 1:In; 27:Out → 25:In1; 29:Out → 25:In2 |
| `vehicles_metaquest.questphase / h7195 / 39` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","seconds":4}}}` | 14:Out → 39:In; 24:Out → 39:In; 39:Out → 36:In |
| `vehicles_metaquest.questphase / h7195 / 40` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#vehicles_metaquest_spwn_chevalier_emperor"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 3:Out → 40:In; 40:Out → 41:In |
| `vehicles_metaquest.questphase / h7195 / 42` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterSpawned_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#vehicles_metaquest_spwn_herrera_outlaw"},"comparisonParams":{"$type":"questComparisonParam","comparisonType":"Greater"}}}}` | 21:Out → 42:In; 42:Out → 43:In |
| `vehicles_metaquest.questphase / h7195 / 56` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleName":"Vehicle.v_standard3_chevalier_emperor_player"}}}` | 59:Out → 56:In; 60:Out → 56:In; 56:Out → 57:In |
| `vehicles_metaquest.questphase / h7195 / 57` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#vehicles_metaquest_spwn_chevalier_emperor"},"timeInterval":0.0,"onScreenTest":true}}}` | 56:Out → 57:In; 57:True → 59:In; 57:False → 58:In |
| `vehicles_metaquest.questphase / h7195 / 58` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#vehicles_metaquest_spwn_chevalier_emperor"},"childIsPlayer":true}}}` | 58:False → 33:In; 57:False → 58:In; 58:True → 59:In |
| `vehicles_metaquest.questphase / h7195 / 64` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questVehicleCondition","type":{"$type":"questVehicleSpawned_ConditionType","vehicleType":"SpecificVehicle","vehicleName":"Vehicle.v_sport1_herrera_outlaw_player"}}}` | 63:Out → 64:In; 67:Out → 64:In; 64:Out → 65:In |
| `vehicles_metaquest.questphase / h7195 / 65` | `questConditionNodeDefinition` `{"condition":{"$type":"questSystemCondition","type":{"$type":"questCameraFocus_ConditionType","objectRef":{"$type":"gameEntityReference","reference":"#vehicles_metaquest_spwn_herrera_outlaw"},"timeInterval":0.0,"onScreenTest":true}}}` | 64:Out → 65:In; 65:True → 67:In; 65:False → 66:In |
| `vehicles_metaquest.questphase / h7195 / 66` | `questConditionNodeDefinition` `{"condition":{"$type":"questCharacterCondition","type":{"$type":"questCharacterMount_ConditionType","parentRef":{"$type":"gameEntityReference","reference":"#vehicles_metaquest_spwn_herrera_outlaw"},"childIsPlayer":true}}}` | 66:False → 35:In; 65:False → 66:In; 66:True → 67:In |
| `vehicles_metaquest_new.questphase / h21 / 23` | `questConditionNodeDefinition` `{"condition":{"$type":"questJournalCondition","type":{"$type":"questJournalEntryState_ConditionType","path":{"$type":"gameJournalPath","realPath":"quests/vehicle_metaquest/herrera_outlaw","fileEntryIndex":2,"className":"gameJournalQuest"},"state":"Active"}}}` | 0:Out → 23:In; 23:True → 50:Inactive |
| `vehicle_metaquest_choicehub.scene / scene / 264` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"villefort_columbus_owned"}}}` | 34:0:0 → 264:0:1; 264:0:0 → 37:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 268` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"thorton_colby_owned"}}}` | 49:0:0 → 268:0:1; 268:0:0 → 51:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 272` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mahir_supron_owned"}}}` | 70:0:0 → 272:0:1; 272:0:0 → 72:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 280` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"thorton_colby_pickup_owned"}}}` | 76:0:0 → 280:0:1; 280:0:0 → 78:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 284` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"thorton_mackinaw_owned"}}}` | 24:0:0 → 284:0:1; 284:0:0 → 27:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 288` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"chevalier_thrax_owned"}}}` | 152:0:0 → 288:0:1; 288:0:0 → 154:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 291` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"archer_quartz_owned"}}}` | 67:0:0 → 291:0:1; 291:0:0 → 68:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 295` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"thorton_colby_nomad_owned"}}}` | 99:0:0 → 295:0:1; 295:0:0 → 101:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 303` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"villefort_alvarado_owned"}}}` | 29:0:0 → 303:0:1; 303:0:0 → 32:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 330` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"makigai_maimai_owned"}}}` | 1:0:0 → 330:0:1; 330:0:0 → 2:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 336` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"chevalier_emperor_owned"}}}` | 9:0:0 → 336:0:1; 336:0:0 → 12:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 344` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mizutani_shion_owned"}}}` | 14:0:0 → 344:0:1; 344:0:0 → 17:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 349` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"thorton_galena_owned"}}}` | 19:0:0 → 349:0:1; 349:0:0 → 22:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 368` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"villefort_cortes_owned"}}}` | 39:0:0 → 368:0:1; 368:0:0 → 42:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 377` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"yaiba_kusanagi_owned"}}}` | 44:0:0 → 377:0:1; 377:0:0 → 47:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 388` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"vehicle_metaquest_website_quadra_type66_ncu_bought"}}}` | 62:0:0 → 388:0:1; 388:0:0 → 64:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 403` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"herrera_outlaw_owned"}}}` | 73:0:0 → 403:0:1; 403:0:0 → 75:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 414` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"quadra_type66_owned"}}}` | 79:0:0 → 414:0:1; 414:0:0 → 81:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 421` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"arch_owned"}}}` | 82:0:0 → 421:0:1; 421:0:0 → 84:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 425` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"quadra_type66_avenger_owned"}}}` | 85:0:0 → 425:0:1; 425:0:0 → 87:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 435` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rayfield_aerondight_owned"}}}` | 88:0:0 → 435:0:1; 435:0:0 → 90:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 442` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"brennan_apollo_owned"}}}` | 91:0:0 → 442:0:1; 442:0:0 → 93:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 449` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"rayfield_caliburn_owned"}}}` | 125:0:0 → 449:0:1; 449:0:0 → 95:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 455` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"thorton_galena_nomad_owned"}}}` | 96:0:0 → 455:0:1; 455:0:0 → 98:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 469` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"mizutani_shion_nomad_owned"}}}` | 127:0:0 → 469:0:1; 469:0:0 → 129:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 476` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"quadra_turbo_r_owned"}}}` | 130:0:0 → 476:0:1; 476:0:0 → 132:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 487` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"quadra_type66_nomad_owned"}}}` | 155:0:0 → 487:0:1; 487:0:0 → 157:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 491` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"quadra_turbo_owned"}}}` | 162:0:0 → 491:0:1; 491:0:0 → 164:0:0 |
| `vehicle_metaquest_choicehub.scene / scene / 501` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questFactsDBCondition","type":{"$type":"questVarComparison_ConditionType","factName":"archer_bandit_owned"}}}` | 251:0:0 → 501:0:1; 501:0:0 → 252:0:0 |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `actor_readiness` | vehicles_metaquest.questphase / h7195 / 40; vehicles_metaquest.questphase / h7195 / 42 | community/entry or actor reference + count policy → actor available. Test already-spawned, delayed and missing actors before speech or commands. |
| `choice_gate` | vehicle_metaquest_choicehub.scene / scene / 10; vehicle_metaquest_choicehub.scene / scene / 100; vehicle_metaquest_choicehub.scene / scene / 128; vehicle_metaquest_choicehub.scene / scene / 131; +25 locations in catalogue.json | choice + eligibility predicates + commit effects → selected option or defer/interruption. Keep knowledge, skill eligibility and persistent decision separate; test return to the choice. |
| `conditional_route` | vehicle_metaquest_choicehub.scene / scene / 20; vehicle_metaquest_choicehub.scene / scene / 264; vehicle_metaquest_choicehub.scene / scene / 268; vehicle_metaquest_choicehub.scene / scene / 272; +26 locations in catalogue.json | fact + exact comparison + branch sockets → selected branch. Fact dependencies are not execution edges; identify producers and cancellation. |
| `journal_transition` | vehicles_metaquest.questphase / h7188 / 27; vehicles_metaquest.questphase / h7188 / 5; vehicles_metaquest.questphase / h7188 / 7; vehicles_metaquest.questphase / h7195 / 30; +6 locations in catalogue.json | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `mount_state` | vehicles_metaquest.questphase / h7195 / 58; vehicles_metaquest.questphase / h7195 / 66 | parent vehicle/puppet + child + role/event → mount/unmount condition. Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness. |
| `parallel_join` | vehicles_metaquest.questphase / h7195 / 25 | named branch completion signals + reset policy → all required inputs observed. Test either completion order, early events, interruption and save/load at the join. |
| `persistent_decision` | vehicle_metaquest_achievement.questphase / h0 / 55; vehicle_metaquest_choicehub.scene / scene / 535; vehicle_metaquest_choicehub.scene / scene / 542; vehicle_metaquest_choicehub.scene / scene / 545; +29 locations in catalogue.json | namespaced fact + explicit write mode/value → durable state update. Separate scene-local presentation facts from public outcome state and review omitted defaults. |
| `realtime_delay` | vehicles_metaquest.questphase / h7195 / 39 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |
| `reward_commit` | vehicles_metaquest.questphase / h7195 / 46; vehicles_metaquest.questphase / h7195 / 47 | reward record + eligibility + once-only commit → reward delivered/committed. Verify inventory/currency and objective state; prevent repeated awards after load. |
| `scene_interface` | vehicles_metaquest.questphase / h7195 / 22; vehicles_metaquest.questphase / h7195 / 4 | scene + entry + actor/marker bindings → named exits and cancellation. Validate every consumed entry/exit and distinguish terminating from notification outputs. |
| `vehicle_control` | vehicles_metaquest.questphase / h7195 / 27; vehicles_metaquest.questphase / h7195 / 29; vehicles_metaquest.questphase / h7195 / 41; vehicles_metaquest.questphase / h7195 / 43; +10 locations in catalogue.json | vehicle reference + typed operation + world route → operation-specific result. Vehicle spawning, seats, driving, arrival and cleanup have separate owners. |
| `weighted_branch` | vehicles_metaquest.questphase / h7195 / 36 | ordered output weights + explicit route bindings → one authored weighted output. Preserve output ordering, reset scope and persistence; compose difficulty and timing as separate gates. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicle_metaquest_achievement.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` | content candidate; journal anchor | `base-shared` |
| `base\open_world\vendors\vehicles_metaquest\scenes\vehicle_metaquest_choicehub.scene` | content candidate; forward dependency | `base-shared` |

Evidence shards for this dossier (including parent context): [base-ma-bls-ina-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-07.json.gz), [base-ma-bls-ina-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-08.json.gz), [base-ma-bls-ina-se1-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-bls-ina-se1-22.json.gz), [base-ma-cct-dtn-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-03.json.gz), [base-ma-cct-dtn-07](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-cct-dtn-07.json.gz), [base-ma-hey-spr-04](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-04.json.gz), [base-ma-hey-spr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-hey-spr-06.json.gz), [base-ma-pac-cvi-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-08.json.gz), [base-ma-pac-cvi-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-pac-cvi-15.json.gz), [base-ma-std-arr-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-arr-06.json.gz), [base-ma-std-rcr-11](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-std-rcr-11.json.gz), [base-ma-wat-kab-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-02.json.gz), [base-ma-wat-kab-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-kab-08.json.gz), [base-ma-wat-lch-06](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-lch-06.json.gz), [base-ma-wat-nid-03](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-03.json.gz), [base-ma-wat-nid-15](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-15.json.gz), [base-ma-wat-nid-22](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ma-wat-nid-22.json.gz), [base-mq000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq000.json.gz), [base-mq001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq001.json.gz), [base-mq003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq003.json.gz), [base-mq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq006.json.gz), [base-mq007](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq007.json.gz), [base-mq008](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq008.json.gz), [base-mq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq011.json.gz), [base-mq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq012.json.gz), [base-mq013](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq013.json.gz), [base-mq014](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq014.json.gz), [base-mq015](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq015.json.gz), [base-mq016](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq016.json.gz), [base-mq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq017.json.gz), [base-mq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq018.json.gz), [base-mq019](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq019.json.gz), [base-mq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq021.json.gz), [base-mq022](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq022.json.gz), [base-mq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq023.json.gz), [base-mq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq024.json.gz), [base-mq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq025.json.gz), [base-mq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq026.json.gz), [base-mq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq028.json.gz), [base-mq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq030.json.gz), [base-mq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq032.json.gz), [base-mq033](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq033.json.gz), [base-mq035](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq035.json.gz), [base-mq037](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq037.json.gz), [base-mq038](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq038.json.gz), [base-mq040](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq040.json.gz), [base-mq041](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq041.json.gz), [base-mq048](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq048.json.gz), [base-mq055](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mq055.json.gz), [base-mws-wat-08](../../../../../reference/quests/deep-dives/all-quests/evidence/base-mws-wat-08.json.gz), [base-q000](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q000.json.gz), [base-q001](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q001.json.gz), [base-q003](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q003.json.gz), [base-q004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q004.json.gz), [base-q005](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q005.json.gz), [base-q101](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q101.json.gz), [base-q103](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q103.json.gz), [base-q105](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q105.json.gz), [base-q110](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q110.json.gz), [base-q112](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q112.json.gz), [base-q113](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q113.json.gz), [base-q114](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q114.json.gz), [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-q201](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q201.json.gz), [base-q202](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q202.json.gz), [base-q203](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q203.json.gz), [base-q204](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q204.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [base-sq004](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq004.json.gz), [base-sq006](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq006.json.gz), [base-sq011](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq011.json.gz), [base-sq012](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq012.json.gz), [base-sq017](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq017.json.gz), [base-sq018](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq018.json.gz), [base-sq021](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq021.json.gz), [base-sq023](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq023.json.gz), [base-sq024](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq024.json.gz), [base-sq025](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq025.json.gz), [base-sq026](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq026.json.gz), [base-sq027](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq027.json.gz), [base-sq028](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq028.json.gz), [base-sq029](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq029.json.gz), [base-sq030](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq030.json.gz), [base-sq031](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq031.json.gz), [base-sq032](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sq032.json.gz), [base-sts-hey-rey-02](../../../../../reference/quests/deep-dives/all-quests/evidence/base-sts-hey-rey-02.json.gz), [base-ue-metro](../../../../../reference/quests/deep-dives/all-quests/evidence/base-ue-metro.json.gz), [ep1-mq301](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq301.json.gz), [ep1-mq303](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq303.json.gz), [ep1-mq304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq304.json.gz), [ep1-mq305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mq305.json.gz), [ep1-mws-cz-03](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-mws-cz-03.json.gz), [ep1-q304](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q304.json.gz), [ep1-q305](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q305.json.gz), [ep1-q306](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q306.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

31 repeated typed/socket path signatures in this selected graph context; 1 distinct direct resource identities; 1 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `808c42396a9735fe3a65` | `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7195 / 18 -> 21 -> 42 | questInputNodeDefinition -> questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]; Out -> In; Out -> In |
| `62513b1c2fdaf0c74a1c` | `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7188 / 7 -> 27 -> 33 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType]; Out -> Active; Out -> In |
| `bff957bf33a10413a685` | `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7195 / 3 -> 40 -> 41 | questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType] -> questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam] -> questVehicleNodeDefinition[questToggleDoor_NodeType]; Out -> In; Out -> In |
| `05da58ffa41a47aeb533` | `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7188 / 5 -> 7 -> 27 | questJournalNodeDefinition[questJournalEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> Active; Out -> Active |
| `450070a422af0dc83c00` | `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7195 / 41 -> 52 -> 48 | questVehicleNodeDefinition[questToggleDoor_NodeType] -> questVehicleNodeDefinition[questSetImmovable_NodeType] -> questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]; Out -> In; Out -> In |
| `c8edfa02eaa729f5bae9` | `base\open_world\vendors\vehicles_metaquest\scenes\vehicle_metaquest_choicehub.scene` / scene / 34 -> 264 -> 37 | scnStartNode[scnNodeId] -> questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType] -> scnEndNode[scnNodeId]; 0:0 -> 0:1; 0:0 -> 0:0 |
| `3081631a4b93918af715` | `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase` / h21 / 0 -> 23 -> 50 | questInputNodeDefinition -> questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType] -> questJournalNodeDefinition[questJournalQuestEntry_NodeType]; Out -> In; True -> Inactive |
| `d05eb5010cfeefc29656` | `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7195 / 40 -> 41 -> 52 | questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam] -> questVehicleNodeDefinition[questToggleDoor_NodeType] -> questVehicleNodeDefinition[questSetImmovable_NodeType]; Out -> In; Out -> In |
| `5d73a2f49ed5d74832e0` | `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7195 / 14 -> 46 -> 61 | questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questRewardManagerNodeDefinition[questGiveReward_NodeType] -> questDeletionMarkerNodeDefinition; Out -> In; Out -> In |
| `6af8b80a229195c55094` | `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7195 / 30 -> 14 -> 39 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; Out -> In; Out -> In |
| `6e95d8c6c6e3a1379384` | `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7195 / 30 -> 14 -> 46 | questJournalNodeDefinition[questJournalQuestEntry_NodeType] -> questFactsDBManagerNodeDefinition[questSetVar_NodeType] -> questRewardManagerNodeDefinition[questGiveReward_NodeType]; Out -> In; Out -> In |
| `48448adc7ed0a82b2da1` | `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7195 / 39 -> 36 -> 38 | questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> questRandomizerNodeDefinition -> questJournalNodeDefinition[questJournalEntry_NodeType]; Out -> In; Out2 -> Active |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| `base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase` / h7188 / 2 | `h7195` | [{"$type":"questInputNodeDefinition","id":0,"socketName":"chevalier_emperor"},{"$type":"questOutputNodeDefinition","id":1,"socketName":"Bought"},{"$type":"questInputNodeDefinition","id":18,"socketName":"herrera_outlaw"}] |

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
| `base\open_world\vendors\vehicles_metaquest\vehicles_metaquest.gamedef` | content candidate | base\open_world\vendors\vehicles_metaquest\vehicles_metaquest.quest |
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
| `base\open_world\vendors\vehicles_metaquest\scenes\vehicle_metaquest_choicehub.scene` | scene flow | content/basegame_4_gamedata.archive; structurally indexed |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| `arch_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 129; 1 total source locations in compressed evidence |
| `archer_bandit_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 130; base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h2397 / 19; 2 total source locations in compressed evidence |
| `archer_quartz_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 131; 1 total source locations in compressed evidence |
| `brennan_apollo_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 132; 1 total source locations in compressed evidence |
| `car_quest_delay` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase / h66 / 43; base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase / h66 / 45; base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase / h1568 / 34; base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase / h1568 / 36; 11 total source locations in compressed evidence |
| `carbought` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase / h0 / 337; base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase / h75 / 13; base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase / h75 / 25; base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest.questphase / h535 / 11; 73 total source locations in compressed evidence |
| `carbought_money_counter` | base\open_world\vendors\vehicles_metaquest\phases\vehicle_metaquest_achievement.questphase / h0 / 31; base\open_world\vendors\vehicles_metaquest\phases\vehicle_metaquest_achievement.questphase / h0 / 32; base\open_world\vendors\vehicles_metaquest\phases\vehicle_metaquest_achievement.questphase / h0 / 33; base\open_world\vendors\vehicles_metaquest\phases\vehicle_metaquest_achievement.questphase / h0 / 34; 27 total source locations in compressed evidence |
| `chevalier_emperor_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 133; 1 total source locations in compressed evidence |
| `chevalier_thrax_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 134; 1 total source locations in compressed evidence |
| `herrera_outlaw_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 135; 1 total source locations in compressed evidence |
| `mahir_supron_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 136; 1 total source locations in compressed evidence |
| `makigai_maimai_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 137; 1 total source locations in compressed evidence |
| `mizutani_shion_nomad_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 139; 1 total source locations in compressed evidence |
| `mizutani_shion_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 138; 1 total source locations in compressed evidence |
| `quadra_turbo_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 140; 1 total source locations in compressed evidence |
| `quadra_type66_avenger_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 142; 1 total source locations in compressed evidence |
| `quadra_type66_nomad_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 143; 1 total source locations in compressed evidence |
| `quadra_type66_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 141; 1 total source locations in compressed evidence |
| `rayfield_aerondight_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 145; 1 total source locations in compressed evidence |
| `rayfield_caliburn_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 146; 1 total source locations in compressed evidence |
| `thorton_colby_nomad_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 148; 1 total source locations in compressed evidence |
| `thorton_colby_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 147; 1 total source locations in compressed evidence |
| `thorton_colby_pickup_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 149; 1 total source locations in compressed evidence |
| `thorton_galena_nomad_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 151; 1 total source locations in compressed evidence |
| `thorton_galena_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 150; 1 total source locations in compressed evidence |
| `thorton_mackinaw_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 152; 1 total source locations in compressed evidence |
| `vehicle_metaquest_website_quadra_type66_ncu_bought` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h2703 / 47; 1 total source locations in compressed evidence |
| `vehicle_metaquest_website_thorton_galena_bought` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h3078 / 31; 1 total source locations in compressed evidence |
| `villefort_alvarado_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 153; 1 total source locations in compressed evidence |
| `villefort_columbus_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 154; 1 total source locations in compressed evidence |
| `villefort_cortes_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 155; 1 total source locations in compressed evidence |
| `yaiba_kusanagi_owned` | base\open_world\vendors\vehicles_metaquest\phases\vehicles_metaquest_new.questphase / h21 / 156; 1 total source locations in compressed evidence |

NodeRef uses: 84; TweakDB binding uses: 60. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| `base\open_world\vendors\vehicles_metaquest\scenes\vehicle_metaquest_choicehub.scene` | 0 / 0 |  |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
