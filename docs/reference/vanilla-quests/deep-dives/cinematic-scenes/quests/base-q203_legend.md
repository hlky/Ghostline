# Path of Glory: scene presentation

Journal identity: `quests/main_quest/epilogues/q203_legend`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q203_legend.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene`

109 graph nodes, 124 edges; 10 event-bearing sections, 29 events; 13 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Iguana (actor 0, spawner); Johnny (actor 1, spawnDespawn); IguanaQ203 (actor 2, spawner); NibblesPuff (actor 3, community); IguanaPuff (actor 4, spawner); Player (actor 5, findInContext).

Entries: `mws_wat_02_in` → 1; `mws_wat_02_iguana_cat_in` → 560; `johnny_jamming` → 690; `mws_wat_02_q203_in` → 478.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 7 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 382 / 329 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/5` |
| `scnIKEvent` | 2 | 382 / 324 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/1` |
| `scnLookAtEvent` | 1 | 114 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/2` |
| `scnPlaySkAnimEvent` | 7 | 114 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scnUnmountEvent` | 1 | 382 / 328 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 1 | 382 / 326 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/3` |
| `scneventsSocket` | 12 | 114 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 3
- idle_animation: 2
- socket_signal: 2
- skeletal_animation, gaze, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `33bb5b12f99603e0e79c811b20b9fef3f6ff13a7caf8a7648e3ac3ff382a84ff`. Binary SHA-256: `1e4a5430ce064434338c0abd2ac2f2b6f742a21ad036cdc209a64074c1f2abf6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\mini_world_stories\watson\mws_wat_02\scenes\mws_wat_02.scene" --events
```

## `base\quest\main_quests\epilogue\q203\scenes\q203_02_shower.scene`

65 graph nodes, 63 edges; 12 event-bearing sections, 78 events; 22 screenplay lines, 13 screenplay options, 8 choice nodes.

Actors: sobchak (actor 0, spawnSet); rogue (actor 1, spawnSet); judy (actor 2, spawnSet); kerry (actor 3, spawnSet); assistant (actor 4, findInContext); tpp_male (actor 5, spawnDespawn); tpp_female (actor 6, spawnDespawn); V (actor 7, findInContext).

Entries: `in_shower` → 149; `Start 12` → 4388; `Start 13` → 4391; `q203_02_assistant_help_IN` → 330.

Exits: `out_shower` → 150; `q203_02_assistant_help_OUT` → 331.

End nodes: 150: `NonTerminating`; 331: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 350 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |
| `scnChangeIdleAnimEvent` | 3 | 352 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/2` |
| `scnDialogLineEvent` | 7 | 337 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 350 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/5` |
| `scnIKEvent` | 6 | 350 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scnPlaySkAnimEvent` | 11 | 350 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scnUnmountEvent` | 3 | 350 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/8` |
| `scneventsAttachPropToPerformer` | 2 | 461 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 461 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/3` |
| `scneventsCameraParamsEvent` | 6 | 350 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 3 | 350 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/7` |
| `scneventsSocket` | 12 | 350 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/6` |
| `scneventsVFXEvent` | 8 | 352 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, camera, vfx, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, camera, audio: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `679d8047e6cb6beea49a42d1b2d2f90ea46b27556b980ac4f145a9bfcf12bbce`. Binary SHA-256: `583478364a0b3c9b167d65dfcb99ff57dc83761f35bd8116583e666fd429ee3f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q203\scenes\q203_02_shower.scene" --events
```

## `base\quest\main_quests\epilogue\q203\scenes\q203_02b_kerry.scene`

208 graph nodes, 254 edges; 49 event-bearing sections, 490 events; 130 screenplay lines, 32 screenplay options, 17 choice nodes.

Actors: kerry (actor 0, spawnSet); q203_02b_female_tpp (actor 1, spawnDespawn); q203_02b_male_tpp (actor 2, spawnDespawn); delamain_av (actor 3, spawnSet); v (actor 4, findInContext).

