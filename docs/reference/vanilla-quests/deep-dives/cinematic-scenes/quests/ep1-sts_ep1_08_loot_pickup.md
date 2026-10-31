# Money For Nothing: scene presentation

Journal identity: `ep1/quests/minor_quest/sts_ep1_08_loot_pickup`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-sts_ep1_08_loot_pickup.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_target_meeting.scene`

248 graph nodes, 274 edges; 39 event-bearing sections, 184 events; 78 screenplay lines, 18 screenplay options, 10 choice nodes.

Actors: target (actor 0, spawnSet); bana_voice (actor 1, findInContext); Ana (actor 2, spawnSet); bana_impersonated (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `Bana intro` → 1; `fake input to keep lines alive` → 1971; `Start 11` → 2490; `Meeting` → 348; `eliminate enemies` → 890; `katya dead comment` → 1407; `enemies defeated` → 923.

Exits: `dead` → 24; `meeting_point` → 1293; `friendly` → 1073; `phone end 01` → 887; `eliminate enemies end` → 891; `End 12` → 1409; ` enemies defeated end` → 924; `katya killed before order` → 1416.

End nodes: 24: `<omitted>`; 887: `NonTerminating`; 891: `NonTerminating`; 924: `NonTerminating`; 1073: `NonTerminating`; 1293: `NonTerminating`; 1409: `NonTerminating`; 1416: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1344 / 609 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/4` |
| `scnChangeIdleAnimEvent` | 8 | 187 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 71 | 79 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 1109 / 485 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/20` |
| `scnIKEvent` | 2 | 1109 / 477 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/13` |
| `scnLookAtAdvancedEvent` | 3 | 201 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scnLookAtEvent` | 25 | 201 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnPlaySkAnimEvent` | 22 | 1027 / 302 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 187 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnUnmountEvent` | 1 | 1109 / 484 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/19` |
| `scneventsAttachPropToNode` | 1 | 1344 / 611 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/6` |
| `scneventsAttachPropToPerformer` | 1 | 1344 / 608 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 1 | 1109 / 480 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/16` |
| `scneventsSocket` | 39 | 187 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsVFXDurationEvent` | 3 | 201 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scneventsVFXEvent` | 3 | 1109 / 458 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, skeletal_animation, socket_signal: 4
- speech, gaze: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, idle_animation, socket_signal: 2
- idle_animation, socket_signal, animation_state: 1
- speech, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `d05346023180176a807920783b4a3324e84f8174450439209b711238171eeba2`. Binary SHA-256: `81142f72b147e1e00ccdb0c897bafe3bc81660633dd38e01c88732227e79de82`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_target_meeting.scene" --events
```

