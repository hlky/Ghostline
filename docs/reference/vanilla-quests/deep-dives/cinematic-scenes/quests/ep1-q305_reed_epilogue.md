# Four Score and Seven: scene presentation

Journal identity: `ep1/quests/main_quest/q305_reed_epilogue`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q305_reed_epilogue.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\vendors\watson\kabuki\wat_kab_netrunner_01\wat_kab_netrunner_01.scene`

257 graph nodes, 318 edges; 50 event-bearing sections, 527 events; 120 screenplay lines, 36 screenplay options, 13 choice nodes.

Actors: wat_kab_netrunner_01 (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `wat_kab_netrunner_01_start` → 4; `wait_yoko_in` → 453; `Start 1` → 1324.

Exits: `wait_yoko_out` → 455; `time_change` → 475.

End nodes: 455: `NonTerminating`; 475: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 30 | 137 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/14` |
| `scnChangeIdleAnimEvent` | 14 | 125 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/1` |
| `scnDialogLineEvent` | 103 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 167 / 293 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/7` |
| `scnIKEvent` | 9 | 167 / 285 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scnLookAtAdvancedEvent` | 5 | 155 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/2` |
| `scnLookAtEvent` | 87 | 7 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnOverridePhantomParamsEvent` | 1 | 402 / 988 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/12` |
| `scnPlaySkAnimEvent` | 128 | 125 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/2` |
| `scnPoseCorrectionEvent` | 4 | 125 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/6` |
| `scnUnmountEvent` | 3 | 167 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/11` |
| `scneventsAttachPropToPerformer` | 7 | 167 / 307 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/15` |
| `scneventsAttachPropToWorld` | 7 | 167 / 309 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/17` |
| `scneventsEquipItemToPerformer` | 9 | 137 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/20` |
| `scneventsSetAnimFeatureEvent` | 3 | 167 / 294 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/8` |
| `scneventsSocket` | 105 | 125 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/8` |
| `scneventsUnequipItemFromPerformer` | 7 | 149 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/13` |
| `scneventsVFXEvent` | 2 | 1300 / 2177 | `/Data/RootChunk/sceneGraph/Data/graph/236/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, gaze: 5
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- skeletal_animation, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, audio, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, audio, socket_signal: 1
- socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 1

Raw SHA-256: `746ab3e3d81b9f2bdfe9a28eea401dabbfd4ceb580745a7b300704b452298d13`. Binary SHA-256: `3618c469468e73c67f6d1f9d8a4a85babda949fa1692a204dde7c732ee253104`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\vendors\watson\kabuki\wat_kab_netrunner_01\wat_kab_netrunner_01.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_01_holocalls_to_netrunner.scene`

183 graph nodes, 192 edges; 28 event-bearing sections, 79 events; 82 screenplay lines, 14 screenplay options, 6 choice nodes.

Actors: Nix (actor 0, spawnSet); 8ug8ear (actor 1, spawnSet); mrhands (actor 2, spawnSet); Chang_Hoon_Nam (actor 3, spawnSet); Carol (actor 4, spawnSet); Sandra_Dorsett (actor 5, spawnSet); kerry_holo (actor 6, spawnSet); river_holo (actor 7, spawnSet); V (actor 8, findInContext).

Entries: `nix_test` → 1633; `q305_01_Carol_return_call_in` → 856; `kerry_test` → 1653; `river_test` → 1654; `q305_01_Sandra_main_call_in` → 515; `q305_01_Carol_main_call_in` → 719; `q305_01_Chang_main_call_in` → 156; `q305_01_Sandra_return_call_in` → 553; `q305_01_Chang_return_call_in` → 371.

Exits: `q305_01_Sandra_finished_call_out` → 801; `q305_01_Carol_return_call_out` → 841; `q305_01_Chang_finished_call_out` → 1439; `q305_01_Sandra_main_call_out` → 517; `q305_01_Carol_main_call_out` → 721; `q305_01_Chang_main_call_out` → 158; `q305_01_Sandra_return_call_out` → 771; `q305_01_Chang_return_call_out` → 385.

End nodes: 158: `<omitted>`; 385: `<omitted>`; 517: `<omitted>`; 721: `<omitted>`; 771: `<omitted>`; 801: `<omitted>`; 841: `<omitted>`; 1439: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 79 | 757 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 28

Raw SHA-256: `23932ca0986ff87c23ab642c0c75d8115eabbac998e05572613db8d4e6e156c9`. Binary SHA-256: `b1ba1a7b960fee7520e1afd4243c8e4c203b2bee127fc350c08840663ff87ba9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_01_holocalls_to_netrunner.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_02b_nix.scene`

134 graph nodes, 177 edges; 27 event-bearing sections, 320 events; 54 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: Nix (actor 0, community); Johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `q305_02b_nix_meeting_in` → 1; `wait_nix_in` → 185.

Exits: `q305_02b_nix_meeting_terminating_out` → 271; `q305_02b_nix_meeting_out` → 2; `wait_nix_out` → 187; `time_change` → 226.

End nodes: 2: `NonTerminating`; 187: `NonTerminating`; 226: `NonTerminating`; 271: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 67 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/14` |
| `scnChangeIdleAnimEvent` | 8 | 58 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/7` |
| `scnDialogLineEvent` | 43 | 58 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnGameplayTransitionEvent` | 8 | 105 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/29` |
| `scnIKEvent` | 16 | 105 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/31` |
| `scnLookAtAdvancedEvent` | 8 | 59 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnLookAtEvent` | 39 | 58 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnPlaySkAnimEvent` | 85 | 58 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnUnmountEvent` | 8 | 105 / 358 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/36` |
| `scneventsAttachPropToPerformer` | 5 | 67 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/16` |
| `scneventsAttachPropToWorld` | 3 | 70 / 150 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |
| `scneventsEquipItemToPerformer` | 20 | 67 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 8 | 105 / 347 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/27` |
| `scneventsSocket` | 64 | 58 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- skeletal_animation, props_equipment, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1

Raw SHA-256: `eed487dca98774a4ce1057d0d0208cba5c044969b5e1fb38437feafecb58d917`. Binary SHA-256: `53df0a3f436021139a12bba905565ded8c0b136677b8903999567e134efdd5e1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_02b_nix.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_02d_chang.scene`

141 graph nodes, 181 edges; 32 event-bearing sections, 302 events; 89 screenplay lines, 13 screenplay options, 9 choice nodes.

Actors: chang (actor 0, community); Johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `q305_02d_chang_in` → 1; `Start 0` → 591; `wait_chang_in` → 322; `Start 1` → 538.

Exits: `q305_02d_chang_terminate_out` → 2; `End 0` → 593; `wait_chang_out` → 324; `time_change` → 348; `q305_02d_chang_out` → 270.

End nodes: 2: `<omitted>`; 270: `NonTerminating`; 324: `NonTerminating`; 348: `NonTerminating`; 593: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 14 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 51 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 6 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/22` |
| `scnIKEvent` | 6 | 6 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scnLookAtEvent` | 63 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 1 | 416 / 893 | `/Data/RootChunk/sceneGraph/Data/graph/80/Data/events/1` |
| `scnPlaySkAnimEvent` | 103 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 6 | 32 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/7` |
| `scnUnmountEvent` | 3 | 6 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/21` |
| `scneventsAttachPropToWorld` | 2 | 130 / 441 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/0` |
| `scneventsEquipItemToPerformer` | 4 | 130 / 460 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 3 | 6 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scneventsSocket` | 41 | 6 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsUnequipItemFromPerformer` | 2 | 130 / 462 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- skeletal_animation, socket_signal: 3
- speech: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, gaze: 2
- skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- gaze, socket_signal: 1
- gaze: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `e4473b2e906691bedbe0bc63d3a63314f46add8ce8062ba0a0abf535033da34f`. Binary SHA-256: `6cc9aeaaa224643dadb06f610884ac333fa7b7127754ea99b2015382ebe68ee8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_02d_chang.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_02e_sandra.scene`

143 graph nodes, 171 edges; 35 event-bearing sections, 387 events; 84 screenplay lines, 19 screenplay options, 10 choice nodes.

Actors: sandra (actor 0, community); Johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `q305_02e_sandra_in` → 1; `wait_sandra_in` → 357; `Start 2` → 616.

Exits: `q305_02e_sandra_out_non_terminate` → 2; `time_change` → 383; `q305_02e_sandra_out_terminate` → 443; `wait_sandra_out` → 359.

End nodes: 2: `NonTerminating`; 359: `NonTerminating`; 383: `NonTerminating`; 443: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 21 | 9 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnChangeIdleAnimEvent` | 11 | 9 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scnDialogLineEvent` | 68 | 9 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 8 | 37 / 185 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/32` |
| `scnIKEvent` | 16 | 37 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/19` |
| `scnLookAtAdvancedEvent` | 6 | 46 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnLookAtEvent` | 75 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnOverridePhantomParamsEvent` | 1 | 474 / 906 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/12` |
| `scnPlaySkAnimEvent` | 72 | 9 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 12 | 40 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/28` |
| `scnUnmountEvent` | 8 | 37 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/31` |
| `scneventsAttachPropToPerformer` | 5 | 37 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/24` |
| `scneventsAttachPropToWorld` | 12 | 37 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/26` |
| `scneventsCameraParamsEvent` | 3 | 91 / 377 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/5` |
| `scneventsEquipItemToPerformer` | 2 | 113 / 430 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 8 | 37 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/28` |
| `scneventsSocket` | 58 | 9 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 299 / 589 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- gaze: 3
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, camera, socket_signal, animation_state: 2
- props_equipment: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- speech, socket_signal: 1
- idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1
- speech: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `4f9ca52852c688cd1b0470fc7043e2c37edeec280e457c068bd7cf1444cbcc20`. Binary SHA-256: `2de39d29020c52e00d06af6bc35e02ba5ab0ab0189d933b8acc526149711e8d9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_02e_sandra.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_04_pre_ambush_meeting.scene`

