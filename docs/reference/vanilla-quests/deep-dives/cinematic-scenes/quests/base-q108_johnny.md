# Never Fade Away: scene presentation

Journal identity: `quests/main_quest/act_01/q108_johnny`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q108_johnny.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q108\scenes\q108_02_backstage.scene`

177 graph nodes, 219 edges; 26 event-bearing sections, 605 events; 32 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: Kerry (actor 0, spawnSet); alt (actor 1, spawnSet); fan_backstage_m_01 (actor 2, community); fan_backstage_f_01 (actor 3, community); hammer_bdg_01 (actor 4, community); hammer_bdg_02 (actor 5, community); hammer_bdg_03 (actor 6, community); johnny_mirror (actor 7, spawnSet); denny (actor 8, spawnSet); henry (actor 9, spawnSet); nancy (actor 10, spawnSet); fan_backstage_m_02 (actor 11, community); fan_backstage_f_02 (actor 12, community); fan_backstage_f_03 (actor 13, community); fan_backstage_m_03 (actor 14, community); fan_backstage_m_04 (actor 15, community); staff_backstage_f_01 (actor 16, community); staff_backstage_m_01 (actor 17, community); staff_backstage_m_02 (actor 18, community); Player (actor 19, findInContext).

Entries: `in` → 1453; `Start 3` → 1700.

Exits: `out` → 3.

End nodes: 3: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 37 | 84 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnChangeIdleAnimEvent` | 5 | 88 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 30 | 84 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnLookAtEvent` | 28 | 84 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnPlayRidAnimEvent` | 82 | 1092 / 309 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/18` |
| `scnPlaySkAnimEvent` | 226 | 84 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsAttachPropToNode` | 1 | 1307 / 1205 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/40` |
| `scneventsAttachPropToPerformer` | 23 | 84 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scneventsAttachPropToWorld` | 16 | 84 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/17` |
| `scneventsCameraParamsEvent` | 3 | 764 / 181 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/9` |
| `scneventsPlayRidCameraAnimEvent` | 47 | 1092 / 325 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/23` |
| `scneventsSocket` | 75 | 84 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 32 | 1092 / 297 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal: 1
- skeletal_animation, gaze, rid_actor, camera, rid_camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, rid_actor, camera, rid_camera, props_equipment, audio, vfx, socket_signal: 1
- speech, gaze: 1
- props_equipment: 1
- skeletal_animation: 1

Raw SHA-256: `2e208ceacb77a94d2e714f941264413e0373a94ed17f9990b1628fdd06358e97`. Binary SHA-256: `f3eb856032f6e5e1f2d5ead1a1e9f78552bced0f83aacecc0f7675bb4e5c21ce`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_02_backstage.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_04_exit.scene`

148 graph nodes, 189 edges; 32 event-bearing sections, 228 events; 48 screenplay lines, 15 screenplay options, 8 choice nodes.

Actors: alt (actor 0, spawnSet); kerry (actor 1, spawnSet); fan (actor 2, spawnDespawn); Johnny_mirror (actor 3, spawnSet); Johnny (actor 4, findInContext).

Entries: `in` → 1; `Start 8` → 1186; `Start 6` → 856.

Exits: `out` → 220.

End nodes: 220: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 16 | 136 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scnChangeIdleAnimEvent` | 17 | 136 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 41 | 136 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnGameplayTransitionEvent` | 1 | 206 / 306 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/12` |
| `scnIKEvent` | 2 | 206 / 297 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/4` |
| `scnLookAtEvent` | 25 | 136 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnPlaySkAnimEvent` | 52 | 136 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnUnmountEvent` | 1 | 206 / 305 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/11` |
| `scneventsAttachPropToPerformer` | 2 | 210 / 339 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/2` |
| `scneventsAttachPropToWorld` | 9 | 157 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scneventsCameraParamsEvent` | 4 | 143 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 1 | 206 / 303 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/10` |
| `scneventsSocket` | 45 | 136 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsVFXDurationEvent` | 4 | 317 / 503 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/11` |
| `scneventsVFXEvent` | 8 | 136 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation, gaze: 3
- skeletal_animation: 3
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, socket_signal: 2
- speech: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- socket_signal: 1
- skeletal_animation, props_equipment, vfx, socket_signal: 1
- camera: 1

