# M'ap Tann Pèlen: scene presentation

Journal identity: `quests/main_quest/act_01/q110_01_voodooboys`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q110_01_voodooboys.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\community\e3_2019\scenes\e3_q110_warehouse_chat.scene`

66 graph nodes, 73 edges; 4 event-bearing sections, 31 events; 10 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: garage_dirtboy_001 (actor 0, spawnSet); garage_dirtboy_002 (actor 1, spawnSet); garage_driver (actor 2, spawnSet); car (actor 3, spawnSet).

Entries: `warehouse_chat_001_start` → 1; `warehouse_chat_002_start` → 8.

Exits: `warehouse_chat_001_end` → 2; `warehouse_chat_002_end` → 9.

End nodes: 2: `<omitted>`; 9: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 5 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnChangeIdleAnimEvent` | 2 | 5 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 8 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 5 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/19` |
| `scnIKEvent` | 2 | 5 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scnLookAtEvent` | 6 | 5 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnPlaySkAnimEvent` | 3 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 1 | 5 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 1 | 5 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scneventsSocket` | 6 | 5 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- skeletal_animation, socket_signal: 1
- idle_animation: 1

Raw SHA-256: `aa63c0e0e743689c6368c90abf75564724b746838a4660edf03923bab92930be`. Binary SHA-256: `7820fea279fdff455d26c82351e9d8f5edbcdce4fe0de21e23af63fc9fc56a3c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\community\e3_2019\scenes\e3_q110_warehouse_chat.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_00_fixer.scene`

90 graph nodes, 112 edges; 19 event-bearing sections, 59 events; 49 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: mr_hands (actor 0, spawnSet); johnny (actor 1, findInContext); v (actor 2, findInContext).

Entries: `q110_calling_fixer_in` → 1; `OLD` → 630; `Start1` → 643; `MrHandsCallsBackIn` → 228.

Exits: `q110_calling_fixer_out` → 2; `WaitForMrHandsOut` → 222.

End nodes: 2: `<omitted>`; 222: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 48 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 1 | 641 / 384 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/1` |
| `scneventsSocket` | 10 | 151 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, socket_signal: 9
- gaze, socket_signal: 1

Raw SHA-256: `27415004730e7bd7e2da388cf686018398f7819db362e8ea310d66727e1d0a9a`. Binary SHA-256: `ec395068019bceb557ac45a6ff8d27bb718b0d382a6eeb91e971a95ac4a2318c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_00_fixer.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_01_sermon.scene`

102 graph nodes, 123 edges; 16 event-bearing sections, 128 events; 45 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: sermon_leader (actor 0, spawnSet); Johnny (actor 1, spawnSet); voodoo_contact (actor 2, spawnSet); faithfull_interactive_01 (actor 3, findInWorld); faithfull_interactive_02 (actor 4, findInWorld); faithfull_interactive_03 (actor 5, findInWorld); faithfull_interactive_04 (actor 6, findInWorld); faithfull_synced_01 (actor 7, findInWorld); Player (actor 8, findInContext).

Entries: `ChapeGateAnimationIn` → 820; `q110_01_sermon_in` → 18; `WaitingForSermonIn` → 933.

Exits: `q110_01_cut_all_signal` → 453; `q110_01_sermon_out` → 19; `WaitingForSermonOut` → 964.

End nodes: 19: `NonTerminating`; 453: `<omitted>`; 964: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 27 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnChangeIdleAnimEvent` | 3 | 158 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/0` |
| `scnDialogLineEvent` | 39 | 25 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 265 / 269 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/7` |
| `scnIKEvent` | 4 | 265 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/3` |
| `scnLookAtEvent` | 13 | 25 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/28` |
| `scnPlaySkAnimEvent` | 36 | 25 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 1 | 25 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 2 | 265 / 276 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/13` |
| `scneventsCameraParamsEvent` | 2 | 27 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 2 | 265 / 272 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/10` |
| `scneventsSocket` | 21 | 25 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation: 1
- gaze: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `f02b4063ff0191f833165c7b22934639e818e7c5ffdd8cb9f1ae9f90d2b2bc06`. Binary SHA-256: `7dc322fca6ab9ae1fe33ff85dbc8c9b1a485fcb275f7195389fae8b23dce62a4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_01_sermon.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_02_placide.scene`

263 graph nodes, 378 edges; 50 event-bearing sections, 265 events; 92 screenplay lines, 13 screenplay options, 6 choice nodes.

