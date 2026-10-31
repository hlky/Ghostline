# Rebel! Rebel!: scene presentation

Journal identity: `quests/side_quest/sq017_kerry`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq017_kerry.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq017\scenes\sq017_01_phone_call_1.scene`

30 graph nodes, 32 edges; 5 event-bearing sections, 33 events; 17 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: kerry (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `Start 0` → 1; `Start 2` → 186.

Exits: `End 0` → 2; `rejected_out` → 444.

End nodes: 2: `<omitted>`; 444: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 16 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 8 | 3 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 3 | 40 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, idle_animation, socket_signal: 1

Raw SHA-256: `d2bdbf5db00be2d3b1ea793abed716d96f4e612441af6d7020480ed8bfcad17a`. Binary SHA-256: `5b2dcc29e478ae2cd69018dd465ce436fb18e241fc4a17a88011802ee5119b80`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_01_phone_call_1.scene" --events
```

## `base\quest\side_quests\sq017\scenes\sq017_02_coffee_cart.scene`

71 graph nodes, 79 edges; 9 event-bearing sections, 36 events; 9 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: filipino_barista (actor 0, community); kerry (actor 1, spawnSet); kerry_car (actor 2, spawnSet); v (actor 3, findInContext).

Entries: `Start_coffee_cart` → 481; `Start 3` → 1380.

Exits: `End_coffee_cart` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 1311 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/0` |
| `scnDialogLineEvent` | 2 | 8 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnGameplayActionEvent` | 1 | 1375 / 258 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 1283 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/5` |
| `scnIKEvent` | 4 | 1283 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/3` |
| `scnLookAtEvent` | 6 | 8 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 5 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnUnmountEvent` | 1 | 1283 / 197 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/8` |
| `scneventsAttachPropToPerformer` | 2 | 1311 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 3 | 1283 / 195 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/7` |
| `scneventsSocket` | 7 | 1275 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/2` |
| `scneventsVFXEvent` | 2 | 1275 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2
- speech, skeletal_animation, gaze: 1
- speech, gaze: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, props_equipment: 1
- skeletal_animation, idle_animation, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, ik, socket_signal, animation_state: 1

Raw SHA-256: `106f8fc815c4f77870f67257f8ce666bddb8f841f543e3f53ee03b8b6acf71e9`. Binary SHA-256: `31f8e117a3d8a2ae66424f5bd4e95c950671e5d2fbebd292c11f73cdda4d28cb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_02_coffee_cart.scene" --events
```

## `base\quest\side_quests\sq017\scenes\sq017_03_freeway_drive.scene`

104 graph nodes, 138 edges; 25 event-bearing sections, 162 events; 42 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: kerry (actor 0, spawnSet); johnny (actor 1, spawnDespawn); kerry_car (actor 2, spawnSet); v (actor 3, findInContext).

Entries: `Start 0` → 1; `JohnnyHighwayCut` → 375; `Start 1` → 311.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 12 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnDialogLineEvent` | 26 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 62 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 317 / 374 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/0` |
| `scnPlaySkAnimEvent` | 27 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 4 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsSocket` | 29 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, gaze: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech: 1
- speech, socket_signal: 1
- socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `7da44a681810816a8c4eb471c667f881981f3cc5d13a3d54a316f035555de7c6`. Binary SHA-256: `87b09523c8c24ff390ba8ddd7e95abae95462de0470e5bef3530db509c1948cc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_03_freeway_drive.scene" --events
```

## `base\quest\side_quests\sq017\scenes\sq017_04_highwaymen.scene`

471 graph nodes, 629 edges; 101 event-bearing sections, 636 events; 143 screenplay lines, 23 screenplay options, 14 choice nodes.

Actors: kerry (actor 0, spawnSet); truck_driver (actor 1, spawnSet); johnny (actor 2, spawnDespawn); truck_crewman (actor 3, spawnSet); crew_truck (actor 4, spawnSet); kerry_vehicle (actor 5, spawnSet); v (actor 6, findInContext).

Entries: `Start_arrival` → 1; `Start_setup` → 12; `Start 9` → 2133; `Start1` → 2581; `Start 18` → 4313; `Start 13` → 2627; `Start 14` → 2643; `Truck_only` → 2254; `Start 12` → 2444.

Exits: `End_setup` → 15; `JohnnyFreewayCut` → 3270.

End nodes: 15: `NonTerminating`; 3270: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 31 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnChangeIdleAnimEvent` | 27 | 16 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 102 | 3 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scnGameplayActionEvent` | 1 | 4178 / 2553 | `/Data/RootChunk/sceneGraph/Data/graph/344/Data/events/3` |
| `scnGameplayTransitionEvent` | 12 | 356 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/12` |
| `scnIKEvent` | 32 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtAdvancedEvent` | 2 | 828 / 577 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/6` |
| `scnLookAtEvent` | 170 | 3 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnPlaySkAnimEvent` | 113 | 3 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnUnmountEvent` | 12 | 356 / 175 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/11` |
| `scneventsAttachPropToPerformer` | 4 | 828 / 565 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 828 / 590 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/15` |
| `scneventsEquipItemToPerformer` | 1 | 651 / 435 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 15 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsSocket` | 126 | 3 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 651 / 448 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/13` |
| `scneventsVFXDurationEvent` | 4 | 2251 / 1573 | `/Data/RootChunk/sceneGraph/Data/graph/153/Data/events/5` |
| `scneventsVFXEvent` | 2 | 2251 / 1572 | `/Data/RootChunk/sceneGraph/Data/graph/153/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 29
- skeletal_animation, gaze: 15
- speech, skeletal_animation, gaze, socket_signal: 7
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech: 2
- speech, gaze, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- speech, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, vfx: 1
- skeletal_animation, ik, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- props_equipment: 1
- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- gaze, audio: 1

Raw SHA-256: `6ac6158c577227a6de0de511c154cd0967253a40e78989df3b733dcad0d4a4b7`. Binary SHA-256: `40cef68997ad9d4f3bffef1f9e02a72ed5ebf5287a23f44bb2383e49c3846c82`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_04_highwaymen.scene" --events
```

