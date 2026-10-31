# Life During Wartime: scene presentation

Journal identity: `quests/main_quest/act_01/q104_02_av_chase`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q104_02_av_chase.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

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

## `base\quest\main_quests\part1\q104\scenes\q104_03_av_chasing.scene`

60 graph nodes, 55 edges; 11 event-bearing sections, 111 events; 28 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Panam (actor 0, spawnSet); Mitch (actor 1, spawnDespawn); Scorpion (actor 2, spawnDespawn); Panam_Veh (actor 3, spawnSet); Crashed_AV (actor 4, community); V (actor 5, findInContext).

Entries: `q104_chasing_av_in` → 12; `drones_repair` → 77; `drones_radar` → 194; `Start 22` → 534; `sq027_turret_jam_clone_in` → 590; `drones_defeated` → 161.

Exits: `turretout` → 541; `drones_defeated_done` → 167; `sq027_turret_jam_clone_out` → 600; `q104_chasing_av_out` → 13; `drones_radar_done` → 195; `turret_fixed` → 95; `drones_repair_done` → 99.

End nodes: 13: `<omitted>`; 95: `NonTerminating`; 99: `<omitted>`; 167: `NonTerminating`; 195: `<omitted>`; 541: `NonTerminating`; 600: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 28 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/25` |
| `scnChangeIdleAnimEvent` | 8 | 28 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnDialogLineEvent` | 23 | 28 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnIKEvent` | 6 | 163 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnLookAtEvent` | 22 | 28 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 193 / 146 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/15` |
| `scnPlaySkAnimEvent` | 19 | 28 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 8 | 94 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsSocket` | 16 | 28 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsVFXEvent` | 6 | 98 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- ik, socket_signal, animation_state: 1
- speech: 1
- vfx: 1

Raw SHA-256: `482881a25fc166b7873a3dcc0e865ce2028ead5031e2967a092a666cb481508d`. Binary SHA-256: `72d49667d9b3d1596bcb1a5e143f6528a40f34a2630540e35eb181c4801b3d4a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_03_av_chasing.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_04_nomad_hurt.scene`

112 graph nodes, 121 edges; 18 event-bearing sections, 101 events; 40 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: Panam (actor 0, spawnSet); mitch_radio (actor 1, findInContext); pilot (actor 2, community); mitch (actor 3, spawnSet); Panam_Veh (actor 4, spawnSet); V (actor 5, findInContext).

Entries: `q104_panam_got_hit_in` → 1; `q104_scanned_turret` → 127; `q104_scanned_zetatech` → 128; `q104_scanned_bodies` → 129; `q104_scanned_mitch` → 130; `q104_panam_driving_in` → 151; `Start 6` → 576; `q104_scanned_drones_in` → 164; `q104_drone_ending` → 185; `Medpack_Debug` → 402.

Exits: `q104_drone_recon_killing` → 747; `q104_drone_recon_end` → 124; `q104_scanned_turret_done` → 139; `q104_scanned_zetatech_done` → 140; `q104_scanned_bodies_done` → 141; `q104_scanned_mitch_done` → 142; `q104_panam_driving_out` → 152; `q104_scanned_drones_out` → 166; `q104_drone_ending_out` → 186.

End nodes: 124: `NonTerminating`; 139: `NonTerminating`; 140: `NonTerminating`; 141: `NonTerminating`; 142: `NonTerminating`; 152: `<omitted>`; 166: `NonTerminating`; 186: `NonTerminating`; 747: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 119 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnChangeIdleAnimEvent` | 4 | 211 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/3` |
| `scnDialogLineEvent` | 30 | 119 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnIKEvent` | 8 | 211 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/12` |
| `scnLookAtEvent` | 12 | 119 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 18 | 119 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsAttachPropToPerformer` | 1 | 214 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/1` |
| `scneventsAttachPropToWorld` | 1 | 214 / 150 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 6 | 211 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/0` |
| `scneventsSocket` | 17 | 134 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scneventsVFXEvent` | 3 | 211 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- skeletal_animation: 4
- speech, socket_signal: 2
- speech, skeletal_animation, gaze, audio: 1
- speech, skeletal_animation: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1
- vfx: 1
- ik, socket_signal, animation_state: 1

Raw SHA-256: `29d1dc64ed69cfe7a96e7654674268e76f0d82a2b5051f90233862a674e334b8`. Binary SHA-256: `c91c6a25492ffb543e5163e8619b2a9b5330f158e22fa22adf5442cef833361c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_04_nomad_hurt.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_05_av_debris.scene`

336 graph nodes, 399 edges; 76 event-bearing sections, 822 events; 219 screenplay lines, 29 screenplay options, 15 choice nodes.

Actors: Panam (actor 0, spawnSet); AV_pilot (actor 1, community); Mitch (actor 2, spawnSet); Johnny (actor 3, spawnSet); panam_vehicle (actor 4, spawnSet); kang_tao_av (actor 5, community); V (actor 6, findInContext).

Entries: `Start 26` → 4509; `q104_canyon_starts_in` → 277; `Start 34` → 5861; `q104_enter_car_turret_in` → 301; `q104_repair_bike_in` → 2964; `Start 36` → 5897; `Start 27` → 4603; `q104_05_disabling_turret` → 5409; `q104_av_door_idle` → 5945; `DebugCineStart` → 4113; `q104_05_panam_combat_arrival_in` → 2549; `q104_05_turret_disabled_in` → 2554; `Start 32` → 5736; `q104_05_enemies_killed_in` → 2566; `q104_hostage_mitch_in` → 528.

Exits: `q104_04_av_debris_TerminatingOutput` → 5566; `q104_canyon_starts_out` → 278; `q104_enter_car_turret_out` → 302; `q104_start_tracking_out` → 3522; `q104_05_disabling_turret_out` → 5410; `q104_av_door_idle_out` → 5950; `q104_05_panam_combat_arrival_out` → 2551; `q104_05_turret_disabled_out` → 2556; `q104_05_enemies_killed_out` → 2568.

End nodes: 278: `<omitted>`; 302: `<omitted>`; 2551: `<omitted>`; 2556: `<omitted>`; 2568: `<omitted>`; 3522: `NonTerminating`; 5410: `<omitted>`; 5566: `<omitted>`; 5950: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 28 | 546 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnChangeIdleAnimEvent` | 58 | 546 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnDialogLineEvent` | 194 | 303 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 1511 / 264 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/3` |
| `scnGameplayTransitionEvent` | 7 | 1511 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/24` |
| `scnIKEvent` | 16 | 1346 / 192 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/0` |
| `scnLookAtEvent` | 142 | 830 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/6` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 4114 / 1622 | `/Data/RootChunk/sceneGraph/Data/graph/136/Data/events/0` |
| `scnPlaySkAnimEvent` | 178 | 546 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnUnmountEvent` | 6 | 3025 / 880 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/16` |
| `scneventsEquipItemToPerformer` | 1 | 5891 / 2718 | `/Data/RootChunk/sceneGraph/Data/graph/311/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 11 | 1346 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/2` |
| `scneventsSocket` | 176 | 546 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |
| `scneventsVFXEvent` | 2 | 1346 / 206 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 14
- speech: 8
- speech, skeletal_animation, gaze, socket_signal: 7
- speech, idle_animation, audio, socket_signal: 4
- speech, socket_signal: 4
- skeletal_animation, socket_signal: 4
- speech, idle_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, gaze: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, audio, socket_signal: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze: 1
- speech, audio: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- idle_animation, gameplay_action: 1

Raw SHA-256: `1bf234dc1f30ffd18ce781ef29247c42246fd1c963dd81d596fe07eeca386f7b`. Binary SHA-256: `f9ea06f4c8c400bd465fca186fd85ba56f561043eeb9708553493e6e6f5ba264`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_05_av_debris.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_06_following_tracks.scene`

