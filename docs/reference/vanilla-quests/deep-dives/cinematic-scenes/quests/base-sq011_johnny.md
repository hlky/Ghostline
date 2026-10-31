# Second Conflict: scene presentation

Journal identity: `quests/side_quest/sq011_johnny`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq011_johnny.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\fixers\padre\scenes\padre_default.scene`

71 graph nodes, 72 edges; 9 event-bearing sections, 61 events; 30 screenplay lines, 5 screenplay options, 1 choice nodes.

Actors: Padre (actor 0, spawnSet); Padre_holo (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `facetoface_in` → 1; `holocall_in` → 86; `welcome` → 41; `talk_later_in` → 47; `enter_idle_in` → 229; `enter_limited_in` → 230.

Exits: `holocall_out` → 2; `welcome_out` → 140; `holo_to_facetoface_out` → 220; `talk_later_out` → 48.

End nodes: 2: `<omitted>`; 48: `<omitted>`; 140: `<omitted>`; 220: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 25 | 10 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnLookAtEvent` | 12 | 10 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 11 | 10 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsSocket` | 13 | 10 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 3
- speech: 2
- socket_signal: 2
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation: 1

Raw SHA-256: `7dbd751bf02ef7dda3ceb75f4a651ab4308eed78247f7829ed69dd5a6387d518`. Binary SHA-256: `f14800f90c08c2ea0f35102a99dd6e6360e6736645da5fa7783f6296f186de58`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\fixers\padre\scenes\padre_default.scene" --events
```

## `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\scenes\ma_wat_nid_03_brief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `regina_brief_in` → 1.

Exits: `regina_brief_out` → 2; `rejected_out` → 271.

End nodes: 2: `<omitted>`; 271: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 39 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `f2337a3b5d42c23de048f3631f1e619786968cd90d4d23bf7dfc817e6c0d1f64`. Binary SHA-256: `2ca0bedd17dbf43a206f7847c3ae17d6d98c9d37e2511cd89d29b4e15345141e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\northside\ma_wat_nid_03\scenes\ma_wat_nid_03_brief.scene" --events
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

## `base\quest\side_quests\sq011\scenes\sq011_00_intro.scene`

82 graph nodes, 94 edges; 20 event-bearing sections, 176 events; 53 screenplay lines, 14 screenplay options, 6 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `sq011_00_intro_in` → 1.

Exits: `Kill Signal` → 745; `sq011_00_intro_out` → 84.

End nodes: 84: `NonTerminating`; 745: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 333 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnDialogLineEvent` | 50 | 111 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 35 | 333 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnPlaySkAnimEvent` | 36 | 333 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/6` |
| `scneventsAttachPropToNode` | 9 | 333 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/11` |
| `scneventsAttachPropToPerformer` | 5 | 333 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/9` |
| `scneventsSocket` | 33 | 333 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 4
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `fc272c2f42c2a3512bdb412f36bdf1943e404b254d026f699aae4361d36d146e`. Binary SHA-256: `4666d597a4edbb0b4acf48d83f035e8426f22869113227716e05ab00a3996ea6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq011\scenes\sq011_00_intro.scene" --events
```

## `base\quest\side_quests\sq011\scenes\sq011_01_kerry_mansion.scene`

585 graph nodes, 730 edges; 119 event-bearing sections, 740 events; 239 screenplay lines, 44 screenplay options, 26 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Kerry (actor 1, spawnSet); Stephen (actor 2, spawnSet); Player (actor 3, findInContext); V_Posessed (actor 4, findInContext).

Entries: `sq011_01_bots_comment_in` → 1542; `drinking_with_kerry_preview` → 2670; `intercom_scene_preview` → 2684; `sq011_01_kerry_in` → 197; `calling_nancy_preview` → 2762; `guitar_wall_preview` → 2941; `drinking_upstairs_preview` → 2951; `v_collapse_preview` → 3000; `stephen_holocall_preview` → 3012.

Exits: `sq011_01_kerry_out` → 2; `sq011_01_kill_singal_out` → 1813; `sq011_01_bots_comment_out` → 3990.