964 graph nodes, 1207 edges; 210 event-bearing sections, 1642 events; 429 screenplay lines, 60 screenplay options, 24 choice nodes.

Actors: boz (actor 0, spawnDespawn); gunner (actor 1, community); reed (actor 2, spawnSet); johnny (actor 3, spawnDespawn); 6th_male4 (actor 4, community); 6th_male5 (actor 5, community); 6th_male6 (actor 6, community); 6th_male7 (actor 7, community); 6th_male8 (actor 8, community); 6th_male9 (actor 9, community); 6th_female4 (actor 10, community); captain (actor 11, community); friend1 (actor 12, community); friend2 (actor 13, community); friend3 (actor 14, community); chang_holo (actor 15, spawnSet); holo_van_1 (actor 16, community); holo_van_2 (actor 17, community); holo_van_3 (actor 18, community); V_tpp_fem (actor 19, spawnDespawn); V_tpp_male (actor 20, spawnDespawn); 6th_male10 (actor 21, community); 6th_male11 (actor 22, community); 6th_male12 (actor 23, community); 6th_male13 (actor 24, community); 6th_male14 (actor 25, community); 6th_male15 (actor 26, community); 6th_male16 (actor 27, community); mackinaw (actor 28, community); drone_veh (actor 29, community); drone_lookat (actor 30, community); green_holo_car1 (actor 31, community); green_holo_car2 (actor 32, community); green_holo_car3 (actor 33, community); green_holo_car4 (actor 34, community); drone (actor 35, community); V (actor 36, findInContext).

Entries: `q305_01_pre_ambush_meeting_in` → 1; `Start 12` → 5771; `Start 18` → 7666; `Start1` → 6756; `Start 13` → 5838; `Start 20` → 8728; `johnny_pre_ambush` → 1165; `Start 6` → 1341; `instant_preview` → 5159; `Start 21` → 8998; `Start 22` → 9002; `Start 25` → 9979; `Start 10` → 3431; `Start 16` → 6344; `Start 23` → 9314; `Start 24` → 9326; `Start 17` → 6625.

Exits: `q305_01_pre_ambush_meeting_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 2208 / 1760 | `/Data/RootChunk/sceneGraph/Data/graph/143/Data/events/11` |
| `scnChangeIdleAnimEvent` | 78 | 150 / 233 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnDialogLineEvent` | 230 | 20 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 27 | 137 / 218 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/19` |
| `scnIKEvent` | 54 | 137 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/12` |
| `scnLookAtAdvancedEvent` | 21 | 544 / 621 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/5` |
| `scnLookAtEvent` | 410 | 20 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 363 | 20 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 16 | 84 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scnUnmountEvent` | 27 | 137 / 217 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/18` |
| `scneventsAttachPropToNode` | 1 | 5818 / 3678 | `/Data/RootChunk/sceneGraph/Data/graph/364/Data/events/9` |
| `scneventsAttachPropToPerformer` | 8 | 273 / 401 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/0` |
| `scneventsAttachPropToWorld` | 2 | 280 / 438 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/12` |
| `scneventsEquipItemToPerformer` | 30 | 184 / 284 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 27 | 137 / 213 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/15` |
| `scneventsSocket` | 326 | 81 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/8` |
| `scneventsUnequipItemFromPerformer` | 2 | 5121 / 3064 | `/Data/RootChunk/sceneGraph/Data/graph/286/Data/events/6` |
| `scneventsVFXEvent` | 17 | 81 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 23
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 18
- speech, socket_signal: 16
- skeletal_animation, idle_animation: 16
- speech, skeletal_animation, gaze, socket_signal: 15
- speech: 15
- skeletal_animation, socket_signal: 13
- skeletal_animation: 8
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 7
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 5
- skeletal_animation, gaze, socket_signal: 5
- socket_signal: 5
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- skeletal_animation, gaze, props_equipment, socket_signal: 5
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, gaze: 4
- skeletal_animation, idle_animation, socket_signal: 4
- skeletal_animation, vfx, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, props_equipment, vfx, socket_signal: 2
- skeletal_animation, gaze: 2
- skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- gaze, props_equipment, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `85e0c6569f676d9cc1f903044fcbf6c2d8b76c2c8103e3cae11de619330d35ca`. Binary SHA-256: `44c9f2236b6375fd836cf46ad2c422239b80ce5f1d25cdcdcc4d814ed4e75d2d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_04_pre_ambush_meeting.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_04a_waiting_pre_ambush.scene`

17 graph nodes, 17 edges; 2 event-bearing sections, 13 events; 2 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Player (actor 0, findInContext).

Entries: `q305_04a_waiting_pre_ambush_in` → 1.

Exits: `q305_04a_waiting_pre_ambush_out` → 2; `q305_04a_waiting_pre_ambush_out_non_term` → 50.

End nodes: 2: `<omitted>`; 50: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 29 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnIKEvent` | 2 | 29 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 2 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 29 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 1 | 29 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scneventsSocket` | 4 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `0ea6246f438b0c9baa500bd2ddff8c945dbf52586cc8b54f53ff5022df631c58`. Binary SHA-256: `b1a5968e206039b6648478edf24197d38ace29043c3668bbcebf95242f8d1075`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_04a_waiting_pre_ambush.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_05_ambush_scenes.scene`

713 graph nodes, 861 edges; 57 event-bearing sections, 618 events; 88 screenplay lines, 11 screenplay options, 6 choice nodes.

Actors: reed_holo (actor 0, spawnSet); songbird (actor 1, findInContext); maxtac_01 (actor 2, community); maxtac_02 (actor 3, community); maxtac_03 (actor 4, community); maxtac_04 (actor 5, community); maxtac_05 (actor 6, community); maxtac_06 (actor 7, community); maxtac_07 (actor 8, community); maxtac_08 (actor 9, community); maxtac_09 (actor 10, community); maxtac_av_01 (actor 11, community); maxtac_av_02 (actor 12, community); maxtac_av_03 (actor 13, community); maxtac_av_04 (actor 14, community); miniboss_1 (actor 15, community); miniboss_2 (actor 16, community); reed_sniper (actor 17, spawnSet); songbird_prison (actor 18, spawnDespawn); reed_gp (actor 19, community); apc_fake_driver (actor 20, spawnDespawn); 6th_explosive_car_majster_woman (actor 21, community); 6th_explosive_car_majster_man_01 (actor 22, community); 6th_explosive_car_majster_man_02 (actor 23, community); 6th_street_demolition_man (actor 24, community); veh_maxtac_01 (actor 25, community); veh_maxtac_02 (actor 26, community); veh_maxtac_apc (actor 27, community); veh_maxtac_destro_1 (actor 28, community); veh_maxtac_destro_2 (actor 29, community); add_car002 (actor 30, spawner); boom_car1 (actor 31, community); veh_blockade (actor 32, community); V (actor 33, findInContext).

Entries: `Start 0` → 1; `Start 46` → 6536; `Start 21` → 2963; `q305_05_av_drop_start` → 815; `Start 40` → 5160; `Start 32` → 4457; `Start 41` → 5952; `Start 25` → 3825; `Start 43` → 6053; `check_truck_in` → 1013; `Start 27` → 3921; `Start 34` → 4644; `Start 35` → 4654; `Start 22` → 3252; `Start 44` → 6137; `q305_05_maxtac_from_apc` → 1832; `Start 23` → 3344; `Ambush_end_in` → 460; `Start 24` → 3365; `Q305_combat_midway_in` → 506; `Start 45` → 6298; `Q305_combat_reminder_1_in` → 1296; `q305_05_somi_drive_away_in` → 612; `q305_05_v_escape_in` → 638; `q305_05_quest_failed_in` → 654; `Start 31` → 4275.

Exits: `End 0` → 2; `Ambush_end_out` → 2209; `Ambush_hacks` → 812; `q305_05_av_drop_end` → 910; `av_01_out` → 914; `av_02_out` → 915; `av_03_out` → 917; `av_04_out` → 919; `check_truck_out` → 1014; `q305_05_maxtac_out_apc` → 1868; `Q305_combat_midway_out` → 507; `q305_05_v_escape_out` → 640; `q305_05_quest_failed_out` → 660.