93 graph nodes, 80 edges; 16 event-bearing sections, 65 events; 65 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnSet); Panam (actor 1, spawnSet); Mitch (actor 2, community); V (actor 3, findInContext).

Entries: `q104_to_gas_station_in` → 97; `q104_to_airstrip_chat` → 286; `airstrip_combat_chats` → 291; `q104_vehicle_spotted_in` → 197; `q104_06_tracks_continued_in` → 203; `q104_lost_tracks_airfield_in` → 27; `q104_see_broken_gate_in` → 32; `airstrip_combat_chats_02` → 323; `airstrip_combat_chats_03'` → 324; `q104_06_crash_to_gas_straight_in` → 333; `q104_06_hangar_checked_in` → 242; `q104_broken_car_oil_in` → 62; `q104_gas_no_crash_site` → 346; `q104_crash_track_comment` → 547; `q104_gas_station_in` → 266; `q104_06_haru_not_here_in` → 281.

Exits: `q104_gas_station_out` → 98; `q104_to_airstrip_chat_out` → 287; `airstrip_combat_chats_out` → 292; `q104_vehicle_spotted_out` → 198; `q104_06_tracks_continued_out` → 205; `q104_lost_tracks_airfield_out` → 28; `q104_see_broken_gate_out` → 33; `airstrip_combat_chats_02_out` → 328; `airstrip_combat_chats_03_out` → 329; `q104_06_crash_to_gas_straight_out` → 334; `q104_06_hangar_checked_out` → 243; `q104_gas_no_crash_site_out` → 345; `q104_broken_car_oil_out` → 63; `q104_to_gas_station_out` → 264; `q104_crash_track_comment_out` → 548; `q104_06_haru_not_here_out` → 179.

