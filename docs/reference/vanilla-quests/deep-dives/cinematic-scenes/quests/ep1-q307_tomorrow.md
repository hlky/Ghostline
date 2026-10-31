# Things Done Changed: scene presentation

Journal identity: `ep1/quests/main_quest/q307_tomorrow`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q307_tomorrow.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\holocalls\delamain\delamain_holocall.scene`

1203 graph nodes, 1327 edges; 26 event-bearing sections, 41 events; 40 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: delamain (actor 0, spawnSet); delamain_angry (actor 1, spawnSet); delamain_sad (actor 2, spawnSet); delamain_suicidal (actor 3, spawnSet); delamain_mean (actor 4, spawnSet); delamain_scared (actor 5, spawnSet); delamain_manic (actor 6, spawnSet); delamain_deep (actor 7, spawnSet); delamain_receptionist (actor 8, spawnSet).

Entries: `holo_delamain_calls_v_start` → 4; `holo_delamain_calls_v_end` → 6; `holo_v_calls_delamain_start` → 7; `holo_v_calls_delamain_end` → 8; `holo_delamain_deep_calls_v_start` → 1287; `holo_delamain_deep_calls_v_end` → 1288; `holo_v_calls_delamain_deep_start` → 1289; `holo_v_calls_delamain_deep_end` → 1290; `holo_delamain_screen_calls_v_start` → 1422; `holo_delamain_screen_calls_v_end` → 1423; `holo_v_calls_delamain_screen_start` → 1424; `holo_v_calls_delamain_screen_end` → 1425; `holo_delamain_receptionist_calls_v_start` → 1566; `holo_delamain_receptionist_calls_v_end` → 1567; `holo_v_calls_delamain_receptionist_start` → 1568; `holo_v_calls_delamain_receptionist_end` → 1569; `Start 1` → 1707; `holo_delamain_angry_calls_v_start` → 476; `holo_delamain_angry_calls_v_end` → 477; `holo_v_calls_delamain_angry_start` → 478; `holo_v_calls_delamain_angry_end` → 479; `holo_delamain_receptionist_screen` → 1729; `Start 3` → 1781; `holo_delamain_sad_calls_v_start` → 610; `holo_delamain_sad_calls_v_end` → 611; `Start 4` → 1856; `holo_v_calls_delamain_sad_start` → 612; `holo_v_calls_delamain_sad_end` → 613; `Start 5` → 1865; `Start1` → 1875; `Start2` → 1884; `Start3` → 1893; `Start4` → 1903; `Start5` → 1912; `Start 6` → 1978; `holo_delamain_main_screen` → 1988; `holo_delamain_suicidal_calls_v_start` → 744; `holo_delamain_suicidal_calls_v_end` → 745; `holo_v_calls_delamain_suicidal_start` → 746; `holo_v_calls_delamain_suicidal_end` → 747; `holo_delamain_mean_calls_v_start` → 878; `holo_delamain_mean_calls_v_end` → 879; `holo_v_calls_delamain_mean_start` → 880; `holo_v_calls_delamain_mean_end` → 881; `holo_delamain_deep_vehicle_talk` → 2204; `holo_delamain_scared_calls_v_start` → 1012; `holo_delamain_scared_calls_v_end` → 1013; `holo_v_calls_delamain_scared_start` → 1014; `holo_v_calls_delamain_scared_end` → 1015; `holo_delamain_manic_calls_v_start` → 1146; `holo_delamain_manic_calls_v_end` → 1147; `holo_v_calls_delamain_manic_start` → 1148; `holo_v_calls_delamain_manic_end` → 1149.

Exits: `holo_delamain_out` → 5; `holo_delamain_out_non` → 1800; `holo_delamain_deep_vehicle_talk_finish` → 2229.

End nodes: 5: `<omitted>`; 1800: `NonTerminating`; 2229: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 15 | 1858 / 3457 | `/Data/RootChunk/sceneGraph/Data/graph/626/Data/events/1` |
| `scnLookAtEvent` | 25 | 65 / 303 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 1789 / 3413 | `/Data/RootChunk/sceneGraph/Data/graph/609/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- idle_animation, gaze: 15
- gaze: 10
- camera: 1

