# Get It Together: scene presentation

Journal identity: `ep1/quests/main_quest/q303_hands`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q303_hands.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

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

## `ep1\quest\main_quests\q303\scenes\q303_04_mr_hands.scene`

301 graph nodes, 394 edges; 55 event-bearing sections, 665 events; 118 screenplay lines, 22 screenplay options, 12 choice nodes.

Actors: Mr_Hands (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start0` → 1; `cinedebug_mrhands` → 1665; `cinedebug_handstalk` → 1685; `Start 7` → 4036; `Start 8` → 4117; `Start 9` → 4132.

Exits: `out_clean_up` → 780.

End nodes: 780: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 3370 / 1131 | `/Data/RootChunk/sceneGraph/Data/graph/96/Data/events/3` |
| `scnChangeIdleAnimEvent` | 26 | 383 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnDialogLineEvent` | 98 | 207 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 2987 / 761 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/6` |
| `scnIKEvent` | 4 | 2987 / 755 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/2` |
| `scnLookAtAdvancedEvent` | 4 | 1527 / 154 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |
| `scnLookAtEvent` | 133 | 383 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 212 | 383 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPoseCorrectionEvent` | 1 | 2483 / 493 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/16` |
| `scnUnmountEvent` | 2 | 2987 / 769 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/11` |
| `scneventsAttachPropToNode` | 1 | 4593 / 2448 | `/Data/RootChunk/sceneGraph/Data/graph/272/Data/events/0` |
| `scneventsAttachPropToPerformer` | 25 | 383 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scneventsAttachPropToWorld` | 17 | 1527 / 163 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/10` |
| `scneventsEquipItemToPerformer` | 1 | 3375 / 1135 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 2 | 2987 / 765 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/8` |
| `scneventsSocket` | 105 | 207 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 1 | 3375 / 1144 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/4` |
| `scneventsVFXDurationEvent` | 5 | 2393 / 377 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/11` |
| `scneventsVFXEvent` | 23 | 1565 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 5
- speech: 4
- skeletal_animation: 4
- skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- skeletal_animation, props_equipment, vfx, socket_signal: 2
- skeletal_animation, audio, socket_signal: 2
- gaze: 2
- skeletal_animation, gaze: 2
- skeletal_animation, socket_signal: 2
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- props_equipment: 1
- idle_animation: 1

Raw SHA-256: `72c2c87fc115c82452a7d0cb8b910efde3b4b4ff631db918225b9dfe494aafbf`. Binary SHA-256: `f4a684feac94901866ddee9b07d54b2e7c3b21abf0450d73fed7a69f0fb91f3a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_04_mr_hands.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_04a_call_reed.scene`

14 graph nodes, 13 edges; 2 event-bearing sections, 13 events; 6 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Reed (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 27 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnDialogLineEvent` | 6 | 27 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnPlaySkAnimEvent` | 6 | 27 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation: 1

Raw SHA-256: `60d5715282aa984e13df9ddaaaa93257e391e16a8d3b2c8711d14099034da0b7`. Binary SHA-256: `270642efb078af11e303b1f7dd818125bca6d371c5cecfded548405faadd5850`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_04a_call_reed.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_04b_call_hands.scene`

38 graph nodes, 45 edges; 12 event-bearing sections, 77 events; 40 screenplay lines, 5 screenplay options, 3 choice nodes.

Actors: hands (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start1` → 4; `Start_from_debrief` → 223.

Exits: `End1` → 18.

End nodes: 18: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 40 | 33 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnPlaySkAnimEvent` | 37 | 33 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 12

Raw SHA-256: `f35f3e2905e5559e7ba39b65cb0671d074d22a160de6eaabf081e2a40929f2e3`. Binary SHA-256: `0d8bd41742897faf2bca5118f0606c333cdfee8b2b6bc05b950023fb654440f4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_04b_call_hands.scene" --events
```

## `ep1\quest\main_quests\q303\scenes\q303_05_safehouse.scene`

629 graph nodes, 725 edges; 109 event-bearing sections, 1011 events; 238 screenplay lines, 37 screenplay options, 15 choice nodes.

Actors: Reed (actor 0, spawnSet); Alex (actor 1, spawnSet); Droid (actor 2, community); Player (actor 3, findInContext).

Entries: `preview_full` → 6138; `start` → 3721; `Start 5` → 6201; `Start 6` → 6289; `door_idle` → 8751; `Start 8` → 8173; `Start 11` → 8866; `Start 7` → 6438; `Start1` → 5409; `dbg_safehouse` → 5411; `intro_wait` → 6661.

Exits: `out` → 2; `intro_wait_out` → 6710.

End nodes: 2: `NonTerminating`; 6710: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 67 | 2470 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/8` |
| `scnChangeIdleAnimEvent` | 48 | 2320 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnDialogLineEvent` | 166 | 2320 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnGameplayTransitionEvent` | 11 | 2351 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/15` |
| `scnIKEvent` | 22 | 2351 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/8` |
| `scnLookAtAdvancedEvent` | 8 | 4298 / 848 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/6` |
| `scnLookAtEvent` | 199 | 2320 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnPlaySkAnimEvent` | 212 | 2320 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnPoseCorrectionEvent` | 25 | 2351 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/10` |
| `scnUnmountEvent` | 11 | 2351 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/14` |
| `scneventsAttachPropToNode` | 1 | 2470 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/21` |
| `scneventsAttachPropToPerformer` | 2 | 2470 / 156 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/6` |
| `scneventsAttachPropToWorld` | 1 | 2470 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/7` |
| `scneventsCameraParamsEvent` | 4 | 6257 / 2156 | `/Data/RootChunk/sceneGraph/Data/graph/206/Data/events/29` |
| `scneventsEquipItemToPerformer` | 4 | 8849 / 4330 | `/Data/RootChunk/sceneGraph/Data/graph/562/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 11 | 2351 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/11` |
| `scneventsSocket` | 188 | 2320 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 1 | 8849 / 4332 | `/Data/RootChunk/sceneGraph/Data/graph/562/Data/events/5` |
| `scneventsVFXDurationEvent` | 7 | 4592 / 1188 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/5` |
| `scneventsVFXEvent` | 23 | 2971 / 307 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 13
- speech, skeletal_animation, gaze, socket_signal: 12
- speech: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- speech, gaze, socket_signal: 5
- speech, skeletal_animation, gaze: 5
- skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze, vfx, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal, animation_state: 3
- vfx: 3
- gaze: 3
- skeletal_animation, gaze, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 1
- vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, gaze: 1
- skeletal_animation, audio, socket_signal: 1
- camera: 1
- skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 1
- socket_signal: 1
- idle_animation: 1
- idle_animation, audio: 1
- skeletal_animation, gaze: 1
- gaze, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `5e9df7088cc1d1b3e4ea59eccd5b108b1a00cd6b52db6310d0adc02515bc0bee`. Binary SHA-256: `6171834570a03bd1f555a8c1227044a9845bc2dcdda1547077bc5f81ea6633cf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q303\scenes\q303_05_safehouse.scene" --events
```

