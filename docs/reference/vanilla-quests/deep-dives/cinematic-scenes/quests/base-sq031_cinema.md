# Blistering Love: scene presentation

Journal identity: `quests/side_quest/sq031_cinema`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq031_cinema.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq031\scenes\sq031_00_johnny.scene`

72 graph nodes, 97 edges; 9 event-bearing sections, 80 events; 17 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: Johnny (actor 0, spawnSet); Emmerick (actor 1, spawnSet); Claire (actor 2, spawnSet); Player (actor 3, findInContext); V_Posessed (actor 4, findInContext).

Entries: `sq031_00_johnny_in` → 1.

Exits: `sq031_00_johnny_out` → 2; `sq031_00_kill_signal` → 376.

End nodes: 2: `NonTerminating`; 376: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 94 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scnChangeIdleAnimEvent` | 3 | 91 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 16 | 36 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 174 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/9` |
| `scnIKEvent` | 4 | 174 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |
| `scnLookAtEvent` | 14 | 36 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 36 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnUnmountEvent` | 2 | 174 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/8` |
| `scneventsAttachPropToPerformer` | 1 | 94 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scneventsAttachPropToWorld` | 1 | 94 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/9` |
| `scneventsCameraParamsEvent` | 2 | 94 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 2 | 174 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/5` |
| `scneventsSocket` | 20 | 91 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsVFXEvent` | 3 | 174 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `bbcddebd33f1697156cb824787c8e2dc87512b43fb42e758f6fbd31633d94de6`. Binary SHA-256: `64bba6134c1e4ca9f8f91e3fbb7f0ade8162aed8510726f00c62ecbc97678205`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_00_johnny.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_01a_smack_afterlife.scene`

90 graph nodes, 117 edges; 23 event-bearing sections, 233 events; 32 screenplay lines, 7 screenplay options, 5 choice nodes.

Actors: Johnny (actor 0, spawnSet); Rogue (actor 1, spawnSet); Clair (actor 2, spawnSet); Emmerick (actor 3, spawnSet); bar_guest (actor 4, spawnDespawn); V_Posessed (actor 5, findInContext).

Entries: `sq031_01_afterlife_bartender_in` → 18; `sq031_01a_not_leave_out` → 522; `Start 5` → 1512.

Exits: `sq031_01_afterlife_bartender_out` → 906.

End nodes: 906: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 19 | 397 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnChangeIdleAnimEvent` | 3 | 20 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 21 | 20 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnLookAtEvent` | 24 | 397 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnPlaySkAnimEvent` | 37 | 20 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsAttachPropToPerformer` | 17 | 397 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scneventsAttachPropToWorld` | 16 | 397 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/13` |
| `scneventsEquipItemToPerformer` | 2 | 1057 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/0` |
| `scneventsSocket` | 41 | 20 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 20 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsVFXDurationEvent` | 8 | 1068 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/4` |
| `scneventsVFXEvent` | 43 | 20 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 4
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 3
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 3
- speech: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- gaze: 1
- speech, gaze: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `52a9eecfadce9ccabc716eb30bdb86b5495dccddc61a0d71b25d9b4a07e75c41`. Binary SHA-256: `5693f9900a3dd57156e83e40943ad77adbc8cc22bbddc38655011c00cdc4a44d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_01a_smack_afterlife.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_01b_smack_tatto.scene`

67 graph nodes, 86 edges; 9 event-bearing sections, 91 events; 15 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Johnny (actor 0, spawnSet); Cassious (actor 1, spawnSet); Pandora (actor 2, spawner); Player (actor 3, findInContext).

Entries: `sq031_01_tattoo_in` → 206.

Exits: `sq031_01_tattoo_out` → 209; `cleaning_aftelife` → 548.

End nodes: 209: `NonTerminating`; 548: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 14 | 207 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scnChangeIdleAnimEvent` | 2 | 207 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnDialogLineEvent` | 14 | 207 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scnLookAtEvent` | 8 | 207 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/12` |
| `scnPlaySkAnimEvent` | 16 | 207 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsAttachPropToPerformer` | 6 | 207 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 207 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scneventsCameraParamsEvent` | 1 | 311 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/5` |
| `scneventsSocket` | 15 | 207 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 265 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |
| `scneventsVFXEvent` | 11 | 207 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- gaze: 1