Raw SHA-256: `458e99f7035d4c74b18f509546163fd50d89bf8d747de1baed1203125505a187`. Binary SHA-256: `617266251a387beea8711cae1dabac1cf07b40cb7716eea234a5cfd79419cddf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\holocalls\delamain\delamain_holocall.scene" --events
```

## `base\quest\holocalls\judy\judy_holocall.scene`

203 graph nodes, 230 edges; 2 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: judy (actor 0, spawnSet).

Entries: `holo_judy_calls_v_start` → 4; `holo_judy_calls_v_end` → 6; `holo_v_calls_judy_start` → 7; `holo_v_calls_judy_end` → 8; `audio_judy_calls_v_start` → 476; `audio_judy_calls_v_end` → 478; `audio_v_calls_judy_start` → 479; `audio_v_calls_judy_end` → 480.

Exits: `holo_judy_out` → 5; `audio_judy_out` → 477; `holo_judy_out_non` → 594.

End nodes: 5: `<omitted>`; 477: `<omitted>`; 594: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnLookAtEvent` | 2 | 65 / 303 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2

Raw SHA-256: `64ebc3e0ecb477b554a57fcdd003f671dc22ed11654b05a874a0bd1eeb3f5432`. Binary SHA-256: `53269b5e9eb17d056fee2730aad93cea84278e6e1caef145c76b16083ac01637`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\holocalls\judy\judy_holocall.scene" --events
```

## `base\quest\holocalls\kerry\kerry_holocall.scene`

127 graph nodes, 142 edges; 2 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: kerry (actor 0, spawnSet).

Entries: `holo_kerry_calls_v_start` → 4; `holo_kerry_calls_v_end` → 6; `holo_v_calls_kerry_start` → 7; `holo_v_calls_kerry_end` → 8.

Exits: `holo_kerry_out` → 5; `holo_kerry_out_non` → 476.

End nodes: 5: `<omitted>`; 476: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnLookAtEvent` | 2 | 65 / 303 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2

Raw SHA-256: `862b8ae0bc13d9876c631757cf9d224698d7cae9b98142eec4256a0c379a6d1d`. Binary SHA-256: `8c088b1af58d9a095aa378d9d995faa82c4ba1421f91359e7e665e8d6c0b1801`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\holocalls\kerry\kerry_holocall.scene" --events
```

## `base\quest\holocalls\panam\panam_holocall.scene`

193 graph nodes, 216 edges; 2 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: panam (actor 0, spawnSet).

Entries: `holo_panam_calls_v_start` → 4; `holo_panam_calls_v_end` → 6; `holo_v_calls_panam_start` → 7; `holo_v_calls_panam_end` → 8; `audio_panam_calls_v_start` → 710; `audio_panam_calls_v_end` → 714; `audio_v_calls_panam_start` → 716; `audio_v_calls_panam_end` → 718.

Exits: `holo_panam_out` → 5; `holo_panam_out_non` → 477; `audio_panam_out` → 712.

End nodes: 5: `<omitted>`; 477: `NonTerminating`; 712: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnLookAtEvent` | 2 | 65 / 303 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2

Raw SHA-256: `92d40e1ecaaca8e303a466050cf3029083eeee6f1683fd035f8bf31a60fa348d`. Binary SHA-256: `b803f59a9874d7f3b3ffaabe69df0d4675971ad3e2ff0e94845d65e06ea5cc6d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\holocalls\panam\panam_holocall.scene" --events
```

## `base\quest\holocalls\river\river_holocall.scene`

129 graph nodes, 145 edges; 2 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: river (actor 0, spawnSet).

Entries: `holo_river_calls_v_start` → 4; `holo_river_calls_v_end` → 6; `holo_v_calls_river_start` → 7; `holo_v_calls_river_end` → 8.

Exits: `holo_river_out` → 5; `holo_river_out_non` → 476.

End nodes: 5: `<omitted>`; 476: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnLookAtEvent` | 2 | 65 / 303 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2