End nodes: 28: `<omitted>`; 33: `<omitted>`; 63: `<omitted>`; 98: `<omitted>`; 179: `<omitted>`; 198: `<omitted>`; 205: `<omitted>`; 243: `<omitted>`; 264: `<omitted>`; 287: `<omitted>`; 292: `<omitted>`; 328: `<omitted>`; 329: `<omitted>`; 334: `<omitted>`; 345: `<omitted>`; 548: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 65 | 29 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16

Raw SHA-256: `4314ba27c5b20a17965204960e4223cd7470fb7eb6b04ae407bdd95011202ff7`. Binary SHA-256: `ddbcf84c0a2aa2169440fd25ff326f5835e16d340f5f7c815c964bbe7d261d77`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_06_following_tracks.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_07_gas_station_chats.scene`

39 graph nodes, 41 edges; 8 event-bearing sections, 110 events; 42 screenplay lines, 4 screenplay options, 1 choice nodes.

Actors: KangTao_Gas12 (actor 0, community); KangTao_Gas1 (actor 1, community); KangTao_Gas13_Sniper (actor 2, community); KangTao_Gas8_Sniper (actor 3, community); Owner (actor 4, spawnSet); Player (actor 5, findInContext).

Entries: `gas_owner_chat` → 26; `q104_07_sniper_comms_in` → 12; `q104_07_about_haru_in` → 15.

Exits: `gas_owner_chat_out` → 27; `q104_07_sniper_comms_out` → 14; `q104_07_about_haru_out` → 17; `owner_chat_done` → 187.

End nodes: 14: `<omitted>`; 17: `<omitted>`; 27: `<omitted>`; 187: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 14 | 28 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |
| `scnDialogLineEvent` | 42 | 13 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 8 | 28 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/3` |
| `scnPlaySkAnimEvent` | 24 | 28 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scneventsSocket` | 22 | 28 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech: 2

Raw SHA-256: `51f2b2fba04c823865d1b81405ff78485841da9af514ea13e0e9aadf8f0b0904`. Binary SHA-256: `f9f19b739f08eb6585b748ab5790dcb1e6bc44a11e0e2ba714c7312145feb2f2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_07_gas_station_chats.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_07a_gas_station_infiltration.scene`

18 graph nodes, 12 edges; 6 event-bearing sections, 10 events; 10 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Panam (actor 0, spawnSet); Johnny (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `q104_07a_nomad_vehicles_in` → 1; `q104_07a_combat_comment` → 44; `q104_07a_scouting_prompt_in` → 12; `q104_07a_haru_located` → 49; `q104_07a_snipers_in` → 32; `q104_07a_main_building_in` → 17.

Exits: `q104_07a_main_building_out` → 18; `q104_07a_nomad_vehicles_out` → 2; `q104_07a_combat_comment_out` → 45; `q104_07a_scouting_prompt_out` → 13; `q104_07a_haru_located_out` → 50; `q104_07a_snipers_out` → 33.

End nodes: 2: `<omitted>`; 13: `<omitted>`; 18: `<omitted>`; 33: `<omitted>`; 45: `<omitted>`; 50: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 10 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6

Raw SHA-256: `4d834b98941b2e73183f69da84c2f035258285b5cc145a8a5467fbd39c8cc0c8`. Binary SHA-256: `57348b56a602a636bdc13f8b9eb5d57dffefb022ce719f74304a24e1963429ab`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_07a_gas_station_infiltration.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_07b_haru_found.scene`