Raw SHA-256: `8c472d36615ac61378aaa9585588e18d0598925cd2b6e31f0002957801788ec0`. Binary SHA-256: `349fcfe23ece8cbf14ea95d4d922887bbe42192377dc2601093ffa31df6c3982`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_04_exit.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_05_backalley.scene`

137 graph nodes, 173 edges; 34 event-bearing sections, 215 events; 69 screenplay lines, 11 screenplay options, 6 choice nodes.

Actors: alt (actor 0, spawnSet); Thug_01 (actor 1, community); thompson (actor 2, spawnSet); Thug_02 (actor 3, community); Thug_03 (actor 4, community); Thug_04 (actor 5, community); kerry (actor 6, spawnSet); Player (actor 7, findInContext).

Entries: `in_thug_02_die` → 1088; `in_thug_01` → 831; `in_thug_03` → 834; `in_thug_04` → 837; `in_dbg_combat_start` → 973; `in` → 47.

Exits: `out_end_scene` → 985; `out_combat` → 63.

End nodes: 63: `NonTerminating`; 985: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 215 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/5` |
| `scnChangeIdleAnimEvent` | 8 | 36 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 43 | 29 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnGameplayTransitionEvent` | 4 | 1060 / 486 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/11` |
| `scnIKEvent` | 8 | 1060 / 465 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/1` |
| `scnLookAtEvent` | 38 | 29 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 43 | 36 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnUnmountEvent` | 4 | 1060 / 485 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/10` |
| `scneventsAttachPropToPerformer` | 1 | 569 / 274 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/5` |
| `scneventsAttachPropToWorld` | 4 | 36 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/12` |
| `scneventsEquipItemToPerformer` | 2 | 215 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 4 | 1060 / 481 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/7` |
| `scneventsSocket` | 47 | 36 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1158 / 621 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/7` |
| `scneventsVFXEvent` | 3 | 36 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- speech, skeletal_animation, gaze: 5
- speech, skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, gaze: 2
- speech, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `0ef1c5afdbfd81e9c3e27960a74be6c7d38e4ef3652057b3887720b4cabac1c9`. Binary SHA-256: `3ae03264248e7c0005af9ed668e2fc4a4a7fb6e4378c66fb529737d882701217`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_05_backalley.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_09_taken.scene`

80 graph nodes, 85 edges; 7 event-bearing sections, 80 events; 9 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: alt (actor 0, spawnSet); thompson (actor 1, spawnSet); boss (actor 2, community); cat (actor 3, spawner); thug_02 (actor 4, community); thug_van (actor 5, spawner); johnny (actor 6, findInContext).

Entries: `in` → 6; `fx_test` → 2080; `PLACEHOLDER` → 452.

Exits: `out` → 7.

End nodes: 7: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 29 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnChangeIdleAnimEvent` | 3 | 224 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/9` |
| `scnDialogLineEvent` | 6 | 29 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 4 | 224 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/12` |
| `scnPlaySkAnimEvent` | 17 | 29 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsCameraParamsEvent` | 5 | 29 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 18 | 29 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsVFXEvent` | 22 | 29 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 2
- speech, skeletal_animation, camera, audio, vfx, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- camera: 1

Raw SHA-256: `28716f23fade08b98b186ab8ed70a1421d88c17ecf63aeaa72e94714cf34fc1e`. Binary SHA-256: `267fedd8db33d2e3724b710253d216f0fe0fb22100d4d35bfc54ff690abfb2da`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_09_taken.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_10_ripper.scene`

69 graph nodes, 73 edges; 10 event-bearing sections, 154 events; 44 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: ripper (actor 0, community); thompson (actor 1, spawnSet); Johnny (actor 2, findInContext).

Entries: `in_intro` → 1.

Exits: `out_first_part` → 637.

