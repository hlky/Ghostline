# With a Little Help from My Friends: scene presentation

Journal identity: `quests/side_quest/sq027_01_basilisk_convoy`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq027_01_basilisk_convoy.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

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

## `base\quest\side_quests\sq027\scenes\sq027_01_phone_call.scene`

50 graph nodes, 52 edges; 8 event-bearing sections, 41 events; 25 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: Panam (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `sq027_01_phone_call_in` → 1; `call_again` → 77; `panam_holo_preview` → 238.

Exits: `sq027_01_taken_out` → 2; `sq027_01_delayed_out` → 73; `sq027_01_omit_out` → 339.

End nodes: 2: `<omitted>`; 73: `<omitted>`; 339: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 64 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 23 | 60 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 1 | 94 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scnPlaySkAnimEvent` | 7 | 60 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 2 | 60 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation: 3
- speech, skeletal_animation, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, socket_signal: 1

Raw SHA-256: `1921b98aaa6c55755ac3ae1c93281b99fe81ee2dbff3d93b7bcb12d4fea53054`. Binary SHA-256: `11bfb162341e8e6c8abda81b4e29894506991cd37055779ebaf46f0905930c8a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_01_phone_call.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_02_camp_mood_scenes.scene`

28 graph nodes, 29 edges; 6 event-bearing sections, 87 events; 14 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: m_01 (actor 0, community); m_02 (actor 1, community); f_01 (actor 2, community); m_03 (actor 3, community); f_02 (actor 4, community); vehicle_1 (actor 5, community); vehicle_2 (actor 6, community).

Entries: `mood_001_in` → 1.

Exits: `mood_001_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 9 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 2 | 44 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/9` |
| `scnIKEvent` | 4 | 44 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scnLookAtEvent` | 23 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 20 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnUnmountEvent` | 2 | 44 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/8` |
| `scneventsEquipItemToPerformer` | 3 | 46 / 192 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 2 | 44 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/5` |
| `scneventsSocket` | 12 | 4 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsUnequipItemFromPerformer` | 1 | 46 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `44bf95a161c531b306e38f8a693c78da70eca17bed7f33501528a54cc25e512d`. Binary SHA-256: `4eaa1583ab9a8d99fe0e179b4fb3275a475169abb46396a1c831c72e8ca91970`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_02_camp_mood_scenes.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_02_panam_and_santiago.scene`

709 graph nodes, 918 edges; 124 event-bearing sections, 1110 events; 230 screenplay lines, 29 screenplay options, 16 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); Mitch (actor 2, spawnSet); Carol (actor 3, spawnSet); Bob (actor 4, spawnSet); Teddy (actor 5, spawnSet); Cassidy (actor 6, spawnSet); Johnny (actor 7, spawnDespawn); Nomad_block_01 (actor 8, community); Nomad_block_02 (actor 9, community); panam_vehicle (actor 10, spawnSet); jammer_vehicle (actor 11, community); teddy_vehicle (actor 12, community); cassidy_Vehicle (actor 13, community); bob_vehicle (actor 14, community); V (actor 15, findInContext).

Entries: `sq027_02_panam_and_santiago_in` → 1; `DebugDrive_In` → 1252; `Start 13` → 4392; `DebugVeteranTalk_In` → 1380; `sq027_02_drive_urge_in` → 1514; `CineDebug_TableEnd` → 1555; `sq027_02_lets_drive_in` → 2196; `CineDebug_StartSaulConv` → 1619; `CineDebug_questions` → 1653; `Start 16` → 4691; `Start 17` → 4694; `CineDebug_start` → 1765; `SaulExit` → 1802; `CineDebug_PanamEnd` → 1814.

Exits: `sq027_02_panam_and_santiago_out` → 2; `sq027_02_drive_urge_out` → 1515; `sq027_02_santiago_whistleblowing_out` → 968; `sq027_02_lets_drive_out` → 2198.

End nodes: 2: `NonTerminating`; 968: `NonTerminating`; 1515: `<omitted>`; 2198: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 14 | 4054 / 4277 | `/Data/RootChunk/sceneGraph/Data/graph/614/Data/events/3` |
| `scnChangeIdleAnimEvent` | 200 | 482 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 136 | 482 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnGameplayTransitionEvent` | 13 | 503 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/16` |
| `scnIKEvent` | 32 | 503 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/6` |
| `scnLookAtEvent` | 296 | 482 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 197 | 483 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnUnmountEvent` | 13 | 503 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/17` |
| `scneventsAttachPropToWorld` | 1 | 1274 / 1665 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/35` |
| `scneventsEquipItemToPerformer` | 9 | 483 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 21 | 503 / 199 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/15` |
| `scneventsSocket` | 174 | 483 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 2 | 503 / 242 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/38` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 537 / 614 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/19` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 34
- skeletal_animation: 22
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 16
- speech, idle_animation, gaze: 9
- speech, idle_animation, gaze, socket_signal: 6
- speech: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze: 2
- skeletal_animation, idle_animation, gaze, ik, audio, socket_signal, animation_state: 2
- skeletal_animation, gaze, audio, socket_signal, animation_state: 2
- skeletal_animation, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, gaze: 1
- speech, idle_animation: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- gaze, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `bed28c49b5baf4efd728fded9ee01f2cf626780654707519eec7cd0dabdaa224`. Binary SHA-256: `22da54c8856d9ef8d6d412d7de5af0dc1ce2518191d4425421959251ccc5e277`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_02_panam_and_santiago.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_03_panams_plan.scene`

273 graph nodes, 331 edges; 26 event-bearing sections, 480 events; 47 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: Panam (actor 0, spawnSet); Bob (actor 1, spawnSet); Mitch (actor 2, spawnSet); Teddy (actor 3, spawnSet); Carol (actor 4, spawnSet); Cassidy (actor 5, spawnSet); panam_vehicle (actor 6, spawnSet); teddy_vehicle (actor 7, community); cassidy_vehicle (actor 8, community); carol_jammer (actor 9, community); V (actor 10, findInContext).

Entries: `preview` → 1836; `sq027_03_after_together_in` → 1; `cinedebug_endscene` → 856; `sq027_03_after_omited_in` → 250; `cinedebug_panamspeech` → 876; `cinedebug_carol` → 2557.

Exits: `sq027_03_panams_plan_out` → 2; `panam_at_door_spot_end` → 1106; `KillSignal` → 371.

End nodes: 2: `NonTerminating`; 371: `<omitted>`; 1106: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 1121 / 1111 | `/Data/RootChunk/sceneGraph/Data/graph/110/Data/events/4` |
| `scnChangeIdleAnimEvent` | 73 | 122 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 25 | 122 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 17 | 277 / 344 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/68` |
| `scnIKEvent` | 40 | 277 / 314 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/47` |
| `scnLookAtEvent` | 110 | 122 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 62 | 131 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 860 / 918 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/9` |
| `scnUnmountEvent` | 17 | 277 / 345 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/69` |
| `scneventsEquipItemToPerformer` | 5 | 131 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/45` |
| `scneventsSetAnimFeatureEvent` | 23 | 277 / 341 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/66` |
| `scneventsSocket` | 102 | 131 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 2 | 277 / 328 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/57` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, idle_animation, gaze: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- ik, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `9072ff31a1f7f39d6a43028f7e12c78f36249e5b7dae0719dcd22fb871e021d3`. Binary SHA-256: `62dfd6e958e0a9257854388789afb62c223ba1d95630cb0fbd1ab9c01709f9e2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_03_panams_plan.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_03_saul_whistleblowing.scene`

90 graph nodes, 118 edges; 23 event-bearing sections, 221 events; 63 screenplay lines, 9 screenplay options, 3 choice nodes.

Actors: Saul (actor 0, spawnSet); Johnny (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `abort_panam_path_out` → 150; `End 0` → 2; `ratted_out` → 410.

End nodes: 2: `<omitted>`; 150: `NonTerminating`; 410: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 42 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 49 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 35 | 13 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnPlaySkAnimEvent` | 63 | 13 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scneventsEquipItemToPerformer` | 2 | 437 / 710 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/1` |
| `scneventsSocket` | 28 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 1 | 437 / 714 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/5` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 118 / 415 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- gaze: 5
- skeletal_animation: 3
- socket_signal: 3
- speech, idle_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2

Raw SHA-256: `80530089726e46a7db8ebc56c1b525b9048a2283dbdb604e02829456a7188756`. Binary SHA-256: `7c02ac7cd644aeab9ca19a80a3e533288fd454c2af8699c86f8224acfb401120`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_03_saul_whistleblowing.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_03a_chats_to_locomotive.scene`

89 graph nodes, 87 edges; 17 event-bearing sections, 187 events; 37 screenplay lines, 6 screenplay options, 6 choice nodes.

Actors: Panam (actor 0, spawnSet); Mitch (actor 1, spawnSet); Bob (actor 2, spawnSet); Cassidy (actor 3, spawnSet); Teddy (actor 4, spawnSet); Carol (actor 5, spawnSet); Panam_Veh (actor 6, spawnSet); Jammer (actor 7, community); Cassidy_veh (actor 8, community); Teddy_veh (actor 9, community); V (actor 10, findInContext).

Entries: `sq027_03a_chat_start_in` → 1; `sq027_03a_chat_001_in` → 7; `sq027_03a_chat_002_in` → 12; `preview_setup` → 670; `sq027_03a_chat_arrived_in` → 17; `sq027_03a_chat_003_in` → 22; `teddy_station_unmount` → 759; `sq027_03a_drive_skip_in` → 175; `carol_station_unmount` → 761; `cassidy_station_unmount` → 763; `bob_station_unmount` → 765; `mitch_station_unmount` → 767.

Exits: `sq027_03a_chat_start_out` → 2; `sq027_03a_chat_001_out` → 8; `sq027_03a_chat_002_out` → 13; `sq027_03a_chat_arrived_out` → 18; `sq027_03a_chat_003_out` → 23; `sq027_03a_drive_skip_out` → 176; `teddy_station_unmount_out` → 780; `carol_station_unmount_out` → 782; `cassidy_station_unmount_out` → 784; `bob_station_unmount_out` → 786; `mitch_station_unmount_out` → 788.

End nodes: 2: `NonTerminating`; 8: `NonTerminating`; 13: `NonTerminating`; 18: `NonTerminating`; 23: `NonTerminating`; 176: `<omitted>`; 780: `NonTerminating`; 782: `NonTerminating`; 784: `NonTerminating`; 786: `NonTerminating`; 788: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 774 / 428 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/5` |
| `scnChangeIdleAnimEvent` | 16 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 29 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 6 | 774 / 435 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/11` |
| `scnIKEvent` | 32 | 9 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/7` |
| `scnLookAtEvent` | 19 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 26 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 6 | 774 / 434 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 17 | 9 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsSocket` | 26 | 9 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 3
- speech, idle_animation, gaze, ik, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation: 1
- idle_animation, gaze: 1
- ik, socket_signal, animation_state: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `9b12ced1e33d3f819fd2464593d547d86792fdae9ee47efc3bdaeba8a862d667`. Binary SHA-256: `ad36fe1c3e03e8e4f6666977bd6fe892912f9ca9b5d5e5515e0c101e1d3b8f84`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_03a_chats_to_locomotive.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_03a_holocall_panam_betrayed.scene`

26 graph nodes, 29 edges; 10 event-bearing sections, 57 events; 25 screenplay lines, 6 screenplay options, 2 choice nodes.

Actors: Panam (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 20 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 24 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 1 | 135 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 9 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsSocket` | 3 | 6 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation: 3
- speech, idle_animation: 3
- speech, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- gaze: 1

Raw SHA-256: `0e5b1d0974bfd2a6ba4f01ec43b3bc78029affcf054757fbfa4fea6aca3f2f57`. Binary SHA-256: `ca33be0b36c38ed79640a90d5bf7259fa7c76d4056ec1a3b8a57f1635cf0d941`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_03a_holocall_panam_betrayed.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_04_preparations_carol.scene`

29 graph nodes, 32 edges; 10 event-bearing sections, 71 events; 24 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: Carol (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `sq027_04_prep_carol_in` → 488; `Start 4` → 780.

Exits: `sq027_04_prep_carol_out` → 511.

End nodes: 511: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 16 | 535 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 19 | 535 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 15 | 535 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 6 | 544 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scneventsSocket` | 13 | 544 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scneventsVFXEvent` | 2 | 535 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, idle_animation: 2
- speech, idle_animation, gaze: 2
- speech, idle_animation, gaze, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `5708e91234fafa477a7ab9af6c3d3b577f83e63747b9296ef5376418d6d003bd`. Binary SHA-256: `e7c7697b4f14bd6d8e8f064e8ede851215c04b7cf81a87c698c45aa903da4320`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_04_preparations_carol.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_04_preparations_cassidy_teddy.scene`

122 graph nodes, 153 edges; 20 event-bearing sections, 210 events; 45 screenplay lines, 11 screenplay options, 4 choice nodes.

Actors: Teddy (actor 0, spawnSet); Cassidy (actor 1, spawnSet); Nomad_CassidyCar (actor 2, community); Nomad_TeddyCar (actor 3, community); V (actor 4, findInContext).

Entries: `sq027_04_prep_teddy_cass_in` → 489; `CinematicDebug` → 577.

Exits: `sq027_04_prep_teddy_cass_out` → 507.

End nodes: 507: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 25 | 508 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 34 | 508 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 57 | 508 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 43 | 508 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnPoseCorrectionEvent` | 2 | 551 / 230 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/14` |
| `scneventsEquipItemToPerformer` | 1 | 551 / 276 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/38` |
| `scneventsSetAnimFeatureEvent` | 3 | 551 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/8` |
| `scneventsSocket` | 44 | 508 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 551 / 229 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- gaze: 4
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1

Raw SHA-256: `34f6194800024febfdcfc528cbca0c88459fa9e08e57e1c739737fb867a63677`. Binary SHA-256: `d7378d0d7cc042ce439692cafb476b07d93433b25bb857123d461449d406a954`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_04_preparations_cassidy_teddy.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_04_preparations_mitch_bob.scene`

89 graph nodes, 106 edges; 15 event-bearing sections, 90 events; 26 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Bob (actor 0, spawnSet); Mitch (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `sq027_04_prep_bob_mitch_in` → 490; `CineDebug_Fix` → 642.

Exits: `sq027_04_prep_bob_mitch_out_terminating` → 997; `sq027_04_prep_bob_mitch_out` → 510.

End nodes: 510: `NonTerminating`; 997: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 19 | 10 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 15 | 10 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 17 | 10 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 18 | 10 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scneventsEquipItemToPerformer` | 5 | 10 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scneventsSocket` | 16 | 10 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 6
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, idle_animation, gaze: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1

Raw SHA-256: `2d981b69290f3c659e61c1231e069c5723cbecb99a7f94c2b71598fb382e137e`. Binary SHA-256: `42e08d236be72082005f9f0abca632f0ce97975c0b2158a089c9ddd5d93b2318`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_04_preparations_mitch_bob.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_04_preparations_panam.scene`

606 graph nodes, 752 edges; 110 event-bearing sections, 953 events; 219 screenplay lines, 39 screenplay options, 22 choice nodes.

Actors: Panam (actor 0, spawnSet); Carol (actor 1, spawnSet); Bob (actor 2, spawnSet); Mitch (actor 3, spawnSet); Johnny (actor 4, spawnDespawn); Teddy (actor 5, spawnSet); Cassidy (actor 6, spawnSet); Train (actor 7, community); trailer_001 (actor 8, community); trailer_002 (actor 9, community); V (actor 10, findInContext).

Entries: `CinematicDebug_TowerEnter003` → 2063; `CineDebug_PanamWindow` → 2067; `CinematicDebug_console` → 2069; `CineDebug_LocomotiveMoving` → 2071; `CineDebug_CardFound` → 2081; `techie_input` → 1116; `solo_input` → 1132; `netruner_imput` → 1133; `generic_imput` → 1134; `cinedebug_card_hold` → 3192; `sq027_04_panam_at_door_in` → 675; `Cinedebug_DoorOpen` → 3943; `sq027_04_approach_eng_in` → 968; `sq027_04_approach_generic_in` → 969; `sq027_04_approach_net_in` → 970; `sq027_04_approach_solo_in` → 971; `cinedebug_sceneend` → 4071.

Exits: `return_walktalk_out` → 2161; `sq027_04_approach_out` → 676; `sq027_04_emotions_out` → 744; `sq027_time_set_out` → 2017.

End nodes: 676: `<omitted>`; 744: `<omitted>`; 2017: `NonTerminating`; 2161: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 698 / 486 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/3` |
| `scnChangeIdleAnimEvent` | 190 | 579 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 160 | 505 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 16 | 607 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/27` |
| `scnIKEvent` | 32 | 607 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/19` |
| `scnLookAtEvent` | 159 | 579 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 180 | 579 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnUnmountEvent` | 16 | 607 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/26` |
| `scneventsAttachPropToNode` | 2 | 4749 / 4137 | `/Data/RootChunk/sceneGraph/Data/graph/590/Data/events/0` |
| `scneventsAttachPropToPerformer` | 3 | 698 / 485 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 698 / 489 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/6` |
| `scneventsCameraParamsEvent` | 5 | 1106 / 1129 | `/Data/RootChunk/sceneGraph/Data/graph/73/Data/events/8` |
| `scneventsEquipItemToPerformer` | 4 | 873 / 626 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 16 | 607 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/23` |
| `scneventsSocket` | 163 | 595 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 4421 / 3892 | `/Data/RootChunk/sceneGraph/Data/graph/541/Data/events/1` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 873 / 630 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 24
- skeletal_animation: 10
- speech: 8
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 8
- speech, skeletal_animation, idle_animation, gaze: 6
- skeletal_animation, socket_signal: 5
- gaze: 5
- speech, idle_animation, gaze: 4
- props_equipment: 4
- skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 3
- idle_animation, gaze, socket_signal: 3
- speech, idle_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, idle_animation: 2
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- socket_signal: 2
- camera: 2
- speech, skeletal_animation, idle_animation, props_equipment, audio: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `d4da5a33bc4acaf2552879118b22aaf220ad2179e4e8bba90ddf48c6c5d73ff5`. Binary SHA-256: `8f8acbc3d4b63b5fa1095cdad0f6fe3c81402fb556813f4caeb70ade191b124e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_04_preparations_panam.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_04a_camping.scene`

670 graph nodes, 899 edges; 155 event-bearing sections, 637 events; 195 screenplay lines, 12 screenplay options, 5 choice nodes.

Actors: Panam (actor 0, spawnSet); Mitch (actor 1, spawnSet); Carol (actor 2, spawnSet); Bob (actor 3, spawnSet); Teddy (actor 4, spawnSet); Cassidy (actor 5, spawnSet); V (actor 6, findInContext).

Entries: `cinedebug_chars_drinking` → 2573; `cinedebug_v_drink` → 1991; `cinematic_debug_preview` → 2066; `sq027_04a_cassidy_start_playing` → 914; `sq027_04a_panam_comment_in` → 443.

Exits: `End1` → 352.

End nodes: 352: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 416 / 495 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/4` |
| `scnChangeIdleAnimEvent` | 115 | 299 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 56 | 12 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnLookAtEvent` | 200 | 12 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 127 | 299 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsAttachPropToPerformer` | 13 | 652 / 894 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/1` |
| `scneventsAttachPropToWorld` | 12 | 652 / 896 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/3` |
| `scneventsCameraParamsEvent` | 1 | 1973 / 2092 | `/Data/RootChunk/sceneGraph/Data/graph/357/Data/events/1` |
| `scneventsEquipItemToPerformer` | 4 | 897 / 1162 | `/Data/RootChunk/sceneGraph/Data/graph/113/Data/events/0` |
| `scneventsSocket` | 103 | 299 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/25` |
| `scneventsVFXEvent` | 5 | 299 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 82
- skeletal_animation: 21
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- socket_signal: 10
- skeletal_animation, gaze, props_equipment, socket_signal: 9
- speech, idle_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, gaze, socket_signal: 1
- speech: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- vfx, socket_signal: 1
- skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- camera, vfx: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- props_equipment: 1

Raw SHA-256: `20fea9c26fb4714b20f2722362ef6b81cba2ac7aa5f18feeb13c40cc44cf5937`. Binary SHA-256: `3fc9218f1edb9886bcf5e7b469a562232ceb6ae355fbc6533f821d86e652f035`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_04a_camping.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_05_ambush.scene`

532 graph nodes, 617 edges; 74 event-bearing sections, 349 events; 97 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Panam (actor 0, spawnSet); Teddy (actor 1, spawnSet); Cassidy (actor 2, spawnSet); Bob (actor 3, spawnSet); Carol (actor 4, spawnSet); Mitch (actor 5, spawnSet); MilitechSec_001 (actor 6, community); panam_vehicle (actor 7, spawnSet); teddy_vehicle (actor 8, community); cassidy_vehidle (actor 9, community); carol_vehicle (actor 10, community); V (actor 11, findInContext).

Entries: `sq027_05_battlecry_01_in` → 8; `sq027_05_battlecry_02_in` → 21; `sq027_05_drivestart_in` → 36; `sq027_05_escorts_defeated_in` → 44; `sq027_05_get_in_car` → 59; `sq027_05_escorts_engaged_in` → 98; `sq027_05_trucks_start_moving_in` → 108; `sq027_05_battlecry_03_in` → 112; `sq027_05_trucks_arrive_in` → 123; `sq027_03a_militech_combat_001_in` → 127; `sq027_03a_militech_combat_002_in` → 130; `sq027_03a_nomads_combat_001_in` → 133; `sq027_03a_nomads_combat_002_in` → 136; `sq027_05_clamp_shot_in` → 254; `cinedebug_drivingsections` → 1839; `Start 5` → 2839; `Start 6` → 2841; `Start 7` → 2845.

Exits: `sq027_05_get_in_car_out` → 75; `sq027_05_drivestart_out` → 82; `sq027_05_battlecry_01_out` → 83; `sq027_05_battlecry_02_out` → 84; `sq027_05_escorts_engaged_out` → 100; `sq027_05_battlecry_03_out` → 114; `sq027_05_trucks_arrive_out` → 124; `sq027_03a_militech_combat_001_out` → 129; `sq027_03a_militech_combat_002_out` → 132; `sq027_03a_nomads_combat_001_out` → 135; `sq027_03a_nomads_combat_002_out` → 138; `sq027_05_cut_nomad_driving_out` → 2150; `sq027_05_trucks_drive_arrived_out` → 2155; `sq027_05_clamp_shot_out` → 255; `sq027_05_connect_out` → 953.

End nodes: 75: `<omitted>`; 82: `NonTerminating`; 83: `NonTerminating`; 84: `NonTerminating`; 100: `NonTerminating`; 114: `NonTerminating`; 124: `<omitted>`; 129: `<omitted>`; 132: `<omitted>`; 135: `<omitted>`; 138: `<omitted>`; 255: `NonTerminating`; 953: `NonTerminating`; 2150: `NonTerminating`; 2155: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 104 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/9` |
| `scnChangeIdleAnimEvent` | 35 | 37 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 44 | 37 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnGameplayTransitionEvent` | 11 | 104 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/16` |
| `scnIKEvent` | 48 | 37 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnLookAtEvent` | 40 | 37 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 58 | 37 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnUnmountEvent` | 10 | 104 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 28 | 37 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsSocket` | 58 | 37 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 978 / 901 | `/Data/RootChunk/sceneGraph/Data/graph/145/Data/events/9` |
| `scneventsVFXEvent` | 6 | 245 / 334 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/16` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 23
- gaze: 15
- speech: 11
- speech, idle_animation: 3
- speech, idle_animation, gaze: 2
- skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 2
- idle_animation, gaze, ik, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, ik, socket_signal, animation_state: 1
- socket_signal: 1
- skeletal_animation, ik, audio, socket_signal, animation_state: 1
- skeletal_animation, gaze, audio, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `fb398643f49a0e5289192dd224e3c5197c4ac02c92c9c44e18a399c79d7d44f2`. Binary SHA-256: `249313e4ba43839aa2ed563c1340b7637c7dc660bd6f098ab938b55bf7f92478`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_05_ambush.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_05a_transport_delivered.scene`

303 graph nodes, 380 edges; 35 event-bearing sections, 425 events; 64 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Saul (actor 0, spawnSet); Panam (actor 1, spawnSet); Carol (actor 2, spawnSet); Bob (actor 3, spawnSet); Teddy (actor 4, spawnSet); Cassidy (actor 5, spawnSet); Mitch (actor 6, spawnSet); guard1 (actor 7, community); guard2 (actor 8, community); guard3 (actor 9, community); Panzer_Flatbed_A (actor 10, community); Panzer_Flatbed_B (actor 11, community); V (actor 12, findInContext).

Entries: `sq027_05a_saul_reception_in` → 1; `cinedebug_end` → 1790; `cinedebug_panamend` → 1339.

Exits: `sq027_05a_saul_reception_out` → 2; `sq027_05a_scene_over_out` → 579.

End nodes: 2: `<omitted>`; 579: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 77 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 38 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 13 | 25 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/36` |
| `scnIKEvent` | 26 | 25 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/18` |
| `scnLookAtEvent` | 70 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 77 | 25 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnUnmountEvent` | 13 | 25 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/34` |
| `scneventsEquipItemToPerformer` | 3 | 350 / 582 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/112` |
| `scneventsSetAnimFeatureEvent` | 13 | 25 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/32` |
| `scneventsSocket` | 93 | 25 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 2 | 338 / 414 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, socket_signal: 8
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation: 3
- speech, idle_animation, gaze: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1

Raw SHA-256: `1161d3819c6445e6f39ff6f56e8a45629ac1a2b8bc2fbc4aeef1fc3c1fb07c0a`. Binary SHA-256: `07de58be6e6be0cbce17a082dc610f1df8043d525ab01dc7060ad15e213a90e6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_05a_transport_delivered.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_05b_holocall_basilisk_ready.scene`

31 graph nodes, 35 edges; 3 event-bearing sections, 14 events; 7 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Panam (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 11 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 7 | 11 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation: 3

Raw SHA-256: `f9fe815b5790246e27d2e6f3257205e8111b0176d77c01713ce5cda39227c9f7`. Binary SHA-256: `69cec76c5fef205e35ec19ced27d2dd20f479fd2179eceba4e9ac70ef425ad2f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_05b_holocall_basilisk_ready.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_06_panzer.scene`

838 graph nodes, 1041 edges; 147 event-bearing sections, 1310 events; 234 screenplay lines, 18 screenplay options, 10 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, findInContext); Mitch (actor 2, spawnSet); Teddy (actor 3, spawnSet); Carol (actor 4, spawnSet); Cassidy (actor 5, spawnSet); Bob (actor 6, spawnSet); Johnny (actor 7, spawnDespawn); TPP_V_Male (actor 8, spawnDespawn); FPP_Panam (actor 9, spawnDespawn); TPP_V_Female (actor 10, spawnDespawn); TPP_V_Male_No_Impostor (actor 11, spawnDespawn); Panzer (actor 12, spawnSet); V (actor 13, findInContext).

Entries: `sq027_06_marauders_in` → 985; `sq027_06_near_panzer_in` → 423; `CineDebug_PanamSex` → 1290; `sq027_06_scene_setup` → 5257; `sq027_06_arrived_in` → 575; `Cinedebug_v_plugin` → 2921; `sq027_06_sex_in` → 592; `sq027_06_testdrive_in` → 595; `CineDebug_PanamSex2` → 1429.

Exits: `sq027_06_sex_out` → 983; `sq027_06_marauders_out` → 986; `sq027_06_basilisk_out` → 568; `sq027_06_arrived_out` → 578; `sq027_06_testdrive_out` → 596; `Quest_Boundaries_Out` → 2248.

End nodes: 568: `NonTerminating`; 578: `<omitted>`; 596: `<omitted>`; 983: `<omitted>`; 986: `<omitted>`; 2248: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 19 | 881 / 691 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/7` |
| `scnChangeIdleAnimEvent` | 132 | 424 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 137 | 424 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayActionEvent` | 6 | 1448 / 1096 | `/Data/RootChunk/sceneGraph/Data/graph/143/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 3185 / 3427 | `/Data/RootChunk/sceneGraph/Data/graph/276/Data/events/6` |
| `scnIKEvent` | 6 | 3185 / 3423 | `/Data/RootChunk/sceneGraph/Data/graph/276/Data/events/3` |
| `scnLookAtEvent` | 115 | 424 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 2045 / 2763 | `/Data/RootChunk/sceneGraph/Data/graph/174/Data/events/11` |
| `scnPlayRidAnimEvent` | 166 | 1448 / 1112 | `/Data/RootChunk/sceneGraph/Data/graph/143/Data/events/7` |
| `scnPlaySkAnimEvent` | 427 | 424 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/16` |
| `scnPoseCorrectionEvent` | 4 | 451 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnUnmountEvent` | 1 | 6665 / 6394 | `/Data/RootChunk/sceneGraph/Data/graph/832/Data/events/4` |
| `scneventsAttachPropToPerformer` | 3 | 3344 / 3585 | `/Data/RootChunk/sceneGraph/Data/graph/292/Data/events/4` |
| `scneventsAttachPropToWorld` | 1 | 3930 / 4192 | `/Data/RootChunk/sceneGraph/Data/graph/386/Data/events/0` |
| `scneventsEquipItemToPerformer` | 3 | 798 / 446 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/5` |
| `scneventsPlayRidCameraAnimEvent` | 54 | 1448 / 1122 | `/Data/RootChunk/sceneGraph/Data/graph/143/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 31 | 577 / 205 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scneventsSocket` | 149 | 424 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 1 | 798 / 449 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/8` |
| `scneventsVFXEvent` | 51 | 1448 / 1218 | `/Data/RootChunk/sceneGraph/Data/graph/143/Data/events/44` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 34
- skeletal_animation: 20
- gaze: 15
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- vfx: 5
- speech, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, idle_animation, gaze, socket_signal: 3
- skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, idle_animation: 3
- socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 2
- speech, idle_animation: 2
- speech, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- skeletal_animation, idle_animation, rid_actor, camera, rid_camera, vfx, socket_signal: 2
- skeletal_animation, idle_animation, props_equipment: 2
- animation_state: 2
- skeletal_animation, socket_signal, animation_state: 2
- speech, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, rid_actor, camera, rid_camera, audio, vfx, socket_signal, gameplay_action: 1
- skeletal_animation, vfx, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- gaze, socket_signal: 1
- idle_animation, audio, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, audio, socket_signal, animation_state: 1
- idle_animation, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- idle_animation, ik, gameplay_transition, socket_signal, animation_state, gameplay_action: 1
- idle_animation, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- idle_animation, gaze: 1
- skeletal_animation, socket_signal: 1
- gaze, socket_signal, animation_state: 1
- props_equipment, vfx: 1
- idle_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal, animation_state: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, audio, socket_signal, animation_state: 1
- speech, audio, socket_signal: 1
- idle_animation, socket_signal, animation_state, gameplay_action: 1
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `e513f9bddaefd7a0e03eea910600288d909f2e0a85f2389624d12ddfd6d40c10`. Binary SHA-256: `2e9029faf8b8c8efe612d97bc5ffe7b900a79235e3237c0b9b087bad4ceae68d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_06_panzer.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_07_nomad_camp_attack.scene`

41 graph nodes, 38 edges; 9 event-bearing sections, 33 events; 13 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnDespawn); Panzer (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `sq027_07_marauders_in` → 338; `sq027_07_leave_warning_ambush_reuse_in` → 345; `sq027_07_hit_comment` → 232; `sq027_07_camp_in` → 27; `sq027_07_leave_warning_in` → 332; `sq027_07_reminder_in` → 376.

Exits: `sq027_07_marauders_out` → 340; `sq027_07_leave_warning_ambush_reuse_out` → 347; `sq027_07_camp_out` → 323; `sq027_07_leave_warning_out` → 334.

End nodes: 323: `<omitted>`; 334: `<omitted>`; 340: `<omitted>`; 347: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 230 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 10 | 230 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnLookAtEvent` | 6 | 230 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnPlaySkAnimEvent` | 6 | 230 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 1 | 230 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze: 1

Raw SHA-256: `ed5a9b9ecdfd8f4f3f6eeac5256ce412ad2c27708703b3736121d1e23b8c5235`. Binary SHA-256: `5bee64f652e2a1f3aa5a259604abdaf27676f749dd55ce54cc52a3c09fcddf19`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_07_nomad_camp_attack.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_08_camp_saved.scene`

426 graph nodes, 507 edges; 78 event-bearing sections, 628 events; 127 screenplay lines, 15 screenplay options, 7 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); Mitch (actor 2, spawnSet); Teddy (actor 3, spawnSet); Bob (actor 4, spawnSet); Carol (actor 5, spawnSet); Cassidy (actor 6, spawnSet); Saul_holocall (actor 7, spawnDespawn); ALDECALDOS_01 (actor 8, community); ALDECALDOS_02 (actor 9, community); ALDECALDOS_03 (actor 10, community); Panzer (actor 11, spawnSet); Teddy_Car (actor 12, community); Bob_Car (actor 13, community); Cassity_Car (actor 14, community); Mitch_Car (actor 15, spawnSet); Carol_Car (actor 16, community); V (actor 17, findInContext).

Entries: `Cinedebug_saulend` → 1217; `RETROFIX_CYB661006` → 3230; `CineDebug_BarScene` → 912; `cinedebug_PanamSaul_end` → 2591; `sq027_08_01_mood_chat_in` → 1456; `Cinedebug_SaulPanam` → 1068; `sq027_08_camp_saved_in` → 702; `cinedebug_walktalk` → 1177.

Exits: `sq027_08_camp_saved_out` → 238; `sq027_08_01_mood_chat_out` → 1457.

End nodes: 238: `<omitted>`; 1457: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 2768 / 2449 | `/Data/RootChunk/sceneGraph/Data/graph/342/Data/events/9` |
| `scnChangeIdleAnimEvent` | 110 | 277 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/5` |
| `scnDialogLineEvent` | 85 | 9 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 11 | 277 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/93` |
| `scnIKEvent` | 22 | 277 / 186 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/85` |
| `scnLookAtEvent` | 105 | 277 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnPlaySkAnimEvent` | 118 | 277 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnUnmountEvent` | 11 | 277 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/94` |
| `scneventsAttachPropToPerformer` | 11 | 492 / 461 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/3` |
| `scneventsAttachPropToWorld` | 9 | 492 / 470 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/10` |
| `scneventsCameraParamsEvent` | 4 | 641 / 648 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/1` |
| `scneventsEquipItemToPerformer` | 2 | 2604 / 2312 | `/Data/RootChunk/sceneGraph/Data/graph/321/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 15 | 277 / 199 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/92` |
| `scneventsSocket` | 111 | 277 / 142 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/55` |
| `scneventsUnequipItemFromPerformer` | 1 | 3120 / 2874 | `/Data/RootChunk/sceneGraph/Data/graph/402/Data/events/2` |
| `scneventsUnequipItemFromPerformerByItem` | 3 | 1129 / 905 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/2` |
| `scneventsVFXEvent` | 8 | 284 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/17` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- skeletal_animation, props_equipment, socket_signal: 6
- idle_animation, gaze: 5
- speech, idle_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation: 3
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- gaze: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, socket_signal: 1
- vfx: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment, socket_signal, animation_state: 1
- socket_signal, animation_state: 1

Raw SHA-256: `68694fe08359cac8a4ebcbf4cfd1b8cbe38f192168a5df7548ad698caf67f26d`. Binary SHA-256: `6c5d4682e491207dd70d1aea022b31df8206388decb3534b6cafa95b2300c967`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_08_camp_saved.scene" --events
```

## `base\quest\side_quests\sq027\scenes\sq027_09_new_camp_wakeup.scene`

344 graph nodes, 415 edges; 77 event-bearing sections, 647 events; 141 screenplay lines, 21 screenplay options, 10 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); Mitch (actor 2, spawnSet); Teddy (actor 3, spawnSet); Bob (actor 4, spawnSet); Carol (actor 5, spawnSet); Cassidy (actor 6, spawnSet); Johnny (actor 7, spawnDespawn); V (actor 8, findInContext).

Entries: `CineDebug_Car` → 1248; `sq027_09_new_camp_wakeup_in` → 702; `cinedebug_endatcar` → 1319.

Exits: `sq027_09_new_camp_wakeup_out` → 238.

End nodes: 238: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 847 / 703 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/4` |
| `scnChangeIdleAnimEvent` | 113 | 545 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 100 | 545 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 7 | 600 / 408 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/9` |
| `scnIKEvent` | 14 | 600 / 400 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scnLookAtEvent` | 95 | 545 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 179 | 545 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 7 | 600 / 407 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/8` |
| `scneventsCameraParamsEvent` | 7 | 847 / 706 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/7` |
| `scneventsEquipItemToPerformer` | 2 | 3163 / 2676 | `/Data/RootChunk/sceneGraph/Data/graph/331/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 7 | 600 / 405 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/7` |
| `scneventsSocket` | 105 | 545 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scneventsUnequipItemFromPerformer` | 1 | 3163 / 2678 | `/Data/RootChunk/sceneGraph/Data/graph/331/Data/events/7` |
| `scneventsVFXEvent` | 8 | 615 / 553 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 24
- speech, skeletal_animation, idle_animation, socket_signal: 6
- skeletal_animation: 5
- skeletal_animation, idle_animation, gaze, socket_signal: 4
- gaze: 4
- skeletal_animation, idle_animation, gaze: 4
- skeletal_animation, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, idle_animation, gaze: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, socket_signal: 2
- vfx: 2
- speech: 2
- speech, idle_animation: 2
- skeletal_animation, gaze: 2
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, camera, vfx: 1
- skeletal_animation, gaze, camera, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `d3cc5af2fc50b4476c53066484dd9eb41c649e4e9cfdf9fba1f45c5c4229834e`. Binary SHA-256: `5cca608d7a3162d361705447d24bce7b1de3257968241a0889505771abd8686f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq027\scenes\sq027_09_new_camp_wakeup.scene" --events
```