End nodes: 2: `NonTerminating`; 507: `NonTerminating`; 640: `NonTerminating`; 660: `NonTerminating`; 812: `NonTerminating`; 910: `<omitted>`; 914: `NonTerminating`; 915: `NonTerminating`; 917: `NonTerminating`; 919: `NonTerminating`; 1014: `NonTerminating`; 1868: `<omitted>`; 2209: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 23 | 185 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |
| `scnChangeIdleAnimEvent` | 19 | 462 / 224 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/2` |
| `scnDialogLineEvent` | 48 | 177 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 462 / 237 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/11` |
| `scnGameplayTransitionEvent` | 23 | 462 / 287 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/56` |
| `scnIKEvent` | 46 | 462 / 283 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/52` |
| `scnLookAtEvent` | 28 | 1021 / 582 | `/Data/RootChunk/sceneGraph/Data/graph/95/Data/events/14` |
| `scnPlaySkAnimEvent` | 98 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 6046 / 3394 | `/Data/RootChunk/sceneGraph/Data/graph/491/Data/events/4` |
| `scnUnmountEvent` | 23 | 462 / 286 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/55` |
| `scneventsAttachPropToPerformer` | 1 | 1021 / 567 | `/Data/RootChunk/sceneGraph/Data/graph/95/Data/events/7` |
| `scneventsAttachPropToWorld` | 1 | 972 / 502 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/0` |
| `scneventsCameraParamsEvent` | 25 | 462 / 226 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/4` |
| `scneventsEquipItemToPerformer` | 7 | 3518 / 1923 | `/Data/RootChunk/sceneGraph/Data/graph/278/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 23 | 462 / 280 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/50` |
| `scneventsSocket` | 161 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 6071 / 3442 | `/Data/RootChunk/sceneGraph/Data/graph/499/Data/events/4` |
| `scneventsVFXEvent` | 87 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- skeletal_animation, camera, vfx, socket_signal: 9
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 8
- speech, audio, socket_signal: 4
- skeletal_animation, vfx, socket_signal: 3
- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- socket_signal: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, vfx, socket_signal: 1
- speech, audio: 1
- speech, skeletal_animation, idle_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, vfx, socket_signal: 1
- props_equipment, socket_signal, animation_state: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1

Raw SHA-256: `d51172abdf6315c86b2442639e1975419832c449f5b78bbd5804258706c368b9`. Binary SHA-256: `0293f55018c27805cc1f2971d394617950541e7229eadd3e8afa12870d21456f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_05_ambush_scenes.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_05a_maxtac_commands.scene`

229 graph nodes, 278 edges; 44 event-bearing sections, 48 events; 54 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: maxtac (actor 0, community); droid_maxtac (actor 1, community); maxtac_netrunner (actor 2, community); reed_holo (actor 3, spawnSet); droid_maxtac_backup (actor 4, community); Player (actor 5, findInContext).

Entries: `q305_05a_droid_commands_first_in` → 1; `q305_05a_maxtac_killed_in` → 244; `q305_05_coop_lines1_in` → 950; `q305_05_out_of_range_in` → 958; `q305_05_plan_reminder_in` → 962; `q305_05_fight_reminder1_in` → 968; `q305_05a_additional_comments1_in` → 280; `q305_05a_maxtac_commands_mines2_in` → 1688; `q305_05a_maxtac_commands_sniper2_in` → 1696; `q305_05a_vulgar_comments1_in` → 300; `q305_05a_additional_comments2_in` → 1703; `q305_05a_additional_comments3_in` → 1709; `q305_05a_maxtac_hit_reaction2_in` → 1717; `q305_05a_maxtac_taunt2_in` → 1726; `q305_05a_maxtac_taunt3_in` → 1731; `q305_05a_vulgar_comments2_in` → 1740; `q305_05_coop_lines2_in` → 1752; `q305_05_targeting02_in` → 1761; `q305_05_maxtac_shot2_in` → 1771; `q305_05a_maxtac_commands_mines1_in` → 147; `q305_05_maxtac_shot3_in` → 1781; `q305_05_maxtac_shot4_in` → 1787; `q305_05a_maxtac_commands_sniper1_in` → 160; `q305_05_trashtalk2_in` → 1801; `q305_05_reed_kill_comment2_in` → 1811; `q305_05_targeting01_in` → 880; `q305_05_fight_reminder2_in` → 1820; `q305_05_maxtac_shot1_in` → 892; `q305_05a_maxtac_taunt1_in` → 193; `q305_05_V_killing_comment2_in` → 1828; `q305_05_comment_hotel_in` → 904; `q305_05_trashtalk1_in` → 910; `q305_05_V_killing_comment1_in` → 920; `q305_05a_maxtac_distance_in` → 225; `q305_05a_maxtac_hit_reaction1_in` → 230; `q305_05_reed_kill_comment1_in` → 930.

Exits: `q305_05_reed_kill_comment_out` → 932; `q305_05a_droid_commands_first_out` → 2; `q305_05a_maxtac_killed_out` → 245; `q305_05_coop_lines_out` → 952; `q305_05_out_of_range_out` → 960; `q305_05_plan_reminder_out` → 964; `End1` → 1676; `q305_05_fight_reminder_out` → 978; `q305_05a_additional_comments_out` → 281; `q305_05a_vulgar_comments_out` → 301; `q305_05a_maxtac_commands_mines_out` → 154; `q305_05a_maxtac_commands_sniper_out` → 165; `q305_05_targeting_out` → 882; `q305_05a_maxtac_taunt_out` → 194; `q305_05_maxtac_shot_out` → 894; `q305_05_comment_hotel_out` → 908; `q305_05_trashtalk_out` → 912; `q305_05_V_killing_comment_out` → 922; `q305_05a_maxtac_distance_out` → 226; `q305_05a_maxtac_hit_reaction_out` → 231.

End nodes: 2: `NonTerminating`; 154: `NonTerminating`; 165: `NonTerminating`; 194: `NonTerminating`; 226: `NonTerminating`; 231: `NonTerminating`; 245: `NonTerminating`; 281: `NonTerminating`; 301: `NonTerminating`; 882: `NonTerminating`; 894: `NonTerminating`; 908: `NonTerminating`; 912: `NonTerminating`; 922: `NonTerminating`; 932: `NonTerminating`; 952: `NonTerminating`; 960: `NonTerminating`; 964: `NonTerminating`; 978: `NonTerminating`; 1676: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 48 | 10 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 44

Raw SHA-256: `5a3f669998c6f1a172468df69265c78707d4e3a3353852c14d6e0debfe23ea40`. Binary SHA-256: `18618d471f51676564d563e82d5560dda644425923795739e2cae696fc54009b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_05a_maxtac_commands.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_06_chase_scenes.scene`

395 graph nodes, 535 edges; 52 event-bearing sections, 231 events; 121 screenplay lines, 13 screenplay options, 10 choice nodes.

Actors: reed_holo (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); argue_01_ma (actor 2, community); argue_02_wa (actor 3, community); comment_01_ma (actor 4, community); comment_02_ma (actor 5, community); comment_03_ma (actor 6, community); comment_04_wa (actor 7, community); argue_03_ma (actor 8, community); argue_04_ma (actor 9, community); comment_hole_01 (actor 10, community); comment_hole_02 (actor 11, community); dead_max_tac (actor 12, community); scene1_corpo1 (actor 13, community); scene1_looker_2 (actor 14, community); V (actor 15, findInContext).

Entries: `Start 12` → 2636; `Start 5` → 961; `Reed_holo_start_in` → 120; `headlamp_retrofix_in` → 2756; `car_delivery_in` → 1515; `q305_06_chase_comments_in` → 1092; `q305_chase_reed_distance_comment_in` → 731; `headlamp_in` → 2479; `Start 9` → 1652.

Exits: `q305_Johny_about_leap_of_faith_out` → 10; `q305_chase_quest_fail_out` → 874; `headlamp_retrofix` → 2751; `q305_chase_reed_distance_comment_out` → 733; `headlamp_unequip` → 2518; `headlamp_end` → 2564.

End nodes: 10: `NonTerminating`; 733: `NonTerminating`; 874: `<omitted>`; 2518: `NonTerminating`; 2564: `NonTerminating`; 2751: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 53 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 78 | 53 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnGameplayTransitionEvent` | 1 | 1114 / 717 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/35` |
| `scnIKEvent` | 2 | 1114 / 701 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/25` |
| `scnLookAtEvent` | 28 | 53 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 3 | 55 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/29` |
| `scnPlaySkAnimEvent` | 52 | 53 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnUnmountEvent` | 1 | 1114 / 716 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/34` |
| `scneventsAttachPropToNode` | 1 | 2480 / 1774 | `/Data/RootChunk/sceneGraph/Data/graph/264/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 2494 / 1793 | `/Data/RootChunk/sceneGraph/Data/graph/268/Data/events/0` |
| `scneventsEquipItemToPerformer` | 2 | 2734 / 2114 | `/Data/RootChunk/sceneGraph/Data/graph/322/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 1 | 1114 / 712 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/31` |
| `scneventsSocket` | 47 | 53 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsUnequipItemFromPerformer` | 1 | 2734 / 2116 | `/Data/RootChunk/sceneGraph/Data/graph/322/Data/events/5` |
| `scneventsVFXEvent` | 6 | 174 / 237 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 34
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, socket_signal: 2
- skeletal_animation, gaze: 2
- props_equipment: 2
- skeletal_animation, vfx, socket_signal: 1
- gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1
- vfx, socket_signal: 1
- speech, vfx: 1
- skeletal_animation, props_equipment, socket_signal: 1
- gaze: 1

Raw SHA-256: `e30b7da07268f053054ca66d4375e97866a7433c6da063898aba93460fac1286`. Binary SHA-256: `4e2080b37718e619606ba71fa5cfbb359e1044cea6deb2554eed42fe5f368121`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_06_chase_scenes.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_06b_bunker_intro.scene`

720 graph nodes, 941 edges; 98 event-bearing sections, 750 events; 179 screenplay lines, 20 screenplay options, 8 choice nodes.

Actors: Reed_holo (actor 0, spawnSet); Songbird_holo (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); Security (actor 3, findInContext); songbird_holo_test (actor 4, spawnDespawn); Player (actor 5, findInContext).

Entries: `Start 9` → 3480; `Start 0` → 1; `Debug_before_elevator` → 73; `Start 4` → 2942; `johnny_unplugged` → 1705; `Start 3` → 1721; `q305_project_cynosure_johnny_in` → 350; `Start 5` → 3163; `elevator` → 1100; `Start 6` → 3293; `Start 8` → 3433.

Exits: `q305_08_elevator_scene_out` → 342; `q305_08_elevator_set_up_jumpscare` → 3256; `q305_08_elevator_scene_faster_out` → 667.

