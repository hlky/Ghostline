# Small Man, Big Mouth: scene presentation

Journal identity: `quests/minor_quest/mq017_streetkid`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq017_streetkid.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_01b_meet_your_fixer.scene`

334 graph nodes, 408 edges; 60 event-bearing sections, 647 events; 101 screenplay lines, 29 screenplay options, 18 choice nodes.

Actors: kirk_sawyer (actor 0, spawnSet); bartender (actor 1, spawnSet); big_joe (actor 2, community); v_male_tpp (actor 3, spawnDespawn); v_female_tpp (actor 4, spawnDespawn); Player_fpp (actor 5, findInContext).

Entries: `Meet_Your_Fixer_In` → 1; `coyote_performance_test` → 1743; `q000_pepe_after_kirk` → 1302; `mq017_reminder_in` → 1831; `kirk_preview` → 371.

Exits: `Meet_Your_Fixer_Out` → 2; `activate_chats` → 364.

End nodes: 2: `NonTerminating`; 364: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 28 | 62 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnChangeIdleAnimEvent` | 43 | 62 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 101 | 60 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 179 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scnIKEvent` | 10 | 179 / 337 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 159 / 300 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/32` |
| `scnLookAtEvent` | 105 | 62 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 164 | 60 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 5 | 179 / 357 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/15` |
| `scneventsAttachPropToNode` | 1 | 848 / 1654 | `/Data/RootChunk/sceneGraph/Data/graph/135/Data/events/6` |
| `scneventsAttachPropToPerformer` | 16 | 159 / 275 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/15` |
| `scneventsAttachPropToWorld` | 14 | 62 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scneventsCameraParamsEvent` | 19 | 154 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 5 | 179 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/12` |
| `scneventsSocket` | 123 | 60 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsVFXEvent` | 6 | 197 / 378 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- gaze: 7
- camera: 6
- speech, gaze: 4
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `6fdc79f6cae99f93b73f2970fa5e5e18ed0d0a279763f8c5fa5a149bea4fe590`. Binary SHA-256: `afdad5ffee1d0b1535ec9cfac659e31622c0298d12a7fe6aaab299c8fa1bd855`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_01b_meet_your_fixer.scene" --events
```

## `base\quest\minor_quests\mq017\scenes\mq017_streetkid_01_kirk_calling.scene`

23 graph nodes, 23 edges; 3 event-bearing sections, 28 events; 15 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Kirk_sawyer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `call_rejected` → 264.

End nodes: 2: `<omitted>`; 264: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 9 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 15 | 9 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 3 | 9 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation: 2
- speech, idle_animation: 1

Raw SHA-256: `a6fa305df30300a81ff1e65a5e52efa05f1806b53361995433f7a4fd2417b519`. Binary SHA-256: `cdc5881ca2e57dcda48ad4ba61ae3769ac6b48367a257d849f0440d55d467a5e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq017\scenes\mq017_streetkid_01_kirk_calling.scene" --events
```

## `base\quest\minor_quests\mq017\scenes\mq017_streetkid_01a_johnny.scene`

28 graph nodes, 33 edges; 6 event-bearing sections, 36 events; 16 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `Cinedebug_start` → 123.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 13 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 5 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnOverridePhantomParamsEvent` | 1 | 129 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 129 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsSocket` | 2 | 129 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scneventsVFXEvent` | 3 | 175 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation, gaze: 3
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- gaze, vfx, socket_signal: 1
- vfx: 1

Raw SHA-256: `5ba1117e5ee248899bf677d7c9ec78fad8b3bf00a2999aee2c83685fc17fa39b`. Binary SHA-256: `4c24c1cfbee78e16278dbeff2c64252d810be87388ed7587199a7f03bd25f126`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq017\scenes\mq017_streetkid_01a_johnny.scene" --events
```

## `base\quest\minor_quests\mq017\scenes\mq017_streetkid_02_reunion.scene`

