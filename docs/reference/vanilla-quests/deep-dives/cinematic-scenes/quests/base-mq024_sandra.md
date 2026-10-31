# Full Disclosure: scene presentation

Journal identity: `quests/minor_quest/mq024_sandra`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq024_sandra.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene`

23 graph nodes, 26 edges; 8 event-bearing sections, 34 events; 33 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: sandra (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 33 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 1 | 19 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, socket_signal: 1

Raw SHA-256: `a11cb82a2856c827fc0173a2190575e663282c82ceb64f8ce561101b365a5d11`. Binary SHA-256: `c9dc1954a60e1f25c708377e09a9b3ba8f12d36d2905b7ceca63e9768d2ec483`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq024\scenes\mq024_01_call_sandra.scene" --events
```

## `base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene`

132 graph nodes, 152 edges; 21 event-bearing sections, 165 events; 70 screenplay lines, 20 screenplay options, 11 choice nodes.

Actors: sandra (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `prev_cross` → 519; `prev_good_normal` → 447.

Exits: `End 0` → 2; `End_killed_door` → 527.

End nodes: 2: `NonTerminating`; 527: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 10 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnDialogLineEvent` | 65 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 2 | 6 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnIKEvent` | 4 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 6 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 31 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 6 | 20 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/10` |
| `scnUnmountEvent` | 2 | 6 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsAttachPropToPerformer` | 2 | 10 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 10 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scneventsEquipItemToPerformer` | 6 | 20 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 2 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsSocket` | 34 | 6 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 5
- speech, skeletal_animation, props_equipment, socket_signal: 3
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, props_equipment, socket_signal, animation_state: 2
- speech, skeletal_animation, props_equipment, audio: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, props_equipment, socket_signal: 1
- gaze: 1
- skeletal_animation, socket_signal, animation_state: 1
- speech: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `efeb53035b3352b18657889f64a5cf5a8aa30a555b7b25d49bdac6048b9d45db`. Binary SHA-256: `949fab003c6e830c88634b060cdb6968657d8c454e6206af27e38cfc813929d5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq024\scenes\mq024_02_meet_sandra.scene" --events
```

