# Play It Safe: scene presentation

Journal identity: `quests/main_quest/act_01/q112_03_dashi_parade`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q112_03_dashi_parade.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q101\scenes\q101_08_takemura_v_room.scene`

325 graph nodes, 381 edges; 84 event-bearing sections, 801 events; 243 screenplay lines, 49 screenplay options, 16 choice nodes.

Actors: takemura (actor 0, spawnSet); takemura_phone (actor 1, spawnSet); Tom (actor 2, community); Johnny (actor 3, spawnDespawn); toms_client6 (actor 4, community); suit1 (actor 5, community); suit2 (actor 6, community); client1 (actor 7, community); client2 (actor 8, community); client3 (actor 9, community); client4 (actor 10, community); client5 (actor 11, community); lady (actor 12, community); customer7 (actor 13, community); waitress (actor 14, community); v (actor 15, findInContext).

Entries: `v_flat_in` → 1; `call_in` → 45; `cup_in` → 2031; `Start 4` → 758; `q112_takemura_clone` → 1462.

Exits: `v_flat_out` → 2; `call_out` → 46; `End 4` → 1464.

End nodes: 2: `NonTerminating`; 46: `<omitted>`; 1464: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 18 | 69 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/6` |
| `scnChangeIdleAnimEvent` | 31 | 69 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnDialogLineEvent` | 158 | 47 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnGameplayTransitionEvent` | 11 | 105 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/20` |
| `scnIKEvent` | 22 | 105 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/13` |
| `scnLookAtAdvancedEvent` | 1 | 202 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scnLookAtEvent` | 156 | 47 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 188 | 66 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnPoseCorrectionEvent` | 10 | 105 / 203 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/22` |
| `scnUnmountEvent` | 11 | 105 / 195 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/19` |
| `scneventsAttachPropToPerformer` | 7 | 69 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scneventsAttachPropToWorld` | 3 | 173 / 267 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/6` |
| `scneventsCameraParamsEvent` | 3 | 69 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 11 | 105 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/16` |
| `scneventsSocket` | 170 | 66 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/3` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1337 / 2272 | `/Data/RootChunk/sceneGraph/Data/graph/201/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 15
- skeletal_animation, gaze: 11
- skeletal_animation: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- skeletal_animation, gaze, socket_signal: 4
- speech: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze, socket_signal, animation_state: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation: 2
- speech, gaze, socket_signal: 2
- idle_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 1
- skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `319646b526930fecabfd3ac649c1272da642c5e0eaea6af9745144f189e363d4`. Binary SHA-256: `56b99f3de7037c8bf46a0c76b2233fb932fd0463575c604e457e90401b8e4750`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q101\scenes\q101_08_takemura_v_room.scene" --events
```

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

## `base\quest\main_quests\part1\q112\scenes\q112_03_reconnaissance.scene`

511 graph nodes, 652 edges; 89 event-bearing sections, 291 events; 136 screenplay lines, 26 screenplay options, 24 choice nodes.

Actors: Takemura (actor 0, spawnSet); Corrupt_Guard (actor 1, community); V (actor 2, findInContext).

Entries: `q112_03_rec_enter_in` → 11; `Downstairs_prev_elevator_up` → 3772; `q112_03_rec_arrived_in` → 20; `hack` → 2414; `Start 10` → 3832; `scanning_preview` → 3855; `q112_03_takemura_leaves_in` → 2134; `sq021_nothing_left_in` → 2289; `Downstairs_prev_elevator_down` → 3749.

Exits: `q112_03_rec_enter_out` → 18; `q112_03_rec_out` → 225; `show_scanning_component` → 2132; `pipes` → 793; `q112_03_takemura_leaves_out` → 2209; `sq021_nothing_left_out` → 2290; `Cleanup` → 2298.

