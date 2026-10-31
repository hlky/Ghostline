# Only Pain: scene presentation

Journal identity: `quests/minor_quest/mq005_alley`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq005_alley.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene`

156 graph nodes, 198 edges; 28 event-bearing sections, 270 events; 77 screenplay lines, 18 screenplay options, 7 choice nodes.

Actors: Police_Officer_01 (actor 0, community); Police_Officer_02 (actor 1, community); Police_Officer_03 (actor 2, community); Corpo (actor 3, community); car_01 (actor 4, spawner); car_02 (actor 5, spawner); Player (actor 6, findInContext).

Entries: `Start_in` → 1; `Wrapup_in` → 377; `old` → 520.

Exits: `Combat_out` → 2; `End_Out` → 4; `StreetKidSuccess_out` → 45; `Ignored_out` → 49; `player_attack_corpo_out` → 200; `CombatFromInterruption` → 631; `CorpoKilledInCrossfire` → 244.

End nodes: 2: `NonTerminating`; 4: `NonTerminating`; 45: `NonTerminating`; 49: `<omitted>`; 200: `<omitted>`; 244: `<omitted>`; 631: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 14 | 13 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scnDialogLineEvent` | 72 | 13 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnGameplayTransitionEvent` | 5 | 40 / 245 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/46` |
| `scnIKEvent` | 10 | 40 / 227 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/37` |
| `scnLookAtEvent` | 57 | 13 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 59 | 13 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnPoseCorrectionEvent` | 7 | 13 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scnUnmountEvent` | 5 | 40 / 246 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/47` |
| `scneventsSetAnimFeatureEvent` | 5 | 40 / 243 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/45` |
| `scneventsSocket` | 35 | 13 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 40 / 208 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/25` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation: 3
- speech: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- gaze: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- idle_animation, socket_signal: 1

Raw SHA-256: `e585c406ba31086e0628d7fa17077f3dcfd095e5ac9daf9d97f9d20f43f38a83`. Binary SHA-256: `ee2b94791d7eee93e479c3bfec51828b7531c503042bebbb8c7bdc8a174eb108`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene" --events
```