Raw SHA-256: `a9b960d4d75af1b9523e94d82ce04feee0fc17da531d4c87e65874c41db3eac5`. Binary SHA-256: `05db92b63e9dd48cc0977200d4f4cfd9d8cfa23fd915d2c4a8174217f85261b6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\holocalls\river\river_holocall.scene" --events
```

## `base\quest\holocalls\victor\victor_holocall.scene`

125 graph nodes, 140 edges; 2 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: victor (actor 0, spawnSet).

Entries: `holo_victor_calls_v_start` → 4; `holo_victor_calls_v_end` → 6; `holo_v_calls_victor_start` → 7; `holo_v_calls_victor_end` → 8.

Exits: `holo_victor_out` → 5; `holo_victor_out_non` → 476.

End nodes: 5: `<omitted>`; 476: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnLookAtEvent` | 2 | 65 / 303 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2

Raw SHA-256: `152a507f947f86349337abfc206ff5e8e5fa98fee842c247d5bab0fcbfc27eb2`. Binary SHA-256: `12647ba8ffec4c6715d5db8a65c82b0c009c012471ae4ce7535f012c0342e3b6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\holocalls\victor\victor_holocall.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_01_pickup.scene`

528 graph nodes, 650 edges; 126 event-bearing sections, 976 events; 256 screenplay lines, 67 screenplay options, 27 choice nodes.

Actors: fia_agent (actor 0, spawnDespawn); fia_doctor (actor 1, spawnDespawn); johnny (actor 2, spawnDespawn); trauma_av (actor 3, spawner); trailer_av (actor 4, spawner); Player (actor 5, findInContext).

Entries: `Start 0` → 1; `Timing` → 2948; `Start 8` → 1542; `Start 18` → 3489; `Start 9` → 1561; `Start 10` → 1565; `CP77-62202_retrofix_in` → 3517; `return_in` → 1688; `Start 13` → 2258; `Start 17` → 3272.

Exits: `End 0` → 2; `abort_sitting_out` → 3420; `abort_out` → 1744.

End nodes: 2: `<omitted>`; 1744: `<omitted>`; 3420: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 22 | 38 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/7` |
| `scnChangeIdleAnimEvent` | 78 | 30 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 205 | 30 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnGameplayActionEvent` | 2 | 1097 / 1408 | `/Data/RootChunk/sceneGraph/Data/graph/152/Data/events/4` |
| `scnGameplayTransitionEvent` | 4 | 710 / 1064 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/4` |
| `scnIKEvent` | 9 | 710 / 1061 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/1` |
| `scnLookAtEvent` | 158 | 30 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 191 | 30 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnUnmountEvent` | 4 | 710 / 1069 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/8` |
| `scneventsAttachPropToPerformer` | 7 | 246 / 501 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/8` |
| `scneventsAttachPropToWorld` | 2 | 1276 / 1614 | `/Data/RootChunk/sceneGraph/Data/graph/181/Data/events/7` |
| `scneventsCameraParamsEvent` | 13 | 256 / 518 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/5` |
| `scneventsEquipItemToPerformer` | 20 | 789 / 1112 | `/Data/RootChunk/sceneGraph/Data/graph/126/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 38 | 38 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/16` |
| `scneventsSocket` | 197 | 30 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsSpawnEntityEvent` | 2 | 1276 / 1615 | `/Data/RootChunk/sceneGraph/Data/graph/181/Data/events/8` |
| `scneventsUnequipItemFromPerformer` | 10 | 193 / 389 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/5` |
| `scneventsVFXEvent` | 14 | 38 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 12
- speech, skeletal_animation, socket_signal: 8
- speech, skeletal_animation, idle_animation, socket_signal: 6
- speech, idle_animation, gaze, socket_signal: 6
- speech, idle_animation, gaze, audio, socket_signal: 5
- speech, skeletal_animation: 5
- speech, skeletal_animation, idle_animation, gaze: 5
- speech, idle_animation: 4
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 4
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 4
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- idle_animation: 3
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal, animation_state: 2
- speech, gaze, camera, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, props_equipment, vfx, socket_signal: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, audio: 1
- speech, idle_animation, audio: 1
- speech, skeletal_animation, audio: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- idle_animation, audio, vfx, socket_signal, gameplay_action: 1
- props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state, entity_lifecycle: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, audio: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, camera, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, props_equipment, vfx, socket_signal, animation_state, entity_lifecycle: 1
- skeletal_animation, idle_animation, ik, camera, vfx, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, camera, props_equipment, socket_signal, animation_state: 1
- camera, socket_signal, animation_state: 1
- skeletal_animation, camera, socket_signal: 1

Raw SHA-256: `c851cf7e61ca8570c3b41726019fa939f87b82493e8e5cd8dac3a35b28baa862`. Binary SHA-256: `2f63a1c376eaaa978fdda055e56166e7adf923026a9faba0f4db02273f39500d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_01_pickup.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_03_hospital.scene`

314 graph nodes, 388 edges; 76 event-bearing sections, 586 events; 162 screenplay lines, 46 screenplay options, 20 choice nodes.

Actors: Reed (actor 0, spawnSet); receptionist (actor 1, spawnDespawn); patient (actor 2, spawnDespawn); Player (actor 3, findInContext).

Entries: `Start 0` → 1; `Start 6` → 1496; `Start 3` → 1240; `Start 7` → 1536; `Start 8` → 1562; `skip_reed_in` → 1323; `Start 1` → 1088; `Start 5` → 1395; `Start 10` → 1985; `Start 9` → 1715; `Start 2` → 1136.

Exits: `End 0` → 2; `tpp_mirror_actor` → 1484.

End nodes: 2: `<omitted>`; 1484: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 58 | 10 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scnChangeIdleAnimEvent` | 36 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 121 | 10 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/22` |
| `scnGameplayTransitionEvent` | 6 | 807 / 955 | `/Data/RootChunk/sceneGraph/Data/graph/86/Data/events/6` |
| `scnIKEvent` | 12 | 807 / 950 | `/Data/RootChunk/sceneGraph/Data/graph/86/Data/events/1` |
| `scnLookAtAdvancedEvent` | 33 | 101 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/13` |
| `scnLookAtEvent` | 48 | 10 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scnPlaySkAnimEvent` | 127 | 10 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 6 | 807 / 959 | `/Data/RootChunk/sceneGraph/Data/graph/86/Data/events/9` |
| `scneventsCameraParamsEvent` | 15 | 10 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 6 | 807 / 957 | `/Data/RootChunk/sceneGraph/Data/graph/86/Data/events/8` |
| `scneventsSocket` | 112 | 10 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 6 | 10 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 11
- speech: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 6
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation: 3
- skeletal_animation, audio, socket_signal: 3
- skeletal_animation, camera, socket_signal: 3
- speech, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, camera, audio, socket_signal: 2
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, audio, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal: 1
- speech, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- skeletal_animation: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation: 1
- socket_signal: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `94320e3220718eeec3671f4473c2504c4e05a078d7da88b1d7fcc2e0bacd2421`. Binary SHA-256: `91e6d8baa10395d39343ee4df1ed389c2f4e2c365f3602b61cf4515333ce1229`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_03_hospital.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_03a_friends_holocall.scene`

