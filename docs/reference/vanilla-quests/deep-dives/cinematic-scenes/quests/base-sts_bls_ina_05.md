# Gig: Goodbye, Night City: scene presentation

Journal identity: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_05`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_bls_ina_05.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\scenes\sts_bls_ina_05_archibald.scene`

49 graph nodes, 57 edges; 4 event-bearing sections, 66 events; 9 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: bruce (actor 0, community); archibald (actor 1, community); archibald_truck (actor 2, community); Player (actor 3, findInContext).

Entries: `ina_05_archibald_start` → 1.

Exits: `ina_05_archibald_end` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 6 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnGameplayTransitionEvent` | 2 | 4 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/48` |
| `scnIKEvent` | 4 | 4 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/40` |
| `scnLookAtEvent` | 7 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 20 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 2 | 4 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/46` |
| `scneventsSetAnimFeatureEvent` | 3 | 4 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/45` |
| `scneventsSocket` | 12 | 4 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scneventsUnequipItemFromPerformer` | 1 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 2 | 1929 / 273 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `e3412c5e84aca16b97cd61d3f2c8facb71349f34853d4776c1592e286efc7b74`. Binary SHA-256: `c8d156cfcba0c264b6a475c0939edb7c8792ef07b926634aaaba683fb9cffdba`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\scenes\sts_bls_ina_05_archibald.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\scenes\sts_bls_ina_05_bruce.scene`

79 graph nodes, 81 edges; 21 event-bearing sections, 91 events; 32 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: bruce (actor 0, community); archibald (actor 1, findInWorld); Player (actor 2, findInContext).

Entries: `ina_05_bruce_start` → 1; `Start 4` → 93; `Start 5` → 96; `interrupt` → 100; `interrupt_var_1` → 104; `ina_05_following_start` → 34; `interrupt_var_2` → 105; `return_answer` → 110; `return_answer_var_1` → 112; `return_answer_var_2` → 113; `urge` → 114; `urge_var_1` → 116; `urge_var_2` → 117; `ina_05_no_car_start` → 55.

Exits: `ina_05_bruce_follow` → 2; `ina_05_bruce_no_follow` → 22; `ina_05_following_end` → 35; `ina_05_no_car_end` → 56.

End nodes: 2: `NonTerminating`; 22: `NonTerminating`; 35: `NonTerminating`; 56: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 15 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 29 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 17 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 16 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 14 | 12 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, idle_animation: 1
- idle_animation, gaze, socket_signal: 1

Raw SHA-256: `da47d2f187584d75f717a30a73360b5a83583cb712d122ae051a33437934227c`. Binary SHA-256: `33cecefe0353eba72bdcbaec03a4f48141623a0546d54c89943bd053584610dc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\scenes\sts_bls_ina_05_bruce.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\scenes\sts_bls_ina_05_holocall_debriefs.scene`

29 graph nodes, 39 edges; 4 event-bearing sections, 10 events; 10 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: dakota (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 285.

End nodes: 2: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 10 | 68 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `a3f3fefde2e046041bf1ed6613c6acd4700126a2fd5411daf88e2084016873aa`. Binary SHA-256: `73f0f3d93d5dc7a3cc1bf3eb1d2dc9022c340a92b19202be6d3d90b6f7913866`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\scenes\sts_bls_ina_05_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\scenes\sts_bls_ina_05_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: dakota (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 68 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `8aed9b8c71a57d4e95477bd030dba9949a2394499cbba264f0bf015166e0467a`. Binary SHA-256: `364911746d83eb2ab1855efb336aa5053414c77e1e70e235b2843880e7a2df27`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_05\scenes\sts_bls_ina_05_holocall_prebrief.scene" --events
```