## `base\quest\side_quests\sq017\scenes\sq017_05_car_chase.scene`

56 graph nodes, 70 edges; 13 event-bearing sections, 90 events; 22 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: kerry (actor 0, spawnSet); Johnny (actor 1, findInContext); kerry_car (actor 2, spawnSet); v (actor 3, findInContext).

Entries: `Start_pursuit_chats` → 1; `Start_pursuit_end` → 3; `Start_caliente` → 26.

Exits: `End_pursuit_chats` → 2; `End_caliente_no` → 4; `End_caliente_yes` → 20; `End_pursuit_end` → 24.

End nodes: 2: `NonTerminating`; 4: `<omitted>`; 20: `<omitted>`; 24: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 18 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 12 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/11` |
| `scnIKEvent` | 4 | 12 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnLookAtEvent` | 27 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 21 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnUnmountEvent` | 2 | 12 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 3 | 9 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsSocket` | 8 | 9 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 3
- skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech: 1
- gaze, socket_signal: 1

Raw SHA-256: `71513ca6552e791c2a20341dbed2f4a955e5cc396c9858d04f92f2c73b1c68b4`. Binary SHA-256: `abd3324a29270edf485c2116b95a555e2baf90d72a0670cc8ddf67b654dcba46`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_05_car_chase.scene" --events
```

## `base\quest\side_quests\sq017\scenes\sq017_06_capitan_caliente.scene`

239 graph nodes, 314 edges; 66 event-bearing sections, 423 events; 106 screenplay lines, 19 screenplay options, 8 choice nodes.

Actors: kerry (actor 0, spawnSet); caliente_waitress (actor 1, community); caliente_man (actor 2, community); johnny (actor 3, spawnDespawn); kerry_vehicle (actor 4, spawnSet); v (actor 5, findInContext).

Entries: `Start 8` → 1410; `Start_order_new` → 764; `Start 14` → 2770; `Start1` → 2580; `Start 11` → 1780; `Start 12` → 1786.

Exits: `End _breakfast` → 16.

End nodes: 16: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 20 | 397 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scnDialogLineEvent` | 75 | 38 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnGameplayTransitionEvent` | 4 | 89 / 139 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/15` |
| `scnIKEvent` | 8 | 89 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/7` |
| `scnLookAtEvent` | 122 | 38 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 84 | 38 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnUnmountEvent` | 4 | 89 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/14` |
| `scneventsAttachPropToPerformer` | 7 | 1096 / 621 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/1` |
| `scneventsAttachPropToWorld` | 7 | 1096 / 622 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/2` |
| `scneventsCameraParamsEvent` | 6 | 820 / 436 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 4 | 89 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/13` |
| `scneventsSocket` | 80 | 38 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsVFXEvent` | 2 | 792 / 250 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, socket_signal: 8
- gaze: 8
- speech, skeletal_animation, gaze, socket_signal: 7
- speech: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, gaze: 5
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- socket_signal: 2
- camera: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, camera: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1
- skeletal_animation, props_equipment: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `b202b75a8bd00708f9f01053fa394c9f28bc77f9bb7ec8007b7a31afcf427291`. Binary SHA-256: `9a932021c622aab5fa268776abf0becb94d4c0e8f1b6bfa1d253ea024a4a7c7a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_06_capitan_caliente.scene" --events
```

## `base\quest\tertiary_characters\default_dialogues\kerry_default.scene`

80 graph nodes, 93 edges; 19 event-bearing sections, 347 events; 81 screenplay lines, 15 screenplay options, 3 choice nodes.

Actors: Kerry (actor 0, spawnSet); johnny (actor 1, spawnDespawn); Kerry_holo (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `in` → 1; `Start 0` → 28; `holo_vt_in` → 362; `holo_in` → 233.

Exits: `holo_out` → 2; `deactivage_while_sleeping_out` → 504; `holo_facetoface_out` → 431.

End nodes: 2: `<omitted>`; 431: `NonTerminating`; 504: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 59 | 6 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 71 | 6 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 102 | 6 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnPlaySkAnimEvent` | 106 | 6 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scneventsSocket` | 9 | 77 / 347 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, idle_animation: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation: 1

Raw SHA-256: `1301781925d78c195ca1e02ef8a243983d53e29d48ca3b1ab00306db0fa1996a`. Binary SHA-256: `c9c576e33f27c06bc132778758877bedf1351540e78883fd34ebdca7c7e0bce2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\tertiary_characters\default_dialogues\kerry_default.scene" --events
```

