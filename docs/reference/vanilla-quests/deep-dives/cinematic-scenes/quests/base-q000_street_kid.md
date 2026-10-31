# The Streetkid: scene presentation

Journal identity: `quests/main_quest/prologue/q000_street_kid`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q000_street_kid.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q115\scenes\q115_00_johnny.scene`

175 graph nodes, 235 edges; 50 event-bearing sections, 331 events; 122 screenplay lines, 25 screenplay options, 7 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 15` → 3120; `Start 16` → 3122; `Start 0` → 2969; `Start 13` → 2628; `q000_car_line_reuse` → 2841; `elevator_in` → 1779.

Exits: `q000_car_line_reuse_end` → 2843; `elevator_out` → 1780.

End nodes: 1780: `<omitted>`; 2843: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 2243 / 484 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/3` |
| `scnChangeIdleAnimEvent` | 26 | 1818 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 99 | 1782 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 2218 / 469 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/15` |
| `scnIKEvent` | 8 | 2218 / 466 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/12` |
| `scnLookAtEvent` | 28 | 1826 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/15` |
| `scnPlaySkAnimEvent` | 54 | 1822 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnUnmountEvent` | 4 | 2218 / 468 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/14` |
| `scneventsAttachPropToNode` | 2 | 2243 / 483 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/2` |
| `scneventsAttachPropToPerformer` | 4 | 2409 / 547 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/2` |
| `scneventsCameraParamsEvent` | 3 | 2218 / 462 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 4 | 2218 / 463 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/10` |
| `scneventsSocket` | 84 | 1818 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scneventsVFXEvent` | 3 | 2218 / 449 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- speech: 5
- speech, idle_animation, socket_signal: 4
- speech, idle_animation: 3
- speech, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, socket_signal: 2
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- gaze, socket_signal: 2
- skeletal_animation, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `9b6ce12f5753742524ff7b6e7533bca1f515afb1977ce975c26a41de6bfc8dcd`. Binary SHA-256: `aee544c6cc434ac5af2256f8b73db5bee8ec3b5d9502d0d1a25ab1c2483f1b23`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_00_johnny.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_01b_meet_your_fixer.scene`

334 graph nodes, 408 edges; 60 event-bearing sections, 647 events; 101 screenplay lines, 29 screenplay options, 18 choice nodes.

Actors: kirk_sawyer (actor 0, spawnSet); bartender (actor 1, spawnSet); big_joe (actor 2, community); v_male_tpp (actor 3, spawnDespawn); v_female_tpp (actor 4, spawnDespawn); Player_fpp (actor 5, findInContext).

Entries: `Meet_Your_Fixer_In` → 1; `coyote_performance_test` → 1743; `q000_pepe_after_kirk` → 1302; `mq017_reminder_in` → 1831; `kirk_preview` → 371.

Exits: `Meet_Your_Fixer_Out` → 2; `activate_chats` → 364.

End nodes: 2: `NonTerminating`; 364: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 28 | 62 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnChangeIdleAnimEvent` | 43 | 62 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 101 | 60 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 179 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scnIKEvent` | 10 | 179 / 337 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 159 / 300 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/32` |
| `scnLookAtEvent` | 105 | 62 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 164 | 60 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 5 | 179 / 357 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/15` |
| `scneventsAttachPropToNode` | 1 | 848 / 1654 | `/Data/RootChunk/sceneGraph/Data/graph/135/Data/events/6` |
| `scneventsAttachPropToPerformer` | 16 | 159 / 275 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/15` |
| `scneventsAttachPropToWorld` | 14 | 62 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scneventsCameraParamsEvent` | 19 | 154 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 5 | 179 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/12` |
| `scneventsSocket` | 123 | 60 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsVFXEvent` | 6 | 197 / 378 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- gaze: 7
- camera: 6
- speech, gaze: 4
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `6fdc79f6cae99f93b73f2970fa5e5e18ed0d0a279763f8c5fa5a149bea4fe590`. Binary SHA-256: `afdad5ffee1d0b1535ec9cfac659e31622c0298d12a7fe6aaab299c8fa1bd855`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_01b_meet_your_fixer.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_01c_car.scene`

269 graph nodes, 337 edges; 59 event-bearing sections, 494 events; 105 screenplay lines, 12 screenplay options, 9 choice nodes.

Actors: Padre (actor 0, spawnSet); Marcus (actor 1, community); 6h_street_ganger (actor 2, community); 6th_street_trunk (actor 3, spawnDespawn); 6th_street_ganger_02 (actor 4, community); embers_worker (actor 5, community); embers_homeless (actor 6, community); padre_car (actor 7, spawnSet); 6th_street_car (actor 8, spawner); av_lux (actor 9, spawner); Player (actor 10, findInContext).