215 graph nodes, 257 edges; 94 event-bearing sections, 581 events; 405 screenplay lines, 99 screenplay options, 23 choice nodes.

Actors: viktor (actor 0, spawnSet); river (actor 1, spawnSet); kerry (actor 2, spawnSet); judy (actor 3, spawnSet); receptionist (actor 4, spawnDespawn); operator (actor 5, findInContext); tpp_male_v (actor 6, spawnDespawn); tpp_female_v (actor 7, spawnDespawn); Player (actor 8, findInContext).

Entries: `river_in` → 1; `panam_in` → 6; `judy_in` → 8; `kerry_in` → 10; `viktor_in` → 12; `receptionist_in` → 14; `tpp_mirror_actor_in` → 973.

Exits: `call_out` → 2; `viktor_out` → 16; `receptionist_out` → 18.

End nodes: 2: `<omitted>`; 16: `<omitted>`; 18: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 894 / 1333 | `/Data/RootChunk/sceneGraph/Data/graph/152/Data/events/4` |
| `scnChangeIdleAnimEvent` | 74 | 51 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/8` |
| `scnDialogLineEvent` | 241 | 51 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/5` |
| `scnGameplayTransitionEvent` | 2 | 1028 / 1547 | `/Data/RootChunk/sceneGraph/Data/graph/191/Data/events/6` |
| `scnIKEvent` | 4 | 1028 / 1541 | `/Data/RootChunk/sceneGraph/Data/graph/191/Data/events/1` |
| `scnLookAtAdvancedEvent` | 13 | 570 / 514 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/4` |
| `scnLookAtEvent` | 11 | 51 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scnPlaySkAnimEvent` | 178 | 51 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/0` |
| `scnUnmountEvent` | 2 | 1028 / 1546 | `/Data/RootChunk/sceneGraph/Data/graph/191/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 2 | 1028 / 1544 | `/Data/RootChunk/sceneGraph/Data/graph/191/Data/events/4` |
| `scneventsSocket` | 41 | 51 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |
| `scneventsVFXEvent` | 10 | 51 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 19
- speech, skeletal_animation: 17
- speech, skeletal_animation, idle_animation, socket_signal: 13
- speech, skeletal_animation, socket_signal: 12
- speech, skeletal_animation, idle_animation: 9
- speech, skeletal_animation, idle_animation, gaze: 4
- speech, idle_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, idle_animation, gaze, vfx, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, audio, vfx: 1
- audio: 1
- idle_animation: 1

