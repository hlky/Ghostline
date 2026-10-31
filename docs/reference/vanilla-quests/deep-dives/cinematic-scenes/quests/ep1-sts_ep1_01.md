# Gig: Dogtown Saints: scene presentation

Journal identity: `ep1/quests/street_stories/sts_ep1_01`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-sts_ep1_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_anderson_saved.scene`

212 graph nodes, 242 edges; 42 event-bearing sections, 258 events; 76 screenplay lines, 17 screenplay options, 5 choice nodes.

Actors: anderson (actor 0, community); Player (actor 1, findInContext).

Entries: `combat` → 1; `nika_alive` → 75; `backup2` → 982; `default_talk` → 721; `backup` → 876; `secret` → 297.

Exits: `secret_out` → 303; `scavs_dead` → 2; `clear` → 476; `nika_alive_end` → 196; `scavs_alive` → 72; `default_talk_end` → 723.

End nodes: 2: `NonTerminating`; 72: `NonTerminating`; 196: `NonTerminating`; 303: `<omitted>`; 476: `NonTerminating`; 723: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 38 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnChangeIdleAnimEvent` | 8 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 60 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 535 / 527 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/10` |
| `scnIKEvent` | 4 | 535 / 519 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/3` |
| `scnLookAtAdvancedEvent` | 1 | 293 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/5` |
| `scnLookAtEvent` | 25 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 61 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 2 | 535 / 526 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/9` |
| `scneventsEquipItemToPerformer` | 5 | 329 / 418 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 2 | 535 / 522 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/6` |
| `scneventsSocket` | 87 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 18
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation: 1
- speech: 1
- props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- idle_animation: 1

Raw SHA-256: `daf22aae2daa2719ee30700884dca2a5fe32b6815446566f6727380aaad3962d`. Binary SHA-256: `695e0f4f8ad625753326df3c9e34c50fee6a7925b2b8f19fff8547f91d8ff698`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_anderson_saved.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_final.scene`

354 graph nodes, 539 edges; 53 event-bearing sections, 414 events; 111 screenplay lines, 19 screenplay options, 13 choice nodes.

Actors: anderson (actor 0, community); nika (actor 1, community); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `Start 2` → 728; `Start 4` → 1139; `Start 1` → 531; `Start 6` → 1701; `PUC` → 1034; `Start 5` → 1425.

Exits: `clear` → 715; `failed` → 117; `combat` → 118; `nika_alive` → 120.

End nodes: 117: `NonTerminating`; 118: `NonTerminating`; 120: `NonTerminating`; 715: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 357 / 434 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/4` |
| `scnChangeIdleAnimEvent` | 32 | 41 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnDialogLineEvent` | 83 | 22 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtAdvancedEvent` | 13 | 41 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/13` |
| `scnLookAtEvent` | 84 | 41 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnPlaySkAnimEvent` | 81 | 41 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnPoseCorrectionEvent` | 4 | 41 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scneventsAttachPropToPerformer` | 4 | 410 / 525 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/1` |
| `scneventsAttachPropToWorld` | 3 | 460 / 593 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/13` |
| `scneventsCameraParamsEvent` | 1 | 1165 / 1182 | `/Data/RootChunk/sceneGraph/Data/graph/166/Data/events/1` |
| `scneventsSocket` | 104 | 41 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/9` |
| `scneventsVFXEvent` | 4 | 460 / 591 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, gaze, socket_signal: 7
- speech: 6
- speech, gaze, socket_signal: 3
- speech, gaze: 3
- idle_animation: 3
- speech, skeletal_animation, gaze: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 2
- socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- idle_animation, socket_signal: 1
- gaze: 1
- idle_animation, camera: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `7e327cdb556c4c888b5d15be31c93e59a035a0c88ca96b8a958d9684901569e2`. Binary SHA-256: `7031d288ad10e730d003c23d99935c9620027f6aa874a99d9b296f50e8991386`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_final.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_holocall_debrief.scene`

34 graph nodes, 40 edges; 5 event-bearing sections, 9 events; 9 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `not_rejectable_q303_start` → 164.

Exits: `End 0` → 2; `rejected_out` → 116; `not_rejectable_q303_end` → 166.

End nodes: 2: `<omitted>`; 116: `<omitted>`; 166: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 9 | 20 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5

Raw SHA-256: `63373233844a94640fd755015a922aef0838a6a65047fde0e75cf9fe662886ab`. Binary SHA-256: `c03d33568c5b212be1fbca5e002498907a477ca1050874949c6958917baef2eb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_holocall_debrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_holocall_prebrief.scene`

29 graph nodes, 35 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 162.

End nodes: 2: `<omitted>`; 162: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 101 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `525a9328dd78c5b461e9ee28c67b1e75235dc780cba1d34322119d2f19728e0e`. Binary SHA-256: `3a479ea66e7cc2a763bf65838d7dc178048e7ab556785feb2af592e474104772`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_holocall_prebrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_nika_alive.scene`