End nodes: 18: `<omitted>`; 225: `NonTerminating`; 793: `NonTerminating`; 2132: `NonTerminating`; 2209: `<omitted>`; 2290: `<omitted>`; 2298: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 203 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/4` |
| `scnChangeIdleAnimEvent` | 5 | 214 / 131 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scnDialogLineEvent` | 78 | 12 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 44 | 27 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnPlaySkAnimEvent` | 78 | 203 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/1` |
| `scneventsAttachPropToPerformer` | 1 | 1885 / 1140 | `/Data/RootChunk/sceneGraph/Data/graph/165/Data/events/4` |
| `scneventsAttachPropToWorld` | 1 | 203 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/7` |
| `scneventsSocket` | 73 | 27 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 16
- skeletal_animation, socket_signal: 16
- speech: 13
- speech, socket_signal: 10
- speech, gaze: 8
- skeletal_animation, audio, socket_signal: 6
- socket_signal: 4
- skeletal_animation, gaze, audio, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `cceca32631832b1ebcecbd3667c3e4f47795fc1db8ae94a6573e66425e039663`. Binary SHA-256: `953b0fc48178270730482bda089920e9dca1b5782fab32a1defa91e8739db4f5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_03_reconnaissance.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_04_takemura.scene`

248 graph nodes, 321 edges; 68 event-bearing sections, 486 events; 125 screenplay lines, 31 screenplay options, 12 choice nodes.

Actors: Takemura (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); cat (actor 2, spawner); Guard (actor 3, community); V (actor 4, findInContext).

Entries: `q112_04_takemura_in` → 1.

Exits: `q112_04_takemura_out` → 2; `q101_takemura_clone` → 1802; `End1` → 1631; `cleanup` → 2102.

End nodes: 2: `NonTerminating`; 1631: `NonTerminating`; 1802: `NonTerminating`; 2102: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 421 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/3` |
| `scnChangeIdleAnimEvent` | 18 | 528 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scnDialogLineEvent` | 111 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 421 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/14` |
| `scnIKEvent` | 8 | 421 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnLookAtEvent` | 111 | 160 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scnPlaySkAnimEvent` | 112 | 38 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnUnmountEvent` | 4 | 421 / 143 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/13` |
| `scneventsAttachPropToPerformer` | 1 | 528 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scneventsAttachPropToWorld` | 1 | 528 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/9` |
| `scneventsCameraParamsEvent` | 4 | 160 / 98 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 4 | 421 / 139 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/10` |
| `scneventsSocket` | 104 | 38 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 17
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- speech, skeletal_animation, gaze: 7
- skeletal_animation, socket_signal: 5
- speech, gaze, socket_signal: 4
- gaze: 4
- socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, idle_animation, gaze, socket_signal: 2
- camera: 2
- speech: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation, gaze, audio, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, idle_animation: 1
- speech, gaze: 1
- camera, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, audio: 1
- skeletal_animation, audio, socket_signal: 1

Raw SHA-256: `6efa178305e7043addbe6a9e765f1241d06be2d3559386021f2f17bbffb61482`. Binary SHA-256: `34b93c3009397b12d9f5108546ee0500068d833369b47a925f39b249cad96945`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_04_takemura.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_05_infiltration.scene`

86 graph nodes, 88 edges; 21 event-bearing sections, 73 events; 46 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Takemura (actor 0, spawnSet); Takemura_Voice (actor 1, findInContext); takemura_van (actor 2, spawner); V (actor 3, findInContext).

Entries: `q112_05_ifiltration_in` → 1; `q112_05_inside_in` → 36; `q112_05_reinforcements_in` → 128; `q112_05_takemura_chatter_in` → 133; `preview` → 401; `q112_05_van_inside_in` → 146; `q112_05_after_guard_in` → 163.

Exits: `q112_05_van_guard_out` → 179; `q112_05_ifiltration_out` → 26; `q112_05_inside_out` → 39; `q112_05_reinforcements_out` → 131; `End1` → 80.

End nodes: 26: `NonTerminating`; 39: `<omitted>`; 80: `<omitted>`; 131: `<omitted>`; 179: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 19 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 40 | 14 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 281 / 259 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/8` |
| `scnIKEvent` | 2 | 281 / 251 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/1` |
| `scnLookAtEvent` | 4 | 22 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 13 | 14 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 193 / 215 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/0` |
| `scnUnmountEvent` | 1 | 281 / 258 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 1 | 281 / 256 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/6` |
| `scneventsSocket` | 6 | 19 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- gaze: 2
- speech, skeletal_animation: 1
- speech, idle_animation, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation: 1
- socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1

Raw SHA-256: `8cbe6df46ca11eca3b3edc21c50d3c8a378b0a52affb277e5031d2e86ac2e3ca`. Binary SHA-256: `3921b953418bd583620afea7f9d65eab6fbbda1c58806128fe9e382e1826962b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_05_infiltration.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_05c_guard_fluff.scene`

89 graph nodes, 90 edges; 15 event-bearing sections, 85 events; 35 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: infiltration_enemy_guard_01 (actor 0, community); infiltration_worker_03 (actor 1, community); guard_officer_03 (actor 2, community); guard_officer_10 (actor 3, community); guard_08 (actor 4, community); Corrupt_Guard (actor 5, community); Gate_Guard (actor 6, community); civilian_18 (actor 7, community); V (actor 8, findInContext).

Entries: `q112_05c_corrupt_in` → 88; `q112_05c_guard_door_in` → 175; `q112_05c_chats_in` → 51; `q112_05c_wrong_gate_in` → 144.

Exits: `q112_05c_guard_door_out` → 245; `q112_05c_corrupt_out` → 89; `End1` → 330; `End2` → 333; `q112_05c_guard_door_clone` → 182; `q112_05c_corrupt_fail` → 109; `q112_05c_civilian_18_clone` → 282; `q112_05c_chats_out` → 52; `q112_05c_wrong_gate_out` → 147.