Raw SHA-256: `db75917f60f7f0f6e7831a0cf4fab2c898d9a6885b53c400365eaa24c60193cf`. Binary SHA-256: `0c70b7ce455b78943eb9298ea453cc5ae69bda5850ca1dfd6a1ca1a769ebbb80`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_01b_smack_tatto.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_01c_smack_striptease.scene`

307 graph nodes, 355 edges; 38 event-bearing sections, 493 events; 49 screenplay lines, 7 screenplay options, 6 choice nodes.

Actors: Johnny (actor 0, spawnSet); Ruby (actor 1, community); Barkeeper (actor 2, community); Brawler1 (actor 3, community); Brawler2 (actor 4, community); Guard (actor 5, community); Simone (actor 6, spawner); Drunk_Guy (actor 7, spawner); Drunk_Girl (actor 8, spawner); Cybereyes_Guy (actor 9, spawner); Back_Woman (actor 10, spawner); player_tpp_male (actor 11, spawnDespawn); player_tpp_female (actor 12, spawnDespawn); Ruby_vehicle (actor 13, spawner); Player (actor 14, findInContext).

Entries: `preview` → 2913; `preview_02` → 2924; `sq031_01_streapptease_in` → 225; `sq031_01_brawl_in` → 1540.

Exits: `sq031_01_smbu_ends_out` → 285.

End nodes: 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 36 | 227 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnChangeIdleAnimEvent` | 14 | 252 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 36 | 286 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/17` |
| `scnGameplayActionEvent` | 1 | 853 / 411 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/6` |
| `scnGameplayTransitionEvent` | 4 | 858 / 502 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/26` |
| `scnIKEvent` | 8 | 858 / 468 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/1` |
| `scnLookAtEvent` | 35 | 252 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scnPlaySkAnimEvent` | 94 | 227 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 4 | 858 / 501 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/25` |
| `scneventsAttachPropToPerformer` | 26 | 252 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsAttachPropToWorld` | 22 | 252 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/23` |
| `scneventsCameraParamsEvent` | 35 | 227 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 12 | 853 / 392 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/0` |
| `scneventsSocket` | 84 | 227 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 2207 / 1596 | `/Data/RootChunk/sceneGraph/Data/graph/154/Data/events/7` |
| `scneventsVFXEvent` | 81 | 227 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 3
- speech: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 2
- skeletal_animation, camera, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, audio, socket_signal: 2
- skeletal_animation, camera, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx: 1
- skeletal_animation, idle_animation, gaze, camera, audio, vfx: 1
- speech, skeletal_animation, idle_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, vfx, socket_signal: 1
- skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, gaze, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, camera, vfx, socket_signal: 1
- skeletal_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- skeletal_animation, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, audio: 1
- gaze: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, camera, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `9d1cb74e02d78066dc72d2216a7e907c23ac8300d364fcecb7b6231b96a9051b`. Binary SHA-256: `7fa17cdf91324ef625312f04551d8ed9f82db96756d1071bbc7672c826758aab`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_01c_smack_striptease.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_01d_smack_rogue.scene`

154 graph nodes, 179 edges; 27 event-bearing sections, 257 events; 85 screenplay lines, 16 screenplay options, 8 choice nodes.

