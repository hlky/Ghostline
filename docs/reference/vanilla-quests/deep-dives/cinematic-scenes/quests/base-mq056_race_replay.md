# The Distance: scene presentation

Journal identity: `quests/minor_quest/mq056_race_replay`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq056_race_replay.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq056\scenes\mq056_00_commentary.scene`

44 graph nodes, 47 edges; 21 event-bearing sections, 21 events; 21 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, community); Player (actor 1, findInContext).

Entries: `you_ready_in` → 1; `car_hp_drop_in` → 7; `v_lose_in` → 55; `sandstorm_in` → 12; `speeding_in` → 17; `destroying_enemy_in` → 22; `johnny_win_in` → 24; `johnny_lose_in` → 26; `v_win_in` → 74.

Exits: `you_ready_out` → 2; `car_hp_drop_out` → 8; `v_lose_out` → 56; `sandstorm_out` → 13; `speeding_out` → 18; `destroying_enemy_out` → 23; `johnny_win_out` → 25; `johnny_lose_out` → 27; `v_win_out` → 75.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 13: `<omitted>`; 18: `<omitted>`; 23: `<omitted>`; 25: `<omitted>`; 27: `<omitted>`; 56: `<omitted>`; 75: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 21 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 21

Raw SHA-256: `6e3504d9bf29d301ce75658a8e3afb4626c8c5af34921c5f7ea791d42fd6afe4`. Binary SHA-256: `44db90f4db5382c40b2d671459353e7482b2bd1d7d17e5822a8b29769fa8e37a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq056\scenes\mq056_00_commentary.scene" --events
```

## `base\quest\minor_quests\mq056\scenes\mq056_01_city_race.scene`

42 graph nodes, 39 edges; 5 event-bearing sections, 22 events; 8 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: announcer (actor 0, findInContext); Player (actor 1, findInContext).

Entries: `mq056_01_city_announcer_in` → 1; `mq056_01_city_countdown_in` → 176; `mq056_01_city_waiting_in` → 55.

Exits: `mq056_01_city_announcer_out` → 10; `fade_out` → 97; `sq024_announcer_start_countdown_out` → 16; `End 16` → 26; `mq056_01_city_waiting_out` → 161.

End nodes: 10: `NonTerminating`; 16: `NonTerminating`; 26: `<omitted>`; 97: `NonTerminating`; 161: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 12 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 154 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/4` |
| `scnIKEvent` | 2 | 154 / 175 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/1` |
| `scnPlaySkAnimEvent` | 2 | 121 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/0` |
| `scnUnmountEvent` | 1 | 154 / 182 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/7` |
| `scneventsCameraParamsEvent` | 2 | 101 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 1 | 154 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/6` |
| `scneventsSocket` | 7 | 14 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1
- speech, socket_signal: 1
- camera, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `c8ecfd12f96493b9673aa6bcd53301ccb68563fd316356f3104d55f173ec46fe`. Binary SHA-256: `fd7a1419d6514543613db67a1275d2d2240ec0f72da5c3e547b75c404083bbeb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq056\scenes\mq056_01_city_race.scene" --events
```

## `base\quest\minor_quests\mq056\scenes\mq056_02_badlands.scene`

54 graph nodes, 45 edges; 4 event-bearing sections, 20 events; 8 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: announcer (actor 0, findInContext); johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `mq056_02_badlands_waiting_in` → 1; `mq056_02_badlands_announcer_in` → 110; `mq056_02_badlands_in_car` → 201.

Exits: `mq056_02_badlands_waiting_out` → 2; `mq056_02_badlands_fade_out` → 9; `mq056_02_badlands_announcer_out` → 120.

End nodes: 2: `NonTerminating`; 9: `NonTerminating`; 120: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 121 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/1` |
| `scnDialogLineEvent` | 4 | 111 / 142 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 39 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnIKEvent` | 2 | 39 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnPlaySkAnimEvent` | 2 | 39 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnUnmountEvent` | 1 | 39 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 1 | 39 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |
| `scneventsSocket` | 5 | 39 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- speech: 1
- speech, audio, socket_signal: 1