End nodes: 52: `<omitted>`; 89: `NonTerminating`; 109: `NonTerminating`; 147: `<omitted>`; 182: `NonTerminating`; 245: `<omitted>`; 282: `NonTerminating`; 330: `<omitted>`; 333: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 102 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scnDialogLineEvent` | 27 | 56 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 186 / 252 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/9` |
| `scnIKEvent` | 2 | 186 / 238 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 111 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scnLookAtEvent` | 9 | 102 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnPlaySkAnimEvent` | 24 | 102 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnUnmountEvent` | 1 | 186 / 251 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 1 | 186 / 241 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/4` |
| `scneventsSocket` | 14 | 102 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- idle_animation, gaze: 1
- idle_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `081183b30a31018081ca895b1c1789c266507f1345383bcab4f311ca289041c5`. Binary SHA-256: `a8128dbe549c6b6ed484a0b9f83aeac28ee484b495788e59f2bcd71e7ca5cb76`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_05c_guard_fluff.scene" --events
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

## `base\quest\main_quests\part1\q112\scenes\q112_06b_parade_meeting.scene`

76 graph nodes, 96 edges; 16 event-bearing sections, 128 events; 46 screenplay lines, 7 screenplay options, 4 choice nodes.

Actors: Takemura (actor 0, spawnSet); Sniper_01 (actor 1, spawnSet); Sniper_02 (actor 2, spawnSet); Sniper_03 (actor 3, spawnSet); Cook (actor 4, community); V (actor 5, findInContext).

Entries: `q112_07_hideshi_poster_in` → 763; `q112_07_meet_takemura_in` → 176.

Exits: `q112_07_meet_takemura_out` → 182; `End 6` → 499; `q112_07_wakako_clone` → 572; `q112_07_hideshi_poster_out` → 765.

End nodes: 182: `NonTerminating`; 499: `<omitted>`; 572: `NonTerminating`; 765: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 179 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 41 | 179 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 20 | 186 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnPlaySkAnimEvent` | 30 | 186 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scneventsAttachPropToPerformer` | 3 | 474 / 170 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 476 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/7` |
| `scneventsSocket` | 27 | 179 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 476 / 181 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 3
- speech: 2
- gaze: 2
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `8dbfe42a36810ab91dc9015e9c4f01003dd86b8927f5900f929c65ce62d83970`. Binary SHA-256: `e21f7bdfedbd10b235e5852e56791b08d436fba2988a9d6de72cf28f695be699`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_06b_parade_meeting.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_07_parade_intro.scene`

154 graph nodes, 194 edges; 33 event-bearing sections, 83 events; 77 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Takemura (actor 0, spawnSet); Sniper_01 (actor 1, spawnSet); Sniper_02 (actor 2, spawnSet); Sniper_03 (actor 3, spawnSet); Oda (actor 4, findInContext); Smasher (actor 5, findInContext); Cheer_01 (actor 6, community); Cheer_02 (actor 7, community); V (actor 8, findInContext).

Entries: `q112_07_phone_in` → 4; `q112_07_sniper_01_in` → 110; `q112_07_sniper_02_in` → 115; `q112_07_sniper_03_in` → 120; `q112_07_time_for_parade_in` → 140.

Exits: `q112_07_phone_out` → 5; `q112_07_sniper_01_out` → 113; `q112_07_sniper_02_out` → 117; `q112_07_sniper_03_out` → 122; `ninja_cable_idle_out` → 927; `q112_07_time_for_parade_out` → 141.

End nodes: 5: `<omitted>`; 113: `<omitted>`; 117: `<omitted>`; 122: `<omitted>`; 141: `<omitted>`; 927: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 73 | 45 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnLookAtEvent` | 1 | 142 / 206 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 142 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/4` |
| `scneventsCameraParamsEvent` | 2 | 848 / 772 | `/Data/RootChunk/sceneGraph/Data/graph/137/Data/events/4` |
| `scneventsSocket` | 3 | 142 / 213 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/5` |
| `scneventsVFXEvent` | 2 | 848 / 769 | `/Data/RootChunk/sceneGraph/Data/graph/137/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 30
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, camera, vfx, socket_signal: 1
- camera: 1