55 graph nodes, 60 edges; 13 event-bearing sections, 107 events; 22 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: nika (actor 0, community); johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `anderson_alive` → 1; `Start 2` → 237; `body_found` → 62.

Exits: `End 0` → 2; `End 1` → 195.

End nodes: 2: `NonTerminating`; 195: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 5 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 16 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 98 / 160 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/7` |
| `scnIKEvent` | 4 | 98 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/4` |
| `scnLookAtEvent` | 22 | 5 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnOverridePhantomParamsEvent` | 1 | 98 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scnPlaySkAnimEvent` | 24 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 2 | 98 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 2 | 98 / 154 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/2` |
| `scneventsSocket` | 26 | 5 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 1 | 98 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- idle_animation, socket_signal: 2
- speech, gaze, socket_signal: 1
- ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1
- skeletal_animation: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `053a59f48d0bdb68fbca04941b42e0812202ae775f235b21efa8a31a2ecdb8ba`. Binary SHA-256: `57720be7abfa4ba692ae1df85d74d8cfbedd0a1cc8a6d60cdef387cf521d1dfe`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_nika_alive.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_odel.scene`

268 graph nodes, 344 edges; 53 event-bearing sections, 359 events; 106 screenplay lines, 24 screenplay options, 11 choice nodes.

Actors: odel (actor 0, community); patient_01 (actor 1, community); patient_02 (actor 2, community); Player (actor 3, findInContext).

Entries: `brief` → 1; `failed` → 70; `finished` → 77; `default_talk` → 1261.

Exits: `End 0` → 2; `failed_out` → 75; `finished_out` → 82; `kill_scene` → 817; `default_talk_end` → 1265; `terminate` → 1079; `patient_chat_end` → 208.

End nodes: 2: `NonTerminating`; 75: `NonTerminating`; 82: `NonTerminating`; 208: `NonTerminating`; 817: `<omitted>`; 1079: `<omitted>`; 1265: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 22 | 23 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scnDialogLineEvent` | 83 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 50 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/19` |
| `scnIKEvent` | 4 | 50 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |
| `scnLookAtEvent` | 75 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 91 | 23 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnUnmountEvent` | 2 | 50 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/18` |
| `scneventsEquipItemToPerformer` | 1 | 1575 / 1482 | `/Data/RootChunk/sceneGraph/Data/graph/212/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 2 | 50 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/15` |
| `scneventsSocket` | 77 | 23 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, skeletal_animation, gaze, socket_signal: 7
- gaze: 7
- speech, skeletal_animation, socket_signal: 6
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation: 2
- speech: 2
- skeletal_animation, gaze, socket_signal: 2
- gaze, socket_signal: 2
- socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation: 2
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1

Raw SHA-256: `86a9418a5220c2c945d908a0a29138187f798f0c783a31cf5aa47ef8b30d606c`. Binary SHA-256: `6016f081dbc611218321d8f27cf4d1385b698c3cf293178a94ce93c2e994ffba`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_odel.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_scavs_checking_basement.scene`

5 graph nodes, 6 edges; 1 event-bearing sections, 1 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: enemy_01 (actor 0, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 12 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `2b800d8d70721bdb29d66522cb6709c1425e7009a70929196452d5dd5b38ed8e`. Binary SHA-256: `db9f8d6b31fe60b3de449ff0fee7cc2af0069e0bde1c5e2099f46b07314ad611`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_01\scenes\sts_ep1_01_scavs_checking_basement.scene" --events
```

