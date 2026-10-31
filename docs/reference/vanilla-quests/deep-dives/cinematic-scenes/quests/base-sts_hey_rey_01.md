# Gig: Bring Me the Head of Gustavo Orta: scene presentation

Journal identity: `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_01`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_hey_rey_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\scenes\sts_hey_rey_01_03_gustavo.scene`

36 graph nodes, 39 edges; 11 event-bearing sections, 76 events; 36 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: gustavo (actor 0, community); Nolan (actor 1, findInContext); V (actor 2, findInContext).

Entries: `rey_01_gustavo_start` → 1; `Start 1` → 282.

Exits: `rey_01_gustavo_kill_end` → 37; `rey_01_gustavo_spare_end` → 2; `rey_01_gustavo_spare_end_terminate` → 413; `End 3` → 425; `End 2` → 283.

End nodes: 2: `NonTerminating`; 37: `<omitted>`; 283: `<omitted>`; 413: `<omitted>`; 425: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 9 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 33 | 9 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 5 | 107 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 21 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 7 | 9 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech: 3
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation: 1

Raw SHA-256: `8aad54472198a6cefb2e957d4e52aa47b699767d5e25f0fd925cd90062bf583f`. Binary SHA-256: `a2bd89b983bb72ba175103a5010b205c55c205e220d8a5976826bbea25fdb336`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\scenes\sts_hey_rey_01_03_gustavo.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\scenes\sts_hey_rey_01_chats.scene`

5 graph nodes, 7 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: guard1 (actor 0, community).

Entries: `rey_01_guard_001_start` → 7.

Exits: `rey_01_phone_end` → 8.

End nodes: 8: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `5032f9a968ce217c0f03e8ec0059db59804354ded60baa2dc3d583dd60a5d24a`. Binary SHA-256: `0f4f752fff62c65a1718d40fe56a22bc8ac7b1f3030c1f8bffcf84a39af4e2ed`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\scenes\sts_hey_rey_01_chats.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\scenes\sts_hey_rey_01_holocall_debriefs.scene`

38 graph nodes, 53 edges; 5 event-bearing sections, 14 events; 14 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: padre (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 287.

End nodes: 2: `<omitted>`; 287: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 14 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5

Raw SHA-256: `525ce995abc2ff5ccbfc96f79fca375dec9fceac5657c0e754afc3475cf3becb`. Binary SHA-256: `15c52380501e7a00298b39d32d9a03a0fb6d088a01c1400435707d3113949a92`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\scenes\sts_hey_rey_01_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\scenes\sts_hey_rey_01_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Padre (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `6ad9f70760d12e5d0aac2f4957e2346d250354f4c7ec957ff2c261c4f22e4918`. Binary SHA-256: `0d5f7ad505b9b86eb1bbcc778b47055b82ef79ee9c41841c2e0f21336de25b81`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\scenes\sts_hey_rey_01_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\scenes\sts_hey_rey_01_intercom.scene`

15 graph nodes, 16 edges; 4 event-bearing sections, 8 events; 8 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Intercom (actor 0, community); guard_001 (actor 1, community); V (actor 2, findInContext).

Entries: `rey_01_intercom_start` → 1; `Start 1` → 32; `Start 2` → 58.

Exits: `rey_01_intercom_end` → 2; `End 1` → 33; `End 2` → 54.

