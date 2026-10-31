# For Whom the Bell Tolls: scene presentation

Journal identity: `quests/main_quest/act_01/q115_afterlife`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q115_afterlife.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q115\scenes\q115_00b_hanako.scene`

566 graph nodes, 706 edges; 139 event-bearing sections, 817 events; 250 screenplay lines, 41 screenplay options, 14 choice nodes.

Actors: hanako (actor 0, spawnSet); hanako_phone (actor 1, findInContext); johnny (actor 2, spawnDespawn); guard_01 (actor 3, community); waitress (actor 4, findInWorld); guard_02 (actor 5, community); guard_street_01 (actor 6, community); guard_street_02 (actor 7, community); bartender (actor 8, community); av (actor 9, spawner); Player (actor 10, findInContext).

Entries: `hanako_meeting_in` → 535; `Start 8` → 2055; `Start 9` → 2065; `Start 10` → 2093; `Start 25` → 3619; `Start 21` → 3149; `Start 26` → 3674; `Start 16` → 2687; `hanako_sitting_choice` → 2190; `Start 12` → 2197; `Start 17` → 2703; `Start 18` → 2715; `Start 19` → 2717; `Start 20` → 2719; `Start 27` → 3727; `q115_00b_hanako_street_guards` → 1238; `Start 4` → 1754; `after_player_got_up` → 3286; `Start 13` → 2312; `Start 14` → 2347; `Start 23` → 3385; `Start 5` → 1885; `Start 6` → 1886; `Start 15` → 2401; `Start 24` → 3428; `Start 29` → 3956; `Start 30` → 3958; `Start 31` → 3966.

Exits: `hanako_meeting_out` → 5; `End1` → 2659; `enable_elevator` → 1898.

End nodes: 5: `NonTerminating`; 1898: `NonTerminating`; 2659: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 1637 / 1354 | `/Data/RootChunk/sceneGraph/Data/graph/131/Data/events/0` |
| `scnChangeIdleAnimEvent` | 45 | 294 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/10` |
| `scnDialogLineEvent` | 153 | 188 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 13 | 294 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/20` |
| `scnIKEvent` | 26 | 294 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnLookAtAdvancedEvent` | 2 | 1486 / 1263 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/1` |
| `scnLookAtEvent` | 103 | 293 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnPlaySkAnimEvent` | 185 | 293 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnUnmountEvent` | 13 | 294 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/19` |
| `scneventsAttachPropToNode` | 1 | 419 / 517 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/39` |
| `scneventsAttachPropToPerformer` | 9 | 294 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/7` |
| `scneventsAttachPropToWorld` | 6 | 294 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/14` |
| `scneventsCameraParamsEvent` | 6 | 296 / 143 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/16` |
| `scneventsSetAnimFeatureEvent` | 13 | 294 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/16` |
| `scneventsSocket` | 217 | 188 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsVFXEvent` | 22 | 212 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 17
- speech, skeletal_animation, socket_signal: 14
- socket_signal: 10
- speech: 8
- speech, skeletal_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- skeletal_animation: 7
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 6
- speech, skeletal_animation, idle_animation, socket_signal: 5
- skeletal_animation, gaze, socket_signal: 5
- speech, socket_signal: 4
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, gaze, socket_signal: 2
- speech, idle_animation, socket_signal: 2
- speech, gaze: 2
- idle_animation, gaze: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- audio: 2
- skeletal_animation, gaze: 2
- camera: 2
- speech, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation: 1
- idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, props_equipment, vfx: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx, socket_signal: 1
- skeletal_animation, audio: 1
- gaze, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `3d79d866b804d17a62213d9ca34f1a2cd3f1d998b6ce38568f4c717e9f6b19ad`. Binary SHA-256: `709287b5d977e2a4784472694dd392cf03a4f3f234f15d367af5a98bd9778c2c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_00b_hanako.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_03_rogue.scene`

391 graph nodes, 486 edges; 97 event-bearing sections, 777 events; 220 screenplay lines, 30 screenplay options, 15 choice nodes.

Actors: rogue (actor 0, spawnSet); weyland (actor 1, spawnSet); claire (actor 2, spawnSet); nix (actor 3, spawnSet); client_male_4 (actor 4, community); client_female_0 (actor 5, community); client_male_1 (actor 6, community); client_male_3 (actor 7, community); client_female_5 (actor 8, community); barman (actor 9, spawnSet); emmerick (actor 10, spawnSet); V (actor 11, findInContext).

