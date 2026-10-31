# War Pigs: scene presentation

Journal identity: `quests/minor_quest/mq041_corpo`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq041_corpo.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene`

17 graph nodes, 16 edges; 1 event-bearing sections, 9 events; 9 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Frank (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 270.

End nodes: 2: `<omitted>`; 270: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 9 | 8 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `012253e0e76fdc5860481e269ca0b26a9cc96d35c5ecaa7c21a90c95cabe3844`. Binary SHA-256: `ca0940fdd56f5cbf5a8332968919a0e3e9a95e5c32cd78d9b1ad595390d9cef0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq041\scenes\mq041_corpo_01_deadmans_switch.scene" --events
```

## `base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene`

167 graph nodes, 238 edges; 29 event-bearing sections, 301 events; 72 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: Frank (actor 0, spawnSet); johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `CYB-637601` → 808; `Start 2` → 975; `Start1` → 1195.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 34 | 29 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnDialogLineEvent` | 69 | 14 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnGameplayTransitionEvent` | 8 | 173 / 270 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/8` |
| `scnIKEvent` | 16 | 173 / 264 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/3` |
| `scnLookAtEvent` | 50 | 14 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 71 | 29 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnUnmountEvent` | 8 | 173 / 269 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 8 | 173 / 267 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/6` |
| `scneventsSocket` | 37 | 14 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 7
- speech, skeletal_animation, idle_animation: 4
- speech: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- speech, idle_animation: 2
- socket_signal: 2
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- gaze: 1

Raw SHA-256: `eb94dd0c9820709de15eff97bb92ab90fd1979919451c32f6c1d988377f9cd08`. Binary SHA-256: `b9e409b4af9877410039bcf0423676839ff7c4a223eeccd0b19f83bea9fb3c70`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq041\scenes\mq041_corpo_02_confrontation.scene" --events
```