87 graph nodes, 99 edges; 17 event-bearing sections, 124 events; 33 screenplay lines, 7 screenplay options, 6 choice nodes.

Actors: kirk_sawyer (actor 0, spawnSet); big_joe (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `mq017_kirk_reminder_out` → 280.

End nodes: 2: `<omitted>`; 280: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 21 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/11` |
| `scnChangeIdleAnimEvent` | 26 | 10 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnDialogLineEvent` | 23 | 10 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 138 / 279 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/7` |
| `scnIKEvent` | 4 | 138 / 272 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/1` |
| `scnLookAtEvent` | 10 | 10 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 28 | 10 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnUnmountEvent` | 2 | 138 / 278 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/6` |
| `scneventsAttachPropToPerformer` | 1 | 232 / 345 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 2 | 138 / 276 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/5` |
| `scneventsSocket` | 20 | 10 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, props_equipment, socket_signal: 1
- idle_animation, gaze: 1

Raw SHA-256: `a79220f4901221eefeca7d734d9e95bb7955551c3e304b4ba9b41d051f9bdcf5`. Binary SHA-256: `e02dfe5b0c46b1556fe995259f5bacc22f58e72c3c7959fa8d225822e6284046`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq017\scenes\mq017_streetkid_02_reunion.scene" --events
```

## `base\quest\minor_quests\mq017\scenes\mq017_streetkid_03_confront_thugs.scene`

349 graph nodes, 477 edges; 44 event-bearing sections, 315 events; 68 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: kirk_sawyer (actor 0, spawnSet); thomas (actor 1, community); johnny (actor 2, spawnDespawn); big_joe (actor 3, spawnSet); thug_03 (actor 4, community); thug_01 (actor 5, community); thug_02 (actor 6, community); thug_04 (actor 7, community); thug_05 (actor 8, community); thug_06 (actor 9, community); thug_07 (actor 10, community); mq017_delivery_truck (actor 11, spawner); mq017_gangers_car (actor 12, spawner); Player (actor 13, findInContext).

Entries: `Start 0` → 1; `Start 9` → 2311; `Start 7` → 2077; `cinedebug_van` → 1774; `Cinedebug_end` → 1783; `Start 8` → 2120.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 198 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnChangeIdleAnimEvent` | 58 | 41 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 42 | 41 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 275 / 446 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/34` |
| `scnIKEvent` | 6 | 275 / 418 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/19` |
| `scnLookAtEvent` | 53 | 41 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnOverridePhantomParamsEvent` | 1 | 1843 / 1894 | `/Data/RootChunk/sceneGraph/Data/graph/263/Data/events/1` |
| `scnPlaySkAnimEvent` | 67 | 41 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnUnmountEvent` | 3 | 275 / 447 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/35` |
| `scneventsAttachPropToNode` | 2 | 198 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 1986 / 2091 | `/Data/RootChunk/sceneGraph/Data/graph/294/Data/events/3` |
| `scneventsEquipItemToPerformer` | 5 | 1378 / 1407 | `/Data/RootChunk/sceneGraph/Data/graph/171/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 6 | 275 / 442 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/31` |
| `scneventsSocket` | 60 | 41 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 3 | 275 / 407 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/10` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1390 / 1428 | `/Data/RootChunk/sceneGraph/Data/graph/173/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 10
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech: 3
- speech, idle_animation, gaze: 2
- speech, idle_animation: 2
- skeletal_animation, gaze, socket_signal: 2
- idle_animation, gaze, socket_signal: 2
- skeletal_animation, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, props_equipment, audio, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1
- idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- props_equipment: 1

Raw SHA-256: `f0beca8099cee510b6d40ec150a3c91d996657939aa7a6301fd7eed1e7d0f3d7`. Binary SHA-256: `06fe494fce2c2cb270d5bd82df0ed5bc567f4c6de4aa1279c9c481e1f81db7c2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq017\scenes\mq017_streetkid_03_confront_thugs.scene" --events
```

