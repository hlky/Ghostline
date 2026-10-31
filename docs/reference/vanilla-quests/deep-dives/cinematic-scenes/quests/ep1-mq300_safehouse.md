# Water Runs Dry: scene presentation

Journal identity: `ep1/quests/minor_quest/mq300_safehouse`. Stored type: **MinorQuest**. Attribution: **POI-linked; quest activation unresolved**.

[Full quest flow dossier](../../all-quests/ep1-mq300_safehouse.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene`

294 graph nodes, 347 edges; 42 event-bearing sections, 223 events; 45 screenplay lines, 30 screenplay options, 21 choice nodes.

Actors: johnny_mirror (actor 0, spawnDespawn); v_male_tpp (actor 1, spawnDespawn); v_female_tpp (actor 2, spawnDespawn); Johnny (actor 3, spawnDespawn); idris_shot_myers (actor 4, spawnDespawn); idris_shot_reed (actor 5, spawnDespawn); idris_shot_kurt (actor 6, spawnDespawn); idris_shot_songbird (actor 7, spawnDespawn); idris_shot_johnny (actor 8, spawnDespawn); idris_shot_additional_npc (actor 9, spawnDespawn); Player (actor 10, findInContext).

Entries: `Start 0` → 1; `idris_shot` → 1463.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 15 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnChangeIdleAnimEvent` | 3 | 649 / 994 | `/Data/RootChunk/sceneGraph/Data/graph/149/Data/events/1` |
| `scnDialogLineEvent` | 5 | 696 / 1119 | `/Data/RootChunk/sceneGraph/Data/graph/164/Data/events/0` |
| `scnGameplayTransitionEvent` | 11 | 68 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/6` |
| `scnIKEvent` | 22 | 68 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scnLookAtEvent` | 11 | 616 / 978 | `/Data/RootChunk/sceneGraph/Data/graph/147/Data/events/2` |
| `scnPlayRidAnimEvent` | 1 | 1420 / 1754 | `/Data/RootChunk/sceneGraph/Data/graph/268/Data/events/1` |
| `scnPlaySkAnimEvent` | 58 | 15 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 11 | 68 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/10` |
| `scneventsAttachPropToNode` | 3 | 429 / 660 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/4` |
| `scneventsAttachPropToPerformer` | 3 | 429 / 657 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/1` |
| `scneventsCameraParamsEvent` | 2 | 60 / 98 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/3` |
| `scneventsPlayRidCameraAnimEvent` | 1 | 1420 / 1784 | `/Data/RootChunk/sceneGraph/Data/graph/268/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 11 | 68 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/7` |
| `scneventsSocket` | 55 | 15 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsVFXEvent` | 16 | 15 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 8
- skeletal_animation: 5
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- speech: 4
- skeletal_animation, props_equipment, vfx, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, audio, vfx, socket_signal: 2
- skeletal_animation, vfx, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, audio, vfx: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, rid_actor, camera, rid_camera, socket_signal: 1

Raw SHA-256: `27e6e4b6a030cdff28e562bceb0fa7961671ea5e5e272b341366f47e4d4bf8fc`. Binary SHA-256: `5c5ec1d51b2c9df31dcb626e0d715d4a4ce1a057b103dab24c04e7903e303090`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq300\scenes\mq300_safehouse_interactions.scene" --events
```

