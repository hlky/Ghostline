# Bullets: scene presentation

Journal identity: `quests/minor_quest/mq030_melisa`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq030_melisa.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene`

623 graph nodes, 808 edges; 72 event-bearing sections, 448 events; 114 screenplay lines, 13 screenplay options, 8 choice nodes.

Actors: Zane (actor 0, spawnSet); Johnny (actor 1, spawnSet); mq030_jinguji_bodyguard_1 (actor 2, community); mq030_jinguji_bodyguard_2 (actor 3, community); mq030_cyberpsycho (actor 4, community); mq030_max_tac_1 (actor 5, community); mq030_max_tac_2 (actor 6, community); mq030_max_tac_3 (actor 7, community); mq030_max_tac_4 (actor 8, community); mq030_melisa (actor 9, community); mq030_max_tac_5 (actor 10, community); mq030_max_tac_6 (actor 11, community); mq030_max_tac_7 (actor 12, community); mq030_max_tac_8 (actor 13, community); mq030_max_tac_9 (actor 14, community); mq030_street_crowd_phone_nervous (actor 15, community); mq030_street_crowd_phone_calm (actor 16, community); mq030_street_crowd_angry (actor 17, community); Heli (actor 18, spawner); Player (actor 19, findInContext).

Entries: `sit_preview` → 1367; `max_tac_spawn` → 3189; `Linestoreuse` → 944; `Start 11` → 2806; `psycho` → 1651; `mq030_01_melisa_scene_in` → 521.

Exits: `mq030_failed_out` → 934; `mq030_01_melisa_scene_out` → 451.

End nodes: 451: `NonTerminating`; 934: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 421 / 698 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/10` |
| `scnChangeIdleAnimEvent` | 5 | 206 / 262 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/2` |
| `scnDialogLineEvent` | 98 | 4 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 8 | 316 / 523 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/18` |
| `scnIKEvent` | 16 | 316 / 515 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/11` |
| `scnLookAtEvent` | 90 | 10 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 118 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnUnmountEvent` | 8 | 316 / 522 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/17` |
| `scneventsAttachPropToPerformer` | 1 | 1731 / 2011 | `/Data/RootChunk/sceneGraph/Data/graph/256/Data/events/2` |
| `scneventsEquipItemToPerformer` | 1 | 1731 / 2013 | `/Data/RootChunk/sceneGraph/Data/graph/256/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 8 | 316 / 518 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/14` |
| `scneventsSocket` | 92 | 10 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 2 | 1030 / 1503 | `/Data/RootChunk/sceneGraph/Data/graph/184/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, skeletal_animation, gaze, socket_signal: 12
- speech, skeletal_animation, gaze: 8
- speech, gaze: 6
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze: 1
- gaze, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `d508b112ce2178dd4269de2f2384a42e29b9827f61df008439a9f91a4cff9ee2`. Binary SHA-256: `9fe1e530166b01dde3513373740cb5988b3127c2d9e95d1bc267b60f82564e08`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene" --events
```

## `base\quest\minor_quests\mq030\scenes\mq030_02_jinguji_community.scene`

6 graph nodes, 5 edges; 0 event-bearing sections, 0 events; 0 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: mq030_jinguji_customer_uncertain (actor 0, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |

Presentation families coexisting in an event section (counts are sections, not durations):


Raw SHA-256: `a403b07c49f9e8825fe6606cc767b8ede8979f4ece9702199812400453a7dfb4`. Binary SHA-256: `24d58e10daf4d5a3f480fa840c881a55f3320fcb54e5e5e156387d1168bd22d3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq030\scenes\mq030_02_jinguji_community.scene" --events
```