End nodes: 637: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 16 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/12` |
| `scnChangeIdleAnimEvent` | 3 | 32 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 35 | 16 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scnGameplayTransitionEvent` | 1 | 881 / 512 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/17` |
| `scnIKEvent` | 2 | 881 / 493 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/1` |
| `scnLookAtEvent` | 31 | 16 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 25 | 16 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnUnmountEvent` | 1 | 881 / 511 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/16` |
| `scneventsAttachPropToNode` | 1 | 16 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/18` |
| `scneventsAttachPropToPerformer` | 4 | 16 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsAttachPropToWorld` | 2 | 16 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/13` |
| `scneventsCameraParamsEvent` | 4 | 16 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 1 | 881 / 507 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/13` |
| `scneventsSocket` | 34 | 16 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsVFXEvent` | 4 | 16 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 2
- speech: 2
- speech, skeletal_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal: 1
- camera, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `6ba6c0f97dc7fda2cd68c0f4e262aab7ee669fbfe929dd35f58ab3b48c22027c`. Binary SHA-256: `efe81178f3a27a21ea760718ad9913d1ea9120f1bc55ac1973b59f3fb32be8f5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_10_ripper.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_11_thompson.scene`

130 graph nodes, 194 edges; 32 event-bearing sections, 201 events; 55 screenplay lines, 18 screenplay options, 12 choice nodes.

Actors: thompson (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 11` → 1359; `in` → 289; `Start 13` → 1388.

Exits: `out` → 36.

End nodes: 36: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 454 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnChangeIdleAnimEvent` | 6 | 452 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnDialogLineEvent` | 50 | 452 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 746 / 292 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/12` |
| `scnIKEvent` | 4 | 746 / 281 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/2` |
| `scnLookAtEvent` | 19 | 452 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnPlaySkAnimEvent` | 50 | 454 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnUnmountEvent` | 2 | 746 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/11` |
| `scneventsAttachPropToNode` | 2 | 567 / 208 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/11` |
| `scneventsAttachPropToPerformer` | 4 | 567 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scneventsAttachPropToWorld` | 2 | 567 / 195 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 2 | 746 / 287 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/8` |
| `scneventsSocket` | 43 | 454 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsVFXEvent` | 4 | 532 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 6
- speech, skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, audio, socket_signal: 1

Raw SHA-256: `108c48ed85b950988d0d59b2398fb5f83ec41a0cda4be85fefe835f28b9db808`. Binary SHA-256: `ba080c581911d0e8ae36acf5586235317bd11d9ebc3bce7bb6e901ebd8c20008`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_11_thompson.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_13_atlantis_memory.scene`

170 graph nodes, 184 edges; 37 event-bearing sections, 365 events; 96 screenplay lines, 13 screenplay options, 10 choice nodes.

Actors: bouncer_entrance (actor 0, community); barman_f_01_dancefloor (actor 1, community); barman_m_01_bar (actor 2, community); barman_m_02_dancefloor (actor 3, community); Johnny (actor 4, spawnSet); crowd_m_01_bar (actor 5, community); crowd_m_02_bar (actor 6, community); crowd_m_03_dancefloor_chat (actor 7, community); crowd_f_01_dancefloor_chat (actor 8, community); staff_m_01_backroom_chat (actor 9, community); staff_m_02_backroom_chat (actor 10, community); mercenary_f_01_deal_chat (actor 11, community); mercenary_f_02_deal_chat (actor 12, community); mercenary_m_01_deal_chat (actor 13, community); mercenary_mb_02_drinking (actor 14, community); crowd_f_02_drugs (actor 15, community); mercenary_f_03_drug_deal (actor 16, community); crowd_f_02_vending_machine (actor 17, community); mercenary_m_03_drug_deal (actor 18, community); mercenary_m_04_drug_deal (actor 19, community); mercenary_m_07_argument (actor 20, community); mercenary_m_06_argument (actor 21, community); mercenary_f_04_argument (actor 22, community); mercenary_m_05_argument (actor 23, community); mercenary_f_05_argument (actor 24, community); Player (actor 25, findInContext).