Raw SHA-256: `1a36d689ae2a108dee5a821a91284beffc43ae970943c11a2ae275a864cabe5e`. Binary SHA-256: `e30c50810e58e41f7bb8f32f82dff9bf8ec2c50ce289c9cce93b1a6978880803`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_07_parade_intro.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_07a_parade_gameplay_and_combat_routines.scene`

109 graph nodes, 103 edges; 31 event-bearing sections, 116 events; 71 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: guard_001 (actor 0, community); guard_002 (actor 1, community); guard_003 (actor 2, community); worker_001 (actor 3, community); worker_002 (actor 4, community); scene_01_man (actor 5, community); scene_01_woman (actor 6, community); scene_02_arasaka_01 (actor 7, community); scene_02_arasaka_02 (actor 8, community); scene_02_man_01 (actor 9, community); scene_02_man_03 (actor 10, community); scene_02_woman_02 (actor 11, community); scene_03_man (actor 12, community); scene_03_woman (actor 13, community); scene_04_man (actor 14, community); scene_05_woman_01 (actor 15, community); scene_05_woman_02 (actor 16, community); scene_06_agent (actor 17, community); scene_07_man_big (actor 18, community); Takemura (actor 19, findInContext); Smasher (actor 20, findInContext); Oda (actor 21, findInContext); Johnny (actor 22, spawnDespawn); V (actor 23, findInContext).

Entries: `construction_warning_int_in` → 110; `q112_07a_feed_in` → 121; `worker_001_002` → 13; `q112_07a_scene_01_in` → 21; `q112_07a_scene_02_in` → 26; `guard_001_002` → 137; `q112_07a_scene_03_in` → 31; `guard_004` → 142; `q112_07a_scene_04_in` → 36; `q112_07a_scene_05_in` → 47; `q112_07a_scene_06_in` → 51; `q112_07a_scene_07_in` → 56; `q112_07a_construction_spotted_in` → 72; `construction_refuge_in` → 81; `q112_07a_johnny_bridge_in` → 194; `construction_heatoff_in` → 92; `construction_enter_again_in` → 101.

Exits: `construction_warning_int_out` → 117; `worker_001_002_out` → 14; `q112_07a_feed_out` → 126; `q112_07a_scene_01_out` → 24; `guard_001_002_out` → 138; `q112_07a_scene_02_out` → 29; `guard_004_out` → 143; `q112_07a_scene_03_out` → 34; `q112_07a_scene_04_out` → 39; `q112_07a_scene_05_out` → 48; `q112_07a_scene_06_out` → 52; `q112_07a_scene_07_out` → 59; `q112_07a_construction_spotted_out` → 79; `construction_refuge_out` → 90; `costruction_heatoff_out` → 99; `q112_07a_johnny_bridge_out` → 210; `End1` → 104.

End nodes: 14: `<omitted>`; 24: `<omitted>`; 29: `<omitted>`; 34: `<omitted>`; 39: `<omitted>`; 48: `<omitted>`; 52: `<omitted>`; 59: `<omitted>`; 79: `<omitted>`; 90: `<omitted>`; 99: `<omitted>`; 104: `<omitted>`; 117: `<omitted>`; 126: `<omitted>`; 138: `<omitted>`; 143: `<omitted>`; 210: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 16 | 17 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 69 | 17 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 4 | 37 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnPlaySkAnimEvent` | 19 | 17 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsEquipItemToPerformer` | 1 | 199 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/0` |
| `scneventsSocket` | 5 | 37 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scneventsVFXEvent` | 2 | 145 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 14
- speech, skeletal_animation, idle_animation: 5
- speech, skeletal_animation: 4
- skeletal_animation, idle_animation, socket_signal: 2
- speech, idle_animation: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, vfx: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, gaze: 1

Raw SHA-256: `c0cee9037e584077bfba32d2279ad0a08f6028c926028bf6cbf4a68663a0099d`. Binary SHA-256: `54f0838c8b1fd8d88550f43cf2387f6c868320e65e0bc09bda2836de71d265eb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_07a_parade_gameplay_and_combat_routines.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_08_parade_speech.scene`

213 graph nodes, 238 edges; 36 event-bearing sections, 163 events; 75 screenplay lines, 7 screenplay options, 6 choice nodes.

Actors: Takemura (actor 0, findInContext); Hanako (actor 1, spawnDespawn); Oda (actor 2, spawnSet); Netrunner (actor 3, community); Takemura_holocall (actor 4, spawnSet); Hanako_song (actor 5, spawnSet); V (actor 6, findInContext).

Entries: `q112_08_speech_start` → 10; `q112_08_oda_intimidates_v_in` → 632; `q112_08_oda_no_choice_in` → 633; `q112_08_u_should_left_town_in` → 634; `q112_08_oda_about_takemura_in` → 635; `q112_08_before_camouflage_in` → 636; `q112_08_oda_last_words_in` → 637; `q112_08_lean_in` → 1052; `wire_idle` → 3553; `q112_08_takemura_about_mask_in` → 711; `q112_08_takemura_about_distance_in` → 714; `q112_08_takemura_oda_low_health_in` → 716; `q112_08_takemura_v_low_health_in` → 718; `q112_08_hanako_arrives_in` → 123; `idles_start` → 540; `q112_08_hanako_song_in` → 971.

Exits: `q112_08_speech_ninja_attack` → 11; `autosave` → 425; `q112_08_oda_intimidates_v_out` → 638; `q112_08_oda_no_choice_out` → 639; `q112_08_u_should_left_town_out` → 640; `q112_08_oda_about_takemura_out` → 641; `q112_08_before_camouflage_out` → 642; `q112_08_oda_last_words_out` → 643; `q112_08_speech_out` → 65; `wire_idle_out` → 3564; `q112_08_takemura_about_mask_out` → 722; `q112_08_takemura_about_distance_out` → 724; `q112_08_takemura_oda_low_health_out` → 726; `q112_08_takemura_v_low_health_out` → 728; `hanako_song_end` → 129; `q112_08_hanako_song_out` → 972; `idles_start_cleanup` → 989; `End1` → 1002; `Cleanup` → 608.

End nodes: 11: `NonTerminating`; 65: `NonTerminating`; 129: `NonTerminating`; 425: `NonTerminating`; 608: `<omitted>`; 638: `<omitted>`; 639: `<omitted>`; 640: `<omitted>`; 641: `<omitted>`; 642: `<omitted>`; 643: `<omitted>`; 722: `<omitted>`; 724: `<omitted>`; 726: `<omitted>`; 728: `<omitted>`; 972: `<omitted>`; 989: `NonTerminating`; 1002: `<omitted>`; 3564: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 390 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/7` |
| `scnChangeIdleAnimEvent` | 7 | 16 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 68 | 16 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 1 | 3242 / 846 | `/Data/RootChunk/sceneGraph/Data/graph/155/Data/events/3` |
| `scnIKEvent` | 6 | 390 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/5` |
| `scnLookAtEvent` | 2 | 16 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/51` |
| `scnPlaySkAnimEvent` | 46 | 16 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 1 | 3242 / 850 | `/Data/RootChunk/sceneGraph/Data/graph/155/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 1 | 3242 / 848 | `/Data/RootChunk/sceneGraph/Data/graph/155/Data/events/5` |
| `scneventsSocket` | 25 | 16 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 3 | 63 / 181 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- speech, socket_signal: 2
- skeletal_animation: 2
- skeletal_animation, idle_animation, ik, socket_signal: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, audio, socket_signal: 1
- ik: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1

Raw SHA-256: `668867b02fdad1f5e2cf4ad17b6fab0a51f8619d3f37b7a9c3b339ca3626e516`. Binary SHA-256: `c73b0c60e531c80042484895c9e75eb338dd49a7bea1318449d5e2e747518d1e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_08_parade_speech.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_09_parade_abduction.scene`

147 graph nodes, 179 edges; 24 event-bearing sections, 172 events; 59 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Takemura (actor 0, spawnSet); Hanako (actor 1, spawnSet); Yorinobu (actor 2, spawnSet); Victim (actor 3, community); Arasaka_Soldier (actor 4, community); Injured_Man (actor 5, community); Injured_Woman (actor 6, community); Gillean_Jordan (actor 7, community); Johnny (actor 8, spawnDespawn); V (actor 9, findInContext).

Entries: `q112_09_abduction_in` → 1; `q112_09_victim_death_in` → 173; `q112_09_johnny_in` → 625; `q112_09_injured_man_in` → 526; `q112_09_news54_in` → 531; `arasaka_soldier_combat` → 1099.

Exits: `q112_09_abduction_out` → 2; `q112_09_victim_death_combat` → 1133; `End 9` → 737; `q112_09_victim_death_out` → 183; `q112_09_johnny_out` → 632; `End 10` → 772; `q112_09_injured_man_out` → 529; `q112_09_news54_out` → 540.

End nodes: 2: `NonTerminating`; 183: `<omitted>`; 529: `<omitted>`; 540: `<omitted>`; 632: `NonTerminating`; 737: `<omitted>`; 772: `<omitted>`; 1133: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 15 | 161 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/2` |
| `scnDialogLineEvent` | 52 | 17 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 167 / 207 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/16` |
| `scnIKEvent` | 6 | 167 / 197 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/7` |
| `scnLookAtAdvancedEvent` | 3 | 515 / 405 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/3` |
| `scnLookAtEvent` | 28 | 17 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 35 | 17 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnUnmountEvent` | 3 | 167 / 206 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/15` |
| `scneventsAttachPropToPerformer` | 1 | 161 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/14` |
| `scneventsAttachPropToWorld` | 1 | 161 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 3 | 167 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/12` |
| `scneventsSocket` | 20 | 17 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/36` |
| `scneventsVFXEvent` | 2 | 161 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/16` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, gaze: 2
- speech, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation: 1
- idle_animation: 1
- skeletal_animation, socket_signal: 1
- gaze, socket_signal: 1
- gaze: 1

Raw SHA-256: `1dddc38c64f51e725843407c28760074f24d225e38ac0d71d08a9dd863f647a9`. Binary SHA-256: `b8ce55852de19fa2382b1d05675314485914597d708709dba30edd1d1ee08fff`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_09_parade_abduction.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_10_safe_house.scene`

