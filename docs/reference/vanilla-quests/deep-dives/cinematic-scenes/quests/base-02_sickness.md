# Nocturne Op55N1: scene presentation

Journal identity: `quests/meta/02_sickness`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-02_sickness.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q113\scenes\q113_13_adam_smasher.scene`

190 graph nodes, 198 edges; 29 event-bearing sections, 98 events; 40 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: smasher (actor 0, spawnSet); Takemura (actor 1, spawnSet); Hanako (actor 2, spawnSet); smasher_q116 (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `q113_12_adam_in` → 4; `q113_12_adam_defeated_in` → 9; `q113_13_smasher_reinforcements_01_in` → 292; `q113_13_smasher_reinforcements_02_in` → 296; `q113_13_smasher_come_to_daddy_in` → 307; `q113_13_v_low_health_in` → 311; `q113_13_smasher_low_health_in` → 316; `q113_13_smasher_to_takemura_in` → 320; `q113_13_smasher_about_oda_in` → 324; `q113_13_smasher_about_rogue_in` → 332; `q113_13_takemura_to_smasher_01_in` → 336; `q113_13_takemura_to_smasher_02_in` → 340; `q113_13_takemura_to_smasher_03_in` → 341; `q113_13_takemura_tip_rockets_in` → 344.

Exits: `q113_12_adam_out` → 5; `q113_12_adam_defeated_out` → 10; `End 2` → 253; `q113_13_smasher_reinforcements_02_out` → 297; `q113_13_smasher_come_to_daddy_out` → 309; `End1` → 114; `q113_13_v_low_health_out` → 313; `q113_13_smasher_low_health_out` → 318; `q113_13_smasher_to_takemura_out` → 322; `q113_13_smasher_about_oda_out` → 329; `q113_13_smasher_about_rogue_out` → 334; `q113_13_takemura_to_smasher_01_out` → 338; `q113_13_takemura_to_smasher_02_out` → 352; `q113_13_takemura_to_smasher_03_out` → 353; `q113_13_takemura_tip_rockets_out` → 355.

End nodes: 5: `NonTerminating`; 10: `NonTerminating`; 114: `<omitted>`; 253: `<omitted>`; 297: `<omitted>`; 309: `<omitted>`; 313: `<omitted>`; 318: `<omitted>`; 322: `<omitted>`; 329: `<omitted>`; 334: `<omitted>`; 338: `<omitted>`; 352: `<omitted>`; 353: `<omitted>`; 355: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 24 | 606 / 497 | `/Data/RootChunk/sceneGraph/Data/graph/119/Data/events/3` |
| `scnDialogLineEvent` | 31 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 2315 / 664 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/7` |
| `scnIKEvent` | 4 | 2315 / 658 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/2` |
| `scnLookAtEvent` | 1 | 606 / 507 | `/Data/RootChunk/sceneGraph/Data/graph/119/Data/events/13` |
| `scnPlaySkAnimEvent` | 7 | 149 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/0` |
| `scnUnmountEvent` | 2 | 2315 / 663 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 2 | 2315 / 661 | `/Data/RootChunk/sceneGraph/Data/graph/139/Data/events/5` |
| `scneventsSocket` | 16 | 149 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/2` |
| `scneventsVFXEvent` | 9 | 149 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 22
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, vfx, socket_signal: 1
- vfx: 1
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- vfx, socket_signal: 1

Raw SHA-256: `79a06e02d780ceeb3389dea5d44442016c565af15ada8dd51fdd7fab71aa6be9`. Binary SHA-256: `81cc5ae2686d708c101567d0eef669184109ca2e9aeb4b83851e713a84fe933d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_13_adam_smasher.scene" --events
```

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

## `base\quest\main_quests\part1\q115\scenes\q115_00b_hanako_holocall.scene`

25 graph nodes, 29 edges; 7 event-bearing sections, 31 events; 24 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: hanako (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `hanako_call_in` → 4; `Start 1` → 141.

Exits: `hanako_call_out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 28 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 18 | 9 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 3 | 9 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 47 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scneventsCameraEvent` | 1 | 132 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 132 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scneventsSocket` | 3 | 9 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze, socket_signal: 1
- speech, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation: 1
- camera: 1

Raw SHA-256: `4b8252ae4556c6a761aff3bd39b92064ae796eebeddf214a94e9129c7e110f93`. Binary SHA-256: `743ea763f660400c64e122b2a292e4e53968ba4dba0879853ab638d22a959bd7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_00b_hanako_holocall.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_02_ripperdoc.scene`

286 graph nodes, 367 edges; 66 event-bearing sections, 443 events; 136 screenplay lines, 24 screenplay options, 10 choice nodes.

Actors: victor_vector (actor 0, spawnSet); panam (actor 1, findInContext); rogue (actor 2, findInContext); sobchak (actor 3, findInContext); judy (actor 4, findInContext); kerry (actor 5, findInContext); johnny (actor 6, spawnDespawn); hanako (actor 7, findInContext); misty (actor 8, spawnSet); TV_sports_commentator (actor 9, findInContext); q115_ripperdoc_screens (actor 10, spawner); q115_ripperdoc_monitor (actor 11, spawner); V (actor 12, findInContext).

