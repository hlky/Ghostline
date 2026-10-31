# Gig: Cuckoo's Nest: scene presentation

Journal identity: `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_02`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_std_rcr_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_chats.scene`

15 graph nodes, 14 edges; 3 event-bearing sections, 11 events; 10 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: enemy_002 (actor 0, community); enemy_003 (actor 1, community); enemy_004 (actor 2, community); enemy_001 (actor 3, community); enemy_005 (actor 4, community); doctor_001 (actor 5, community); doctor_002 (actor 6, community); dixon (actor 7, community); Player (actor 8, findInContext).

Entries: `hall_talk` → 4; `Start1` → 37; `upper` → 7; `window` → 12.

Exits: `hall_talk_o` → 6; `upper_o` → 8; `End 1` → 42; `window_o` → 14.

End nodes: 6: `<omitted>`; 8: `<omitted>`; 14: `<omitted>`; 42: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 9 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnDialogLineEvent` | 10 | 5 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, idle_animation: 1

Raw SHA-256: `6434e2f25284c6b1cc439dd679880fa9383183b854955e6bbdc131de237e5c2b`. Binary SHA-256: `b0870929f0ac3e6072520e594d210372a46d8a5863a414487420939979d51c7d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_chats.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_dixon.scene`

48 graph nodes, 53 edges; 14 event-bearing sections, 60 events; 22 screenplay lines, 5 screenplay options, 3 choice nodes.

Actors: dixon (actor 0, community); enemy_005 (actor 1, community); fixer (actor 2, community); Player (actor 3, findInContext).

Entries: `Start 1` → 130; `dixon` → 4; `Start 2` → 266; `Start 3` → 278; `at escape car` → 293.

Exits: `End 2` → 132.

End nodes: 132: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 10 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 14 | 10 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 232 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/11` |
| `scnIKEvent` | 2 | 232 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/5` |
| `scnLookAtEvent` | 13 | 13 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 2 | 232 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/3` |
| `scnUnmountEvent` | 1 | 232 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 1 | 232 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/9` |
| `scneventsSocket` | 10 | 13 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation: 1
- socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `b94ddbaaf7150f0d346828c83ffa99a277298b82ea96f1f0d2191a103cbc1b33`. Binary SHA-256: `3c325491ddb2700bc9c6a61348482eddecd108b9e86df1a29783c6d6d831d13b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_dixon.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_holocall_debriefs.scene`

25 graph nodes, 33 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 285.

End nodes: 2: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `89be2fce7899b1c9042bb7ee5111d0b8e20b797f61032200d6735cb33f088d7d`. Binary SHA-256: `bb7288919def53078727e7e172965101b32fdbecb72ac9324dedc1772b15a523`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 29 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `9d98b84a82fdd61f8419ce880fd1236c5d687767ac7ba4025c218308942b3158`. Binary SHA-256: `9cd475980cc4e7447cef469b63db28456e561e3443b2c7bda2fb03f23ecbcac9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_johnny.scene`

13 graph nodes, 14 edges; 2 event-bearing sections, 21 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 5 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 7 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 3 | 4 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze: 1

Raw SHA-256: `a917dd544cfab5911bc1d80402b116dc1011b16e73e7456a4951bed88cbc530d`. Binary SHA-256: `f533e8936e555b2f67730e11ca8d022641339bc0e7aa2ee00fe7d5a4610ac4bc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_johnny.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_reception.scene`

36 graph nodes, 44 edges; 7 event-bearing sections, 58 events; 40 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: receptionist (actor 0, community); dixon (actor 1, community); doctor_003 (actor 2, community); player (actor 3, findInContext).

Entries: `reception` → 1; `pickup shard` → 4685; `Start1` → 273.

Exits: `reception_o` → 2; `reception_end` → 4692; `End1` → 275.

End nodes: 2: `<omitted>`; 275: `<omitted>`; 4692: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 15 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnLookAtEvent` | 11 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 7 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 14 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 2 | 9 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech: 1
- idle_animation, gaze, socket_signal: 1
- gaze: 1

Raw SHA-256: `6690f725637ea8a367a97e0079241493d3e764683852e001dcce70d16bd00c6a`. Binary SHA-256: `825f2a81bb46825071ab00f74461b7d987ec7657db6c26f6b0ab311864a9eadd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_reception.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_wheelchair.scene`

38 graph nodes, 46 edges; 5 event-bearing sections, 19 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: doctor_003 (actor 0, community); patient_001 (actor 1, community); wheelchair (actor 2, community); receptionist (actor 3, community).

Entries: `rcr_02_wheelchair` → 4; `Combat` → 260.

Exits: `End 0` → 44; `End 1` → 257.

End nodes: 44: `<omitted>`; 257: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 49 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 3 | 49 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnLookAtEvent` | 3 | 49 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 6 | 49 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSocket` | 1 | 148 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `d22e49ca2209c33a877c8bf20445aa450f9668c4f4905a6b787437fd11126ec9`. Binary SHA-256: `9fe6d0010ea2062b17108ce0a5b6b279d4726eef06d65cac8588db0491555c82`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_02\scenes\sts_std_rcr_02_wheelchair.scene" --events
```