418 graph nodes, 577 edges; 64 event-bearing sections, 528 events; 107 screenplay lines, 19 screenplay options, 9 choice nodes.

Actors: Takemura (actor 0, spawnSet); Hanako (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); arasaka_01 (actor 3, community); arasaka_02 (actor 4, community); arasaka_03 (actor 5, community); Takemura_holo (actor 6, spawnSet); arasaka_04 (actor 7, community); adam_smasher (actor 8, spawnSet); arasaka_end_01 (actor 9, community); arasaka_end_02 (actor 10, community); arasaka_end_03 (actor 11, community); arasaka_victim (actor 12, spawnDespawn); arasaka_victim_02 (actor 13, spawnDespawn); arasaka_victim_03 (actor 14, spawnDespawn); arasaka_no_react_01 (actor 15, community); arasaka_no_react_02 (actor 16, community); arasaka_no_react_03 (actor 17, community); av (actor 18, spawner); V (actor 19, findInContext).

Entries: `q112_10_phone_in` → 25; `q112_10_safe_house_in` → 38; `johnny_sickness_in` → 2335; `backedup line` → 2431; `q112_safe_house_combat` → 1035; `q112_arasaka_patrol_chat_001_in` → 1073; `q112_arasaka_raport_in` → 1076.

Exits: `q112_10_phone_out` → 26; `door_shot` → 1187; `End 10` → 2338; `arasaka_soldiers_appear` → 137; `q112_arasaka_patrol_chat_001_out` → 2854; `q112_arasaka_raport_out` → 2856; `q112_10_safe_house_out` → 216; `ai_command_takemura` → 604; `checkpoint` → 607; `av_gunfire_start` → 3709; `av_gunfire_stop` → 3711.

