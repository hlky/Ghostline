# These Boots Are Made for Walkin': scene presentation

Journal identity: `quests/minor_quest/mq042_nomad`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq042_nomad.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene`

41 graph nodes, 43 edges; 12 event-bearing sections, 105 events; 31 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: johnny (actor 0, spawnDespawn); performer (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `interrupt_in` → 83.

Exits: `End 0` → 2; `interrupt_out` → 85; `mq023_johnny_out` → 218.

End nodes: 2: `NonTerminating`; 85: `NonTerminating`; 218: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 26 | 11 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnDialogLineEvent` | 30 | 11 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnLookAtEvent` | 18 | 11 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 20 | 11 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsSocket` | 9 | 11 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsVFXEvent` | 2 | 225 / 309 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze: 4
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech: 1
- skeletal_animation, gaze, vfx, socket_signal: 1

Raw SHA-256: `fb943e8a5c6d2b4de9b9bc2f7dd973bbf5db4db7f152d3e20ceb6af52752ac49`. Binary SHA-256: `23d3a608acb36e7fb29121107e27b485c8d00860c5434101297d012befeb69a7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene" --events
```

## `base\quest\minor_quests\mq042\scenes\mq042_nomad_01_gps_signal.scene`

3 graph nodes, 2 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Player (actor 0, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `a18531619bd334c6667547ced69974697c3dff1cb86b153a1b75d4d3a2acb047`. Binary SHA-256: `23141d6bc6198d02881798b19117008480a5481bcf69b131a052a521d1becfce`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq042\scenes\mq042_nomad_01_gps_signal.scene" --events
```

## `base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene`

142 graph nodes, 159 edges; 31 event-bearing sections, 300 events; 75 screenplay lines, 14 screenplay options, 7 choice nodes.

Actors: Lana (actor 0, spawnSet); johnny (actor 1, spawnDespawn); nomad_car (actor 2, spawner); temp_car (actor 3, spawner); Player (actor 4, findInContext).

Entries: `Start 5` → 1098; `Start 0` → 1; `Start 6` → 1100; `debug_input` → 874; `Start 4` → 1080.

Exits: `End 0` → 2; `journal_update` → 830.

End nodes: 2: `NonTerminating`; 830: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 15 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/6` |
| `scnDialogLineEvent` | 66 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 15 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/7` |
| `scnIKEvent` | 8 | 15 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnLookAtEvent` | 30 | 15 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnPlaySkAnimEvent` | 135 | 13 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnUnmountEvent` | 4 | 15 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/12` |
| `scneventsEquipItemToPerformer` | 3 | 924 / 1080 | `/Data/RootChunk/sceneGraph/Data/graph/108/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 4 | 15 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/9` |
| `scneventsSocket` | 37 | 13 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, gaze: 3
- skeletal_animation, props_equipment, socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze: 1

Raw SHA-256: `bd604352685f073be234e20d21bbbba13613477d884ca31ffb3a423e3e1c17e7`. Binary SHA-256: `46722d67c435e7ca730801112df0558fb4cdf5740bf7986a9000322356fc3a45`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq042\scenes\mq042_nomad_02_car_found.scene" --events
```