End nodes: 342: `<omitted>`; 667: `NonTerminating`; 3256: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 183 / 360 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/9` |
| `scnChangeIdleAnimEvent` | 44 | 105 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/2` |
| `scnDialogLineEvent` | 121 | 103 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 133 / 214 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/39` |
| `scnIKEvent` | 12 | 105 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/5` |
| `scnLookAtAdvancedEvent` | 57 | 161 / 322 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/63` |
| `scnLookAtEvent` | 100 | 105 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/8` |
| `scnOverridePhantomParamsEvent` | 9 | 133 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/16` |
| `scnPlaySkAnimEvent` | 136 | 105 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scnPoseCorrectionEvent` | 7 | 105 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/7` |
| `scnUnmountEvent` | 5 | 133 / 212 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/37` |
| `scneventsAttachPropToPerformer` | 3 | 3138 / 4257 | `/Data/RootChunk/sceneGraph/Data/graph/503/Data/events/5` |
| `scneventsAttachPropToWorld` | 3 | 2997 / 4085 | `/Data/RootChunk/sceneGraph/Data/graph/484/Data/events/17` |
| `scneventsCameraParamsEvent` | 35 | 161 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/6` |
| `scneventsCameraPlacementEvent` | 2 | 2997 / 4066 | `/Data/RootChunk/sceneGraph/Data/graph/484/Data/events/5` |
| `scneventsEquipItemToPerformer` | 14 | 161 / 229 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 5 | 133 / 209 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/35` |
| `scneventsSocket` | 143 | 99 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 4 | 370 / 749 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1280 / 1667 | `/Data/RootChunk/sceneGraph/Data/graph/178/Data/events/1` |
| `scneventsVFXEvent` | 39 | 133 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 31
- skeletal_animation: 9
- speech, socket_signal: 8
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, skeletal_animation, gaze, socket_signal: 5
- skeletal_animation, gaze: 4
- skeletal_animation, gaze, props_equipment, socket_signal: 3
- skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal: 2
- gaze: 2
- socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, camera: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal: 1
- vfx: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- vfx, socket_signal: 1
- gaze, socket_signal: 1
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `22c57985a091dafec53d8c705aa0b53b0c9d61c22bbcc28a2fb69d4ae5f428b9`. Binary SHA-256: `f2844c26d11f1089aaf13a7f017a3a234361fd0ab71c6e3517c73960135e028e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_06b_bunker_intro.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_07_brain_hack.scene`

408 graph nodes, 545 edges; 91 event-bearing sections, 1199 events; 248 screenplay lines, 24 screenplay options, 10 choice nodes.

Actors: Songbird_present (actor 0, spawnSet); Somi_past_birthday (actor 1, spawnDespawn); friend1 (actor 2, community); friend2 (actor 3, community); friend3 (actor 4, community); Boyfriend (actor 5, community); Reed (actor 6, spawnDespawn); neighbour (actor 7, spawnDespawn); somi_past_angry (actor 8, spawnDespawn); somi_past_gramophone (actor 9, spawnDespawn); somi_past_party (actor 10, spawnDespawn); somi_past_argument (actor 11, spawnDespawn); somi_past_reed (actor 12, spawnDespawn); Player (actor 13, findInContext).

Entries: `Start 0` → 1; `Start 21` → 5251; `Start 7` → 4218; `Start2` → 1640; `Start 4` → 3850; `Start 5` → 3852; `Start 6` → 3858; `Start 9` → 4388; `Start 10` → 4397; `Start 18` → 4934; `Start 19` → 4946; `Start 14` → 4435; `test` → 420; `Start 3` → 3580; `Start 2` → 3073.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 143 | 1384 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/15` |
| `scnChangeIdleAnimEvent` | 109 | 1384 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnDialogLineEvent` | 123 | 1384 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/29` |
| `scnLookAtAdvancedEvent` | 46 | 1384 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/30` |
| `scnLookAtEvent` | 230 | 1384 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |
| `scnPlaySkAnimEvent` | 262 | 1384 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsAttachPropToNode` | 1 | 3471 / 2220 | `/Data/RootChunk/sceneGraph/Data/graph/151/Data/events/12` |
| `scneventsAttachPropToPerformer` | 9 | 1384 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |
| `scneventsAttachPropToWorld` | 14 | 1384 / 156 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/111` |
| `scneventsCameraParamsEvent` | 17 | 1520 / 527 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/1` |
| `scneventsCameraPlacementEvent` | 1 | 3453 / 2192 | `/Data/RootChunk/sceneGraph/Data/graph/149/Data/events/1` |
| `scneventsEquipItemToPerformer` | 1 | 1428 / 236 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/25` |
| `scneventsSocket` | 148 | 1384 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/26` |
| `scneventsVFXEvent` | 95 | 1384 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- vfx: 26
- skeletal_animation, gaze: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 9
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 4
- gaze: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, socket_signal: 3
- speech: 3
- audio: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 2
- speech, idle_animation: 2
- audio, vfx: 2
- skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal: 1
- camera, vfx: 1
- camera: 1
- idle_animation: 1
- socket_signal: 1

Raw SHA-256: `195b39bcc48f0cc2a723bcef71194e8d78fa00b9f9ffaa386e0e38504ac258d1`. Binary SHA-256: `b066cc158cea6e4679d51e390db93e6806b264e31c9eb717d48b6eec26ccf0b8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_07_brain_hack.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08_outer_bunker_scenes.scene`

756 graph nodes, 921 edges; 36 event-bearing sections, 175 events; 45 screenplay lines, 19 screenplay options, 18 choice nodes.

Actors: johnny (actor 0, spawnDespawn); songbird_holo (actor 1, findInContext); security_ghost_01 (actor 2, community); command_ghost_01 (actor 3, community); netwatch_ghost_01 (actor 4, community); Kurtz (actor 5, spawnSet); Songbird (actor 6, spawnSet); myers (actor 7, spawnSet); ripperdoc (actor 8, community); Reed_Holo (actor 9, spawnSet); fake_robot (actor 10, community); Fake_songbird (actor 11, spawnSet); Security (actor 12, findInContext); cerberus (actor 13, community); V (actor 14, findInContext).

Entries: `Airlock Jumpscare` → 5766; `q305_airlock_doors_in` → 2490; `q305_08_robot_hits_door_in` → 31; `q305_08_see_robot_in` → 36; `q305_08_printing_room_in` → 1724; `q305_08_gate_shuts_down_in` → 161; `Start 71` → 5912; `Start 72` → 5917; `Start 73` → 5922; `Debug_prop_activation` → 7571; `Start 79` → 7740; `debug_gate_preview` → 3669; `q305_open_the_gate` → 2113; `q305_08_jumpscare_with_cargo` → 6231; `Start 64` → 5486; `Start 65` → 5552; `q305_08_engineering_jumpscare_in` → 1462; `q305_08_video_commented_in` → 1463; `Start 67` → 5724.

Exits: `q305_airlock_doors_out` → 2491; `q305_08_printing_room_out` → 1725; `q305_08_gate_shuts_down_out` → 162; `Autosaving_out_02` → 5207; `autosaving_out_03` → 5215; `End 53` → 6241; `q305_airlock_doors_terminating_out` → 7947; `q305_08_video_commented_out` → 1467; `dataterm_bravo_ou` → 4795.

End nodes: 162: `NonTerminating`; 1467: `<omitted>`; 1725: `<omitted>`; 2491: `NonTerminating`; 4795: `NonTerminating`; 5207: `NonTerminating`; 5215: `NonTerminating`; 6241: `NonTerminating`; 7947: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 13 | 1872 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/4` |
| `scnChangeIdleAnimEvent` | 22 | 1872 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/3` |
| `scnDialogLineEvent` | 24 | 1129 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 3400 / 605 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/8` |
| `scnIKEvent` | 4 | 3400 / 595 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/1` |
| `scnPlaySkAnimEvent` | 27 | 1872 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/0` |
| `scnUnmountEvent` | 2 | 3400 / 610 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/12` |
| `scneventsCameraParamsEvent` | 2 | 2554 / 208 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 2 | 3400 / 606 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/9` |
| `scneventsSocket` | 24 | 1872 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/10` |
| `scneventsVFXDurationEvent` | 1 | 1872 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/5` |
| `scneventsVFXEvent` | 52 | 1872 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- skeletal_animation, idle_animation: 6
- skeletal_animation, idle_animation, socket_signal: 4
- skeletal_animation: 2
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, socket_signal: 1
- camera, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx: 1

Raw SHA-256: `5fdc129b5c00d312824482381abb32fdb886bd119ce7bf85abcc013eb97056b7`. Binary SHA-256: `491fb0cb352d2e78008a10aafcb7267dcb874a8e728038f615229d31d451b9ca`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08_outer_bunker_scenes.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08b_bunker_holocalls.scene`

212 graph nodes, 253 edges; 78 event-bearing sections, 91 events; 121 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Songbird_holo (actor 0, spawnSet); Security (actor 1, spawnSet); Blackwall_AI (actor 2, spawnSet); Cerberus (actor 3, community); Cerberus_inner_bunker (actor 4, community); V (actor 5, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 3.

End nodes: 3: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 91 | 32 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 78

Raw SHA-256: `a6264adce0048f9c7d9110562387b0aa21ce6a00d409204e55f6cd0dc9de2409`. Binary SHA-256: `5cc3a388c2086ddebd6a6bf5309ba8842940fc8278f8ce94ae9f1dd7ae003563`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08b_bunker_holocalls.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08c_outer_bunker_hallucination_kurt.scene`

92 graph nodes, 98 edges; 12 event-bearing sections, 116 events; 23 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Kurt (actor 0, community); Songbird (actor 1, community); Songbird_holo (actor 2, spawnSet); Kurt_soldier_01 (actor 3, community); Kurt_soldier_02 (actor 4, community); cerberus_foreshadow (actor 5, community); Player (actor 6, findInContext).

