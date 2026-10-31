# Gig: Scrolls before Swine: scene presentation

Journal identity: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_07`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_nid_07.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\scenes\sts_wat_nid_07_aaron_mccarlson.scene`

86 graph nodes, 91 edges; 18 event-bearing sections, 142 events; 42 screenplay lines, 6 screenplay options, 2 choice nodes.

Actors: aaron (actor 0, findInWorld); johnny (actor 1, spawnDespawn); v (actor 2, findInContext).

Entries: `Start 0` → 1; `recording_seen` → 57; `johnny_afterwards` → 62.

Exits: `peace` → 2; `johnny_afterwards_end` → 69; `war` → 35; `recording_seen_end` → 60.

End nodes: 2: `<omitted>`; 35: `<omitted>`; 60: `<omitted>`; 69: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 22 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnDialogLineEvent` | 38 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 138 / 376 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/7` |
| `scnIKEvent` | 4 | 138 / 369 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/1` |
| `scnLookAtEvent` | 9 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 37 | 13 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPoseCorrectionEvent` | 4 | 22 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scnUnmountEvent` | 2 | 138 / 375 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 2 | 138 / 373 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/5` |
| `scneventsSocket` | 35 | 13 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scneventsVFXEvent` | 4 | 17 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 3
- speech, gaze: 2
- speech, skeletal_animation, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `06dda8aaab1aa735c9388c40dcb5f1f6efbabc06ddb534b847801d959c5d1caf`. Binary SHA-256: `22e187b32851726c21158b105929a58a53ee06e58d27d9840aefdf8db524b026`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\scenes\sts_wat_nid_07_aaron_mccarlson.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\scenes\sts_wat_nid_07_holocall_debriefs.scene`

27 graph nodes, 33 edges; 3 event-bearing sections, 5 events; 5 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 288.

End nodes: 2: `<omitted>`; 288: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 30 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `e5ade60b1b3f0ae76ec91670a762def96d3bf4ea189dd1fd33d248c999eda492`. Binary SHA-256: `306b51f788701851328cfea1d17c2e897e3154ec020afde181c0a265f68fc966`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\scenes\sts_wat_nid_07_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\scenes\sts_wat_nid_07_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `07a7007f77b2acc84f43b9391a6d43312a418d7f8ae6765034b3cee159f679a2`. Binary SHA-256: `f2c0504a7c7fb792cab233d1d5b50eb9b568af518b66a9724a4cd4eb7d2ad921`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_07\scenes\sts_wat_nid_07_holocall_prebrief.scene" --events
```