Entries: `in ` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 100 / 420 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/1` |
| `scnChangeIdleAnimEvent` | 2 | 208 / 589 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/2` |
| `scnDialogLineEvent` | 82 | 15 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 4 | 23 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/39` |
| `scnIKEvent` | 8 | 23 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/25` |
| `scnLookAtEvent` | 58 | 15 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 123 | 15 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 4 | 23 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/38` |
| `scneventsAttachPropToPerformer` | 5 | 70 / 312 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/5` |
| `scneventsAttachPropToWorld` | 5 | 70 / 313 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/6` |
| `scneventsEquipItemToPerformer` | 3 | 23 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/45` |
| `scneventsSetAnimFeatureEvent` | 4 | 23 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/35` |
| `scneventsSocket` | 58 | 15 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 1 | 324 / 908 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/10` |
| `scneventsVFXEvent` | 6 | 56 / 269 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 8
- speech, skeletal_animation, gaze: 5
- skeletal_animation, socket_signal: 5
- socket_signal: 5
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation: 2
- gaze: 2
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, gaze, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `f546c117097ae5649b6095ac612b206b50008f2a758a560744ffcaa71a654929`. Binary SHA-256: `77082244fcea1de651624e9123ff27a7478dd314f4e5151a1c2fb3f18e6e3bfe`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_13_atlantis_memory.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_14_rogue.scene`

218 graph nodes, 248 edges; 32 event-bearing sections, 387 events; 66 screenplay lines, 18 screenplay options, 8 choice nodes.

Actors: Rogue (actor 0, spawnSet); Santiago (actor 1, spawnSet); arasaka_leader (actor 2, community); Thompson (actor 3, spawnSet); junkie (actor 4, community); arasaka_bar_table_01 (actor 5, community); arasaka_bar_table_02 (actor 6, community); porsche (actor 7, spawnSet); Player (actor 8, findInContext).

Entries: `in` → 1; `Start 12` → 9924; `Start 11` → 1437.

Exits: `out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 291 / 453 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/6` |
| `scnChangeIdleAnimEvent` | 40 | 26 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 63 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 2 | 417 / 577 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/30` |
| `scnIKEvent` | 4 | 417 / 566 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/20` |
| `scnLookAtEvent` | 84 | 59 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 70 | 109 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnUnmountEvent` | 2 | 417 / 576 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/29` |
| `scneventsAttachPropToPerformer` | 3 | 417 / 542 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/9` |
| `scneventsAttachPropToWorld` | 3 | 417 / 546 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/13` |
| `scneventsCameraParamsEvent` | 2 | 291 / 463 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 5 | 417 / 523 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/2` |
| `scneventsSocket` | 96 | 26 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 5 | 417 / 540 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 13
- skeletal_animation, socket_signal: 3
- speech: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, idle_animation, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- idle_animation, gaze, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1

Raw SHA-256: `9adec78c88ed3ba05fc7f26501831733280edc08ec90ee76cbdce0d38f4bd10c`. Binary SHA-256: `3796d71423272deced7bdcab2952ba3fa6280f9b511f367bc7427ce2a27e5a2a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_14_rogue.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_14a_escape.scene`

97 graph nodes, 100 edges; 14 event-bearing sections, 18 events; 15 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Rogue (actor 0, spawnSet); Santiago (actor 1, spawnSet); Johnny (actor 2, spawnSet); Thompson (actor 3, findInContext); q108_arasaka_helicopter (actor 4, spawnSet).

Entries: `in_thompson_hurries` → 198; `in_santiago_combat` → 709; `in_rogue_combat` → 730; `in` → 936.

Exits: `out_thompson_hurries` → 202; `out` → 966.

End nodes: 202: `<omitted>`; 966: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 2701 / 538 | `/Data/RootChunk/sceneGraph/Data/graph/96/Data/events/1` |
| `scnDialogLineEvent` | 14 | 40 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 2701 / 535 | `/Data/RootChunk/sceneGraph/Data/graph/96/Data/events/0` |
| `scnLookAtEvent` | 2 | 938 / 320 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- speech, gaze: 1
- idle_animation, gameplay_action: 1

Raw SHA-256: `adc236a99ee8522798490da19b00d62bb6c75847a399fd1b5a6fd12972012fea`. Binary SHA-256: `7c8650dd1de30543d176211b93484ead4834980b2a3fef790dda51619db93845`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_14a_escape.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_14b_lift.scene`

85 graph nodes, 103 edges; 12 event-bearing sections, 25 events; 8 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Rogue (actor 0, spawnSet); Santiago (actor 1, spawnSet); Johnny (actor 2, spawnSet); Thompson (actor 3, findInContext); q108_arasaka_lift_agent_wa (actor 4, community); q108_arasaka_lift_agent_ma (actor 5, community); Player (actor 6, findInContext).

Entries: `Start 8` → 1032; `in` → 44; `in_arasaka_elevator` → 1158.

Exits: `out` → 46; `out_thompson` → 888.

End nodes: 46: `<omitted>`; 888: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 8 | 45 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 13 | 1175 / 472 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 1025 / 301 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/0` |
| `scneventsSocket` | 2 | 1025 / 307 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- skeletal_animation, socket_signal: 2
- gaze: 2