Entries: `meet_rogue_in` → 1; `Start 10` → 1841; `Start 11` → 1853; `ending_kiss` → 1854; `Start 19` → 2771; `Start 20` → 2787; `Start 16` → 2518; `Start 13` → 1923; `Start 17` → 2565; `Start 15` → 1956; `Start 4` → 1688; `Start1` → 2621; `claire_leaving` → 1718; `Start 6` → 1733; `Start 7` → 1736; `Start 0` → 2354; `Start 8` → 1805; `people_leavin` → 1807; `Start 1` → 1502; `Start 2` → 1504; `Start 3` → 1506; `Start 18` → 2738.

Exits: `meet_rogue_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 14 | 683 / 269 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/2` |
| `scnChangeIdleAnimEvent` | 31 | 300 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnDialogLineEvent` | 169 | 300 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnGameplayTransitionEvent` | 11 | 1195 / 1003 | `/Data/RootChunk/sceneGraph/Data/graph/77/Data/events/14` |
| `scnIKEvent` | 22 | 1195 / 989 | `/Data/RootChunk/sceneGraph/Data/graph/77/Data/events/1` |
| `scnLookAtEvent` | 123 | 300 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnPlaySkAnimEvent` | 179 | 300 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 11 | 1195 / 1002 | `/Data/RootChunk/sceneGraph/Data/graph/77/Data/events/13` |
| `scneventsAttachPropToPerformer` | 9 | 718 / 306 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/7` |
| `scneventsAttachPropToWorld` | 7 | 718 / 324 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/21` |
| `scneventsCameraParamsEvent` | 8 | 718 / 304 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 11 | 1195 / 998 | `/Data/RootChunk/sceneGraph/Data/graph/77/Data/events/10` |
| `scneventsSocket` | 167 | 326 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scneventsVFXEvent` | 15 | 718 / 323 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/20` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 11
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- speech, skeletal_animation, socket_signal: 10
- gaze: 10
- skeletal_animation: 7
- socket_signal: 5
- skeletal_animation, socket_signal: 5
- speech, skeletal_animation, idle_animation, socket_signal: 4
- speech, gaze, socket_signal: 4
- speech, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- vfx: 2
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, camera, audio, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `3289f180d94f7eb9825b5b08e109ab713c07829481e0c46ea20087aa20fbd53a`. Binary SHA-256: `95cc57ba47f90e46e960a712644b0c18a5f7bbe9314fa2b3562ca6ca06e849cc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_03_rogue.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_03a_alt.scene`

354 graph nodes, 481 edges; 61 event-bearing sections, 265 events; 145 screenplay lines, 25 screenplay options, 13 choice nodes.

Actors: alt (actor 0, spawnSet); nix (actor 1, spawnSet); johnny (actor 2, spawnSet); tpp_male (actor 3, spawnDespawn); tpp_female (actor 4, spawnDespawn); alt_additional_01 (actor 5, spawnDespawn); alt_additional_02 (actor 6, spawnDespawn); alt_additional_03 (actor 7, spawnDespawn); alt_additional_04 (actor 8, spawnDespawn); V_POSESSED (actor 9, findInContext).

Entries: `q115_03a_sink_in` → 763; `Start 11` → 6064; `q115_03a_talk_alt_in` → 779; `Start 4` → 816; `q115_cyberspace_start` → 1200; `Start 10` → 1646; `Start 7` → 929; `Start 0` → 1501.

Exits: `q115_03a_sink_out` → 764; `q115_03a_talk_alt_out` → 781; `End1` → 6719.

End nodes: 764: `<omitted>`; 781: `NonTerminating`; 6719: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 565 / 362 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/3` |
| `scnChangeIdleAnimEvent` | 2 | 208 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnDialogLineEvent` | 117 | 8 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnGameplayTransitionEvent` | 4 | 787 / 514 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/12` |
| `scnIKEvent` | 8 | 787 / 496 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/2` |
| `scnLookAtEvent` | 11 | 208 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 38 | 208 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnUnmountEvent` | 4 | 787 / 518 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/15` |
| `scneventsAttachPropToPerformer` | 1 | 847 / 569 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/8` |
| `scneventsAttachPropToWorld` | 1 | 847 / 578 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/16` |
| `scneventsCameraParamsEvent` | 5 | 783 / 485 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 4 | 787 / 516 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/14` |
| `scneventsSocket` | 45 | 208 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |
| `scneventsVFXEvent` | 20 | 8 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 23
- skeletal_animation, vfx, socket_signal: 8
- speech, skeletal_animation: 6
- speech, vfx, socket_signal: 4
- speech, vfx: 3
- skeletal_animation, gaze, socket_signal: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx, socket_signal: 1
- gaze: 1
- idle_animation, socket_signal: 1
- vfx: 1
- camera: 1

Raw SHA-256: `1691e704e921371789bdb2158a9f318ea58342179f6aeaba4ec1591641de78b1`. Binary SHA-256: `be9965126c13c7d511c1b2690067773785e06e724ba4a755d8394ef9bc8ccb30`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_03a_alt.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_04_plan.scene`

