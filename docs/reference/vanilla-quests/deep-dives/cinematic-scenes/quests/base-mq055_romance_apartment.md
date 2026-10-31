# I Really Want to Stay at Your House: scene presentation

Journal identity: `quests/minor_quest/mq055_romance_apartment`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq055_romance_apartment.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq055\scenes\mq055_01_megabuilding.scene`

1703 graph nodes, 2385 edges; 271 event-bearing sections, 1963 events; 515 screenplay lines, 128 screenplay options, 66 choice nodes.

Actors: judy (actor 0, spawnDespawn); kerry (actor 1, spawnDespawn); panam (actor 2, spawnDespawn); river (actor 3, spawnDespawn); mirror_v_male (actor 4, spawnDespawn); mirror_v_female (actor 5, spawnSet); Player (actor 6, findInContext).

Entries: `judy` → 1; `kerry` → 4; `panam` → 9; `river` → 14; `Start3` → 5123; `Start4` → 5129; `Start5` → 5137; `Start6` → 5143; `Start1` → 3749; `panam_cuddle` → 2283; `Start2` → 3977; `Start 1` → 773; `Start9` → 7600; `Start10` → 7622; `Start11` → 7633; `Start7` → 6100; `Start12` → 9409; `Start8` → 6240; `Start 6` → 9573.

Exits: `judy_done` → 2; `kerry_done` → 6; `panam_done` → 11; `river_done` → 16.

End nodes: 2: `<omitted>`; 6: `<omitted>`; 11: `<omitted>`; 16: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 1978 / 2539 | `/Data/RootChunk/sceneGraph/Data/graph/322/Data/events/0` |
| `scnChangeIdleAnimEvent` | 280 | 613 / 671 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/3` |
| `scnDialogLineEvent` | 367 | 568 / 650 | `/Data/RootChunk/sceneGraph/Data/graph/104/Data/events/0` |
| `scnGameplayTransitionEvent` | 22 | 331 / 425 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/3` |
| `scnIKEvent` | 44 | 331 / 423 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/1` |
| `scnLookAtEvent` | 340 | 389 / 486 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/1` |
| `scnPlaySkAnimEvent` | 475 | 326 / 408 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/0` |
| `scnPoseCorrectionEvent` | 42 | 727 / 862 | `/Data/RootChunk/sceneGraph/Data/graph/127/Data/events/4` |
| `scnUnmountEvent` | 22 | 331 / 429 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/6` |
| `scneventsAttachPropToNode` | 1 | 687 / 807 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/10` |
| `scneventsAttachPropToPerformer` | 2 | 687 / 792 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/1` |
| `scneventsAttachPropToWorld` | 1 | 851 / 1042 | `/Data/RootChunk/sceneGraph/Data/graph/144/Data/events/18` |
| `scneventsCameraParamsEvent` | 49 | 687 / 802 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/5` |
| `scneventsEquipItemToPerformer` | 2 | 2188 / 2929 | `/Data/RootChunk/sceneGraph/Data/graph/365/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 22 | 331 / 427 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/5` |
| `scneventsSocket` | 245 | 326 / 414 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 2 | 2198 / 2950 | `/Data/RootChunk/sceneGraph/Data/graph/368/Data/events/4` |
| `scneventsVFXEvent` | 35 | 676 / 774 | `/Data/RootChunk/sceneGraph/Data/graph/119/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 39
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 18
- speech, skeletal_animation, idle_animation, gaze: 18
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 15
- speech, skeletal_animation, idle_animation, socket_signal: 13
- gaze: 12
- camera: 12
- speech, skeletal_animation, idle_animation: 11
- skeletal_animation: 10
- socket_signal: 9
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 8
- skeletal_animation, gaze: 7
- skeletal_animation, socket_signal: 6
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 6
- speech, skeletal_animation, gaze: 6
- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation: 5
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- skeletal_animation, vfx, socket_signal: 4
- skeletal_animation, gaze, camera, vfx, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal, animation_state: 4
- skeletal_animation, audio, vfx, socket_signal: 4
- skeletal_animation, camera, vfx, socket_signal: 4
- speech, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze, audio: 3
- speech, idle_animation: 3
- vfx: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 2
- props_equipment, socket_signal: 2
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, camera, socket_signal: 2
- skeletal_animation, audio, vfx: 2
- gaze, socket_signal: 1
- speech, skeletal_animation, camera, socket_signal: 1
- skeletal_animation, idle_animation, gaze: 1
- speech, gaze, audio: 1
- skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, audio: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, idle_animation, gaze: 1
- speech, socket_signal: 1
- animation_state: 1
- vfx, socket_signal: 1

Raw SHA-256: `5ef5fb0d96f0e679ba27a30ee1bf50337cff49aad5dd8f8f94a340a00c3ca2a8`. Binary SHA-256: `774026bb3c8c0768fe87ddb0bec4229f2c4993dfb9f0fa63104f61825d80763a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq055\scenes\mq055_01_megabuilding.scene" --events
```

## `base\quest\minor_quests\mq055\scenes\mq055_02_northside.scene`

2237 graph nodes, 3073 edges; 312 event-bearing sections, 2051 events; 521 screenplay lines, 144 screenplay options, 84 choice nodes.

Actors: judy (actor 0, spawnDespawn); kerry (actor 1, spawnDespawn); panam (actor 2, spawnDespawn); river (actor 3, spawnDespawn); v_male_tpp (actor 4, spawnDespawn); v_female_tpp (actor 5, spawnDespawn); johnny_mirror (actor 6, spawnDespawn); Player (actor 7, findInContext).

Entries: `judy` → 4; `kerry` → 8; `panam` → 12; `river` → 16; `Start1_mirror` → 4464; `Start 28` → 10732; `Start 21` → 6564; `Start 5` → 2597; `Start 29` → 11190; `Start 30` → 11269; `rivr_enters_preview` → 11400; `panam_enters_preview` → 11442; `river_cudle_preview` → 11457; `Start 24` → 9465; `Start 2` → 1363; `Start1` → 1366; `Start2` → 1371; `Start 3` → 1473; `judy_cuddle_preview` → 5673; `Start 7` → 5694; `Start 8` → 5711; `Start 9` → 5729; `preview_judy_bed` → 9913; `Start 10` → 5747; `preview_panam_bed` → 9921; `preview_river_bed` → 9928; `Start 11` → 5761; `kerry_cuddle_preview` → 5797; `Start 13` → 5811; `Start 14` → 5830; `Start 15` → 5844; `Start 16` → 5870; `Start 17` → 5890; `judy_enters_preview` → 5912; `kerry_enters_preview` → 5936.

Exits: `judy_done` → 6; `kerry_done` → 10; `panam_done` → 14; `river_done` → 18.

End nodes: 6: `<omitted>`; 10: `<omitted>`; 14: `<omitted>`; 18: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 46 | 1842 / 2539 | `/Data/RootChunk/sceneGraph/Data/graph/355/Data/events/2` |
| `scnChangeIdleAnimEvent` | 239 | 378 / 596 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/11` |
| `scnDialogLineEvent` | 334 | 378 / 594 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/9` |
| `scnGameplayTransitionEvent` | 22 | 398 / 660 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/11` |
| `scnIKEvent` | 44 | 398 / 653 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/5` |
| `scnLookAtAdvancedEvent` | 12 | 378 / 597 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/12` |
| `scnLookAtEvent` | 271 | 378 / 607 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/20` |
| `scnPlaySkAnimEvent` | 501 | 378 / 583 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/4` |
| `scnPoseCorrectionEvent` | 6 | 1851 / 2559 | `/Data/RootChunk/sceneGraph/Data/graph/358/Data/events/2` |
| `scnUnmountEvent` | 22 | 398 / 659 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/10` |
| `scneventsAttachPropToPerformer` | 3 | 378 / 592 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/7` |
| `scneventsAttachPropToWorld` | 2 | 749 / 1145 | `/Data/RootChunk/sceneGraph/Data/graph/158/Data/events/19` |
| `scneventsCameraParamsEvent` | 50 | 378 / 578 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 22 | 398 / 655 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/7` |
| `scneventsSocket` | 375 | 378 / 581 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/2` |
| `scneventsVFXEvent` | 102 | 378 / 580 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 37
- skeletal_animation, socket_signal: 23
- skeletal_animation, gaze, socket_signal: 20
- speech, gaze: 17
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 15
- speech, skeletal_animation, idle_animation, gaze: 15
- socket_signal: 14
- skeletal_animation, audio, vfx, socket_signal: 12
- speech, skeletal_animation, idle_animation, socket_signal: 12
- camera: 12
- speech, skeletal_animation, idle_animation: 8
- skeletal_animation, gaze, vfx, socket_signal: 8
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 7
- skeletal_animation: 7
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 6
- speech, idle_animation, gaze, socket_signal: 6
- skeletal_animation, gaze: 6
- skeletal_animation, vfx, socket_signal: 5
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- skeletal_animation, idle_animation, gaze, socket_signal: 5
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- speech, skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 4
- speech, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, idle_animation, socket_signal: 4
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, socket_signal: 4
- vfx, socket_signal: 4
- speech, idle_animation: 3
- gaze: 3
- skeletal_animation, audio: 3
- idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- idle_animation, gaze, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 2
- skeletal_animation, gaze, camera, socket_signal: 2
- skeletal_animation, gaze, camera, vfx, socket_signal: 2
- socket_signal, animation_state: 2
- skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, camera, socket_signal, animation_state: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- idle_animation, gaze: 1
- speech, gaze, socket_signal: 1