Raw SHA-256: `e0611929dcd6ffcd0dd9114601e333597ced35eb57ae51bcec2e2f7e68db3665`. Binary SHA-256: `dee67bad69a2f3b6435850e8f6fa0f48beb41dc1ae68eee00b262f9fc0557190`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq056\scenes\mq056_02_badlands.scene" --events
```

## `base\quest\minor_quests\mq056\scenes\mq056_03_santo_domingo.scene`

43 graph nodes, 40 edges; 4 event-bearing sections, 25 events; 10 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: announcer (actor 0, findInContext); Player (actor 1, findInContext).

Entries: `mq056_santo_domingo_waiting_in` → 1; `mq056_sd_v_in_car_in` → 180; `mq056_02_announcer_01_in` → 128.

Exits: `mq056_announcer_01_out` → 130; `mq056_santo_domingo_waiting_out` → 2; `mq056_02_spawn_out` → 91; `sq024_02_announcer_countdown_out` → 136; `End 8` → 142; `mq056_santo_domingo_time_skip_out` → 81.

End nodes: 2: `NonTerminating`; 81: `NonTerminating`; 91: `NonTerminating`; 130: `NonTerminating`; 136: `NonTerminating`; 142: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 134 / 160 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/3` |
| `scnDialogLineEvent` | 8 | 126 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 85 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/6` |
| `scnIKEvent` | 2 | 85 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnPlaySkAnimEvent` | 2 | 15 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 1 | 85 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 85 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/4` |
| `scneventsSocket` | 6 | 15 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech: 1
- speech, audio, socket_signal: 1

Raw SHA-256: `67e810340b24684ab990972e9d2e8e7b1a722848da1a3a22dec449eb94068ee8`. Binary SHA-256: `88360d6dabe0f1d2012f68607f27931c9842cc8d0eee7305c42e65964a60f985`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq056\scenes\mq056_03_santo_domingo.scene" --events
```

## `base\quest\minor_quests\mq056\scenes\mq056_04_big_race.scene`

47 graph nodes, 45 edges; 5 event-bearing sections, 24 events; 9 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: announcer (actor 0, findInContext); Player (actor 1, findInContext).

Entries: `mq056_bigrace_announcer_in` → 1; `mq056_bigrace_waiting_in` → 10.

Exits: `mq056_bigrace_announcer_out` → 2; `countdown_out` → 144; `mq056_bigrace_waiting_out` → 11; `sq024_05_spawn_race_out` → 12; `End 9` → 148.

End nodes: 2: `<omitted>`; 11: `NonTerminating`; 12: `NonTerminating`; 144: `NonTerminating`; 148: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 140 / 182 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/2` |
| `scnDialogLineEvent` | 5 | 138 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 82 / 143 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/3` |
| `scnIKEvent` | 2 | 82 / 141 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scnPlaySkAnimEvent` | 3 | 20 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnUnmountEvent` | 1 | 82 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 1 | 82 / 145 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/5` |
| `scneventsSocket` | 7 | 20 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech: 1
- speech, audio, socket_signal: 1

Raw SHA-256: `c2b55647025b9b171fe33ba871bd1375c94e7db44213e137657c2c426b946395`. Binary SHA-256: `3b70b8c11c9673eab06e2ef96a9a5428c2d4e60a716f16cec7e599e77ff2768d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq056\scenes\mq056_04_big_race.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_03b_badlands_race_end.scene`

60 graph nodes, 62 edges; 17 event-bearing sections, 95 events; 39 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: claire (actor 0, spawnSet); racer_1 (actor 1, community); racer_2 (actor 2, community); announcer (actor 3, findInContext); crowd_end_civ (actor 4, community); crowd_end_ald (actor 5, community); crowd_end_wrt (actor 6, community); beast (actor 7, community); Player (actor 8, findInContext).

Entries: `sq024_03b_race_finish_in` → 10; `sq024_03b_talking_racers_in` → 20; `sq024_03b_end_wrt_start` → 191; `sq024_03b_end_ald_start` → 194; `sq024_03b_end_civ_start` → 197.

Exits: `sq024_03b_ride_to_garage_out` → 9; `sq024_03b_race_finish_out` → 11; `sq024_03b_end_wrt_end` → 193; `sq024_03b_end_ald_end` → 196; `sq024_03b_end_civ_end` → 199; `sq024_03b_end_out` → 41; `badlands_fail` → 367.

End nodes: 9: `<omitted>`; 11: `<omitted>`; 41: `<omitted>`; 193: `<omitted>`; 196: `<omitted>`; 199: `<omitted>`; 367: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 22 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnDialogLineEvent` | 36 | 12 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 32 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scnIKEvent` | 4 | 32 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scnLookAtEvent` | 7 | 25 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scnPlaySkAnimEvent` | 22 | 22 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnPoseCorrectionEvent` | 3 | 32 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/5` |
| `scnUnmountEvent` | 2 | 32 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 2 | 32 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/8` |
| `scneventsSocket` | 12 | 22 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze: 1
- socket_signal, animation_state: 1

Raw SHA-256: `79966981eef4bcb4168e38d557304b4665cb349963965451946a5dcf1ca36aaf`. Binary SHA-256: `9aefdae7407d954f5e4de25296ff7b62d3720d24e2dce0967a7c422a91c26d6e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_03b_badlands_race_end.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_04_city_race.scene`

