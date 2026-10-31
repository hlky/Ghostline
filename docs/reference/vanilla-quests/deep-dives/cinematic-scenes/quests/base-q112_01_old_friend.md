# Down on the Street: scene presentation

Journal identity: `quests/main_quest/act_01/q112_01_old_friend`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q112_01_old_friend.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q112\scenes\q112_00a_meeting_phonecall.scene`

31 graph nodes, 39 edges; 6 event-bearing sections, 38 events; 19 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Takemura (actor 0, spawnSet); Wakako (actor 1, findInContext); V (actor 2, findInContext).

Entries: `q112_00a_phonecall_in` → 1.

Exits: `q112_00a_phonecall_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 19 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 3 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 8 | 4 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsSocket` | 3 | 4 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech: 1

Raw SHA-256: `45f53624e5757efa21262829d29fa407c25df1e2cdd777710b9b03561a6485d3`. Binary SHA-256: `c37a74f844ba82d31c9d1e4cd4a4b218a33154aa12a5847d8509113fee09bce7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_00a_meeting_phonecall.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_00b_secret_meeting.scene`

437 graph nodes, 576 edges; 88 event-bearing sections, 626 events; 152 screenplay lines, 25 screenplay options, 11 choice nodes.

Actors: Takemura (actor 0, spawnSet); Cyberninja_Oda (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); cat (actor 3, spawner); q112_00b_ship (actor 4, spawner); q112_takemura_car_preview (actor 5, spawner); q112_oda_car_preview (actor 6, spawner); V (actor 7, findInContext).

Entries: `q112_00b_secret_meeting_in` → 1; `q112_00b_clone_question_in` → 1490; `takemura_exit_car` → 3778; `get_on_mr_t_car` → 3407; `q112_00b_skip_travel_in` → 2353; `q112_00b_johnny_despawner_in` → 3858.

Exits: `q112_00b_clone_question_out` → 1488; `q112_00b_secret_meeting_out` → 57; `takemura_exit_car_out` → 3782; `q112_00b_skip_travel_out` → 2374; `q112_00b_oda_exit` → 3492; `q112_00b_johnny_despawner_out` → 3866; `q112_00b_cut_driving` → 2405; `cargo_av` → 1313.

End nodes: 57: `NonTerminating`; 1313: `NonTerminating`; 1488: `NonTerminating`; 2374: `<omitted>`; 2405: `NonTerminating`; 3492: `NonTerminating`; 3782: `<omitted>`; 3866: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 540 / 678 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/5` |
| `scnChangeIdleAnimEvent` | 9 | 22 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnDialogLineEvent` | 122 | 10 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 3913 / 3143 | `/Data/RootChunk/sceneGraph/Data/graph/424/Data/events/0` |
| `scnGameplayTransitionEvent` | 11 | 915 / 822 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/7` |
| `scnIKEvent` | 24 | 915 / 815 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/1` |
| `scnLookAtAdvancedEvent` | 9 | 129 / 347 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/13` |
| `scnLookAtEvent` | 134 | 10 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 2817 / 2386 | `/Data/RootChunk/sceneGraph/Data/graph/299/Data/events/0` |
| `scnPlaySkAnimEvent` | 158 | 10 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 540 / 690 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/10` |
| `scnUnmountEvent` | 10 | 915 / 821 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/6` |
| `scneventsCameraParamsEvent` | 8 | 540 / 689 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 14 | 915 / 819 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/5` |
| `scneventsSocket` | 117 | 10 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 17
- skeletal_animation, socket_signal: 12
- speech, skeletal_animation, gaze: 8
- skeletal_animation: 7
- speech: 6
- speech, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, gaze, socket_signal: 2
- skeletal_animation, gaze: 2
- camera: 2
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal, animation_state: 1
- idle_animation, camera, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, camera, socket_signal: 1
- gaze: 1
- animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- ik, gameplay_transition, socket_signal, animation_state: 1
- skeletal_animation, audio, animation_state, mount_workspot: 1
- idle_animation, gameplay_action: 1

Raw SHA-256: `092f63081d25fc33d204c11882755074038a4d614e0b7a781bd2249084818a6b`. Binary SHA-256: `0bdcd3020814be29bfe696d7cd13ae8518192aadee451fb7199d9417d775d685`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_00b_secret_meeting.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_00c_wakako.scene`

416 graph nodes, 602 edges; 76 event-bearing sections, 792 events; 146 screenplay lines, 35 screenplay options, 23 choice nodes.