121 graph nodes, 136 edges; 23 event-bearing sections, 142 events; 40 screenplay lines, 3 screenplay options, 3 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Panam (actor 1, spawnSet); Haru (actor 2, spawnSet); Takamura (actor 3, spawnSet); Paramedic (actor 4, community); V (actor 5, findInContext).

Entries: `haru_idles` → 533; `Start 13` → 2112; `Start 9` → 1712; `anders_full_scene` → 1736; `placeholder input` → 1742; `q104_07b_carrying_comment_in` → 809.

Exits: `haru_idles_end` → 1934; `q104_09_haru_knockout_out` → 600; `q104_07b_carrying_comment_out` → 811.

End nodes: 600: `NonTerminating`; 811: `NonTerminating`; 1934: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 800 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scnChangeIdleAnimEvent` | 19 | 827 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scnDialogLineEvent` | 32 | 794 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnLookAtEvent` | 13 | 794 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 20 | 794 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scneventsAttachPropToNode` | 1 | 2076 / 766 | `/Data/RootChunk/sceneGraph/Data/graph/96/Data/events/14` |
| `scneventsAttachPropToPerformer` | 2 | 2056 / 688 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/1` |
| `scneventsEquipItemToPerformer` | 4 | 810 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 2 | 1982 / 671 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/5` |
| `scneventsSocket` | 34 | 794 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 1 | 810 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/9` |
| `scneventsVFXDurationEvent` | 3 | 800 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scneventsVFXEvent` | 4 | 2056 / 696 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, idle_animation, socket_signal: 3
- socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation: 1
- skeletal_animation, audio, socket_signal, animation_state: 1

Raw SHA-256: `037ac1a6496a525172ad868c1541e24933302ac7bf4c10a86556b5a42dc9e83c`. Binary SHA-256: `ade3fa39fcefb0b98a2d36174d5dc1b2f7e0fda2ad41d6190aaa549bb6c939e7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_07b_haru_found.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_07c_nomads_arrive.scene`

224 graph nodes, 259 edges; 45 event-bearing sections, 662 events; 151 screenplay lines, 12 screenplay options, 6 choice nodes.

Actors: Panam (actor 0, spawnSet); Haru (actor 1, spawnSet); Mitch (actor 2, spawnSet); Saul (actor 3, spawnSet); Nomad_01 (actor 4, community); Nomad_02 (actor 5, community); Nomad_03 (actor 6, community); Nomad_Radio (actor 7, spawnDespawn); Nomad_Radio2 (actor 8, spawnDespawn); nomad_pair_01_m (actor 9, community); nomad_pair_02_m (actor 10, community); nomad_trio_01_f (actor 11, community); nomad_trio_02_f (actor 12, community); nomad_trio_03_m (actor 13, community); nomadtruck (actor 14, spawner); bike (actor 15, community); V (actor 16, findInContext).

