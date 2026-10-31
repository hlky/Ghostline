# A Like Supreme: scene presentation

Journal identity: `quests/side_quest/sq011_concert`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq011_concert.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

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

## `base\quest\side_quests\sq011\scenes\sq011_09_nancy_call.scene`

42 graph nodes, 42 edges; 5 event-bearing sections, 23 events; 11 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnSet); Nancy (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `nancy_call_preview` → 218; `sq011_06_concer_call_in` → 14; `sq011_06_concert_call_rejected_in` → 1126.

Exits: `sq011_06_concert_call_rejected_out` → 1140; `sq011_06_concer_call_out` → 15; `rejected_out` → 1114.

End nodes: 15: `<omitted>`; 1114: `<omitted>`; 1140: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnDialogLineEvent` | 10 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnLookAtEvent` | 5 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/5` |
| `scneventsCameraParamsEvent` | 1 | 219 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 2
- speech, idle_animation, gaze: 1
- speech, idle_animation: 1
- camera: 1

Raw SHA-256: `d44bec883ec0944252345caecc0b61742ced21a768fab8b3929ad85b37247eb8`. Binary SHA-256: `aab94055431c41a3d0fd04c8e533dc3dd5e7a639b298fa24382c8b2975226d0f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq011\scenes\sq011_09_nancy_call.scene" --events
```

## `base\quest\side_quests\sq011\scenes\sq011_10_concert.scene`

800 graph nodes, 1038 edges; 128 event-bearing sections, 1154 events; 271 screenplay lines, 36 screenplay options, 26 choice nodes.

Actors: Johnny (actor 0, spawnSet); Nancy (actor 1, spawnSet); Henry (actor 2, spawnSet); Kerry (actor 3, spawnSet); BarOwner (actor 4, community); Denny (actor 5, spawnSet); Drausin (actor 6, community); Girl_Fan (actor 7, spawnDespawn); Boy_Fan (actor 8, spawnDespawn); Girl_Fan_02 (actor 9, spawnDespawn); v_tpp_female (actor 10, spawnDespawn); v_tpp_male (actor 11, spawnDespawn); Karim (actor 12, spawner); Player (actor 13, findInContext); V_Posessed (actor 14, findInContext).

Entries: `concert_preview` → 2134; `taking_pills_preview` → 2269; `before_concert_prev` → 3710; `sq011_10_concert_in` → 247; `Start 12` → 4586; `player_performance` → 3273; `concert_scene_testing` → 1916; `chat_with_band_prev` → 3351; `vocals_test` → 4778; `concert_starts` → 5548; `after_concert` → 5553; `post_concert_preview` → 2088.

Exits: `sq011_10_concert_out` → 487; `to_concert` → 5546; `concert_ends` → 5551.

End nodes: 487: `NonTerminating`; 5546: `NonTerminating`; 5551: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 19 | 534 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/10` |
| `scnChangeIdleAnimEvent` | 94 | 534 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnDialogLineEvent` | 163 | 524 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnGameplayTransitionEvent` | 4 | 524 / 98 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/16` |
| `scnIKEvent` | 8 | 524 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |
| `scnLookAtEvent` | 242 | 524 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/6` |
| `scnPlayRidAnimEvent` | 4 | 1364 / 1075 | `/Data/RootChunk/sceneGraph/Data/graph/101/Data/events/2` |
| `scnPlaySkAnimEvent` | 299 | 524 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scnPoseCorrectionEvent` | 2 | 2372 / 3034 | `/Data/RootChunk/sceneGraph/Data/graph/296/Data/events/1` |
| `scnUnmountEvent` | 4 | 524 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/15` |
| `scneventsAttachPropToNode` | 17 | 2122 / 2614 | `/Data/RootChunk/sceneGraph/Data/graph/239/Data/events/0` |
| `scneventsAttachPropToPerformer` | 24 | 563 / 262 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/1` |
| `scneventsAttachPropToWorld` | 12 | 563 / 266 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/5` |
| `scneventsCameraParamsEvent` | 11 | 1376 / 1362 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 4 | 524 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/12` |
| `scneventsSocket` | 236 | 524 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scneventsVFXEvent` | 11 | 574 / 287 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 21
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 17
- speech, skeletal_animation, gaze, socket_signal: 10
- speech: 9
- speech, skeletal_animation, idle_animation, gaze: 4
- socket_signal: 4
- camera: 4
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- skeletal_animation, gaze: 3
- skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, idle_animation: 3
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- idle_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- idle_animation, socket_signal: 2
- skeletal_animation: 2
- props_equipment: 2
- socket_signal, animation_state: 2
- vfx: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, rid_actor, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- idle_animation, props_equipment: 1
- speech, skeletal_animation: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera: 1

Raw SHA-256: `deb95de4df36cead9a924724c3e6e9528fd2ac931fba195a0776ce902c01dbf4`. Binary SHA-256: `cbdae241c5cc5bff475fa8c709c91b8f5bbe4a45022608c52842a76aa7e3be94`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq011\scenes\sq011_10_concert.scene" --events
```