Actors: Takemura (actor 0, spawnSet); Johnny (actor 1, spawnSet); Wakako (actor 2, spawnSet); Old_man (actor 3, community); Guard (actor 4, community); hooker (actor 5, spawnDespawn); q112_takemura_van (actor 6, spawner); V (actor 7, findInContext).

Entries: `test_prev` → 2156; `q112_00c_parade_meeting_clone_in` → 950; `q112_12_hideshi_scene_in` → 1913; `q112_00c_wakako_in` → 118; `q112_00c_car_exit_after_takemura_drive` → 1958; `q112_00c_takemura_fluff_in` → 141; `Start 5` → 1500.

Exits: `q112_00c_parade_meeting_clone_out` → 954; `q112_12_hideshi_scene_out` → 1914; `q112_00c_wakako_out` → 123; `End 5` → 1961; `q112_00c_takemura_fluff_out` → 144; `Cleanup` → 504.

End nodes: 123: `NonTerminating`; 144: `Terminating`; 504: `Terminating`; 954: `Terminating`; 1914: `Terminating`; 1961: `Terminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 2250 / 3070 | `/Data/RootChunk/sceneGraph/Data/graph/393/Data/events/1` |
| `scnChangeIdleAnimEvent` | 23 | 4 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/11` |
| `scnDialogLineEvent` | 119 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnGameplayTransitionEvent` | 9 | 115 / 348 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/14` |
| `scnIKEvent` | 18 | 115 / 337 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scnLookAtAdvancedEvent` | 8 | 108 / 224 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/9` |
| `scnLookAtEvent` | 260 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnPlaySkAnimEvent` | 152 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/6` |
| `scnPoseCorrectionEvent` | 13 | 20 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/8` |
| `scnUnmountEvent` | 9 | 115 / 347 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/13` |
| `scneventsAttachPropToPerformer` | 2 | 363 / 694 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 177 / 509 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 9 | 115 / 343 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/10` |
| `scneventsSocket` | 166 | 4 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 13
- speech, skeletal_animation, gaze, socket_signal: 11
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 5
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation: 3
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, gaze: 2
- gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 2
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, props_equipment, socket_signal: 1
- speech: 1
- gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `c15426f0c0aeb790a6dcaf4fbe341328a7ed444da2d40f9ae26028fe4cf2a2b4`. Binary SHA-256: `99a5e0234bcb1761d32b730f79cd081bf97be83d68e4b845554a6ff745fe39fd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_00c_wakako.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_01_market.scene`

208 graph nodes, 266 edges; 46 event-bearing sections, 343 events; 82 screenplay lines, 20 screenplay options, 11 choice nodes.

Actors: Takemura (actor 0, spawnSet); Cook (actor 1, community); Johnny (actor 2, spawnSet); Security_01 (actor 3, community); Security_02 (actor 4, community); Client (actor 5, spawner); Construction_worker_01 (actor 6, spawnDespawn); Construction_worker_02 (actor 7, spawnDespawn); V (actor 8, findInContext).

Entries: `Start 4` → 1835; `briefing_in` → 1837; `q112_01_market_in` → 15; `Start 5` → 2404; `q112_01_wait_in` → 1548.

Exits: `End 0` → 1838; `q112_01_market_out` → 16; `q112_01_wait_out` → 1558; `q112_01_wait_spawn_takemura` → 1560; `Cleanup` → 1207.

End nodes: 16: `NonTerminating`; 1207: `<omitted>`; 1558: `<omitted>`; 1560: `NonTerminating`; 1838: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 786 / 587 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/5` |
| `scnChangeIdleAnimEvent` | 21 | 17 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 70 | 17 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 407 / 232 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/8` |
| `scnIKEvent` | 6 | 407 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scnLookAtEvent` | 73 | 17 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 93 | 17 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 2 | 1450 / 789 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/11` |
| `scnUnmountEvent` | 3 | 407 / 231 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/7` |
| `scneventsAttachPropToPerformer` | 3 | 786 / 586 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/4` |
| `scneventsAttachPropToWorld` | 1 | 786 / 589 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/7` |
| `scneventsPlayRidCameraAnimEvent` | 1 | 2294 / 1482 | `/Data/RootChunk/sceneGraph/Data/graph/181/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 3 | 407 / 229 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/6` |
| `scneventsSocket` | 61 | 17 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, skeletal_animation, gaze, socket_signal: 5
- gaze: 4
- speech, gaze: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, props_equipment: 1
- skeletal_animation: 1
- speech, idle_animation: 1
- speech, socket_signal: 1
- camera, rid_camera: 1
- socket_signal, animation_state: 1

