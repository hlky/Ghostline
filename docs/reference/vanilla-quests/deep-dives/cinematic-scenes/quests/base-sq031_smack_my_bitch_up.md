# A Cool Metal Fire: scene presentation

Journal identity: `quests/side_quest/sq031_smack_my_bitch_up`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq031_smack_my_bitch_up.md) · [All cinematic studies](../README.md)

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

