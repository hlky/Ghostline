# Imagine: scene presentation

Journal identity: `quests/minor_quest/mq014_zen`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq014_zen.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene`

56 graph nodes, 91 edges; 10 event-bearing sections, 17 events; 13 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: kid (actor 0, community); kid_1 (actor 1, community); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `Start1` → 327; `face preview` → 106.

Exits: `End 0` → 2; `kid_rest_01` → 321; `kid_rest_02` → 329; `kid_rest_03` → 334.

End nodes: 2: `<omitted>`; 321: `<omitted>`; 329: `<omitted>`; 334: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 14 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnLookAtEvent` | 2 | 247 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/1` |
| `scnPlaySkAnimEvent` | 12 | 14 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 6
- skeletal_animation, idle_animation: 2
- idle_animation, gaze: 1
- gaze: 1

Raw SHA-256: `15036dfa94b0097c9578495d471fb4b4423026a8fdc102b1b568df7abaa3d8ab`. Binary SHA-256: `f62fa5d4520ec997cde555648a0a1e15bb236bbecca552f58acec8ec3a03ba5a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\mini_world_stories\heywood\mws_hey_01\scenes\mws_hey_01_follow.scene" --events
```

## `base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene`

121 graph nodes, 150 edges; 31 event-bearing sections, 128 events; 53 screenplay lines, 11 screenplay options, 6 choice nodes.

Actors: Master (actor 0, community); Player (actor 1, findInContext).

Entries: `first_talk_in` → 7; `after_in` → 48; `Start 6` → 314; `Start 7` → 316.

Exits: `first_talk_out` → 8; `after_out` → 49.

End nodes: 8: `<omitted>`; 49: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 9 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 42 | 4 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnLookAtEvent` | 37 | 9 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 11 | 9 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsAttachPropToPerformer` | 4 | 258 / 374 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 74 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scneventsCameraParamsEvent` | 3 | 1712 / 567 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/0` |
| `scneventsSocket` | 12 | 9 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/12` |
| `scneventsVFXEvent` | 7 | 25 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 5
- speech, gaze: 4
- speech: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- camera: 3
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- vfx: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, vfx: 1
- speech, skeletal_animation, props_equipment: 1
- skeletal_animation: 1
- props_equipment, socket_signal: 1
- idle_animation, socket_signal: 1

Raw SHA-256: `48646faf46e0dfd0f52d9c03cc96a389040207d9a9d6cd799587db954d433e78`. Binary SHA-256: `16cf500f84d982903b3acbc5a2c3f289175933f74975b48a5097db5785caf301`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene" --events
```

## `base\quest\minor_quests\mq014\scenes\mq014_02_earth.scene`

27 graph nodes, 26 edges; 4 event-bearing sections, 17 events; 12 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Master (actor 0, community); Player (actor 1, findInContext).

Entries: `earth_in` → 1.

Exits: `earth_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 11 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraParamsEvent` | 3 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 2 | 87 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scneventsVFXEvent` | 1 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, camera, vfx: 1
- camera, socket_signal: 1
- socket_signal: 1
- camera: 1

Raw SHA-256: `5b037841fbfb9baec7b7214a23fbe5e4a535d1262f8fa7051ce9d44df19ecc2a`. Binary SHA-256: `c2115c46ee2c90bbac1535fb4327bd20e091368d33a0c1ad6c51bb2c9ad203ab`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq014\scenes\mq014_02_earth.scene" --events
```

## `base\quest\minor_quests\mq014\scenes\mq014_03_second.scene`

107 graph nodes, 120 edges; 26 event-bearing sections, 99 events; 33 screenplay lines, 7 screenplay options, 4 choice nodes.

Actors: Master (actor 0, community); Player (actor 1, findInContext).

Entries: `second_in` → 1; `Start 2` → 1739; `chicken_second_in` → 148; `after_in` → 62.

Exits: `second_out` → 2; `after_out` → 63.

End nodes: 2: `<omitted>`; 63: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 21 | 5 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 66 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/5` |
| `scnIKEvent` | 2 | 66 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnLookAtEvent` | 20 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 13 | 9 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 1 | 66 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/9` |
| `scneventsAttachPropToPerformer` | 4 | 200 / 314 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 66 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scneventsCameraParamsEvent` | 3 | 1641 / 514 | `/Data/RootChunk/sceneGraph/Data/graph/80/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 66 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/6` |
| `scneventsSocket` | 18 | 5 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsVFXEvent` | 7 | 23 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- camera: 3
- speech, skeletal_animation, socket_signal: 2
- vfx: 2
- gaze: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech: 1
- speech, vfx: 1
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze: 1
- props_equipment, socket_signal: 1
- idle_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `9f5a1bd1602981ffd92695ff5d6f28d762a4d5997596e94e28327c028021468d`. Binary SHA-256: `87f8155db2123e2d6cf982b273d1343fc058608b9a782f71e61c3420578eb018`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq014\scenes\mq014_03_second.scene" --events
```

## `base\quest\minor_quests\mq014\scenes\mq014_04_water.scene`

30 graph nodes, 29 edges; 4 event-bearing sections, 19 events; 14 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Master (actor 0, community); Player (actor 1, findInContext).

Entries: `water_in` → 1.

Exits: `water_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 11 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 63 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scneventsCameraParamsEvent` | 3 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 3 | 63 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/2` |
| `scneventsVFXEvent` | 1 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, camera, vfx: 1
- skeletal_animation, camera, socket_signal: 1
- socket_signal: 1
- camera: 1