Raw SHA-256: `f8b8d4b3a9d6ec0f05e00a0b6199825da29ba4e9ea25e484a0b32d64de323cb8`. Binary SHA-256: `0c43b697b8754182fce25c80e13ddac40ac8d06361fad470db13a31aea5b4ced`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_01_market.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_01_market_02.scene`

404 graph nodes, 531 edges; 100 event-bearing sections, 665 events; 140 screenplay lines, 29 screenplay options, 17 choice nodes.

Actors: Takemura (actor 0, spawnSet); Cook (actor 1, community); Johnny (actor 2, spawnDespawn); Security_01 (actor 3, community); Security_02 (actor 4, community); Client (actor 5, spawner); Construction_worker_01 (actor 6, spawnDespawn); Construction_worker_02 (actor 7, spawnDespawn); V (actor 8, findInContext).

Entries: `q112_01_market_02_in` → 15; `q112_01_wakako_drive_clone_in` → 1585; `the_plan` → 1925.

Exits: `q112_01_market_02_out` → 16; `End1` → 2096; `Cleanup` → 2107; `q112_01_wakako_drive_clone_out` → 1587.

End nodes: 16: `NonTerminating`; 1587: `NonTerminating`; 2096: `<omitted>`; 2107: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 44 | 78 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/9` |
| `scnChangeIdleAnimEvent` | 23 | 421 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scnDialogLineEvent` | 107 | 54 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 8 | 1009 / 444 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/9` |
| `scnIKEvent` | 16 | 1009 / 436 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/2` |
| `scnLookAtEvent` | 92 | 54 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 156 | 78 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnPoseCorrectionEvent` | 8 | 427 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/8` |
| `scnUnmountEvent` | 8 | 1009 / 443 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/8` |
| `scneventsAttachPropToPerformer` | 39 | 1449 / 840 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/10` |
| `scneventsAttachPropToWorld` | 38 | 1381 / 770 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/12` |
| `scneventsCameraParamsEvent` | 5 | 1285 / 556 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 8 | 1009 / 441 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/7` |
| `scneventsSocket` | 113 | 54 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 21
- props_equipment, audio: 18
- speech, skeletal_animation, gaze, socket_signal: 13
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech: 5
- gaze: 5
- speech, gaze, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation: 2
- socket_signal: 2
- camera: 2
- speech, skeletal_animation, gaze, audio: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal: 1

Raw SHA-256: `c5a05a8f5609df4359063a09f2c9b1c41f7a018d1ee2548306991e5beef03a1b`. Binary SHA-256: `bad465232a7558c0cffada2db6d1ca32e2fb3f45214371f79f8db44506137e13`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_01_market_02.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_01b_market_phonecall.scene`