Raw SHA-256: `3fb1c37191fb546212206f6c72f720d3f03f48f9273d26d6a6af8efeb95e921a`. Binary SHA-256: `845a7dc45639667d26f2c7128603bdd80954e2392c23c2fe8fc5603a5ecfa739`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_03a_friends_holocall.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_04_cabride.scene`

273 graph nodes, 417 edges; 76 event-bearing sections, 290 events; 221 screenplay lines, 44 screenplay options, 18 choice nodes.

Actors: delamain (actor 0, spawnSet); radio_host1 (actor 1, findInContext); radio_host2 (actor 2, findInContext); junior_delamain (actor 3, findInContext); delamain_cab (actor 4, spawner); av1 (actor 5, spawner); av2 (actor 6, spawner); Player (actor 7, findInContext).

Entries: `Start 0` → 1; `av_landing_in` → 1799.

Exits: `End 0` → 2; `End1` → 1059.

End nodes: 2: `NonTerminating`; 1059: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1783 / 1177 | `/Data/RootChunk/sceneGraph/Data/graph/216/Data/events/1` |
| `scnChangeIdleAnimEvent` | 1 | 1783 / 1178 | `/Data/RootChunk/sceneGraph/Data/graph/216/Data/events/2` |
| `scnDialogLineEvent` | 203 | 22 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 1085 / 655 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/8` |
| `scnIKEvent` | 4 | 1085 / 646 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/1` |
| `scnPlaySkAnimEvent` | 16 | 210 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scnUnmountEvent` | 2 | 1085 / 659 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/11` |
| `scneventsAttachPropToPerformer` | 5 | 1085 / 649 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/4` |
| `scneventsAttachPropToWorld` | 2 | 1085 / 654 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/7` |
| `scneventsCameraParamsEvent` | 11 | 210 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 4 | 1085 / 657 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/10` |
| `scneventsSocket` | 37 | 210 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scneventsVFXEvent` | 2 | 1783 / 1179 | `/Data/RootChunk/sceneGraph/Data/graph/216/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 56
- speech, socket_signal: 7
- skeletal_animation, camera, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, camera, props_equipment, socket_signal: 2
- speech, skeletal_animation, camera, socket_signal: 1
- skeletal_animation, camera, props_equipment, socket_signal, animation_state: 1
- skeletal_animation: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1