244 graph nodes, 261 edges; 46 event-bearing sections, 294 events; 100 screenplay lines, 13 screenplay options, 6 choice nodes.

Actors: claire (actor 0, spawnSet); announcer (actor 1, findInContext); claire_phone (actor 2, spawnSet); racer_1 (actor 3, community); racer_corp_1 (actor 4, community); sampson (actor 5, community); racer_mox_2 (actor 6, community); racer_corp_2 (actor 7, community); racer_val_1 (actor 8, community); racer_val_2 (actor 9, community); crowd_civ_1 (actor 10, community); crowd_civ_2 (actor 11, community); crowd_civ_3 (actor 12, community); crowd_civ_4 (actor 13, community); claire_car (actor 14, community); race_vehicle_01 (actor 15, community); race_vehicle_02 (actor 16, community); race_vehicle_03 (actor 17, community); race_vehicle_04 (actor 18, community); race_vehicle_05 (actor 19, community); sampsons_car (actor 20, community); v (actor 21, findInContext).

Entries: `sq024_03_city_call_in` → 1; `chicken_in` → 860; `sq024_04_city_pre_race_in` → 16; `sq024_03_random_banter_in` → 244; `Start 13` → 684; `sq024_04_talk_racers_in` → 286; `sq024_04_announcer_01_in` → 94; `sq024_city_together_in` → 306; `sq024_04_racers_talk_corp_start` → 945; `sq024_04_racers_talk_val_start` → 950; `sq024_04_crowd_civ_4_start` → 955; `sq024_04_crowd_civ_3_start` → 960; `sq024_04_crowd_civ_2_start` → 965; `sq024_04_crowd_civ_1_start` → 970; `sharp_turn_in` → 978; `too_far_1_in` → 611; `too_far_2_in` → 612; `too_far_3_in` → 613; `get_out_1_in` → 628; `get_out_2_in` → 629; `let_me_out_1_in` → 630; `let_me_out_2_in` → 631.

Exits: `sq024_03_city_call_out` → 2; `get_out_1_out` → 636; `get_out_2_out` → 637; `let_me_out_1_out` → 638; `let_me_out_2_out` → 639; `End 18` → 1279; `sq024_04_city_pre_race_out` → 17; `sq024_announcer_start_countdown_out` → 445; `sq024_04_announcer_01_out` → 95; `sq024_city_together_out` → 307; `sq024_04_racers_talk_corp_end` → 947; `sq024_04_racers_talk_val_end` → 952; `sq024_04_crowd_civ_4_end` → 957; `sq024_04_crowd_civ_3_end` → 962; `sq024_04_crowd_civ_2_end` → 967; `sq024_04_crowd_civ_1_end` → 972; `sharp_turn_out` → 979; `fade_out` → 395; `too_far_1_out` → 614; `too_far_2_out` → 615; `too_far_3_out` → 616; `End 16` → 1041; `End 17` → 1261.

End nodes: 2: `NonTerminating`; 17: `NonTerminating`; 95: `NonTerminating`; 307: `<omitted>`; 395: `NonTerminating`; 445: `NonTerminating`; 614: `<omitted>`; 615: `<omitted>`; 616: `<omitted>`; 636: `<omitted>`; 637: `<omitted>`; 638: `<omitted>`; 639: `<omitted>`; 947: `<omitted>`; 952: `<omitted>`; 957: `<omitted>`; 962: `<omitted>`; 967: `<omitted>`; 972: `<omitted>`; 979: `<omitted>`; 1041: `<omitted>`; 1261: `<omitted>`; 1279: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 428 / 357 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/2` |
| `scnChangeIdleAnimEvent` | 13 | 20 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnDialogLineEvent` | 86 | 20 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnGameplayTransitionEvent` | 6 | 341 / 189 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/29` |
| `scnIKEvent` | 12 | 341 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/21` |
| `scnLookAtEvent` | 42 | 20 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 53 | 20 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnUnmountEvent` | 6 | 341 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/28` |
| `scneventsAttachPropToPerformer` | 2 | 341 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/3` |
| `scneventsAttachPropToWorld` | 2 | 341 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/7` |
| `scneventsCameraParamsEvent` | 3 | 400 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 6 | 341 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/25` |
| `scneventsSocket` | 58 | 20 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsVFXEvent` | 1 | 341 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 21
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- socket_signal: 2
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, audio, socket_signal: 1
- gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation: 1
- gaze: 1

Raw SHA-256: `b164b74049bd06a2cc276927177b2fed20d8596ed26e59604c2e97486704c989`. Binary SHA-256: `7b749b7704a8e5eef1a7cfd9b33e2030ba1db7575ec1d88e5896d1a50b107e6b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_04_city_race.scene" --events
```