Raw SHA-256: `4ff8253cce4cbc32e2fda68bf1b5090564f11a2485af751053aa0193028090fd`. Binary SHA-256: `46115e15c9f65e5db1abd0f0913de0c1f90de0a1b87d3ad88dd030c5818e83c2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq014\scenes\mq014_04_water.scene" --events
```

## `base\quest\minor_quests\mq014\scenes\mq014_05_third.scene`

109 graph nodes, 128 edges; 29 event-bearing sections, 101 events; 37 screenplay lines, 7 screenplay options, 4 choice nodes.

Actors: Master (actor 0, community); Player (actor 1, findInContext).

Entries: `third_in` → 4; `thirdhook_in` → 45; `after_in` → 72.

Exits: `third_out` → 5; `after_out` → 73.

End nodes: 5: `<omitted>`; 73: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 8 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnDialogLineEvent` | 23 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 75 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/5` |
| `scnIKEvent` | 2 | 75 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/2` |
| `scnLookAtEvent` | 17 | 8 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 13 | 8 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnUnmountEvent` | 1 | 75 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/9` |
| `scneventsAttachPropToPerformer` | 4 | 211 / 295 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 75 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/0` |
| `scneventsCameraParamsEvent` | 3 | 1614 / 479 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 75 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/6` |
| `scneventsSocket` | 20 | 14 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scneventsVFXEvent` | 7 | 15 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 3
- skeletal_animation, socket_signal: 3
- camera: 3
- speech: 2
- speech, idle_animation, gaze: 2
- socket_signal: 2
- vfx: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, socket_signal: 1
- speech, vfx, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- gaze: 1
- skeletal_animation: 1

Raw SHA-256: `852f80c78af9b4382122318d8c815f51c87bff915882d151f1cc06c2ac35c186`. Binary SHA-256: `0897474319e46ae24dba779c5b9bbc2d768034b48c2fd15a76562a34c8481bc3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq014\scenes\mq014_05_third.scene" --events
```

## `base\quest\minor_quests\mq014\scenes\mq014_06_fire.scene`

26 graph nodes, 25 edges; 3 event-bearing sections, 20 events; 14 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Master (actor 0, community); Player (actor 1, findInContext).

Entries: `fire_in` → 4.

Exits: `fire_out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 13 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 83 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scneventsCameraParamsEvent` | 3 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 2 | 83 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scneventsVFXEvent` | 1 | 6 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, camera, vfx: 1
- skeletal_animation, camera, socket_signal: 1
- camera: 1

Raw SHA-256: `e3b2549cef32f825d944c8d038ca2c519224ac5a4edc74e46fa09ca89fe27584`. Binary SHA-256: `73022a23690109bba8cc9911b7e7288d7573677a205d8ae1b5c58be90fd75397`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq014\scenes\mq014_06_fire.scene" --events
```

## `base\quest\minor_quests\mq014\scenes\mq014_07_fourth.scene`

106 graph nodes, 133 edges; 27 event-bearing sections, 109 events; 39 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: Master (actor 0, community); Johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `fourth_in` → 4; `fourthhook_in` → 23; `after_in` → 62; `Start 1` → 291.

Exits: `fourth_out` → 5; `after_out` → 63.

End nodes: 5: `<omitted>`; 63: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 9 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |
| `scnDialogLineEvent` | 33 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 65 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/4` |
| `scnIKEvent` | 2 | 65 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/1` |
| `scnLookAtEvent` | 22 | 8 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 13 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 1 | 65 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/8` |
| `scneventsAttachPropToPerformer` | 4 | 229 / 364 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/1` |
| `scneventsAttachPropToWorld` | 1 | 447 / 492 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/3` |
| `scneventsCameraParamsEvent` | 3 | 1601 / 547 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 65 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/5` |
| `scneventsSocket` | 17 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsVFXEvent` | 7 | 15 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 3
- camera: 3
- speech, skeletal_animation: 2
- socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, gaze, vfx: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze: 1
- speech, idle_animation: 1
- skeletal_animation, socket_signal: 1
- props_equipment, socket_signal: 1
- vfx: 1
- vfx, socket_signal: 1

Raw SHA-256: `2a814b00c246e40bf4e500cbbc358adf651272f37c59c7f895d8a4bd2c5e6a5b`. Binary SHA-256: `5334fa912ae7801488b0f2302b7711ab08747d2bd21f4cb16ef704f4cf2eaad5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq014\scenes\mq014_07_fourth.scene" --events
```

## `base\quest\minor_quests\mq014\scenes\mq014_08_air.scene`

30 graph nodes, 27 edges; 4 event-bearing sections, 18 events; 15 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Master (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 150; `air_in` → 4; `Start1` → 166.

Exits: `air_out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 12 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraParamsEvent` | 3 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 2 | 78 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |
| `scneventsVFXEvent` | 1 | 6 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, camera, vfx: 1
- camera, socket_signal: 1
- socket_signal: 1
- camera: 1

Raw SHA-256: `b7ec793ba7e329027bb4aa4317a83d5574fe3c4e27c21156dc9458b2424379a8`. Binary SHA-256: `eed58b7f078cdbdf4914420aeb6ef33a996ff33e6757747ffd298055c6d4b048`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq014\scenes\mq014_08_air.scene" --events
```