37 graph nodes, 41 edges; 2 event-bearing sections, 28 events; 11 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Takemura (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `q112_01_tak_rec_done_in` → 411; `q112_01_market_in` → 15.

Exits: `q112_01_tak_rec_done_out` → 412; `q112_01_market_out` → 16.

End nodes: 16: `<omitted>`; 412: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 413 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 11 | 413 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnLookAtEvent` | 6 | 413 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 7 | 413 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 2

Raw SHA-256: `b5c8364a0193ea067a1b44872721e49f719eb38f5791cc047e0c5abc0a89cfd8`. Binary SHA-256: `920c315dae7fdc2d72c515c86f65ef0b7d1d190dde8357d005d952c9fb9beffc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_01b_market_phonecall.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_06_warehouse.scene`

47 graph nodes, 59 edges; 8 event-bearing sections, 24 events; 22 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Takemura (actor 0, spawnDespawn); V (actor 1, findInContext).

Entries: `q112_06_warehouse_in` → 1; `q112_06_it_worked_clone_in` → 153.

Exits: `q112_06_warehouse_out` → 2; `search_avs` → 150; `q112_06_it_worked_clone_out` → 155; `antenna_moves` → 73.

End nodes: 2: `<omitted>`; 73: `NonTerminating`; 150: `NonTerminating`; 155: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 22 | 41 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scneventsSocket` | 2 | 41 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, socket_signal: 2

Raw SHA-256: `3ed35139eeeb4d909772623075a52b7071d6c31be8a460f72db38aca469a4529`. Binary SHA-256: `3568f459e5f3b68ddea384819529c82afc9e0d7da02a510e8b200f79e6b291f1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_06_warehouse.scene" --events
```

## `base\quest\primary_characters\vsets\vset_v.scene`

422 graph nodes, 365 edges; 171 event-bearing sections, 171 events; 171 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: vset_v (actor 0, findInContext).

Entries: `battlecry_curse` → 14; `scene_thanks` → 864; `scene_thanks_var_1` → 866; `scene_thanks_var_2` → 871; `scene_thanks_var_3` → 874; `battlecry_curse_var_1` → 29; `battlecry_curse_var_2` → 30; `interrupt` → 31; `scene_insult` → 879; `scene_insult_var_1` → 881; `interrupt_var_1` → 35; `interrupt_var_2` → 36; `scene_insult_var_2` → 886; `return` → 41; `follower_end_var_1` → 1311; `follower_end_var_2` → 1312; `scene_insult_var_3` → 889; `return_var_1` → 43; `follower_end_var_3` → 1313; `return_var_2` → 44; `follower_end` → 1314; `scene_insult_var_4` → 892; `scene_insult_var_5` → 895; `gp_vehicle_steal` → 481; `gp_vehicle_steal_var_1` → 483; `yelling_happy` → 1331; `gp_vehicle_steal_var_2` → 488; `gp_vehicle_steal_var_3` → 491; `yelling_happy_var_1` → 1340; `scene_holocall_start` → 917; `yelling_happy_var_2` → 1341; `yelling_happy_var_3` → 1342; `scene_holocall_start_var_1` → 919; `gp_vehicle_reckless` → 496; `gp_vehicle_reckless_var_1` → 498; `scene_holocall_start_var_2` → 924; `gp_vehicle_reckless_var_2` → 503; `scene_holocall_end` → 929; `gp_vehicle_reckless_var_3` → 506; `scene_holocall_end_var_1` → 931; `gp_vehicle_destroyed` → 511; `scene_holocall_end_var_2` → 936; `gp_vehicle_destroyed_var_1` → 513; `scene_crowd` → 940; `gp_vehicle_destroyed_var_2` → 518; `scene_crowd_var_1` → 942; `gp_vehicle_v_hit` → 522; `scene_crowd_var_2` → 947; `gp_vehicle_v_hit_var_1` → 524; `gp_vehicle_v_hit_var_2` → 529; `gp_vehicle_v_hit_var_3` → 532; `interrupt_phone` → 113; `interrupt_phone_var_1` → 117; `interrupt_phone_var_2` → 118; `timelapse` → 126; `reaction_wtf` → 974; `timelapse_var_1` → 128; `timelapse_var_2` → 129; `reaction_wtf_var_1` → 976; `reaction_wtf_var_2` → 981; `generic_7` → 1407; `reaction_wtf_var_3` → 984; `generic_9` → 1408; `interrupt_var_3` → 139; `generic_8` → 1409; `generic_3` → 1410; `generic_5` → 1411; `interrupt_var_4` → 142; `generic_6` → 1412; `reaction_inspect` → 989; `generic_10` → 1414; `reaction_inspect_var_1` → 991; `interrupt_var_5` → 145; `generic_1` → 1415; `generic_2` → 1416; `interrupt_var_6` → 148; `reaction_inspect_var_2` → 996; `interrupt_var_7` → 151; `reaction_inspect_var_3` → 999; `reaction_inspect_var_4` → 1002; `generic_4` → 1426; `generic_17` → 1427; `generic_19` → 1428; `reaction_inspect_var_5` → 1005; `generic_18` → 1429; `interrupt_var_8` → 160; `generic_13` → 1430; `generic_15` → 1431; `interrupt_var_9` → 162; `generic_16` → 1432; `generic_20` → 1433; `interrupt_var_10` → 164; `generic_11` → 1434; `generic_12` → 1435; `reaction_hostiles` → 1012; `generic_14` → 1436; `generic_27` → 1437; `reaction_hostiles_var_1` → 1014; `generic_29` → 1438; `generic_28` → 1439; `generic_23` → 1440; `generic_25` → 1441; `generic_26` → 1442; `reaction_hostiles_var_2` → 1019; `generic_30` → 1443; `interrupt_phone_var_3` → 174; `generic_21` → 1444; `interrupt_phone_var_4` → 175; `generic_22` → 1445; `reaction_hostiles_var_3` → 1022; `generic_24` → 1446; `generic_sickness_1` → 1447; `generic_sickness_3` → 1448; `reaction_hostiles_var_4` → 1025; `generic_sickness_2` → 1449; `interrupt_phone_var_5` → 180; `interrupt_phone_var_6` → 181; `reaction_hostiles_var_5` → 1028; `generic_sickness_4` → 1453; `interrupt_phone_var_7` → 185; `reaction_surprise` → 1035; `reaction_surprise_var_1` → 1037; `generic_sickness` → 1461; `return_var_3` → 196; `return_var_4` → 197; `return_var_5` → 202; `return_var_6` → 203; `return_var_7` → 207; `reaction_surprise_var_2` → 1056; `return_var_8` → 211; `return_var_9` → 212; `sts_wat_kab_04_distract_01` → 1905; `reaction_surprise_var_3` → 1059; `return_var_10` → 214; `reaction_curse` → 1064; `q112_parade_speech_sickness_in` → 1911; `reaction_curse_var_1` → 1066; `character_creation` → 1916; `reaction_curse_var_2` → 1071; `reaction_curse_var_3` → 1074; `battlecry_curse_var_3` → 228; `battlecry_curse_var_4` → 229; `reaction_curse_var_4` → 1077; `reaction_curse_var_5` → 1080; `battlecry_curse_var_5` → 234; `battlecry_curse_var_6` → 235; `battlecry_curse_var_7` → 238; `battlecry_curse_var_8` → 239; `reaction_happy` → 1087; `reaction_happy_var_1` → 1089; `battlecry_curse_var_9` → 246; `battlecry_curse_var_10` → 247; `reaction_happy_var_2` → 1094; `reaction_happy_var_3` → 1097; `generic_vendor_v1` → 1946; `reaction_shocked` → 1102; `generic_vendor_v2` → 1949; `reaction_shocked_var_1` → 1104; `generic_vendor_v3` → 1954; `reaction_shocked_var_2` → 1109; `reaction_shocked_var_3` → 1112; `generic_vendor_v4` → 1961; `reaction_sickness` → 1117; `reaction_sickness_01_var_1` → 1119; `reaction_sickness_01_var_2` → 1124; `hint_check` → 1136; `hint_check_var_1` → 1138; `hint_check_var_2` → 1143; `hint_check_var_3` → 1146; `hint_check_var_4` → 1149; `scene_johnny_move` → 1155; `scene_johnny_move_var_2` → 1162; `scene_johnny_move_var_3` → 1164; `scene_johnny_move_var_1` → 1170; `scene_johnny_shoot` → 1172; `scene_johnny_shoot_var_2` → 1175; `scene_johnny_shoot_var_3` → 1177; `scene_johnny_shoot_var_1` → 1179; `reaction_sickness_02_var_1` → 1195; `reaction_sickness_02_var_2` → 1196; `combat_ally_check` → 352; `combat_ally_check_var_1` → 354; `timelapse_var_3` → 780; `combat_ally_check_var_2` → 359; `timelapse_var_4` → 783; `combat_ally_check_var_3` → 362; `timelapse_var_5` → 786; `combat_ally_cover` → 367; `combat_ally_cover_var_1` → 369; `reaction_sickness_03_var_1` → 1219; `reaction_sickness_03_var_2` → 1220; `combat_ally_cover_var_2` → 374; `combat_ally_cover_var_3` → 377; `combat_ally_stealth` → 382; `combat_ally_stealth_var_1` → 384; `combat_ally_stealth_var_2` → 389; `combat_ally_stealth_var_3` → 392; `reaction_sickness_04_var_1` → 1242; `reaction_sickness_04_var_2` → 1243; `combat_ally_warning` → 397; `combat_ally_warning_var_1` → 399; `combat_ally_warning_var_2` → 410; `combat_ally_warning_var_3` → 413; `reaction_sickness_05_var_1` → 1265; `reaction_sickness_05_var_2` → 1266.

Exits: `timelapse_output` → 1297.

End nodes: 1297: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 171 | 16 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 171

Raw SHA-256: `a86e2b56dfac6fd163b0014605c3555f094870a69e0dc88b51809ee9d3e6c7dd`. Binary SHA-256: `816152da18c67c66bd850c38e721940f541c31737e689f287f3b0f09756a434a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\primary_characters\vsets\vset_v.scene" --events
```

