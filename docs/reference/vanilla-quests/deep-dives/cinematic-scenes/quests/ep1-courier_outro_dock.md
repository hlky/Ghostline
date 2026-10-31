# Baby Let Me Take You: scene presentation

Journal identity: `ep1/quests/sandbox_activities/courier_outro_dock`. Stored type: **CourierSideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-courier_outro_dock.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\sandbox_activities\courier_spot\outro_quest\outro_dock\scenes\daniels_ambush\sa_ep1_courier_outro_daniels_ambush.scene`

208 graph nodes, 231 edges; 35 event-bearing sections, 122 events; 51 screenplay lines, 9 screenplay options, 6 choice nodes.

Actors: daniels_voice (actor 0, findInContext); daniels (actor 1, community); fixer_voice (actor 2, findInContext); arasaka_truck (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `i_see_you` → 1; `input_end_call_no_line` → 1009; `daniels_afterbrief` → 216; `garage_no_enemies` → 618; `daniels_after_save` → 23; `fight_started_no_meeting` → 631; `v_truck_found` → 32; `daniels_ambushed` → 33; `Fight_started` → 255; `V_leaving_zone` → 261; `muammar_call_road` → 291; `garage_ambush` → 313; `daniels_dock_meeting` → 142; `equipment damaged` → 357; `chase_info` → 974; `aftersave_goaway` → 183.

Exits: `i_see_you_end` → 2; `output_end call no line` → 1013; `garage_no_enemies_end` → 625; `aftersave_dialogue` → 28; `daniel_ambushed_end` → 1033; `fight started no meeting end` → 634; `End 2` → 36; `truck_found` → 41; `instant` → 449; `End 12` → 256; `v_leaving_docks_end` → 262; `muammar_road_end` → 292; `garage_ambush_talkend` → 314; `daniels_dock_meeting_done` → 143; `equipment damaged end` → 359; `chase info end` → 975.

End nodes: 2: `NonTerminating`; 28: `NonTerminating`; 36: `<omitted>`; 41: `NonTerminating`; 143: `NonTerminating`; 256: `NonTerminating`; 262: `NonTerminating`; 292: `<omitted>`; 314: `<omitted>`; 359: `<omitted>`; 449: `NonTerminating`; 625: `<omitted>`; 634: `NonTerminating`; 975: `<omitted>`; 1013: `<omitted>`; 1033: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 26 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnDialogLineEvent` | 43 | 16 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 25 | 26 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnPlaySkAnimEvent` | 26 | 26 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsEquipItemToPerformer` | 3 | 279 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/16` |
| `scneventsSocket` | 19 | 26 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 1 | 346 / 218 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/7` |
| `scneventsVFXEvent` | 1 | 1091 / 791 | `/Data/RootChunk/sceneGraph/Data/graph/157/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- speech, gaze: 4
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, socket_signal: 1
- props_equipment, socket_signal: 1
- idle_animation, gaze: 1
- gaze, vfx: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `150331a47b64b0cb28736ccb3a64b97ad4c3407902363bcf6cb065d2653e00ab`. Binary SHA-256: `0f9e037908e060364c6515093413d0d9d3765981c2e2964aed18cd929bfa7290`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\sandbox_activities\courier_spot\outro_quest\outro_dock\scenes\daniels_ambush\sa_ep1_courier_outro_daniels_ambush.scene" --events
```

## `ep1\openworld\sandbox_activities\courier_spot\outro_quest\outro_dock\scenes\muammar_end\sa_ep1_courier_outro_end.scene`

83 graph nodes, 97 edges; 22 event-bearing sections, 156 events; 36 screenplay lines, 8 screenplay options, 3 choice nodes.