End nodes: 26: `<omitted>`; 137: `NonTerminating`; 216: `<omitted>`; 604: `NonTerminating`; 607: `NonTerminating`; 1187: `NonTerminating`; 2338: `<omitted>`; 2854: `<omitted>`; 2856: `<omitted>`; 3709: `NonTerminating`; 3711: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 41 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnChangeIdleAnimEvent` | 17 | 291 / 263 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/4` |
| `scnDialogLineEvent` | 96 | 27 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 6 | 366 / 506 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/20` |
| `scnIKEvent` | 12 | 366 / 498 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/13` |
| `scnLookAtEvent` | 102 | 27 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 99 | 69 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 406 / 548 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/3` |
| `scnUnmountEvent` | 6 | 366 / 505 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/19` |
| `scneventsAttachPropToPerformer` | 4 | 1132 / 1242 | `/Data/RootChunk/sceneGraph/Data/graph/147/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 1141 / 1256 | `/Data/RootChunk/sceneGraph/Data/graph/148/Data/events/1` |
| `scneventsCameraParamsEvent` | 3 | 982 / 1008 | `/Data/RootChunk/sceneGraph/Data/graph/112/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 6 | 366 / 501 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/16` |
| `scneventsSocket` | 110 | 69 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scneventsVFXEvent` | 55 | 406 / 550 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, skeletal_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- gaze: 5
- skeletal_animation, socket_signal: 4
- skeletal_animation, gaze, audio, vfx, socket_signal: 4
- socket_signal: 3
- speech, gaze: 2
- speech, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, camera, socket_signal: 2
- skeletal_animation, vfx, socket_signal: 2
- speech, gaze, audio: 1
- speech, gaze, vfx, animation_state: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx: 1
- skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, vfx, socket_signal: 1
- vfx: 1

Raw SHA-256: `511d509c4ff55d1f1ac495fd6517bafc2608654fe74c380e9d29c88b8313f24a`. Binary SHA-256: `327076165157bbfc1755a4e0df0b2d864493eefa83951d08ff9a2aa5c9f70ebb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_10_safe_house.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_11_shotgun.scene`

283 graph nodes, 392 edges; 69 event-bearing sections, 501 events; 179 screenplay lines, 24 screenplay options, 11 choice nodes.

Actors: Hanako (actor 0, findInContext); Johnny (actor 1, spawnDespawn); Doll (actor 2, community); delamain (actor 3, spawner); V (actor 4, findInContext).

Entries: `q112_11_shotgun_in` → 16; `johnny_prev` → 2503; `q115_reuse_in` → 1183.

Exits: `q112_11_shotgun_out` → 17; `q112_11_shotgun_out_non_canceling` → 768; `q115_reuse_out` → 1184; `doll_leaves` → 717.