Actors: placide (actor 0, spawnSet); butcher_01 (actor 1, spawnSet); johnny (actor 2, findInContext); vendor (actor 3, spawnSet); grandma (actor 4, spawnSet); chicken_alive (actor 5, spawnSet); chicken_alive_2 (actor 6, spawnSet); v (actor 7, findInContext).

Entries: `q110_02_butcher_in` → 271; `Downstairs` → 668; `Start 13` → 973.

Exits: `q110_02_placide_after_gate_end` → 1237; `q110_02_butcher_out` → 272; `SwitchTime` → 769; `DespawnSermon` → 1072; `AVScene` → 1084.

End nodes: 272: `NonTerminating`; 769: `NonTerminating`; 1072: `NonTerminating`; 1084: `NonTerminating`; 1237: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 348 / 141 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/9` |
| `scnChangeIdleAnimEvent` | 8 | 348 / 154 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/22` |
| `scnDialogLineEvent` | 62 | 273 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 348 / 160 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/27` |
| `scnIKEvent` | 2 | 348 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/6` |
| `scnLookAtEvent` | 82 | 273 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlayRidAnimEvent` | 3 | 348 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/2` |
| `scnPlaySkAnimEvent` | 36 | 273 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 1 | 1045 / 678 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/7` |
| `scnUnmountEvent` | 1 | 348 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/26` |
| `scneventsAttachPropToPerformer` | 3 | 784 / 439 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/0` |
| `scneventsAttachPropToWorld` | 4 | 348 / 143 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 1 | 348 / 155 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/23` |
| `scneventsSocket` | 57 | 273 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scneventsVFXEvent` | 2 | 348 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- gaze: 7
- speech, skeletal_animation, gaze, socket_signal: 6
- speech, gaze: 5
- speech, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 3
- skeletal_animation: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, ik, rid_actor, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, socket_signal: 1
- props_equipment: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze: 1
- idle_animation, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `78844af1d2d20ac0789edb532c0e8ce560ac1f9399389b45c14aaf5d3aba1fa0`. Binary SHA-256: `1c5318c3a185d3b6d6ac39d522a07eaa1a12bc0484122dfdcb2e66f198db9979`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_02_placide.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_03_market.scene`

289 graph nodes, 348 edges; 38 event-bearing sections, 335 events; 89 screenplay lines, 1 screenplay options, 0 choice nodes.

Actors: placide (actor 0, spawnSet); grann_ertha (actor 1, spawnSet); vdb_entrance (actor 2, spawnSet); flirting_girl (actor 3, spawnSet); food_chat_man_01 (actor 4, spawnSet); food_chat_man_02 (actor 5, spawnSet); old_man_chatting_01 (actor 6, spawnSet); old_man_chatting_02 (actor 7, spawnSet); welcoming_vendor (actor 8, spawnSet); vdb_corridor_01 (actor 9, spawnSet); vdb_corridor_02 (actor 10, spawnSet); vdb_guard_lift_01 (actor 11, spawnSet); vdb_guard_lift_02 (actor 12, spawnSet); vdb_entrance_2 (actor 13, spawnSet); vdb_stairs_1 (actor 14, spawnSet); vdb_stairs_2 (actor 15, spawnSet); vdb_av_shooter (actor 16, spawnSet); tv (actor 17, spawner); vdb_office_goon_03 (actor 18, spawnSet); couch_dude_01 (actor 19, spawnSet); couch_dude_02 (actor 20, spawnSet); couch_dude_03 (actor 21, spawnSet); v (actor 22, findInContext).

Entries: `q110_03_market_in` → 91; `Start 15` → 1180; `TVNewsCastIn` → 1033; `TvSceneBackup` → 1842; `MarketTestIn` → 513.

Exits: `q110_03_market_spline_out` → 1149; `q110_03_market_out` → 127; `TVNewsCastOut` → 1037; `change_time` → 511.