Entries: `in_wake_up` → 1; `Start 15` → 2930; `Start 5` → 2427; `Start 12` → 2692; `Start 13` → 2694; `Start 17` → 3493; `Start 7` → 2442; `in_pills` → 2457; `Start 14` → 2786; `Start 9` → 2536; `radio_in` → 3372; `Start 10` → 2593; `Start 11` → 2595.

Exits: `fin` → 2180; `radio_out` → 3373; `q115_02_ripperdoc_out` → 2074.

End nodes: 2074: `NonTerminating`; 2180: `NonTerminating`; 3373: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 1076 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scnChangeIdleAnimEvent` | 17 | 821 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 96 | 821 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 6 | 1745 / 503 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/7` |
| `scnIKEvent` | 12 | 1745 / 497 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/1` |
| `scnLookAtEvent` | 94 | 821 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 76 | 1076 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 6 | 1745 / 508 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/11` |
| `scneventsAttachPropToPerformer` | 7 | 1325 / 308 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/17` |
| `scneventsAttachPropToWorld` | 2 | 2365 / 901 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/2` |
| `scneventsCameraParamsEvent` | 7 | 1745 / 499 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 6 | 1745 / 504 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/8` |
| `scneventsSocket` | 104 | 821 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 5 | 821 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 5
- gaze: 5
- speech: 4
- speech, socket_signal: 4
- skeletal_animation: 4
- camera: 3
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, camera, audio, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- camera, socket_signal: 1
- skeletal_animation, gaze: 1
- vfx: 1
- props_equipment, socket_signal: 1
- ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1
- socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `bb7909e2acfa6a64953922db31013f7010f722fd7f5e0e68893795dba967511d`. Binary SHA-256: `0b9a20ce1c69feb784a8a11b71b0af6015c9fcdd60e9b4174b49bd2ed7037876`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_02_ripperdoc.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_02b_ripperdoc_roof.scene`

853 graph nodes, 1025 edges; 157 event-bearing sections, 1165 events; 401 screenplay lines, 58 screenplay options, 22 choice nodes.

Actors: misty (actor 0, spawnSet); victor (actor 1, spawnSet); sobchak (actor 2, spawnSet); panam (actor 3, spawnSet); judy (actor 4, spawnSet); kerry (actor 5, spawnSet); hanako (actor 6, findInContext); rogue (actor 7, findInContext); johnny (actor 8, spawnDespawn); V_male (actor 9, spawner); V_female (actor 10, spawner); Player (actor 11, findInContext); V_POSESSED (actor 12, findInContext).

Entries: `sq024_02b_in` → 4; `Start 39` → 4150; `Start 15` → 1678; `roof_in` → 52; `misty_urge` → 1736; `Start 17` → 1745; `Start 18` → 1747; `Start 19` → 1748; `panam` → 1749; `Start 22` → 1762; `kerry` → 1770; `record_start` → 3436; `river` → 1778; `Start 25` → 1786; `Start 26` → 1870; `Start 0` → 2722; `Start 34` → 3578; `Start 27` → 1939; `describing_options` → 1950; `Start1` → 2834; `Start 35` → 3675; `Start 36` → 3677; `Start 4` → 1190; `Start 37` → 3679; `hanako` → 1201; `Start 6` → 1203; `Start 7` → 1216; `solo_in` → 1232; `Start2` → 2914; `Start 40` → 4613; `Start 38` → 3852; `Start 29` → 2237; `Start 9` → 1421; `Start 30` → 2255; `Start 10` → 1434; `Start 11` → 1436; `Start 31` → 3123; `Start 12` → 1472; `Start 32` → 3169; `Start 14` → 1553; `Start 33` → 3231; `Start 2` → 784; `Start 3` → 787.

Exits: `End3` → 3438; `out_afterlife` → 226; `out_nomads` → 277; `out_hanako` → 280; `terminado` → 2056; `out_dead` → 403; `solo_out` → 1246; `End 4` → 1303; `ai_out` → 1364.

