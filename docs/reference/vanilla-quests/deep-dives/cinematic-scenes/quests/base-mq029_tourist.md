# The Highwayman: scene presentation

Journal identity: `quests/minor_quest/mq029_tourist`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq029_tourist.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq029\scenes\mq029_01_james.scene`

79 graph nodes, 95 edges; 14 event-bearing sections, 136 events; 36 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: james (actor 0, community); Player (actor 1, findInContext).

Entries: `mq029_01_james_IN` → 1; `Start1` → 263; `returnal` → 269.

Exits: `mq029_01_james_combat_OUT` → 2; `mq029_01_james_no_fight_OUT` → 80.

End nodes: 2: `NonTerminating`; 80: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 7 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnChangeIdleAnimEvent` | 14 | 7 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scnDialogLineEvent` | 33 | 7 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnLookAtEvent` | 21 | 7 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnPlaySkAnimEvent` | 44 | 7 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsAttachPropToNode` | 1 | 7 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsAttachPropToPerformer` | 1 | 7 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsSocket` | 20 | 7 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `0aa0ec3ab14edcfdd5c9c924f56ccf507d405e2f708ee8e4478db3945b31af96`. Binary SHA-256: `5ed14875213dca5ee51a0c06a012a2712c8814bfd1a17251bddbf82e0b5c5f22`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq029\scenes\mq029_01_james.scene" --events
```

## `base\quest\minor_quests\mq029\scenes\mq029_01a_garage.scene`

19 graph nodes, 17 edges; 2 event-bearing sections, 18 events; 5 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `mq029_01a_destroyed_bike_IN` → 1; `mq029_01a_pickup_photo_IN` → 48.

Exits: `mq029_01a_destroyed_bike_OUT` → 2; `mq029_01a_pickup_photo_OUT` → 49.

End nodes: 2: `<omitted>`; 49: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 51 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scnChangeIdleAnimEvent` | 2 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 2 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 6 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsAttachPropToNode` | 1 | 51 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/4` |
| `scneventsAttachPropToPerformer` | 1 | 51 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, props_equipment, audio: 1

Raw SHA-256: `650ab6bdf919e345bc7220f44c6c655cca8aa2a647d4066d28c6ea4574fc5980`. Binary SHA-256: `ba19486693c66b746bed34f58cda52edb9ecc2b410f7501d90d2d8f2472d7dd5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq029\scenes\mq029_01a_garage.scene" --events
```

## `base\quest\minor_quests\mq029\scenes\mq029_01b_josie_body.scene`

11 graph nodes, 9 edges; 1 event-bearing sections, 5 events; 3 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `mq029_01b_josie_body_IN` → 1; `mq029_01b_final_note_in` → 9.

Exits: `mq029_01b_josie_body_OUT` → 2; `mq029_01b_final_note_out` → 10.

End nodes: 2: `NonTerminating`; 10: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 2 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 1

Raw SHA-256: `5215411d69b23b152b849c7326613820daa3f61923ad6be635a1ac42655a8cab`. Binary SHA-256: `34faebbc9ce4462caf7d30f7c1f5d7be23c3f01e57dd2228c502fe1a3c9c686f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq029\scenes\mq029_01b_josie_body.scene" --events
```

