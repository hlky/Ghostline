# Love Rollercoaster: scene presentation

Journal identity: `quests/minor_quest/mq006_rollercoaster`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq006_rollercoaster.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene`

159 graph nodes, 197 edges; 43 event-bearing sections, 416 events; 102 screenplay lines, 21 screenplay options, 9 choice nodes.

Actors: jean (actor 0, spawnSet); anel (actor 1, spawnSet); darline (actor 2, spawnSet); farah (actor 3, spawnSet); sandley (actor 4, spawnSet); roller_coaster_cart (actor 5, spawner); Player (actor 6, findInContext).

Entries: `mq006_01_intro_in` → 1; `mq006_jean_post_q110_in` → 148; `darline_fake_default_in` → 158; `farah_fake_default_in` → 160; `anel_preview` → 167; `jean_preview` → 174; `old` → 336.

Exits: `mq006_01_intro_out` → 2; `StartJournal` → 73; `QuestTriggered` → 77.

End nodes: 2: `<omitted>`; 73: `NonTerminating`; 77: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 50 / 246 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/15` |
| `scnChangeIdleAnimEvent` | 34 | 5 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 85 | 5 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnGameplayTransitionEvent` | 2 | 217 / 825 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/13` |
| `scnIKEvent` | 4 | 217 / 808 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/1` |
| `scnLookAtEvent` | 106 | 5 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 103 | 5 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnUnmountEvent` | 2 | 217 / 824 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/12` |
| `scneventsEquipItemToPerformer` | 10 | 5 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 2 | 217 / 820 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/9` |
| `scneventsSocket` | 61 | 5 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 3 | 50 / 251 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/18` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 60 / 325 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 10
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation: 1
- speech, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- idle_animation, gaze: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `7febb7b24ce28e4fa26d8a5126a50c4ceed7c168255bf40fbd7e29e6009cc7b7`. Binary SHA-256: `6027939a010af667af9fbef0761da029b4c0ebdd1819a68a165dd44acc2509ca`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq006\scenes\mq006_01_intro.scene" --events
```

## `base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene`

235 graph nodes, 279 edges; 59 event-bearing sections, 333 events; 99 screenplay lines, 12 screenplay options, 10 choice nodes.

Actors: jean (actor 0, spawnSet); anel (actor 1, spawnSet); darline (actor 2, spawnSet); farah (actor 3, spawnSet); sandley (actor 4, spawnSet); johnny (actor 5, spawnDespawn); rollercoaster_cart (actor 6, spawner); Player (actor 7, findInContext).

Entries: `mq006_02_finale_in` → 1; `Old` → 444; `mq006_quest_end_chat_in` → 239; `mq006_jean_final_interaction_in` → 241; `RollercoasterSittingTest` → 497; `mq006_02_ride_standalone_in` → 509; `mq006_02_ride_no_quest` → 129; `ridestart` → 351; `old` → 816; `mq006_darlene_final_interaction_in` → 404.

Exits: `mq006_02_finale_out` → 2; `StartRollercoaster` → 40; `StartRollecoasterStandalone` → 520; `mq006_02_ride_standalone_out` → 538; `mq006_02_ride_no_quest_out` → 175.

End nodes: 2: `NonTerminating`; 40: `NonTerminating`; 175: `<omitted>`; 520: `NonTerminating`; 538: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 14 | 50 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/3` |
| `scnChangeIdleAnimEvent` | 12 | 8 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/19` |
| `scnDialogLineEvent` | 74 | 5 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 6 | 50 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/19` |
| `scnIKEvent` | 12 | 50 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/14` |
| `scnLookAtEvent` | 89 | 5 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnPlaySkAnimEvent` | 57 | 5 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnUnmountEvent` | 6 | 50 / 224 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 15 | 50 / 222 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/17` |
| `scneventsSocket` | 48 | 8 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 18
- gaze: 6
- speech, skeletal_animation, gaze: 4
- skeletal_animation, audio, socket_signal, animation_state: 4
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation: 3
- idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, audio, socket_signal, animation_state: 1
- speech, idle_animation: 1
- speech, socket_signal, animation_state: 1
- speech, gaze: 1
- idle_animation, gaze, socket_signal: 1
- idle_animation, socket_signal: 1

Raw SHA-256: `27c1666f70e6e861c82ae02ab9eeed19d313af5a139782c7bc11f4328c582fac`. Binary SHA-256: `00a86142503e41a765f04908241b6a1087f3824d6527fe05592277ec0c3df481`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq006\scenes\mq006_02_finale.scene" --events
```