End nodes: 2: `<omitted>`; 33: `<omitted>`; 54: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 8 | 12 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `2c5125959d9b0a7541696572a4ea608294124f13cbfe5560e57b02c1972eab3a`. Binary SHA-256: `28e3381e670d87cb1b6417b7124867c769bc610d762e35a501ff9646975d3741`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_01\scenes\sts_hey_rey_01_intercom.scene" --events
```

## `base\quest\side_quests\sq018\scenes\sq018_03_funeral.scene`

359 graph nodes, 431 edges; 65 event-bearing sections, 528 events; 111 screenplay lines, 23 screenplay options, 10 choice nodes.

Actors: Mama_Welles (actor 0, spawnSet); Victor_Vector (actor 1, spawnSet); Padre (actor 2, spawnSet); Misty (actor 3, spawnSet); ma_ganger_01_talking (actor 4, community); ma_ganger_02 (actor 5, community); elcoyote_barman (actor 6, spawnSet); ma_ganger_03 (actor 7, community); fa_ganger_01 (actor 8, community); fa_ganger_02 (actor 9, community); rey_gustavo (actor 10, community); rey_gustavo_girlfriend (actor 11, community); gle_bouncer (actor 12, community); gle_dad (actor 13, community); gle_mom (actor 14, community); rey_01_ma_friend_01 (actor 15, community); rey_01_ma_friend_02 (actor 16, community); V (actor 17, findInContext).

Entries: `in_before` → 1; `preview` → 1882.

Exits: `out_ceremony` → 2; `Valentinos_out` → 2439; `out_optional_scenes` → 813.

End nodes: 2: `NonTerminating`; 813: `NonTerminating`; 2439: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 329 / 316 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/4` |
| `scnChangeIdleAnimEvent` | 18 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 90 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 10 | 196 / 204 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/9` |
| `scnIKEvent` | 20 | 196 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnLookAtEvent` | 141 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 94 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 4 | 142 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnUnmountEvent` | 10 | 196 / 211 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/15` |
| `scneventsAttachPropToNode` | 3 | 136 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/12` |
| `scneventsAttachPropToPerformer` | 14 | 301 / 247 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/6` |
| `scneventsAttachPropToWorld` | 6 | 142 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/24` |
| `scneventsEquipItemToPerformer` | 1 | 1022 / 893 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 10 | 196 / 207 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/12` |
| `scneventsSocket` | 94 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsVFXEvent` | 12 | 329 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 5
- speech, idle_animation: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, props_equipment, socket_signal: 3
- speech, idle_animation, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze: 2
- skeletal_animation, gaze, socket_signal: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal, animation_state: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1
- vfx: 1
- skeletal_animation: 1
- gaze, socket_signal: 1

Raw SHA-256: `c8dd34d720a40d2414a2bade84252f4169a1b64ffa58e04ef93bca01658689b8`. Binary SHA-256: `f9fb4978219a4cb589edd0a97681b4b8ad6bddf2295450f9d6b4ab103ea97b5a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq018\scenes\sq018_03_funeral.scene" --events
```

## `base\quest\side_quests\sq018\scenes\sq018_04b_valentinos_el_coyote.scene`

206 graph nodes, 226 edges; 25 event-bearing sections, 116 events; 61 screenplay lines, 10 screenplay options, 6 choice nodes.

Actors: fa_ganger_01 (actor 0, community); fa_ganger_02 (actor 1, community); gle_04_bouncer (actor 2, community); ma_ganger_01 (actor 3, community); ma_ganger_02 (actor 4, community); ma_ganger_03 (actor 5, community); rey_01_martha (actor 6, community); rey_01_gustavo (actor 7, community); rey_01_ma_friend_01 (actor 8, community); rey_01_ma_friend_02 (actor 9, community); gle_01_mom (actor 10, community); gle_01_dad (actor 11, community); V (actor 12, findInContext).

Entries: `in` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 2509 / 898 | `/Data/RootChunk/sceneGraph/Data/graph/133/Data/events/3` |
| `scnDialogLineEvent` | 49 | 8 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnLookAtEvent` | 29 | 8 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 13 | 14 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsAttachPropToPerformer` | 2 | 2509 / 896 | `/Data/RootChunk/sceneGraph/Data/graph/133/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 2509 / 899 | `/Data/RootChunk/sceneGraph/Data/graph/133/Data/events/4` |
| `scneventsEquipItemToPerformer` | 1 | 106 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scneventsSocket` | 15 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsVFXEvent` | 3 | 2509 / 897 | `/Data/RootChunk/sceneGraph/Data/graph/133/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, socket_signal: 4
- speech, gaze: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- skeletal_animation, props_equipment, audio, vfx: 2
- speech, skeletal_animation, props_equipment, socket_signal: 1
- socket_signal: 1
- vfx: 1

Raw SHA-256: `5e3bf1e55ec1987c36d5c14f7f645e67d6148b656abb69e53da582c6e1d65a2e`. Binary SHA-256: `9312434802aa452d76b52ad06310ae1658c5b036c01246b5340201798758d687`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq018\scenes\sq018_04b_valentinos_el_coyote.scene" --events
```

