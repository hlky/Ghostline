# Venus in Furs: scene presentation

Journal identity: `quests/main_quest/prologue/q003_stout`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q003_stout.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene`

34 graph nodes, 43 edges; 7 event-bearing sections, 36 events; 15 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: johnny (actor 0, spawnDespawn); johnny_spawnset_cat (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `q003_cat_flat_reaction_in` → 199.

Exits: `End 0` → 2; `q003_cat_flat_reaction_out` → 200.

End nodes: 2: `<omitted>`; 200: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 17 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnDialogLineEvent` | 15 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 7 | 10 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 7 | 10 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsSocket` | 6 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 3
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, gaze: 1

Raw SHA-256: `8f564be05586715a43a7099da8cdcab48cd29ed8ade4643e832e337981cde855`. Binary SHA-256: `5578cbbdf013f163a6653b9362fbeccf989e523e02eedb62c6850618ca59eb85`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_07a_final_corp.scene`

301 graph nodes, 351 edges; 41 event-bearing sections, 310 events; 80 screenplay lines, 12 screenplay options, 6 choice nodes.

Actors: Jackie (actor 0, spawnSet); Meredith (actor 1, spawnSet); Bodyguard_01 (actor 2, community); Bodyguard_02 (actor 3, community); suv (actor 4, community); militech_soldier1 (actor 5, community); militech_soldier2 (actor 6, community); militech_soldier3 (actor 7, community); militech_soldier4 (actor 8, community); militech_soldier5 (actor 9, community); militech_soldier6 (actor 10, community); militech_drone (actor 11, community); Johnny (actor 12, spawnSet); Meredith_holocall (actor 13, spawnSet); jackie_bike (actor 14, spawnSet); av1 (actor 15, community); av2 (actor 16, community); Player (actor 17, findInContext).

Entries: `q003_07a_finale_in` → 1; `q003_07a_drone_in` → 1495; `jackie_bye_preview` → 2708; `q003_07a_stout_corpse_in` → 2152; `q003_07a_stout_sex_end_in` → 2197; `q003_militech_pushback_in` → 2560; `Start 14` → 2869; `q003_07a_stout_holocall_in` → 2286; `meredith_holocall_preview` → 2606; `Start 15` → 2936.

Exits: `q003_07a_finale_out` → 4; `KillSignal` → 2091; `q003_07a_stout_corpse_out` → 2153; `q003_07a_stout_sex_end_out` → 2200; `q003_07a_drone_jackie_out` → 2024; `q003_07a_stout_runn_off_out` → 2321.