Raw SHA-256: `ae5ecffe9e87b13df061de1b891e2b24a280ec411ca8198e8a9638ab4d262ae6`. Binary SHA-256: `a8a0e38d8ba90b4f35bfb879dafdaee51dbd6598194e4e561ed80004a9e98b37`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_04_cabride.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_05_alley.scene`

39 graph nodes, 52 edges; 11 event-bearing sections, 117 events; 27 screenplay lines, 5 screenplay options, 1 choice nodes.

Actors: thug_01 (actor 0, community); thug_02 (actor 1, community); Player (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 9 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 22 | 9 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnLookAtEvent` | 39 | 9 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnPlaySkAnimEvent` | 21 | 9 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsEquipItemToPerformer` | 1 | 61 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/5` |
| `scneventsSocket` | 26 | 9 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 199 / 223 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- gaze: 2
- gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `6ef8c758c1a5b0924d5b37cc6930f53ae52226a51b67f7497a2fa4197d360131`. Binary SHA-256: `d468e9472060bbd6b6fdb3af07d9bd231a71f94d07b7b3905d0b7bd282666a83`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_05_alley.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_06_viktor.scene`

319 graph nodes, 432 edges; 94 event-bearing sections, 911 events; 227 screenplay lines, 50 screenplay options, 16 choice nodes.

Actors: zetatech_clerk (actor 0, community); viktor (actor 1, spawnSet); new_merc (actor 2, community); drone (actor 3, community); Player (actor 4, findInContext).

Entries: `Start 0` → 1; `Start1` → 1498; `Start 1` → 1237; `Start 3` → 1995; `Start 4` → 2370.

Exits: `End 0` → 2; `End 1` → 1210.

End nodes: 2: `<omitted>`; 1210: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 101 | 73 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/8` |
| `scnChangeIdleAnimEvent` | 74 | 12 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnDialogLineEvent` | 194 | 12 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnGameplayTransitionEvent` | 1 | 78 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/12` |
| `scnIKEvent` | 5 | 78 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scnLookAtEvent` | 186 | 12 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnPlaySkAnimEvent` | 180 | 12 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnUnmountEvent` | 1 | 78 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/17` |
| `scneventsAttachPropToPerformer` | 2 | 1402 / 1477 | `/Data/RootChunk/sceneGraph/Data/graph/109/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 517 / 383 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/9` |
| `scneventsCameraParamsEvent` | 7 | 78 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/8` |
| `scneventsEquipItemToPerformer` | 3 | 12 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 78 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/13` |
| `scneventsSocket` | 143 | 12 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsVFXEvent` | 11 | 46 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 14
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 12
- gaze: 9
- speech: 8
- speech, gaze: 6
- speech, skeletal_animation, gaze: 6
- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation, gaze, vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 3
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, gaze, vfx: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, idle_animation, gaze, audio: 1
- speech, skeletal_animation, gaze, audio: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, camera, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1

Raw SHA-256: `b1b2f3bb779667778572308a280fbda2e16dd67c10d6b6a3eea331247ead2a98`. Binary SHA-256: `5beba3a839fc6d5db20d7ef70e925bb5cee1860daf0a0985602c164b20c940a0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_06_viktor.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_07_thugs.scene`

77 graph nodes, 102 edges; 24 event-bearing sections, 191 events; 49 screenplay lines, 10 screenplay options, 2 choice nodes.

Actors: thug_01 (actor 0, community); thug_02 (actor 1, community); Player (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 324 / 394 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/13` |
| `scnChangeIdleAnimEvent` | 13 | 10 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 37 | 10 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnLookAtEvent` | 26 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 44 | 10 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsCameraParamsEvent` | 1 | 10 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsEquipItemToPerformer` | 3 | 283 / 245 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/2` |
| `scneventsSocket` | 46 | 10 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsVFXEvent` | 20 | 283 / 262 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech: 2
- skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `775f2227e4284857afd27dd31600f0e63ac53d374181ff760b10e6b06b217882`. Binary SHA-256: `110cf3fb23c1839c2985eba57579abbf6102644af03dfb5ba94ec682cfdbef63`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_07_thugs.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_08_misty.scene`