Raw SHA-256: `c350e578a2de99b730b4a64ed6310f6e37b5e214c51c6bf55ccbb9aed0ed361e`. Binary SHA-256: `bcb6a8d8d498e2c3860415b2380c757d816e873e3b500147521dc6955a796c3c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq055\scenes\mq055_02_northside.scene" --events
```

## `base\quest\minor_quests\mq055\scenes\mq055_03_japantown.scene`

2357 graph nodes, 3222 edges; 375 event-bearing sections, 2110 events; 575 screenplay lines, 147 screenplay options, 72 choice nodes.

Actors: judy (actor 0, spawnDespawn); kerry (actor 1, spawnDespawn); panam (actor 2, spawnDespawn); river (actor 3, spawnDespawn); Player (actor 4, findInContext).

Entries: `Start 0` → 1; `judy` → 4; `kerry` → 8; `panam` → 12; `Start 23` → 6254; `river` → 16; `Start 3` → 2337; `Start1` → 8822; `Start 24` → 7202; `bed_preview` → 7558; `shower_preview` → 7584; `preview_kerry_sofa` → 7663; `preview_river_sofa` → 7669; `judy_prev_first_date_entry` → 5677; `judy_prev_window_entry` → 5851; `judy_prev_1` → 5858; `judy_prev_2` → 5861; `judy_prev_3` → 5864; `judy_prev_sofa` → 5868; `judy_prev_bedroom` → 5871; `judy_prev_kitchen` → 5874; `judy_prev_shower` → 5877; `judy_prev_bed` → 5880; `preview_judy_waits` → 7996; `kerry_prev_1` → 5916; `kerry_prev_2` → 5918; `kerry_prev_3` → 5919; `kerry_prev_sofa` → 5920; `Start 18` → 5955; `panam_prev_3` → 5973; `panam_prev_bedroom` → 6122; `panam_prev_kitchen` → 6125; `cuddle_prev` → 10319.

