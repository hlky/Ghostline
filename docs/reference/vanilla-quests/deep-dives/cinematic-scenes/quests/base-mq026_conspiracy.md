# The Prophet's Song: scene presentation

Journal identity: `quests/minor_quest/mq026_conspiracy`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq026_conspiracy.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene`

355 graph nodes, 409 edges; 58 event-bearing sections, 385 events; 116 screenplay lines, 18 screenplay options, 6 choice nodes.

Actors: Prophet (actor 0, community); Tourist_01 (actor 1, community); Tourist_02 (actor 2, community); Disciple (actor 3, community); Nomad01 (actor 4, community); Nomad02 (actor 5, community); Player (actor 6, findInContext).

Entries: `cyberspace_in` → 1; `reptilians_in` → 15; `vampire_in` → 18; `nomads_in` → 19; `eyes_in` → 21; `rambling in` → 618; `flex` → 2227.

Exits: `end_scene` → 47; `nomads_out` → 171; `debug_repeat` → 495; `killed_out` → 2547.

End nodes: 47: `<omitted>`; 171: `<omitted>`; 495: `<omitted>`; 2547: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 41 | 11 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 94 | 7 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 4 | 963 / 961 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/20` |
| `scnIKEvent` | 8 | 963 / 945 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/9` |
| `scnLookAtAdvancedEvent` | 10 | 396 / 334 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/6` |
| `scnLookAtEvent` | 35 | 111 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/11` |
| `scnPlaySkAnimEvent` | 91 | 7 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 4 | 963 / 960 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/19` |
| `scneventsEquipItemToPerformer` | 1 | 963 / 924 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 4 | 963 / 956 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/16` |
| `scneventsSocket` | 92 | 7 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 963 / 939 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 16
- speech, skeletal_animation, socket_signal: 12
- idle_animation, socket_signal: 4
- socket_signal: 4
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- skeletal_animation: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze: 1

Raw SHA-256: `7eaf0054b384d33262629d2fbb81cf9663b5c07d3bd20d706d2189fc43205031`. Binary SHA-256: `a13b4a2f36b6ae9b248b8b49b046f8efe5dca94ec0ba5b825eecb90a44c8ff4c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq026\scenes\mq026_01_prophecy.scene" --events
```

## `base\quest\minor_quests\mq026\scenes\mq026_02_death.scene`

102 graph nodes, 122 edges; 25 event-bearing sections, 126 events; 62 screenplay lines, 16 screenplay options, 7 choice nodes.

Actors: Disciple (actor 0, community); Johnny (actor 1, spawnDespawn); Prophet (actor 2, community); Player (actor 3, findInContext).

Entries: `Start 0` → 1; `test` → 294.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 15 | 31 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnDialogLineEvent` | 59 | 19 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnLookAtEvent` | 4 | 31 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 20 | 155 / 185 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/0` |
| `scneventsAttachPropToNode` | 1 | 155 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/4` |
| `scneventsAttachPropToPerformer` | 2 | 155 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scneventsSocket` | 25 | 19 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation: 6
- speech, skeletal_animation: 5
- speech, socket_signal: 3
- speech, idle_animation, socket_signal: 3
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal: 1

Raw SHA-256: `2984129b9411c374b72931358dcfe4d917b56d18befc005ee9aec8c06273283e`. Binary SHA-256: `c088e33f1752ee467b45452e7f421e9e2ec215b47f750bf88a5adc8de1d8de3f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq026\scenes\mq026_02_death.scene" --events
```

## `base\quest\minor_quests\mq026\scenes\mq026_03_nomad.scene`

197 graph nodes, 259 edges; 31 event-bearing sections, 285 events; 75 screenplay lines, 15 screenplay options, 6 choice nodes.

Actors: Prophet (actor 0, community); Nomad01 (actor 1, community); Nomad02 (actor 2, community); Player (actor 3, findInContext).

Entries: `Start 0` → 1; `Start 2` → 1236; `test02` → 825.

Exits: `End 0` → 339; `reveal_out` → 150.

End nodes: 150: `NonTerminating`; 339: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 21 | 43 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnDialogLineEvent` | 64 | 43 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scnGameplayTransitionEvent` | 4 | 565 / 813 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/7` |
| `scnIKEvent` | 8 | 565 / 806 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/1` |
| `scnLookAtAdvancedEvent` | 6 | 52 / 214 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/14` |
| `scnLookAtEvent` | 45 | 43 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnPlaySkAnimEvent` | 75 | 43 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnUnmountEvent` | 4 | 565 / 812 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/6` |
| `scneventsEquipItemToPerformer` | 3 | 559 / 768 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 4 | 565 / 810 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/5` |
| `scneventsSocket` | 50 | 43 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/12` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 559 / 784 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze: 4
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze, socket_signal: 1
- speech: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `469accc73f76d83e29c2249a8ba498fff603dacd1e63ced141d20b81812bc764`. Binary SHA-256: `03685bb480270e81e99739d0bbee7b8dcff64a94d868d505f0297ee369934912`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq026\scenes\mq026_03_nomad.scene" --events
```

## `base\quest\minor_quests\mq026\scenes\mq026_04_smuggler.scene`

314 graph nodes, 369 edges; 23 event-bearing sections, 120 events; 41 screenplay lines, 7 screenplay options, 4 choice nodes.

Actors: MIB01 (actor 0, community); MIB02 (actor 1, community); GangRifle01 (actor 2, community); GangMelee01 (actor 3, community); GangHandgun01 (actor 4, community); GangMachete02 (actor 5, community); GangShotgun (actor 6, community); Johnny (actor 7, spawnDespawn); GangTank01 (actor 8, community); maelstrom_dying (actor 9, community); mq026_van (actor 10, spawner); mq026_mal_01 (actor 11, spawner); mq026_mal_02 (actor 12, spawner); Player (actor 13, findInContext).

Entries: `Start 0` → 725; `cyberpsycho_line` → 2016.

Exits: `cyberpsycho_out` → 2025; `cleanup_out` → 518.

End nodes: 518: `<omitted>`; 2025: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 525 / 716 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/0` |
| `scnDialogLineEvent` | 31 | 40 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scnGameplayTransitionEvent` | 4 | 1283 / 1465 | `/Data/RootChunk/sceneGraph/Data/graph/199/Data/events/11` |
| `scnIKEvent` | 8 | 1283 / 1458 | `/Data/RootChunk/sceneGraph/Data/graph/199/Data/events/5` |
| `scnLookAtEvent` | 10 | 495 / 691 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/4` |
| `scnPlaySkAnimEvent` | 28 | 40 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnUnmountEvent` | 4 | 1283 / 1464 | `/Data/RootChunk/sceneGraph/Data/graph/199/Data/events/10` |
| `scneventsEquipItemToPerformer` | 2 | 1139 / 1328 | `/Data/RootChunk/sceneGraph/Data/graph/181/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 4 | 1283 / 1460 | `/Data/RootChunk/sceneGraph/Data/graph/199/Data/events/7` |
| `scneventsSocket` | 21 | 40 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/3` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1139 / 1330 | `/Data/RootChunk/sceneGraph/Data/graph/181/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation: 3
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, idle_animation, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, idle_animation: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1

Raw SHA-256: `9b91c01394fd8b88126c22871e9a17c7ec483205ae055cda31b765bb94ca3e60`. Binary SHA-256: `436d0517bb59a9c654cd640dedf7a5659f5a5af558f58280476a03f2d86bee79`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq026\scenes\mq026_04_smuggler.scene" --events
```

