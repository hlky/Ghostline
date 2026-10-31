# Don't Lose Your Mind: scene presentation

Journal identity: `quests/side_quest/sq025b_delamain_insurgence`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq025b_delamain_insurgence.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq025\scenes\sq025_07_resurgence.scene`

55 graph nodes, 60 edges; 3 event-bearing sections, 10 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Delamain (actor 1, spawnSet); sq025_resurgence_truck_01 (actor 2, spawner); sq025_resurgence_delamain_broken_04 (actor 3, spawner); sq025_resurgence_delamain_broken_03 (actor 4, spawner); Player (actor 5, findInContext).

Entries: `resurgence_in` → 1; `Start 1` → 136.

Exits: `resurgence_out` → 2; `exit` → 97.

End nodes: 2: `NonTerminating`; 97: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 7 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 2 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 1 | 171 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 1
- speech, socket_signal: 1
- speech: 1

Raw SHA-256: `cacdd871cb515af924a647c1a6f41066c7875366050fc7f0f77eaf91cabd10f8`. Binary SHA-256: `7874e068ffcb83180daa16e94e0db4d6547f0d1d56c0026c20629ef6b60accec`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_07_resurgence.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_08_backoffice.scene`

17 graph nodes, 14 edges; 5 event-bearing sections, 7 events; 7 screenplay lines, 3 screenplay options, 3 choice nodes.

Actors: Delamain (actor 0, spawnSet); Johnny (actor 1, spawnSet); Business (actor 2, community); Player (actor 3, findInContext).

Entries: `reception_in` → 1; `backoffice_in` → 40; `corrdidor_in` → 163.

Exits: `reception_out` → 2; `backoffice_out` → 165.

End nodes: 2: `<omitted>`; 165: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 2 | 170 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, socket_signal: 2

Raw SHA-256: `e50dd8831566708ec04e83b2fea340694e7d1c7160591862915b7b81cfa147fe`. Binary SHA-256: `f3c1273f2759ebec58907911f3e61d709257d523acfef75de025f5e7ed926182`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_08_backoffice.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_09_labyrinth.scene`

80 graph nodes, 76 edges; 15 event-bearing sections, 88 events; 42 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Delamain_distorted (actor 1, findInContext); Delamain_angry (actor 2, findInContext); Delamain_sad (actor 3, findInContext); Delamain_manic (actor 4, findInContext); Delamain_mean (actor 5, findInContext); Delamain_scared (actor 6, findInContext); Delamain_deep (actor 7, findInContext); Delamain_suicidal (actor 8, findInContext); sq025_spwn_delamain_garage_push_cab (actor 9, spawner); Player (actor 10, findInContext).

Entries: `banter01_in` → 90; `banter02_in` → 91; `push_cab_in` → 11; `Start 11` → 332; `hangar_in` → 99; `q115_reuse__in` → 115; `Start 9` → 122; `Start 12` → 373; `workshop_intro_in` → 64; `sq025_09_custom_arms` → 388; `Start 10` → 239.

Exits: `q115_reuse__out` → 116; `workshop_intro_out` → 65.

End nodes: 65: `NonTerminating`; 116: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 106 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/3` |
| `scnDialogLineEvent` | 24 | 66 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 173 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/5` |
| `scnIKEvent` | 2 | 173 / 160 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/1` |
| `scnLookAtEvent` | 1 | 66 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnPlaySkAnimEvent` | 48 | 106 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnUnmountEvent` | 1 | 173 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/4` |
| `scneventsCameraParamsEvent` | 2 | 106 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 1 | 173 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/3` |
| `scneventsSocket` | 7 | 66 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 7
- speech: 3
- speech, socket_signal: 2
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, camera: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `c28f6a9e09a6688edcd70946f2ad7a510d3a91026fdf5b13e543d7f83878e4fb`. Binary SHA-256: `1645cbcd9a4f6b7915fa416f5451dfe683ad975b6467926a406100067662dab1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_09_labyrinth.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_10_resolution.scene`

685 graph nodes, 808 edges; 58 event-bearing sections, 218 events; 143 screenplay lines, 13 screenplay options, 6 choice nodes.

Actors: Delamain (actor 0, spawnDespawn); Drone03 (actor 1, community); Drone04 (actor 2, community); Drone05 (actor 3, community); Drone06 (actor 4, community); Drone07 (actor 5, community); Johnny (actor 6, spawnDespawn); Delamain_Merged (actor 7, spawnDespawn); Delamain_Angry (actor 8, spawnDespawn); Delamain_Mean (actor 9, spawnDespawn); Delamain_Sad (actor 10, spawnDespawn); Delamain_Suicidal (actor 11, spawnDespawn); Delamain_Scared (actor 12, spawnDespawn); Delamain_Deep (actor 13, spawnDespawn); Delamain_Manic (actor 14, spawnDespawn); Delamain_Shy (actor 15, spawnDespawn); del_r1_l1 (actor 16, spawner); del_r1_l2 (actor 17, spawner); del_r1_l3 (actor 18, spawner); del_r1_l4 (actor 19, spawner); del_r1_l5 (actor 20, spawner); del_r2_l1 (actor 21, spawner); del_r2_l2_SAD (actor 22, spawner); del_r2_l3 (actor 23, spawner); del_r2_l4 (actor 24, spawner); del_r2_l5 (actor 25, spawner); del_player (actor 26, spawner); Player (actor 27, findInContext).

