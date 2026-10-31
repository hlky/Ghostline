# The Hunt: scene presentation

Journal identity: `quests/side_quest/sq021_sick_dreams`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq021_sick_dreams.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\epilogue\q203\scenes\q203_03_sobchak.scene`

211 graph nodes, 253 edges; 53 event-bearing sections, 433 events; 119 screenplay lines, 34 screenplay options, 17 choice nodes.

Actors: sobchak (actor 0, spawnSet); tpp_female (actor 1, spawnDespawn); tpp_male (actor 2, spawnDespawn); q203_03_delamain_av (actor 3, spawnSet); v (actor 4, findInContext).

Entries: `Start 9` → 4387; `q203_01a_shower_in` → 426; `sq021_okay_in` → 812; `preview_kitchen` → 857; `preview_balcony` → 859.

Exits: `q205_02_sobchak_out` → 8; `sq021_okay_out` → 813; `q203_03_sobchak_d_arrives_out` → 824.

End nodes: 8: `NonTerminating`; 813: `<omitted>`; 824: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 24 | 150 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnChangeIdleAnimEvent` | 16 | 87 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 89 | 87 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 352 / 578 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/9` |
| `scnIKEvent` | 10 | 352 / 574 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/5` |
| `scnLookAtEvent` | 57 | 87 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 98 | 87 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnUnmountEvent` | 5 | 352 / 584 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/14` |
| `scneventsAttachPropToPerformer` | 3 | 569 / 844 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/2` |
| `scneventsAttachPropToWorld` | 4 | 276 / 326 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/11` |
| `scneventsCameraParamsEvent` | 17 | 352 / 579 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 5 | 352 / 580 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/11` |
| `scneventsSocket` | 82 | 87 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/13` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 276 / 325 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/10` |
| `scneventsVFXEvent` | 16 | 150 / 212 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 2
- skeletal_animation, camera, audio, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- camera: 2
- speech, gaze: 2
- skeletal_animation, gaze, audio, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, camera, vfx, socket_signal: 1
- speech, skeletal_animation, camera, socket_signal: 1
- skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, audio, vfx: 1
- speech: 1
- skeletal_animation, audio, socket_signal: 1
- gaze: 1
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, camera: 1

Raw SHA-256: `93bb83bab4a4049577033ac7c2c0c39e0719adf5ea7b821b8ded87e173ef92f8`. Binary SHA-256: `a959f4ed3d30bcb43fced3ead9b98eba7defaca8bc678e8a223f238508eea12a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q203\scenes\q203_03_sobchak.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_03_reconnaissance.scene`

511 graph nodes, 652 edges; 89 event-bearing sections, 291 events; 136 screenplay lines, 26 screenplay options, 24 choice nodes.

Actors: Takemura (actor 0, spawnSet); Corrupt_Guard (actor 1, community); V (actor 2, findInContext).

Entries: `q112_03_rec_enter_in` → 11; `Downstairs_prev_elevator_up` → 3772; `q112_03_rec_arrived_in` → 20; `hack` → 2414; `Start 10` → 3832; `scanning_preview` → 3855; `q112_03_takemura_leaves_in` → 2134; `sq021_nothing_left_in` → 2289; `Downstairs_prev_elevator_down` → 3749.

Exits: `q112_03_rec_enter_out` → 18; `q112_03_rec_out` → 225; `show_scanning_component` → 2132; `pipes` → 793; `q112_03_takemura_leaves_out` → 2209; `sq021_nothing_left_out` → 2290; `Cleanup` → 2298.

End nodes: 18: `<omitted>`; 225: `NonTerminating`; 793: `NonTerminating`; 2132: `NonTerminating`; 2209: `<omitted>`; 2290: `<omitted>`; 2298: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 203 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/4` |
| `scnChangeIdleAnimEvent` | 5 | 214 / 131 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scnDialogLineEvent` | 78 | 12 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 44 | 27 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnPlaySkAnimEvent` | 78 | 203 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/1` |
| `scneventsAttachPropToPerformer` | 1 | 1885 / 1140 | `/Data/RootChunk/sceneGraph/Data/graph/165/Data/events/4` |
| `scneventsAttachPropToWorld` | 1 | 203 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/7` |
| `scneventsSocket` | 73 | 27 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 16
- skeletal_animation, socket_signal: 16
- speech: 13
- speech, socket_signal: 10
- speech, gaze: 8
- skeletal_animation, audio, socket_signal: 6
- socket_signal: 4
- skeletal_animation, gaze, audio, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `cceca32631832b1ebcecbd3667c3e4f47795fc1db8ae94a6573e66425e039663`. Binary SHA-256: `953b0fc48178270730482bda089920e9dca1b5782fab32a1defa91e8739db4f5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_03_reconnaissance.scene" --events
```

