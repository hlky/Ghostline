# Gig: Bloodsport: scene presentation

Journal identity: `quests/street_stories/watson/little_china/sts_wat_lch_03`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_lch_03.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\little_china\sts_wat_lch_03\scenes\sts_wat_lch_03_dojo_owner.scene`

27 graph nodes, 36 edges; 11 event-bearing sections, 23 events; 23 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: owner (actor 0, findInWorld); V (actor 1, findInContext).

Entries: `lch_03_owner_routine` → 1; `lch_03_owner_dialogue_start` → 457.

Exits: `sts_wat_lch_03_owner_solo` → 517; `End 2` → 493; `lch_03_owner_routine_end` → 439.

End nodes: 439: `NonTerminating`; 493: `<omitted>`; 517: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 23 | 440 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11

Raw SHA-256: `1ba48d254a7aab72fcb08d888814820a73158d8ca7e17cb25640bf7b7a08bd07`. Binary SHA-256: `84543adfb75f54a560911dc76ffbd260e74df71ff0521a312cbca4537bda8c9d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\little_china\sts_wat_lch_03\scenes\sts_wat_lch_03_dojo_owner.scene" --events
```

## `base\open_world\street_stories\watson\little_china\sts_wat_lch_03\scenes\sts_wat_lch_03_holocall_debriefs.scene`

27 graph nodes, 39 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 18.

Exits: `rejected_out` → 285; `End 0` → 42.

End nodes: 42: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 46 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `36998436193bfa855a65a6e22398807521643bfcb8cd910026fa51831ceec925`. Binary SHA-256: `39ef51ff92152ddfbacfd8ef7a0093ffcb9d143990f0926c4319e39b9a3a7f23`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\little_china\sts_wat_lch_03\scenes\sts_wat_lch_03_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\watson\little_china\sts_wat_lch_03\scenes\sts_wat_lch_03_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `a0dc16a0e1173360832cc36040899050ac7e50b0cfc0112b2589d3d71991768e`. Binary SHA-256: `fb3c5f8c7fadd051fffadfa48063fa95a8f2e942ddd6fc1aecf65753babc3751`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\little_china\sts_wat_lch_03\scenes\sts_wat_lch_03_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\watson\little_china\sts_wat_lch_03\scenes\sts_wat_lch_03_ricky_wu.scene`

98 graph nodes, 149 edges; 20 event-bearing sections, 108 events; 39 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: roh_chi_won (actor 0, community); torturer (actor 1, community); V (actor 2, findInContext).

Entries: `welcome` → 1; `Start 3` → 216; `Start 0` → 218; `done` → 25; `Start 2` → 192.

Exits: `welcome_end` → 2; `done_end` → 26; `objective_talk` → 305; `new_objective_talk_with_ricky` → 307.

End nodes: 2: `NonTerminating`; 26: `NonTerminating`; 305: `NonTerminating`; 307: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 7 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 26 | 7 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 17 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/19` |
| `scnIKEvent` | 4 | 17 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scnLookAtEvent` | 17 | 7 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 32 | 7 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 2 | 7 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scnUnmountEvent` | 2 | 17 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 2 | 17 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/14` |
| `scneventsSocket` | 15 | 7 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 4
- speech, skeletal_animation: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `72acf28ad91f9da0f99ac93bba0782af17bd2271b40d6e549ef9292445fe92b3`. Binary SHA-256: `83186430cffea99d98cca6e6303c83e7b83e4a4cba4a3de904993f002d096174`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\little_china\sts_wat_lch_03\scenes\sts_wat_lch_03_ricky_wu.scene" --events
```