End nodes: 226: `NonTerminating`; 277: `NonTerminating`; 280: `NonTerminating`; 403: `<omitted>`; 1246: `<omitted>`; 1303: `<omitted>`; 1364: `NonTerminating`; 2056: `<omitted>`; 3438: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 16 | 344 / 624 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/1` |
| `scnChangeIdleAnimEvent` | 49 | 19 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scnDialogLineEvent` | 331 | 14 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 17 / 142 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |
| `scnIKEvent` | 6 | 17 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnLookAtAdvancedEvent` | 13 | 4043 / 5220 | `/Data/RootChunk/sceneGraph/Data/graph/715/Data/events/1` |
| `scnLookAtEvent` | 117 | 15 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnPlayRidAnimEvent` | 65 | 2233 / 3019 | `/Data/RootChunk/sceneGraph/Data/graph/410/Data/events/4` |
| `scnPlaySkAnimEvent` | 316 | 14 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnPlayVideoEvent` | 1 | 2233 / 3554 | `/Data/RootChunk/sceneGraph/Data/graph/410/Data/events/200` |
| `scnUnmountEvent` | 3 | 17 / 141 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |
| `scneventsAttachPropToNode` | 1 | 1214 / 1839 | `/Data/RootChunk/sceneGraph/Data/graph/214/Data/events/7` |
| `scneventsAttachPropToPerformer` | 6 | 525 / 921 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/1` |
| `scneventsAttachPropToWorld` | 7 | 525 / 927 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/7` |
| `scneventsCameraParamsEvent` | 5 | 525 / 922 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/2` |
| `scneventsEquipItemToPerformer` | 6 | 4681 / 5957 | `/Data/RootChunk/sceneGraph/Data/graph/816/Data/events/0` |
| `scneventsPlayRidCameraAnimEvent` | 31 | 2233 / 3043 | `/Data/RootChunk/sceneGraph/Data/graph/410/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 3 | 17 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |
| `scneventsSocket` | 172 | 15 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scneventsVFXEvent` | 14 | 237 / 576 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 24
- skeletal_animation: 19
- speech, skeletal_animation, gaze, socket_signal: 18
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 18
- speech, socket_signal: 7
- gaze: 7
- speech, skeletal_animation, socket_signal: 5
- socket_signal: 5
- speech, idle_animation, gaze, socket_signal: 4
- gaze, camera, socket_signal: 4
- camera, rid_camera: 4
- speech, gaze: 3
- skeletal_animation, audio, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation: 2
- speech, idle_animation: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, audio, vfx, socket_signal: 2
- speech, gaze, socket_signal: 2
- props_equipment: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1
- speech, audio: 1
- gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- gaze, socket_signal: 1
- props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, rid_actor, camera, rid_camera, props_equipment, audio, socket_signal, video: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1

Raw SHA-256: `3ff92369e9b58796f825c82ec7059b50aa2b54257c88c9ee2e46d8601ec0bfc4`. Binary SHA-256: `0506831be23656c51947cf3bf920a95700235d4cc52065dc18e91a09c337dd83`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_02b_ripperdoc_roof.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_02c_holocalls.scene`

62 graph nodes, 73 edges; 12 event-bearing sections, 83 events; 59 screenplay lines, 9 screenplay options, 3 choice nodes.

Actors: hanako (actor 0, spawnSet); panam (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 6` → 336; `Start1` → 339; `q115_02c_panam_holocall_in` → 48; `Start 2` → 286; `q115_02c_hanako_holocall_in` → 71.

Exits: `q115_02c_hanako_holocall_out` → 2; `q115_02c_panam_holocall_out` → 49; `End 2` → 287.

End nodes: 2: `<omitted>`; 49: `<omitted>`; 287: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 183 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/3` |
| `scnChangeIdleAnimEvent` | 7 | 13 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 49 | 13 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 183 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/4` |
| `scnIKEvent` | 2 | 183 / 150 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scnPlaySkAnimEvent` | 13 | 13 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 1 | 183 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/8` |
| `scneventsCameraParamsEvent` | 2 | 342 / 247 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 183 / 154 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/5` |
| `scneventsSocket` | 6 | 13 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- camera: 2
- speech: 1
- speech, idle_animation: 1
- speech, skeletal_animation: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `66229320f9e3c338a8e5fb5f921c4668d6db07b5b6adc1281e0cc2fda99ea40e`. Binary SHA-256: `e6b4f56896e5f936f9fe520f4fb7b15ba83a233ac1f52d7f246dca509d5c8e1b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_02c_holocalls.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_02d_misty.scene`

514 graph nodes, 666 edges; 111 event-bearing sections, 751 events; 242 screenplay lines, 28 screenplay options, 18 choice nodes.

Actors: victor_vector (actor 0, spawnSet); Misty (actor 1, spawnSet); cat (actor 2, spawner); Anders (actor 3, spawnSet); Takemura (actor 4, spawnSet); Panam (actor 5, spawnSet); q115_02d_anders_car (actor 6, spawner); q115_02d_panam_car (actor 7, spawnSet); Player (actor 8, findInContext).

Entries: `Start 17` → 1470; `q113_02_misty_in` → 60; `Start1` → 2004; `tarot` → 1096; `taror_initial` → 1104; `q115_02d_chakras_panam_in` → 146; `Start 12` → 1113; `q115_02d_chakras_hanako_in` → 154; `refuse_tarot` → 1138; `Start 14` → 1152; `Start 23` → 2610; `Start 15` → 1174; `Start 16` → 1178; `Start 19` → 2244; `Start 18` → 1764; `test` → 810; `Start 24` → 2739; `Start 20` → 2337; `Start 21` → 2358; `Start 22` → 2361; `q113` → 920; `Start 8` → 923; `Start 9` → 935; `Start 0` → 1915.

Exits: `q115_02d_chakras_panam_out` → 150; `q115_02d_chakras_hanako_out` → 156.

End nodes: 150: `<omitted>`; 156: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 832 / 1577 | `/Data/RootChunk/sceneGraph/Data/graph/146/Data/events/3` |
| `scnChangeIdleAnimEvent` | 71 | 80 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 161 | 80 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayTransitionEvent` | 10 | 316 / 371 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/12` |
| `scnIKEvent` | 20 | 316 / 345 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/1` |
| `scnLookAtEvent` | 129 | 95 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 151 | 80 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnUnmountEvent` | 10 | 316 / 372 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/13` |
| `scneventsAttachPropToPerformer` | 20 | 253 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/8` |
| `scneventsAttachPropToWorld` | 19 | 376 / 768 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/8` |
| `scneventsCameraParamsEvent` | 6 | 283 / 181 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 10 | 316 / 363 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/10` |
| `scneventsSocket` | 132 | 80 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsVFXEvent` | 10 | 256 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- skeletal_animation: 10
- skeletal_animation, gaze, socket_signal: 7
- skeletal_animation, socket_signal: 7
- gaze: 7
- speech, skeletal_animation, idle_animation, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, gaze, socket_signal: 6
- speech, idle_animation: 3
- speech, idle_animation, gaze: 2
- speech, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze: 2
- speech, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment: 2
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- vfx: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- skeletal_animation, gaze: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment: 1
- skeletal_animation, camera, socket_signal: 1
- vfx, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- camera: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `dd2c3b62cd1ef64f449a91cc69091ca0c0e2c8f481f60333829103241dd24711`. Binary SHA-256: `5bab1f7ab58b846004dbbbd47691dd44d73becdcacc909f0414030f9329abe0f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_02d_misty.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_06_regroup.scene`