Exits: `judy_done` → 6; `kerry_done` → 10; `panam_done` → 14; `river_done` → 18.

End nodes: 6: `<omitted>`; 10: `<omitted>`; 14: `<omitted>`; 18: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 26 | 2333 / 4387 | `/Data/RootChunk/sceneGraph/Data/graph/572/Data/events/2` |
| `scnChangeIdleAnimEvent` | 158 | 328 / 440 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/8` |
| `scnDialogLineEvent` | 318 | 328 / 439 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/7` |
| `scnGameplayTransitionEvent` | 47 | 332 / 484 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/17` |
| `scnIKEvent` | 94 | 332 / 470 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/4` |
| `scnLookAtAdvancedEvent` | 2 | 627 / 1106 | `/Data/RootChunk/sceneGraph/Data/graph/151/Data/events/5` |
| `scnLookAtEvent` | 277 | 328 / 451 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/17` |
| `scnPlaySkAnimEvent` | 477 | 307 / 368 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/0` |
| `scnPoseCorrectionEvent` | 6 | 4143 / 7484 | `/Data/RootChunk/sceneGraph/Data/graph/988/Data/events/4` |
| `scnUnmountEvent` | 47 | 332 / 483 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/16` |
| `scneventsAttachPropToPerformer` | 3 | 328 / 427 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/1` |
| `scneventsAttachPropToWorld` | 3 | 328 / 444 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/12` |
| `scneventsCameraParamsEvent` | 37 | 328 / 438 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 47 | 332 / 479 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/13` |
| `scneventsSocket` | 466 | 307 / 376 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/3` |
| `scneventsUnequipItemFromPerformer` | 1 | 6004 / 9966 | `/Data/RootChunk/sceneGraph/Data/graph/1355/Data/events/1` |
| `scneventsVFXEvent` | 101 | 307 / 374 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, socket_signal: 64
- speech: 34
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 22
- skeletal_animation, socket_signal: 20
- socket_signal: 20
- speech, gaze: 19
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 16
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 15
- skeletal_animation, gaze: 15
- speech, skeletal_animation, idle_animation: 13
- skeletal_animation, gaze, audio, vfx, socket_signal: 12
- camera: 12
- skeletal_animation: 11
- speech, skeletal_animation, idle_animation, gaze: 9
- speech, skeletal_animation, idle_animation, socket_signal: 7
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 6
- skeletal_animation, vfx, socket_signal: 5
- skeletal_animation, idle_animation, gaze, vfx, socket_signal: 5
- skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, socket_signal: 4
- vfx, socket_signal: 4
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, gaze, camera, socket_signal: 3
- speech, idle_animation, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, gaze, vfx, socket_signal: 3
- speech, idle_animation: 3
- speech, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- skeletal_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, gaze, camera, vfx, socket_signal: 2
- gaze: 2
- speech, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, audio, vfx, socket_signal: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, camera, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- skeletal_animation, idle_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, camera, socket_signal, animation_state: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 1

Raw SHA-256: `9c7df86f266a2f0d4815755737736bade914b20b003831b753ba3278557b606f`. Binary SHA-256: `399decb56dd252c8ea5e02f24163d678a397f91560fd01dfe92fde625d8d3de2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq055\scenes\mq055_03_japantown.scene" --events
```

## `base\quest\minor_quests\mq055\scenes\mq055_04_heywood.scene`

2494 graph nodes, 3862 edges; 393 event-bearing sections, 2356 events; 615 screenplay lines, 136 screenplay options, 78 choice nodes.

Actors: judy (actor 0, spawnDespawn); kerry (actor 1, spawnDespawn); panam (actor 2, spawnDespawn); river (actor 3, spawnDespawn); v_male_tpp (actor 4, spawnDespawn); v_female_tpp (actor 5, spawnDespawn); johnny_mirror (actor 6, spawnDespawn); Player (actor 7, findInContext).

Entries: `judy` → 4; `kerry` → 8; `panam` → 12; `river` → 16; `judy_pos1_light_preview` → 9665; `judy_pos2_light_preview` → 9666; `judy_pos3_light_preview` → 9668; `judy_pos4_light_preview` → 9670; `judy_pos5_light_preview` → 9672; `judy_pos6_light_preview` → 9728; `Start 5` → 14651; `kerry_pos2_light_preview` → 10554; `kerry_pos1_light_preview` → 10556; `kerry_pos3_light_preview` → 10558; `kerry_pos4_light_preview` → 10560; `kerry_pos5_light_preview` → 10562; `kerry_pos6_light_preview` → 10564; `panam_pool_light_preview` → 10631; `panam_kitchen_light_preview` → 10642; `panam_table_light_preview` → 10654; `river_bag_light_preview` → 10666; `river_kitchen_light_preview` → 10678; `Start 7` → 15619; `Start 8` → 15624; `Start 9` → 15629; `Start 10` → 15692; `Start1` → 8689.

Exits: `judy_done` → 6; `kerry_done` → 10; `panam_done` → 14; `river_done` → 18.

End nodes: 6: `<omitted>`; 10: `<omitted>`; 14: `<omitted>`; 18: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 31 | 5307 / 5984 | `/Data/RootChunk/sceneGraph/Data/graph/729/Data/events/2` |
| `scnChangeIdleAnimEvent` | 240 | 315 / 419 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/2` |
| `scnDialogLineEvent` | 346 | 315 / 429 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/9` |
| `scnGameplayTransitionEvent` | 42 | 315 / 435 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/14` |
| `scnIKEvent` | 84 | 315 / 424 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/4` |
| `scnLookAtAdvancedEvent` | 4 | 411 / 594 | `/Data/RootChunk/sceneGraph/Data/graph/78/Data/events/5` |
| `scnLookAtEvent` | 284 | 315 / 427 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/7` |
| `scnPlaySkAnimEvent` | 595 | 302 / 386 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/0` |
| `scnPoseCorrectionEvent` | 49 | 334 / 474 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/4` |
| `scnUnmountEvent` | 42 | 315 / 434 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/13` |
| `scneventsAttachPropToPerformer` | 2 | 1725 / 1657 | `/Data/RootChunk/sceneGraph/Data/graph/217/Data/events/3` |
| `scneventsAttachPropToWorld` | 2 | 1725 / 1663 | `/Data/RootChunk/sceneGraph/Data/graph/217/Data/events/9` |
| `scneventsCameraParamsEvent` | 53 | 411 / 592 | `/Data/RootChunk/sceneGraph/Data/graph/78/Data/events/3` |
| `scneventsEquipItemToPerformer` | 1 | 852 / 876 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 42 | 315 / 430 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/10` |
| `scneventsSocket` | 421 | 302 / 393 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/2` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 873 / 944 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/2` |
| `scneventsVFXEvent` | 117 | 302 / 392 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 61
- skeletal_animation, gaze, socket_signal: 28
- skeletal_animation, gaze, socket_signal, animation_state: 20
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 17
- socket_signal: 16
- skeletal_animation, gaze: 16
- speech, skeletal_animation, idle_animation, socket_signal: 16
- skeletal_animation: 13
- camera: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- speech, skeletal_animation, idle_animation, gaze: 11
- skeletal_animation, socket_signal, animation_state: 10
- skeletal_animation, socket_signal: 10
- speech, skeletal_animation, idle_animation: 9
- gaze: 8
- gaze, vfx, socket_signal: 8
- speech, gaze: 8
- speech, idle_animation, socket_signal: 7
- skeletal_animation, idle_animation, gaze, socket_signal: 6
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 6
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 6
- skeletal_animation, audio, vfx, socket_signal: 6
- skeletal_animation, gaze, camera, vfx, socket_signal: 5
- skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 5
- skeletal_animation, gaze, vfx, socket_signal: 5
- speech, skeletal_animation, socket_signal: 5
- skeletal_animation, vfx, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, idle_animation, gaze, socket_signal: 4
- speech, idle_animation: 4
- idle_animation, gaze, socket_signal: 4
- skeletal_animation, gaze, vfx, socket_signal, animation_state: 4
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- vfx, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 4
- skeletal_animation, gaze, camera, socket_signal: 3
- speech, socket_signal: 3
- speech, skeletal_animation: 3
- skeletal_animation, camera, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 2
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, animation_state: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, camera, vfx, socket_signal: 1
- gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, gaze, camera, socket_signal, animation_state: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `31d0b37d2aaa341d867cd365f21372265dea409ac008288d6a2635b505e8ad92`. Binary SHA-256: `bedd9f11f9db54f957cfa02043e85854c564fe7cef3bac44b58e0c83f8b074fc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq055\scenes\mq055_04_heywood.scene" --events
```