Entries: `Start 0` → 1; `Start 3` → 1215; `u_turn_test` → 1520; `preview_pt2` → 819; `Start 6` → 1536; `ck_begin_drive` → 362; `Start 7` → 1550; `Start 8` → 1849.

Exits: `End 1` → 39; `End FT` → 1885.

End nodes: 39: `NonTerminating`; 1885: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 61 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/5` |
| `scnChangeIdleAnimEvent` | 56 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 76 | 5 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayActionEvent` | 7 | 61 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/10` |
| `scnIKEvent` | 18 | 61 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/12` |
| `scnLookAtEvent` | 106 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 10 | 61 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/30` |
| `scnPlaySkAnimEvent` | 98 | 5 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scneventsAttachPropToNode` | 1 | 656 / 806 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/3` |
| `scneventsAttachPropToPerformer` | 3 | 186 / 523 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/4` |
| `scneventsAttachPropToWorld` | 1 | 223 / 630 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/11` |
| `scneventsCameraParamsEvent` | 5 | 223 / 624 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 29 | 61 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scneventsSocket` | 73 | 5 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsVFXEvent` | 2 | 64 / 227 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- skeletal_animation: 8
- gaze: 7
- speech, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state, gameplay_action: 3
- speech, skeletal_animation, socket_signal: 2
- speech, idle_animation, gaze: 2
- skeletal_animation, gaze: 2
- socket_signal, animation_state, mount_workspot: 2
- camera: 2
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, ik, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, camera, audio, socket_signal, gameplay_action: 1
- idle_animation, gaze, socket_signal, animation_state: 1
- speech: 1
- skeletal_animation, idle_animation, gaze, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `056e0b760e8d44a4e88b40562de4c0e910601d2a08690ff924d8a2a9de3f5bac`. Binary SHA-256: `7927e2da4f9645b7c1a54b67df3f21e29ad7fc03ca2436697e123373a55728b2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_01c_car.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_02_fixer_calls.scene`

64 graph nodes, 74 edges; 8 event-bearing sections, 71 events; 18 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: fixer_kirk (actor 0, spawnSet); parking_security_booth (actor 1, community); eric_dawson (actor 2, community); Player (actor 3, findInContext).

Entries: `Fixer_Calls_in` → 1.

Exits: `Fixer_Calls_Out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 13 | 10 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 17 | 10 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtEvent` | 13 | 10 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 9 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 6 | 297 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scneventsSocket` | 13 | 297 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `60ea7320f26d3b64f33446db5d45b6c60c54d95f708281407d30b7e15804821a`. Binary SHA-256: `db2f7865d711decdd4a8199750dc91650426273ddccecdfa5f4a35760a40dacb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_02_fixer_calls.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_02a_confront_jackie.scene`

180 graph nodes, 199 edges; 28 event-bearing sections, 480 events; 59 screenplay lines, 8 screenplay options, 5 choice nodes.

Actors: jackie (actor 0, spawnSet); Stints (actor 1, community); fujioka_kaoru (actor 2, community); police_officer_03 (actor 3, community); police_officer_02 (actor 4, community); police_officer_01 (actor 5, community); Kirk (actor 6, spawnSet); bodyguard_01 (actor 7, community); bodyguard_02 (actor 8, community); cop_vehicle_01 (actor 9, community); cop_vehicle_02 (actor 10, community); rayfield (actor 11, spawner); Player (actor 12, findInContext).

Entries: `Confront_Jackie_In` → 1; `Start 4` → 1444; `Police_Arrival_In` → 241.

