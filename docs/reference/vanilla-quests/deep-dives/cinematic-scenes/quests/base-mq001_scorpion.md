# I'll Fly Away: scene presentation

Journal identity: `quests/minor_quest/mq001_scorpion`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq001_scorpion.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq001\scenes\mq001_01_funeral_aftermath.scene`

118 graph nodes, 143 edges; 31 event-bearing sections, 169 events; 64 screenplay lines, 12 screenplay options, 5 choice nodes.

Actors: Mitch (actor 0, spawnSet); Mitch_Veh (actor 1, spawnSet); Scorpion_Veh (actor 2, community); V (actor 3, findInContext).

Entries: `Y_U_DISCONNECT` → 396; `Start` → 103.

Exits: `End` → 2; `Kill_Call_out` → 400; `ActivateOut` → 408.

End nodes: 2: `NonTerminating`; 400: `NonTerminating`; 408: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 16 | 38 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnDialogLineEvent` | 60 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 53 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scnIKEvent` | 4 | 53 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/5` |
| `scnLookAtEvent` | 21 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 43 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnUnmountEvent` | 2 | 53 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 2 | 53 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/8` |
| `scneventsSocket` | 19 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, skeletal_animation: 4
- speech, skeletal_animation, idle_animation: 4
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- idle_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `669ebc1c15b5d304af49d57a245baed9649660f726047a9b3241800cc3dc7df0`. Binary SHA-256: `2474dc9784d977c47fb704c786bb2d4ae7f881e4e6031ac95fde01052e18214c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq001\scenes\mq001_01_funeral_aftermath.scene" --events
```

## `base\quest\minor_quests\mq001\scenes\mq001_01_mood_scenes_funeral.scene`

11 graph nodes, 8 edges; 3 event-bearing sections, 17 events; 10 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: pile_scene_001_fat_001 (actor 0, community); pile_scene_001_child_001 (actor 1, community); pile_scene_001_child_002 (actor 2, community); pile_scene_002_man_001 (actor 3, community); pile_scene_002_man_002 (actor 4, community); bodies_scene_001_man_001 (actor 5, community); bodies_scene_001_woman_001 (actor 6, community); bodies_scene_001_woman_002 (actor 7, community); pile_scene_001_drone (actor 8, community).

Entries: `mq001_01_pile_scene_002_in` → 9; `mq001_01_pile_scene_001_in` → 1; `mq001_01_bodies_scene_001_in` → 11.

Exits: `mq001_01_pile_scene_002_out` → 10; `mq001_01_pile_scene_001_out` → 2; `mq001_01_bodies_scene_001_out` → 12.

End nodes: 2: `<omitted>`; 10: `<omitted>`; 12: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 10 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 4 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 1 | 6 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scneventsSocket` | 2 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `c48f67f935088ff2709791b71de53494c03d7e9be04a3091bbf53f5b3eced346`. Binary SHA-256: `bb254612a2cd16619c1b26152d7cf21965fbba2d8a47b057a61953e7fcc46f97`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq001\scenes\mq001_01_mood_scenes_funeral.scene" --events
```

## `base\quest\minor_quests\mq001\scenes\mq001_02_drive_to_cliff.scene`

