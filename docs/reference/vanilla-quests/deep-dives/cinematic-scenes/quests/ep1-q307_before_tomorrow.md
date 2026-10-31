# Who Wants to Live Forever: scene presentation

Journal identity: `ep1/quests/main_quest/q307_before_tomorrow`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q307_before_tomorrow.md) · [All cinematic studies](../README.md)

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

## `base\quest\main_quests\part1\q115\scenes\q115_02b_ripperdoc_roof.scene`

853 graph nodes, 1025 edges; 157 event-bearing sections, 1165 events; 401 screenplay lines, 58 screenplay options, 22 choice nodes.

Actors: misty (actor 0, spawnSet); victor (actor 1, spawnSet); sobchak (actor 2, spawnSet); panam (actor 3, spawnSet); judy (actor 4, spawnSet); kerry (actor 5, spawnSet); hanako (actor 6, findInContext); rogue (actor 7, findInContext); johnny (actor 8, spawnDespawn); V_male (actor 9, spawner); V_female (actor 10, spawner); Player (actor 11, findInContext); V_POSESSED (actor 12, findInContext).

Entries: `sq024_02b_in` → 4; `Start 39` → 4150; `Start 15` → 1678; `roof_in` → 52; `misty_urge` → 1736; `Start 17` → 1745; `Start 18` → 1747; `Start 19` → 1748; `panam` → 1749; `Start 22` → 1762; `kerry` → 1770; `record_start` → 3436; `river` → 1778; `Start 25` → 1786; `Start 26` → 1870; `Start 0` → 2722; `Start 34` → 3578; `Start 27` → 1939; `describing_options` → 1950; `Start1` → 2834; `Start 35` → 3675; `Start 36` → 3677; `Start 4` → 1190; `Start 37` → 3679; `hanako` → 1201; `Start 6` → 1203; `Start 7` → 1216; `solo_in` → 1232; `Start2` → 2914; `Start 40` → 4613; `Start 38` → 3852; `Start 29` → 2237; `Start 9` → 1421; `Start 30` → 2255; `Start 10` → 1434; `Start 11` → 1436; `Start 31` → 3123; `Start 12` → 1472; `Start 32` → 3169; `Start 14` → 1553; `Start 33` → 3231; `Start 2` → 784; `Start 3` → 787.

Exits: `End3` → 3438; `out_afterlife` → 226; `out_nomads` → 277; `out_hanako` → 280; `terminado` → 2056; `out_dead` → 403; `solo_out` → 1246; `End 4` → 1303; `ai_out` → 1364.

End nodes: 226: `NonTerminating`; 277: `NonTerminating`; 280: `NonTerminating`; 403: `<omitted>`; 1246: `<omitted>`; 1303: `<omitted>`; 1364: `NonTerminating`; 2056: `<omitted>`; 3438: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 16 | 344 / 624 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/1` |
| `scnChangeIdleAnimEvent` | 49 | 19 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scnDialogLineEvent` | 331 | 14 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 17 / 142 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |
| `scnIKEvent` | 6 | 17 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnLookAtAdvancedEvent` | 13 | 4043 / 5220 | `/Data/RootChunk/sceneGraph/Data/graph/715/Data/events/1` |
| `scnLookAtEvent` | 117 | 15 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnPlayRidAnimEvent` | 65 | 2233 / 3019 | `/Data/RootChunk/sceneGraph/Data/graph/410/Data/events/4` |
| `scnPlaySkAnimEvent` | 316 | 14 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnPlayVideoEvent` | 1 | 2233 / 3554 | `/Data/RootChunk/sceneGraph/Data/graph/410/Data/events/200` |
| `scnUnmountEvent` | 3 | 17 / 141 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |
| `scneventsAttachPropToNode` | 1 | 1214 / 1839 | `/Data/RootChunk/sceneGraph/Data/graph/214/Data/events/7` |
| `scneventsAttachPropToPerformer` | 6 | 525 / 921 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/1` |
| `scneventsAttachPropToWorld` | 7 | 525 / 927 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/7` |
| `scneventsCameraParamsEvent` | 5 | 525 / 922 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/2` |
| `scneventsEquipItemToPerformer` | 6 | 4681 / 5957 | `/Data/RootChunk/sceneGraph/Data/graph/816/Data/events/0` |
| `scneventsPlayRidCameraAnimEvent` | 31 | 2233 / 3043 | `/Data/RootChunk/sceneGraph/Data/graph/410/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 3 | 17 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |
| `scneventsSocket` | 172 | 15 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scneventsVFXEvent` | 14 | 237 / 576 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 24
- skeletal_animation: 19
- speech, skeletal_animation, gaze, socket_signal: 18
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 18
- speech, socket_signal: 7
- gaze: 7
- speech, skeletal_animation, socket_signal: 5
- socket_signal: 5
- speech, idle_animation, gaze, socket_signal: 4
- gaze, camera, socket_signal: 4
- camera, rid_camera: 4
- speech, gaze: 3
- skeletal_animation, audio, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation: 2
- speech, idle_animation: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, audio, vfx, socket_signal: 2
- speech, gaze, socket_signal: 2
- props_equipment: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1
- speech, audio: 1
- gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- gaze, socket_signal: 1
- props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, rid_actor, camera, rid_camera, props_equipment, audio, socket_signal, video: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1

Raw SHA-256: `3ff92369e9b58796f825c82ec7059b50aa2b54257c88c9ee2e46d8601ec0bfc4`. Binary SHA-256: `0506831be23656c51947cf3bf920a95700235d4cc52065dc18e91a09c337dd83`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_02b_ripperdoc_roof.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_00_pickup_holocall.scene`

69 graph nodes, 81 edges; 16 event-bearing sections, 42 events; 37 screenplay lines, 6 screenplay options, 1 choice nodes.

Actors: Reed (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `v_calls_reed_back` → 278; `confirm_rooftop_in` → 144; `reed_calls_v_in` → 6; `v_calls_reed_rooftop_first` → 303.

Exits: `End1` → 20; `confirm_rooftop_out` → 171.

End nodes: 20: `<omitted>`; 171: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 3. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 128 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/2` |
| `scnDialogLineEvent` | 35 | 35 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnLookAtEvent` | 3 | 35 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 43 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scneventsSocket` | 1 | 128 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, gaze: 2
- speech, skeletal_animation: 2
- speech, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `224eda1eceba4fa47977d501489bcb70e185e26a2211728514a9e2b44376f862`. Binary SHA-256: `14c312d404691f53cbdd1725079088350dfb46ac2df7ee7094a4e87aa7957255`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_00_pickup_holocall.scene" --events
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