End nodes: 2: `NonTerminating`; 1813: `<omitted>`; 3990: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 796 / 294 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/5` |
| `scnChangeIdleAnimEvent` | 60 | 171 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 213 | 171 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 4 | 1335 / 964 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/16` |
| `scnIKEvent` | 8 | 1335 / 951 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/4` |
| `scnLookAtAdvancedEvent` | 4 | 906 / 373 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/11` |
| `scnLookAtEvent` | 90 | 171 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnPlaySkAnimEvent` | 153 | 171 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnUnmountEvent` | 4 | 1335 / 963 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/15` |
| `scneventsAttachPropToNode` | 3 | 532 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/3` |
| `scneventsAttachPropToPerformer` | 10 | 532 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/2` |
| `scneventsAttachPropToWorld` | 8 | 1013 / 457 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/10` |
| `scneventsCameraParamsEvent` | 12 | 1013 / 443 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 4 | 1335 / 959 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/12` |
| `scneventsSocket` | 140 | 171 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 23 | 532 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 23
- speech, skeletal_animation, gaze, socket_signal: 13
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- speech, skeletal_animation: 10
- speech, skeletal_animation, socket_signal: 10
- speech, skeletal_animation, idle_animation, socket_signal: 5
- speech, skeletal_animation, idle_animation: 4
- speech, skeletal_animation, gaze: 4
- camera: 4
- speech, skeletal_animation, idle_animation, gaze: 3
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 2
- speech, gaze: 2
- speech, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, audio, socket_signal: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, camera, props_equipment: 1
- idle_animation: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- idle_animation, socket_signal: 1
- gaze, socket_signal: 1
- vfx: 1

Raw SHA-256: `c31f751ab6d2200c77f7e034dd53149aba13e847f4846bef56062bb61c7bc32e`. Binary SHA-256: `a76cc673c14f414315823db02166623bfb4bb48229306f6ee35847f4a441fe94`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq011\scenes\sq011_01_kerry_mansion.scene" --events
```

## `base\quest\side_quests\sq011\scenes\sq011_02_totentanz.scene`

111 graph nodes, 133 edges; 14 event-bearing sections, 73 events; 24 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Johnny (actor 0, spawnSet); Bouncer (actor 1, spawnSet); ElevatorMaelstrom (actor 2, community); Player (actor 3, findInContext).

Entries: `sq011_01_enter_totentanz_in` → 709; `elevator_ride` → 1216; `sq011_01_drive_to_totentanz_in` → 648.

Exits: `sq011_01_drive_to_totentanz_out` → 1225.

End nodes: 1225: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 668 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnDialogLineEvent` | 21 | 668 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnLookAtEvent` | 9 | 668 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scnPlaySkAnimEvent` | 15 | 668 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |
| `scneventsSocket` | 19 | 711 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, gaze: 2
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- idle_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `1d759eab2a70dee454122e1d985cc62a617e16c303e0598e4982cbb044055d12`. Binary SHA-256: `daf148d3d92617df6a300afb9dad25f24194a136a2b3c9759642b2b18b760174`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq011\scenes\sq011_02_totentanz.scene" --events
```

## `base\quest\side_quests\sq011\scenes\sq011_07a_royce.scene`

454 graph nodes, 540 edges; 73 event-bearing sections, 587 events; 179 screenplay lines, 18 screenplay options, 7 choice nodes.

Actors: Johnny (actor 0, spawnSet); Royce (actor 1, spawnSet); DumDum (actor 2, spawnSet); Nancy (actor 3, spawnSet); sq011_maelstrom_machete (actor 4, community); sq011_maelstrom_rifle (actor 5, community); sq011_maelstrom_shotgun (actor 6, community); sq011_maelstrom_room_guard (actor 7, community); sq011_totentanz_bouncer (actor 8, spawnSet); sq011_maelstrom_elevator (actor 9, community); Player (actor 10, findInContext).

Entries: `sq011_07a_royce_in` → 1; `walking_to_car` → 2663; `sq011_07a_nancy_in` → 1558; `sneaking_out_preview` → 2127; `nancy_by_elevator_prev` → 2141; `test_royce_interview` → 1799.