Entries: `q203_02b_kerry_in` → 49; `test_preview_balcony` → 584; `preview_bed` → 596; `Start 7` → 2207; `kerry_proximity` → 685.

Exits: `q203_02b_kerry_in_out` → 14; `q203_02b_kerry_d_lands_out` → 570.

End nodes: 14: `NonTerminating`; 570: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 25 | 15 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnChangeIdleAnimEvent` | 20 | 15 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 115 | 10 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 40 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/9` |
| `scnIKEvent` | 10 | 40 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scnLookAtEvent` | 90 | 15 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 105 | 15 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnUnmountEvent` | 5 | 40 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/14` |
| `scneventsAttachPropToPerformer` | 5 | 15 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scneventsAttachPropToWorld` | 3 | 15 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/21` |
| `scneventsCameraParamsEvent` | 15 | 40 / 197 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 5 | 40 / 198 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/11` |
| `scneventsSocket` | 78 | 15 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 9 | 214 / 736 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- speech, skeletal_animation, gaze, socket_signal: 9
- speech, gaze: 3
- gaze: 3
- speech, skeletal_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- camera: 2
- speech: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx: 1
- skeletal_animation, audio, socket_signal: 1
- camera, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `214ed06d1a90e42841c90ae1aacef22d2d43e2597bf70ff1b0eb5987469fb6f1`. Binary SHA-256: `b716daa6a81396dafc4806387bd68ae7f9270d4419d4e0a41c3aa71fd680eccf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q203\scenes\q203_02b_kerry.scene" --events
```

## `base\quest\main_quests\epilogue\q203\scenes\q203_02c_judy.scene`

172 graph nodes, 223 edges; 54 event-bearing sections, 481 events; 117 screenplay lines, 32 screenplay options, 17 choice nodes.

Actors: judy (actor 0, spawnSet); v_female_tpp (actor 1, spawnDespawn); v_male_tpp (actor 2, spawnDespawn); q203_02c_delamain_av (actor 3, spawnSet); v (actor 4, findInContext).

Entries: `preview_bed` → 957; `q203_02c_judy_in` → 113; `in_goodbye` → 150; `preview_01` → 926.

Exits: `q203_02c_judy_out` → 9; `q203_02c_judy_d_lands_out` → 914.

End nodes: 9: `NonTerminating`; 914: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 21 | 15 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnChangeIdleAnimEvent` | 22 | 15 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scnDialogLineEvent` | 97 | 10 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 7 | 324 / 604 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/8` |
| `scnIKEvent` | 14 | 324 / 596 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/1` |
| `scnLookAtEvent` | 83 | 10 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 129 | 10 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnUnmountEvent` | 7 | 324 / 603 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/7` |
| `scneventsAttachPropToPerformer` | 1 | 698 / 997 | `/Data/RootChunk/sceneGraph/Data/graph/80/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 698 / 1000 | `/Data/RootChunk/sceneGraph/Data/graph/80/Data/events/5` |
| `scneventsCameraParamsEvent` | 20 | 15 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 7 | 324 / 601 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/6` |
| `scneventsSocket` | 63 | 10 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsVFXEvent` | 9 | 329 / 612 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- camera: 2
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, audio, vfx: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, camera, socket_signal: 1
- skeletal_animation, camera, audio, vfx, socket_signal: 1
- skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, camera, vfx, socket_signal: 1
- idle_animation: 1
- skeletal_animation, idle_animation, camera, audio: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `e6485c8f41717bbe2a3fbf31b864a9b929a3150b5cb3dfb2e8274888a21b8240`. Binary SHA-256: `da34446e5a2d12f2179327d3fd701e9db800047fe13f6f0e5972fac9120b4b77`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q203\scenes\q203_02c_judy.scene" --events
```

## `base\quest\main_quests\epilogue\q203\scenes\q203_02d_panam.scene`

155 graph nodes, 190 edges; 38 event-bearing sections, 394 events; 91 screenplay lines, 27 screenplay options, 13 choice nodes.