## `base\quest\side_quests\sq012\scenes\sq012_05a_sex_shop.scene`

300 graph nodes, 351 edges; 58 event-bearing sections, 449 events; 111 screenplay lines, 24 screenplay options, 10 choice nodes.

Actors: sobchak (actor 0, spawnSet); shop_owner (actor 1, spawnSet); passerby (actor 2, spawnDespawn); river_car (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `sq012_05a_river_explains_in` → 1; `sq012_05a_sex_shop_owner_in` → 9; `sq012_05a_interrogation_in` → 26; `arriving_at_shop_preview` → 510; `sq012_05a_where_now_IN` → 45; `sq012_05a_timelapse_in` → 73; `sq012_05a_sit_car_in` → 1060; `sq012_05a_river_explains_player_drives_in` → 400; `sq021_intuition_in` → 210.

Exits: `sq012_05a_river_explains_out` → 2; `sq012_05a_sex_shop_owner_out` → 13; `sq012_05a_sex_shop_timelapse_msg` → 1205; `sq012_05a_where_now_rqr_with_riverOUT` → 46; `sq012_05a_where_now_market_with_river_IN` → 47; `sq012_05a_where_now_market_alone_IN` → 48; `sq012_05a_where_now_rqr_alone_OUT` → 49; `sq012_05a_timelapse_out` → 74; `sq012_05a_sit_car_out` → 1061; `sq021_intuition_out` → 212.

End nodes: 2: `NonTerminating`; 13: `NonTerminating`; 46: `NonTerminating`; 47: `NonTerminating`; 48: `NonTerminating`; 49: `NonTerminating`; 74: `<omitted>`; 212: `<omitted>`; 1061: `NonTerminating`; 1205: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 120 / 439 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/2` |
| `scnChangeIdleAnimEvent` | 35 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnDialogLineEvent` | 80 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 7 | 12 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/19` |
| `scnIKEvent` | 18 | 12 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/6` |
| `scnLookAtEvent` | 95 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 77 | 4 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnUnmountEvent` | 7 | 12 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/18` |
| `scneventsEquipItemToPerformer` | 1 | 10 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 15 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSocket` | 110 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 10 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsVFXEvent` | 2 | 408 / 1027 | `/Data/RootChunk/sceneGraph/Data/graph/112/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 12
- speech: 8
- gaze: 7
- skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- vfx, socket_signal: 1
- socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, ik, socket_signal, animation_state: 1

Raw SHA-256: `f1fc6d7fa738eda26fe889ef2ce42726199719d0cac04edcc6e400e5386c3691`. Binary SHA-256: `224f0dd3b96f2b8a033497ee41171f58024ef4c633533ed46ddd1d986796a02f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq012\scenes\sq012_05a_sex_shop.scene" --events
```

## `base\quest\side_quests\sq017\scenes\sq017_10_us_crack_intro.scene`

312 graph nodes, 357 edges; 49 event-bearing sections, 673 events; 100 screenplay lines, 13 screenplay options, 8 choice nodes.

Actors: kerry (actor 0, spawnSet); blue_moon (actor 1, community); purple_force (actor 2, community); red_menace (actor 3, community); johnny (actor 4, spawnDespawn); v (actor 5, findInContext).

Entries: `Start 0` → 1; `Start 6` → 2742; `Start 1` → 590.

Exits: `End 0` → 2; `cut_distance_pause` → 2798; `end_no_deal` → 380.

End nodes: 2: `<omitted>`; 380: `<omitted>`; 2798: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 41 | 32 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 81 | 32 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scnGameplayTransitionEvent` | 3 | 362 / 909 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/38` |
| `scnIKEvent` | 6 | 362 / 900 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/33` |
| `scnLookAtEvent` | 244 | 32 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 147 | 32 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 1 | 32 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/27` |
| `scnUnmountEvent` | 3 | 362 / 910 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/39` |
| `scneventsAttachPropToPerformer` | 4 | 41 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/45` |
| `scneventsSetAnimFeatureEvent` | 3 | 362 / 911 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/40` |
| `scneventsSocket` | 132 | 32 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scneventsVFXEvent` | 8 | 362 / 869 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 10
- gaze: 8
- skeletal_animation, socket_signal: 4
- speech, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, vfx: 1
- vfx: 1

Raw SHA-256: `0b7ce248b4d12865f7ed3afa98568b0de22f4664bdafa81103fa69860c2c57bf`. Binary SHA-256: `b4b55ee1eac2f0511a431373c01eb80412a622cf22c3c1c435c706687a5c76ce`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_10_us_crack_intro.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_01_hook.scene`

781 graph nodes, 1152 edges; 138 event-bearing sections, 870 events; 258 screenplay lines, 44 screenplay options, 33 choice nodes.

Actors: Sobchak (actor 0, spawnSet); Yawen_Packard (actor 1, community); Johnny (actor 2, spawnDespawn); Homeless_1 (actor 3, community); Homeless_2 (actor 4, community); towfiq_iqbal (actor 5, findInContext); police_officer_01 (actor 6, findInContext); police_officer_02 (actor 7, findInContext); police_operator_female (actor 8, findInContext); anthony_harris (actor 9, findInContext); pickup (actor 10, spawnSet); V (actor 11, findInContext).

Entries: `johnny_car_in` → 1445; `Start 38` → 2956; `Start 39` → 2958; `basic_river_in` → 2964; `techie_river_in` → 3018; `river_room_holo_in` → 1593; `parking_basic_in` → 911; `enter_techie_in` → 925; `lab_fence_start` → 227; `lab_parking_start` → 232; `lab_gate_start` → 239; `v_found_room_in` → 264; `river_comment_2_in` → 980; `parking_gate_in` → 1008; `river_techie_prev` → 5347; `river_found_room_in` → 1078; `briefing_in` → 3937; `Start 48` → 5376; `river_in_room_in` → 407; `Start 42` → 3295; `wrong_dir_in` → 1186; `going_back_in` → 1191; `v_is_back_in` → 1199; `at_place_in` → 1215; `from_cloned_in` → 4805; `lab_chicken_in` → 1244; `Start 46` → 4966.

Exits: `crossing_call_out` → 2936; `river_room_holo_out` → 1595; `lab_mitsuko_end` → 200; `lab_fence_end` → 228; `lab_parking_end` → 233; `lab_gate_end` → 240; `river_comment_2_out` → 981; `securing_dist_2` → 4584; `clues_out_2` → 4586; `securing_distance` → 3223; `briefing_out` → 3939; `clues_out` → 3225; `secure_distance_river` → 4676; `river_in_room_out` → 437; `End 31` → 1187; `End 32` → 1192; `back_out` → 1197; `later_out` → 1200; `at_place_out` → 1216.

End nodes: 200: `<omitted>`; 228: `<omitted>`; 233: `<omitted>`; 240: `<omitted>`; 437: `<omitted>`; 981: `<omitted>`; 1187: `<omitted>`; 1192: `<omitted>`; 1197: `<omitted>`; 1200: `<omitted>`; 1216: `NonTerminating`; 1595: `<omitted>`; 2936: `NonTerminating`; 3223: `NonTerminating`; 3225: `NonTerminating`; 3939: `<omitted>`; 4584: `NonTerminating`; 4586: `NonTerminating`; 4676: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 199 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/9` |
| `scnChangeIdleAnimEvent` | 18 | 199 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnDialogLineEvent` | 205 | 199 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/8` |
| `scnGameplayActionEvent` | 3 | 682 / 711 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/3` |
| `scnGameplayTransitionEvent` | 26 | 199 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/12` |
| `scnIKEvent` | 52 | 199 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |
| `scnLookAtEvent` | 151 | 199 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 167 | 199 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnPoseCorrectionEvent` | 3 | 377 / 277 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/5` |
| `scnUnmountEvent` | 26 | 199 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/16` |
| `scneventsSetAnimFeatureEvent` | 35 | 199 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/13` |
| `scneventsSocket` | 167 | 199 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/14` |
| `scneventsVFXEvent` | 6 | 555 / 409 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 40
- speech, skeletal_animation, gaze, socket_signal: 17
- skeletal_animation, socket_signal: 15
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 15
- speech, skeletal_animation, gaze: 6
- speech, skeletal_animation, gaze, socket_signal, animation_state: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- socket_signal: 4
- skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation: 3
- speech, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, socket_signal: 2
- speech, gaze: 2
- idle_animation, socket_signal, animation_state: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, socket_signal, animation_state: 1

Raw SHA-256: `a36008276ba53c9c5cf62f1ae4356241c25b92e3c074ba494ea01f7e744d1458`. Binary SHA-256: `e24711c86c1e8a6383c91b8342ac01c0e67aec16120644d5daa75c4ca42f6417`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_01_hook.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_02_ride.scene`

86 graph nodes, 109 edges; 14 event-bearing sections, 125 events; 40 screenplay lines, 9 screenplay options, 4 choice nodes.

Actors: Sobchak (actor 0, spawnSet); pickup (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `Start 0` → 422; `ride_in` → 9.

Exits: `End 0` → 423; `ride_end_out` → 288.

End nodes: 288: `<omitted>`; 423: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 106 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 39 | 3 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnIKEvent` | 2 | 666 / 625 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/0` |
| `scnLookAtEvent` | 35 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 106 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 39 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 2 | 106 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 2 | 106 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 7
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation: 1
- ik: 1

Raw SHA-256: `d6f45dc6885b15c3c8d5c60f252f74597754e0b13b288aabd62059f35d3b88e9`. Binary SHA-256: `5607cf613b0836a3d8466efe19f109e8cdf3d24ed741dc5322233956462bd42a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_02_ride.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_03_trailer_park.scene`

165 graph nodes, 181 edges; 30 event-bearing sections, 305 events; 67 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: Sobchak (actor 0, spawnSet); Joss (actor 1, spawnSet); Boy (actor 2, spawnSet); Girl (actor 3, spawnSet); Johnny (actor 4, spawnDespawn); pickup (actor 5, spawnSet); V (actor 6, findInContext).

Entries: `joss_in` → 1; `kids` → 905; `Start 8` → 1051; `johnny` → 930.

Exits: `kids_go_out` → 239.

End nodes: 239: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 118 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 48 | 118 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayTransitionEvent` | 7 | 134 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/23` |
| `scnIKEvent` | 16 | 134 / 163 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/16` |
| `scnLookAtEvent` | 89 | 118 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnPlaySkAnimEvent` | 63 | 118 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnUnmountEvent` | 7 | 134 / 170 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/22` |
| `scneventsSetAnimFeatureEvent` | 7 | 134 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/19` |
| `scneventsSocket` | 54 | 118 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/15` |
| `scneventsVFXEvent` | 5 | 657 / 697 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 6
- skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, gaze: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, vfx, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech: 1
- vfx: 1

Raw SHA-256: `560610f6636bb79dffa6fa2bcf538d27674094b9b4bdb85d481b908faed54ea4`. Binary SHA-256: `f2baec4f00b3bd16f1c74cab3b11a4b09a2e34e20c9a71e2632c6c8f6e0f0d8f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_03_trailer_park.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_04_randys_room.scene`

390 graph nodes, 524 edges; 49 event-bearing sections, 248 events; 64 screenplay lines, 21 screenplay options, 17 choice nodes.

Actors: Sobchak (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `Start 18` → 1486; `inv_start_in` → 159; `sq021_lab_cabinet_in` → 2766; `Start 19` → 1815; `Start 21` → 2937.

Exits: `inv_start_out` → 160; `sq021_lab_cabinet_out` → 2768.

End nodes: 160: `NonTerminating`; 2768: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 47 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnChangeIdleAnimEvent` | 12 | 55 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnDialogLineEvent` | 51 | 39 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 6 | 166 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/14` |
| `scnIKEvent` | 12 | 166 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/8` |
| `scnLookAtEvent` | 57 | 39 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 46 | 93 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnUnmountEvent` | 6 | 166 / 143 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 6 | 166 / 139 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/10` |
| `scneventsSocket` | 44 | 93 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |
| `scneventsVFXEvent` | 2 | 166 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 10
- speech: 5
- speech, skeletal_animation, gaze: 4
- skeletal_animation, socket_signal: 4
- skeletal_animation: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation: 2
- speech, gaze, audio: 1
- speech, idle_animation, gaze, audio: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `04e43624ffd647271f7129d66afcfacd1b6eb646a82e68b30885d579075f05bb`. Binary SHA-256: `f9266bc8cee7d4f460481869962f9125430b9bdcde0de82bc8a49dd0f6383d32`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_04_randys_room.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_04b_randys_pc.scene`

144 graph nodes, 147 edges; 23 event-bearing sections, 107 events; 48 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Sobchak (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `pc_conclusion_in` → 272; `clue06_in` → 275; `clue01_in` → 6; `file_recognized_in` → 570; `hidden_in` → 577; `clue07_in` → 310; `clue08_in` → 316; `webfile_in` → 592; `pc_reminder` → 1018; `failed_in` → 648; `file_cartoon_in` → 519; `clue04_in` → 253; `clue05_in` → 254; `clue03_in` → 255; `clue02_in` → 256.

Exits: `clue06_out` → 276; `file_recognized_out` → 572; `hidden_out` → 578; `clue07_out` → 311; `clue08_out` → 317; `webfile_out` → 593; `pc_reminder_out` → 1020; `file_cartoon_out` → 520; `pc_conclusion_out` → 119; `clue01_out` → 257; `clue02_out` → 258; `clue03_out` → 259; `clue04_out` → 260; `clue05_out` → 261.

End nodes: 119: `NonTerminating`; 257: `<omitted>`; 258: `<omitted>`; 259: `<omitted>`; 260: `<omitted>`; 261: `<omitted>`; 276: `<omitted>`; 311: `<omitted>`; 317: `<omitted>`; 520: `<omitted>`; 572: `<omitted>`; 578: `<omitted>`; 593: `<omitted>`; 1020: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 279 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/3` |
| `scnChangeIdleAnimEvent` | 1 | 279 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/4` |
| `scnDialogLineEvent` | 47 | 184 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 285 / 98 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/7` |
| `scnIKEvent` | 6 | 285 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scnLookAtEvent` | 7 | 218 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnPlaySkAnimEvent` | 12 | 218 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnUnmountEvent` | 3 | 285 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 3 | 285 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/8` |
| `scneventsSocket` | 18 | 218 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsVFXEvent` | 2 | 218 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio: 1
- speech, skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, audio: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `2494a15001f9907f3fa883cacde9eec5db281bbfce0ed6629348a4bdea192d12`. Binary SHA-256: `6ea0bd1493a32c8638036e89e1bcd5ca8ee00c34a76acc1db9b6cb4c586394c2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_04b_randys_pc.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_05_bbq.scene`

172 graph nodes, 201 edges; 35 event-bearing sections, 315 events; 64 screenplay lines, 19 screenplay options, 14 choice nodes.

Actors: Sobchak (actor 0, spawnSet); Boy (actor 1, spawnSet); Girl (actor 2, spawnSet); Joss (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `sit_in` → 35; `sleep_in` → 41; `prev_from_randys_room` → 6186; `river_bedroom_in` → 393; `for_preview` → 850; `joss_beforebbq_in` → 121; `joss_smokin_in` → 416.

Exits: `sit_out` → 36; `sleep_out` → 42; `river_bedroom_out` → 394; `joss_beforebbq_out` → 122; `joss_smokin_out` → 417; `joss_no_quest_ends` → 126.

End nodes: 36: `<omitted>`; 42: `<omitted>`; 122: `<omitted>`; 126: `<omitted>`; 394: `<omitted>`; 417: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 427 / 455 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/1` |
| `scnChangeIdleAnimEvent` | 15 | 130 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scnDialogLineEvent` | 47 | 116 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 7 | 123 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/33` |
| `scnIKEvent` | 14 | 123 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/22` |
| `scnLookAtEvent` | 97 | 116 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnPlaySkAnimEvent` | 55 | 116 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scnUnmountEvent` | 7 | 123 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/32` |
| `scneventsAttachPropToPerformer` | 3 | 123 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scneventsAttachPropToWorld` | 2 | 300 / 311 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/12` |
| `scneventsCameraParamsEvent` | 3 | 427 / 456 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/2` |
| `scneventsEquipItemToPerformer` | 4 | 283 / 198 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 7 | 123 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/29` |
| `scneventsSocket` | 49 | 116 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/10` |
| `scneventsUnequipItemFromPerformer` | 2 | 283 / 204 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/5` |
| `scneventsVFXEvent` | 2 | 613 / 563 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 4
- speech, gaze: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation: 2
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech: 1
- skeletal_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- gaze: 1
- vfx: 1
- idle_animation, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `d3f861cc2ef81a077a7d6bb7d9761af128a0ab314333f8470971517c90dfd2d1`. Binary SHA-256: `d2e856126caec56c8be9e3cbaecf28661bd017456fdf4141637c8248da6f78b4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_05_bbq.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_06_call.scene`

41 graph nodes, 40 edges; 8 event-bearing sections, 21 events; 18 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Johnny (actor 0, spawnSet); River (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `crossing_call_in` → 266; `phone_hook_start` → 195.

Exits: `rejected_out` → 602; `crossing_call_out` → 267; `phone_hook_end` → 197.

End nodes: 197: `<omitted>`; 267: `<omitted>`; 602: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 210 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 11 | 210 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 7 | 268 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 5
- idle_animation, gaze: 2
- speech, idle_animation: 1

Raw SHA-256: `d9755e2dd6c8de245a40e4a94079da6e9af807081cd8982f8712104e59d52f51`. Binary SHA-256: `5031219883823a6b9a79d88f7147c885686a992a2b419698627810b946dbe5f5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_06_call.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_07_ride_back.scene`

219 graph nodes, 256 edges; 42 event-bearing sections, 259 events; 72 screenplay lines, 7 screenplay options, 5 choice nodes.

Actors: Sobchak (actor 0, spawnSet); dd (actor 1, spawnDespawn); pickup (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `wake_up_in` → 1; `sq021_bd_let_work_in` → 599; `after_bd_in` → 53; `to_workshop_in` → 56; `good_after_wrong_in` → 68; `prev_car` → 1165.

Exits: `wake_up_out` → 2; `sq021_bd_let_work_out` → 600; `farm_chosen_out` → 54; `river_distance_out` → 512; `car_farm_talk_out` → 726.

End nodes: 2: `<omitted>`; 54: `NonTerminating`; 512: `NonTerminating`; 600: `<omitted>`; 726: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 3 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scnChangeIdleAnimEvent` | 9 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 56 | 3 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnGameplayActionEvent` | 1 | 277 / 336 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/3` |
| `scnGameplayTransitionEvent` | 6 | 277 / 341 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/6` |
| `scnIKEvent` | 18 | 277 / 334 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/1` |
| `scnLookAtEvent` | 33 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 3 | 424 / 393 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/2` |
| `scnPlaySkAnimEvent` | 45 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnUnmountEvent` | 6 | 277 / 346 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/10` |
| `scneventsAttachPropToPerformer` | 6 | 3 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsAttachPropToWorld` | 1 | 313 / 379 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/3` |
| `scneventsCameraParamsEvent` | 7 | 3 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 12 | 277 / 342 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/7` |
| `scneventsSocket` | 40 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 13 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, gaze: 5
- skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze: 2
- skeletal_animation, idle_animation, vfx: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, props_equipment, socket_signal: 1
- speech, gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, animation_state, mount_workspot: 1
- speech, vfx: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio: 1
- speech, skeletal_animation: 1
- vfx: 1
- camera, vfx: 1
- skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `bd38be69bbf3d804778131d10046617a42759d9731f446ad00bc4b8aa125ce1c`. Binary SHA-256: `210cce84a5ab74a7d8cfea1f90141584a6b9a6662a7954a871e637a265a5dc39`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_07_ride_back.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_09_bd_school.scene`

164 graph nodes, 197 edges; 11 event-bearing sections, 124 events; 30 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: V (actor 0, spawnSet); YoungMeatman (actor 1, spawnDespawn); Schoolkid1 (actor 2, spawnDespawn); Schoolkid2 (actor 3, spawnDespawn); Schoolkid3 (actor 4, spawnDespawn); Schoolkid4 (actor 5, spawnDespawn); River (actor 6, findInContext); Teacher (actor 7, spawnDespawn); Schoolkid5 (actor 8, spawnDespawn); cow (actor 9, spawnDespawn).

Entries: `teacher_in` → 31; `Start 14` → 4665; `bd_finish_com_farm_in` → 626.

Exits: `bd_school_out` → 362; `bd_finish_com_farm_out` → 628.

End nodes: 362: `<omitted>`; 628: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioDurationEvent` | 28 | 111 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/24` |
| `scnDialogLineEvent` | 27 | 23 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlayRidAnimEvent` | 3 | 111 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scnPlaySkAnimEvent` | 42 | 111 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 111 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scneventsBraindanceVisibilityEvent` | 2 | 111 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/19` |
| `scneventsCameraParamsEvent` | 1 | 111 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |
| `scneventsClueEvent` | 4 | 111 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/18` |
| `scneventsPlayRidCameraAnimEvent` | 3 | 111 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/17` |
| `scneventsSocket` | 10 | 111 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/22` |
| `scneventsVFXEvent` | 3 | 424 / 624 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, skeletal_animation, rid_actor, camera, rid_camera, props_equipment, audio, socket_signal, clues, bd_visibility_ui: 1
- vfx, socket_signal: 1
- vfx: 1
- socket_signal: 1

Raw SHA-256: `85b09257517e12be4b7c30387b01e72a1fe6a232ce930f33f4df0f708fe66937`. Binary SHA-256: `eaa82d9a0c33ac61fb0669b922c7a89ffb1cd390c3bb56319697eec6fb732ab5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_09_bd_school.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_10_bd_farm.scene`

561 graph nodes, 721 edges; 38 event-bearing sections, 272 events; 65 screenplay lines, 25 screenplay options, 24 choice nodes.

Actors: V (actor 0, spawnSet); Young_Meatman (actor 1, spawnDespawn); Meatman (actor 2, spawnDespawn); Father (actor 3, spawnDespawn); Victim (actor 4, spawnDespawn); River (actor 5, findInContext); Victim_01 (actor 6, spawnDespawn); Victim_02 (actor 7, spawnDespawn); Victim_03 (actor 8, spawnDespawn); cow1 (actor 9, spawnDespawn); cow2 (actor 10, spawnDespawn); cow3 (actor 11, spawnDespawn); Mother (actor 12, spawnDespawn); cpu_voice (actor 13, findInContext).

Entries: `Start 37` → 4710; `Start 38` → 4713; `Start 39` → 4755; `BD_FARM` → 222; `bd_farm_present_in` → 389.

Exits: `bd_farm_texas_out` → 387; `bd_farm_present_out` → 528.

End nodes: 387: `<omitted>`; 528: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioDurationEvent` | 42 | 219 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/16` |
| `scnAudioEvent` | 1 | 1574 / 2284 | `/Data/RootChunk/sceneGraph/Data/graph/311/Data/events/1` |
| `scnDialogLineEvent` | 58 | 47 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlayRidAnimEvent` | 10 | 219 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/13` |
| `scnPlaySkAnimEvent` | 98 | 219 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/3` |
| `scneventsAttachPropToPerformer` | 4 | 219 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/1` |
| `scneventsBraindanceVisibilityEvent` | 4 | 219 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/15` |
| `scneventsCameraParamsEvent` | 2 | 219 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/0` |
| `scneventsClueEvent` | 20 | 219 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/23` |
| `scneventsPlayRidCameraAnimEvent` | 7 | 219 / 160 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/18` |
| `scneventsSocket` | 17 | 219 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/24` |
| `scneventsVFXBraindanceEvent` | 6 | 219 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/88` |
| `scneventsVFXEvent` | 3 | 219 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/25` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 32
- vfx: 2
- speech, skeletal_animation, rid_actor, camera, rid_camera, props_equipment, audio, vfx, socket_signal, clues, bd_visibility_ui: 1
- speech, skeletal_animation, rid_actor, camera, rid_camera, props_equipment, audio, socket_signal, clues, bd_visibility_ui: 1
- socket_signal: 1
- speech, audio: 1

Raw SHA-256: `eb02866047fcedf2ce41a1dbaca03b105c7a846d148501131807046b1b16d0e5`. Binary SHA-256: `2ca07215c4022c3b5a905a01ec17f29b01afe4bc1c53dc0803c4d54d39313f09`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_10_bd_farm.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_11_finale.scene`

526 graph nodes, 630 edges; 105 event-bearing sections, 777 events; 203 screenplay lines, 39 screenplay options, 27 choice nodes.

Actors: Sobchak (actor 0, spawnSet); Randy (actor 1, community); Victim01 (actor 2, community); Victim02 (actor 3, community); Victim03 (actor 4, community); Johnny (actor 5, spawnDespawn); Policewoman (actor 6, spawnSet); Trauma_Team (actor 7, spawnSet); Policeman (actor 8, spawnSet); policeman2 (actor 9, spawnSet); policeman3 (actor 10, spawnSet); policewoman2 (actor 11, spawnSet); policewoman3 (actor 12, spawnSet); policewoman4 (actor 13, spawnSet); trauma2 (actor 14, spawnSet); rivers_pickup (actor 15, spawnSet); car1 (actor 16, spawnSet); car2 (actor 17, spawnSet); car3 (actor 18, spawnSet); av1 (actor 19, community); av2 (actor 20, spawnSet); V (actor 21, findInContext).

Entries: `good_farm_in` → 1; `term_in` → 18; `Start 42` → 1422; `Start 43` → 1469; `dogs_in` → 553; `teleport_in` → 137; `Start 44` → 1556; `fin_talk_in` → 159; `cameras_in` → 686; `gate_idle` → 4424; `silo_in` → 698; `fighting_in` → 703; `Start 50` → 2111; `Start 45` → 1649; `beware_in` → 1255; `second_warning_in` → 1260; `gate_in` → 330; `secret_doors_in` → 1266; `secret_room_in` → 1271; `turn_off_security_in` → 1277; `barn_no_go_in` → 1290; `riv_back_in` → 1295; `rivers_body_in` → 1304; `Start 46` → 1780; `police_fluff_in` → 1315; `police_work_in` → 1319; `from_good_in` → 1797; `from_bad_in` → 1798; `security_in` → 428; `roof_in` → 921; `Start1` → 4658; `Start2` → 4660; `Start3` → 4662.

Exits: `good_farm_out` → 16; `term_out` → 21; `dogs_out` → 554; `teleport_out` → 138; `fin_talk_good_out` → 161; `gate_idle_out` → 4430; `End 50` → 4462; `help_randy_out` → 740; `End 51` → 4484; `beware_out` → 1256; `gate_out` → 332; `turn_off_security_out` → 1278; `riv_back_out` → 1296; `rivers_body_out` → 1305; `second_warning_out` → 4583; `silo_out` → 4584; `police_fluff_out` → 1316; `fighting_out` → 4587; `police_work_out` → 1320; `barn_no_go_out` → 4589; `cameras_out` → 4595; `security_out` → 430; `river_calls_out` → 447.

End nodes: 16: `NonTerminating`; 21: `<omitted>`; 138: `NonTerminating`; 161: `NonTerminating`; 332: `NonTerminating`; 430: `NonTerminating`; 447: `NonTerminating`; 554: `NonTerminating`; 740: `<omitted>`; 1256: `NonTerminating`; 1278: `NonTerminating`; 1296: `NonTerminating`; 1305: `NonTerminating`; 1316: `<omitted>`; 1320: `<omitted>`; 4430: `NonTerminating`; 4462: `NonTerminating`; 4484: `NonTerminating`; 4583: `NonTerminating`; 4584: `NonTerminating`; 4587: `NonTerminating`; 4589: `NonTerminating`; 4595: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 30 | 56 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scnChangeIdleAnimEvent` | 52 | 56 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/5` |
| `scnDialogLineEvent` | 167 | 27 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnGameplayTransitionEvent` | 21 | 629 / 640 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/12` |
| `scnIKEvent` | 46 | 629 / 626 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/1` |
| `scnLookAtEvent` | 98 | 158 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/3` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 1557 / 2123 | `/Data/RootChunk/sceneGraph/Data/graph/268/Data/events/3` |
| `scnPlaySkAnimEvent` | 162 | 27 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnUnmountEvent` | 21 | 629 / 639 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/11` |
| `scneventsAttachPropToPerformer` | 1 | 1097 / 1477 | `/Data/RootChunk/sceneGraph/Data/graph/160/Data/events/12` |
| `scneventsAttachPropToWorld` | 1 | 904 / 1287 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/4` |
| `scneventsCameraParamsEvent` | 10 | 629 / 688 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/38` |
| `scneventsEquipItemToPerformer` | 2 | 1097 / 1475 | `/Data/RootChunk/sceneGraph/Data/graph/160/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 24 | 629 / 635 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/8` |
| `scneventsSocket` | 109 | 27 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsUnequipItemFromPerformerByItem` | 6 | 165 / 256 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/16` |
| `scneventsVFXEvent` | 26 | 1097 / 1467 | `/Data/RootChunk/sceneGraph/Data/graph/160/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 39
- speech, skeletal_animation, idle_animation, audio: 6
- speech, skeletal_animation, gaze: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- socket_signal: 4
- skeletal_animation: 4
- idle_animation: 4
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, socket_signal: 2
- speech, gaze: 2
- speech, audio, socket_signal: 2
- skeletal_animation, vfx: 2
- skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 2
- vfx: 2
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- skeletal_animation, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1
- skeletal_animation, camera: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `c8965fe4299d22730f2705d5cfb654b8db2e563f7201c625486241cbfb7cbf16`. Binary SHA-256: `10100586e576735c5d378a930a6fbceced636174117b4fb42ab51312cff7c9f1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_11_finale.scene" --events
```

## `base\quest\side_quests\sq021\scenes\sq021_13_wrong_farm.scene`

88 graph nodes, 95 edges; 10 event-bearing sections, 52 events; 20 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Sobchak (actor 0, spawnSet); pickup (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `to_bad_farm_in` → 4; `river_about_wraiths_in` → 210; `bad_barn_in` → 53; `back_in` → 85.

Exits: `to_bad_farm_out` → 5; `river_about_wraiths_out` → 211; `follower_stop` → 4371; `bad_barn_out` → 54; `back_out` → 86.

End nodes: 5: `<omitted>`; 54: `<omitted>`; 86: `<omitted>`; 211: `<omitted>`; 4371: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 4393 / 457 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/1` |
| `scnDialogLineEvent` | 15 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 4416 / 483 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/5` |
| `scnIKEvent` | 6 | 209 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scnLookAtEvent` | 7 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 4464 / 526 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/0` |
| `scnPlaySkAnimEvent` | 10 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnUnmountEvent` | 1 | 4416 / 487 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 3 | 4416 / 485 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/7` |
| `scneventsSocket` | 6 | 55 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- skeletal_animation, idle_animation: 2
- speech, skeletal_animation, gaze: 1
- speech, socket_signal: 1
- speech, skeletal_animation, ik, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- animation_state, mount_workspot: 1

Raw SHA-256: `fa10a8a3b27821f39559555e305e672b37d2ab7e196896b4d8a59dbba220896c`. Binary SHA-256: `4364832bac5cd5f9956fda142bd7f2d68cf9c10dd448a1644de591c95d57074d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq021\scenes\sq021_13_wrong_farm.scene" --events
```