Exits: `sq011_07a_royce_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1808 / 1902 | `/Data/RootChunk/sceneGraph/Data/graph/208/Data/events/2` |
| `scnChangeIdleAnimEvent` | 36 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 155 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 8 | 8 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/19` |
| `scnIKEvent` | 16 | 8 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnLookAtEvent` | 106 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 126 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 8 | 8 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/18` |
| `scneventsCameraParamsEvent` | 6 | 1291 / 910 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 8 | 8 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/15` |
| `scneventsSocket` | 111 | 4 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsVFXEvent` | 6 | 8 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/22` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, socket_signal: 7
- speech, skeletal_animation: 6
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 3
- skeletal_animation, gaze, socket_signal: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- socket_signal: 2
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- camera: 2
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, audio: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, socket_signal: 1

Raw SHA-256: `dd9e959dae12148616ccb8e0a6598e080bf4948fa2d737b5405a7c86aa3b110e`. Binary SHA-256: `5acb80fc5fadf66d248bc809e710cf64cff95a04cbde5105e04b15e9bc63bb44`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq011\scenes\sq011_07a_royce.scene" --events
```

## `base\quest\side_quests\sq011\scenes\sq011_07b_thugs.scene`

535 graph nodes, 628 edges; 100 event-bearing sections, 654 events; 196 screenplay lines, 13 screenplay options, 5 choice nodes.

Actors: Johnny (actor 0, spawnSet); sq011_maelstrom_machete (actor 1, community); sq011_maelstrom_rifle (actor 2, community); sq011_maelstrom_shotgun (actor 3, community); Nancy (actor 4, spawnSet); Patricia (actor 5, community); Brick (actor 6, spawnSet); sq011_totentanz_bouncer (actor 7, spawnSet); sq011_elevator_maelstromer (actor 8, community); Player (actor 9, findInContext).

Entries: `sq011_07b_patricia_in` → 1; `walkin_with_pati_prev` → 2258; `elevator_with_nancy` → 2375; `pat_is_king_preview` → 1606; `sq011_07b_patricia_combat_in` → 1213; `brick_is_boss_preview` → 1705; `brick_interview` → 1731; `nancy_saved_preview` → 1767.

Exits: `sq011_07b_patricia_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 29 | 330 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |
| `scnDialogLineEvent` | 162 | 323 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scnGameplayTransitionEvent` | 9 | 488 / 480 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/5` |
| `scnIKEvent` | 18 | 488 / 475 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 1075 / 1471 | `/Data/RootChunk/sceneGraph/Data/graph/173/Data/events/5` |
| `scnLookAtEvent` | 133 | 330 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scnPlaySkAnimEvent` | 129 | 330 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/2` |
| `scnUnmountEvent` | 9 | 488 / 479 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/4` |
| `scneventsCameraParamsEvent` | 5 | 1156 / 1595 | `/Data/RootChunk/sceneGraph/Data/graph/189/Data/events/3` |
| `scneventsEquipItemToPerformer` | 2 | 330 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 9 | 488 / 477 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/3` |
| `scneventsSocket` | 140 | 330 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/11` |
| `scneventsUnequipItemFromPerformer` | 2 | 330 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/10` |
| `scneventsVFXEvent` | 5 | 790 / 1024 | `/Data/RootChunk/sceneGraph/Data/graph/129/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, skeletal_animation, socket_signal: 13
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- speech, skeletal_animation: 8
- skeletal_animation, gaze, socket_signal: 7
- socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 4
- gaze: 4
- speech, gaze: 2
- speech, idle_animation: 2
- skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, idle_animation, gaze, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `52d59ad46a5db1cd82ab4df2d9294952bd6a47814fbfbc89a604899e64da5ba0`. Binary SHA-256: `636c254c2b5d31c0d94cb4aad920d3f1bed438fa5b27e362bbc5d61096a1cdfb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq011\scenes\sq011_07b_thugs.scene" --events
```

## `base\quest\side_quests\sq011\scenes\sq011_07c_combat.scene`

12 graph nodes, 8 edges; 4 event-bearing sections, 25 events; 14 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: sq011_ws_club_thug_11 (actor 0, community); sq011_ws_club_thug_10 (actor 1, community); sq011_ws_club_thug_05 (actor 2, community); sq011_ws_club_thug_08 (actor 3, community); sq011_ws_club_thug_09 (actor 4, community); sq011_ws_club_thug_07 (actor 5, community).

Entries: `thug08_in` → 13; `thug11_in` → 1; `thug09_in` → 18; `thug10_in` → 8.

Exits: `thug08_out` → 12; `thug11_out` → 2; `thug09_out` → 19; `thug10_out` → 9.

End nodes: 2: `<omitted>`; 9: `<omitted>`; 12: `<omitted>`; 19: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 14 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 11 | 7 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 3
- speech: 1