End nodes: 127: `<omitted>`; 511: `NonTerminating`; 1037: `NonTerminating`; 1149: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 168 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnChangeIdleAnimEvent` | 4 | 168 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnDialogLineEvent` | 70 | 139 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnGameplayTransitionEvent` | 4 | 139 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scnIKEvent` | 8 | 139 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 113 | 139 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 56 | 139 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 4 | 139 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsAttachPropToPerformer` | 4 | 168 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scneventsAttachPropToWorld` | 2 | 168 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/19` |
| `scneventsCameraParamsEvent` | 2 | 1452 / 1097 | `/Data/RootChunk/sceneGraph/Data/graph/147/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 4 | 139 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsSocket` | 60 | 139 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 6
- gaze: 6
- speech, gaze: 6
- speech: 4
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `d67729e8a23d853974ee2f4a2cd53c8a0b599a4e28441bbaf2c058ba140a9d41`. Binary SHA-256: `c9e184e76cf6e29ea8ba221fdb1c623d98a645613e7ed08f914924c5fd1fc55d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_03_market.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_04_netrunners_den.scene`

347 graph nodes, 446 edges; 70 event-bearing sections, 515 events; 138 screenplay lines, 27 screenplay options, 12 choice nodes.

Actors: placide (actor 0, spawnSet); vdb_netrunner (actor 1, spawnSet); johnny (actor 2, spawnDespawn); Goon_1 (actor 3, spawnSet); Goon_2 (actor 4, spawnSet); Goon_3 (actor 5, spawnSet); holocall_placide (actor 6, spawnDespawn); ti_neptune (actor 7, community); guard_garage_01 (actor 8, spawnSet); guard_garage_02 (actor 9, spawnSet); Player (actor 10, findInContext).

Entries: `q110_04_netrunners_den_in` → 1; `vdb_interrupt` → 1782; `q110_04_signal_test_in` → 267; `q110_04_guards_garage` → 2308.

Exits: `q110_04_netrunners_den_out` → 2; `UnlockElevators` → 815; `EnablePlacideDefault` → 1191; `q110_04_guards_garage_terminate` → 2558; `q110_04_signal_test_out` → 268.

End nodes: 2: `<omitted>`; 268: `<omitted>`; 815: `NonTerminating`; 1191: `NonTerminating`; 2558: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 220 / 459 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/6` |
| `scnChangeIdleAnimEvent` | 21 | 98 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 114 | 98 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 3 | 919 / 925 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/15` |
| `scnIKEvent` | 9 | 343 / 575 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/6` |
| `scnLookAtEvent` | 108 | 98 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnPlaySkAnimEvent` | 119 | 98 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnUnmountEvent` | 3 | 919 / 931 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/20` |
| `scneventsCameraParamsEvent` | 8 | 98 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 3 | 919 / 927 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/17` |
| `scneventsSocket` | 117 | 98 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsVFXEvent` | 6 | 138 / 295 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 9
- speech: 9
- gaze: 8
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 5
- skeletal_animation, socket_signal: 4
- skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation: 2
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- idle_animation, gaze: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, socket_signal: 1
- speech, skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, camera, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `45b1d4cc2fa63bd64719a99a61a2ff2e934e0061c7c63107ff8f87614d3a62f3`. Binary SHA-256: `bcfcfb2c56d22945b0638d62d28e49a7dbb5b9df5cf7d20b01d896a0dcd04dae`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_04_netrunners_den.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_13_alt_intro.scene`

683 graph nodes, 799 edges; 72 event-bearing sections, 667 events; 154 screenplay lines, 30 screenplay options, 17 choice nodes.