Entries: `resolution_in` → 1; `Start 3` → 1625; `Start 4` → 1687; `Start 5` → 1689; `Start 11` → 3253; `Start 6` → 1724; `rec` → 3355; `Start 8` → 2761; `suicidal_only` → 2031; `Start 13` → 3659; `controlroom_in` → 580; `Start 9` → 3000; `Start 10` → 3060; `Start 2` → 1538.

Exits: `controlroom_out` → 581; `resolution_out` → 586.

End nodes: 581: `NonTerminating`; 586: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1270 / 346 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/3` |
| `scnChangeIdleAnimEvent` | 31 | 31 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnDialogLineEvent` | 98 | 25 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 1627 / 877 | `/Data/RootChunk/sceneGraph/Data/graph/118/Data/events/8` |
| `scnIKEvent` | 2 | 2993 / 2089 | `/Data/RootChunk/sceneGraph/Data/graph/315/Data/events/3` |
| `scnLookAtEvent` | 10 | 1264 / 314 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/2` |
| `scnPlaySkAnimEvent` | 32 | 1264 / 323 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/10` |
| `scneventsCameraParamsEvent` | 4 | 1270 / 345 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/2` |
| `scneventsEquipItemToPerformer` | 3 | 1264 / 319 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/7` |
| `scneventsSocket` | 34 | 25 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 1 | 1264 / 329 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- idle_animation: 14
- speech, socket_signal: 11
- speech, gaze: 3
- speech, gaze, socket_signal: 2
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation: 1
- skeletal_animation, idle_animation, gameplay_action: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, socket_signal: 1
- socket_signal: 1
- skeletal_animation, ik, camera, socket_signal: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `a458a34e3f140486010e42ca35d64584133da5667c05bd81842f50239f2912d7`. Binary SHA-256: `6c1c965b2557b8ada4372b226f3702c93362e73076b7bbe368b780f57c880aee`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_10_resolution.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_04_cabride.scene`

273 graph nodes, 417 edges; 76 event-bearing sections, 290 events; 221 screenplay lines, 44 screenplay options, 18 choice nodes.

Actors: delamain (actor 0, spawnSet); radio_host1 (actor 1, findInContext); radio_host2 (actor 2, findInContext); junior_delamain (actor 3, findInContext); delamain_cab (actor 4, spawner); av1 (actor 5, spawner); av2 (actor 6, spawner); Player (actor 7, findInContext).

Entries: `Start 0` → 1; `av_landing_in` → 1799.

Exits: `End 0` → 2; `End1` → 1059.

End nodes: 2: `NonTerminating`; 1059: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1783 / 1177 | `/Data/RootChunk/sceneGraph/Data/graph/216/Data/events/1` |
| `scnChangeIdleAnimEvent` | 1 | 1783 / 1178 | `/Data/RootChunk/sceneGraph/Data/graph/216/Data/events/2` |
| `scnDialogLineEvent` | 203 | 22 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 1085 / 655 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/8` |
| `scnIKEvent` | 4 | 1085 / 646 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/1` |
| `scnPlaySkAnimEvent` | 16 | 210 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scnUnmountEvent` | 2 | 1085 / 659 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/11` |
| `scneventsAttachPropToPerformer` | 5 | 1085 / 649 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/4` |
| `scneventsAttachPropToWorld` | 2 | 1085 / 654 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/7` |
| `scneventsCameraParamsEvent` | 11 | 210 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 4 | 1085 / 657 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/10` |
| `scneventsSocket` | 37 | 210 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scneventsVFXEvent` | 2 | 1783 / 1179 | `/Data/RootChunk/sceneGraph/Data/graph/216/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 56
- speech, socket_signal: 7
- skeletal_animation, camera, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, camera, props_equipment, socket_signal: 2
- speech, skeletal_animation, camera, socket_signal: 1
- skeletal_animation, camera, props_equipment, socket_signal, animation_state: 1
- skeletal_animation: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1

Raw SHA-256: `ae5ecffe9e87b13df061de1b891e2b24a280ec411ca8198e8a9638ab4d262ae6`. Binary SHA-256: `a8a0e38d8ba90b4f35bfb879dafdaee51dbd6598194e4e561ed80004a9e98b37`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_04_cabride.scene" --events
```

