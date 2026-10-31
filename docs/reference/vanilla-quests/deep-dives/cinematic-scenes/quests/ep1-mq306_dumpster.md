# No Easy Way Out: scene presentation

Journal identity: `ep1/quests/minor_quest/mq306_dumpster`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-mq306_dumpster.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\minor_quests\mq306\scenes\mq306_01_intro.scene`

350 graph nodes, 432 edges; 69 event-bearing sections, 517 events; 114 screenplay lines, 23 screenplay options, 10 choice nodes.

Actors: Aaron (actor 0, community); Boxer (actor 1, community); Referee (actor 2, community); spectator_7 (actor 3, community); spectator_1 (actor 4, community); spectator_2 (actor 5, community); spectator_3 (actor 6, community); spectator_4 (actor 7, community); spectator_5 (actor 8, community); spectator_6 (actor 9, community); spectator_8 (actor 10, community); spectator_9 (actor 11, community); spectator_10 (actor 12, community); spectator_female_1 (actor 13, community); spectator_female_2 (actor 14, community); child_01 (actor 15, community); child_02 (actor 16, community); Johnny (actor 17, spawnDespawn); Player (actor 18, findInContext).

Entries: `Start 5` → 1561; `Start 0` → 1; `Start 4` → 1506; `back_to_scene` → 1839.

Exits: `End 0` → 2; `End1` → 1282; `rejected_out` → 362; `rejected_loop_out` → 364.

End nodes: 2: `NonTerminating`; 362: `NonTerminating`; 364: `<omitted>`; 1282: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 36 | 6 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnChangeIdleAnimEvent` | 20 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 68 | 6 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/39` |
| `scnGameplayTransitionEvent` | 5 | 6 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/60` |
| `scnIKEvent` | 10 | 6 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/48` |
| `scnLookAtAdvancedEvent` | 15 | 16 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/7` |
| `scnLookAtEvent` | 68 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 161 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 1 | 633 / 758 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/13` |
| `scnUnmountEvent` | 5 | 6 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/61` |
| `scneventsEquipItemToPerformer` | 13 | 633 / 748 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 5 | 6 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/58` |
| `scneventsSocket` | 95 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 3 | 1143 / 1317 | `/Data/RootChunk/sceneGraph/Data/graph/127/Data/events/2` |
| `scneventsVFXEvent` | 12 | 6 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/55` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 8
- skeletal_animation, socket_signal: 7
- speech, skeletal_animation, gaze, socket_signal: 6
- skeletal_animation, props_equipment, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- skeletal_animation, audio: 5
- speech, skeletal_animation, socket_signal: 4
- gaze: 4
- speech, skeletal_animation: 3
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech: 2
- skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- props_equipment, socket_signal: 1
- socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- vfx, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `c1f235bec74706af823f34e29d08e301ba5efede79b8020a164ca177fde8cc09`. Binary SHA-256: `6374a4d10c5fe828c1c6d34e93d61c12a32e36b913d448dce37fba1fa759400a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq306\scenes\mq306_01_intro.scene" --events
```

## `ep1\quest\minor_quests\mq306\scenes\mq306_02_tech_expo_exploration.scene`

166 graph nodes, 198 edges; 34 event-bearing sections, 159 events; 54 screenplay lines, 7 screenplay options, 5 choice nodes.

Actors: Aaron (actor 0, community); Guard_01 (actor 1, community); Guard_02 (actor 2, community); Guard_03 (actor 3, community); Guard_04 (actor 4, community); Guard_05 (actor 5, community); Player (actor 6, findInContext).

Entries: `Start 0` → 1; `location_chat_start` → 886; `crate_chat_start` → 894; `warning_start` → 918; `Start 1` → 439; `scav_outlook_preview` → 458; `exploration_00_chat_start` → 945; `exploration_01_chat_start` → 947; `exploration_02_chat_start` → 949; `exploration_03_chat_start` → 951.

Exits: `checking_combat_out` → 828; `exploration` → 226; `spawn_out` → 883; `location_chat_end` → 888; `crate_chat_end` → 899; `warning_end` → 921; `exploration_00_chat_end` → 956; `exploration_01_chat_end` → 958; `exploration_02_chat_end` → 960; `exploration_03_chat_end` → 962.

End nodes: 226: `<omitted>`; 828: `NonTerminating`; 883: `NonTerminating`; 888: `<omitted>`; 899: `<omitted>`; 921: `<omitted>`; 956: `<omitted>`; 958: `<omitted>`; 960: `<omitted>`; 962: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 310 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/6` |
| `scnChangeIdleAnimEvent` | 3 | 283 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/8` |
| `scnDialogLineEvent` | 50 | 26 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 331 / 189 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/13` |
| `scnIKEvent` | 6 | 331 / 182 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/7` |
| `scnLookAtAdvancedEvent` | 5 | 283 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/10` |
| `scnLookAtEvent` | 31 | 59 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 27 | 26 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnUnmountEvent` | 3 | 331 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 3 | 331 / 186 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/11` |
| `scneventsSocket` | 24 | 283 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/20` |
| `scneventsVFXEvent` | 2 | 1058 / 493 | `/Data/RootChunk/sceneGraph/Data/graph/78/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- speech, gaze: 4
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- vfx: 1

Raw SHA-256: `f3941a1e9f9d502f24652693aff48d1ef001e6394d7df5c1da415f20a20e245d`. Binary SHA-256: `a33e80c5f094910ef73320575c0cbcae7de78b835848cf68fc8f5c9ca4fe9c22`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq306\scenes\mq306_02_tech_expo_exploration.scene" --events
```

