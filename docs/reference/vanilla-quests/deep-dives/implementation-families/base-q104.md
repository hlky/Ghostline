# base-q104

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\part1\q104\q104_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\part1\q104\q104_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\part1\q104\q104_quest_bugfixes.questphase` | repair | 11 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_airstrip_combat.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_arasaka_av.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_arasaka_av_operators.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_av_drones.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_av_pilot.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_crashed_av.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_fake_takemura.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_gas_station_owner.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_gas_station_paramedic.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_gas_station_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_mitch_vehicle.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_nomads_arrive_background.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_panam_bike.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_panam_drone.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_petrochem_gas_station.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_power_plant_drones.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\communities\q104_tracking_vehicles.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\phases\combat\q104_06a_gas_station_combat.questphase` | content candidate | 8 / 0 |  |
| `base\quest\main_quests\part1\q104\phases\combat\q104_airstrip_combat.questphase` | content candidate | 1 / 0 | base\quest\main_quests\part1\q104\scenes\q104_06_following_tracks.scene |
| `base\quest\main_quests\part1\q104\phases\combat\q104_av_crashsite_combat.questphase` | content candidate | 1 / 0 |  |
| `base\quest\main_quests\part1\q104\phases\combat\q104_av_crashsite_gameplay.questphase` | content candidate | 4 / 0 |  |
| `base\quest\main_quests\part1\q104\phases\combat\q104_powerplant_combat.questphase` | content candidate | 1 / 0 | base\quest\main_quests\part1\q104\scenes\q104_02a_breaking_antenna.scene |
| `base\quest\main_quests\part1\q104\phases\debug\q104_chicken.questphase` | test/debug | 1 / 0 |  |
| `base\quest\main_quests\part1\q104\phases\debug\q104_debug_setup.questphase` | test/debug | 1 / 0 |  |
| `base\quest\main_quests\part1\q104\phases\debug\temp_heal_player.questphase` | test/debug | 1 / 0 |  |
| `base\quest\main_quests\part1\q104\phases\q104_02_power_plant.questphase` | content candidate | 4 / 0 | base\quest\main_quests\part1\q104\phases\combat\q104_powerplant_combat.questphase; base\quest\main_quests\part1\q104\scenes\q104_02a_breaking_antenna.scene |
| `base\quest\main_quests\part1\q104\phases\q104_attacking_av.questphase` | content candidate | 3 / 0 | base\quest\main_quests\part1\q104\scenes\q104_02_av_shotdown.scene; base\quest\main_quests\part1\q104\scenes\q104_02a_breaking_antenna.scene |
| `base\quest\main_quests\part1\q104\phases\q104_av_crash_site.questphase` | content candidate | 15 / 0 | base\quest\main_quests\part1\q104\phases\combat\q104_av_crashsite_combat.questphase; base\quest\main_quests\part1\q104\phases\combat\q104_av_crashsite_gameplay.questphase; base\quest\main_quests\part1\q104\phases\subphases\q104_av_crash_site_setup.questphase; base\quest\main_quests\part1\q104\scenes\q104_04_nomad_hurt.scene; base\quest\main_quests\part1\q104\scenes\q104_05_av_debris.scene |
| `base\quest\main_quests\part1\q104\phases\q104_chasing_av.questphase` | content candidate | 11 / 0 | base\quest\main_quests\part1\q104\scenes\q104_02_av_shotdown.scene; base\quest\main_quests\part1\q104\scenes\q104_03_av_chasing.scene |
| `base\quest\main_quests\part1\q104\phases\q104_followup.questphase` | content candidate | 1 / 0 |  |
| `base\quest\main_quests\part1\q104\phases\q104_gas_station.questphase` | content candidate | 14 / 0 | base\quest\main_quests\part1\q104\phases\combat\q104_06a_gas_station_combat.questphase; base\quest\main_quests\part1\q104\scenes\q104_06_following_tracks.scene; base\quest\main_quests\part1\q104\scenes\q104_07_gas_station_chats.scene; base\quest\main_quests\part1\q104\scenes\q104_07a_gas_station_infiltration.scene; base\quest\main_quests\part1\q104\scenes\q104_07b_haru_found.scene; base\quest\main_quests\part1\q104\scenes\q104_07c_nomads_arrive.scene |
| `base\quest\main_quests\part1\q104\phases\q104_motel.questphase` | content candidate | 4 / 0 | base\quest\main_quests\part1\q104\scenes\q104_08_courier_talks.scene |
| `base\quest\main_quests\part1\q104\phases\q104_preparations.questphase` | content candidate | 7 / 0 | base\quest\main_quests\part1\q104\phases\q104_02_power_plant.questphase; base\quest\main_quests\part1\q104\scenes\q104_01a_roadhouse_meeting.scene; base\quest\main_quests\part1\q104\scenes\q104_01b_calibration.scene |
| `base\quest\main_quests\part1\q104\phases\q104_tracking_av.questphase` | content candidate | 15 / 0 | base\quest\main_quests\part1\q104\phases\combat\q104_airstrip_combat.questphase; base\quest\main_quests\part1\q104\scenes\q104_05_av_debris.scene; base\quest\main_quests\part1\q104\scenes\q104_06_following_tracks.scene |
| `base\quest\main_quests\part1\q104\phases\subphases\q104_av_crash_site_setup.questphase` | content candidate | 1 / 0 |  |
| `base\quest\main_quests\part1\q104\q104.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q104\q104.quest` | content candidate | 1 / 0 | base\quest\holocalls\holocall_initializers.questphase; base\quest\main_quests\part1\q104\phases\debug\q104_chicken.questphase; base\quest\main_quests\part1\q104\phases\debug\q104_debug_setup.questphase; base\quest\main_quests\part1\q104\q104.questphase; base\quest\main_quests\part1\q104\test\q104_chicken_test.scene |
| `base\quest\main_quests\part1\q104\q104.questphase` | content candidate | 11 / 0 | base\quest\main_quests\part1\q104\phases\q104_attacking_av.questphase; base\quest\main_quests\part1\q104\phases\q104_av_crash_site.questphase; base\quest\main_quests\part1\q104\phases\q104_chasing_av.questphase; base\quest\main_quests\part1\q104\phases\q104_gas_station.questphase; base\quest\main_quests\part1\q104\phases\q104_motel.questphase; base\quest\main_quests\part1\q104\phases\q104_preparations.questphase; base\quest\main_quests\part1\q104\phases\q104_tracking_av.questphase; base\quest\side_quests\sq032\phases\sq032_tapeworm_setup.questphase |
| `base\quest\main_quests\part1\q104\scenes\q104_01a_roadhouse_meeting.scene` | content candidate | 0 / 157 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_01b_calibration.scene` | content candidate | 0 / 293 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_02_av_shotdown.scene` | content candidate | 0 / 142 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_02a_breaking_antenna.scene` | content candidate | 0 / 130 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_03_av_chasing.scene` | content candidate | 0 / 60 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_04_nomad_hurt.scene` | content candidate | 0 / 112 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_05_av_debris.scene` | content candidate | 0 / 336 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_06_following_tracks.scene` | content candidate | 0 / 93 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_07_gas_station_chats.scene` | content candidate | 0 / 39 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_07a_gas_station_infiltration.scene` | content candidate | 0 / 18 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_07b_haru_found.scene` | content candidate | 0 / 121 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_07c_nomads_arrive.scene` | content candidate | 0 / 224 |  |
| `base\quest\main_quests\part1\q104\scenes\q104_08_courier_talks.scene` | content candidate | 0 / 394 |  |
| `base\quest\main_quests\part1\q104\test\q104_chicken_test.scene` | test/debug | 0 / 45 |  |

## Journal paths observed in these resources

- `contacts/panam`
- `contacts/panam/q104_follow_up/01_msg_panam_follow`
- `contacts/panam/q104_follow_up/02_msg_panam_open`
- `contacts/panam/q104_follow_up/03_ch_opening`
- `contacts/panam/q104_follow_up/03_ch_opening/03_ch_a_ok`
- `contacts/panam/q104_follow_up/03_ch_opening/03_ch_b_v_comments`
- `contacts/panam/q104_follow_up/04_panam_continues`
- `contacts/panam/q104_follow_up/04a_panam_furious`
- `contacts/panam/q104_follow_up/05_v_answers`
- `contacts/panam/q104_follow_up_no_crash_site/01_msg_panam_follow_bad`
- `contacts/panam/q104_follow_up_no_crash_site/02_msg_panam_bad_2`
- `contacts/panam/q104_follow_up_no_crash_site/03_ch_v_responds`
- `contacts/panam/q104_follow_up_no_crash_site/03_ch_v_responds/03a_v_apologies`
- `contacts/panam/q104_follow_up_no_crash_site/04a_panam_understands`
- `contacts/panam/q104_follow_up_no_crash_site/04b_panam_worried`
- `contacts/panam/q104_follow_up_no_crash_site/05_v_thanks`
- `contacts/player`
- `contacts/takemura`
- `quests/main_quest/act_01/q104_01_sabotage`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/calibrate_turret`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/calibrate_turret/mp_1`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/calibrate_turret/mp_2`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/calibrate_turret/mp_3`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/car1`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/drive`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/drive_panam_hill`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/go_bottom_bunker1`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/meet_panam`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/meet_panam/mp_garage`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/meet_panam/mp_garage_guidance`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/meet_panam/mp_wait`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/meet_panam/q104_description`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/plant_security`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/plant_security/mp_drone_1`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/plant_security/mp_drone_2`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/plant_security/mp_drone_3`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/plant_security/mp_drone_4`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/plug_in`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/shoot_av`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/talk_panam`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/talk_panam/mp_garage_guidance`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/talk_panam/panam`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/talk_panam1`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/terminal_control`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/terminal_control/mp_terminal`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/terminal_control/mp_terminal1`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/terminal_control/mp_terminal2`
- `quests/main_quest/act_01/q104_01_sabotage/preparations/wait_for_av`
- `quests/main_quest/act_01/q104_02_av_chase`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/chase_av`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/chase_av/q104_02_description`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/deal_with_drones`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/deal_with_drones/drone_base_01`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/deal_with_drones/drone_base_02`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/deal_with_drones/drone_base_03`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/deal_with_drones/q104_02_description`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/drive_canyon`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/drive_canyon/q104_02_description`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/follow_av`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/follow_av/av_mp`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/follow_av/q104_after_crash_description`
- `quests/main_quest/act_01/q104_02_av_chase/av_chase/panam_patch`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/airstrip_oil_tracks`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/airstrip_oil_tracks/mp_airstrip_tracks_001`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/airstrip_oil_tracks/mp_airstrip_tracks_002`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/airstrip_oil_tracks/mp_airstrip_tracks_003`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/airstrip_oil_tracks/mp_airstrip_tracks_004`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/call_takemura`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/call_takemura/phone`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/car_area`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/carry_haru_outside`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/confront_anders`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/deal_av_turret`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/disconnect_drone`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/find_courier_gas`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/find_courier_gas_precise`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_pan_gas`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_panam`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks/mp_tracks_001`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks/mp_tracks_002`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks/mp_tracks_003`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks_post_airstrip`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks_post_airstrip/mp_tracks_002`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks_post_airstrip/mp_tracks_003`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks_post_airstrip/mp_tracks_004`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks_post_airstrip/mp_tracks_005`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/follow_tracks_post_airstrip/mp_tracks_006`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/gas_station_vantage_point`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/get_info_from_mitch`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/get_inside_av`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/get_on_bike_tracking`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/kill_petrochem_av`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/leave_roadhouse`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_kill_airstrip_kangtao`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_kill_airstrip_kangtao/mp_enemy_01`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_kill_airstrip_kangtao/mp_enemy_02`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_kill_airstrip_kangtao/mp_enemy_03`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_kill_airstrip_kangtao/mp_enemy_04`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_scan_aldecados`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_scan_drones`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_scan_mitch`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_scan_mitch/mitch`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_scan_turret`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_scan_zetatech`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_take_bike`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_take_bike/mp_bike_nomad`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/optional_take_bike/mp_bike_scorpion`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/pickup_haru`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/put_haru_on_bike`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/reach_gas_station`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/recon_crashsite_w_panam`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/resolve_hostage_situation`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/scan_tire_tracks`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/subdue_haru`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/talk_panam_gas_station`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/talk_with_courier`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/tracking_plan`
- `quests/main_quest/act_01/q104_02_av_chase/finding_courier/wait_panam`
- `quests/main_quest/act_01/q104_courier/finding_courier/recon_crashsite_w_panam`
- `quests/main_quest/act_01/q105_02_jigjig`
- `quests/main_quest/act_01/q105_03_braindance_studio`
- `quests/main_quest/act_01/q105_04_judys`
- `quests/main_quest/act_01/q105_dollhouse`
- `quests/main_quest/act_01/q110_01_voodooboys`
- `quests/main_quest/act_01/q110_03_cyberspace`
- `quests/main_quest/act_01/q110_voodoo`
- `quests/main_quest/act_01/q112_01_old_friend`
- `quests/main_quest/act_01/q112_02_industrial_park`
- `quests/main_quest/act_01/q112_03_dashi_parade`
- `quests/main_quest/act_01/q112_04_hideout`
- `quests/side_quest/sq031_rogue`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 35 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 19 |
| `questAudioNodeDefinition[questRadioSongNodeType]` | 1 |
| `questCharacterManagerNodeDefinition` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_AssignSquad,questCharacterManagerCombat_NodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_EquipWeapon,questCharacterManagerCombat_NodeType]` | 11 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 11 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 10 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_HealPlayer,questCharacterManagerParameters_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAnimset]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 19 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 12 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 20 |
| `questCombatNodeDefinition` | 30 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 12 |
| `questCombatNodeDefinition[questCombatNodeParams_PrimaryWeapon]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_ShootAt]` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 4 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterGender_CondtionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 7 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 82 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 7 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 43 |
| `questConditionNodeDefinition[questLifePath_ConditionType,questStatsCondition,questUniversalRef]` | 1 |
| `questConditionNodeDefinition[questTimeCondition,questTimePeriod_ConditionType]` | 3 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_ControlCrowd]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 7 |
| `questCutControlNodeDefinition` | 18 |
| `questDeletionMarkerNodeDefinition` | 51 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerMountPuppet_NodeType]` | 3 |
| `questEntityManagerNodeDefinition[questEntityManagerSetAttachment_NodeType,questEntityManagerSetAttachment_ToActor]` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 2 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleMirrorsArea_NodeType]` | 2 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 6 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 26 |
| `questEventManagerNodeDefinition` | 125 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 15 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 141 |
| `questFlowControlNodeDefinition` | 10 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 20 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 29 |
| `questGameManagerNodeDefinition[questRumble_NodeType]` | 2 |
| `questInputNodeDefinition` | 156 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 4 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 121 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questSetLootInteractionAccess_NodeType]` | 1 |
| `questItemManagerNodeDefinition[questUniversalRef,questUseWeapon_NodeType]` | 6 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 12 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 180 |
| `questJournalNodeDefinition[questJournalTrackQuest_NodeType]` | 12 |
| `questLogicalAndNodeDefinition` | 61 |
| `questLogicalHubNodeDefinition` | 33 |
| `questLogicalXorNodeDefinition` | 19 |
| `questLookAtDrivenTurnsNode` | 3 |
| `questMappinManagerNodeDefinition` | 61 |
| `questMiscAICommandNode` | 31 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 6 |
| `questMovePuppetNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questObservableUniversalRef,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 6 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 10 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 1 |
| `questMovePuppetNodeDefinition[questPatrolParams]` | 18 |
| `questOutputNodeDefinition` | 121 |
| `questPauseConditionNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 14 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 19 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterCover_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterEquippedItem_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 15 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 18 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 51 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 51 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterTriggeredCombatInSecuritySystem_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questLogicalCondition,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 7 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 26 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 45 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questSystemCondition]` | 5 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questMenuState_ConditionType,questTimeCondition,questTimePeriod_ConditionType,questTriggerCondition,questUICondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTimeCondition,questTimePeriod_ConditionType,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 20 |
| `questPauseConditionNodeDefinition[questPhone_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 130 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 26 |
| `questPauseConditionNodeDefinition[questTimeCondition,questTimePeriod_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 110 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 7 |
| `questPhaseNodeDefinition` | 109 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 8 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 2 |
| `questPhoneManagerNodeDefinition[questCallContact_NodeType]` | 37 |
| `questPhoneManagerNodeDefinition[questSetPhoneStatus_NodeType]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 20 |
| `questRandomizerNodeDefinition` | 1 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 26 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 4 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 18 |
| `questSceneManagerNodeDefinition[questToggleEventExecutionTag_NodeType]` | 4 |
| `questSceneNodeDefinition[scnInterruptionScenarioId,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 58 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 63 |
| `questSpawnManagerNodeDefinition[questLegacy_NodeType,questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 3 |
| `questSpawnManagerNodeDefinition[questLegacy_NodeType,questSpawnManagerNodeActionEntry]` | 18 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 36 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 48 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 20 |
| `questTimeManagerNodeDefinition[questPauseTime_NodeType]` | 13 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 7 |
| `questTimeManagerNodeDefinition[questShiftTime_NodeType]` | 2 |
| `questUIManagerNodeDefinition[questAddCombatLogMessage_NodeType]` | 3 |
| `questUIManagerNodeDefinition[questBriefingSequencePlayer_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questGlobalTvScheduler_NodeType]` | 2 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 6 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 8 |
| `questUIManagerNodeDefinition[questShowCustomTooltip_NodeType]` | 3 |
| `questUIManagerNodeDefinition[questShowOnscreen_NodeType]` | 3 |
| `questUIManagerNodeDefinition[questSwitchNameplate_NodeType]` | 2 |
| `questUIManagerNodeDefinition[questSwitchToScenario_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 12 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1,questUseWorkspotPlayerParams]` | 42 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 103 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 151 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 208 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 54 |
| `questVehicleNodeDefinition[questEnablePlayerVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questFlushAutopilot_NodeType]` | 4 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 3 |
| `questVehicleNodeDefinition[questMoveOnSplineAndKeepDistance_NodeType]` | 12 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType,scnMarker,scnVehicleMoveOnSpline_Overrides]` | 6 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 16 |
| `questVehicleNodeDefinition[questOverrideSplineSpeed_NodeType]` | 6 |
| `questVehicleNodeDefinition[questRequestVehicleCameraPerspective_NodeType]` | 3 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questStartVehicle_NodeType]` | 5 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 15 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 3 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 28 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 6 |
| `questVehicleNodeDefinition[questToggleWindow_NodeType]` | 2 |
| `questVisionModesManagerNodeDefinition[questEnableScanning_NodeType]` | 38 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 4 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 15 |
| `questWorldDataManagerNodeDefinition[questPrefetchStreaming_NodeTypeV2]` | 4 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 22 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 74 |
| `scnAndNode[scnNodeId]` | 20 |
| `scnChoiceNode[questBuild_ConditionType,questFactsDBCondition,questStatsCondition,questUniversalRef,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questCharacterCondition,questCharacterMount_ConditionType,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questCharacterCondition,questCharacterMount_ConditionType,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsAttachToScreenParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questJournalCondition,questLogicalCondition,questMappinState_ConditionType,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questLifePath_ConditionType,questStatsCondition,questUniversalRef,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsAttachToScreenParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 12 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 6 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsAttachToScreenParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnReferencePointId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 9 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 13 |
| `scnCutControlNode[scnNodeId]` | 16 |
| `scnDeletionMarkerNode[scnNodeId]` | 8 |
| `scnEndNode[scnNodeId]` | 84 |
| `scnHubNode[scnNodeId]` | 63 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 3 |
| `scnRandomizerNode[scnNodeId]` | 27 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 426 |
| `scnStartNode[scnNodeId]` | 106 |
| `scnXorNode[scnNodeId]` | 14 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1cd1354c978ceeec83a5` | 19 | `base\quest\bugfixing\part1\q104\q104_quest_bugfixes.questphase` / h144 / 14 -> 18 -> 21 |
| `4518cc0fb86e98005539` | 18 | `base\quest\main_quests\part1\q104\scenes\q104_01b_calibration.scene` / scene / 2102 -> 1768 -> 2202 |
| `c067e690fdec9fead717` | 18 | `base\quest\main_quests\part1\q104\scenes\q104_08_courier_talks.scene` / scene / 1324 -> 1322 -> 1536 |
| `bfe95df47bd1ca67330f` | 17 | `base\quest\main_quests\part1\q104\phases\debug\q104_debug_setup.questphase` / h0 / 19 -> 18 -> 20 |
| `f42ba76b1fa04f334984` | 16 | `base\quest\main_quests\part1\q104\scenes\q104_05_av_debris.scene` / scene / 2550 -> 2572 -> 2551 |
| `8cd3b647ae3f592ad947` | 15 | `base\quest\main_quests\part1\q104\scenes\q104_01a_roadhouse_meeting.scene` / scene / 1686 -> 1688 -> 1687 |
| `3245d843805c9648b920` | 13 | `base\quest\main_quests\part1\q104\scenes\q104_06_following_tracks.scene` / scene / 197 -> 199 -> 382 |
| `a53561b4c002bc02b58a` | 13 | `base\quest\main_quests\part1\q104\phases\q104_av_crash_site.questphase` / h1431 / 114 -> 3 -> 177 |
| `d4e1a5b22fd6f160ccc6` | 13 | `base\quest\main_quests\part1\q104\phases\q104_av_crash_site.questphase` / h407 / 2 -> 29 -> 14 |
| `98195aee375ef1c62045` | 11 | `base\quest\main_quests\part1\q104\q104.questphase` / h708 / 9 -> 10 -> 11 |
| `ad9170fa6ecab8d058e8` | 11 | `base\quest\main_quests\part1\q104\scenes\q104_08_courier_talks.scene` / scene / 4519 -> 1324 -> 4520 |
| `e02d8e9cefb8e6797ff8` | 11 | `base\quest\main_quests\part1\q104\q104.questphase` / h708 / 8 -> 10 -> 11 |
| `e683d8f0b7fd72d68342` | 11 | `base\quest\main_quests\part1\q104\q104.questphase` / h708 / 10 -> 11 -> 12 |
| `eaf5aab427d50e5598b6` | 11 | `base\quest\bugfixing\part1\q104\q104_cinematic_bugfixes.questphase` / h7 / 0 -> 9 -> 8 |
| `19665e3783f6f51a7337` | 10 | `base\quest\main_quests\part1\q104\scenes\q104_01a_roadhouse_meeting.scene` / scene / 1803 -> 1804 -> 2339 |
| `43d1a3cdcdcb1d73aed9` | 10 | `base\quest\main_quests\part1\q104\scenes\q104_07c_nomads_arrive.scene` / scene / 2208 -> 2203 -> 2202 |
| `4cee280f32674c35f8ed` | 10 | `base\quest\main_quests\part1\q104\scenes\q104_08_courier_talks.scene` / scene / 4519 -> 1324 -> 4522 |
| `7ad3c6d21e732da5d287` | 10 | `base\quest\main_quests\part1\q104\phases\debug\q104_chicken.questphase` / h0 / 67 -> 118 -> 119 |
| `93977b2a92f554edcd12` | 10 | `base\quest\main_quests\part1\q104\phases\q104_gas_station.questphase` / h523 / 3 -> 11 -> 6 |
| `b3ed6f00d272a0396626` | 10 | `base\quest\main_quests\part1\q104\scenes\q104_08_courier_talks.scene` / scene / 1329 -> 1331 -> 4526 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