Actors: Briggite (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Elder_1 (actor 2, spawnSet); Elder_2 (actor 3, spawnSet); Elder_3 (actor 4, spawnSet); Alt (actor 5, spawnSet); Elder_4 (actor 6, spawnSet); Elder_5 (actor 7, spawnSet); Placide (actor 8, spawnSet); V_tpp_male (actor 9, spawnDespawn); V_tpp_female (actor 10, spawnDespawn); TiNeptune (actor 11, spawnSet); johnny_replacer (actor 12, spawnSet); V (actor 13, findInContext).

Entries: `preview` → 3849; `q110_cyberspace_before_q108` → 3862; `bath_preview` → 2026; `cyberspace_preview` → 2052; `DebugStartTrainLights` → 3289; `cyberspace_recording` → 1509; `q110_13_before_q108_in` → 909; `q110_13_after_q108_in` → 914; `Start 9` → 2875; `Start 13` → 4777.

Exits: `cyberspace_recording_end` → 1522; `q110_13_before_q108_out` → 912; `q110_13_after_q108_out` → 917; `cyberspace_on` → 2847.

End nodes: 912: `<omitted>`; 917: `<omitted>`; 1522: `<omitted>`; 2847: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 45 | 1082 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/13` |
| `scnChangeIdleAnimEvent` | 28 | 1170 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |
| `scnDialogLineEvent` | 126 | 860 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 9 | 1082 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/23` |
| `scnIKEvent` | 18 | 1082 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/20` |
| `scnLookAtEvent` | 94 | 1170 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/2` |
| `scnPlaySkAnimEvent` | 109 | 860 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnPoseCorrectionEvent` | 4 | 1170 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/12` |
| `scnUnmountEvent` | 9 | 1082 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/22` |
| `scneventsAttachPropToNode` | 1 | 1667 / 613 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/3` |
| `scneventsAttachPropToPerformer` | 4 | 1355 / 341 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/13` |
| `scneventsAttachPropToWorld` | 1 | 1355 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/20` |
| `scneventsCameraParamsEvent` | 3 | 1082 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 9 | 1082 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/18` |
| `scneventsSocket` | 175 | 860 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/9` |
| `scneventsVFXEvent` | 32 | 1082 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 9
- speech: 8
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, socket_signal: 4
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, audio, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 3
- speech, skeletal_animation: 2
- skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- socket_signal: 2
- speech, skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- idle_animation, props_equipment, socket_signal: 1
- speech, audio: 1
- speech, skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- idle_animation, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, socket_signal: 1

Raw SHA-256: `a8db01eeec6c130696b01ccd33d26ecf7ac37519cc3721b25cfacf8da11bb191`. Binary SHA-256: `78ef65c267c826ba0796881b287a274992b25e2df1ad7ccb103af9b02a5b9df5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_13_alt_intro.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_14_alt.scene`

195 graph nodes, 362 edges; 56 event-bearing sections, 360 events; 137 screenplay lines, 24 screenplay options, 9 choice nodes.

Actors: Alt (actor 0, spawnSet); johnny (actor 1, spawnDespawn); voodoo_queen (actor 2, spawnSet); Mosley (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `q110_14_alt_in` → 566.

Exits: `q110_14_alt_out` → 462.

End nodes: 462: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 915 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/4` |
| `scnDialogLineEvent` | 124 | 576 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 77 | 576 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scnPlaySkAnimEvent` | 103 | 576 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 1111 / 671 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/3` |
| `scneventsSocket` | 50 | 576 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 1 | 1111 / 678 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 22
- skeletal_animation, socket_signal: 8
- speech: 7
- speech, skeletal_animation, gaze: 4
- speech, gaze: 3
- speech, skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, camera, vfx, socket_signal: 1
- idle_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `1860d4bf184b7dafa95d68fd5b5d6dd24a5146d14b746dd142d27c57f9eea910`. Binary SHA-256: `e9f18b5a26beb061f6e8822b76b53f310867c90218e59eed181ab211bce3398f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_14_alt.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_15_vdb_fight.scene`

132 graph nodes, 135 edges; 30 event-bearing sections, 141 events; 52 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); voodoo_boy_001 (actor 1, community); voodoo_boy_002 (actor 2, community); voodoo_boy_003 (actor 3, community); voodoo_boy_004 (actor 4, community); voodoo_boy_010 (actor 5, community); voodoo_boy_009 (actor 6, community); placide (actor 7, spawnSet); vdb_elder_01 (actor 8, spawnSet); vdb_elder_02 (actor 9, spawnSet); vdb_elder_03 (actor 10, spawnSet); vdb_elder_04 (actor 11, spawnSet); vdb_elder_05 (actor 12, spawnSet); voodoo_boy_005 (actor 13, community); voodoo_boy_006 (actor 14, community); brigitte (actor 15, spawnSet); Player (actor 16, findInContext).

Entries: `q110_15_escape_fight_in` → 15; `PlacideChurchFightIn` → 294; `Old` → 308; `q110_15_placide_in_chapel_in` → 197; `q110_15_alerted_patrol_in` → 322; `q110_15_what_was_that` → 208; `q110_15_johnny_need_to_go_in` → 238.

Exits: `q110_15_johnny_need_to_go_out` → 245; `PlacideChurchFightOut` → 295; `placide_chapel_done` → 312; `CheckingOnNetrunnersStart` → 557; `q110_15_alerted_patrol_out` → 324; `StopScene` → 686; `dead_netrunners_spotted` → 327; `alert_start_walking_out` → 330.

End nodes: 245: `NonTerminating`; 295: `<omitted>`; 312: `NonTerminating`; 324: `<omitted>`; 327: `NonTerminating`; 330: `NonTerminating`; 557: `NonTerminating`; 686: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 339 / 369 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/2` |
| `scnChangeIdleAnimEvent` | 8 | 239 / 255 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/1` |
| `scnDialogLineEvent` | 45 | 54 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 209 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/19` |
| `scnIKEvent` | 8 | 209 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/10` |
| `scnLookAtEvent` | 21 | 209 / 199 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/1` |
| `scnPlaySkAnimEvent` | 14 | 209 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/0` |
| `scnUnmountEvent` | 4 | 209 / 227 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/18` |
| `scneventsCameraParamsEvent` | 2 | 339 / 368 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 4 | 209 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/17` |
| `scneventsSocket` | 30 | 195 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- speech, socket_signal: 4
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal: 1
- idle_animation, gaze: 1
- gaze: 1

Raw SHA-256: `71c546eaa420e82f9b05682bcb7e0df6c57b0f488db048361099db7a4e33c880`. Binary SHA-256: `e1d2657efaa925906343037c49a1fd51768998324a02a2e96c8960256cd50339`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_15_vdb_fight.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_16b_closing_funeral.scene`

100 graph nodes, 109 edges; 24 event-bearing sections, 144 events; 44 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: placide (actor 0, spawnSet); voodoo_queen (actor 1, spawnSet); vdb_01 (actor 2, spawnSet); vdb_02 (actor 3, spawnSet); vdb_03 (actor 4, spawnSet); vdb_04 (actor 5, spawnSet); vdb_05 (actor 6, spawnSet); vdb_02_chapel (actor 7, community); Player (actor 8, findInContext).

Entries: `q110_16b_closing_funeral_in` → 1; `PlacideChatChapel` → 105.

Exits: `q110_16b_closing_funeral_out` → 2; `SwitchToEscape` → 69.

End nodes: 2: `NonTerminating`; 69: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 119 / 243 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/4` |
| `scnChangeIdleAnimEvent` | 4 | 25 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/6` |
| `scnDialogLineEvent` | 28 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 119 / 270 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/18` |
| `scnIKEvent` | 6 | 119 / 262 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/11` |
| `scnLookAtEvent` | 6 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 35 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 137 / 296 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/2` |
| `scnUnmountEvent` | 3 | 119 / 269 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/17` |
| `scneventsCameraParamsEvent` | 4 | 119 / 241 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 3 | 119 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/14` |
| `scneventsSocket` | 49 | 6 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 5
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech: 2
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, socket_signal, animation_state: 1
- idle_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `07050d795be87fa1ac31542dc3b6db8b34907951fb067c6b0a13ef3d6eef44a8`. Binary SHA-256: `4f656c230d846cf28b54b58dddbee57c3378b20472362c59adf5fde37b516404`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_16b_closing_funeral.scene" --events
```

## `ep1\openworld\fixers\mr_hands\scenes\mr_hands_combat_zone_default.scene`

324 graph nodes, 400 edges; 60 event-bearing sections, 249 events; 143 screenplay lines, 29 screenplay options, 10 choice nodes.

Actors: mr_hands (actor 0, spawnSet); mr_hands_holo (actor 1, spawnSet); johnny (actor 2, findInContext); Player (actor 3, findInContext).

Entries: `q110_calling_fixer_in` → 1185; `holo_in` → 1; `welcome` → 29; `q110_MrHandsCallsBackIn` → 1235; `debrief_perfect_in` → 949; `debrief_failed_in` → 955; `facetoface_in` → 112; `q110_2_fixer_in` → 1327; `enter_idle_in` → 757; `enter_limited_in` → 758; `prebrief_in` → 1110; `Start 4` → 1461.

Exits: `q110_calling_fixer_out` → 1187; `q110_WaitForMrHandsOut` → 1233; `debrief_perfect_end_out` → 951; `debrief_failed_end_out` → 957; `welcome_out` → 685; `debrief_rejected_perfect_out` → 1039; `holo_to_facetoface_out` → 743; `debrief_rejected_failed_out` → 1047; `holo_out` → 167; `prebrief_out` → 1112; `prebrief_rejected_out` → 1142; `End 3` → 1462.

End nodes: 167: `<omitted>`; 685: `<omitted>`; 743: `NonTerminating`; 951: `<omitted>`; 957: `<omitted>`; 1039: `<omitted>`; 1047: `<omitted>`; 1112: `<omitted>`; 1142: `<omitted>`; 1187: `<omitted>`; 1233: `<omitted>`; 1462: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 1538 / 1431 | `/Data/RootChunk/sceneGraph/Data/graph/246/Data/events/2` |
| `scnDialogLineEvent` | 131 | 795 / 264 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/0` |
| `scnLookAtEvent` | 16 | 102 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 54 | 102 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsSocket` | 44 | 102 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsVFXEvent` | 2 | 102 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 29
- speech, socket_signal: 14
- speech, skeletal_animation, socket_signal: 6
- gaze, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze: 1
- vfx: 1

Raw SHA-256: `ad261d8e5d174d9b2769cc2de36b766cf1cfdd9bcce43e0581c81dbf6135f6cd`. Binary SHA-256: `f3c2a479878811257c036b04c8aa8d6e39d69151c424744dc0ac7603208881a2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\fixers\mr_hands\scenes\mr_hands_combat_zone_default.scene" --events
```