Entries: `q104_09_after_haru_finale_in` → 181; `Start 10` → 2436; `Start 7` → 1842; `Start 6` → 1384; `Start 0` → 2198.

Exits: `q104_09_after_haru_finale_out` → 183.

End nodes: 183: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 785 / 264 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/42` |
| `scnChangeIdleAnimEvent` | 50 | 434 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 129 | 382 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayActionEvent` | 1 | 2021 / 1814 | `/Data/RootChunk/sceneGraph/Data/graph/153/Data/events/2` |
| `scnGameplayTransitionEvent` | 11 | 434 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/13` |
| `scnIKEvent` | 22 | 434 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnLookAtEvent` | 157 | 382 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 142 | 434 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnUnmountEvent` | 11 | 434 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 13 | 434 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsSocket` | 120 | 434 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scneventsVFXEvent` | 1 | 1010 / 655 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 9
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech: 4
- speech, skeletal_animation: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 3
- skeletal_animation: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze: 2
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal, gameplay_action: 1

Raw SHA-256: `25f81908a7b27efc7f41cef94da0fe28c484cf9e19f024470e7af6e6672b4b6f`. Binary SHA-256: `2d0c1ad95a1f0c9516b2cbf64211e7d50d24e90ac3be43421abfd7c10d9e8c1e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_07c_nomads_arrive.scene" --events
```

## `base\quest\main_quests\part1\q104\scenes\q104_08_courier_talks.scene`

394 graph nodes, 492 edges; 70 event-bearing sections, 910 events; 214 screenplay lines, 37 screenplay options, 16 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Haru (actor 1, spawnSet); Takemura (actor 2, community); V (actor 3, findInContext).

Entries: `Start 20` → 5080; `q104_08_courier_talk_in` → 1; `Start 21` → 5117; `Start 22` → 5119; `Start 11` → 3852; `Start 4` → 2639; `Start 13` → 3964; `Start 16` → 3978; `Start 0` → 3479; `fluff_dialogue` → 1986; `placeholder 1` → 3261.

Exits: `q104_09b_haru_taken_out` → 1731; `fluff_dialogue_out` → 1987.

End nodes: 1731: `NonTerminating`; 1987: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 1321 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnChangeIdleAnimEvent` | 96 | 755 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnDialogLineEvent` | 186 | 755 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayTransitionEvent` | 3 | 1584 / 519 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/32` |
| `scnIKEvent` | 6 | 1584 / 483 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/6` |
| `scnLookAtAdvancedEvent` | 2 | 5144 / 3480 | `/Data/RootChunk/sceneGraph/Data/graph/387/Data/events/17` |
| `scnLookAtEvent` | 114 | 755 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnOverridePhantomParamsEvent` | 3 | 1420 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/17` |
| `scnPlaySkAnimEvent` | 210 | 755 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnUnmountEvent` | 3 | 1584 / 518 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/31` |
| `scneventsAttachPropToNode` | 7 | 1584 / 513 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/27` |
| `scneventsAttachPropToPerformer` | 11 | 1321 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsEquipItemToPerformer` | 4 | 1584 / 491 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 3 | 1584 / 514 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/28` |
| `scneventsSocket` | 230 | 755 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 2 | 1584 / 508 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/22` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1612 / 732 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/11` |
| `scneventsVFXDurationEvent` | 7 | 1420 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/16` |
| `scneventsVFXEvent` | 15 | 1139 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 24
- speech: 7
- speech, skeletal_animation, idle_animation, socket_signal: 6
- speech, skeletal_animation, gaze, socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, idle_animation: 1
- speech, idle_animation, props_equipment: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- idle_animation, vfx, socket_signal: 1

Raw SHA-256: `04183ddcc156a4d541ab767440353504fde0bd6658fe15afef6089a09b5d7c3d`. Binary SHA-256: `03e15f87d33d2745e16bb6780dba6c6499e7038cfb647580e4fc15511798d26d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q104\scenes\q104_08_courier_talks.scene" --events
```