Actors: fixer (actor 0, spawnSet); worker (actor 1, community); reward_car (actor 2, community); car (actor 3, spawnSet); nicecar (actor 4, community); Player (actor 5, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `move_truck` → 80.

End nodes: 2: `NonTerminating`; 80: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 10 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 25 | 10 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 63 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/16` |
| `scnIKEvent` | 6 | 63 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |
| `scnLookAtEvent` | 34 | 10 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 46 | 10 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 3 | 63 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/15` |
| `scneventsEquipItemToPerformer` | 3 | 384 / 417 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 3 | 63 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |
| `scneventsSocket` | 22 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 1 | 384 / 419 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, gaze: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation: 1
- gaze, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `2517d95d43f0839d32a57a883e6c03d9bc1bc479e4b6bed74612e90c75417cc1`. Binary SHA-256: `89c26de23211f8ccd30282ef401d156a2d4099cf5e865da7aa7016bc59fd90ae`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\sandbox_activities\courier_spot\outro_quest\outro_dock\scenes\muammar_end\sa_ep1_courier_outro_end.scene" --events
```

## `ep1\openworld\sandbox_activities\courier_spot\outro_quest\outro_dock\scenes\muammar_ride_holocall\sa_ep1_outro_muamar_ride_holocall.scene`

57 graph nodes, 63 edges; 8 event-bearing sections, 12 events; 12 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer_voice (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `combat_near_muamar_end` → 2; `no_combat_near_muamar_end` → 175.

End nodes: 2: `<omitted>`; 175: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 12 | 91 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8

Raw SHA-256: `ba5cad7f8e561eff0c4d44ab571c5b091414af9df0ab400ff9f74a854651a7e4`. Binary SHA-256: `b0cc078d042dcc6acdc8c4f62c6ed789cd9537893da5230b0e9bf36d05f73b44`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\sandbox_activities\courier_spot\outro_quest\outro_dock\scenes\muammar_ride_holocall\sa_ep1_outro_muamar_ride_holocall.scene" --events
```

## `ep1\openworld\sandbox_activities\courier_spot\outro_quest\outro_dock\scenes\muammar_start_dam_meetup\sa_ep1_courier_outro_muammar_dam.scene`

117 graph nodes, 149 edges; 31 event-bearing sections, 297 events; 61 screenplay lines, 14 screenplay options, 7 choice nodes.

Actors: fixer (actor 0, spawnSet); daniels (actor 1, community); johnny (actor 2, spawnDespawn); police (actor 3, community); car (actor 4, community); Player (actor 5, findInContext).

Entries: `Start 0` → 1; `talk_interaction` → 874.

Exits: `mummar_alldone` → 2; `all done_johny_despawn` → 840; `hide_ui_loop_end` → 1129; `police car leaves` → 787.

End nodes: 2: `NonTerminating`; 787: `NonTerminating`; 840: `NonTerminating`; 1129: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 136 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scnChangeIdleAnimEvent` | 10 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 43 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 203 / 454 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/14` |
| `scnIKEvent` | 6 | 203 / 447 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/8` |
| `scnLookAtEvent` | 80 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 2 | 128 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/12` |
| `scnPlaySkAnimEvent` | 87 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 4 | 172 / 349 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/9` |
| `scnUnmountEvent` | 3 | 203 / 453 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/13` |
| `scneventsCameraParamsEvent` | 4 | 947 / 912 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/3` |
| `scneventsEquipItemToPerformer` | 2 | 965 / 953 | `/Data/RootChunk/sceneGraph/Data/graph/96/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 3 | 203 / 449 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/10` |
| `scneventsSocket` | 45 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 1 | 965 / 955 | `/Data/RootChunk/sceneGraph/Data/graph/96/Data/events/7` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 136 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 6
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, socket_signal: 1
- gaze: 1
- socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- speech, gaze: 1

Raw SHA-256: `503c1108095f5aaada1d6927c875336a5e0331326f9ea3aea6cbf7268f311ffa`. Binary SHA-256: `704bb383687039e5e2523428b231246197407336d94e86e6e536c112b03cb0d2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\sandbox_activities\courier_spot\outro_quest\outro_dock\scenes\muammar_start_dam_meetup\sa_ep1_courier_outro_muammar_dam.scene" --events
```

## `ep1\openworld\sandbox_activities\courier_spot\outro_quest\outro_dock\scenes\muammar_start_holocall\sa_ep1_courier_outro_muammar_start.scene`

20 graph nodes, 21 edges; 3 event-bearing sections, 6 events; 6 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 10.

Exits: `End 0` → 21; `rejected_out` → 45.

End nodes: 21: `<omitted>`; 45: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 35 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `b9d76ddcb7d9a8c13cfbd7cdf2a7ce57b12cd08dae62e78894086830c60df76c`. Binary SHA-256: `e76a4efc286bbffaa1395f455938786f77eb9283e5ca72f12efbe87519bff9c2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\sandbox_activities\courier_spot\outro_quest\outro_dock\scenes\muammar_start_holocall\sa_ep1_courier_outro_muammar_start.scene" --events
```

