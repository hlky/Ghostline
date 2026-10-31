# Violence: scene presentation

Journal identity: `quests/minor_quest/mq019_paparazzi`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq019_paparazzi.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq019\scenes\mq019_01_notell_motel.scene`

92 graph nodes, 118 edges; 24 event-bearing sections, 194 events; 80 screenplay lines, 13 screenplay options, 6 choice nodes.

Actors: Lizzy_Wizzy (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `in` → 1.

Exits: `out` → 2; `out_end_scene` → 212.

End nodes: 2: `NonTerminating`; 212: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 25 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnChangeIdleAnimEvent` | 2 | 614 / 695 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/7` |
| `scnDialogLineEvent` | 75 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 171 / 381 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/5` |
| `scnIKEvent` | 2 | 171 / 377 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/1` |
| `scnLookAtEvent` | 23 | 29 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnPlaySkAnimEvent` | 55 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnUnmountEvent` | 1 | 171 / 385 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/8` |
| `scneventsAttachPropToPerformer` | 5 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsAttachPropToWorld` | 2 | 124 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/6` |
| `scneventsCameraParamsEvent` | 1 | 171 / 380 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 1 | 171 / 383 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/7` |
| `scneventsSocket` | 20 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 2 | 124 / 231 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 7
- speech: 3
- speech, skeletal_animation, gaze: 3
- speech, gaze: 2
- speech, skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1

Raw SHA-256: `58a697ac3ef074fc0d2f11edffc8aefcd632e99a7c748a62eaf9915ec60ace04`. Binary SHA-256: `e8baed4c0d2e1b0f2ec0c844b15932797fc948db2f7070a58f76a5c0ac883b92`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq019\scenes\mq019_01_notell_motel.scene" --events
```

## `base\quest\minor_quests\mq019\scenes\mq019_03_night_club.scene`

132 graph nodes, 187 edges; 32 event-bearing sections, 201 events; 64 screenplay lines, 18 screenplay options, 11 choice nodes.

Actors: riot_barman (actor 0, spawnSet); riot_bouncer (actor 1, spawnSet); girl_01 (actor 2, community); girl_02 (actor 3, community); girl_03 (actor 4, community); staff_01 (actor 5, community); Player (actor 6, findInContext).

Entries: `in` → 1; `Start 2` → 651.

Exits: `out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 60 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/3` |
| `scnDialogLineEvent` | 58 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 175 / 392 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/11` |
| `scnIKEvent` | 4 | 175 / 387 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/6` |
| `scnLookAtEvent` | 26 | 26 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnPlaySkAnimEvent` | 63 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 2 | 175 / 396 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 2 | 175 / 394 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/13` |
| `scneventsSocket` | 35 | 4 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scneventsVFXEvent` | 6 | 149 / 314 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 7
- speech, skeletal_animation, gaze: 6
- speech, skeletal_animation, socket_signal: 3
- speech, gaze: 3
- socket_signal: 3
- speech, skeletal_animation, vfx: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `909d81a549129db8b74cec1a251b21018dc3d62c0beff8bf9c14d38ec5eb1c4d`. Binary SHA-256: `7733ed623dfa236f04a3fddd8f06aacd79882846672b29936982da43d9d9b973`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq019\scenes\mq019_03_night_club.scene" --events
```

## `base\quest\minor_quests\mq019\scenes\mq019_04_manager.scene`

158 graph nodes, 207 edges; 33 event-bearing sections, 158 events; 63 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: Liam (actor 0, community); Technician (actor 1, community); johnny (actor 2, spawnDespawn); Player (actor 3, findInContext).

Entries: `in` → 1; `in_combat` → 748; `in_johnny` → 200.

Exits: `out` → 302; `out_johnny` → 202; `out_overheard_done` → 223; `out_security_called` → 78.

End nodes: 78: `<omitted>`; 202: `NonTerminating`; 223: `NonTerminating`; 302: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 21 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |
| `scnDialogLineEvent` | 58 | 6 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 15 | 21 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnOverridePhantomParamsEvent` | 6 | 595 / 761 | `/Data/RootChunk/sceneGraph/Data/graph/109/Data/events/1` |
| `scnPlaySkAnimEvent` | 62 | 6 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 14 | 128 / 236 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/6` |
| `scneventsVFXEvent` | 2 | 128 / 232 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 12
- skeletal_animation, socket_signal, animation_state: 6
- speech, skeletal_animation, gaze: 5
- skeletal_animation, socket_signal: 3
- speech: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, gaze: 1
- socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `5157cc11f9e18c9097c2842d55c3bbd3118d1c6eb4c9d6c5f03bd302bbfbc62a`. Binary SHA-256: `1e614ec8620123f5e4a79be4c4585edb903fe3b8c06c1b602300c738ca873bf8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq019\scenes\mq019_04_manager.scene" --events
```

## `base\quest\minor_quests\mq019\scenes\mq019_05_holocall.scene`

48 graph nodes, 49 edges; 12 event-bearing sections, 28 events; 22 screenplay lines, 5 screenplay options, 4 choice nodes.

Actors: Lizzy_Wizzy (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 1` → 529; `in` → 1; `in_finale` → 58.

Exits: `out` → 2; `out_finale` → 59.

End nodes: 2: `<omitted>`; 59: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 65 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scnDialogLineEvent` | 22 | 9 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 2 | 12 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsSocket` | 3 | 65 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, gaze: 2
- speech, socket_signal: 2
- speech, audio, socket_signal: 1

Raw SHA-256: `1f2d29d2149669301ebf2eeda30be6cf51ed96e092c4aa8374238a8d563bd5d6`. Binary SHA-256: `344cddc2a7606266d9874fff5cfeffa7cf0085f95f0fd356681144fb17d5ea36`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq019\scenes\mq019_05_holocall.scene" --events
```

## `base\quest\minor_quests\mq019\scenes\mq019_06_finale.scene`

87 graph nodes, 106 edges; 13 event-bearing sections, 88 events; 34 screenplay lines, 9 screenplay options, 6 choice nodes.

Actors: Lizzy_Wizzy (actor 0, spawnSet); Liam (actor 1, community); Player (actor 2, findInContext).

Entries: `in` → 1.

Exits: `out_completed` → 2; `out_failed` → 110.

End nodes: 2: `NonTerminating`; 110: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 32 | 8 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnLookAtEvent` | 10 | 8 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 25 | 8 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scneventsEquipItemToPerformer` | 2 | 11 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/10` |
| `scneventsSocket` | 18 | 8 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scneventsUnequipItemFromPerformer` | 1 | 11 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `bfecfb54db2db748bae6363df0f78ecdcb9bce454d07c97d39e6500635a37330`. Binary SHA-256: `1ebcb660189727f33e5838d8e5a7db6f9e53db7571d2d3169c9e21f3067509ed`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq019\scenes\mq019_06_finale.scene" --events
```