369 graph nodes, 379 edges; 69 event-bearing sections, 186 events; 144 screenplay lines, 15 screenplay options, 5 choice nodes.

Actors: rogue (actor 0, spawnSet); weyland (actor 1, spawnSet); guard_1 (actor 2, community); guard_2 (actor 3, community); arasaka_ai (actor 4, spawnDespawn); trying_to_get_inside_av (actor 5, community); q115_crashed_av (actor 6, spawner); V (actor 7, findInContext).

Entries: `q115_solo_ai_in` → 1211; `q115_05_birbs_in` → 1218; `commander_dead_in` → 833; `near_elevator_no_weyland_in` → 850; `used_elevator_no_weyland_in` → 856; `secret_elevator_no_weyland_in` → 868; `targeting_weyland_1` → 467; `secret_elevator_weyland_in` → 874; `secret_elevator_ledge_in` → 886; `secret_elevator_in` → 895; `q115_rogue_weyland_to_elev_in` → 1702; `spotted_first_guards_in` → 928; `rogue_second_td_done` → 558; `after_first_guards_in` → 963; `first_guards_player_left_in` → 973; `takedown_activate_in` → 608; `spotted_combat_in` → 1019; `weyland_second_thanks_in` → 621; `q115_05_stealth_takedown_in` → 1039; `landing_in` → 240; `q115_05_use_terminal_in` → 1050; `rogue_first_guards_in` → 245; `q115_05_play_chippin_in` → 1053; `rogue_first_guards_td_in` → 250; `q115_05_lights_in` → 1060; `weyland_thanks_in` → 255; `q115_05_fog_in` → 1065; `rogue_weyland_in` → 260; `rogue_first_guards_02_in` → 265; `commander_keycard_looted_in` → 1076; `q113_lockdown_start_in` → 1105; `Start 20` → 1130; `q115_06_terminal_in` → 1132; `die` → 1139; `regroup_commander_in` → 336; `elevator_fluff_in` → 380; `Start 25` → 1593; `commander_takedown_ready_in` → 799; `Start 27` → 2011.

Exits: `landing_out` → 411; `q115_05_birbs_out` → 1219; `commander_dead_out` → 834; `near_elevator_no_weyland_out` → 851; `used_elevator_no_weyland_out` → 857; `weyland_imprisoned_out` → 465; `secret_elevator_no_weyland_out` → 869; `secret_elevator_weyland_out` → 875; `secret_elevator_ledge_out` → 887; `secret_elevator_out` → 896; `first_guards_sneak_out` → 929; `q115_rogue_weyland_to_elev_out` → 1736; `first_guards_takedown_out` → 930; `after_first_guards_out` → 964; `first_guards_player_left_out` → 974; `guards_move` → 1011; `takedown_activate_out` → 614; `spotted_combat_out` → 1020; `regroup_commander_walk` → 618; ` weyland_second_thanks_out` → 624; `q115_05_stealth_takedown_out` → 1040; `q115_05_use_terminal_out` → 1051; `rogue_first_guards_out` → 246; `q115_05_play_chippin_out` → 1054; `rogue_first_guards_td_out` → 251; `q115_05_lights_out` → 1061; `weyland_to_commander_out` → 256; `q115_05_fog_out` → 1066; `rogue_first_guards_02_out` → 266; `commander_keycard_looted_out` → 1077; `regroup_commander_out` → 343; `elevator_fluff_out` → 383; `weyland_to_elevator_out` → 786; `commander_takedown_ready_out` → 800; `q115_solo_ai_out` → 1208.