144 graph nodes, 201 edges; 62 event-bearing sections, 574 events; 129 screenplay lines, 39 screenplay options, 10 choice nodes.

Actors: misty (actor 0, community); PASSERBY_1 (actor 1, spawnDespawn); PASSERBY_2 (actor 2, spawnDespawn); PASSERBY_3 (actor 3, spawnDespawn); PASSERBY_4 (actor 4, spawnDespawn); PASSERBY_animset_02 (actor 5, spawnDespawn); PASSERBY_animset_03 (actor 6, spawnDespawn); PASSERBY_animset_04 (actor 7, spawnDespawn); Player (actor 8, findInContext).

Entries: `Start 0` → 1; `Start 5` → 911.

Exits: `End 0` → 2; `PRELOAD` → 740.

End nodes: 2: `<omitted>`; 740: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 33 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnChangeIdleAnimEvent` | 48 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 112 | 6 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnLookAtAdvancedEvent` | 51 | 153 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scnLookAtEvent` | 110 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 128 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 229 / 273 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/20` |
| `scneventsCameraParamsEvent` | 2 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsEquipItemToPerformer` | 4 | 520 / 802 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/8` |
| `scneventsSocket` | 64 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 1 | 557 / 902 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/12` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 818 / 1181 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/10` |
| `scneventsVFXEvent` | 18 | 6 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 16
- gaze: 7
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze: 4
- speech, skeletal_animation, gaze, audio, socket_signal: 3
- speech: 3
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 2
- skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- vfx, socket_signal: 1
- skeletal_animation, props_equipment: 1

Raw SHA-256: `b9afc6abac5314438d02a5c83bc7ce580587f0e8ef1fd7bfcb97cd0cd31a21c7`. Binary SHA-256: `c4444c28d2abe45214f81fa3600a21dc93068591238e5ed1a6af67087c2606c9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_08_misty.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_09_cutscene.scene`