Exits: `Confront_Jackie_Out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 27 | 55 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnChangeIdleAnimEvent` | 50 | 55 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 53 | 55 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scnGameplayActionEvent` | 4 | 55 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnGameplayTransitionEvent` | 3 | 1312 / 1292 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/87` |
| `scnIKEvent` | 6 | 1312 / 1160 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 55 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scnLookAtEvent` | 98 | 55 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnPlaySkAnimEvent` | 114 | 55 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 1312 / 1279 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/77` |
| `scnUnmountEvent` | 3 | 1312 / 1290 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/85` |
| `scneventsAttachPropToNode` | 2 | 897 / 551 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/12` |
| `scneventsAttachPropToPerformer` | 7 | 99 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 1276 / 949 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/44` |
| `scneventsCameraParamsEvent` | 8 | 55 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 8 | 99 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scneventsSocket` | 76 | 55 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scneventsVFXDurationEvent` | 2 | 1276 / 888 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/12` |
| `scneventsVFXEvent` | 14 | 55 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation: 4
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 3
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, gameplay_action: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, props_equipment, audio, vfx, socket_signal, gameplay_action: 1
- idle_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `577510bc6c22ea37c819e1e794af6a0d0b730c5a3afa63f079e5c9e6e1479e48`. Binary SHA-256: `d8572d9e3661f66092c35d34e1c49f96be238e26081d3352fc830bdbc657e636`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_02a_confront_jackie.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_03_back_to_bar.scene`

83 graph nodes, 94 edges; 18 event-bearing sections, 186 events; 45 screenplay lines, 9 screenplay options, 5 choice nodes.

Actors: jackie (actor 0, spawnSet); walker_01 (actor 1, community); police_officer_01 (actor 2, spawnDespawn); police_officer_02 (actor 3, spawnDespawn); q000_police_car_01 (actor 4, spawner); Player (actor 5, findInContext).

Entries: `Back_To_Bar_In` → 1.

Exits: `Back_To_Bar_Out` → 2; `MontagePreloadOut` → 390.

End nodes: 2: `<omitted>`; 390: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 90 / 249 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/10` |
| `scnChangeIdleAnimEvent` | 17 | 33 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 42 | 33 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 122 / 386 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/15` |
| `scnIKEvent` | 4 | 122 / 367 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/1` |
| `scnLookAtEvent` | 29 | 44 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 33 | 33 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 3 | 65 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/19` |
| `scnUnmountEvent` | 2 | 122 / 385 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/14` |
| `scneventsCameraParamsEvent` | 7 | 65 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 2 | 122 / 381 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/11` |
| `scneventsSocket` | 40 | 33 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 3 | 90 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- speech: 2
- camera: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `4b097e755b1e6afb731298f99bb736c59d6f18b919069ebdb37287c5c424b569`. Binary SHA-256: `29de55aeaa65a6555f19570a6adfcbade714bd257ecc286c11b614b1850c4b3e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_03_back_to_bar.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_05b_trauma_team.scene`

250 graph nodes, 295 edges; 35 event-bearing sections, 365 events; 77 screenplay lines, 7 screenplay options, 5 choice nodes.

Actors: claire (actor 0, spawnSet); sampson (actor 1, spawnSet); sampson_gunner (actor 2, spawnSet); crash_car_driver (actor 3, spawner); crowd_driver_front (actor 4, spawner); crowd_driver_right_0 (actor 5, spawner); crowd_driver_right_1 (actor 6, spawner); crowd_driver_back (actor 7, spawner); crowd_driver_left_0 (actor 8, spawner); crowd_driver_left_1 (actor 9, spawner); crowd_helper_0 (actor 10, spawner); crowd_helper_1 (actor 11, spawner); crowd_bystander_0 (actor 12, spawner); crowd_bystander_1 (actor 13, spawner); crowd_bystander_2 (actor 14, spawner); crowd_bystander_3 (actor 15, spawner); crowd_bystander_4 (actor 16, spawner); crowd_bystander_5 (actor 17, spawner); sq024_05b_sampson_car (actor 18, spawnSet); sq024_05b_crash_car (actor 19, spawner); crowd_car_front (actor 20, spawner); crowd_car_right_0 (actor 21, spawner); crowd_car_right_1 (actor 22, spawner); crowd_car_back (actor 23, spawner); crowd_car_left_0 (actor 24, spawner); crowd_car_left_1 (actor 25, spawner); claire_car (actor 26, community); v (actor 27, findInContext).

Entries: `sq024_05b_tt_in` → 1; `q000_car_reuse` → 1233; `claire_kills` → 1161; `scene_pass_claire_spares` → 1170; `claire_kills_no_choice` → 1193.

Exits: `sq024_05b_sampson_dead_out` → 2; `q000_hijack_end` → 1236; `check_player_left` → 553.

End nodes: 2: `<omitted>`; 553: `NonTerminating`; 1236: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 506 / 514 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/5` |
| `scnChangeIdleAnimEvent` | 14 | 140 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 60 | 116 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 9 | 212 / 150 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/24` |
| `scnIKEvent` | 18 | 212 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnLookAtEvent` | 76 | 206 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 70 | 206 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnUnmountEvent` | 9 | 212 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/23` |
| `scneventsSetAnimFeatureEvent` | 9 | 212 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/19` |
| `scneventsSocket` | 94 | 140 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsVFXEvent` | 4 | 212 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 8
- speech: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 2
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `565881eae525b90a9ec57983daf0ccc7135128f47a598b8c9685ab4484a601da`. Binary SHA-256: `9b5a455f8025a4bed7df122e700efe45c430ffef5562b39771acc8a568f11dd4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_05b_trauma_team.scene" --events
```