End nodes: 4: `NonTerminating`; 2024: `NonTerminating`; 2091: `<omitted>`; 2153: `<omitted>`; 2200: `<omitted>`; 2321: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 31 | 319 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnChangeIdleAnimEvent` | 24 | 116 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnDialogLineEvent` | 65 | 105 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 1977 / 550 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/17` |
| `scnIKEvent` | 10 | 1977 / 541 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/9` |
| `scnLookAtEvent` | 32 | 105 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 70 | 105 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 5 | 1977 / 549 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/16` |
| `scneventsAttachPropToPerformer` | 6 | 505 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 1977 / 545 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/13` |
| `scneventsSocket` | 45 | 105 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXDurationEvent` | 2 | 319 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |
| `scneventsVFXEvent` | 10 | 319 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 6
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation: 4
- speech: 4
- speech, idle_animation, gaze: 3
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 2
- skeletal_animation, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `ca0cc3b04c5c44a13cb79e0d12ff6679c2f41e3b8a5dae28cb48bd1c1e61ade3`. Binary SHA-256: `d3435d0eae2d629a19021d10eee06fd77998321ee629c0d1cd1c319c6eb460d5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_07a_final_corp.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_07aa_final_traitor.scene`

364 graph nodes, 417 edges; 50 event-bearing sections, 406 events; 92 screenplay lines, 11 screenplay options, 5 choice nodes.

Actors: Anthony (actor 0, spawnSet); Jackie (actor 1, spawnSet); bodyguard1 (actor 2, community); bodyguard2 (actor 3, community); soldier1 (actor 4, community); soldier2 (actor 5, community); soldier3 (actor 6, community); soldier4 (actor 7, community); soldier5 (actor 8, community); soldier6 (actor 9, community); Johnny (actor 10, spawnSet); soldier7 (actor 11, community); soldier8 (actor 12, community); soldier9 (actor 13, community); soldier10 (actor 14, community); Anthony_holocall (actor 15, spawnSet); drone (actor 16, community); jackie_bike (actor 17, spawnSet); av1 (actor 18, community); av2 (actor 19, community); q003_suv (actor 20, community); Player (actor 21, findInContext).

Entries: `q003_07_traitor_in` → 1; `av_arrival_preview` → 1503; `Start 5` → 1580; `q003_07aa_gilchrist_holocall_in` → 1025; `jackie_talk_preview` → 1346; `gilchrist_holocall_preview` → 1373; `q003_07aa_gilchrist_corpse_in` → 799.

Exits: `q003_07_traitor_out` → 2; `q003_soldier_pushback_out` → 1290; `q003_07a_gilchrist_runn_off_out` → 1039; `KillSignal` → 754; `q003_07aa_gilchrist_corpse_out` → 800.

End nodes: 2: `NonTerminating`; 754: `<omitted>`; 800: `<omitted>`; 1039: `NonTerminating`; 1290: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 431 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/4` |
| `scnChangeIdleAnimEvent` | 17 | 3 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 69 | 3 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnGameplayActionEvent` | 2 | 1623 / 1978 | `/Data/RootChunk/sceneGraph/Data/graph/256/Data/events/2` |
| `scnGameplayTransitionEvent` | 7 | 381 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/9` |
| `scnIKEvent` | 14 | 381 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnLookAtAdvancedEvent` | 10 | 925 / 740 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/15` |
| `scnLookAtEvent` | 56 | 3 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 82 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 7 | 381 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |
| `scneventsAttachPropToPerformer` | 6 | 433 / 145 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 7 | 381 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scneventsSocket` | 111 | 3 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 6 | 431 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation: 2
- speech, gaze: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- idle_animation, gaze, socket_signal, gameplay_action: 1

Raw SHA-256: `489e8d61e95f85997d1be85ea1a0953b16746482c7b3f8e4b5aa2140ec6e2a12`. Binary SHA-256: `b7ebbe3e1c42af9b1ff0f9d08763973487101517857c130e6724add32000c79b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_07aa_final_traitor.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_08_stout.scene`

192 graph nodes, 208 edges; 31 event-bearing sections, 157 events; 21 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: Meredith (actor 0, spawnSet); Nibbles (actor 1, community); Johnny (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `q003_07a_stout_sex_in` → 1771; `q003_08_cat_in` → 1397; `stout_sex_preview` → 1970; `cat_eat_in` → 2362; `cat_clean_in` → 2364; `cat_idle_in` → 2366; `cat_sleep_in` → 2377; `preview_wakinup` → 2021; `cat_sleep_2_in` → 2420; `cat_scratch_in` → 2431; `cat_lie_in` → 2442.

Exits: `cat_lie_out` → 2444; `q003_08_stout_out` → 3; `q003_07a_stout_no_sex_out` → 1776; `cat_out` → 2359; `cat_eat_out` → 2363; `cat_clean_out` → 2365; `cat_idle_out` → 2367; `cat_sleep_out` → 2379; `q003_08_farewell_stout_out` → 1442; `cat_sleep_2_out` → 2422; `cat_scratch_out` → 2433.

End nodes: 3: `Terminating`; 1442: `NonTerminating`; 1776: `Terminating`; 2359: `NonTerminating`; 2363: `Terminating`; 2365: `Terminating`; 2367: `Terminating`; 2379: `Terminating`; 2422: `Terminating`; 2433: `Terminating`; 2444: `Terminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 54 | 1540 / 230 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/4` |
| `scnChangeIdleAnimEvent` | 11 | 1770 / 434 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/2` |
| `scnDialogLineEvent` | 4 | 1770 / 433 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 1748 / 418 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/3` |
| `scnIKEvent` | 2 | 1748 / 416 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/1` |
| `scnLookAtEvent` | 7 | 1770 / 432 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/0` |
| `scnPlayRidAnimEvent` | 34 | 1540 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/1` |
| `scnPlaySkAnimEvent` | 15 | 1540 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/0` |
| `scnUnmountEvent` | 1 | 1748 / 422 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/6` |
| `scneventsPlayRidCameraAnimEvent` | 14 | 1540 / 229 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 1 | 1748 / 420 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/5` |
| `scneventsSocket` | 7 | 1748 / 419 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/4` |
| `scneventsVFXEvent` | 6 | 1721 / 376 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- rid_actor, camera, rid_camera, audio: 7
- idle_animation: 7
- skeletal_animation, rid_actor, camera, rid_camera, audio: 5
- skeletal_animation, rid_actor, camera, rid_camera, audio, vfx: 2
- gaze: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech: 1
- idle_animation, socket_signal: 1
- socket_signal: 1
- skeletal_animation, vfx: 1
- skeletal_animation, idle_animation, vfx, socket_signal: 1

Raw SHA-256: `44f006b51c7bc91a73f8a2566192963819e55c220f1b79d468ed5f2ec7503e39`. Binary SHA-256: `a96bcf1f8dafc993697631faaf9c1908986bb928a2db425766bdd6e5f9839184`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_08_stout.scene" --events
```

## `base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene`

248 graph nodes, 322 edges; 70 event-bearing sections, 431 events; 124 screenplay lines, 45 screenplay options, 22 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); johnny_spawnset_cat (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `in_q105` → 1; `in_q110` → 7; `in_q104` → 10; `in_q112` → 13; `q104_end` → 1071; `q003_cat_reaction_in` → 894; `q112_end` → 1135; `Start1` → 1871.

Exits: `out` → 2; `q003_cat_reaction_out` → 895; `out_clean_up` → 1437.

End nodes: 2: `NonTerminating`; 895: `<omitted>`; 1437: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 11 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnChangeIdleAnimEvent` | 4 | 45 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/2` |
| `scnDialogLineEvent` | 117 | 8 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnGameplayTransitionEvent` | 6 | 74 / 317 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/5` |
| `scnIKEvent` | 12 | 74 / 313 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scnLookAtEvent` | 61 | 8 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnPlaySkAnimEvent` | 92 | 8 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnUnmountEvent` | 6 | 74 / 323 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/10` |
| `scneventsAttachPropToPerformer` | 4 | 74 / 318 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/6` |
| `scneventsAttachPropToWorld` | 4 | 74 / 335 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/14` |
| `scneventsCameraParamsEvent` | 13 | 74 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 6 | 74 / 319 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/7` |
| `scneventsSocket` | 81 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsVFXEvent` | 23 | 8 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 17
- speech: 16
- speech, skeletal_animation, gaze, vfx, socket_signal: 7
- speech, skeletal_animation: 4
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, camera, vfx, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- speech, gaze: 2
- camera: 2
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- speech, skeletal_animation, props_equipment: 1

Raw SHA-256: `741c9afca4a9bfd7f85b046bb95a55a58f3c8097aaa576df847557bb64192e01`. Binary SHA-256: `96d4c0b4a3c808443ffa337f140bff840293d275ae97115658d190964cdfab10`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq032\scenes\sq032_04_fourth_episode.scene" --events
```