Actors: Johnny (actor 0, spawnSet); Rogue (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `sq031_01_motel_fluff_2_in` → 2086; `sq031_01_motel_fluff_1_in` → 712; `q115_reuse_johnny` → 955; `sq031_01_motel_arrived_in` → 305.

Exits: `sq031_01_motel_room_out` → 311; `sq031_01_motel_fluff_out` → 1128.

End nodes: 311: `<omitted>`; 1128: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 633 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/5` |
| `scnChangeIdleAnimEvent` | 3 | 633 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/2` |
| `scnDialogLineEvent` | 79 | 633 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scnGameplayTransitionEvent` | 1 | 848 / 672 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/6` |
| `scnIKEvent` | 2 | 848 / 667 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/1` |
| `scnLookAtEvent` | 44 | 633 / 131 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnPlaySkAnimEvent` | 49 | 633 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scnUnmountEvent` | 1 | 848 / 676 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/9` |
| `scneventsAttachPropToPerformer` | 1 | 740 / 347 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/9` |
| `scneventsAttachPropToWorld` | 1 | 740 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/15` |
| `scneventsCameraParamsEvent` | 8 | 633 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 1 | 848 / 674 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/8` |
| `scneventsSocket` | 55 | 633 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/3` |
| `scneventsVFXEvent` | 3 | 677 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 13
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 2
- speech, skeletal_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech: 1

Raw SHA-256: `8acada1d6551ab4dc3efcc8e08c44650fd4d36a8a281ac2545fdad472b5eda63`. Binary SHA-256: `b9542e945e13d006a29a4628f8fd724a06101671b515f51f58e35ec63b8811e3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_01d_smack_rogue.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_02a_rogue_call.scene`

36 graph nodes, 37 edges; 4 event-bearing sections, 9 events; 8 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Rogue (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `sq031_02a_rogue_call_rejected_in` → 253; `sq031_02a_rogue_call_in` → 1.

Exits: `sq031_02a_rogue_call_out` → 2; `sq031_02a_rogue_call_rejected_out` → 263; `rejected_out` → 304.

End nodes: 2: `<omitted>`; 263: `<omitted>`; 304: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 8 | 12 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 1 | 12 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, gaze: 1

Raw SHA-256: `664f7cc89bd7c676fa2b531217da1e0e4e71a98237d2af97d09cfa1449010570`. Binary SHA-256: `c06b8203c7f5e0d03aad229bd895a68595f9f2a9c358e348e2e8860b879d41e9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_02a_rogue_call.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_02b_rogue_afterlife.scene`

282 graph nodes, 363 edges; 44 event-bearing sections, 261 events; 86 screenplay lines, 15 screenplay options, 8 choice nodes.

Actors: Johnny (actor 0, spawnSet); Rogue (actor 1, spawnSet); Emmerick (actor 2, spawnSet); Weyland (actor 3, spawnSet); sq031_ebunike_worker_1 (actor 4, spawner); sq031_ebunike_worker_2 (actor 5, spawner); sq031_ebunike_worker_3 (actor 6, spawner); rogue_car (actor 7, spawnSet); Player (actor 8, findInContext).

Entries: `preview_ebunike` → 1142; `placeholder` → 1469; `sq031_rogue_afterlife_timelapse_in` → 1218; `sq031_rogue_afterlife_in` → 203; `preview_01` → 1256; `sq031_02b_emmerick_warning_in` → 252; `q115_reuse_clone_in` → 1294.

Exits: `q115_reuse_clone_out` → 1296; `sq031_rogue_afterlife_timelapse_out` → 1220; `sq031_rogue_afterlife_out` → 185; `sq031_02b_emmerick_warning_out` → 253.

End nodes: 185: `NonTerminating`; 253: `<omitted>`; 1220: `NonTerminating`; 1296: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 327 / 232 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/4` |
| `scnChangeIdleAnimEvent` | 5 | 237 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnDialogLineEvent` | 78 | 181 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 210 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnIKEvent` | 4 | 210 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnLookAtEvent` | 86 | 181 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 35 | 210 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnUnmountEvent` | 1 | 210 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scneventsAttachPropToPerformer` | 1 | 1103 / 996 | `/Data/RootChunk/sceneGraph/Data/graph/134/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 5 | 210 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scneventsSocket` | 36 | 210 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scneventsVFXEvent` | 2 | 600 / 476 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 13
- speech: 8
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, gaze, vfx: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- gaze: 1
- skeletal_animation, gaze: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, audio, socket_signal, animation_state: 1

Raw SHA-256: `014f4cbd928c1809cda451cc95b116c32fe20d1fa9d60f7195f65c656f44c2f3`. Binary SHA-256: `40a1de3e505a89b92eb99087ce8210fa131631473625a99d9dc37a864b00c5e5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_02b_rogue_afterlife.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_03_ebunike.scene`

277 graph nodes, 329 edges; 57 event-bearing sections, 183 events; 110 screenplay lines, 8 screenplay options, 5 choice nodes.

Actors: Rogue (actor 0, spawnSet); Grayson (actor 1, findInContext); Johnny (actor 2, spawnSet); Smasher (actor 3, findInContext); Anthony (actor 4, findInContext); rogue_car (actor 5, spawnSet); Player (actor 6, findInContext).

Entries: `sq031_02_ebunike_in` → 1; `sq031_03_ebunike_data_term_in` → 284; `sq031_03_right_here_in` → 1111; `sq031_03_data_term_found_in` → 293; `sq031_rogue_let_open` → 586; `sq031_door_opened` → 588; `preview_clues` → 1716; `sq031_03_ship_spotted_in` → 109; `sq031_02_ebunike_after_timelpase_in` → 1258; `sq031_03_ebunike_combat_in` → 1838; `sq031_rogue_idea_in` → 1026; `Tobeimplemented` → 764.

Exits: `sq031_03_ebunike_data_term_out` → 286; `sq031_03_right_here_out` → 1112; `sq031_03_data_term_found_out` → 295; `sq031_rogue_let_open_out` → 587; `sq031_door_opened_out` → 589; `sq031_03_ship_spotted_out` → 137; `sq031_02_ebunike_out` → 1256; `sq031_03_ebunike_combat_out` → 1839; `sq031_rogue_idea_out` → 1027; `Kill Signal Again` → 1580; `Kill Ebunike` → 1583; `sq031_02_ebunike_securing_out` → 1072; `sq031_02_ebunike_after_timelpase_out` → 273.

End nodes: 137: `NonTerminating`; 273: `NonTerminating`; 286: `<omitted>`; 295: `NonTerminating`; 587: `<omitted>`; 589: `<omitted>`; 1027: `<omitted>`; 1072: `NonTerminating`; 1112: `<omitted>`; 1256: `NonTerminating`; 1580: `<omitted>`; 1583: `<omitted>`; 1839: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1269 / 1092 | `/Data/RootChunk/sceneGraph/Data/graph/203/Data/events/3` |
| `scnDialogLineEvent` | 107 | 110 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 1269 / 1093 | `/Data/RootChunk/sceneGraph/Data/graph/203/Data/events/4` |
| `scnIKEvent` | 4 | 823 / 560 | `/Data/RootChunk/sceneGraph/Data/graph/114/Data/events/0` |
| `scnLookAtEvent` | 45 | 127 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnPlaySkAnimEvent` | 10 | 816 / 516 | `/Data/RootChunk/sceneGraph/Data/graph/109/Data/events/3` |
| `scnUnmountEvent` | 1 | 1269 / 1097 | `/Data/RootChunk/sceneGraph/Data/graph/203/Data/events/7` |
| `scneventsEquipItemToPerformer` | 1 | 829 / 588 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 2 | 823 / 563 | `/Data/RootChunk/sceneGraph/Data/graph/114/Data/events/2` |
| `scneventsSocket` | 10 | 335 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 829 / 598 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 33
- speech, gaze: 14
- speech, skeletal_animation, gaze: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `49e59343f3211c4bfce3acb800ceae8ecd354f38fe3f748fead90fd7ddaf7523`. Binary SHA-256: `470052ed000d296a5e0a2114a718744d48339399f931d929db6f3a60b5a72ddc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_03_ebunike.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_03a_ebunike_patrols.scene`

18 graph nodes, 12 edges; 6 event-bearing sections, 27 events; 28 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Maelstrom_Leader (actor 0, community); Maelstrom_Thug_1a (actor 1, community); Maelstrom_Thug_2a (actor 2, community); Maelstrom_Thug_3a (actor 3, community); Maelstrom_Thug_4a (actor 4, community); Maelstrom_Thug_5a (actor 5, community); Maelstrom_Thug_6a (actor 6, community); Maelstrom_Thug_7 (actor 7, community); Maelstrom_Thug_8 (actor 8, community); Maelstrom_Thug_9 (actor 9, community); Maelstrom_Thug_10 (actor 10, community); Player (actor 11, findInContext).

Entries: `sq031_03a_mealstrom_patrol_1_in` → 1; `sq031_03a_mealstrom_patrol_4_in` → 22; `sq031_03a_mealstrom_patrol_5_in` → 27; `sq031_03a_mealstrom_patrol_2_in` → 12; `sq031_03a_mealstrom_patrol_6_in` → 32; `sq031_03a_mealstrom_patrol_3_in` → 17.

Exits: `sq031_03a_mealstrom_patrol_3_out` → 18; `sq031_03a_mealstrom_patrol_1_out` → 2; `sq031_03a_mealstrom_patrol_4_out` → 23; `sq031_03a_mealstrom_patrol_5_out` → 28; `sq031_03a_mealstrom_patrol_2_out` → 13; `sq031_03a_mealstrom_patrol_6_out` → 33.

End nodes: 2: `<omitted>`; 13: `<omitted>`; 18: `<omitted>`; 23: `<omitted>`; 28: `<omitted>`; 33: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 27 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6

Raw SHA-256: `8dd7330889a03b1abd84f1eeb42dcdba27a03fc47fff2021d2940977c8748a51`. Binary SHA-256: `10dddac80f0d47363bdb0e9a924417e01227f32ab77ac54baa68331f05aec45a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_03a_ebunike_patrols.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_04_grayson.scene`

564 graph nodes, 686 edges; 79 event-bearing sections, 635 events; 155 screenplay lines, 22 screenplay options, 14 choice nodes.

Actors: Rogue (actor 0, spawnSet); Grayson (actor 1, spawnSet); Johnny (actor 2, spawnSet); porsche (actor 3, spawnSet); rogue_car (actor 4, spawnSet); Player (actor 5, findInContext).

Entries: `sq031_04_grayson_in` → 1; `Tobereused` → 1625; `sq031_04_ruby_necrology_in` → 1118; `Start 11` → 2728; `sq031_04_grayson_shooting_in` → 185; `sq031_04_car_lift_in` → 1293; `preview_grayson_interrogation` → 1915; `sq031_04_ebunike_door_opened_in` → 2458; `Start 12` → 3107; `placeholder` → 2059; `do not connect` → 2067.

Exits: `sq031_04_grayson_out` → 2; `sq031_04_ruby_necrology_out` → 1119; `sq031_04_car_lift_out` → 2778; `sq031_04_grayson_shooting_out` → 186; `sq031_04_ebunike_door_opened_out` → 2459; `sq031_04_interrogation_failed_out` → 2497; `sq031_04_rogue_messages_out` → 1524.

End nodes: 2: `<omitted>`; 186: `NonTerminating`; 1119: `<omitted>`; 1524: `NonTerminating`; 2459: `<omitted>`; 2497: `<omitted>`; 2778: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 16 | 187 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnChangeIdleAnimEvent` | 10 | 187 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/7` |
| `scnDialogLineEvent` | 143 | 135 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 956 / 558 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/9` |
| `scnIKEvent` | 2 | 956 / 547 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/1` |
| `scnLookAtEvent` | 125 | 135 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnPlaySkAnimEvent` | 265 | 187 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scnUnmountEvent` | 1 | 956 / 557 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/8` |
| `scneventsAttachPropToPerformer` | 4 | 1002 / 606 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/10` |
| `scneventsAttachPropToWorld` | 2 | 1512 / 1200 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 956 / 553 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/5` |
| `scneventsSocket` | 65 | 187 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 18
- speech, skeletal_animation, gaze: 15
- speech, skeletal_animation, gaze, socket_signal: 12
- speech, skeletal_animation: 7
- speech, skeletal_animation, socket_signal: 5
- gaze: 5
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, audio, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, audio: 1
- idle_animation: 1

Raw SHA-256: `cf04b40a7b1414ea83474c15b5e857025ae0191e9aa4323ed9d3e592a638d73b`. Binary SHA-256: `9d1a6b6da1f7ebff5df647329af8a92eb6026b1022a40995055aa0588d84f54e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_04_grayson.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_05_grave.scene`

262 graph nodes, 319 edges; 70 event-bearing sections, 495 events; 157 screenplay lines, 40 screenplay options, 19 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `preview_02` → 1231; `sq031_05_fridge_in` → 867; `linesforreuse` → 1295; `sq031_05_follow_up_in` → 293; `sq031_05_grave_in` → 91; `grave_preview` → 1152.

Exits: `sq031_friends_out` → 60; `sq031_05_follow_up_out` → 1520; `sq031_05_fridge_out` → 1522; `sq031_not_friends_out` → 798.

End nodes: 60: `<omitted>`; 798: `<omitted>`; 1520: `<omitted>`; 1522: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 548 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scnChangeIdleAnimEvent` | 5 | 555 / 131 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scnDialogLineEvent` | 145 | 92 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 946 / 1115 | `/Data/RootChunk/sceneGraph/Data/graph/115/Data/events/7` |
| `scnIKEvent` | 4 | 946 / 1108 | `/Data/RootChunk/sceneGraph/Data/graph/115/Data/events/1` |
| `scnLookAtEvent` | 110 | 551 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scnOverridePhantomParamsEvent` | 8 | 562 / 155 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/5` |
| `scnPlaySkAnimEvent` | 92 | 92 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 2 | 946 / 1114 | `/Data/RootChunk/sceneGraph/Data/graph/115/Data/events/6` |
| `scneventsAttachPropToPerformer` | 13 | 555 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |
| `scneventsAttachPropToWorld` | 8 | 645 / 512 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/6` |
| `scneventsEquipItemToPerformer` | 12 | 599 / 321 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 2 | 946 / 1110 | `/Data/RootChunk/sceneGraph/Data/graph/115/Data/events/3` |
| `scneventsSocket` | 68 | 92 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 8 | 599 / 327 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/3` |
| `scneventsVFXEvent` | 12 | 562 / 154 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 14
- speech, skeletal_animation, gaze: 13
- speech: 7
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 6
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 4
- speech, skeletal_animation: 3
- skeletal_animation, socket_signal: 3
- gaze: 3
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, props_equipment: 2
- props_equipment: 2
- speech, skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1

Raw SHA-256: `8429d9a32eef9bdfe9e19e740f2202472a21bd6ff7292a250cab491541130da6`. Binary SHA-256: `9425bde9137417b96a9a6f42f9b534f5197be0e2ec5203ecb7546af15ad5d5de`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_05_grave.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_06_rogue_call.scene`

31 graph nodes, 29 edges; 4 event-bearing sections, 13 events; 13 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Rogue (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `linestoreuse` → 352; `sq031_06_johnny_request_in` → 55; `Librarytoreuse` → 250.

Exits: `sq031_06_rogue_call_out` → 2; `Kill Signal` → 190.

End nodes: 2: `NonTerminating`; 190: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 12 | 42 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 1 | 42 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, gaze: 1

Raw SHA-256: `5a9d5d446831f8836077bac9fe6af851b4746fbb471bccee1b49c569bbacb841`. Binary SHA-256: `991a468b999cb0b8f4b1a52185fe84e7410943433952469fdd8acb72f50cb257`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_06_rogue_call.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_07_cinema.scene`

401 graph nodes, 487 edges; 46 event-bearing sections, 354 events; 104 screenplay lines, 15 screenplay options, 13 choice nodes.

Actors: Johnny (actor 0, spawnSet); Rogue (actor 1, spawnSet); Emmerick (actor 2, spawnSet); johnny_secret_room (actor 3, spawner); Player (actor 4, findInContext); V_Posessed (actor 5, findInContext).

Entries: `preview` → 1612; `Start 16` → 2455; `preview_emmerick` → 2076; `preview_flex` → 2883; `sq031_07_cinema_in` → 1300; `secret_room_believe_in` → 2222; `secret_room_inside_in` → 2224; `preview_cinema` → 1451; `sq031_07_pick_up_in` → 302; `sq031_07_find_bushido_in` → 712; `Start 8` → 1914.

Exits: `secret_room_believe_out` → 2226; `secret_room_inside_out` → 2227; `sq031_07_pick_up_out` → 304; `sq031_07_find_bushido_out` → 713; `Kill Cinema` → 1909; `sq031_bushido_failed_out` → 1528.

End nodes: 304: `NonTerminating`; 713: `NonTerminating`; 1528: `<omitted>`; 1909: `<omitted>`; 2226: `<omitted>`; 2227: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 874 / 637 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/2` |
| `scnChangeIdleAnimEvent` | 4 | 218 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 81 | 13 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 319 / 243 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/15` |
| `scnIKEvent` | 10 | 319 / 230 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/5` |
| `scnLookAtEvent` | 55 | 13 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/5` |
| `scnPlaySkAnimEvent` | 119 | 13 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnUnmountEvent` | 5 | 319 / 242 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/14` |
| `scneventsAttachPropToPerformer` | 1 | 874 / 640 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/5` |
| `scneventsAttachPropToWorld` | 1 | 874 / 642 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/7` |
| `scneventsCameraParamsEvent` | 2 | 874 / 638 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/3` |
| `scneventsEquipItemToPerformer` | 1 | 1029 / 848 | `/Data/RootChunk/sceneGraph/Data/graph/77/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 5 | 319 / 238 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/11` |
| `scneventsSocket` | 59 | 218 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 3 | 874 / 657 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/17` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 8
- speech, skeletal_animation, gaze: 4
- gaze: 4
- speech: 3
- speech, gaze: 3
- speech, skeletal_animation: 3
- speech, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, audio, socket_signal: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `58fb66cc053717bb2d9a50a00250ef24cdf49d26935983e8ecf5e3a0e816435b`. Binary SHA-256: `6993336073c0b56789f8bea683dc00902869c93da937a9c66480fe04ea4b42b3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_07_cinema.scene" --events
```

## `base\quest\side_quests\sq031\scenes\sq031_08_movie.scene`

183 graph nodes, 233 edges; 52 event-bearing sections, 357 events; 104 screenplay lines, 26 screenplay options, 12 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Rogue (actor 1, spawnSet); V_Posessed (actor 2, findInContext); Player (actor 3, findInContext).

Entries: `rogue_leaves_02` → 1494; `sq031_08_preview` → 1031; `sq031_08_movie_in` → 296; `CYB-622932` → 1607.

Exits: `sq031_08_movie_out` → 200.

End nodes: 200: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 29 | 662 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/6` |
| `scnChangeIdleAnimEvent` | 6 | 131 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnDialogLineEvent` | 94 | 131 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 684 / 356 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/15` |
| `scnIKEvent` | 6 | 684 / 347 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/7` |
| `scnLookAtEvent` | 67 | 131 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnPlayRidAnimEvent` | 6 | 662 / 213 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/16` |
| `scnPlaySkAnimEvent` | 65 | 131 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnUnmountEvent` | 3 | 684 / 355 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/14` |
| `scneventsAttachPropToPerformer` | 2 | 764 / 419 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 927 / 614 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/3` |
| `scneventsCameraParamsEvent` | 14 | 662 / 198 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/4` |
| `scneventsPlayRidCameraAnimEvent` | 6 | 662 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 3 | 684 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/13` |
| `scneventsSocket` | 34 | 131 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/5` |
| `scneventsVFXEvent` | 17 | 662 / 205 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 11
- speech, gaze: 7
- speech, skeletal_animation, idle_animation, gaze: 4
- speech: 4
- speech, skeletal_animation: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, socket_signal: 2
- gaze: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, rid_actor, camera, rid_camera, audio, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, rid_actor, camera, rid_camera, vfx, socket_signal: 1

Raw SHA-256: `cce7a242390af88e9c7fcca97d4c467fff5f9ec494e530df115ef7d69165832a`. Binary SHA-256: `33be817d6b9243891ac5f43dd64df1b5c67706042d5eceed68af3e52f924b260`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq031\scenes\sq031_08_movie.scene" --events
```

