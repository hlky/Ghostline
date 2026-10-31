# Lightning Breaks: scene presentation

Journal identity: `quests/main_quest/act_01/q104_01_sabotage`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q104_01_sabotage.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q103\scenes\q103_15_roadhouse_bar.scene`

360 graph nodes, 465 edges; 66 event-bearing sections, 877 events; 151 screenplay lines, 42 screenplay options, 28 choice nodes.

Actors: Panam (actor 0, spawnSet); bartender (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `Start 6` → 2354; `preview` → 1615; `Start 7` → 2912; `Start 4` → 1714; `chicken_bar` → 1235.

Exits: `roadhouse_slept` → 2; `roadhouse_left` → 849.

End nodes: 2: `<omitted>`; 849: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 56 | 14 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scnChangeIdleAnimEvent` | 86 | 12 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 130 | 12 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 13 | 14 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/23` |
| `scnIKEvent` | 26 | 14 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnLookAtEvent` | 128 | 14 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnPlaySkAnimEvent` | 159 | 12 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnUnmountEvent` | 13 | 14 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/22` |
| `scneventsAttachPropToNode` | 2 | 238 / 482 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/13` |
| `scneventsAttachPropToPerformer` | 41 | 14 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scneventsAttachPropToWorld` | 43 | 14 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scneventsCameraParamsEvent` | 3 | 1293 / 1604 | `/Data/RootChunk/sceneGraph/Data/graph/123/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 13 | 14 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/19` |
| `scneventsSocket` | 160 | 12 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsVFXEvent` | 4 | 1144 / 1528 | `/Data/RootChunk/sceneGraph/Data/graph/112/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, props_equipment, audio, socket_signal: 13
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 11
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- gaze: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `9fc30c02402c7924a3473a2c9c05e49c262c69e538e1c19b2213b6d04f9d3ea2`. Binary SHA-256: `a2e44f93910dc8ee83ebf635ae0bfa595b7e5a1d6f8fa96f75aac8fa1a96a75e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_15_roadhouse_bar.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_01a_roadhouse_meeting.scene`

157 graph nodes, 193 edges; 36 event-bearing sections, 294 events; 77 screenplay lines, 14 screenplay options, 7 choice nodes.