703 graph nodes, 801 edges; 16 event-bearing sections, 259 events; 32 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: MISTY (actor 0, community); TPP_V_fem (actor 1, spawnDespawn); TPP_V_mal (actor 2, spawnDespawn); passerby_npc_cutscene (actor 3, spawnDespawn); NPC1 (actor 4, spawnDespawn); NPC2 (actor 5, spawnDespawn); NPC3 (actor 6, spawnDespawn); NPC4 (actor 7, spawnDespawn); NPC5 (actor 8, spawnDespawn); NPC6 (actor 9, spawnDespawn); NPC7 (actor 10, spawnDespawn); NPC8 (actor 11, spawnDespawn); NPC9 (actor 12, spawnDespawn); NPC10 (actor 13, spawnDespawn); NPC11 (actor 14, spawnDespawn); NPC12 (actor 15, spawnDespawn); NC13 (actor 16, spawnDespawn); NPC14 (actor 17, spawnDespawn); NPC15 (actor 18, spawnDespawn); NPC16 (actor 19, spawnDespawn); NPC17 (actor 20, spawnDespawn); NPC18 (actor 21, spawnDespawn); NPC19 (actor 22, spawnDespawn); NPC20 (actor 23, spawnDespawn); NPC21 (actor 24, spawnDespawn); NPC22 (actor 25, spawnDespawn); NPC23 (actor 26, spawnDespawn); NPC24 (actor 27, spawnDespawn); NPC25 (actor 28, spawnDespawn); NPC26 (actor 29, spawnDespawn); NPC27 (actor 30, spawnDespawn); NPC28 (actor 31, spawnDespawn); NPC29 (actor 32, spawnDespawn); NPC30 (actor 33, spawnDespawn); NPC31 (actor 34, spawnDespawn); NPC32 (actor 35, spawnDespawn); NPC33 (actor 36, spawnDespawn); NPC34 (actor 37, spawnDespawn); NPC35 (actor 38, spawnDespawn); NPC36 (actor 39, spawnDespawn); NPC37 (actor 40, spawnDespawn); NPC38 (actor 41, spawnDespawn); NPC39 (actor 42, spawnDespawn); NPC40 (actor 43, spawnDespawn); NPC41 (actor 44, spawnDespawn); NPC42 (actor 45, spawnDespawn); NPC43 (actor 46, spawnDespawn); NPC44 (actor 47, spawnDespawn); NPC45 (actor 48, spawnDespawn); NPC46 (actor 49, spawnDespawn); NPC47 (actor 50, spawnDespawn); NPC48 (actor 51, spawnDespawn); NPC49 (actor 52, spawnDespawn); NPC50 (actor 53, spawnDespawn); NPC51 (actor 54, spawnDespawn); NPC52 (actor 55, spawnDespawn); NPC53 (actor 56, spawnDespawn); NPC54 (actor 57, spawnDespawn); NPC55 (actor 58, spawnDespawn); NPC56 (actor 59, spawnDespawn); NPC57 (actor 60, spawnDespawn); NPC58 (actor 61, spawnDespawn); NPC59 (actor 62, spawnDespawn); NPC60 (actor 63, spawnDespawn); NPC61_female_average (actor 64, spawnDespawn); NPC62_female_average (actor 65, spawnDespawn); NPC63_female_average (actor 66, spawnDespawn); NPC64_female_average_old (actor 67, spawnDespawn); NPC65_male_average (actor 68, spawnDespawn); NPC66_male_average (actor 69, spawnDespawn); NPC67_male_average (actor 70, spawnDespawn); NPC68_male_average (actor 71, spawnDespawn); NPC69_child (actor 72, spawnDespawn); NPC70_fat (actor 73, spawnDespawn); taxi (actor 74, spawner); car1 (actor 75, spawner); background_vehicle1 (actor 76, spawner); background_vehicle2 (actor 77, spawner); background_vehicle3 (actor 78, spawner); background_vehicle4 (actor 79, spawner); background_vehicle5 (actor 80, spawner); background_vehicle6 (actor 81, spawner); background_vehicle7 (actor 82, spawner); background_vehicle8 (actor 83, spawner); background_vehicle9 (actor 84, spawner); Player (actor 85, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 6 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/24` |
| `scnDialogLineEvent` | 6 | 6 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/38` |
| `scnLookAtEvent` | 20 | 1497 / 512 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/0` |
| `scnPlayRidAnimEvent` | 52 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 68 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsAttachPropToPerformer` | 15 | 7772 / 4636 | `/Data/RootChunk/sceneGraph/Data/graph/565/Data/events/0` |
| `scneventsEquipItemToPerformer` | 1 | 8689 / 5491 | `/Data/RootChunk/sceneGraph/Data/graph/690/Data/events/0` |
| `scneventsPlayRidCameraAnimEvent` | 14 | 6 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsSocket` | 56 | 6 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scneventsVFXEvent` | 22 | 6 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- socket_signal: 4
- props_equipment: 3
- skeletal_animation, gaze, rid_actor, camera, rid_camera, socket_signal: 2
- gaze, socket_signal: 2
- skeletal_animation: 2
- speech, skeletal_animation, rid_actor, camera, rid_camera, audio, vfx, socket_signal: 1
- speech: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `4422782cb086ec89f16bf0c26afae4ae56d88547d41cb2a4887f1538ade7e52a`. Binary SHA-256: `473d7e7769628110044b178efc816eee16ca8d4a4195d6628f754976bb33085c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_09_cutscene.scene" --events
```