End nodes: 17: `<omitted>`; 717: `NonTerminating`; 768: `NonTerminating`; 1184: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 57 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnChangeIdleAnimEvent` | 22 | 20 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 153 | 20 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 4 | 509 / 728 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/15` |
| `scnIKEvent` | 8 | 509 / 713 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/1` |
| `scnLookAtEvent` | 103 | 20 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 108 | 20 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 509 / 720 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/8` |
| `scnUnmountEvent` | 4 | 509 / 727 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/14` |
| `scneventsAttachPropToPerformer` | 3 | 267 / 450 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/6` |
| `scneventsAttachPropToWorld` | 2 | 760 / 1091 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/4` |
| `scneventsCameraParamsEvent` | 2 | 699 / 970 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 4 | 509 / 725 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/13` |
| `scneventsSocket` | 71 | 20 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsVFXEvent` | 6 | 267 / 449 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 14
- speech, skeletal_animation, gaze: 7
- speech, skeletal_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, socket_signal: 5
- gaze: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, audio, socket_signal: 3
- speech, audio: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, socket_signal: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, gaze: 1
- speech, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- audio: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `071bedb0f3b6b5cfcce0a24a47f14c7010aa5639720fab4591a927ce66655c49`. Binary SHA-256: `ae66c50534b3fd58ae6f3736f63d4c78cf560105355b24c29351a50e3519cb1c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_11_shotgun.scene" --events
```

## `base\quest\main_quests\part1\q113\scenes\q113_04_hanako_estate.scene`

255 graph nodes, 303 edges; 52 event-bearing sections, 227 events; 96 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: Takemura (actor 0, spawnSet); Hanako (actor 1, spawnSet); Arasaka_Estate_Guard_009 (actor 2, community); Arasaka_Estate_Guard_010 (actor 3, community); Netrunner (actor 4, community); Arasaka_Estate_guard_011 (actor 5, community); Arasaka_Estate_Guard_006 (actor 6, community); Arasaka_Estate_guard_007 (actor 7, community); Anders (actor 8, spawnSet); Hanako_holocall (actor 9, spawnSet); av (actor 10, spawnSet); q113_03a_thrax (actor 11, spawner); V (actor 12, findInContext).

Entries: `q113_04_hanako_in` → 1; `av_start_anim` → 1572; `q113_04_guard_fluff_takedown_in` → 559; `q113_04_exterior_in` → 44; `q113_04_inside_in` → 48; `q113_04_takemura_pickup_in` → 574; `q113_04_alert_in` → 323; `q113_04_close_in` → 69; `q113_04_done_in` → 73; `q113_04_before_av_in` → 80; `q113_04_v_leaves_in` → 354; `q113_04_takemura_takedown_in` → 139; `q113_04_takemura_takedown_done_in` → 144; `q113_04_takemura_netrunner_in` → 149; `q113_04_before_av_in_setup` → 686; `q113_04_mech_NEWNEW_in` → 688; `Start 18` → 2017; `q113_04_guard_fluff_in` → 237.

Exits: `takemura_exit` → 1291; `q113_04_hanako_out` → 2; `av_start_anim_end` → 1575; `q113_04_guard_fluff_out` → 1592; `q113_04_exterior_out` → 45; `q113_04_inside_out` → 49; `av_setup` → 572; `q113_04_takemura_pickup_out` → 577; `q113_04_alert_out` → 326; `q113_04_close_end` → 70; `q113_04_done_out` → 78; `q113_04_before_av_out` → 83; `q113_04_v_leaves_out` → 357; `q113_04_takemura_takedown_out` → 142; `q113_04_takemura_takedown_done_out` → 145; `q113_04_takemura_netrunner_out` → 152; `q113_04_mech_NEWNEW_out` → 690.

End nodes: 2: `<omitted>`; 45: `<omitted>`; 49: `<omitted>`; 70: `<omitted>`; 78: `<omitted>`; 83: `NonTerminating`; 142: `<omitted>`; 145: `<omitted>`; 152: `<omitted>`; 326: `<omitted>`; 357: `<omitted>`; 572: `NonTerminating`; 577: `<omitted>`; 690: `<omitted>`; 1291: `NonTerminating`; 1575: `NonTerminating`; 1592: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 100 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/7` |
| `scnChangeIdleAnimEvent` | 8 | 100 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/2` |
| `scnDialogLineEvent` | 87 | 68 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 100 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/20` |
| `scnIKEvent` | 8 | 100 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/10` |
| `scnLookAtEvent` | 32 | 100 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 1550 / 1101 | `/Data/RootChunk/sceneGraph/Data/graph/199/Data/events/6` |
| `scnPlaySkAnimEvent` | 30 | 75 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnPoseCorrectionEvent` | 1 | 661 / 523 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/8` |
| `scnUnmountEvent` | 4 | 100 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/19` |
| `scneventsAttachPropToPerformer` | 6 | 100 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 100 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/14` |
| `scneventsEquipItemToPerformer` | 1 | 624 / 507 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 9 | 100 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/16` |
| `scneventsSocket` | 29 | 100 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/13` |
| `scneventsVFXEvent` | 1 | 266 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 23
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, gaze: 3
- speech, skeletal_animation: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, vfx: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- gaze, props_equipment, socket_signal: 1
- gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `862a55f2e479133e1b2c730cc97074915d486d0964ec0adfd85ca6952ad62d43`. Binary SHA-256: `39c61b8b250b99f05c078bda6a1263b44fc7b861f626474ac3baa185199c3519`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q113\scenes\q113_04_hanako_estate.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_corpo_04_lizzies_club.scene`