Actors: Panam (actor 0, spawnSet); Panam_vehicle (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `q104_mission_recap_in` → 1; `panam_to_motel` → 1686; `car_idle` → 1803; `wait_panam` → 1691; `wait_panam_again` → 2516.

Exits: `q104_mission_recap_out` → 1296; `car_idle_out` → 1802; `panam_to_motel_out` → 1687; `wait_panam_out` → 1692.

End nodes: 1296: `NonTerminating`; 1687: `<omitted>`; 1692: `NonTerminating`; 1802: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 1371 / 384 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/23` |
| `scnChangeIdleAnimEvent` | 52 | 461 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnDialogLineEvent` | 62 | 461 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 1333 / 245 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/9` |
| `scnIKEvent` | 6 | 1333 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scnLookAtEvent` | 20 | 461 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scnPlaySkAnimEvent` | 84 | 461 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnUnmountEvent` | 2 | 1333 / 250 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 4 | 1333 / 231 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/4` |
| `scneventsSocket` | 58 | 461 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsVFXEvent` | 2 | 1697 / 512 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- skeletal_animation, idle_animation: 4
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `39fe8b13572e9a45cafdf03073908d200f1f877d174fa0b2dc525de81ee1f0e8`. Binary SHA-256: `8caa565db267930bdbfc20c28c30d6663449d8021f271ebc8b8b341530ad8087`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_01a_roadhouse_meeting.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_01b_calibration.scene`

293 graph nodes, 373 edges; 67 event-bearing sections, 664 events; 183 screenplay lines, 30 screenplay options, 14 choice nodes.

Actors: Panam (actor 0, spawnSet); johnny (actor 1, spawnDespawn); panam_Car (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `Start 22` → 2255; `q104_calibration_test` → 1497; `Calacration3` → 2102; `Start 25` → 3779; `q104_01b_calibration_in` → 1293; `Start 23` → 2415; `Start 24` → 3056.

Exits: `pplant_plugin_out` → 2377.

End nodes: 2377: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 41 | 3835 / 2150 | `/Data/RootChunk/sceneGraph/Data/graph/271/Data/events/1` |
| `scnChangeIdleAnimEvent` | 76 | 51 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnDialogLineEvent` | 169 | 51 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnIKEvent` | 20 | 51 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/13` |
| `scnLookAtEvent` | 164 | 51 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 1374 / 386 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/0` |
| `scnPlaySkAnimEvent` | 110 | 51 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 57 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 21 | 51 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/15` |
| `scneventsSocket` | 51 | 51 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/8` |
| `scneventsVFXEvent` | 10 | 66 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech: 5
- speech, skeletal_animation, gaze: 5
- skeletal_animation, audio: 4
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, gaze: 2
- skeletal_animation, socket_signal, animation_state: 2
- gaze: 2
- speech, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, socket_signal, animation_state: 1
- speech, animation_state, mount_workspot: 1
- speech, vfx: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, vfx, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, ik, socket_signal, animation_state: 1
- vfx: 1

Raw SHA-256: `8703589f0e6b5ac928db9e606f1a1d70f6bfa9b1cb28d4ef0907c39e60d73b5c`. Binary SHA-256: `e856ac619e2fe345e5067e17f62cf23234abdd3b43caa05d6dd164c6dd629067`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_01b_calibration.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_02_av_shotdown.scene`

142 graph nodes, 147 edges; 28 event-bearing sections, 351 events; 79 screenplay lines, 6 screenplay options, 5 choice nodes.

Actors: Panam (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); panam_vehicle (actor 2, spawnSet); av (actor 3, community); V (actor 4, findInContext).

Entries: `q104_chase_starts` → 1384; `Start 8` → 1268; `Start1` → 2772; `q104_driving_hill_in` → 150; `fx_testing` → 2725; `Start 9` → 1617.

Exits: `av_chase_done` → 2765; `q104_driving_hill_out` → 16; `AV_end` → 2745.

End nodes: 16: `NonTerminating`; 2745: `NonTerminating`; 2765: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 17 | 724 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/16` |
| `scnChangeIdleAnimEvent` | 9 | 829 / 335 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/24` |
| `scnDialogLineEvent` | 64 | 623 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 963 / 444 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/27` |
| `scnIKEvent` | 28 | 668 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/7` |
| `scnLookAtEvent` | 24 | 623 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 6 | 963 / 428 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/12` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 1272 / 634 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/7` |
| `scnPlaySkAnimEvent` | 58 | 623 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/1` |
| `scnUnmountEvent` | 2 | 963 / 443 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/26` |
| `scneventsAttachPropToNode` | 4 | 668 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/10` |
| `scneventsAttachPropToPerformer` | 11 | 724 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 26 | 668 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/2` |
| `scneventsSocket` | 55 | 668 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/0` |
| `scneventsVFXDurationEvent` | 1 | 963 / 459 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/36` |
| `scneventsVFXEvent` | 43 | 724 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, audio, socket_signal, animation_state: 2
- skeletal_animation: 2
- speech, skeletal_animation, ik, props_equipment, socket_signal, animation_state: 1
- speech: 1
- speech, skeletal_animation, ik, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- skeletal_animation, ik, audio, socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, audio, vfx: 1
- props_equipment, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, ik, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, socket_signal: 1
- skeletal_animation, ik, socket_signal, animation_state: 1
- idle_animation: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `09303f3cbf062bf6cf79e857cbf0e00e24801cbb785ff110f798501fe9d28cbd`. Binary SHA-256: `5eaab853b6f097a11d0e28bc7d732595c77ac421334d8c544b8b00e155f24b07`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_02_av_shotdown.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_02a_breaking_antenna.scene`

130 graph nodes, 153 edges; 19 event-bearing sections, 212 events; 32 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: panam (actor 0, spawnSet); Johnny (actor 1, spawnSet); Panam_Veh (actor 2, spawnSet); drone_01 (actor 3, community); drone_02 (actor 4, community); drone_03 (actor 5, community); drone_04 (actor 6, community); v (actor 7, findInContext).

Entries: `Start 11` → 3849; `q104_security_done` → 783; `q104_plant_intro` → 921; `q104_pplant_shoot_security` → 65; `leave_plant` → 450; `q104_security_battlecry_01` → 198; `q104_security_battlecry_02` → 199; `Start 10` → 3690; `Start 7` → 877.

Exits: `q104_security_done_out` → 786; `q104_02a_plant_explosives_out` → 40; `leave_plant_out` → 449; `q104_pplant_shoot_security_out` → 66; `q104_security_battlecry_01_out` → 201; `q104_security_battlecry_02_out` → 202.

End nodes: 40: `NonTerminating`; 66: `<omitted>`; 201: `<omitted>`; 202: `<omitted>`; 449: `NonTerminating`; 786: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 19 | 70 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnChangeIdleAnimEvent` | 20 | 70 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 21 | 70 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/13` |
| `scnGameplayActionEvent` | 2 | 70 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/19` |
| `scnGameplayTransitionEvent` | 3 | 70 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/27` |
| `scnIKEvent` | 12 | 70 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnLookAtEvent` | 14 | 70 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnPlaySkAnimEvent` | 41 | 70 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 3 | 70 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/26` |
| `scneventsCameraParamsEvent` | 2 | 269 / 264 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 9 | 70 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scneventsSocket` | 30 | 70 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scneventsVFXEvent` | 36 | 70 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech: 3
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- speech, skeletal_animation, idle_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, audio, vfx, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, ik, audio, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, socket_signal, animation_state: 1
- audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, audio, socket_signal, animation_state: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `d2336fdd9933c235b24861db789c0b0562a0a027e3b21bad1f62964d33d72a1e`. Binary SHA-256: `95534c837e8acf24dbe32822914f7769dbe76748b7fff8eb7342aa0c15c1db4c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_02a_breaking_antenna.scene" --events
```

