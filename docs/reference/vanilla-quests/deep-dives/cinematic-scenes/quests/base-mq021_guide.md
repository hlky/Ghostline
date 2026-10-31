# Fortunate Son: scene presentation

Journal identity: `quests/minor_quest/mq021_guide`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq021_guide.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq021\scenes\mq021_01_briefing.scene`

23 graph nodes, 25 edges; 7 event-bearing sections, 50 events; 24 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: Bob (actor 0, spawnSet); Wife (actor 1, community); Scooter (actor 2, community); Player (actor 3, findInContext).

Entries: `mq021_01_mood` → 1.

Exits: `mq_yes` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnDialogLineEvent` | 24 | 6 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scnLookAtEvent` | 6 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 13 | 6 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsSocket` | 6 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech: 1

Raw SHA-256: `bc23a0ccec6d4b99ac4d10dff649d3569da4a66dc550a920993448bc1b2c3a74`. Binary SHA-256: `b329c3da9c7c43e0bef487187ca3654e25114b40f47a771e85b9366326642513`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq021\scenes\mq021_01_briefing.scene" --events
```

## `base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene`

119 graph nodes, 127 edges; 20 event-bearing sections, 140 events; 41 screenplay lines, 10 screenplay options, 6 choice nodes.

Actors: Doctor (actor 0, community); Security_01 (actor 1, community); van (actor 2, community); Player (actor 3, findInContext).

Entries: `mq021_meeting` → 7; `combat_comment` → 14; `mq021_meeting_interrupted` → 20; `mq021_confrontation` → 27; `mq021_hospital_done_comment` → 481.

Exits: `mq021_meeting_out` → 8; `combat_comment_out` → 15; `mq021_meeting_interrupted_out` → 21; `mq021_confrontation_out` → 28; `mq021_meeting_out_term` → 520; `scene_cut` → 477; `mq021_hospital_done_comment_out` → 482.

End nodes: 8: `NonTerminating`; 15: `<omitted>`; 21: `<omitted>`; 28: `NonTerminating`; 477: `<omitted>`; 482: `<omitted>`; 520: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 40 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |
| `scnDialogLineEvent` | 37 | 9 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 4 | 55 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/11` |
| `scnIKEvent` | 8 | 55 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/4` |
| `scnLookAtEvent` | 6 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 33 | 9 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 4 | 55 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/10` |
| `scneventsAttachPropToNode` | 3 | 78 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/3` |
| `scneventsAttachPropToPerformer` | 5 | 44 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/9` |
| `scneventsEquipItemToPerformer` | 1 | 294 / 596 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 4 | 55 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/7` |
| `scneventsSocket` | 30 | 9 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 9 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, skeletal_animation, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `232e6bc469a1271fe908890b655545233a209d4a33dc7e6fbdf57fecfcfc0ec4`. Binary SHA-256: `9c3a4224a021f971fcc4f11247e773edf683a8def265c14c23fef77ae78c4a4e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq021\scenes\mq021_02_hospital_meeting.scene" --events
```

## `base\quest\minor_quests\mq021\scenes\mq021_03_ending.scene`

31 graph nodes, 33 edges; 6 event-bearing sections, 39 events; 14 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: Bob (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `outcome` → 1; `Start1` → 15.

Exits: `outcome_out` → 2; `End2` → 104; `End1` → 16.

End nodes: 2: `<omitted>`; 16: `NonTerminating`; 104: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 20 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnChangeIdleAnimEvent` | 2 | 9 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 14 | 9 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnLookAtEvent` | 6 | 9 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnPlaySkAnimEvent` | 10 | 9 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsAttachPropToPerformer` | 2 | 20 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 20 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scneventsSocket` | 1 | 28 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, gaze, props_equipment, audio: 2
- speech, skeletal_animation, gaze: 1
- speech, gaze, socket_signal: 1

Raw SHA-256: `249336ebabae05bdefca77f581fcdf4323c14e4203764acab991e36ea0a6933d`. Binary SHA-256: `fea6875ce415724ae1a5683a2f16ad034c32ee01abbe31b5613f591bbfeb8c97`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq021\scenes\mq021_03_ending.scene" --events
```

