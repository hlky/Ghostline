# Gig: Backs Against the Wall: scene presentation

Journal identity: `quests/street_stories/watson/kabuki/sts_wat_kab_03`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_kab_03.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene`

25 graph nodes, 29 edges; 1 event-bearing sections, 1 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start1` → 59.

Exits: `rejected_out` → 301; `End1` → 60.

End nodes: 60: `<omitted>`; 301: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `e4ec84dce44abf40bc9e39b1c425ab80d9049f57732f49f51524ae6a2ea107bf`. Binary SHA-256: `bd088df1d5046502cba3367083b2a4453e5548e7dcf5c66da79a590d137179da`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_debrief.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start1` → 78.

Exits: `End1` → 79; `rejected_out` → 260.

End nodes: 79: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 29 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `36b536c56fa121f4b7b749c32e86e9a2e375e0c845575d622d46972d3fb2d545`. Binary SHA-256: `830ef4b6600b9671e992f8eb5841d6ab6f97dcf10e9a5565de3897125a43bc96`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene`

34 graph nodes, 43 edges; 7 event-bearing sections, 36 events; 15 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: johnny (actor 0, spawnDespawn); johnny_spawnset_cat (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `q003_cat_flat_reaction_in` → 199.

Exits: `End 0` → 2; `q003_cat_flat_reaction_out` → 200.

End nodes: 2: `<omitted>`; 200: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 17 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnDialogLineEvent` | 15 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 7 | 10 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 7 | 10 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsSocket` | 6 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 3
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, gaze: 1

Raw SHA-256: `8f564be05586715a43a7099da8cdcab48cd29ed8ade4643e832e337981cde855`. Binary SHA-256: `5578cbbdf013f163a6653b9362fbeccf989e523e02eedb62c6850618ca59eb85`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_johnny.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene`

103 graph nodes, 134 edges; 26 event-bearing sections, 139 events; 97 screenplay lines, 13 screenplay options, 5 choice nodes.

Actors: solo (actor 0, community); neighbour_001 (actor 1, community); neighbour_002 (actor 2, community); johnny (actor 3, spawnDespawn); player (actor 4, findInContext).

Entries: `solo` → 27; `interrupt` → 1107; `neighbours` → 769.

Exits: `peaceful` → 17; `combat` → 716; `interrupt_default` → 830; `interrupt_o` → 835; `neighbours_o` → 771; `dont move` → 1164.

End nodes: 17: `NonTerminating`; 716: `<omitted>`; 771: `NonTerminating`; 830: `<omitted>`; 835: `NonTerminating`; 1164: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 3. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 551 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnChangeIdleAnimEvent` | 5 | 551 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 71 | 551 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnGameplayTransitionEvent` | 1 | 1203 / 438 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/6` |
| `scnIKEvent` | 2 | 1203 / 433 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/2` |
| `scnLookAtEvent` | 10 | 551 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 24 | 551 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 1 | 1203 / 437 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 1203 / 435 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/4` |
| `scneventsSocket` | 22 | 551 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 5
- speech: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, gaze: 1
- idle_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, audio: 1
- gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `9174562f44c2e293467cbba4e699693e6e4cc8aae9cd03e58a230286aa5beb53`. Binary SHA-256: `1f7063991fe25dc61a7e08a1ab43e770f6ace95dc30b4df476d9958a36a46350`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_03\scenes\sts_wat_kab_03_scene.scene" --events
```

