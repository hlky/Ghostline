# The Pickup: scene presentation

Journal identity: `quests/main_quest/prologue/q003_maelstrom`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q003_maelstrom.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\prologue\q003\scenes\q003_00_call_jackie.scene`

96 graph nodes, 119 edges; 23 event-bearing sections, 98 events; 49 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: Jackie (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `q003_00_call_jackie_in` → 9; `after_evely_preview` → 397; `before_malestrom_preview` → 310; `linesforreuse` → 416; `q003_00_status_update_in` → 74.

Exits: `q003_00_call_jackie_out` → 10; `q003_00_status_update_out` → 75.

End nodes: 10: `<omitted>`; 75: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 21 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnDialogLineEvent` | 47 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnLookAtEvent` | 6 | 129 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/6` |
| `scnPlaySkAnimEvent` | 20 | 84 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scneventsCameraEvent` | 1 | 318 / 296 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/0` |
| `scneventsSocket` | 3 | 129 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation: 8
- speech, idle_animation: 7
- speech, skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 1
- camera: 1
- gaze: 1

Raw SHA-256: `7627e4952b0a2ac1e07b6961383fceb58e9205847c7bb2cecbf9086bc05df746`. Binary SHA-256: `29a840ddd9b9a8669921a257b98b5152f551ab15af450b7969435f43dc221ddd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_00_call_jackie.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_01_call_militech.scene`