## `ep1\quest\minor_quests\mq306\scenes\mq306_03_expo_ripper.scene`

527 graph nodes, 642 edges; 115 event-bearing sections, 776 events; 183 screenplay lines, 28 screenplay options, 11 choice nodes.

Actors: Aaron (actor 0, community); Damir (actor 1, community); Angie (actor 2, community); Animal_01 (actor 3, community); Animal_02 (actor 4, community); Scav_01 (actor 5, community); Scav_02 (actor 6, community); Player (actor 7, findInContext).

Entries: `Start 0` → 1; `Start 11` → 3622; `Start 14` → 4082; `deal_refused` → 149; `angie_combat_comment` → 4183; `animals_defeated` → 2878; `Start 12` → 3784; `Start 16` → 4229; `Start 7` → 2476; `Start 10` → 3363; `Start 13` → 3889; `Start 9` → 3038; `Start 5` → 2157; `animals_entrance_preview` → 874.

Exits: `angie` → 2; `refuse_deal` → 145; `out_animals_setup` → 1030; `out_to_combat` → 4186; `aaron` → 226.

End nodes: 2: `<omitted>`; 145: `<omitted>`; 226: `<omitted>`; 1030: `NonTerminating`; 4186: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAddIdleAnimEvent` | 1 | 1934 / 1480 | `/Data/RootChunk/sceneGraph/Data/graph/148/Data/events/2` |
| `scnAudioEvent` | 2 | 407 / 384 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/1` |
| `scnChangeIdleAnimEvent` | 49 | 17 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 117 | 17 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 7 | 17 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/49` |
| `scnIKEvent` | 14 | 17 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/40` |
| `scnLookAtAdvancedEvent` | 38 | 17 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/16` |
| `scnLookAtEvent` | 130 | 17 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 206 | 17 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 2 | 1904 / 1462 | `/Data/RootChunk/sceneGraph/Data/graph/146/Data/events/15` |
| `scnUnmountEvent` | 7 | 17 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/50` |
| `scneventsCameraParamsEvent` | 2 | 1942 / 1496 | `/Data/RootChunk/sceneGraph/Data/graph/149/Data/events/4` |
| `scneventsEquipItemToPerformer` | 10 | 1595 / 1242 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 7 | 17 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/47` |
| `scneventsSocket` | 172 | 17 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/20` |
| `scneventsUnequipItemFromPerformer` | 4 | 1595 / 1244 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/6` |
| `scneventsVFXEvent` | 8 | 928 / 649 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 17
- skeletal_animation, socket_signal: 15
- skeletal_animation, gaze, socket_signal: 9
- speech: 8
- gaze: 7
- speech, skeletal_animation, socket_signal: 6
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, socket_signal: 5
- skeletal_animation, gaze: 5
- skeletal_animation, props_equipment, socket_signal: 4
- speech, gaze: 3
- speech, skeletal_animation, gaze: 3
- skeletal_animation: 3
- socket_signal: 3
- skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- vfx: 1
- gaze, audio, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- animation_state: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal: 1

Raw SHA-256: `607113f853224db354d4bf9aa820c90058bf7088208201e77cb73b69b5ee3b4b`. Binary SHA-256: `fc8a2a893a236d400c154ed0cbcebde5da345ac2a55142158b715996383f26eb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq306\scenes\mq306_03_expo_ripper.scene" --events
```

## `ep1\quest\minor_quests\mq306\scenes\mq306_04a_aaron_meeting.scene`

67 graph nodes, 83 edges; 14 event-bearing sections, 116 events; 24 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Aaron (actor 0, community); Angie (actor 1, community); Bartender (actor 2, community); Johnny (actor 3, spawnDespawn); Player (actor 4, findInContext).

Entries: `Start 0` → 1.

Exits: `johnny_terminating` → 214; `aaron_dead` → 36.

End nodes: 36: `NonTerminating`; 214: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 18 | 34 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 4 | 52 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/19` |
| `scnIKEvent` | 8 | 52 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnLookAtEvent` | 16 | 34 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnOverridePhantomParamsEvent` | 1 | 52 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/14` |
| `scnPlaySkAnimEvent` | 20 | 34 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnUnmountEvent` | 4 | 52 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/18` |
| `scneventsEquipItemToPerformer` | 5 | 52 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 4 | 52 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scneventsSocket` | 33 | 34 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 3 | 52 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `92a4dde07ffa79a2ad775803a62368a5a71785d9f4902c2d2da7a6dfa49cb3f9`. Binary SHA-256: `406cacbdfc3f33fc91bcdea24ba5a8a5fe494aff3ab8b709496ae0df5af7abe6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq306\scenes\mq306_04a_aaron_meeting.scene" --events
```

## `ep1\quest\minor_quests\mq306\scenes\mq306_04b_angie_meeting.scene`

41 graph nodes, 46 edges; 11 event-bearing sections, 73 events; 19 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Aaron (actor 0, community); Angie (actor 1, community); Animal_01 (actor 2, community); Animals_02 (actor 3, community); Player (actor 4, findInContext).

Entries: `Start 0` → 1; `Start 1` → 93.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 14 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 26 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 15 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsSocket` | 13 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXDurationEvent` | 2 | 16 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze: 1

Raw SHA-256: `851286ea09fbed704b9d22510b5a8161c0fca695423855c68d520aeb80fb7e82`. Binary SHA-256: `e8f55a29e7633c9bbd49b21abc31aff5c83fd76b142c6a77926fbbb536fc1a41`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq306\scenes\mq306_04b_angie_meeting.scene" --events
```

