# Run This Town: scene presentation

Journal identity: `ep1/quests/minor_quest/mq304_succession`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-mq304_succession.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\minor_quests\mq304\scenes\mq304_00_city_scenes.scene`

25 graph nodes, 23 edges; 2 event-bearing sections, 10 events; 2 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: mq304_sts_test (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `lean_in` → 6.

Exits: `End 0` → 2; `lean_out` → 7; `start_cleaning_up` → 61.

End nodes: 2: `<omitted>`; 7: `<omitted>`; 61: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnGameplayTransitionEvent` | 1 | 31 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnIKEvent` | 2 | 31 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnPlaySkAnimEvent` | 2 | 12 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnUnmountEvent` | 1 | 31 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 1 | 31 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/5` |
| `scneventsSocket` | 3 | 12 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `0cb30539aa6437329c72785190bb7ec6fca7aa283cc1e2f89125c1573621b49c`. Binary SHA-256: `27cf3ed5f9c15b403d497f7de9348069cb1c9e070b7b85a90c8d315962b6b21b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq304\scenes\mq304_00_city_scenes.scene" --events
```

## `ep1\quest\minor_quests\mq304\scenes\mq304_01_hook.scene`

32 graph nodes, 37 edges; 7 event-bearing sections, 21 events; 12 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: mr_hands (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 920.

End nodes: 2: `<omitted>`; 920: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 12 | 869 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 876 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scneventsSocket` | 5 | 869 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 3
- speech, socket_signal: 2
- speech: 2

Raw SHA-256: `152362e2261a607fb7ae5e9748f47f6dbc4e662eeb9d08f3cd12113ce90baa63`. Binary SHA-256: `c79bd9a729ad88e99ccd7dcaaa3ac96874493acae16985803cd9fee873fb89df`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq304\scenes\mq304_01_hook.scene" --events
```

## `ep1\quest\minor_quests\mq304\scenes\mq304_02_hands_briefing.scene`

440 graph nodes, 561 edges; 70 event-bearing sections, 492 events; 119 screenplay lines, 33 screenplay options, 21 choice nodes.

Actors: Hands (actor 0, spawnSet); npc1 (actor 1, community); npc2 (actor 2, community); assassin_female_tpp (actor 3, spawnDespawn); assassin_male_tpp (actor 4, spawnDespawn); Player (actor 5, findInContext); assassin_female (actor 6, findInContext); assassin_male (actor 7, findInContext).

Entries: `Start 0` → 1; `Start_as_nicola` → 885; `Start_back_player` → 887; `Start_npcs` → 538.

Exits: `End 0` → 2; `End_change_to_nicola` → 883; `End_change_to_player` → 886; `End_npcs` → 547; `end_quest_denied` → 1052; `End 4` → 2788.

End nodes: 2: `NonTerminating`; 547: `<omitted>`; 883: `NonTerminating`; 886: `NonTerminating`; 1052: `<omitted>`; 2788: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 247 / 170 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/2` |
| `scnChangeIdleAnimEvent` | 33 | 10 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 82 | 10 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 6 | 123 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/8` |
| `scnIKEvent` | 12 | 123 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |
| `scnLookAtEvent` | 94 | 10 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 125 | 10 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnUnmountEvent` | 6 | 123 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/7` |
| `scneventsAttachPropToPerformer` | 3 | 600 / 566 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/2` |
| `scneventsAttachPropToWorld` | 3 | 600 / 571 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/7` |
| `scneventsCameraParamsEvent` | 9 | 231 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/5` |
| `scneventsEquipItemToPerformer` | 1 | 1135 / 1012 | `/Data/RootChunk/sceneGraph/Data/graph/120/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 6 | 123 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |
| `scneventsSocket` | 85 | 10 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsUnequipItemFromPerformer` | 1 | 1135 / 1013 | `/Data/RootChunk/sceneGraph/Data/graph/120/Data/events/6` |
| `scneventsVFXEvent` | 16 | 10 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- skeletal_animation, idle_animation: 4
- gaze: 4
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, camera, socket_signal: 2
- gaze, vfx: 2
- skeletal_animation, vfx: 2
- gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, props_equipment, vfx: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech: 1
- speech, gaze: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `23c396551ae9cc8658ed679ce09a41f4ce00e24b066c3212a43c5b893fbbe931`. Binary SHA-256: `c3a54f7a81e3d522841ec415037343faa09c8a1f3ee6ecb4f90dfbf3fd4a5931`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq304\scenes\mq304_02_hands_briefing.scene" --events
```

## `ep1\quest\minor_quests\mq304\scenes\mq304_03_jago.scene`

388 graph nodes, 484 edges; 103 event-bearing sections, 732 events; 166 screenplay lines, 18 screenplay options, 9 choice nodes.

Actors: johnny (actor 0, spawnDespawn); jago (actor 1, spawnSet); jago_bdgrd1 (actor 2, community); jago_bdgrd2 (actor 3, community); jago_car (actor 4, community); Player (actor 5, findInContext); assassin_female (actor 6, findInContext); assassin_male (actor 7, findInContext).

Entries: `Start 0` → 1.

Exits: `End_peace` → 2; `End_johnny` → 105.

End nodes: 2: `NonTerminating`; 105: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 269 / 457 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/5` |
| `scnChangeIdleAnimEvent` | 12 | 370 / 518 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/1` |
| `scnDialogLineEvent` | 103 | 13 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 14 | 55 / 290 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/21` |
| `scnIKEvent` | 28 | 55 / 281 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/13` |
| `scnLookAtEvent` | 149 | 15 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 203 | 15 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnUnmountEvent` | 14 | 55 / 289 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/20` |
| `scneventsAttachPropToNode` | 2 | 1081 / 1685 | `/Data/RootChunk/sceneGraph/Data/graph/141/Data/events/14` |
| `scneventsAttachPropToPerformer` | 2 | 1081 / 1677 | `/Data/RootChunk/sceneGraph/Data/graph/141/Data/events/6` |
| `scneventsCameraParamsEvent` | 18 | 37 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/8` |
| `scneventsEquipItemToPerformer` | 1 | 512 / 917 | `/Data/RootChunk/sceneGraph/Data/graph/74/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 22 | 55 / 285 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/17` |
| `scneventsSocket` | 149 | 15 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scneventsVFXEvent` | 4 | 269 / 456 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 23
- speech, skeletal_animation, gaze, socket_signal: 18
- speech: 9
- speech, skeletal_animation, gaze: 6
- speech, skeletal_animation, socket_signal: 5
- skeletal_animation, socket_signal, animation_state: 5
- skeletal_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 2
- skeletal_animation: 2
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, camera, socket_signal: 1
- speech, skeletal_animation: 1
- speech, gaze: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- idle_animation: 1
- camera: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `e7f3ac5215ce77d8ddc77d536a8da05a38537b88ee75e453c76d8a20fe3766c3`. Binary SHA-256: `4d495ebf5efc4db564b087c87ed99f5358b9b2bfca582ba49f877cb5f4c771d6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq304\scenes\mq304_03_jago.scene" --events
```

## `ep1\quest\minor_quests\mq304\scenes\mq304_03a_vdb_meeting.scene`

192 graph nodes, 231 edges; 42 event-bearing sections, 219 events; 57 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: vdb1_m (actor 0, community); vdb2_m (actor 1, community); vdb3_m (actor 2, community); vdb4_f (actor 3, community); vdb5_m (actor 4, community); johnny (actor 5, spawnDespawn); vdb6_m (actor 6, community); vdbs_car_01 (actor 7, community); Player (actor 8, findInContext); assassin_female (actor 9, findInContext); assassin_male (actor 10, findInContext).

Entries: `Start_vdb_meet` → 1; `Start_forced_change_nicola` → 355; `Start_warn_player` → 371; `Start_change_to_nicola` → 122; `Start_change_to_player` → 127.

Exits: `End_peacefully` → 2; `End_combat` → 17; `End_forced_change_nicola` → 363; `End_warn_player` → 373; `End_change_to_nicola` → 123; `End_change_to_player` → 128.

End nodes: 2: `<omitted>`; 17: `<omitted>`; 123: `<omitted>`; 128: `<omitted>`; 363: `<omitted>`; 373: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 216 / 380 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/5` |
| `scnChangeIdleAnimEvent` | 9 | 10 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnDialogLineEvent` | 31 | 6 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |
| `scnGameplayTransitionEvent` | 5 | 6 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/19` |
| `scnIKEvent` | 10 | 6 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtEvent` | 65 | 6 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/20` |
| `scnOverridePhantomParamsEvent` | 1 | 822 / 1052 | `/Data/RootChunk/sceneGraph/Data/graph/153/Data/events/2` |
| `scnPlaySkAnimEvent` | 33 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 5 | 6 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scneventsEquipItemToPerformer` | 2 | 223 / 392 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 5 | 6 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scneventsSocket` | 50 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 1 | 216 / 379 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 12
- speech: 8
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, socket_signal: 2
- socket_signal: 2
- gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, animation_state: 1

Raw SHA-256: `6f8a36c23706e47b6bb82d5fd67218c58f92abf2992ce6a6b6f7de01a2116d59`. Binary SHA-256: `09a8c4c2dfd4f252b78732fd68986bf8f54e226c382266a6787790ac50f6eb6a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq304\scenes\mq304_03a_vdb_meeting.scene" --events
```

## `ep1\quest\minor_quests\mq304\scenes\mq304_04_report_holocall.scene`

21 graph nodes, 25 edges; 7 event-bearing sections, 35 events; 29 screenplay lines, 4 screenplay options, 1 choice nodes.

Actors: mr_hands (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 22 | 37 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnPlaySkAnimEvent` | 12 | 37 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scneventsSocket` | 1 | 37 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 5
- speech, skeletal_animation, socket_signal: 1
- speech: 1

Raw SHA-256: `b0c2ba511f474f1cd7415db5f013078c6a2041018d9d3faa983ada55e1d4c254`. Binary SHA-256: `fa01751b469ee300808c85c53adf28ef12e0e60f6c8b207991c893437eb19f39`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq304\scenes\mq304_04_report_holocall.scene" --events
```

## `ep1\quest\minor_quests\mq304\scenes\mq304_05_bennett.scene`

424 graph nodes, 534 edges; 89 event-bearing sections, 518 events; 135 screenplay lines, 17 screenplay options, 13 choice nodes.

Actors: bennett (actor 0, spawnSet); johnny (actor 1, spawnDespawn); bodyguard (actor 2, community); bennett_car (actor 3, community); Player (actor 4, findInContext); assassin_female (actor 5, findInContext); assassin_male (actor 6, findInContext).

Entries: `Start_johnny` → 1; `Start_aft_combat` → 64; `Start` → 128; `Start 0` → 2693; `change_back_in` → 1070; `Start 5` → 1564; `after_change` → 2403; `wait_bennett_in` → 743.

Exits: `End_combat` → 2; `End_peace` → 61; `End_aft_combat` → 87; `End_johnny` → 126; `End 0` → 2695; `change_back_out` → 1072; `End_fail` → 278; `End 6` → 1566; `End 8` → 2413; `wait_bennett_out` → 746.

End nodes: 2: `NonTerminating`; 61: `NonTerminating`; 87: `NonTerminating`; 126: `<omitted>`; 278: `NonTerminating`; 746: `<omitted>`; 1072: `NonTerminating`; 1566: `NonTerminating`; 2413: `<omitted>`; 2695: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 18 | 41 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/5` |
| `scnChangeIdleAnimEvent` | 23 | 37 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnDialogLineEvent` | 65 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayActionEvent` | 3 | 41 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scnGameplayTransitionEvent` | 14 | 73 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/7` |
| `scnIKEvent` | 28 | 73 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/4` |
| `scnLookAtEvent` | 59 | 10 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 125 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 14 | 73 / 169 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/11` |
| `scneventsAttachPropToPerformer` | 1 | 49 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/5` |
| `scneventsCameraParamsEvent` | 11 | 41 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 23 | 41 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsSocket` | 118 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsVFXEvent` | 16 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 11
- gaze: 9
- speech: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, audio, vfx, socket_signal: 4
- skeletal_animation: 4
- speech, gaze: 3
- skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, socket_signal: 3
- speech, skeletal_animation, idle_animation, camera, audio, socket_signal, animation_state, gameplay_action: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, audio, socket_signal: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, camera, vfx, socket_signal, animation_state: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, vfx, socket_signal: 2
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, props_equipment, audio, socket_signal, gameplay_action: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, vfx: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `00fe095e3a3fd347cdfe393ed6a8323c8c5b1412dc1ef499e144ba5e0f4babc8`. Binary SHA-256: `78e4bff866d99dc4c704a23bb1e7fd0381f47680c213a842f24b3321fbb37ecb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq304\scenes\mq304_05_bennett.scene" --events
```

## `ep1\quest\minor_quests\mq304\scenes\mq304_06_kurts_wake.scene`

1161 graph nodes, 1368 edges; 302 event-bearing sections, 2339 events; 394 screenplay lines, 28 screenplay options, 13 choice nodes.

Actors: jago (actor 0, spawnSet); bennett (actor 1, spawnSet); johnny (actor 2, spawnDespawn); jago_man1 (actor 3, community); jago_man2 (actor 4, community); bennett_bodyguard_1_gate (actor 5, community); bennett_bodyguard_2 (actor 6, community); bennett_bodyguard_3 (actor 7, community); kurt_corpse (actor 8, spawnDespawn); wake_visitor_001 (actor 9, community); wake_visitor_002 (actor 10, community); wake_visitor_003 (actor 11, community); wake_visitor_004 (actor 12, community); wake_visitor_005 (actor 13, community); wake_guard_001 (actor 14, community); wake_guard_002 (actor 15, community); wake_guard_003 (actor 16, community); wake_guard_004 (actor 17, community); wake_jago_guard_001 (actor 18, community); wake_jago_guard_002 (actor 19, community); wake_jago_guard_003 (actor 20, community); Dodger (actor 21, community); babs (actor 22, spawnSet); paco (actor 23, spawnSet); ross_ulmer (actor 24, community); bennett_guard_001 (actor 25, community); bennett_guard_002 (actor 26, community); bennett_guard_003 (actor 27, community); wake_visitor_006 (actor 28, community); bennett_guard_004 (actor 29, community); jago_guard_004 (actor 30, community); wake_scav_001 (actor 31, community); wake_scav_002 (actor 32, community); wake_visitor_007 (actor 33, community); wake_visitor_008 (actor 34, community); wake_visitor_009 (actor 35, community); wake_visitor_010 (actor 36, community); wake_bennett_guard_007 (actor 37, community); wake_bennett_guard_005 (actor 38, community); wake_bennett_guard_006 (actor 39, community); wake_bennett_guard_009 (actor 40, community); wake_bennett_guard_010 (actor 41, community); wake_bennett_guard_011 (actor 42, community); wake_jago_guard_007 (actor 43, community); wake_jago_guard_008 (actor 44, community); kyle_araujo (actor 45, community); wake_bennett_guard_008 (actor 46, community); wake_jago_guard_009 (actor 47, community); wake_bennett_guard_012 (actor 48, community); wake_jago_guard_005 (actor 49, community); wake_jago_guard_006 (actor 50, community); wake_jago_guard_004 (actor 51, community); wake_vdb_001 (actor 52, community); wake_vdb_002 (actor 53, community); wake_bennett_guard_013 (actor 54, community); Player (actor 55, findInContext); assassin_female (actor 56, findInContext); assassin_male (actor 57, findInContext).

Entries: `Start 0` → 1; `Start_leave_elev` → 163; `Elevator to wake` → 2429.

Exits: `End 0` → 2; `End_leave_elev` → 185.

End nodes: 2: `NonTerminating`; 185: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 19 | 1373 / 1894 | `/Data/RootChunk/sceneGraph/Data/graph/142/Data/events/2` |
| `scnChangeIdleAnimEvent` | 14 | 112 / 498 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/1` |
| `scnDialogLineEvent` | 157 | 19 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 60 | 95 / 362 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/8` |
| `scnIKEvent` | 120 | 95 / 356 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/4` |
| `scnLookAtEvent` | 558 | 25 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 528 | 23 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 1184 / 1727 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/11` |
| `scnUnmountEvent` | 60 | 95 / 367 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/12` |
| `scneventsAttachPropToNode` | 2 | 3873 / 4753 | `/Data/RootChunk/sceneGraph/Data/graph/488/Data/events/4` |
| `scneventsAttachPropToPerformer` | 19 | 74 / 223 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/2` |
| `scneventsAttachPropToWorld` | 6 | 74 / 226 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/5` |
| `scneventsCameraParamsEvent` | 16 | 95 / 350 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/2` |
| `scneventsEquipItemToPerformer` | 21 | 108 / 423 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 60 | 95 / 363 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/9` |
| `scneventsSocket` | 633 | 19 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 8 | 108 / 451 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/16` |
| `scneventsVFXEvent` | 56 | 99 / 391 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 44
- skeletal_animation, socket_signal: 43
- skeletal_animation, gaze, socket_signal: 27
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 21
- speech, skeletal_animation, gaze, socket_signal: 20
- socket_signal: 20
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 12
- speech, skeletal_animation, gaze: 10
- speech: 9
- skeletal_animation, gaze: 7
- speech, skeletal_animation, socket_signal: 6
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 6
- gaze, socket_signal: 6
- speech, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, gaze, vfx, socket_signal: 4
- speech, skeletal_animation, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- props_equipment, socket_signal: 4
- speech, skeletal_animation, gaze, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, gaze: 3
- skeletal_animation, gaze, vfx, socket_signal: 3
- skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, idle_animation, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation: 2
- skeletal_animation, props_equipment, audio: 2
- skeletal_animation, gaze, props_equipment, socket_signal: 2
- vfx: 2
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1

Raw SHA-256: `0862aa347b92adcfdc53061f059a001725a159cfadfd630e7fa4aa9556a54a1b`. Binary SHA-256: `eda2e4719e6e3235e7fb443212e741ce0ab820e35ec41cece3d3ff31299d4f04`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq304\scenes\mq304_06_kurts_wake.scene" --events
```

## `ep1\quest\minor_quests\mq304\scenes\mq304_06a_meet_bodyguards.scene`

104 graph nodes, 110 edges; 18 event-bearing sections, 89 events; 18 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: nicola_bdgrd1 (actor 0, community); nicola_bdgrd2 (actor 1, community); johnny (actor 2, spawnDespawn); Player (actor 3, findInContext); assassin_female (actor 4, findInContext); assassin_male (actor 5, findInContext).

Entries: `Start 0` → 1; `change_back_in` → 221; `Start_nicola_to_elev` → 139; `Start 2` → 164.

Exits: `End 0` → 2; `End_nicola_to_elev` → 144; `change_back_out` → 239; `End 2` → 163.

End nodes: 2: `<omitted>`; 144: `NonTerminating`; 163: `<omitted>`; 239: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 321 / 207 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/4` |
| `scnChangeIdleAnimEvent` | 2 | 280 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/1` |
| `scnDialogLineEvent` | 5 | 280 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/3` |
| `scnGameplayTransitionEvent` | 6 | 280 / 139 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/14` |
| `scnIKEvent` | 12 | 280 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/8` |
| `scnLookAtEvent` | 6 | 295 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scnPlaySkAnimEvent` | 15 | 280 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/0` |
| `scnUnmountEvent` | 6 | 280 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 6 | 280 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/10` |
| `scneventsSocket` | 25 | 280 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scneventsVFXEvent` | 3 | 321 / 206 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, audio, vfx, socket_signal: 2
- gaze: 2
- skeletal_animation: 2
- gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `8c325b88631f4c029c18b2e31da519cc43064f7bb436d5d86619a4927c328976`. Binary SHA-256: `68f7e6a9de9f1ee07090d16f2be443be32f4795ae043b5ae7b7454850278f474`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq304\scenes\mq304_06a_meet_bodyguards.scene" --events
```

## `ep1\quest\minor_quests\mq304\scenes\mq304_06b_lobby.scene`

174 graph nodes, 176 edges; 49 event-bearing sections, 206 events; 53 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: doorman_01 (actor 0, community); doorman_02 (actor 1, community); guard_01 (actor 2, community); guard_02 (actor 3, community); guest_01 (actor 4, community); guard_03 (actor 5, community); guard_04 (actor 6, community); guest_02 (actor 7, community); guest_03 (actor 8, community); guest_04 (actor 9, community); guard_05 (actor 10, community); guard_06 (actor 11, community); guard_07 (actor 12, community); guard_08 (actor 13, community); guard_09 (actor 14, community); guard_10 (actor 15, community); guard_11 (actor 16, community); guard_12 (actor 17, community); assassin_female (actor 18, spawnSet); assassin_male (actor 19, spawnSet); guard_13 (actor 20, community); Player (actor 21, findInContext).

Entries: `doorman moves away` → 1; `guard_poke` → 311; `Start 1` → 56; `elevator guard` → 191; `guards move away` → 218; `elevator test` → 231; `way back start` → 371.

Exits: `End 2` → 281; `way back end` → 503.

End nodes: 281: `<omitted>`; 503: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 150 / 217 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/6` |
| `scnDialogLineEvent` | 6 | 79 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |
| `scnGameplayTransitionEvent` | 3 | 150 / 252 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/28` |
| `scnIKEvent` | 6 | 150 / 233 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/16` |
| `scnLookAtEvent` | 85 | 11 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 35 | 11 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 3 | 150 / 253 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/29` |
| `scneventsEquipItemToPerformer` | 5 | 24 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 3 | 150 / 249 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/26` |
| `scneventsSocket` | 55 | 11 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 1 | 79 / 154 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/9` |
| `scneventsVFXEvent` | 2 | 887 / 1020 | `/Data/RootChunk/sceneGraph/Data/graph/144/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 28
- skeletal_animation, gaze, socket_signal: 7
- skeletal_animation, socket_signal: 3
- gaze, props_equipment, socket_signal: 2
- skeletal_animation: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, gaze, vfx, socket_signal: 1

Raw SHA-256: `8b9d40cb1608e24ae983a7e7cd652a5242b0604b3236d0356d87b5e8d2346cf6`. Binary SHA-256: `048d4626053d77037c59c1b582c76c63c67d5286930fb42582c7f27bf586b1fc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq304\scenes\mq304_06b_lobby.scene" --events
```

## `ep1\quest\minor_quests\mq304\scenes\mq304_07_end_holocall.scene`

42 graph nodes, 50 edges; 15 event-bearing sections, 33 events; 17 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: mrhands (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 17 | 37 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnPlaySkAnimEvent` | 11 | 45 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scneventsSocket` | 5 | 37 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation: 5
- speech, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2

Raw SHA-256: `f0ab0125f164aece4ea537a43014dca3a4dd41dcab3f9a15c99010fc9863bd71`. Binary SHA-256: `50afa1cb9fe4912d6b7a42a6141af3d87af68f2718f7550b589df7c1b6a36370`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq304\scenes\mq304_07_end_holocall.scene" --events
```