Entries: `Start 0` → 1; `Start 2` → 724; `Start 3` → 760; `Start 4` → 762; `Cerb_foreshadow` → 1283; `Start 5` → 777; `Start 6` → 789.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 945 / 435 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/1` |
| `scnChangeIdleAnimEvent` | 4 | 32 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnDialogLineEvent` | 9 | 32 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scnGameplayTransitionEvent` | 2 | 32 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/25` |
| `scnIKEvent` | 4 | 32 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/17` |
| `scnLookAtEvent` | 21 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 32 | 32 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnUnmountEvent` | 2 | 32 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/26` |
| `scneventsSetAnimFeatureEvent` | 2 | 32 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/22` |
| `scneventsSocket` | 28 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXDurationEvent` | 4 | 945 / 436 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/2` |
| `scneventsVFXEvent` | 6 | 652 / 248 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 4
- vfx: 3
- gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- audio, vfx, socket_signal: 1

Raw SHA-256: `ae554e794a5f6d739d0ae41946a541d5540d3816f16f8036988d4841215181f1`. Binary SHA-256: `e5d19071d26a9ec7faa14b405f71a64639e7f425e147bcb06ffa1b71ccfdc2cc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08c_outer_bunker_hallucination_kurt.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08d_outer_bunker_hallucination_upgrade.scene`

97 graph nodes, 96 edges; 10 event-bearing sections, 131 events; 59 screenplay lines, 5 screenplay options, 0 choice nodes.

Actors: Myers (actor 0, spawnSet); Songbird (actor 1, community); Songbird_holo (actor 2, spawnSet); Technician (actor 3, community); Nurse1 (actor 4, community); Nurse2 (actor 5, community); corridor_personel1 (actor 6, spawnDespawn); corridor_personel2 (actor 7, spawnDespawn); Player (actor 8, findInContext).

Entries: `Start 0` → 1; `Start 1` → 223; `Start 12` → 903; `Start 4` → 685; `Start 5` → 691; `Start 6` → 697; `Start 7` → 699; `Start 8` → 721; `preview` → 284; `Start 13` → 958; `Start 2` → 526; `Start 15` → 1466; `Start 11` → 847; `Start 14` → 1104.

Exits: `End 0` → 2; `End 1` → 262.

End nodes: 2: `<omitted>`; 262: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 13 | 99 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnDialogLineEvent` | 11 | 99 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/30` |
| `scnLookAtEvent` | 52 | 99 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/6` |
| `scnPlaySkAnimEvent` | 23 | 51 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scneventsAttachPropToPerformer` | 3 | 51 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scneventsCameraParamsEvent` | 1 | 1329 / 468 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/0` |
| `scneventsEquipItemToPerformer` | 3 | 76 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scneventsSocket` | 11 | 51 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scneventsVFXEvent` | 14 | 51 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 3
- skeletal_animation, props_equipment, vfx, socket_signal: 1
- props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, vfx: 1
- speech: 1
- camera: 1

Raw SHA-256: `c17b34d6d8b0c963328946884d172bfbd38acc8cffa467b66849604735d9b9fd`. Binary SHA-256: `60c41814feefb0ec4016da939db3b7e84dca68e772f6021ed21ecc0216569c88`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08d_outer_bunker_hallucination_upgrade.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08e_outer_bunker_cerberus_voice.scene`

125 graph nodes, 212 edges; 26 event-bearing sections, 26 events; 26 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Songbird__BW (actor 0, spawnSet); Songbird (actor 1, spawnSet).

Entries: `Start 0` → 1; `chase_debug_in` → 371.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 26 | 35 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 26

Raw SHA-256: `8f4ffa283f95ec89445e13006b289eab62e10195ca8f390a32d71e0beb6cb414`. Binary SHA-256: `c6f2b714b5891743e3cc990b98525cce89206a55bd64fbf4900675c03af25ebe`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08e_outer_bunker_cerberus_voice.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08f_outer_bunker_minor_hallucinations.scene`

82 graph nodes, 94 edges; 8 event-bearing sections, 42 events; 15 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: songbird_smoke (actor 0, community); songbird_netrunner (actor 1, community); songird_gate (actor 2, community); songbird_wheelchair (actor 3, community); Player (actor 4, findInContext).

Entries: `Start 3` → 130; `Start 6` → 369; `Start 4` → 154; `Start 7` → 979; `Start 2` → 49; `in_smoking` → 82; `behind_the_gratings` → 106.

Exits: `End 6` → 894.

End nodes: 894: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 380 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/5` |
| `scnChangeIdleAnimEvent` | 3 | 44 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 67 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnIKEvent` | 2 | 67 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnLookAtEvent` | 3 | 44 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 6 | 67 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnUnmountEvent` | 1 | 67 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scneventsEquipItemToPerformer` | 1 | 170 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 1 | 67 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scneventsSocket` | 16 | 44 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 1 | 803 / 319 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/2` |
| `scneventsVFXEvent` | 6 | 67 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- socket_signal: 2
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `d7b349ffdc0c59ae3051c19d41af00549769f3d2e76e8676413adcbbc0bc3035`. Binary SHA-256: `07e6f3bdb80d45880e04a2eb097e8440588fd6ab674012e0d19886f721850fbf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08f_outer_bunker_minor_hallucinations.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08g_outer_bunker_cerberus_intro.scene`

462 graph nodes, 465 edges; 12 event-bearing sections, 138 events; 21 screenplay lines, 4 screenplay options, 4 choice nodes.

Actors: Cerberus (actor 0, community); Fake_robot (actor 1, community); Songbird (actor 2, findInContext); Blackwall_AI (actor 3, findInContext); Player (actor 4, findInContext).

Entries: `Start 0` → 1; `debug_crawl_under_server_in` → 14; `debug_crawl_back_in` → 39; `Start 7` → 2302; `Start 3` → 1810; `test_killroom` → 1811; `Start 6` → 1858; `Start 1` → 406.

Exits: `q305_robot_introduction_out` → 184.

End nodes: 184: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 8 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnChangeIdleAnimEvent` | 10 | 8 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 10 | 257 / 232 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/37` |
| `scnPlaySkAnimEvent` | 21 | 8 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsCameraParamsEvent` | 12 | 257 / 197 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/4` |
| `scneventsSocket` | 58 | 8 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 17 | 37 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation: 4
- speech, skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 2
- speech: 2
- skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `fea184a2f8c7a33f105cf6369d7cf13aec538e3cc4bf22746d228b9c143b3fa4`. Binary SHA-256: `19917918f66bfc33025eae7651fd94cb46d7379581cf676eb60627648749e569`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08g_outer_bunker_cerberus_intro.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_08h_outer_bunker_killroom.scene`