## `base\quest\minor_quests\mq055\scenes\mq055_05_downtown.scene`

2065 graph nodes, 2920 edges; 360 event-bearing sections, 2365 events; 510 screenplay lines, 136 screenplay options, 69 choice nodes.

Actors: judy (actor 0, spawnDespawn); kerry (actor 1, spawnDespawn); panam (actor 2, spawnDespawn); river (actor 3, spawnDespawn); johnny_mirror (actor 4, spawnDespawn); v_male_tpp (actor 5, spawnDespawn); v_female_tpp (actor 6, spawnDespawn); Player (actor 7, findInContext).

Entries: `judy` → 4; `kerry` → 8; `panam` → 12; `river` → 16; `Start4` → 5596; `Start1` → 5603; `Start2` → 5608; `river_reuse` → 12910; `Start8` → 7485; `Start10` → 11204; `Start 5` → 13245; `Start9` → 7851; `Start3` → 6644; `Start5` → 7027; `lighting_sofa` → 8844; `lighting_shower` → 8847; `lighting_mirror` → 8849; `lighting_sleep` → 8851; `lighting_window` → 8853; `lighting_greet` → 8855; `Start6` → 7043; `Start7` → 7057; `lighting_sofa_male` → 8883; `lighting_shower_male` → 8884; `lighting_mirror_male` → 8886; `lighting_sleep_male` → 8888; `lighting_window_hug_male` → 8890; `lighting_greet_male` → 8892; `DIALOGS` → 3619.