Raw SHA-256: `4db294fc20d252316dd32c653cb4dfdae67eb959d3ffcde38abfdc705ff6b074`. Binary SHA-256: `1cd81f3c7a57505f10989034418f51dc3bb5fd60a4dac50db9c7c906d8648c6f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_14b_lift.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_15a_lift_parking.scene`

23 graph nodes, 26 edges; 2 event-bearing sections, 10 events; 5 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: santiago (actor 0, spawnSet); thompson (actor 1, spawnSet); rogue (actor 2, spawnSet); johnny (actor 3, findInContext).

Entries: `intro` → 1.

Exits: `out` → 266.

End nodes: 266: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 115 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnLookAtEvent` | 5 | 115 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 2

Raw SHA-256: `6f951a95496f7746782d8acaa1fb67295527b08f138bdd9bdbbfc48059aa03e8`. Binary SHA-256: `5405e8a5fd55bba650c723a5fcd52004276e6aa8e9fee9e88779bd66a2869ee2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_15a_lift_parking.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_15b_parking.scene`

101 graph nodes, 126 edges; 10 event-bearing sections, 25 events; 10 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: santiago (actor 0, spawnSet); thompson (actor 1, spawnSet); rogue (actor 2, spawnSet); turret (actor 3, findInWorld); porsche (actor 4, spawnSet); helicopter (actor 5, spawnSet); johnny (actor 6, findInContext).

Entries: `in_chat_on_the_way` → 371; `in` → 97.

Exits: `out_clean_up` → 441; `out` → 98.

End nodes: 98: `NonTerminating`; 441: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 377 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/4` |
| `scnChangeIdleAnimEvent` | 4 | 102 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 9 | 20 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 102 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 377 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 1 | 377 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scneventsSocket` | 3 | 102 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsVFXEvent` | 3 | 377 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, idle_animation, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal, animation_state: 1
- idle_animation, gameplay_action: 1

