# Happy Together: scene presentation

Journal identity: `quests/minor_quest/mq010_barry`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq010_barry.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene`

148 graph nodes, 178 edges; 22 event-bearing sections, 203 events; 46 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: policeman (actor 0, community); policewoman (actor 1, community); barry (actor 2, community); Player (actor 3, findInContext).

Entries: `mq010_01_cops_start` → 1; `mq010_01_cops_and_v_start` → 544.

Exits: `mq010_01_cops_and_v_end` → 2; `combat` → 611; `mq010_01_cops_end` → 542.

End nodes: 2: `<omitted>`; 542: `NonTerminating`; 611: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 40 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 33 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 9 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/13` |
| `scnIKEvent` | 4 | 9 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnLookAtEvent` | 42 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 33 | 3 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |
| `scnPoseCorrectionEvent` | 1 | 591 / 399 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/1` |
| `scnUnmountEvent` | 2 | 9 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 2 | 9 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsSocket` | 44 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- skeletal_animation: 6
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `73ff39bcfd01e0d3c0bda35b7b9daa89b843961451b9b9758c1ab2998f090077`. Binary SHA-256: `d0cccee98a116651d3080f786ec230fb8508c95a1cf6342d73802029b73ee8ca`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene" --events
```

## `base\quest\minor_quests\mq010\scenes\mq010_02_barry_talk.scene`

192 graph nodes, 231 edges; 34 event-bearing sections, 254 events; 96 screenplay lines, 19 screenplay options, 11 choice nodes.

Actors: barry (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `knock_on_door_in` → 84.

Exits: `End 0` → 2; `barry_tier` → 481; `door_locked_out` → 491; `knock_on_door_out` → 144.

End nodes: 2: `NonTerminating`; 144: `<omitted>`; 481: `NonTerminating`; 491: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 53 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnDialogLineEvent` | 76 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 265 / 491 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/9` |
| `scnIKEvent` | 6 | 265 / 482 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/1` |
| `scnLookAtEvent` | 19 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnPlaySkAnimEvent` | 52 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPoseCorrectionEvent` | 9 | 6 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scnUnmountEvent` | 3 | 265 / 490 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/8` |
| `scneventsCameraParamsEvent` | 2 | 265 / 485 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 3 | 265 / 488 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/7` |
| `scneventsSocket` | 28 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, skeletal_animation, idle_animation: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, idle_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, animation_state: 1
- skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation: 1
- idle_animation: 1
- skeletal_animation, camera, socket_signal: 1

Raw SHA-256: `a2551e21e2259ae0573c10ee77b674526b962641642c335dc3f73bcff4b20dad`. Binary SHA-256: `8e4dc3981d6c001999fd894e9eabc4890d9d5cef6827aad3ff876299cc215b9e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq010\scenes\mq010_02_barry_talk.scene" --events
```

## `base\quest\minor_quests\mq010\scenes\mq010_03_columbarium.scene`

99 graph nodes, 122 edges; 17 event-bearing sections, 75 events; 30 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `cinedebug_Johnnyinterrupt_` → 484; `johnny` → 248.

Exits: `End 0` → 2; `End 1` → 54.

End nodes: 2: `NonTerminating`; 54: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 23 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 20 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 9 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 13 | 31 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scneventsSocket` | 6 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsVFXEvent` | 4 | 149 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 5
- speech, idle_animation: 3
- speech, skeletal_animation, idle_animation: 2
- skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- idle_animation, gaze, socket_signal: 1

Raw SHA-256: `4f3c255eaeccb71cce07867eddcd4a8659fac7bde14eeb7471b955071b8ce9f5`. Binary SHA-256: `b03b07be5ac9c1de40de1714336b1354f46a615854ec9f0548d15925eaf5f26e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq010\scenes\mq010_03_columbarium.scene" --events
```

## `base\quest\minor_quests\mq010\scenes\mq010_04_police_talk.scene`

184 graph nodes, 220 edges; 25 event-bearing sections, 249 events; 47 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: policeman (actor 0, community); policewoman (actor 1, community); Player (actor 2, findInContext).

Entries: `mq010_04_ask_about_barry_start` → 1; `mq010_04_police_talk_start` → 212; `mq010_04_mendez_ws_start` → 429.

Exits: `mq010_04_police_talk_end_non_terminating` → 2; `mq010_04_ask_about_barry_end` → 206; `combat` → 657; `mq010_04_police_talk_end_terminating` → 121; `mq010_04_mendez_ws_end` → 439.

End nodes: 2: `NonTerminating`; 121: `<omitted>`; 206: `NonTerminating`; 439: `NonTerminating`; 657: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 48 | 9 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 30 | 9 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnGameplayTransitionEvent` | 2 | 407 / 466 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/16` |
| `scnIKEvent` | 4 | 407 / 446 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/1` |
| `scnLookAtEvent` | 51 | 9 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 44 | 9 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnPoseCorrectionEvent` | 8 | 9 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scnUnmountEvent` | 2 | 407 / 465 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/15` |
| `scneventsEquipItemToPerformer` | 1 | 550 / 584 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 2 | 407 / 461 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/12` |
| `scneventsSocket` | 49 | 9 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/11` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 53 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scneventsVFXEvent` | 6 | 55 / 146 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/26` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 6
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 3
- speech: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- socket_signal: 1
- idle_animation, gaze, socket_signal: 1

Raw SHA-256: `0d69942ec288f1e30f0ae51ec0b0a375dd4bab1d175265c724d8879c6a0fad72`. Binary SHA-256: `810d19e14bbfda0f817689fb7990a51993e17fa01d09b5013ddcd8b7f04f922b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq010\scenes\mq010_04_police_talk.scene" --events
```

## `base\quest\minor_quests\mq010\scenes\mq010_05_barry_shot.scene`

56 graph nodes, 57 edges; 4 event-bearing sections, 102 events; 13 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: barry (actor 0, community); policewoman (actor 1, community); policeman (actor 2, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `combat` → 342.

End nodes: 2: `<omitted>`; 342: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 14 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnChangeIdleAnimEvent` | 17 | 11 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 11 | 11 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnGameplayTransitionEvent` | 2 | 54 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/25` |
| `scnIKEvent` | 4 | 54 / 186 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/11` |
| `scnLookAtEvent` | 14 | 11 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 24 | 11 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnPoseCorrectionEvent` | 3 | 14 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnUnmountEvent` | 2 | 54 / 209 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/24` |
| `scneventsSetAnimFeatureEvent` | 2 | 54 / 205 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/21` |
| `scneventsSocket` | 18 | 11 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1

Raw SHA-256: `074527146b33f51b60a51b992badca2c9a88f276c4d590b8655f98c71657b7de`. Binary SHA-256: `816d2c6ebd4a775e6bb9579778a75dc13859cee62b1031243739530454763706`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq010\scenes\mq010_05_barry_shot.scene" --events
```

