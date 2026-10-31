# Human Nature: scene presentation

Journal identity: `quests/side_quest/sq025_0_pickup`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq025_0_pickup.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq025\scenes\sq025_01_crash.scene`

20 graph nodes, 21 edges; 3 event-bearing sections, 28 events; 9 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `spawned_car_crash_in` → 60; `impact` → 146.

Exits: `spawned_car_crash_out` → 62; `exit` → 110; `impact_out` → 211.

End nodes: 62: `NonTerminating`; 110: `NonTerminating`; 211: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 253 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/0` |
| `scnDialogLineEvent` | 8 | 46 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnLookAtEvent` | 7 | 46 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnPlaySkAnimEvent` | 4 | 46 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/7` |
| `scneventsSocket` | 7 | 46 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `194e55980697fb2943905f4104f84052517110dfac42608e28dfe8f29cbf5a26`. Binary SHA-256: `849b9598dc68f1b833c5901653513da4077ff06d9533e0c29f2d49302effbfd1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_01_crash.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_03_reception.scene`

219 graph nodes, 263 edges; 36 event-bearing sections, 245 events; 83 screenplay lines, 14 screenplay options, 7 choice nodes.

Actors: Delamain_receptionist (actor 0, spawnSet); Delamain (actor 1, spawnSet); Stripper (actor 2, community); Old_Lady (actor 3, community); Maid (actor 4, community); Homeless (actor 5, community); Slacker (actor 6, community); Regular (actor 7, community); Corpo (actor 8, community); Homeless_2 (actor 9, community); Homeless_3 (actor 10, community); Player (actor 11, findInContext).

Entries: `refused_in` → 222; `delamain_compensation_in` → 1; `sq025_03_looping_finale_for_maid` → 1107; `chicken_in` → 238.

Exits: `refused_out` → 223; `delamain_compensation_out` → 2; `End1` → 684; `refused_before_tour_out` → 298; `exit` → 312.

End nodes: 2: `NonTerminating`; 223: `<omitted>`; 298: `NonTerminating`; 312: `<omitted>`; 684: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 12 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 56 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 6 | 12 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/24` |
| `scnIKEvent` | 12 | 12 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/13` |
| `scnLookAtEvent` | 47 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 30 | 12 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnUnmountEvent` | 6 | 12 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/23` |
| `scneventsSetAnimFeatureEvent` | 6 | 12 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/20` |
| `scneventsSocket` | 70 | 5 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 1 | 391 / 441 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- speech, socket_signal: 5
- skeletal_animation, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, idle_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx: 1
- gaze, socket_signal: 1
- speech, gaze: 1
- socket_signal: 1
- idle_animation, socket_signal: 1

Raw SHA-256: `78ad10eaa8899f4542b56898e9be2e52b0364eb5ff8fc074657f6f8b59da0cdd`. Binary SHA-256: `8a39725dfbf189273f51af61b74a0974d9259db677327dcc3729d07fb5445a53`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_03_reception.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_05_scan.scene`

1710 graph nodes, 2004 edges; 75 event-bearing sections, 235 events; 189 screenplay lines, 28 screenplay options, 14 choice nodes.

Actors: Delamain (actor 0, spawnSet); Angry (actor 1, spawnSet); Sad (actor 2, spawnSet); Manic (actor 3, spawnSet); Mean (actor 4, spawnSet); Suicidal (actor 5, spawnSet); Deep (actor 6, spawnSet); Scared (actor 7, spawnSet); GANG_MLS_F_02_ENUS_25 (actor 8, community); GANG_MLS_F_03_ENUS_20 (actor 9, community); GANG_MLS_F_01_ENUS_30 (actor 10, community); GANG_MLS_F_04_ENUS_25 (actor 11, community); cyberpsycho (actor 12, community); Sad_voice (actor 13, findInContext); Deep_vehicle (actor 14, community); Angry_vehicle (actor 15, community); Suicidal_vehicle (actor 16, community); Mean_vehicle (actor 17, community); Scared_vehicle (actor 18, community); Sad_vehicle (actor 19, community); Manic_vehicle (actor 20, community); Player (actor 21, findInContext).

Entries: `angry_in` → 4; `sad_in` → 6; `suicidal_in` → 7; `deep_in` → 8; `scared_in` → 10; `manic_in` → 11; `mean_in` → 12; `Start 12` → 3670; `Start 13` → 3689; `Start 14` → 3706; `Start 15` → 3723; `Start 16` → 3737; `Start 18` → 3758; `Start 26` → 7546; `mobile1` → 7677; `Start 28` → 7801; `beep_in` → 4549; `blasphemer_in` → 6383; `sad_in_talk` → 2926; `angry_in_talk` → 2954; `suicidal_in_talk` → 2955; `deep_in_talk` → 2956; `scared_in_talk` → 2957; `manic_in_talk` → 2958; `mean_in_talk` → 2959; `Start 23` → 6960; `Start 24` → 6967; `Start 25` → 6992.

Exits: `angry_out` → 131; `suicidal_out` → 132; `deep_out` → 133; `scared_out` → 134; `mean_out` → 135; `reward_out` → 136; `manic_out` → 137; `sad_out` → 138; `sad_damage` → 7771; `sad_water` → 7775; `sad_crowd` → 7798; `sad_death` → 7802; `End 9` → 6391.

End nodes: 131: `<omitted>`; 132: `<omitted>`; 133: `<omitted>`; 134: `<omitted>`; 135: `<omitted>`; 136: `<omitted>`; 137: `<omitted>`; 138: `<omitted>`; 6391: `<omitted>`; 7771: `NonTerminating`; 7775: `NonTerminating`; 7798: `NonTerminating`; 7802: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 91 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnDialogLineEvent` | 169 | 79 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 7933 / 7717 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/4` |
| `scnIKEvent` | 2 | 7933 / 7715 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/2` |
| `scnLookAtEvent` | 17 | 79 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |
| `scnPlaySkAnimEvent` | 4 | 1503 / 1464 | `/Data/RootChunk/sceneGraph/Data/graph/245/Data/events/1` |
| `scnUnmountEvent` | 1 | 7933 / 7721 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/7` |
| `scneventsCameraParamsEvent` | 3 | 6997 / 6162 | `/Data/RootChunk/sceneGraph/Data/graph/1023/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 7933 / 7719 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/6` |
| `scneventsSocket` | 33 | 79 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 40
- speech, socket_signal: 19
- speech, gaze, socket_signal: 2
- speech, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- idle_animation, gaze, socket_signal: 2
- speech, idle_animation, gaze: 1
- speech, skeletal_animation: 1
- idle_animation, gaze: 1
- gaze: 1
- gaze, socket_signal: 1
- camera: 1
- camera, socket_signal: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `249ac0c15568c48faedb121c325c5b673bfe319ccda854d8b28d8ee49cb8859d`. Binary SHA-256: `728ee318df921d11651256032dd465e82c0c8169ddf91bcf326349d842b2366a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_05_scan.scene" --events
```