38 graph nodes, 32 edges; 8 event-bearing sections, 55 events; 21 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Mitch (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Mitch_Veh (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `mq001_02_drive_start_in` → 1; `mq001_02_drive_chat_001_in` → 8; `mq001_02_drive_chat_004_in` → 86; `mq001_02_drive_arrived_in` → 53; `mq001_02_drive_chat_003_in` → 18; `mq001_02_drive_distance_warning_in` → 99.

Exits: `mq001_02_drive_start_out` → 2; `mq001_02_drive_chat_001_out` → 9; `mq001_02_drive_chat_004_out` → 87; `mq001_02_drive_arrived_out` → 54; `mq001_02_drive_chat_003_out` → 19; `mq001_02_drive_distance_warning_out` → 100.

End nodes: 2: `<omitted>`; 9: `<omitted>`; 19: `<omitted>`; 54: `<omitted>`; 87: `<omitted>`; 100: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 12 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 20 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 7 | 10 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |
| `scnPlaySkAnimEvent` | 9 | 10 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 3 | 10 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scneventsSocket` | 4 | 10 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- idle_animation, gaze, socket_signal, animation_state: 1

Raw SHA-256: `9b4f8393f67c30eb03a7776df1771acc3ee73376c4e40b020379732706aee194`. Binary SHA-256: `1a191ea7633a58228b3accf76c010c073e93b76ddbe6979bcb23ea601fff105a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq001\scenes\mq001_02_drive_to_cliff.scene" --events
```

## `base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene`

329 graph nodes, 407 edges; 62 event-bearing sections, 345 events; 100 screenplay lines, 16 screenplay options, 10 choice nodes.

Actors: Mitch (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Scorpion (actor 2, spawnSet); Mitch_Vehicle (actor 3, spawnSet); Scorpion_Vehicle (actor 4, community); V (actor 5, findInContext).

Entries: `Start 0` → 1; `CineStart 004` → 894; `CineStart 006` → 912; `CineStart 002` → 914; `CineStart 003` → 922; `DO_NOT_CONNECT_001` → 337; `CineStart 007` → 957; `CineStart 005` → 1002; `DO_NOT_CONNECT_004` → 771; `cinedebug_mitchstart` → 1700; `DO NOT CONNECT 002` → 549.

Exits: `End 0` → 2; `mq001_03_scene_end` → 992; `abandon` → 2318.

End nodes: 2: `NonTerminating`; 992: `NonTerminating`; 2318: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 15 | 40 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/2` |
| `scnChangeIdleAnimEvent` | 51 | 18 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnDialogLineEvent` | 76 | 7 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 56 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/14` |
| `scnIKEvent` | 10 | 56 / 150 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/7` |
| `scnLookAtEvent` | 50 | 18 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnPlaySkAnimEvent` | 57 | 18 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnUnmountEvent` | 5 | 56 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/13` |
| `scneventsAttachPropToNode` | 2 | 764 / 897 | `/Data/RootChunk/sceneGraph/Data/graph/113/Data/events/5` |
| `scneventsAttachPropToPerformer` | 4 | 192 / 436 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/34` |
| `scneventsEquipItemToPerformer` | 3 | 830 / 989 | `/Data/RootChunk/sceneGraph/Data/graph/118/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 7 | 56 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/10` |
| `scneventsSocket` | 52 | 56 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/3` |
| `scneventsUnequipItemFromPerformer` | 1 | 192 / 413 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/22` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1018 / 1178 | `/Data/RootChunk/sceneGraph/Data/graph/146/Data/events/20` |
| `scneventsVFXEvent` | 6 | 1018 / 1151 | `/Data/RootChunk/sceneGraph/Data/graph/146/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, idle_animation, gaze: 7
- speech, idle_animation: 6
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, idle_animation, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- socket_signal: 2
- gaze: 2
- speech, audio: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- idle_animation: 1
- props_equipment: 1
- skeletal_animation, gaze, audio, socket_signal, animation_state: 1
- idle_animation, socket_signal, animation_state: 1
- skeletal_animation, props_equipment, audio: 1

Raw SHA-256: `091ef779187ca6fd52414f609e152e5c37dcfae248f50ad10163568fead31162`. Binary SHA-256: `03444e090cbdf7ed3e50e5d61899d29f10e972970180b2ca42a3f354d98f64a4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_05a_transport_delivered.scene`

303 graph nodes, 380 edges; 35 event-bearing sections, 425 events; 64 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Saul (actor 0, spawnSet); Panam (actor 1, spawnSet); Carol (actor 2, spawnSet); Bob (actor 3, spawnSet); Teddy (actor 4, spawnSet); Cassidy (actor 5, spawnSet); Mitch (actor 6, spawnSet); guard1 (actor 7, community); guard2 (actor 8, community); guard3 (actor 9, community); Panzer_Flatbed_A (actor 10, community); Panzer_Flatbed_B (actor 11, community); V (actor 12, findInContext).

Entries: `sq027_05a_saul_reception_in` → 1; `cinedebug_end` → 1790; `cinedebug_panamend` → 1339.

Exits: `sq027_05a_saul_reception_out` → 2; `sq027_05a_scene_over_out` → 579.

End nodes: 2: `<omitted>`; 579: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 77 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 38 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 13 | 25 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/36` |
| `scnIKEvent` | 26 | 25 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/18` |
| `scnLookAtEvent` | 70 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 77 | 25 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnUnmountEvent` | 13 | 25 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/34` |
| `scneventsEquipItemToPerformer` | 3 | 350 / 582 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/112` |
| `scneventsSetAnimFeatureEvent` | 13 | 25 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/32` |
| `scneventsSocket` | 93 | 25 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 2 | 338 / 414 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, socket_signal: 8
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation: 3
- speech, idle_animation, gaze: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1

Raw SHA-256: `1161d3819c6445e6f39ff6f56e8a45629ac1a2b8bc2fbc4aeef1fc3c1fb07c0a`. Binary SHA-256: `07de58be6e6be0cbce17a082dc610f1df8043d525ab01dc7060ad15e213a90e6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_05a_transport_delivered.scene" --events
```