End nodes: 246: `<omitted>`; 251: `<omitted>`; 256: `<omitted>`; 266: `<omitted>`; 343: `<omitted>`; 383: `<omitted>`; 411: `NonTerminating`; 465: `<omitted>`; 614: `<omitted>`; 618: `NonTerminating`; 624: `<omitted>`; 786: `<omitted>`; 800: `<omitted>`; 834: `<omitted>`; 851: `<omitted>`; 857: `<omitted>`; 869: `<omitted>`; 875: `<omitted>`; 887: `<omitted>`; 896: `<omitted>`; 929: `<omitted>`; 930: `<omitted>`; 964: `<omitted>`; 974: `<omitted>`; 1011: `NonTerminating`; 1020: `<omitted>`; 1040: `<omitted>`; 1051: `<omitted>`; 1054: `<omitted>`; 1061: `<omitted>`; 1066: `<omitted>`; 1077: `<omitted>`; 1208: `<omitted>`; 1219: `<omitted>`; 1736: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 1138 / 924 | `/Data/RootChunk/sceneGraph/Data/graph/203/Data/events/2` |
| `scnDialogLineEvent` | 103 | 247 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 1138 / 921 | `/Data/RootChunk/sceneGraph/Data/graph/203/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 1535 / 1094 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/7` |
| `scnIKEvent` | 4 | 1535 / 1088 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/1` |
| `scnLookAtEvent` | 17 | 257 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnPlaySkAnimEvent` | 19 | 257 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnUnmountEvent` | 2 | 1535 / 1100 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/12` |
| `scneventsCameraParamsEvent` | 3 | 692 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 2 | 1535 / 1096 | `/Data/RootChunk/sceneGraph/Data/graph/230/Data/events/9` |
| `scneventsSocket` | 29 | 257 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scneventsVFXEvent` | 3 | 692 / 316 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 43
- speech, socket_signal: 4
- skeletal_animation: 4
- speech, skeletal_animation, gaze: 3
- speech, gaze: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, camera, vfx, socket_signal: 1
- speech, vfx: 1
- skeletal_animation, idle_animation, vfx, socket_signal, gameplay_action: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `439164211270e7a09bf3d34c248f79f97055262f5551da39bfd332d5d9234796`. Binary SHA-256: `f8604d4eb3e3b20d5cc7d504d6534e7c5b52eea08eee7cd545822dfa5a8e9020`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_06_regroup.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_11_netrunners_nest.scene`

138 graph nodes, 128 edges; 21 event-bearing sections, 65 events; 79 screenplay lines, 1 screenplay options, 0 choice nodes.

Actors: Rogue (actor 0, spawnSet); Weyland (actor 1, spawnSet); guard_008 (actor 2, community); operator (actor 3, community); alt (actor 4, spawnDespawn); netrunner_01 (actor 5, community); netrunner_02 (actor 6, community); netrunner_03 (actor 7, community); guard_009 (actor 8, community); arasaka_elevator_ai (actor 9, spawner); guard_shot (actor 10, spawner); V_POSESSED (actor 11, findInContext).

Entries: `q115_elevator_ai_in` → 589; `q115_01_af_nest_in` → 1; `q115_11_spooky_moment_01_in` → 600; `q115_11_spooky_moment_02_in` → 605; `q115_11_spooky_moment_03_in` → 607; `q115_11_spooky_moment_04_in` → 609; `q115_connect_alt_in` → 415; `q115_01_af_kill_in` → 220; `q115_solo_in` → 1204; `q115_01_rogue_start_brief` → 424; `q115_01_af_nest_brief_control_room` → 430; `q115_11_guard_shot_in` → 627; `q115_01_af_nest_brief_alt` → 437; `q115_01_af_nest_access_granted` → 443; `q115_rogue_nest_start_warning` → 448; `q115_get_to_nest_floor_in` → 454; `q115_nest_banter_walkway_in` → 459; `q115_nest_banter_room_in` → 465; `q115_nest_banter_turret_in` → 470; `q115_nest_banter_engineers_in` → 475; `q115_nest_banter_patrols_in` → 480; `q115_11_alt_in_elevator_in` → 687; `q115_nest_overheat_in` → 495; `q114_11_alt_reminder_in` → 897; `spotted_combat_in` → 507; `q115_11_riding_down_long_elevator_in` → 518; `q115_01_af_see_nest_in` → 136; `q115_nest_defeated_everyone_in` → 531; `q115_01_af_glass_in` → 164; `q115_11_NPC_to_gate_in` → 957; `q115_11_netrunners_in` → 568.

Exits: `q115_elevator_ai_out` → 590; `q115_11_spooky_moment_01_out` → 601; `q115_11_spooky_moment_02_out` → 606; `q115_11_spooky_moment_03_out` → 608; `q115_11_spooky_moment_04_out` → 610; `q115_solo_out` → 1205; `q115_11_guard_shot_out` → 631; `q115_rogue_nest_start_warning_end` → 452; `q115_get_to_nest_floor_out` → 455; `q115_nest_banter_walkway_out` → 460; `q115_11_alt_in_elevator_out` → 688; `q114_11_alt_reminder_out` → 898; `spotted_combat_out` → 508; `q115_11_riding_down_long_elevator_out` → 519; `solo_open_door` → 759; `q115_11_NPC_elevator_out` → 958.

