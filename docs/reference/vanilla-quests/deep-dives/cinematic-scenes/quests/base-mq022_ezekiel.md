# Ezekiel Saw the Wheel: scene presentation

Journal identity: `quests/minor_quest/mq022_ezekiel`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq022_ezekiel.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene`

165 graph nodes, 192 edges; 27 event-bearing sections, 350 events; 52 screenplay lines, 13 screenplay options, 7 choice nodes.

Actors: Ganger_01 (actor 0, community); Ganger_02 (actor 1, community); Ganger_03 (actor 2, community); Owner (actor 3, spawnSet); Diner_01 (actor 4, community); Diner_02 (actor 5, community); Diner_03 (actor 6, community); Diner_04 (actor 7, community); Diner_05 (actor 8, community); Diner_06 (actor 9, community); Diner_07 (actor 10, community); Player (actor 11, findInContext).

Entries: `std_arr_foodshop_04` → 602; `mq022_01_attack` → 140; `std_arr_foodshop_04_from_choice` → 639; `mq022_people_dead` → 173; `mq022_people_alive` → 178; `Start` → 195.

Exits: `mq022_attacked` → 2; `mq022_01_attack_out` → 139; `std_arr_foodshop_04_end` → 620; `mq022_outtalked` → 147; `mq022_owner_outcome_good_out` → 630; `std_arr_foodshop_04_to_choice` → 637; `mq022_owner_outcome_bad_out` → 172.

End nodes: 2: `NonTerminating`; 139: `<omitted>`; 147: `NonTerminating`; 172: `<omitted>`; 620: `<omitted>`; 630: `<omitted>`; 637: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 33 | 155 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/3` |
| `scnDialogLineEvent` | 44 | 52 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 18 | 155 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/23` |
| `scnIKEvent` | 36 | 155 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/12` |
| `scnLookAtEvent` | 40 | 52 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 57 | 52 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPoseCorrectionEvent` | 1 | 790 / 1163 | `/Data/RootChunk/sceneGraph/Data/graph/127/Data/events/1` |
| `scnUnmountEvent` | 18 | 155 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/25` |
| `scneventsPlayerLookAtEvent` | 1 | 204 / 405 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/27` |
| `scneventsSetAnimFeatureEvent` | 18 | 155 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/21` |
| `scneventsSocket` | 83 | 52 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsVFXDurationEvent` | 1 | 155 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, animation_state: 1
- skeletal_animation: 1
- skeletal_animation, idle_animation, gaze: 1

Raw SHA-256: `57170ce1f359b2a71f37caf26eb0c7e934188ab8bbcfb5174ea7b18833922be5`. Binary SHA-256: `7d3df40c3fc69c2d96ee0c3c06735edbac007c022bef706b5241e82c85c901ff`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq022\scenes\mq022_01_diner.scene" --events
```