Exits: `judy_done` → 6; `kerry_done` → 10; `panam_done` → 14; `river_done` → 18.

End nodes: 6: `<omitted>`; 10: `<omitted>`; 14: `<omitted>`; 18: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 36 | 370 / 447 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/1` |
| `scnChangeIdleAnimEvent` | 250 | 1116 / 570 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/0` |
| `scnDialogLineEvent` | 353 | 1667 / 1362 | `/Data/RootChunk/sceneGraph/Data/graph/181/Data/events/0` |
| `scnGameplayTransitionEvent` | 43 | 1241 / 667 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/13` |
| `scnIKEvent` | 86 | 1241 / 656 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/3` |
| `scnLookAtAdvancedEvent` | 1 | 8406 / 9269 | `/Data/RootChunk/sceneGraph/Data/graph/1118/Data/events/5` |
| `scnLookAtEvent` | 309 | 1116 / 577 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/2` |
| `scnPlaySkAnimEvent` | 599 | 370 / 443 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/0` |
| `scnPoseCorrectionEvent` | 47 | 1116 / 579 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/4` |
| `scnUnmountEvent` | 43 | 1241 / 666 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/12` |
| `scneventsAttachPropToPerformer` | 2 | 3133 / 2651 | `/Data/RootChunk/sceneGraph/Data/graph/354/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 3133 / 2668 | `/Data/RootChunk/sceneGraph/Data/graph/354/Data/events/11` |
| `scneventsCameraParamsEvent` | 52 | 2353 / 1884 | `/Data/RootChunk/sceneGraph/Data/graph/248/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 43 | 1241 / 662 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/9` |
| `scneventsSocket` | 440 | 508 / 485 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/2` |
| `scneventsVFXEvent` | 59 | 1154 / 625 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 46
- skeletal_animation, gaze, socket_signal: 34
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 26
- skeletal_animation: 21
- skeletal_animation, gaze, socket_signal, animation_state: 20
- socket_signal: 16
- speech, gaze: 15
- speech, skeletal_animation, idle_animation, socket_signal: 14
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 13
- camera: 12
- speech, skeletal_animation, idle_animation: 11
- speech, skeletal_animation, idle_animation, gaze: 11
- skeletal_animation, socket_signal: 8
- skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, idle_animation, socket_signal: 7
- skeletal_animation, audio, socket_signal: 6
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 6
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 5
- skeletal_animation, audio, vfx, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 5
- skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 5
- skeletal_animation, audio: 4
- skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, audio, vfx, socket_signal, animation_state: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, idle_animation, gaze, vfx, socket_signal: 4
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, idle_animation, gaze, socket_signal: 3
- skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 3
- speech, skeletal_animation, gaze, camera, socket_signal, animation_state: 3
- skeletal_animation, gaze, camera, vfx, socket_signal: 3
- speech, socket_signal: 2
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 2
- speech, idle_animation: 2
- skeletal_animation, gaze, audio, socket_signal, animation_state: 2
- skeletal_animation, gaze: 2
- skeletal_animation, gaze, audio, socket_signal: 2
- skeletal_animation, camera, socket_signal: 2
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation: 1
- speech, idle_animation, gaze: 1
- gaze: 1
- skeletal_animation, camera, vfx, socket_signal: 1
- skeletal_animation, gaze, camera, socket_signal, animation_state: 1
- vfx, socket_signal: 1

Raw SHA-256: `19b8365c6ada1774ded965849701b96d45b8ada9820b1de509f627d34aabea3a`. Binary SHA-256: `0a2968eb8f9b0047fe7ec130683a265bd8e59ee2eddb4e3aaeeb84bc15149efe`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq055\scenes\mq055_05_downtown.scene" --events
```