Raw SHA-256: `5c60357befd48ecb236f7caa0991e9836e877508737546ea28e4d543a026a164`. Binary SHA-256: `94b8848401e6a4792c91962004d8caaae588fbc671e2867270ad5f4f8ae82e93`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_15b_parking.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_15c_car_chase.scene`

308 graph nodes, 335 edges; 12 event-bearing sections, 33 events; 15 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: santiago (actor 0, spawnSet); thompson (actor 1, spawnSet); rogue (actor 2, spawnSet); arasaka_car_01_agent_02 (actor 3, community); arasaka_car_02_agent_02 (actor 4, community); arasaka_car_03_agent_02 (actor 5, community); arasaka_car_01_agent_driver (actor 6, community); arasaka_car_02_agent_driver (actor 7, community); arasaka_car_03_agent_driver (actor 8, community); rogue_bike (actor 9, spawnSet); santiago_bike (actor 10, spawnSet); johnny_vehicle (actor 11, spawnSet); arasaka_car_chase_01 (actor 12, spawner); arasaka_car_chase_02 (actor 13, spawner); arasaka_car_chase_03 (actor 14, spawner); arasaka_helicopter (actor 15, spawnSet); johnny (actor 16, findInContext).

Entries: `q115_atrium_reuse_line_in` → 471; `OLD` → 2957; `in` → 226.

Exits: `out_to_hidden_alley` → 452; `q115_atrium_reuse_line_out` → 479.

End nodes: 452: `<omitted>`; 479: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 2528 / 981 | `/Data/RootChunk/sceneGraph/Data/graph/165/Data/events/5` |
| `scnChangeIdleAnimEvent` | 1 | 2703 / 1273 | `/Data/RootChunk/sceneGraph/Data/graph/215/Data/events/1` |
| `scnDialogLineEvent` | 14 | 12 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnGameplayActionEvent` | 1 | 2703 / 1270 | `/Data/RootChunk/sceneGraph/Data/graph/215/Data/events/0` |
| `scnIKEvent` | 2 | 2528 / 982 | `/Data/RootChunk/sceneGraph/Data/graph/165/Data/events/6` |
| `scnLookAtEvent` | 7 | 12 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 2528 / 967 | `/Data/RootChunk/sceneGraph/Data/graph/165/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 2528 / 972 | `/Data/RootChunk/sceneGraph/Data/graph/165/Data/events/2` |
| `scneventsSocket` | 4 | 12 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, gaze, socket_signal: 2
- speech, gaze: 1
- skeletal_animation, gaze, ik, audio, socket_signal, animation_state: 1
- idle_animation, gameplay_action: 1

Raw SHA-256: `c11b94bc787f60c2b8d3d9b6f24ea4d5632a1f665d29e6a253e0f9c82bac693e`. Binary SHA-256: `0900424cdd3b1112b7b5775efbf785fc63143f1e780ab1d0964f18dfee97bec1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_15c_car_chase.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_15d_alley.scene`

25 graph nodes, 29 edges; 4 event-bearing sections, 54 events; 9 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: santiago (actor 0, spawnSet); thompson (actor 1, spawnSet); rogue (actor 2, spawnSet); porsche (actor 3, spawnSet); rogue_bike (actor 4, spawnSet); santiago_bike (actor 5, spawnSet); johnny (actor 6, findInContext).

Entries: `in` → 27; `Start 6` → 246.

Exits: `out` → 38.

End nodes: 38: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 29 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnChangeIdleAnimEvent` | 4 | 29 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 9 | 29 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scnLookAtEvent` | 9 | 29 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scnPlaySkAnimEvent` | 13 | 29 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 35 / 98 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsAttachPropToWorld` | 1 | 35 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scneventsCameraParamsEvent` | 2 | 29 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 4 | 29 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsSocket` | 6 | 29 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |
| `scneventsVFXEvent` | 3 | 29 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, camera, props_equipment, vfx, socket_signal, animation_state: 1
- speech: 1
- vfx: 1

Raw SHA-256: `c9241a3c7dfd3bb191d3245f46de35d261ef2a5d2e43e46a542f7deaea345d28`. Binary SHA-256: `f05ceb826b38b3d105154623053531cc8ff949a4b4bc3ec3c68486242b0b0b4f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_15d_alley.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_18a_lift.scene`

97 graph nodes, 119 edges; 12 event-bearing sections, 100 events; 20 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: rogue (actor 0, spawnSet); santiago (actor 1, spawnSet); thompson (actor 2, spawnSet); dead_arasaka (actor 3, spawnDespawn); Anchor (actor 4, findInContext); Player (actor 5, findInContext).

Entries: `in` → 6.

Exits: `out_left_elevator` → 7; `Kill Signal` → 1151.

End nodes: 7: `NonTerminating`; 1151: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 76 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/6` |
| `scnChangeIdleAnimEvent` | 6 | 19 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 14 | 39 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnLookAtEvent` | 26 | 19 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 21 | 19 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsAttachPropToNode` | 1 | 76 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/10` |
| `scneventsAttachPropToPerformer` | 2 | 76 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/8` |
| `scneventsCameraParamsEvent` | 2 | 76 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scneventsSocket` | 24 | 19 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsVFXEvent` | 2 | 640 / 300 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 2
- speech: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `5103be9be91d501f58e7e27543f9b5574a51ccf048e215a58bd6f0e22524cfe9`. Binary SHA-256: `2c41bad0cb4059fa4d6a5c09ae470ffc0b5a7c326531418a293c14ffbde42632`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_18a_lift.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_18b_combat.scene`

45 graph nodes, 40 edges; 11 event-bearing sections, 27 events; 21 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: rogue (actor 0, spawnSet); santiago (actor 1, spawnSet); thompson (actor 2, spawnSet); Johnny (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `in_doors_shut` → 198; `in_locked` → 22; `in_access_server_a` → 32; `in_santiago_reinforcements` → 219; `in_rogue_turret` → 221; `in_access_server_b` → 37; `in_santiago_turret` → 223; `in_access_server_c` → 42.

Exits: `out_doors_shut` → 204; `out_locked` → 23; `out_access_server_a` → 33; `out_access_server_b` → 38; `out_access_server_c` → 43.

End nodes: 23: `NonTerminating`; 33: `NonTerminating`; 38: `NonTerminating`; 43: `NonTerminating`; 204: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 21 | 24 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 6 | 34 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, gaze: 3

Raw SHA-256: `aabdef0bc0d594287ddc80c8465997e07b58a0cbcaddc6cd6d849d987dd99cb6`. Binary SHA-256: `a28a4b164e271bcebc1e246f7f11c97383a09b825ac1380167a06791e4829714`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_18b_combat.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_18c_mainframe_access.scene`