End nodes: 452: `<omitted>`; 455: `<omitted>`; 460: `<omitted>`; 508: `<omitted>`; 519: `<omitted>`; 590: `NonTerminating`; 601: `<omitted>`; 606: `<omitted>`; 608: `<omitted>`; 610: `<omitted>`; 631: `<omitted>`; 688: `<omitted>`; 759: `NonTerminating`; 898: `<omitted>`; 958: `<omitted>`; 1205: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 43 | 450 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnLookAtEvent` | 7 | 522 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 522 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/2` |
| `scneventsSocket` | 4 | 588 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/7` |
| `scneventsVFXEvent` | 2 | 588 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, skeletal_animation, gaze: 2
- speech, socket_signal: 2
- skeletal_animation: 2
- speech, gaze, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `3c95461441f6d97125fefa9442df054dcdc65eb9324f40382f5f64d44b30e43a`. Binary SHA-256: `d3f08ebe4b0138497a0f47c02719f45934fc494ee3efef21b986a784d2138b63`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_11_netrunners_nest.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_12b_tower_lobby.scene`

266 graph nodes, 271 edges; 31 event-bearing sections, 106 events; 38 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: johnny (actor 0, spawnDespawn); guard_1 (actor 1, community); arasaka_ai (actor 2, findInContext); minotaur_1 (actor 3, community); minotaur_2 (actor 4, community); minotaur_3 (actor 5, community); guard_voiceover_1 (actor 6, community); guard_voiceover_2 (actor 7, community); guard_voiceover_3 (actor 8, community); guard_voiceover_4 (actor 9, community); Player (actor 10, findInContext).

Entries: `q115_12b_arrive_tower_in` → 4; `q115_12b_many_guards_in` → 9; `Start 0` → 803; `q115_12b_elevator_in` → 29; `q115_12b_loot_in` → 40; `q115_12b_combat_fluff_2_in` → 568; `q115_12b_combat_fluff_3_in` → 573; `q115_12b_elevator_access_in` → 51; `q115_12b_got_loot_in` → 62; `q115_12b_in_elevator_in` → 73; `q115_12b_combat_fluff_1_in` → 84; `q115_12b_heads_up_in` → 897; `Start 5` → 396; `q115_12b_final_mech_in` → 413; `q115_12b_tower_ai_in` → 159; `q115_12b_guard_afam_1_in` → 462; `q115_12b_guard_afam_2_in` → 463; `q115_12b_guard_enus_1_in` → 464; `q115_12b_guard_enus_4_in` → 465; `q115_12b_secret_ending_in` → 1002; `ded_in` → 1010; `in_got_it` → 1023.

Exits: `q115_12b_arrive_tower_out` → 5; `q115_12b_many_guards_out` → 10; `out_got_it` → 1069; `q115_12b_elevator_out` → 30; `q115_12b_loot_out` → 41; `combat_fluff_3_non_terminating_out` → 1103; `q115_12b_elevator_access_out` → 52; `q115_12b_combat_fluff_3_out` → 581; `q115_12b_got_loot_out` → 63; `q115_12b_combat_fluff_out` → 85; `q115_12b_taking_elev_down_out` → 107; `q115_12b_heads_up_out` → 898; `q115_12b_final_mech_out` → 414; `q115_12b_tower_ai_out` → 160; `johnny_mech_reaction` → 435; `End1` → 1224; `End2` → 1228; `q115_12b_guard_afam_1_out` → 466; `q115_12b_guard_afam_2_out` → 467; `q115_12b_guard_enus_1_out` → 468; `q115_12b_guard_enus_4_out` → 469; `despawn_enemies` → 999; `ded_out` → 1011.

End nodes: 5: `NonTerminating`; 10: `<omitted>`; 30: `<omitted>`; 41: `<omitted>`; 52: `<omitted>`; 63: `NonTerminating`; 85: `<omitted>`; 107: `<omitted>`; 160: `NonTerminating`; 414: `NonTerminating`; 435: `NonTerminating`; 466: `<omitted>`; 467: `<omitted>`; 468: `<omitted>`; 469: `<omitted>`; 581: `<omitted>`; 898: `<omitted>`; 999: `NonTerminating`; 1011: `<omitted>`; 1069: `NonTerminating`; 1103: `NonTerminating`; 1224: `<omitted>`; 1228: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 131 / 169 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/7` |
| `scnDialogLineEvent` | 22 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 14 | 11 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 21 | 75 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 131 / 170 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/8` |
| `scneventsEquipItemToPerformer` | 6 | 31 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scneventsSocket` | 28 | 11 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsVFXEvent` | 8 | 108 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- skeletal_animation: 6
- speech, gaze, socket_signal: 3
- speech, gaze, props_equipment, socket_signal: 3
- speech, props_equipment, socket_signal: 3
- skeletal_animation, audio, vfx, socket_signal: 3
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, vfx: 1
- skeletal_animation, camera, audio, vfx, socket_signal: 1
- speech, vfx: 1
- skeletal_animation, socket_signal: 1
- gaze: 1
- vfx: 1