339 graph nodes, 419 edges; 62 event-bearing sections, 429 events; 145 screenplay lines, 18 screenplay options, 8 choice nodes.

Actors: Rogue (actor 0, spawnSet); alt (actor 1, spawnSet); weyland (actor 2, spawnSet); V_POSESSED (actor 3, findInContext).

Entries: `Start 8` → 2249; `Start 9` → 2253; `Start 11` → 2601; `Start 0` → 2608; `Start 2` → 1989; `Start 10` → 2323; `Start 3` → 2021; `q115_04_waking_up_in` → 1082; `Start 12` → 2662; `Start 4` → 2048; `Start 5` → 2064; `weyland_at_the_bar` → 2066; `Start 7` → 2072; `Start1` → 2720.

Exits: `q115_04_waking_up_out` → 1083; `q115_04_weyland_up_elevator_out` → 1869.

End nodes: 1083: `NonTerminating`; 1869: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1790 / 721 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/3` |
| `scnChangeIdleAnimEvent` | 20 | 1108 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnDialogLineEvent` | 117 | 1087 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 1107 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/18` |
| `scnIKEvent` | 6 | 1107 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/10` |
| `scnLookAtEvent` | 74 | 1087 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 88 | 1087 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 3 | 1107 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/17` |
| `scneventsAttachPropToPerformer` | 3 | 1108 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scneventsAttachPropToWorld` | 3 | 1623 / 418 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/13` |
| `scneventsCameraParamsEvent` | 9 | 1108 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scneventsEquipItemToPerformer` | 1 | 1728 / 674 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 3 | 1107 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/14` |
| `scneventsSocket` | 87 | 1087 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1107 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/7` |
| `scneventsVFXEvent` | 10 | 1108 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 7
- gaze: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, gaze: 4
- speech: 4
- skeletal_animation: 4
- speech, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, gaze, vfx, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, props_equipment, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, vfx, socket_signal: 1
- skeletal_animation, idle_animation, camera, vfx, socket_signal: 1
- skeletal_animation, camera, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze: 1
- socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `f4346e3f7bd04aebf6205d2c09adda62571ce5bb8478f7ec9922dd3812a98458`. Binary SHA-256: `11c02d9649810a3c3cc545d2812127c15ec1c6802be70273f6dbf4689f7ab6c9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_04_plan.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_04_preparations_final.scene`

183 graph nodes, 205 edges; 22 event-bearing sections, 139 events; 44 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: rogue (actor 0, spawnSet); weyland (actor 1, spawnSet); q115_com_afterlife_av (actor 2, community); V_POSESSED (actor 3, findInContext).

Entries: `q115_04_prep_final_in` → 1; `Start 3` → 397; `av_idle_in` → 24; `Start 6` → 667; `Start 4` → 485; `Start 7` → 872.

Exits: `terminate` → 564; `av_idle_out` → 28; `weyland_out` → 527; `q115_04_out` → 529.

End nodes: 28: `<omitted>`; 527: `NonTerminating`; 529: `NonTerminating`; 564: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 327 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/8` |
| `scnChangeIdleAnimEvent` | 6 | 148 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnDialogLineEvent` | 27 | 148 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnGameplayActionEvent` | 2 | 600 / 530 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 327 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/14` |
| `scnIKEvent` | 6 | 327 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/5` |
| `scnLookAtEvent` | 25 | 148 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scnPlaySkAnimEvent` | 28 | 148 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnUnmountEvent` | 3 | 327 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 4 | 327 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/10` |
| `scneventsSocket` | 25 | 148 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsVFXEvent` | 4 | 148 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 4
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- skeletal_animation, gaze, audio, socket_signal: 2
- idle_animation, gaze: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- idle_animation, gameplay_action: 1
- speech, skeletal_animation, vfx, socket_signal: 1

Raw SHA-256: `b8f65b849f74145119627cf178bd79ebd5ed0af9a855cbebeead7899f8b0d309`. Binary SHA-256: `6458a7acade21d2b5e37d270a47664485d98b4085dfa0d230cd61ba1d5286046`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_04_preparations_final.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_05_halo_jump.scene`