99 graph nodes, 109 edges; 9 event-bearing sections, 37 events; 14 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: rogue (actor 0, spawnSet); santiago (actor 1, spawnSet); thompson (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `in_get_ready` → 665; `in_go_in` → 667; `in` → 47.

Exits: `out` → 129.

End nodes: 129: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 135 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/8` |
| `scnDialogLineEvent` | 13 | 49 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 8 | 122 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 5 | 135 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 135 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 135 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |
| `scneventsSocket` | 7 | 135 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, socket_signal: 1

Raw SHA-256: `05577a78da63ad27f2f185930119b447b513a8b85b9bc1deb516f14f61b7af11`. Binary SHA-256: `8157e6deb08d3a02cb9f24cbc807ceefad41692423b5581e5ff567e2296175f7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_18c_mainframe_access.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_19_soulkiller.scene`

103 graph nodes, 116 edges; 17 event-bearing sections, 121 events; 28 screenplay lines, 5 screenplay options, 4 choice nodes.

Actors: Alt (actor 0, spawnSet); Thompson (actor 1, spawnSet); toshiro (actor 2, community); Rogue (actor 3, spawnSet); Johnny (actor 4, spawnSet); Santiago (actor 5, spawnSet); Player (actor 6, findInContext).

Entries: `Start 11` → 9795; `in_combat_chat` → 366; `Start1` → 9801; `in_alt_dead` → 25; `in_rogue_before_combat` → 796.

Exits: `out_combat_chat` → 376; `out_alt_dead` → 26.

End nodes: 26: `<omitted>`; 376: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 47 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnChangeIdleAnimEvent` | 10 | 121 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnDialogLineEvent` | 24 | 47 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 22 | 121 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnPlaySkAnimEvent` | 22 | 47 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 125 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/8` |
| `scneventsAttachPropToWorld` | 1 | 133 / 156 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/13` |
| `scneventsCameraParamsEvent` | 3 | 133 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/6` |
| `scneventsSocket` | 26 | 47 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 6 | 125 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- gaze: 2
- speech, skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `bd0fab8ff7af8fb88a9fd68fdd88cad40762f2a40f91f7d6b8436626b24bafcc`. Binary SHA-256: `876df15174f11b5516509ef7131b32506536de09d599524dcc3b999fddcac96b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_19_soulkiller.scene" --events
```

## `base\quest\main_quests\part1\q108\scenes\q108_21_finale.scene`

140 graph nodes, 165 edges; 34 event-bearing sections, 195 events; 87 screenplay lines, 23 screenplay options, 9 choice nodes.

Actors: johnny (actor 0, spawnSet); thompson (actor 1, spawnSet); alt (actor 2, spawnSet); rogue (actor 3, spawnSet); v (actor 4, findInContext); johnny_replacer (actor 5, findInContext).

Entries: `in` → 1.

Exits: `out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1434 / 999 | `/Data/RootChunk/sceneGraph/Data/graph/138/Data/events/0` |
| `scnDialogLineEvent` | 86 | 177 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnLookAtEvent` | 31 | 199 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/7` |
| `scnPlaySkAnimEvent` | 38 | 177 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsSocket` | 35 | 177 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsVFXEvent` | 4 | 177 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, skeletal_animation, socket_signal: 5
- speech, gaze: 5
- speech, skeletal_animation: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, vfx, socket_signal: 1
- socket_signal: 1
- audio, vfx: 1

Raw SHA-256: `da351731fd6e9f42c205c961acfc7551f4c0046c1c6b67e79213dea3a8f3b157`. Binary SHA-256: `ddddab444a6d7805a3adaa94595b448654cee4c495a9c27562c47a2e2c201d84`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q108\scenes\q108_21_finale.scene" --events
```