Actors: panam (actor 0, spawnSet); q203_02d_tpp_female (actor 1, spawnDespawn); q203_02d_tpp_male (actor 2, spawnDespawn); q203_02d_delamain_av (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `q203_02d_panam_in` → 5; `preview_kitchen` → 647; `preview_balcony` → 663; `Start 9` → 2179; `panam_farewell_interaction` → 614; `Start 8` → 938; `Start 10` → 2214.

Exits: `q203_02d_panam_out` → 6; `q203_02d_panam_d_lands` → 611.

End nodes: 6: `NonTerminating`; 611: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 20 | 9 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scnChangeIdleAnimEvent` | 25 | 9 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 64 | 9 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 5 | 9 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/16` |
| `scnIKEvent` | 10 | 9 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnLookAtEvent` | 89 | 9 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnPlaySkAnimEvent` | 99 | 9 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 5 | 9 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scneventsAttachPropToPerformer` | 1 | 504 / 890 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 504 / 892 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/4` |
| `scneventsCameraParamsEvent` | 15 | 132 / 485 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 5 | 9 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scneventsSocket` | 49 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 6 | 199 / 634 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, socket_signal: 3
- speech, gaze: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, camera, audio, socket_signal: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, camera, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, props_equipment, audio: 1
- camera, vfx, socket_signal: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, camera, audio: 1

Raw SHA-256: `66c956d4d3d24631a8188f1564d7f90fc5d1a2ba453a45a6ab8929670e350f1a`. Binary SHA-256: `3346e33fb5772c00a500a2b98d338400cfdad0137cd2850ea43c72a31dda08a0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q203\scenes\q203_02d_panam.scene" --events
```

## `base\quest\main_quests\epilogue\q203\scenes\q203_03_sobchak.scene`

211 graph nodes, 253 edges; 53 event-bearing sections, 433 events; 119 screenplay lines, 34 screenplay options, 17 choice nodes.

Actors: sobchak (actor 0, spawnSet); tpp_female (actor 1, spawnDespawn); tpp_male (actor 2, spawnDespawn); q203_03_delamain_av (actor 3, spawnSet); v (actor 4, findInContext).

Entries: `Start 9` → 4387; `q203_01a_shower_in` → 426; `sq021_okay_in` → 812; `preview_kitchen` → 857; `preview_balcony` → 859.

Exits: `q205_02_sobchak_out` → 8; `sq021_okay_out` → 813; `q203_03_sobchak_d_arrives_out` → 824.

End nodes: 8: `NonTerminating`; 813: `<omitted>`; 824: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 24 | 150 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnChangeIdleAnimEvent` | 16 | 87 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 89 | 87 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 352 / 578 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/9` |
| `scnIKEvent` | 10 | 352 / 574 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/5` |
| `scnLookAtEvent` | 57 | 87 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 98 | 87 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnUnmountEvent` | 5 | 352 / 584 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/14` |
| `scneventsAttachPropToPerformer` | 3 | 569 / 844 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/2` |
| `scneventsAttachPropToWorld` | 4 | 276 / 326 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/11` |
| `scneventsCameraParamsEvent` | 17 | 352 / 579 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 5 | 352 / 580 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/11` |
| `scneventsSocket` | 82 | 87 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/13` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 276 / 325 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/10` |
| `scneventsVFXEvent` | 16 | 150 / 212 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 2
- skeletal_animation, camera, audio, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- camera: 2
- speech, gaze: 2
- skeletal_animation, gaze, audio, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, camera, vfx, socket_signal: 1
- speech, skeletal_animation, camera, socket_signal: 1
- skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, audio, vfx: 1
- speech: 1
- skeletal_animation, audio, socket_signal: 1
- gaze: 1
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, camera: 1

Raw SHA-256: `93bb83bab4a4049577033ac7c2c0c39e0719adf5ea7b821b8ded87e173ef92f8`. Binary SHA-256: `a959f4ed3d30bcb43fced3ead9b98eba7defaca8bc678e8a223f238508eea12a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q203\scenes\q203_03_sobchak.scene" --events
```

## `base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene`

151 graph nodes, 191 edges; 49 event-bearing sections, 203 events; 174 screenplay lines, 20 screenplay options, 8 choice nodes.

Actors: delamain (actor 0, findInContext); emmerick (actor 1, spawnSet); delamain_sad (actor 2, findInContext); Delamain_av (actor 3, spawnSet); v (actor 4, findInContext).

Entries: `q203_04_delemain_in` → 1; `emmerick_holocall_prev` → 1027; `q203_04_delemain_lands_IN` → 580; `q203_04_goodbye_to_nc_in` → 81; `q203_04_delemain_leaves_IN` → 750; `av_preview` → 765; `q203_04_emmerick_calls_IN` → 464.

Exits: `q203_04_delemain_to_afterlife_out` → 2; `q203_04_delemain_lands_out` → 581; `q203_04_delemain_leaves_OUT` → 751; `q203_04_goodbye_to_nc_out` → 86; `q203_04_emmerick_calls_OUT` → 465.

End nodes: 2: `NonTerminating`; 86: `NonTerminating`; 465: `<omitted>`; 581: `NonTerminating`; 751: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 77 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnChangeIdleAnimEvent` | 6 | 582 / 443 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/1` |
| `scnDialogLineEvent` | 157 | 37 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 671 / 555 | `/Data/RootChunk/sceneGraph/Data/graph/95/Data/events/7` |
| `scnGameplayTransitionEvent` | 1 | 714 / 632 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/4` |
| `scnIKEvent` | 2 | 714 / 629 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/1` |
| `scnLookAtEvent` | 1 | 1031 / 743 | `/Data/RootChunk/sceneGraph/Data/graph/128/Data/events/1` |
| `scnPlaySkAnimEvent` | 7 | 582 / 439 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/0` |
| `scnUnmountEvent` | 1 | 714 / 636 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 2 | 671 / 540 | `/Data/RootChunk/sceneGraph/Data/graph/95/Data/events/0` |
| `scneventsSocket` | 4 | 671 / 549 | `/Data/RootChunk/sceneGraph/Data/graph/95/Data/events/3` |
| `scneventsVFXDurationEvent` | 2 | 582 / 445 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/3` |
| `scneventsVFXEvent` | 9 | 77 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 38
- speech, vfx: 3
- speech, audio, vfx: 1
- skeletal_animation, idle_animation, vfx: 1
- skeletal_animation, idle_animation, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, audio, vfx, gameplay_action: 1
- skeletal_animation, idle_animation, audio, vfx: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio: 1
- idle_animation, gaze: 1

Raw SHA-256: `fc464c600600e5b6d181f1cfe3337f33239bb288e16ff1a3e1b1b35b0d776753`. Binary SHA-256: `ea2039355763ca16073bcf52b88371f7b2cd08d7fd77708d866c5eba8b792afc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q203\scenes\q203_04_delamain.scene" --events
```

## `base\quest\main_quests\epilogue\q203\scenes\q203_05_afterlife.scene`

263 graph nodes, 333 edges; 86 event-bearing sections, 850 events; 183 screenplay lines, 29 screenplay options, 16 choice nodes.

Actors: emmerick (actor 0, spawnSet); mr_blue_eyes (actor 1, community); claire (actor 2, spawnSet); weyland (actor 3, spawnSet); rogue (actor 4, spawnSet); janitor (actor 5, community); drunk_at_bar (actor 6, community); man_in_booth_01 (actor 7, community); man_in_booth_02 (actor 8, community); nibbles (actor 9, spawnDespawn); v (actor 10, findInContext).

Entries: `q203_05_afterlife_booth_in` → 227; `Start 13` → 1299; `q203_05_weyland_IN` → 544; `Rogue_start` → 762; `q203_05_emmerick_greets_in` → 352; `q203_05_claire_drink_in` → 357; `Weyland_Rogue` → 851.

Exits: `q203_05_mr_blueeyes_leaving_out` → 246; `q203_05_weyland_OUT` → 545; `q203_05_claire_drink_out` → 359.

End nodes: 246: `<omitted>`; 359: `NonTerminating`; 545: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 19 | 232 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scnChangeIdleAnimEvent` | 17 | 400 / 366 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/6` |
| `scnDialogLineEvent` | 145 | 228 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayTransitionEvent` | 3 | 469 / 818 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/5` |
| `scnIKEvent` | 6 | 469 / 814 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/1` |
| `scnLookAtEvent` | 141 | 228 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 355 | 232 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnUnmountEvent` | 3 | 469 / 822 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/8` |
| `scneventsAttachPropToPerformer` | 21 | 232 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsAttachPropToWorld` | 20 | 232 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/14` |
| `scneventsCameraParamsEvent` | 1 | 555 / 928 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/9` |
| `scneventsEquipItemToPerformer` | 4 | 1027 / 2182 | `/Data/RootChunk/sceneGraph/Data/graph/149/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 3 | 469 / 820 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/7` |
| `scneventsSocket` | 95 | 232 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/18` |
| `scneventsUnequipItemFromPerformer` | 2 | 794 / 1556 | `/Data/RootChunk/sceneGraph/Data/graph/114/Data/events/49` |
| `scneventsVFXEvent` | 15 | 232 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 12
- speech, skeletal_animation, gaze, socket_signal: 8
- speech: 8
- speech, skeletal_animation, gaze: 5
- skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation: 4
- skeletal_animation, audio, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 4
- speech, gaze: 3
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `824e6b16c4a4c2c78c2ac4aa985add9a0a6a38ffea59f9a18c01cb3554901ffc`. Binary SHA-256: `a2cd31fed857345a43250750509947b544fae7d6241aca9e595ba11b663b82f4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q203\scenes\q203_05_afterlife.scene" --events
```

## `base\quest\main_quests\epilogue\q203\scenes\q203_06_cosmos.scene`

141 graph nodes, 146 edges; 13 event-bearing sections, 223 events; 18 screenplay lines, 7 screenplay options, 7 choice nodes.

Actors: mrx (actor 0, findInContext); q203_female_v_tpp (actor 1, spawnDespawn); q203_male_v_tpp (actor 2, spawnDespawn); v (actor 3, findInContext).

Entries: `Start 6` → 3086; `q203_06_cosmos_mr_blue_eyes_IN` → 55; `q203_06_helmet_IN` → 70; `q203_06_see_you_IN` → 78; `q203_06_final_cutscene_IN` → 83.

Exits: `q203_06_cosmos_mr_blue_eyes_OUT` → 56; `q203_06_helmet_OUT` → 71; `q203_06_final_cutscene_OUT` → 84; `clean_up` → 361.

End nodes: 56: `NonTerminating`; 71: `NonTerminating`; 84: `NonTerminating`; 361: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 57 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnChangeIdleAnimEvent` | 7 | 152 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/3` |
| `scnDialogLineEvent` | 15 | 57 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 1 | 146 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scnIKEvent` | 2 | 146 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnPlayRidAnimEvent` | 22 | 198 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/0` |
| `scnPlaySkAnimEvent` | 97 | 57 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 146 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/7` |
| `scneventsAttachPropToPerformer` | 2 | 156 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/2` |
| `scneventsCameraParamsEvent` | 1 | 152 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/1` |
| `scneventsPlayRidCameraAnimEvent` | 22 | 198 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 1 | 146 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/6` |
| `scneventsSocket` | 15 | 57 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXDurationEvent` | 12 | 198 / 245 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/28` |
| `scneventsVFXEvent` | 14 | 156 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- skeletal_animation, rid_actor, camera, rid_camera, audio, vfx, socket_signal: 2
- speech, skeletal_animation, audio, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio: 1
- idle_animation: 1

Raw SHA-256: `7caf4cbf42aa1a9fc344ca090801dbad8394185cf8b92cd4eb7ecddabeb48a4f`. Binary SHA-256: `b45555577d28050896249d3c1e9bc2c12a53617a53272e1a3a83600ed1326ab7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q203\scenes\q203_06_cosmos.scene" --events
```