Raw SHA-256: `b0b5dfae830678d74b77d118158e5bf37274f0c10db6d7da005f8c6daec09ead`. Binary SHA-256: `51f4649df4a3665a5dae69197f53f065566dd32d989e8543ce5d90da8f1a8f91`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq011\scenes\sq011_07c_combat.scene" --events
```

## `base\quest\side_quests\sq011\scenes\sq011_08_nancy_saved.scene`

208 graph nodes, 277 edges; 34 event-bearing sections, 199 events; 70 screenplay lines, 10 screenplay options, 6 choice nodes.

Actors: Johnny (actor 0, spawnSet); Nancy (actor 1, spawnSet); Kerry (actor 2, spawnSet); nancy_car (actor 3, spawner); Player (actor 4, findInContext).

Entries: `sq011_08_ride_in` → 1; ` nancy_ride_prev` → 972; `kerry_call_prev` → 1044; `linestoreuse` → 1632; `johnny_comment_preview` → 712; `at_n54_preview` → 769.

Exits: `sq011_08_ride_out` → 106.

End nodes: 106: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 18 | 33 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 60 | 33 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 33 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/14` |
| `scnIKEvent` | 8 | 33 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scnLookAtEvent` | 34 | 33 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnPlaySkAnimEvent` | 38 | 33 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 3 | 33 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/13` |
| `scneventsEquipItemToPerformer` | 3 | 558 / 556 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 7 | 33 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/12` |
| `scneventsSocket` | 23 | 33 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |
| `scneventsUnequipItemFromPerformer` | 1 | 558 / 566 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/9` |
| `scneventsVFXEvent` | 1 | 558 / 554 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 4
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation: 4
- speech: 3
- speech, gaze: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- skeletal_animation, socket_signal, animation_state: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, vfx, socket_signal: 1
- speech, idle_animation: 1

Raw SHA-256: `cd3d3d3af54766d3d061fc94f48bec7b17052744c6066233921eb3d13a3b6d31`. Binary SHA-256: `05d3898873c59246edfd28b0a50e8d71f09d9575aa2e6992a5adc24842ce81c0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq011\scenes\sq011_08_nancy_saved.scene" --events
```

## `base\quest\side_quests\sq011\scenes\sq011_08b_denny_henry.scene`

399 graph nodes, 519 edges; 64 event-bearing sections, 582 events; 144 screenplay lines, 14 screenplay options, 10 choice nodes.

Actors: Johnny (actor 0, spawnSet); Henry (actor 1, spawnSet); Kerry (actor 2, spawnSet); Denny (actor 3, spawnSet); kerrys_car (actor 4, spawnSet); Player (actor 5, findInContext).

Entries: `sq011_08b_denny_villa_in` → 6; `sq011_08b_denny_return_in` → 1026; `sad_ending_test` → 1068; `denny_argument_prev` → 1163; `decision_preview` → 1169.

Exits: `sq011_08b_denny_villa_out` → 7; `sq011_08b_denny_interrupted_out` → 1024.

End nodes: 7: `NonTerminating`; 1024: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 329 / 512 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/14` |
| `scnChangeIdleAnimEvent` | 27 | 8 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 121 | 5 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 7 | 12 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/25` |
| `scnIKEvent` | 18 | 12 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scnLookAtEvent` | 142 | 8 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 112 | 5 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnUnmountEvent` | 7 | 12 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/24` |
| `scneventsAttachPropToNode` | 1 | 1725 / 2680 | `/Data/RootChunk/sceneGraph/Data/graph/343/Data/events/0` |
| `scneventsAttachPropToPerformer` | 2 | 1138 / 1970 | `/Data/RootChunk/sceneGraph/Data/graph/213/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 329 / 515 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/17` |
| `scneventsSetAnimFeatureEvent` | 10 | 12 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/23` |
| `scneventsSocket` | 131 | 8 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 13
- speech: 10
- gaze: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- props_equipment: 2
- skeletal_animation, ik, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze: 1
- skeletal_animation, socket_signal: 1
- idle_animation, socket_signal: 1
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `c6c1722d34877881d19f4600fabfa1cf3bc7d5de02937754e6c100bb7ee6a09a`. Binary SHA-256: `43f62deb4160dc6b09a8d5be53882669920ab6db781e473e6b57b3c21263f226`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq011\scenes\sq011_08b_denny_henry.scene" --events
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