130 graph nodes, 177 edges; 28 event-bearing sections, 291 events; 62 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: rogue (actor 0, spawnSet); weyland (actor 1, spawnSet); q115_av (actor 2, community); Player (actor 3, findInContext); V_POSESSED (actor 4, findInContext).

Entries: `Start 8` → 393; `Start 5` → 283; `halo_jump` → 326; `RID` → 334; `q115_flight_in` → 80; `Start 10` → 471.

Exits: `q115_shot_out` → 83; `everyone_mounted` → 231.

End nodes: 83: `<omitted>`; 231: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 17 | 131 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnChangeIdleAnimEvent` | 6 | 92 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 44 | 87 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 409 / 623 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/0` |
| `scnLookAtEvent` | 19 | 92 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnPlayRidAnimEvent` | 4 | 332 / 314 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/4` |
| `scnPlaySkAnimEvent` | 65 | 92 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 6 | 224 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/0` |
| `scneventsSocket` | 50 | 92 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsVFXDurationEvent` | 2 | 161 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/8` |
| `scneventsVFXEvent` | 76 | 161 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, gaze: 2
- vfx: 2
- idle_animation, gameplay_action: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- socket_signal, animation_state: 1
- skeletal_animation, rid_actor, audio, vfx, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, gaze, audio, vfx, socket_signal, animation_state: 1

Raw SHA-256: `018847f4a0252025741189f7f0ddb008dd35184c19a06969e14808d4bded4012`. Binary SHA-256: `0e38117864e01bbc845f37495ea5b39c3efecbd7e2e77202626f8d5eefd2834c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_05_halo_jump.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_02b_rogue_afterlife.scene`

282 graph nodes, 363 edges; 44 event-bearing sections, 261 events; 86 screenplay lines, 15 screenplay options, 8 choice nodes.

Actors: Johnny (actor 0, spawnSet); Rogue (actor 1, spawnSet); Emmerick (actor 2, spawnSet); Weyland (actor 3, spawnSet); sq031_ebunike_worker_1 (actor 4, spawner); sq031_ebunike_worker_2 (actor 5, spawner); sq031_ebunike_worker_3 (actor 6, spawner); rogue_car (actor 7, spawnSet); Player (actor 8, findInContext).

Entries: `preview_ebunike` → 1142; `placeholder` → 1469; `sq031_rogue_afterlife_timelapse_in` → 1218; `sq031_rogue_afterlife_in` → 203; `preview_01` → 1256; `sq031_02b_emmerick_warning_in` → 252; `q115_reuse_clone_in` → 1294.

Exits: `q115_reuse_clone_out` → 1296; `sq031_rogue_afterlife_timelapse_out` → 1220; `sq031_rogue_afterlife_out` → 185; `sq031_02b_emmerick_warning_out` → 253.

End nodes: 185: `NonTerminating`; 253: `<omitted>`; 1220: `NonTerminating`; 1296: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 327 / 232 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/4` |
| `scnChangeIdleAnimEvent` | 5 | 237 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnDialogLineEvent` | 78 | 181 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 210 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnIKEvent` | 4 | 210 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnLookAtEvent` | 86 | 181 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 35 | 210 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnUnmountEvent` | 1 | 210 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scneventsAttachPropToPerformer` | 1 | 1103 / 996 | `/Data/RootChunk/sceneGraph/Data/graph/134/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 5 | 210 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scneventsSocket` | 36 | 210 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scneventsVFXEvent` | 2 | 600 / 476 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 13
- speech: 8
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, gaze, vfx: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- gaze: 1
- skeletal_animation, gaze: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, audio, socket_signal, animation_state: 1

Raw SHA-256: `014f4cbd928c1809cda451cc95b116c32fe20d1fa9d60f7195f65c656f44c2f3`. Binary SHA-256: `40a1de3e505a89b92eb99087ce8210fa131631473625a99d9dc37a864b00c5e5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_02b_rogue_afterlife.scene" --events
```

