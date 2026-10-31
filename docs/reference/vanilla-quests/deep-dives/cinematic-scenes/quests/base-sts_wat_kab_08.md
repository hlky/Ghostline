# Gig: Woman of La Mancha: scene presentation

Journal identity: `quests/street_stories/watson/kabuki/sts_wat_kab_08`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_kab_08.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\scenes\sts_wat_kab_08_food_chat.scene`

8 graph nodes, 8 edges; 1 event-bearing sections, 33 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: vendor_female (actor 0, spawnSet); courier_male (actor 1, findInWorld).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 7 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnDialogLineEvent` | 6 | 7 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 3 | 7 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 20 | 7 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 3 | 7 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `951a943aecd6b731c57e75de39f29266c9438c3a72761871909198f0f043aefc`. Binary SHA-256: `c32f91d253145ce202b4ca00ee89ae0c0e5ec3c809b8f2bbebbfdb6330bc4c2d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\scenes\sts_wat_kab_08_food_chat.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\scenes\sts_wat_kab_08_food_courier.scene`

69 graph nodes, 82 edges; 14 event-bearing sections, 173 events; 38 screenplay lines, 8 screenplay options, 3 choice nodes.

Actors: courier_male (actor 0, community); V (actor 1, findInContext).

Entries: `nonmet` → 1.

Exits: `fail` → 2; `dialogue_finished` → 221; `dave_already_located` → 234; `success` → 24.

End nodes: 2: `<omitted>`; 24: `NonTerminating`; 221: `NonTerminating`; 234: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 3 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scnDialogLineEvent` | 33 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 319 / 613 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/8` |
| `scnIKEvent` | 2 | 319 / 606 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/2` |
| `scnLookAtEvent` | 32 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 53 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 1 | 319 / 612 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/7` |
| `scneventsAttachPropToPerformer` | 2 | 13 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 1 | 319 / 610 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/6` |
| `scneventsSocket` | 37 | 3 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsVFXEvent` | 6 | 8 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `ccc136cbe7aa2228a63248038db8ebad559f8047b153483fad4ca3ca5c9a66fd`. Binary SHA-256: `361cafe7351211be22339538255fd85b67f5f5845dd6f23b52a5a971d3b5e7c7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\scenes\sts_wat_kab_08_food_courier.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\scenes\sts_wat_kab_08_holocall_debriefs.scene`

29 graph nodes, 39 edges; 4 event-bearing sections, 12 events; 8 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 285.

End nodes: 2: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 8 | 30 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnLookAtEvent` | 4 | 30 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 4

Raw SHA-256: `052a74415e795d0be8f2db5f12bc66b135b86af91bbe26d91513f5087de0d40b`. Binary SHA-256: `38a5999c63966faaf2f24bc0c7edc2618a2207f756594f5862d10baae1b9e5ff`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\scenes\sts_wat_kab_08_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\scenes\sts_wat_kab_08_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 5 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 26 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 1 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 1

Raw SHA-256: `39500f480b595c29409d650f4fec24d749a89f8dbba2cc5d1a6acc3762a37b0f`. Binary SHA-256: `8468b07b256bf6f28a2f7117b99da4d438b2d6ee14c38a0a23c53cd9514124b9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\scenes\sts_wat_kab_08_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\scenes\sts_wat_kab_08_prostitute.scene`

57 graph nodes, 72 edges; 14 event-bearing sections, 124 events; 30 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: prostitute (actor 0, community); tyger_claw (actor 1, community); V (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `Attacked` → 75; `success` → 2; `go away` → 127; `hamill_already_located` → 248; `combat_started` → 294.

End nodes: 2: `<omitted>`; 75: `<omitted>`; 127: `<omitted>`; 248: `<omitted>`; 294: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 5 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnDialogLineEvent` | 25 | 5 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnLookAtEvent` | 38 | 5 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 26 | 5 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsSocket` | 23 | 5 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scneventsVFXEvent` | 4 | 5 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `a0817e223fd45f38f8468f912dd95dea356bc09159e7db5889d51ac8273bdaae`. Binary SHA-256: `7a4120a4779f090fcb95b0530a8ee42d8116a20e76bb17512aab5933635d5e44`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_08\scenes\sts_wat_kab_08_prostitute.scene" --events
```

