# Beat on the Brat: Arroyo: scene presentation

Journal identity: `quests/minor_quest/mq025_03_arroyo`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq025_03_arroyo.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene`

105 graph nodes, 117 edges; 25 event-bearing sections, 180 events; 51 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: Buck (actor 0, community); crowd_01 (actor 1, community); crowd_02 (actor 2, community); crowd_03 (actor 3, community); 6th (actor 4, community); mq025_arroyo_vehicle (actor 5, spawner); V (actor 6, findInContext).

Entries: `mq025_03_bottles_in` → 101; `mq025_03_start_in` → 7; `mq025_03_after_in` → 24; `mq025_03_post_in` → 144; `mq025_03_loot_in` → 88.

Exits: `mq025_03_bottles_out` → 104; `fight prep` → 20; `mq025_03_fight` → 23; `Cleanup` → 607; `mq025_03_after_out` → 129; `mq025_03_after_out_fight` → 34; `mq025_03_post_out` → 146; `mq025_03_loot_out` → 91.

End nodes: 20: `NonTerminating`; 23: `<omitted>`; 34: `<omitted>`; 91: `<omitted>`; 104: `<omitted>`; 129: `NonTerminating`; 146: `<omitted>`; 607: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 16 | 9 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 46 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |
| `scnGameplayTransitionEvent` | 2 | 466 / 495 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/11` |
| `scnIKEvent` | 4 | 466 / 488 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/5` |
| `scnLookAtEvent` | 30 | 6 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 60 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnUnmountEvent` | 2 | 466 / 494 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/10` |
| `scneventsEquipItemToPerformer` | 2 | 9 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 2 | 466 / 490 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/7` |
| `scneventsSocket` | 16 | 9 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, skeletal_animation, gaze: 4
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- idle_animation, gaze: 1

Raw SHA-256: `7dc6c68ca84cdd8d3420779eba44da768f7036923c16509d666b0f0ea98bec90`. Binary SHA-256: `2a4e5bdd96c40af1392c2984bdf3a824c90cf832c66db793ea0ccde89a928827`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene" --events
```