577 graph nodes, 688 edges; 116 event-bearing sections, 1065 events; 213 screenplay lines, 41 screenplay options, 18 choice nodes.

Actors: Jackie (actor 0, spawnSet); corpo_friend (actor 1, community); arasaka_m_corporate (actor 2, community); arasaka_m_security_01 (actor 3, community); arasaka_m_security_02 (actor 4, community); arasaka_m_security_03 (actor 5, community); lizzies_bouncer (actor 6, community); johnny (actor 7, findInContext); barman (actor 8, spawnSet); basket_player_01 (actor 9, community); basket_player_02 (actor 10, community); basket_player_03 (actor 11, community); waitress (actor 12, community); client (actor 13, community); lizzies_guard (actor 14, community); test (actor 15, community); AI (actor 16, spawnDespawn); flight_bg_m_001 (actor 17, spawnDespawn); flight_bg_m_002 (actor 18, spawnDespawn); flight_bg_m_003 (actor 19, spawnDespawn); flight_bg_f_004 (actor 20, spawnDespawn); av (actor 21, spawner); Player (actor 22, findInContext).

Entries: `q000_corpo_04_lizzies_in` → 1; `Start 19` → 3814; `in_the_club` → 1156; `Start 4` → 1288; `ending` → 3505; `Start 10` → 2440; `q000_corpo_04_lizzies_av_landing_in` → 2443; `q000_corpo_04_q112_clone_in` → 2481; `Start 2` → 863; `q000_corpo_04_q112_clone_02_in` → 2492; `q000_lizzies_chicken_test` → 1962; `q000_corpo_lizzies_basket` → 2043; `FAKE INPUT FOR LOCO2` → 2676; `FAKE INPUT FOR LOCO` → 2701.

Exits: `q000_corpo_04_lizzies_out` → 2; `MontagePreloadOut` → 3800; `q000_corpo_04_lizzies_av_landing_out` → 2444; `q000_corpo_04_q112_clone_out` → 2483; `q000_corpo_04_q112_clone_02_out` → 2494.

End nodes: 2: `<omitted>`; 2444: `NonTerminating`; 2483: `<omitted>`; 2494: `<omitted>`; 3800: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 94 | 14 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/10` |
| `scnChangeIdleAnimEvent` | 46 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 145 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 19 | 60 / 600 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/49` |
| `scnIKEvent` | 38 | 60 / 534 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/3` |
| `scnLookAtEvent` | 161 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 220 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 10 | 14 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scnUnmountEvent` | 19 | 60 / 602 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/51` |
| `scneventsAttachPropToNode` | 3 | 14 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/17` |
| `scneventsAttachPropToPerformer` | 20 | 14 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scneventsAttachPropToWorld` | 11 | 14 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/32` |
| `scneventsCameraParamsEvent` | 10 | 67 / 639 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/5` |
| `scneventsEquipItemToPerformer` | 2 | 951 / 1748 | `/Data/RootChunk/sceneGraph/Data/graph/115/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 19 | 60 / 598 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/48` |
| `scneventsSocket` | 239 | 4 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsVFXDurationEvent` | 1 | 2073 / 3425 | `/Data/RootChunk/sceneGraph/Data/graph/348/Data/events/1` |
| `scneventsVFXEvent` | 8 | 22 / 233 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 14
- skeletal_animation, socket_signal: 12
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 7
- camera: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, socket_signal: 5
- socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze, socket_signal: 2
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio: 1
- speech, skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, audio, vfx: 1
- idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, vfx, socket_signal: 1
- skeletal_animation: 1
- speech, skeletal_animation: 1
- idle_animation: 1

Raw SHA-256: `10e70ec5c7c8da13b9c0b77003eb11519f172e3ee4a47326c4fa940e6af8c073`. Binary SHA-256: `a7b26ade6b37a4b65ec38dfda381aeacea257add915b1a83ec17ad026ec7610f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_corpo_04_lizzies_club.scene" --events
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