76 graph nodes, 91 edges; 11 event-bearing sections, 44 events; 16 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: Meredith (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `q003_01_at_place_in` → 2902; `meredith_holocall_prev` → 3067; `q003_01a_militech_call_in` → 2710; `sq011_wait_concert_in` → 3312.

Exits: `q003_01_at_place_out` → 2903; `Kill Signal` → 3139; `q003_01a_militech_call_out` → 2711; `sq011_wait_concert_out` → 3313; `q003_01_at_place_spawning_out` → 2955.

End nodes: 2711: `<omitted>`; 2903: `<omitted>`; 2955: `NonTerminating`; 3139: `<omitted>`; 3313: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 2824 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnChangeIdleAnimEvent` | 6 | 2709 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnDialogLineEvent` | 12 | 2709 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 2988 / 139 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/7` |
| `scnIKEvent` | 2 | 2988 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |
| `scnLookAtEvent` | 3 | 2713 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 6 | 2824 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnUnmountEvent` | 1 | 2988 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/6` |
| `scneventsAttachPropToPerformer` | 1 | 2713 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsCameraEvent` | 1 | 3063 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 3063 / 227 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 1 | 2988 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/3` |
| `scneventsSocket` | 6 | 2824 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |
| `scneventsVFXEvent` | 2 | 2910 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, idle_animation: 1
- speech, idle_animation, gaze, props_equipment: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- camera: 1
- vfx, socket_signal: 1

Raw SHA-256: `093bd08f6fd72c8d4f8fad8b3f3f0a21b71febdd01cc548e4671bb9abdb4c63a`. Binary SHA-256: `8c127724b75a30aea8e494832d10143a67043fccbaf77e7cac98a1d9b4e71d89`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_01_call_militech.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_01a_militech.scene`

266 graph nodes, 346 edges; 55 event-bearing sections, 457 events; 93 screenplay lines, 19 screenplay options, 7 choice nodes.

Actors: Jackie (actor 0, spawnSet); Meredith (actor 1, spawnSet); Bodyguard01 (actor 2, community); Bodyguard02 (actor 3, community); Anthony (actor 4, spawnSet); DRONE (actor 5, community); SUVwithDRONE (actor 6, community); suv (actor 7, community); Player (actor 8, findInContext).

Entries: `full_scene_prev` → 3684; `Start 16` → 3494; `q003_01a_militech_suv_idle` → 3500; `Start 19` → 3733; `Start 20` → 9975; `q003_malware_removed_in` → 2850; `q003_01a_militech_in` → 1470; `decision_preview` → 3350.

Exits: `q003_01a_militech_out` → 2337; `q003_malware_removed_out` → 2851.

End nodes: 2337: `<omitted>`; 2851: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 51 | 1097 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnChangeIdleAnimEvent` | 29 | 1097 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scnDialogLineEvent` | 74 | 1417 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/24` |
| `scnGameplayTransitionEvent` | 1 | 1448 / 415 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/32` |
| `scnIKEvent` | 2 | 1448 / 403 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/21` |
| `scnLookAtAdvancedEvent` | 1 | 3484 / 1562 | `/Data/RootChunk/sceneGraph/Data/graph/167/Data/events/3` |
| `scnLookAtEvent` | 77 | 1097 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 117 | 1097 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPoseCorrectionEvent` | 4 | 1417 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnUnmountEvent` | 1 | 1448 / 414 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/31` |
| `scneventsAttachPropToPerformer` | 1 | 1448 / 397 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/19` |
| `scneventsAttachPropToWorld` | 1 | 1844 / 469 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/7` |
| `scneventsCameraParamsEvent` | 7 | 1417 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/21` |
| `scneventsSetAnimFeatureEvent` | 1 | 1448 / 410 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/28` |
| `scneventsSocket` | 76 | 1097 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/18` |
| `scneventsVFXEvent` | 14 | 1097 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/16` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 14
- gaze: 11
- speech, skeletal_animation, idle_animation, gaze, audio: 4
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- speech, gaze: 2
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx: 1
- speech, skeletal_animation, gaze, audio: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- camera, vfx: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `60e98007c45d2b540c23888a855956e158f0f92ffbae28be40999ddaee8d4ab3`. Binary SHA-256: `273bc29a9cc23f202771fb4fe2f23234f7b7c81923ead6ef83df274438ef6393`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_01a_militech.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_01b_meat_factory.scene`

211 graph nodes, 318 edges; 33 event-bearing sections, 195 events; 62 screenplay lines, 12 screenplay options, 6 choice nodes.

Actors: Jackie (actor 0, spawnSet); Royce (actor 1, findInContext); DumDum (actor 2, spawnDespawn); Jackie_bike (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `q003_meet_jackie_in` → 1674; `q003_meet_jackie_interrupted_in` → 1873; `q003_bike_idle_in` → 2863; `q003_intercom_interrupted_in` → 1907; `walk_to_factory` → 2488; `Start 16` → 2499.

Exits: `q003_meet_jackie_out` → 1675; `q003_meet_jackie_interrupted_out` → 1871; `q003_intercom_interrupted_out` → 1900.

End nodes: 1675: `<omitted>`; 1871: `<omitted>`; 1900: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 2020 / 545 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/3` |
| `scnChangeIdleAnimEvent` | 22 | 1498 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 53 | 1498 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 2020 / 537 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/0` |
| `scnLookAtEvent` | 33 | 1498 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 36 | 1498 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 13 | 1679 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scneventsSocket` | 32 | 1550 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsVFXDurationEvent` | 3 | 1547 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 6
- speech: 3
- skeletal_animation, idle_animation: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, gaze: 2
- speech, gaze, vfx: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, gaze: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, gameplay_action: 1

Raw SHA-256: `74a05476eed334fc80183904fdefc56c2c28c67eed827629519d0f09a87b6fe8`. Binary SHA-256: `752c6909e56f25fe0f55915f5fb032071ce0d17cd7b57efbf2f67811a95203e4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_01b_meat_factory.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_02_maelstrom_corridor.scene`

177 graph nodes, 266 edges; 19 event-bearing sections, 70 events; 24 screenplay lines, 8 screenplay options, 8 choice nodes.

Actors: Jackie (actor 0, spawnSet); welding_maelstromer (actor 1, spawner); Player (actor 2, findInContext).

Entries: `q003_maelstrom_corridor_in` → 2; `jackie_enter_hall` → 1888; `CYB-657661_retrofix_in` → 2072.

Exits: `q003_maelstrom_corridor_out` → 43; `q003_no_deal_triggered_out` → 1352.

End nodes: 43: `NonTerminating`; 1352: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 188 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 17 | 51 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 4 | 1215 / 252 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/8` |
| `scnIKEvent` | 8 | 1215 / 244 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/1` |
| `scnLookAtEvent` | 6 | 51 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 11 | 51 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnUnmountEvent` | 4 | 1215 / 251 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 4 | 1215 / 247 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/4` |
| `scneventsSocket` | 15 | 194 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 4
- speech: 4
- speech, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `3d1a61881416b56e2464f9e9caef4a8125abcc05a7c71e54737a9380de1990e7`. Binary SHA-256: `2bc5d4d9d18861840350b7c33216fe263330ab09a3f473f1ff2f654d20ff9a8b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_02_maelstrom_corridor.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_02_maelstrom_corridor_part2.scene`

114 graph nodes, 169 edges; 23 event-bearing sections, 51 events; 28 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Jackie (actor 0, spawnSet); Kurt (actor 1, community); Ganger_Catwalk (actor 2, community); Ganger_Catwalk_Hall_01 (actor 3, community); Ganger_Catwalk_Hall_02 (actor 4, community); Lars (actor 5, community); Ganger_Catwalk_Scene_01 (actor 6, community); Ganger_Catwalk_Scene_02 (actor 7, community); Player (actor 8, findInContext).

Entries: `q003_maelstrom_corridor_p2_in` → 744; `q003_02_riding_elevator_in` → 976.

Exits: `q003_maelstrom_corridor_p2_out` → 43; `q003_02_riding_elevator_out` → 973.

End nodes: 43: `NonTerminating`; 973: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 252 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnChangeIdleAnimEvent` | 2 | 252 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scnDialogLineEvent` | 20 | 272 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnLookAtEvent` | 11 | 252 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 8 | 252 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsSocket` | 6 | 252 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scneventsVFXDurationEvent` | 1 | 252 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, gaze: 3
- gaze: 2
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, socket_signal: 1
- idle_animation, gaze: 1

Raw SHA-256: `3290c65fbc6eec8735fa04d81d92bc17f2eefc03afb4199337ef90468cb4cb58`. Binary SHA-256: `2ed9dd67db26ca530239ca899176a3f11927eee918ceacc302a1e514dd6bd8fb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_02_maelstrom_corridor_part2.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_02_no_deal.scene`

119 graph nodes, 117 edges; 20 event-bearing sections, 77 events; 35 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Jackie (actor 0, spawnSet); DumDum (actor 1, spawnSet); Royce (actor 2, spawnDespawn); Netrunner (actor 3, community); Executioner (actor 4, community); Player (actor 5, findInContext).

Entries: `q003_02_die_fuckers_in` → 1; `q003_02_dumdum_kill_intruders_in` → 7; `q005_01_plan_lets_see_in` → 342; `q003_02_mealstrom_dead_in` → 12; `q003_02_mealstrom_dead_elevator_in` → 17; `q003_02_mealstrom_more_office_in` → 22; `q003_02_royce_no_deal_in` → 27; `q003_02_open_world_mealstrom_attacked_in` → 270; `royce_footage_preview` → 396; `q003_02_jackie_shooting_dumdum_in` → 92.

Exits: `q003_02_die_fuckers_out` → 2; `q003_02_dumdum_kill_intruders_out` → 8; `q005_01_plan_lets_see_out` → 343; `q003_02_mealstrom_dead_out` → 13; `q003_02_mealstrom_dead_elevator_out` → 18; `q003_02_mealstrom_more_office_out` → 23; `q003_02_royce_no_deal_out` → 28; `q003_02_open_world_mealstrom_attacked_out` → 272; `q003_02_jackie_shooting_dumdum_out` → 93.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 13: `<omitted>`; 18: `<omitted>`; 23: `<omitted>`; 28: `<omitted>`; 93: `<omitted>`; 272: `<omitted>`; 343: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 134 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/2` |
| `scnChangeIdleAnimEvent` | 11 | 29 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scnDialogLineEvent` | 30 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 11 | 29 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/11` |
| `scnPlaySkAnimEvent` | 10 | 29 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scneventsCameraEvent` | 1 | 416 / 367 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 416 / 369 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/1` |
| `scneventsSocket` | 12 | 29 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- idle_animation, gaze, camera, socket_signal: 1

Raw SHA-256: `8074335ed27c15e734f61cbfdf691178d02b63bd8d8558c80538fb15e4dbf8a9`. Binary SHA-256: `b3cb9997b0fa1ca3af0b33d7418debde728e8a2b40e8a59f104ef0e26649c1e3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_02_no_deal.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_03_deal.scene`

668 graph nodes, 853 edges; 96 event-bearing sections, 1377 events; 213 screenplay lines, 32 screenplay options, 14 choice nodes.

Actors: Royce (actor 0, spawnSet); Lars (actor 1, community); Jackie (actor 2, spawnSet); DumDum (actor 3, spawnSet); Kurt (actor 4, community); Netrunner (actor 5, community); spiderbot (actor 6, community); spiderbot_case (actor 7, community); Player (actor 8, findInContext).

Entries: `q003_03_deal_in` → 2771; `standoff_preview` → 8616; `Start 32` → 9144; `q003_03_brick_killed_in` → 8109; `royce_enters_preview` → 8639; `trailer_prev` → 10218; `post_deal_dialogue_preview` → 8660; `sitting_with_dum_prev` → 9229; `royce_backroom_prev` → 8890.

Exits: `q003_03_deal_peaceful_out` → 5809; `q003_03_deal_hostile_out` → 9019; `Kill Signal Peaceful` → 9034; `q003_03_deal_militech_chip_out` → 2792; `q003_03_brick_killed_out` → 8110; `Kill Signal Hostile` → 7233.

End nodes: 2792: `NonTerminating`; 5809: `NonTerminating`; 7233: `<omitted>`; 8110: `<omitted>`; 9019: `<omitted>`; 9034: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 101 | 3863 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/9` |
| `scnChangeIdleAnimEvent` | 79 | 3835 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnDialogLineEvent` | 175 | 3835 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scnGameplayTransitionEvent` | 29 | 3888 / 340 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/43` |
| `scnIKEvent` | 58 | 3888 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/5` |
| `scnLookAtAdvancedEvent` | 6 | 3863 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/59` |
| `scnLookAtEvent` | 197 | 3835 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnPlayRidAnimEvent` | 1 | 7322 / 2178 | `/Data/RootChunk/sceneGraph/Data/graph/146/Data/events/2` |
| `scnPlaySkAnimEvent` | 286 | 3835 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPoseCorrectionEvent` | 4 | 3835 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scnUnmountEvent` | 29 | 3888 / 341 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/44` |
| `scneventsAttachPropToNode` | 1 | 6476 / 1264 | `/Data/RootChunk/sceneGraph/Data/graph/74/Data/events/5` |
| `scneventsAttachPropToPerformer` | 20 | 3835 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsAttachPropToWorld` | 7 | 3863 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 29 | 3888 / 338 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/42` |
| `scneventsSocket` | 305 | 3835 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scneventsVFXDurationEvent` | 9 | 3863 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/17` |
| `scneventsVFXEvent` | 41 | 3835 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- speech, skeletal_animation: 6
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 5
- speech, skeletal_animation, socket_signal: 5
- idle_animation: 5
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- gaze: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, audio, vfx, socket_signal: 2
- skeletal_animation, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- idle_animation, audio: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- speech, audio: 1
- skeletal_animation, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, rid_actor, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal, animation_state: 1
- idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- idle_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- vfx: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `8cee04932d57d0b16dc65d5dd4fe0e6974baf97ac5f9528967b06e50316f90c2`. Binary SHA-256: `bdf35602e6e3b5ccca2f3a2c51a3a6deee48fa2a7239a2154a237f26a9729dd7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_03_deal.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_03a_militech_invades.scene`

334 graph nodes, 390 edges; 51 event-bearing sections, 299 events; 78 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Jackie (actor 0, spawnSet); Spiderbot_case (actor 1, findInWorld); spiderbot (actor 2, findInWorld); DumDum (actor 3, spawnSet); Ganger_Garage_Scene_01 (actor 4, community); Ganger_Garage_Scene_02 (actor 5, community); Ganger_Garage_Scene_03 (actor 6, community); Kurt (actor 7, community); Lars (actor 8, community); Player (actor 9, findInContext).

Entries: `Start 6` → 2112; `q003_03a_militech_invades_in` → 45; `walk_downstairs_preview` → 1875; `preview` → 2824; `inhaler_give_preview` → 1969; `linestoreuse` → 2639.

Exits: `q003_03a_militech_invades_out` → 46; `q003_03a_kill_signal_out` → 1044; `q003_03a_dumdum_walks_out_out` → 171; `Kill Signal` → 1461.

End nodes: 46: `NonTerminating`; 171: `NonTerminating`; 1044: `<omitted>`; 1461: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 118 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnDialogLineEvent` | 57 | 118 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/6` |
| `scnGameplayTransitionEvent` | 14 | 118 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/18` |
| `scnIKEvent` | 28 | 118 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnLookAtEvent` | 31 | 118 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnPlaySkAnimEvent` | 58 | 118 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scnUnmountEvent` | 14 | 118 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/19` |
| `scneventsAttachPropToNode` | 1 | 1594 / 968 | `/Data/RootChunk/sceneGraph/Data/graph/129/Data/events/5` |
| `scneventsAttachPropToPerformer` | 2 | 940 / 609 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 14 | 118 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/16` |
| `scneventsSocket` | 60 | 118 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/11` |
| `scneventsVFXEvent` | 14 | 124 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, skeletal_animation: 5
- skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze: 4
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, vfx: 1
- gaze: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `f3da32b37310bf4e0c56ab2a64b6d509ad70e0af719359a3fb5c172e5b704834`. Binary SHA-256: `500d73e1c984cd3aa75d70686d341dd185b1d4f85ca1213d27a3a018c5e8f742`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_03a_militech_invades.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_03b_escape_office.scene`

114 graph nodes, 136 edges; 16 event-bearing sections, 36 events; 21 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Jackie (actor 0, spawnSet); DumDum (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `q003_03b_escape_office_no_sit_in` → 2068; `q003_garage_enought_in` → 2194; `q003_03_kill_fuckers_in` → 1348; `q003_03b_escape_office_in` → 1354.

Exits: `q003_garage_enought_out` → 2195; `q003_03_kill_fuckers_out` → 1349; `q003_03b_escape_office_out` → 1355.

End nodes: 1349: `<omitted>`; 1355: `NonTerminating`; 2195: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 21 | 108 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsVFXEvent` | 15 | 1516 / 185 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, vfx: 1

Raw SHA-256: `d89d573d22b5235ebdb6e33d9e6304b267d335cc9095d5b7d4535ecc47dde86d`. Binary SHA-256: `48a7642cb053d29c36fc1d707e1c96cd44b441a1be7d85e8427c187f9d4c0060`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_03b_escape_office.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_04d_shootout_militech.scene`

264 graph nodes, 318 edges; 37 event-bearing sections, 81 events; 57 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: Jackie (actor 0, spawnSet); DumDum (actor 1, spawnSet); Militech1 (actor 2, community); Militech2 (actor 3, community); Militech3 (actor 4, community); Militech4 (actor 5, community); Militech5 (actor 6, findInWorld); Militech6 (actor 7, findInWorld); Militech7 (actor 8, findInWorld); Militech8 (actor 9, findInWorld); Militech9 (actor 10, findInWorld); Royce (actor 11, spawnSet); Militech10 (actor 12, findInWorld); Militech11 (actor 13, findInWorld); Militech12 (actor 14, findInWorld); Militech13 (actor 15, community); Militech14 (actor 16, community); MilitechMech1 (actor 17, community); MilitechMech2 (actor 18, community); Player (actor 19, findInContext).

Entries: `q003_04d_kill_militech_in` → 15; `q003_04d_militech_garage_secured_in` → 281; `q003_04d_militech_about_cargo_in` → 44; `q003_04d_militech_found_cargo_in` → 58; `q003_04d_militech_vs_royce_in` → 69; `approaching_exit_prev` → 1644; `giving_skeef_prev` → 995.

Exits: `q003_04d_kill_militech_out` → 16; `q003_04d_militech_garage_secured_out` → 282; `q003_04d_militech_about_cargo_Out` → 45; `q003_04d_militech_found_cargo_out` → 59; `q003_04d_militech_vs_royce_out` → 70.

End nodes: 16: `<omitted>`; 45: `<omitted>`; 59: `<omitted>`; 70: `NonTerminating`; 282: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 631 / 393 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/1` |
| `scnDialogLineEvent` | 53 | 17 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 852 / 620 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/7` |
| `scnIKEvent` | 2 | 852 / 613 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/1` |
| `scnLookAtEvent` | 2 | 631 / 401 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/4` |
| `scnPlaySkAnimEvent` | 7 | 631 / 394 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/2` |
| `scnUnmountEvent` | 1 | 852 / 619 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/6` |
| `scneventsAttachPropToPerformer` | 2 | 631 / 400 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 842 / 590 | `/Data/RootChunk/sceneGraph/Data/graph/119/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 852 / 617 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/5` |
| `scneventsSocket` | 10 | 17 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 31
- skeletal_animation, socket_signal: 2
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `6abf29d0e36b047a87e0c0425c634fefc255eef6ab722c6cc42860ab60b3c756`. Binary SHA-256: `2b5fc7f0f2002e77d5617e2f50c7796c9ac39c8c9e274c66c6fa9047e26bf30a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_04d_shootout_militech.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_04e_pre_combat_patrol_dialogues.scene`

27 graph nodes, 18 edges; 9 event-bearing sections, 22 events; 22 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: main_enemy_008_rifle (actor 0, community); main_enemy_007_rifle (actor 1, community); transition_enemy_014_shotgun (actor 2, community); transition_enemy_015_shotgun (actor 3, community); transition_enemy_officer_001_rifle (actor 4, community); lab_enemy_006_rifle (actor 5, community); lab_enemy_005_rifle (actor 6, community); Jackie (actor 7, spawnSet); Player (actor 8, findInContext).

Entries: `enemy_14_15_officer_01` → 1; `jackie_transition_hide` → 29; `enemy_07_08` → 6; `jackie_transition_double_takedown` → 34; `enemy_06_05` → 13; `enemy_015_looking_for_013` → 41; `enemy_015_raising_alarm` → 42; `jackie_avoids_routine_007_008` → 17; `jackie_lab_cleared` → 25.

Exits: `jackie_lab_cleared_out` → 27; `enemy_14_15_officer_01_out` → 2; `jackie_transition_hide_out` → 31; `enemy_07_08_out` → 7; `jackie_transition_double_takedown_out` → 36; `enemy_06_05_out` → 14; `enemy_015_looking_for_013_out` → 43; `enemy_015_raising_alarm_out` → 44; `jackie_avoids_routine_007_008_out` → 18.

End nodes: 2: `<omitted>`; 7: `<omitted>`; 14: `<omitted>`; 18: `<omitted>`; 27: `<omitted>`; 31: `<omitted>`; 36: `<omitted>`; 43: `<omitted>`; 44: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 22 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9

Raw SHA-256: `31ddddd8a393c6d4f03f27060abf84fcf2a720842086ca1b22a7ca6a04c74451`. Binary SHA-256: `4ae71f7f32a9f100d3e46929b28b56014ed23ddec62f01ca69175fc6bc0742ef`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_04e_pre_combat_patrol_dialogues.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_05_transition.scene`

223 graph nodes, 273 edges; 36 event-bearing sections, 217 events; 58 screenplay lines, 11 screenplay options, 6 choice nodes.

Actors: Jackie (actor 0, spawnSet); transition_enemy_014_shotgun (actor 1, community); transition_enemy_officer_001_rifle (actor 2, community); transition_enemy_013_shotgun (actor 3, findInWorld); Brick (actor 4, spawnSet); Player (actor 5, findInContext).

Entries: `q003_05_convoy_signatures_in` → 398; `q003_05_brick_prison_in` → 404; `brick_dialogue_preview` → 1246; `detonator_interaction` → 1248; `q003_03_tranisition_chat_in` → 298; `linestoreuse` → 1089; `q003_05_attack_in` → 326; `q003_05_enter_garage_in` → 350; `q003_05_come_on_in` → 385; `q003_05_close_to_exit_in` → 390.

Exits: `q003_05_convoy_signatures_out` → 399; `q003_03_tranisition_chat_out` → 354; `q003_05_brick_prison_out` → 564; `q003_05_attack_out` → 378; `q003_05_enter_garage_out` → 382; `q003_05_come_on_out` → 386; `q003_05_close_to_exit_out` → 391.

End nodes: 354: `<omitted>`; 378: `<omitted>`; 382: `<omitted>`; 386: `<omitted>`; 391: `<omitted>`; 399: `<omitted>`; 564: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 917 / 838 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/6` |
| `scnChangeIdleAnimEvent` | 7 | 467 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/4` |
| `scnDialogLineEvent` | 48 | 297 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnGameplayTransitionEvent` | 10 | 695 / 484 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/15` |
| `scnIKEvent` | 20 | 695 / 463 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/1` |
| `scnLookAtEvent` | 24 | 349 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 35 | 297 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnUnmountEvent` | 10 | 695 / 483 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/14` |
| `scneventsAttachPropToPerformer` | 1 | 680 / 446 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/5` |
| `scneventsAttachPropToWorld` | 3 | 909 / 810 | `/Data/RootChunk/sceneGraph/Data/graph/110/Data/events/10` |
| `scneventsCameraParamsEvent` | 3 | 680 / 437 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 10 | 695 / 479 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/11` |
| `scneventsSocket` | 45 | 417 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 7
- speech: 5
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment: 1

Raw SHA-256: `bff1751d1d36ee82a4b3814f4fc8e35ad8eca3ff07724354e376b5cde947e383`. Binary SHA-256: `12ba4227d328e7421078165cda86b58d7d558ed7be6bba8f2b5777578318d528`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_05_transition.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_06a_boss_combat.scene`

89 graph nodes, 85 edges; 27 event-bearing sections, 80 events; 31 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Shotgunner_Maelstrommer (actor 0, community); Jackie (actor 1, spawnSet); Royce (actor 2, spawnSet); Cable_Maelstrommer (actor 3, community); Player (actor 4, findInContext).

Entries: `q003_06a_royce_dead_in` → 356; `q003_06a_boss_scene_in` → 1; `linestoreuse` → 546; `q003_06a_entering_arena_in` → 552; `royce_hp_comments` → 112; `q003_06a_leave_garage_in` → 394; `q003_06a_leave_fence_in` → 399; `royce_first_beam_attack` → 165; `royce_first_projectile` → 166; `royce_shield_broken` → 167; `royce_player_too_close` → 168; `royce_after_close_beam_attack` → 169; `royce_player_dead` → 170; `jackie_weak_spot` → 171; `q003_05_jackie_car_throw_in` → 172.

Exits: `q003_06a_royce_dead_out` → 357; `q003_06a_entering_arena_out` → 553; `royce_hp_comments_out` → 114; `q003_06a_leave_garage_out` → 395; `q003_06a_leave_fence_out` → 400; `royce_first_beam_attack_end` → 233; `royce_first_projectile_end` → 236; `royce_shield_broken_end` → 239; `royce_player_too_close_end` → 242; `royce_after_close_beam_attack_end` → 245; `royce_player_dead_end` → 248; `jackie_weak_spot_end` → 251; `q003_06a_boss_scene_out` → 260; `q003_05_jackie_car_throw_out` → 351.

End nodes: 114: `<omitted>`; 233: `<omitted>`; 236: `<omitted>`; 239: `<omitted>`; 242: `<omitted>`; 245: `<omitted>`; 248: `<omitted>`; 251: `<omitted>`; 260: `NonTerminating`; 351: `<omitted>`; 357: `<omitted>`; 395: `<omitted>`; 400: `<omitted>`; 553: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 19 | 3 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scnChangeIdleAnimEvent` | 4 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnDialogLineEvent` | 30 | 3 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnLookAtEvent` | 1 | 3 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |
| `scnPlaySkAnimEvent` | 5 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 5 | 3 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scneventsVFXEvent` | 16 | 3 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 23
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, vfx: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `e21746ff4bb28d51693dbe166ab758b15b8402830ea7828fa655609ff5f5eb7d`. Binary SHA-256: `3c7cff197b7ea03e8ca015e70038bebca98aa3f0948a249cf4a865117cb7d1b2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_06a_boss_combat.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_07_final.scene`

70 graph nodes, 78 edges; 12 event-bearing sections, 95 events; 24 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Jackie (actor 0, spawnSet); jackie_bike (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `q003_07_final_in` → 1; `jackie_ride_off` → 223.

Exits: `q003_07_final_out` → 2; `KillSignal` → 44.

End nodes: 2: `NonTerminating`; 44: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 51 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/5` |
| `scnChangeIdleAnimEvent` | 10 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnDialogLineEvent` | 21 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 75 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/8` |
| `scnIKEvent` | 2 | 75 / 213 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/1` |
| `scnLookAtEvent` | 5 | 51 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 51 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/7` |
| `scnPlaySkAnimEvent` | 20 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnUnmountEvent` | 1 | 75 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 9 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSocket` | 22 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 5
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1

Raw SHA-256: `755616970d0ef8b1bf28724b5c10aff476690327609d2301d6d2911e9c0801f2`. Binary SHA-256: `8f6343bde45977f09a5298e1534bbaf226008f1870e6c5870d6587d75e7cfaa8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_07_final.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_07a_final_corp.scene`

301 graph nodes, 351 edges; 41 event-bearing sections, 310 events; 80 screenplay lines, 12 screenplay options, 6 choice nodes.

Actors: Jackie (actor 0, spawnSet); Meredith (actor 1, spawnSet); Bodyguard_01 (actor 2, community); Bodyguard_02 (actor 3, community); suv (actor 4, community); militech_soldier1 (actor 5, community); militech_soldier2 (actor 6, community); militech_soldier3 (actor 7, community); militech_soldier4 (actor 8, community); militech_soldier5 (actor 9, community); militech_soldier6 (actor 10, community); militech_drone (actor 11, community); Johnny (actor 12, spawnSet); Meredith_holocall (actor 13, spawnSet); jackie_bike (actor 14, spawnSet); av1 (actor 15, community); av2 (actor 16, community); Player (actor 17, findInContext).

Entries: `q003_07a_finale_in` → 1; `q003_07a_drone_in` → 1495; `jackie_bye_preview` → 2708; `q003_07a_stout_corpse_in` → 2152; `q003_07a_stout_sex_end_in` → 2197; `q003_militech_pushback_in` → 2560; `Start 14` → 2869; `q003_07a_stout_holocall_in` → 2286; `meredith_holocall_preview` → 2606; `Start 15` → 2936.

Exits: `q003_07a_finale_out` → 4; `KillSignal` → 2091; `q003_07a_stout_corpse_out` → 2153; `q003_07a_stout_sex_end_out` → 2200; `q003_07a_drone_jackie_out` → 2024; `q003_07a_stout_runn_off_out` → 2321.

End nodes: 4: `NonTerminating`; 2024: `NonTerminating`; 2091: `<omitted>`; 2153: `<omitted>`; 2200: `<omitted>`; 2321: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 31 | 319 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnChangeIdleAnimEvent` | 24 | 116 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnDialogLineEvent` | 65 | 105 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 1977 / 550 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/17` |
| `scnIKEvent` | 10 | 1977 / 541 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/9` |
| `scnLookAtEvent` | 32 | 105 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 70 | 105 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 5 | 1977 / 549 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/16` |
| `scneventsAttachPropToPerformer` | 6 | 505 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 1977 / 545 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/13` |
| `scneventsSocket` | 45 | 105 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXDurationEvent` | 2 | 319 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |
| `scneventsVFXEvent` | 10 | 319 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 6
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation: 4
- speech: 4
- speech, idle_animation, gaze: 3
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 2
- skeletal_animation, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `ca0cc3b04c5c44a13cb79e0d12ff6679c2f41e3b8a5dae28cb48bd1c1e61ade3`. Binary SHA-256: `d3435d0eae2d629a19021d10eee06fd77998321ee629c0d1cd1c319c6eb460d5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_07a_final_corp.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_07aa_final_traitor.scene`

364 graph nodes, 417 edges; 50 event-bearing sections, 406 events; 92 screenplay lines, 11 screenplay options, 5 choice nodes.

Actors: Anthony (actor 0, spawnSet); Jackie (actor 1, spawnSet); bodyguard1 (actor 2, community); bodyguard2 (actor 3, community); soldier1 (actor 4, community); soldier2 (actor 5, community); soldier3 (actor 6, community); soldier4 (actor 7, community); soldier5 (actor 8, community); soldier6 (actor 9, community); Johnny (actor 10, spawnSet); soldier7 (actor 11, community); soldier8 (actor 12, community); soldier9 (actor 13, community); soldier10 (actor 14, community); Anthony_holocall (actor 15, spawnSet); drone (actor 16, community); jackie_bike (actor 17, spawnSet); av1 (actor 18, community); av2 (actor 19, community); q003_suv (actor 20, community); Player (actor 21, findInContext).

Entries: `q003_07_traitor_in` → 1; `av_arrival_preview` → 1503; `Start 5` → 1580; `q003_07aa_gilchrist_holocall_in` → 1025; `jackie_talk_preview` → 1346; `gilchrist_holocall_preview` → 1373; `q003_07aa_gilchrist_corpse_in` → 799.

Exits: `q003_07_traitor_out` → 2; `q003_soldier_pushback_out` → 1290; `q003_07a_gilchrist_runn_off_out` → 1039; `KillSignal` → 754; `q003_07aa_gilchrist_corpse_out` → 800.

End nodes: 2: `NonTerminating`; 754: `<omitted>`; 800: `<omitted>`; 1039: `NonTerminating`; 1290: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 431 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/4` |
| `scnChangeIdleAnimEvent` | 17 | 3 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 69 | 3 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnGameplayActionEvent` | 2 | 1623 / 1978 | `/Data/RootChunk/sceneGraph/Data/graph/256/Data/events/2` |
| `scnGameplayTransitionEvent` | 7 | 381 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/9` |
| `scnIKEvent` | 14 | 381 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnLookAtAdvancedEvent` | 10 | 925 / 740 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/15` |
| `scnLookAtEvent` | 56 | 3 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 82 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 7 | 381 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |
| `scneventsAttachPropToPerformer` | 6 | 433 / 145 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 7 | 381 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scneventsSocket` | 111 | 3 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 6 | 431 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation: 2
- speech, gaze: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- idle_animation, gaze, socket_signal, gameplay_action: 1

Raw SHA-256: `489e8d61e95f85997d1be85ea1a0953b16746482c7b3f8e4b5aa2140ec6e2a12`. Binary SHA-256: `b7ebbe3e1c42af9b1ff0f9d08763973487101517857c130e6724add32000c79b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_07aa_final_traitor.scene" --events
```

## `base\quest\main_quests\prologue\q004\scenes\q004_07_lets_meet_dex.scene`

89 graph nodes, 111 edges; 27 event-bearing sections, 78 events; 65 screenplay lines, 7 screenplay options, 2 choice nodes.

Actors: dex (actor 0, spawnSet); jackie (actor 1, spawnSet); v (actor 2, findInContext).

Entries: `callin_dex` → 1; `q005_01_plan_and_flathead_in` → 416; `dex_holocall_preview` → 421; `linestobereused` → 725.

Exits: `callin_dex_out` → 2; `q005_01_plan_and_flathead_out` → 417.

End nodes: 2: `<omitted>`; 417: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 17 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 62 | 3 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 2 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 7 | 29 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scneventsAttachPropToPerformer` | 1 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraEvent` | 1 | 431 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/0` |
| `scneventsSocket` | 2 | 132 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- speech, skeletal_animation: 4
- speech, idle_animation: 2
- speech, gaze, props_equipment: 1
- idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, socket_signal: 1
- camera: 1

Raw SHA-256: `d38aae843999f93b05302e429c4d03e3bb0f814e041140850ed2270024089804`. Binary SHA-256: `f4d0d54e9a58978be46ca0579059e87266bc8af982fa1abd962bfe76777ab21a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q004\scenes\q004_07_lets_meet_dex.scene" --events
```

