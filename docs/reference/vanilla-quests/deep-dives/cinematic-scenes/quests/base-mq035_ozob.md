# Send in the Clowns: scene presentation

Journal identity: `quests/minor_quest/mq035_ozob`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq035_ozob.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq035\scenes\mq035_hook_call.scene`

29 graph nodes, 29 edges; 7 event-bearing sections, 15 events; 15 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Ozob (actor 0, findInContext); Player (actor 1, findInContext).

Entries: `hook_call_in` → 1; `call_again_in` → 43.

Exits: `hook_call_out` → 2; `reject_out` → 45.

End nodes: 2: `<omitted>`; 45: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 15 | 19 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7

Raw SHA-256: `51d2076368eb594ea5ad01b398a72be11ef168611958df5d7647bbe68f774214`. Binary SHA-256: `a8e841bbb146797102b7db39d79b6ce02442cfc29538b273604b388c1f9d0c9b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq035\scenes\mq035_hook_call.scene" --events
```

## `base\quest\minor_quests\mq035\scenes\mq035_ozob_dialogues.scene`

93 graph nodes, 82 edges; 32 event-bearing sections, 141 events; 73 screenplay lines, 5 screenplay options, 3 choice nodes.

Actors: Ozob (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `pickup_in` → 1; `honk_temp_in` → 93; `back_in_car_in` → 97; `drive_chat_1_in` → 7; `drive_chat_2_in` → 10; `drive_chat_3_in` → 13; `return_to_car_2_in` → 108; `arrived_in` → 22; `robbery_combat_ozob_in` → 295; `just_drive_in` → 27; `killem_in` → 32; `back_in_car_2_in` → 123; `chase_chat_in` → 37; `ending_in` → 42; `chase_fail_in` → 133; `combat_1_in` → 138; `combat_2_in` → 143; `combat_3_in` → 147; `combat_4_in` → 151; `combat_5_in` → 155; `fail_distance_in` → 73; `return_to_car_in` → 78.

Exits: `pickup_out` → 2; `honk_temp_out` → 94; `back_in_car_out` → 98; `drive_chat_1_out` → 8; `drive_chat_2_out` → 11; `drive_chat_3_out` → 14; `robbery_combat_out` → 288; `return_to_car_2_out` → 109; `arrived_out` → 23; `just_drive_out` → 28; `killem_out` → 33; `back_in_car_2_out` → 124; `chase_chat_out` → 38; `ending_out` → 43; `chase_fail_out` → 134; `combat_1_out` → 141; `combat_2_out` → 145; `combat_3_out` → 149; `combat_4_out` → 153; `ending_non_term_out` → 335; `combat_5_out` → 157; `fail_distance_out` → 74; `return_to_car_out` → 79.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 11: `<omitted>`; 14: `<omitted>`; 23: `<omitted>`; 28: `<omitted>`; 33: `<omitted>`; 38: `<omitted>`; 43: `<omitted>`; 74: `<omitted>`; 79: `<omitted>`; 94: `<omitted>`; 98: `<omitted>`; 109: `<omitted>`; 124: `<omitted>`; 134: `<omitted>`; 141: `<omitted>`; 145: `<omitted>`; 149: `<omitted>`; 153: `<omitted>`; 157: `<omitted>`; 288: `<omitted>`; 335: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 24 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scnDialogLineEvent` | 71 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 324 / 362 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/6` |
| `scnIKEvent` | 2 | 324 / 356 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/1` |
| `scnLookAtEvent` | 14 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 39 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 1 | 324 / 361 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 324 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/4` |
| `scneventsSocket` | 6 | 29 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/5` |
| `scneventsVFXEvent` | 2 | 57 / 155 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- speech, skeletal_animation: 5
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `d1f6f2ed939ed722ef6d067d15717b66db1f187a38b1cb2e2b72242071ac3f76`. Binary SHA-256: `edb70ad1ccd1f3691d9f9c5220b0e766d0ff84ee6629d09a5b1cd50da79b8309`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq035\scenes\mq035_ozob_dialogues.scene" --events
```

