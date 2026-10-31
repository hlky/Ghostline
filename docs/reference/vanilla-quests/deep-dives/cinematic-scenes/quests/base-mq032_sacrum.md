# Sacrum Profanum: scene presentation

Journal identity: `quests/minor_quest/mq032_sacrum`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq032_sacrum.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene`

78 graph nodes, 88 edges; 27 event-bearing sections, 206 events; 63 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: Cyberware_Monk (actor 0, community); Johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `mq032_01_hook_in` → 1; `mq032_fuck_test_in` → 143.

Exits: `Cleanup` → 185; `mq032_01_hook_out` → 35.

End nodes: 35: `NonTerminating`; 185: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 8 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 45 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 6 | 8 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scnPlaySkAnimEvent` | 123 | 8 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnPoseCorrectionEvent` | 1 | 49 / 323 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/6` |
| `scneventsSocket` | 24 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 11
- speech, skeletal_animation: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze: 1
- idle_animation, socket_signal: 1

Raw SHA-256: `06a8e3f7bf84576b22e8b22435ca76551ea00444dc56404f59ae250e79b5ba5e`. Binary SHA-256: `bc080e620bc70fab39ae306a3cc12b78367880044990ec6fe166929caeaa6ff7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene" --events
```

## `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene`

111 graph nodes, 139 edges; 31 event-bearing sections, 264 events; 82 screenplay lines, 11 screenplay options, 5 choice nodes.

Actors: Brother (actor 0, community); Maelstrom_01 (actor 1, community); Maelstrom_02 (actor 2, community); Maelstrom_08 (actor 3, community); Johnny (actor 4, spawnDespawn); V (actor 5, findInContext).

Entries: `mq032_02_maelstrom_in` → 1; `mq032_02_maelstrom_attack_in` → 12; `mq032_02_saved_in` → 17; `Start 8` → 491; `mq032_02_killed_in` → 60; `mq032_02_maelstrom_fluff_in` → 65; `mq032_monk_animations_in` → 193; `Start 9` → 553; `mq032_02_lethal_01_CLONE_in` → 212; `Start 10` → 572.

Exits: `mq032_02_maelstrom_out` → 2; `mq032_02_maelstrom_attack_out` → 15; `mq032_02_saved_out` → 49; `mq032_02_killed_out` → 63; `mq032_02_maelstrom_fluff_end` → 68; `mq032_02_lethal_01_CLONE_out` → 214; `mq032_02_cleanup_out` → 456.

End nodes: 2: `<omitted>`; 15: `<omitted>`; 49: `NonTerminating`; 63: `<omitted>`; 68: `<omitted>`; 214: `<omitted>`; 456: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 35 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |
| `scnDialogLineEvent` | 68 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 273 / 720 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/6` |
| `scnIKEvent` | 2 | 273 / 714 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/1` |
| `scnLookAtEvent` | 17 | 18 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 122 | 18 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnPoseCorrectionEvent` | 28 | 26 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/7` |
| `scnUnmountEvent` | 1 | 273 / 719 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 273 / 717 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/4` |
| `scneventsSocket` | 18 | 18 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, animation_state: 3
- speech, skeletal_animation, idle_animation, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze: 1

Raw SHA-256: `48cabeebddc650795e5423189faffbce002ed04a5107d1e15bf189b895531882`. Binary SHA-256: `8ed741036cf60563c33551d67e9a5598ca8bcceafbfdda43a7d55d521cfdd6c8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene" --events
```

## `base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene`

43 graph nodes, 47 edges; 16 event-bearing sections, 111 events; 47 screenplay lines, 10 screenplay options, 4 choice nodes.

Actors: Monk_Cyberware (actor 0, community); Monk_Brother (actor 1, community); Johnny (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `mq032_03_success_in` → 43; `mq032_03_monk_cyberware_in` → 1; `mq032_03_dead_in` → 24; `mq032_03_fail_in` → 38; `Start 4` → 168.

Exits: `mq032_03_monk_cyberware_out` → 2; `mq032_03_success_out` → 46; `mq032_03_dead_out` → 36; `mq032_03_fail_out` → 41.

End nodes: 2: `<omitted>`; 36: `<omitted>`; 41: `<omitted>`; 46: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 77 / 253 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/2` |
| `scnDialogLineEvent` | 46 | 5 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 24 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 39 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 1 | 77 / 252 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 9
- speech, skeletal_animation: 5
- speech: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `8fcc398733c083886c75dcf439ed25995a18ba59155ae1df10e62d97823f7deb`. Binary SHA-256: `aa4873fe24498e72f87dc29e6735c1335546a57bdd87742e3a6838e1db661bf5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene" --events
```