Raw SHA-256: `6004eced5f7dc3de436a1961dfd2895b75188e401e896a0c5c306af0f386511f`. Binary SHA-256: `099f958ffcb76aa963188b6204054c2689ad904f810b318f8ee33d7af2664f5f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_12b_tower_lobby.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_12c_tower_nest.scene`

144 graph nodes, 125 edges; 27 event-bearing sections, 86 events; 36 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: johnny (actor 0, spawnDespawn); alt (actor 1, spawnDespawn); guard_voiceover_1 (actor 2, community); guard_voiceover_2 (actor 3, community); guard_voiceover_3 (actor 4, community); guard_voiceover_4 (actor 5, community); guard_voiceover_5 (actor 6, community); guard_voiceover_6 (actor 7, community); guard_voiceover_7 (actor 8, community); guard_voiceover_8 (actor 9, community); guard_voiceover_9 (actor 10, community); guard_voiceover_10 (actor 11, community); guard_voiceover_11 (actor 12, community); guard_voiceover_12 (actor 13, community); mech (actor 14, community); Player (actor 15, findInContext).

Entries: `q115_12c_arrive_nest_in` → 4; `q115_12c_first_security_in` → 21; `q115_12c_security_booth_in` → 34; `q115_12c_mainframe_in` → 47; `q115_12c_connecting_alt_in` → 60; `q115_12c_alt_connected_in` → 73; `fluff_004` → 344; `fluff_006` → 345; `fluff_008` → 346; `fluff_010` → 347; `fluff_012` → 348; `fluff_011` → 349; `fluff_control_room_1` → 350; `fluff_control_room_2` → 351; `fluff_022` → 352; `fluff_002` → 217; `fluff_023` → 353; `fluff_025` → 354; `q115_12c_see_mainframe_booth_in` → 117; `q115_12c_nest_room_in` → 132.

Exits: `q115_12c_arrive_nest_out` → 5; `q115_12c_first_security_out` → 22; `q115_12c_security_booth_out` → 35; `q115_12c_mainframe_out` → 48; `johnny_can_tp` → 196; `door` → 340; `q115_12c_alt_connected_out` → 74; `End 5` → 366; `End 6` → 367; `End 7` → 368; `End 8` → 369; `End 9` → 370; `End 10` → 371; `End 11` → 372; `End 12` → 373; `End 13` → 374; `End 14` → 375; `End 15` → 376; `killing_monsters` → 106; `End 16` → 377; `q115_12c_see_mainframe_booth_out` → 118; `q115_12c_nest_room_out` → 133.

End nodes: 5: `<omitted>`; 22: `NonTerminating`; 35: `<omitted>`; 48: `<omitted>`; 74: `<omitted>`; 106: `NonTerminating`; 118: `<omitted>`; 133: `NonTerminating`; 196: `NonTerminating`; 340: `NonTerminating`; 366: `<omitted>`; 367: `<omitted>`; 368: `<omitted>`; 369: `<omitted>`; 370: `<omitted>`; 371: `<omitted>`; 372: `<omitted>`; 373: `<omitted>`; 374: `<omitted>`; 375: `<omitted>`; 376: `<omitted>`; 377: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 32 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 36 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/15` |
| `scnIKEvent` | 2 | 36 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/7` |
| `scnLookAtEvent` | 12 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 12 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 36 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/14` |
| `scneventsAttachPropToNode` | 1 | 76 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/5` |
| `scneventsAttachPropToPerformer` | 1 | 76 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/2` |
| `scneventsCameraParamsEvent` | 2 | 76 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |
| `scneventsEquipItemToPerformer` | 3 | 138 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 36 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |
| `scneventsSocket` | 16 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 2 | 36 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 14
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- skeletal_animation: 2
- props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation: 1
- speech, gaze, props_equipment, socket_signal: 1
- speech, socket_signal: 1

Raw SHA-256: `69d2c8f3d8ccf8f0e903b749bb70536d19044d8a8c782accb9e6cdd1ebca0157`. Binary SHA-256: `5a3d551637ee8211e89cb62bf2b0aaede0493c7a52b9c8026ea5835579a5f079`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_12c_tower_nest.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_12d_mikoshi.scene`