258 graph nodes, 448 edges; 61 event-bearing sections, 169 events; 82 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: cerberus (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 1` → 313; `Start 0` → 1; `Start 11` → 50; `debug` → 153; `Waiti_for_grab_in` → 816; `instant_killroom` → 1511.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnPlaySkAnimEvent` | 109 | 170 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scneventsCameraParamsEvent` | 2 | 231 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/0` |
| `scneventsSocket` | 58 | 170 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 52
- skeletal_animation: 7
- camera, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `8638356044c06f7e36eccee3cefd5f6f6bb163bcc97cdb60e2547167a2a56f73`. Binary SHA-256: `ad8a8eb536c7cc2b2ef28ca0aa6a0bacd9b90f297dfa7739a4212b48d2e983cd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_08h_outer_bunker_killroom.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09_inner_bunker_scenes.scene`

642 graph nodes, 762 edges; 29 event-bearing sections, 60 events; 56 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: songbird (actor 0, findInContext); Robot (actor 1, community); security (actor 2, findInContext); SongbirdBW (actor 3, findInContext); Cerberus_hunting (actor 4, community); V (actor 5, findInContext); Player (actor 6, findInContext).

Entries: `q305_09_enter_command_chamber_in` → 13; `q305_09_system_reset_in` → 52; `q305_10_kill_robot` → 2087; `Q305_09_IB_airlock_wait_in` → 10998; `Q305_09_IB_airlock_adjusting_pressure_in` → 10999; `Q305_09_IB_airlock_opened_in` → 11001; `Q305_09_IB_airlock_close_in` → 11003; `Q305_09_IB_command_room_computer_in` → 281; `q305_09_trolley_inner_bunker` → 9139; `trolley_devil_from_the_box` → 9154; `q305_09_subsystems_in` → 1150; `Start 18` → 8605; `trolley_compression` → 9296.

Exits: `autosaving_out` → 8131; `q305_09_enter_command_chamber_out` → 16; `End 15` → 8145; `q305_09_interupt_coolant_out` → 22; `End 13` → 2092; `Q305_09_IB_airlock_adjusting_pressure_out` → 11009; `Q305_09_IB_airlock_wait_out` → 11011; `Q305_09_IB_airlock_opened_out` → 11014; `Q305_09_IB_airlock_close_out` → 11016; `Q305_09_IB_command_room_computer_out` → 282; `Terminating_Scene_out` → 11301; `q305_09_subsystems_out` → 1205.

End nodes: 16: `NonTerminating`; 22: `NonTerminating`; 282: `NonTerminating`; 1205: `NonTerminating`; 2092: `<omitted>`; 8131: `NonTerminating`; 8145: `NonTerminating`; 11009: `NonTerminating`; 11011: `NonTerminating`; 11014: `NonTerminating`; 11016: `NonTerminating`; 11301: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 9140 / 1810 | `/Data/RootChunk/sceneGraph/Data/graph/283/Data/events/1` |
| `scnChangeIdleAnimEvent` | 6 | 9140 / 1811 | `/Data/RootChunk/sceneGraph/Data/graph/283/Data/events/2` |
| `scnDialogLineEvent` | 26 | 610 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 7 | 3557 / 568 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/5` |
| `scneventsSocket` | 6 | 3557 / 565 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/2` |
| `scneventsVFXEvent` | 13 | 3557 / 563 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 22
- skeletal_animation, idle_animation: 3
- skeletal_animation, vfx, socket_signal: 1
- speech, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio: 1
- skeletal_animation, idle_animation, audio, vfx: 1

Raw SHA-256: `a201e320dd83a3bb657af3e450365f1e57ae5442ca96482589d3bbed83f2653f`. Binary SHA-256: `bb83f7c46664921d91ad212251ab81fa43fb945433fa07b5952c49105b0fdb95`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09_inner_bunker_scenes.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09a_inner_bunker_hallucination_oath.scene`

142 graph nodes, 178 edges; 13 event-bearing sections, 213 events; 39 screenplay lines, 1 screenplay options, 0 choice nodes.

Actors: Myers (actor 0, spawnDespawn); Songbird (actor 1, spawnDespawn); Songbird_holo (actor 2, spawnSet); Reed (actor 3, community); Songbird2 (actor 4, spawnDespawn); Player (actor 5, findInContext).

Entries: `Start 0` → 1; `Start 7` → 1678; `Start 3` → 862; `preview` → 1786; `Start 9` → 2222; `Start 5` → 974; `Start 6` → 1629; `Start1` → 2473.

Exits: `End 0` → 2; `End 1` → 1619.

End nodes: 2: `<omitted>`; 1619: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 795 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/12` |
| `scnChangeIdleAnimEvent` | 22 | 795 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scnDialogLineEvent` | 19 | 795 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/8` |
| `scnLookAtAdvancedEvent` | 11 | 795 / 185 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/63` |
| `scnLookAtEvent` | 46 | 795 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/4` |
| `scnPlaySkAnimEvent` | 52 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 5 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 30 | 663 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scneventsVFXEvent` | 21 | 795 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, animation_state: 2
- skeletal_animation, socket_signal: 2
- vfx: 2
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- gaze, vfx, socket_signal, animation_state: 1
- skeletal_animation, vfx, socket_signal: 1
- socket_signal: 1
- skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `fd06d71d08a9ad64d8f1b51caf8e14fbca96e7a52ec551eadcbf4889b095c221`. Binary SHA-256: `b652f7a06420209834929193e6e97d3127b41b10c952425fea4289a3020eddd5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09a_inner_bunker_hallucination_oath.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09b_inner_bunker_hallucination_flatline.scene`

273 graph nodes, 392 edges; 23 event-bearing sections, 279 events; 70 screenplay lines, 1 screenplay options, 0 choice nodes.

Actors: Reed (actor 0, community); Songbird (actor 1, community); Songbird_holo (actor 2, spawnSet); Reed2 (actor 3, community); Songbird2 (actor 4, community); Reed3 (actor 5, community); Songbird3 (actor 6, community); Reed4 (actor 7, community); Songbird4 (actor 8, community); Reed_holo (actor 9, spawnSet); Player (actor 10, findInContext).

Entries: `Start 0` → 1; `2nd instance` → 399; `3rd instance` → 434; `4rd instance` → 1419; `Start 9` → 2114; `Start 10` → 2116; `Start 5` → 1821; `Start 11` → 2151; `Start 12` → 2184; `Start 13` → 2189; `Start 14` → 2216; `escalation_preview` → 2546; `audible_hallucination_in` → 2249.

Exits: `End 4` → 2843; `End 3` → 1963.

End nodes: 1963: `<omitted>`; 2843: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 26 | 313 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnDialogLineEvent` | 49 | 313 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnLookAtAdvancedEvent` | 1 | 1910 / 1066 | `/Data/RootChunk/sceneGraph/Data/graph/134/Data/events/11` |
| `scnLookAtEvent` | 24 | 313 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnPlaySkAnimEvent` | 55 | 223 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPoseCorrectionEvent` | 7 | 313 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/25` |
| `scneventsAttachPropToPerformer` | 5 | 313 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scneventsEquipItemToPerformer` | 1 | 797 / 411 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |
| `scneventsSocket` | 66 | 223 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 1 | 313 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/24` |
| `scneventsVFXEvent` | 44 | 306 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 2
- socket_signal: 2
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- vfx: 1

Raw SHA-256: `9dcff607112d0d8fd80433f9e0aa8841cdb83feb645c9c8f0339416c0c2f58ea`. Binary SHA-256: `e6c0f029c7e20fa38518be9714decb0f68a8f5adfdbd25a6d541649fe4a97f07`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09b_inner_bunker_hallucination_flatline.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09c_inner_bunker_minor_hallucinations.scene`

87 graph nodes, 98 edges; 12 event-bearing sections, 61 events; 17 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: somi_angry (actor 0, community); somi_nightmare (actor 1, community); somi_crying (actor 2, community); somi_typing (actor 3, community); computer (actor 4, spawnSet); Player (actor 5, findInContext).

Entries: `start_ib_hallucinations` → 1; `Start 5` → 240; `somi_on_stairs_preview` → 10; `Start 6` → 269; `Start 2` → 40; `Start 7` → 277; `Start 3` → 69; `Start 4` → 82.

Exits: `End 4` → 646.

End nodes: 646: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 9 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 5 | 9 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnLookAtAdvancedEvent` | 6 | 9 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scnLookAtEvent` | 2 | 83 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 15 | 9 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsSocket` | 18 | 9 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsVFXEvent` | 8 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 3
- idle_animation, socket_signal: 3
- vfx: 3
- socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `0ad71f8221a066230a671be7fcdcf101bf0c113560bf6a4f37bbbb240fa82d5e`. Binary SHA-256: `fddee1d8b7409aa967ee0c2a5c7e478882d59d27358a53002dd9deec49e13f80`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09c_inner_bunker_minor_hallucinations.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09d_cerberus_finale.scene`

102 graph nodes, 117 edges; 3 event-bearing sections, 57 events; 7 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Cerberus (actor 0, community); Songbird (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 2` → 277; `q305_09_system_reset_in` → 38; `Cerber_dead` → 101.

Exits: `q305_09_system_reset_out` → 4; `End 1` → 113.

End nodes: 4: `NonTerminating`; 113: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 8 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnChangeIdleAnimEvent` | 3 | 8 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnDialogLineEvent` | 3 | 8 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scnPlaySkAnimEvent` | 5 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsCameraParamsEvent` | 5 | 8 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scneventsSocket` | 17 | 8 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsVFXEvent` | 19 | 8 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 1
- vfx: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1

Raw SHA-256: `db2de1f50e95b1a54e021eea232377ded583c8e8cdcdf7fdce70006d2c357c0d`. Binary SHA-256: `a48f89c29bededb03b67fd22aa2d6a965143e4964517540f1f148643ba27e4f4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09d_cerberus_finale.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09e_inner_bunker_lab_scenes.scene`

207 graph nodes, 300 edges; 20 event-bearing sections, 336 events; 35 screenplay lines, 3 screenplay options, 3 choice nodes.

Actors: Cerberus (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `Start 18` → 1365; `Start 13` → 1175; `Start 20` → 808; `Start 10` → 629; `Start 5` → 441; `Start 4` → 261; `Start 11` → 1101; `Start 12` → 1105; `Start 1` → 140; `Start 19` → 1492; `Start 2` → 142; `Start 16` → 1309; `Start 6` → 542; `Start 7` → 544; `Start 8` → 555; `CP77-65722_IN` → 1917; `Start 9` → 569; `Start 17` → 1342; `Start 3` → 189.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 30 | 10 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnChangeIdleAnimEvent` | 61 | 10 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnGameplayTransitionEvent` | 15 | 10 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/21` |
| `scnIKEvent` | 30 | 10 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/18` |
| `scnPlaySkAnimEvent` | 56 | 10 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnUnmountEvent` | 15 | 10 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/20` |
| `scneventsRagdollEvent` | 1 | 501 / 556 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 19 | 10 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scneventsSetAnimsetWeight` | 2 | 501 / 554 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/10` |
| `scneventsSocket` | 101 | 10 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsVFXEvent` | 6 | 634 / 712 | `/Data/RootChunk/sceneGraph/Data/graph/82/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- skeletal_animation, idle_animation, audio, vfx: 4
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- idle_animation: 2
- skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, idle_animation, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, vfx: 1

Raw SHA-256: `bcbf53d87e6e69f04d441e2562970ea1c7f0c013e880de3de06ed68d084c95ed`. Binary SHA-256: `57a2d334a9a4389b23317eaccc56613f85acc8a3a6b53ee899dab36f6b421c78`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09e_inner_bunker_lab_scenes.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_09f_inner_bunker_killroom.scene`

278 graph nodes, 495 edges; 64 event-bearing sections, 180 events; 70 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Cerberus (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `instant_killroom` → 1191; `Start1` → 612; `Start 11` → 50.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnPlaySkAnimEvent` | 115 | 58 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scneventsCameraParamsEvent` | 2 | 956 / 1470 | `/Data/RootChunk/sceneGraph/Data/graph/216/Data/events/0` |
| `scneventsSocket` | 60 | 28 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/3` |
| `scneventsVFXEvent` | 3 | 28 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 55
- skeletal_animation: 7
- vfx, socket_signal: 1
- camera, socket_signal: 1

Raw SHA-256: `b5e2ff6a45aa28e6f216dd77515fce701b28fb25198a6833ab532db980c41836`. Binary SHA-256: `2991083218edac7d97294abfafb7e5e65b12725970e693964eb2141c548c53f8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_09f_inner_bunker_killroom.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_10_songbird_finale.scene`

203 graph nodes, 253 edges; 53 event-bearing sections, 751 events; 134 screenplay lines, 32 screenplay options, 12 choice nodes.

Actors: Songbird (actor 0, spawnSet); Reed (actor 1, spawnSet); reed_holo (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `Start 0` → 1; `Start 2` → 861; `Start 1` → 717; `Start 4` → 1195.

Exits: `End 0` → 2; `prefetch_out` → 728.

End nodes: 2: `<omitted>`; 728: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 64 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnChangeIdleAnimEvent` | 73 | 6 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scnDialogLineEvent` | 81 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnIKEvent` | 24 | 23 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |
| `scnLookAtAdvancedEvent` | 68 | 23 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/10` |
| `scnLookAtEvent` | 65 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnPlaySkAnimEvent` | 272 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 22 | 6 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scneventsCameraParamsEvent` | 10 | 230 / 623 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/12` |
| `scneventsSocket` | 69 | 6 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/23` |
| `scneventsVFXEvent` | 3 | 313 / 799 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/18` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 6
- speech, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 4
- gaze: 4
- speech, skeletal_animation, gaze, audio, socket_signal: 3
- speech: 3
- speech, audio: 2
- skeletal_animation, idle_animation, camera, audio, socket_signal: 2
- skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, socket_signal: 1
- idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, ik, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, camera, audio, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, audio: 1
- skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, camera, socket_signal: 1

Raw SHA-256: `695fbf3f31f67d142dbc5dddd7a577c8d67d7c0d05b7785c4778df54b88b8dfd`. Binary SHA-256: `b56156e2a426eef392720d4a52b14327a64602be70980d35a7d8a2466baf2294`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_10_songbird_finale.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_11_border_crossing.scene`

1824 graph nodes, 2668 edges; 349 event-bearing sections, 2775 events; 507 screenplay lines, 71 screenplay options, 27 choice nodes.

Actors: reed (actor 0, spawnSet); myers (actor 1, spawnSet); songbird (actor 2, spawnSet); helicopter_crew1 (actor 3, community); helicopter_crew_2 (actor 4, community); secret_service_main (actor 5, community); secret_service_reward (actor 6, community); ripperdoc (actor 7, community); background_agent_01 (actor 8, community); background_agent_02 (actor 9, community); background_agent_03 (actor 10, community); nusa_soldier_01 (actor 11, community); nusa_soldier_03 (actor 12, community); nusa_soldier_04 (actor 13, community); nusa_soldier_05 (actor 14, community); sniper1 (actor 15, community); sniper2 (actor 16, community); nusa_soldier_06 (actor 17, community); nusa_soldier_07 (actor 18, community); nusa_soldier_08 (actor 19, community); foreground_lane_soldier_1 (actor 20, community); foreground_lane_soldier_2 (actor 21, community); foreground_lane_soldier_3 (actor 22, community); foreground_lane_soldier_4 (actor 23, community); foreground_lane_soldier_5 (actor 24, community); foreground_lane_soldier_6 (actor 25, community); foreground_lane_soldier_7 (actor 26, community); foreground_lane_soldier_8 (actor 27, community); nusa_soldier_02 (actor 28, community); soldier_passage_001 (actor 29, community); soldier_passage_002 (actor 30, community); soldier_passage_003 (actor 31, community); soldier_passage_004 (actor 32, community); soldier_passage_005 (actor 33, community); socal_border_guard_passage_001 (actor 34, community); convoy_agent_01 (actor 35, community); convoy_agent_02 (actor 36, community); foreground_lane_soldier_9 (actor 37, community); foregound_lane_soldier_10 (actor 38, community); foreground_agent_001 (actor 39, community); convoy_agent_03 (actor 40, community); convoy_agent_04 (actor 41, community); socal_bg_lane (actor 42, community); socal_bg_lane_02 (actor 43, community); socal_bg_lane_03 (actor 44, community); agent_bg_lane (actor 45, community); mech_patrolling_bg_lane_001 (actor 46, community); soldier_patrolling_bg_lane_001 (actor 47, community); soldier_patrolling_bg_lane_002 (actor 48, community); agent_blockade (actor 49, spawnSet); policeman_1 (actor 50, spawnSet); driver_1 (actor 51, spawnSet); driver_2 (actor 52, spawnSet); traffic_droid_1 (actor 53, community); traffic_droid_2 (actor 54, community); traffic_droid_3 (actor 55, community); traffic_droid_4 (actor 56, community); traffic_droid_5 (actor 57, community); traffic_droid_6 (actor 58, community); traffic_droid_7 (actor 59, community); traffic_droid_8 (actor 60, community); traffic_socal_1 (actor 61, community); traffic_socal_2 (actor 62, community); traffic_socal_3 (actor 63, community); traffic_socal_4 (actor 64, community); traffic_socal_5 (actor 65, community); traffic_socal_6 (actor 66, community); traffic_socal_7 (actor 67, community); traffic_socal_8 (actor 68, community); traffic_socal_9 (actor 69, community); traffic_socal_10 (actor 70, community); traffic_socal_11 (actor 71, community); traffic_socal_12 (actor 72, community); traffic_civ_out_01 (actor 73, community); traffic_civ_out_02 (actor 74, community); traffic_civ_out_03 (actor 75, community); traffic_civ_out_04 (actor 76, community); traffic_civ_out_05 (actor 77, community); traffic_civ_out_06 (actor 78, community); traffic_civ_out_07 (actor 79, community); traffic_civ_out_08 (actor 80, community); traffic_civ_out_09 (actor 81, community); traffic_civ_out_10 (actor 82, community); traffic_civ_out_11 (actor 83, community); traffic_civ_out_12 (actor 84, community); traffic_civ_out_13 (actor 85, community); traffic_civ_out_14 (actor 86, community); traffic_civ_out_15 (actor 87, community); traffic_civ_out_16 (actor 88, community); traffic_socal_commander (actor 89, community); reed_car (actor 90, spawnSet); sbhelicopter (actor 91, community); myers_av (actor 92, community); nusa_av1 (actor 93, community); stretchers (actor 94, community); nusa_av2 (actor 95, community); nusa_car3 (actor 96, community); nusa_car4 (actor 97, community); nusa_car1 (actor 98, community); nusa_suv5 (actor 99, community); nusa_av3 (actor 100, community); nusa_av4 (actor 101, community); convoy_suv_01 (actor 102, community); av_bg_lane (actor 103, community); nusa_av_6 (actor 104, community); nusa_av_7 (actor 105, community); nusa_av_8 (actor 106, community); traffic_car_1 (actor 107, community); traffic_car_2 (actor 108, community); traffic_car_3 (actor 109, community); traffic_car_4 (actor 110, community); traffic_car_5 (actor 111, community); traffic_car_6 (actor 112, community); traffic_car_7 (actor 113, community); traffic_car_8 (actor 114, community); traffic_car_9 (actor 115, community); traffic_car_10 (actor 116, community); traffic_car_11 (actor 117, community); traffic_car_12 (actor 118, community); traffic_car_13 (actor 119, community); traffic_car_14 (actor 120, community); traffic_car_15 (actor 121, community); traffic_car_16 (actor 122, community); traffic_car_17 (actor 123, community); traffic_car_18 (actor 124, community); traffic_car_19 (actor 125, community); traffic_car_20 (actor 126, community); traffic_car_21 (actor 127, community); traffic_car_22 (actor 128, community); traffic_car_23 (actor 129, community); traffic_car_24 (actor 130, community); traffic_car_25 (actor 131, community); traffic_car_26 (actor 132, community); traffic_car_27 (actor 133, community); traffic_car_28 (actor 134, community); traffic_car_29 (actor 135, community); traffic_car_30 (actor 136, community); traffic_car_31 (actor 137, community); traffic_car_32 (actor 138, community); traffic_car_33 (actor 139, community); traffic_car_34 (actor 140, community); traffic_car_35 (actor 141, community); traffic_car_36 (actor 142, community); traffic_car_37 (actor 143, community); traffic_car_38 (actor 144, community); traffic_car_39 (actor 145, community); traffic_car_40 (actor 146, community); traffic_car_41 (actor 147, community); traffic_car_42 (actor 148, community); traffic_car_43 (actor 149, community); traffic_car_44 (actor 150, community); traffic_car_45 (actor 151, community); traffic_car_46 (actor 152, community); traffic_retreating_car (actor 153, community); traffic_overtaking_car (actor 154, community); reed_car_test (actor 155, spawnSet); V (actor 156, findInContext).

Entries: `q305_11_border_crossing_in` → 1; `Start 36` → 8901; `Start 37` → 8913; `Start 40` → 8923; `Start 41` → 8925; `Start 44` → 8936; `Start 45` → 8942; `Start3` → 7479; `Start 46` → 8972; `Start 135` → 16347; `Start 49` → 9075; `Start 51` → 9087; `Start 136` → 16467; `Start 53` → 9117; `preview` → 274; `Start 137` → 16492; `Start 138` → 16498; `Start 116` → 15038; `Start 117` → 15058; `Start 58` → 9243; `helicopter_leaving` → 3352; `Start 120` → 15147; `Start 59` → 9252; `Start 60` → 9254; `Start 64` → 9277; `Start 16` → 7803; `Start 90` → 12231; `Start 65` → 9309; `Start 139` → 16702; `Start 92` → 12282; `Start 17` → 7871; `Start 18` → 7882; `Start 19` → 7887; `Start 20` → 7900; `Start 21` → 7911; `Start 22` → 7915; `Start 67` → 9397; `Start 68` → 9404; `Start 141` → 16790; `Start 23` → 7996; `reed_sit` → 15368; `Start 71` → 9478; `Start 73` → 9540; `Start 79` → 11071; `Start 80` → 11073; `Start 105` → 14050; `Start 81` → 11104; `Start 82` → 11114; `Start 74` → 9657; `Start 143` → 17052; `Start 98` → 12639; `Start 109` → 14248; `Start 126` → 15742; `Start 75` → 9868; `Start 127` → 15811; `Start 27` → 8441; `Start 28` → 8505; `Start 112` → 14442; `Start 7` → 7091; `Start 5` → 4152; `Start 113` → 14486; `Start 76` → 10092; `Start 145` → 17483; `Start 32` → 8691; `Start 129` → 16112; `Start 130` → 16114; `Start 131` → 16122; `Start 132` → 16126; `Start 133` → 16128; `farewell_with_myers` → 4369; `car_stop_units_placement` → 7321; `Start 33` → 8803; `Start 34` → 8805; `Start 134` → 16188; `Start 35` → 8829.

Exits: `End 6` → 8903; `Prefetch_out` → 15100; `q305_11_border_crossing_end` → 4276.

End nodes: 4276: `<omitted>`; 8903: `<omitted>`; 15100: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 33 | 399 / 370 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/17` |
| `scnChangeIdleAnimEvent` | 162 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 319 | 97 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/13` |
| `scnGameplayActionEvent` | 9 | 97 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/31` |
| `scnGameplayTransitionEvent` | 23 | 97 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/26` |
| `scnIKEvent` | 70 | 97 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/18` |
| `scnLookAtAdvancedEvent` | 50 | 3187 / 1760 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/122` |
| `scnLookAtEvent` | 706 | 97 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 385 / 338 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/0` |
| `scnPlaySkAnimEvent` | 565 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnPoseCorrectionEvent` | 24 | 399 / 363 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/10` |
| `scnUnmountEvent` | 23 | 97 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/27` |
| `scneventsAttachPropToPerformer` | 10 | 500 / 408 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/3` |
| `scneventsAttachPropToWorld` | 4 | 3 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsCameraParamsEvent` | 25 | 399 / 368 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/15` |
| `scneventsEquipItemToPerformer` | 43 | 2180 / 820 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/13` |
| `scneventsMountEvent` | 2 | 97 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/32` |
| `scneventsRagdollEvent` | 2 | 3187 / 1583 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/36` |
| `scneventsSetAnimFeatureEvent` | 61 | 97 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/21` |
| `scneventsSetAnimsetWeight` | 20 | 97 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scneventsSocket` | 609 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 8840 / 5171 | `/Data/RootChunk/sceneGraph/Data/graph/510/Data/events/10` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 5144 / 2354 | `/Data/RootChunk/sceneGraph/Data/graph/203/Data/events/8` |
| `scneventsVFXEvent` | 11 | 399 / 376 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/23` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 68
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 44
- gaze: 42
- speech, skeletal_animation, gaze, socket_signal: 15
- skeletal_animation, gaze, socket_signal: 13
- skeletal_animation, socket_signal: 10
- speech, socket_signal: 9
- speech, skeletal_animation, socket_signal: 9
- socket_signal: 8
- props_equipment, socket_signal: 8
- skeletal_animation, gaze: 7
- speech, gaze: 6
- speech, skeletal_animation, gaze, socket_signal, animation_state: 5
- speech, skeletal_animation, gaze: 5
- skeletal_animation, idle_animation, socket_signal: 5
- skeletal_animation: 5
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 3
- idle_animation, gameplay_action: 3
- skeletal_animation, idle_animation: 3
- gaze, socket_signal: 3
- skeletal_animation, props_equipment, socket_signal: 3
- camera: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- ik, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 2
- skeletal_animation, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- socket_signal, animation_state: 2
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, camera, socket_signal, animation_state: 2
- props_equipment: 2
- animation_state: 2
- props_equipment, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, camera, socket_signal, animation_state: 1
- idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, animation_state: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, camera, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- idle_animation: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- idle_animation, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, ik, camera, socket_signal, animation_state: 1

Raw SHA-256: `97cce75b54a372db889c2c478fe565820738824d1c54265eec356b53019a23b6`. Binary SHA-256: `ae78f8c943ef2bb20442666533c899ce2b8e8ef75f2ba6d595e07b9783f342f8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_11_border_crossing.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_12_johnny.scene`

260 graph nodes, 298 edges; 73 event-bearing sections, 792 events; 239 screenplay lines, 53 screenplay options, 9 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); v_mirror_tpp_female (actor 1, spawnDespawn); v_mirror_tpp_male (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `Start 0` → 1; `Start 2` → 612; `Start2` → 956; `Start 4` → 1591; `Start1` → 754.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 28 | 770 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/10` |
| `scnChangeIdleAnimEvent` | 16 | 886 / 432 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/1` |
| `scnDialogLineEvent` | 89 | 770 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnGameplayTransitionEvent` | 21 | 832 / 241 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/9` |
| `scnIKEvent` | 42 | 832 / 233 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/2` |
| `scnLookAtAdvancedEvent` | 5 | 916 / 719 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/11` |
| `scnLookAtEvent` | 125 | 770 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/5` |
| `scnOverridePhantomParamsEvent` | 10 | 832 / 248 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/11` |
| `scnPlaySkAnimEvent` | 210 | 606 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPoseCorrectionEvent` | 14 | 770 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/9` |
| `scnUnmountEvent` | 21 | 832 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/8` |
| `scneventsAttachPropToPerformer` | 2 | 1590 / 1422 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 1590 / 1436 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/8` |
| `scneventsCameraParamsEvent` | 8 | 832 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/4` |
| `scneventsEquipItemToPerformer` | 15 | 770 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 21 | 832 / 236 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/5` |
| `scneventsSocket` | 152 | 606 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsSpawnEntityEvent` | 1 | 1590 / 1437 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/9` |
| `scneventsUnequipItemFromPerformer` | 7 | 770 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/12` |
| `scneventsVFXEvent` | 4 | 850 / 318 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 14
- skeletal_animation, gaze, socket_signal: 10
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal, animation_state: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, socket_signal: 3
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, props_equipment, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- socket_signal: 2
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, audio, vfx: 1
- skeletal_animation, camera, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, animation_state: 1
- speech: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, entity_lifecycle: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `2450446cbee67b1f42090e36cfa0c2a4bec378fd2bbefcb805b7e88cd0bd3564`. Binary SHA-256: `2389f1f738efe13a68cf953415343b7d3956a4efeb74098b3c4c1392b4345fde`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_12_johnny.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_13_reed_epilogue.scene`

228 graph nodes, 333 edges; 84 event-bearing sections, 946 events; 246 screenplay lines, 62 screenplay options, 21 choice nodes.

Actors: player1 (actor 0, community); player2 (actor 1, community); player3 (actor 2, community); player4 (actor 3, community); player5 (actor 4, community); player6 (actor 5, community); reed (actor 6, spawnSet); v (actor 7, findInContext).

Entries: `Start` → 1; `Start 1` → 873.

Exits: `End 0` → 2; `End 2` → 1699.

End nodes: 2: `NonTerminating`; 1699: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 325 / 513 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/5` |
| `scnChangeIdleAnimEvent` | 49 | 11 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnDialogLineEvent` | 194 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 325 / 515 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/7` |
| `scnIKEvent` | 6 | 325 / 509 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/1` |
| `scnLookAtAdvancedEvent` | 45 | 10 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnLookAtEvent` | 257 | 10 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnPlaySkAnimEvent` | 263 | 10 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnUnmountEvent` | 3 | 325 / 520 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/11` |
| `scneventsAttachPropToPerformer` | 8 | 792 / 1467 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/7` |
| `scneventsCameraParamsEvent` | 12 | 11 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 3 | 325 / 516 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/8` |
| `scneventsSocket` | 97 | 10 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 22
- speech, skeletal_animation, gaze, socket_signal: 13
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 7
- skeletal_animation, props_equipment, socket_signal: 7
- gaze: 5
- speech: 4
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, socket_signal: 3
- skeletal_animation, gaze: 3
- speech, gaze: 2
- camera, socket_signal: 2
- speech, skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, audio: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation: 1
- idle_animation, gaze, socket_signal: 1
- audio: 1
- speech, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- camera: 1

Raw SHA-256: `dcc72232ac0ab3385af2e74287e095239892bb98400952faf76c5584bb7db177`. Binary SHA-256: `d9719ebd34a711c5875fe20e51764e1934ef8198c393d47ce681eee9d567ea12`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_13_reed_epilogue.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_13a_reed_waiting.scene`

18 graph nodes, 17 edges; 4 event-bearing sections, 14 events; 5 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Player (actor 0, findInContext).

Entries: `q305_13a_wait_in` → 1.

Exits: `q305_13a_wait_out` → 2; `q305_13a_spawning_out` → 73.

End nodes: 2: `<omitted>`; 73: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 9 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 36 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnIKEvent` | 2 | 36 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 2 | 36 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnUnmountEvent` | 1 | 36 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 1 | 36 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scneventsSocket` | 5 | 18 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1
- speech, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `e39844c6b7af4adb5d98ee25cca5fd23ecdec3937cabf4217aa506315f940191`. Binary SHA-256: `691ddccf277ee235c2ba0224860ca1296c259d9f019deffd61527682dbf879e1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_13a_reed_waiting.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_14_after_quest_fixer_holo.scene`

49 graph nodes, 52 edges; 14 event-bearing sections, 24 events; 24 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: wakako_holo (actor 0, spawnSet); mr_hands_holo (actor 1, spawnSet); alex_holo (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `q305_wakako_afterquest_holo_in` → 4; `q305_mrhands_afterquest_holo_in` → 33.

Exits: `rejected_wakako_out` → 196; `q305_wakako_afterquest_holo_out` → 6; `q305_mrhands_afterquest_holo_out` → 35; `rejected_hands_out` → 183.

End nodes: 6: `<omitted>`; 35: `<omitted>`; 183: `<omitted>`; 196: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 24 | 62 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 14

Raw SHA-256: `2c0f2a4f9268edfba42a4926ea50fbd9635d7abec8ff826c08c6bfd2dab52853`. Binary SHA-256: `429f0cda0d09b31deaa73d601a1ad8b8a36c93c4077fc8b64c101712a273cedf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_14_after_quest_fixer_holo.scene" --events
```