158 graph nodes, 171 edges; 29 event-bearing sections, 138 events; 45 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: johnny (actor 0, spawnSet); alt (actor 1, spawnDespawn); smasher (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `q115_12d_after_bossfight_in` → 1; `Start 5` → 3765; `q115_12d_bossfight_in` → 7; `Start 4` → 373; `Start 2` → 256; `Start 3` → 271; `q115_12d_to_mikoshi_in` → 150; `q115_12d_mikoshi_room_in` → 155; `q115_12d_mikoshi_access_in` → 160.

Exits: `q115_12d_after_bossfight_out` → 2; `q115_12d_bossfight_out` → 8; `johnny_comment` → 3799; `q115_12d_to_mikoshi_out` → 151; `q115_12d_mikoshi_room_out` → 156; `q115_12d_mikoshi_access_out` → 161.

End nodes: 2: `NonTerminating`; 8: `NonTerminating`; 151: `NonTerminating`; 156: `NonTerminating`; 161: `<omitted>`; 3799: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 234 / 146 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/4` |
| `scnChangeIdleAnimEvent` | 3 | 152 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scnDialogLineEvent` | 21 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 10 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 31 | 157 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scneventsCameraParamsEvent` | 5 | 341 / 266 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/2` |
| `scneventsSocket` | 41 | 9 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsVFXEvent` | 22 | 234 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- socket_signal: 3
- skeletal_animation, camera, socket_signal: 3
- speech, gaze: 2
- speech, socket_signal: 2
- gaze, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, vfx, socket_signal: 2
- speech, idle_animation: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, gaze, camera, socket_signal: 1
- idle_animation: 1
- speech, skeletal_animation, camera, audio, vfx, socket_signal: 1
- gaze: 1

Raw SHA-256: `6f32b9b2d338452e40281c47596193d55cbadd7c69550e47d07754fd2a9cd306`. Binary SHA-256: `9bc34491bc5326ca0938ece59def75b42fee11e7a872064ef33cc4aefb0f7078`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_12d_mikoshi.scene" --events
```

## `base\quest\main_quests\part1\q116\scenes\q116_01_adam_smasher.scene`

170 graph nodes, 221 edges; 34 event-bearing sections, 193 events; 46 screenplay lines, 1 screenplay options, 0 choice nodes.

Actors: smasher (actor 0, spawnSet); rogue (actor 1, spawnSet); panam (actor 2, spawnSet); weyland (actor 3, spawnSet); saul (actor 4, spawnSet); alt (actor 5, findInContext); minotaur_1 (actor 6, community); minotaur_2 (actor 7, community); V (actor 8, findInContext); V_possessed (actor 9, findInContext).

Entries: `q116_bossfight_in` → 1; `q116_start_in` → 188; `Start 0` → 907; `q114` → 551; `mech1` → 1222; `mech2` → 1223; `q115` → 520.

Exits: `q116_bossfight_out` → 2; `q116_start_out` → 189.

End nodes: 2: `NonTerminating`; 189: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 515 / 175 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/9` |
| `scnChangeIdleAnimEvent` | 8 | 515 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/10` |
| `scnDialogLineEvent` | 17 | 190 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnLookAtEvent` | 23 | 190 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 44 | 515 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/2` |
| `scneventsAttachPropToNode` | 1 | 515 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/1` |
| `scneventsAttachPropToPerformer` | 3 | 515 / 226 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/37` |
| `scneventsAttachPropToWorld` | 1 | 515 / 234 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/43` |
| `scneventsSocket` | 50 | 190 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsVFXEvent` | 44 | 515 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/20` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- skeletal_animation: 10
- gaze: 4
- skeletal_animation, socket_signal: 3
- speech, gaze, socket_signal: 2
- vfx: 2
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1

Raw SHA-256: `2386c5a14c94c99ba7ed38d1fdcd2ca7e4a6bac3b4b2b67290e4e58a8ceefc36`. Binary SHA-256: `7642406d5e724bfd0fa1c662a7934507d68364a022157291aa9492c92f751eb1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q116\scenes\q116_01_adam_smasher.scene" --events
```

## `base\quest\main_quests\part1\q116\scenes\q116_03b_after_bossfight.scene`

128 graph nodes, 176 edges; 24 event-bearing sections, 106 events; 73 screenplay lines, 15 screenplay options, 7 choice nodes.

Actors: Panam (actor 0, spawnSet); Alt (actor 1, spawnDespawn); rogue (actor 2, spawnSet); weyland (actor 3, spawnSet); smasher (actor 4, spawnSet); saul (actor 5, spawnSet); V (actor 6, findInContext); V_possessed (actor 7, findInContext).

Entries: `q116_03b_after_bossfight_in` → 1; `Start 2` → 345; `panam_to_finale` → 532; `Start 4` → 538; `Start 5` → 572; `Start 8` → 922; `q116_03b_player_dies` → 598; `Start 9` → 959; `panam` → 814.

Exits: `q116_03b_after_bossfight_out` → 16; `q116_03b_player_dies_out` → 752.

End nodes: 16: `NonTerminating`; 752: `Terminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 364 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/2` |
| `scnDialogLineEvent` | 47 | 135 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 382 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/7` |
| `scnIKEvent` | 2 | 382 / 214 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/1` |
| `scnLookAtEvent` | 7 | 188 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnPlaySkAnimEvent` | 13 | 183 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnUnmountEvent` | 1 | 382 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/6` |
| `scneventsAttachPropToPerformer` | 4 | 183 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 1 | 382 / 218 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/5` |
| `scneventsSocket` | 25 | 135 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, skeletal_animation, props_equipment, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- socket_signal: 2
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, gaze: 1
- idle_animation: 1

Raw SHA-256: `80a9c15ecf241698bdd440c7654667a8a1353d1e3a67347760746ba342f3a90f`. Binary SHA-256: `ab7fd4a0d8dd6e6223df7db328daeb4dd0a7820e6b331f6db173023fbcee05c7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q116\scenes\q116_03b_after_bossfight.scene" --events
```

