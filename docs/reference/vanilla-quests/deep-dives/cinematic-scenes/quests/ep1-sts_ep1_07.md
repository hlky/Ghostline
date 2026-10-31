# Gig: Roads to Redemption: scene presentation

Journal identity: `ep1/quests/street_stories/sts_ep1_07`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-sts_ep1_07.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_bomb_interaction.scene`

76 graph nodes, 100 edges; 22 event-bearing sections, 74 events; 32 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `Detonator Swaped` → 2; `End 1` → 237.

End nodes: 2: `NonTerminating`; 237: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 10 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 17 | 10 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 201 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/5` |
| `scnIKEvent` | 2 | 201 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/2` |
| `scnLookAtEvent` | 7 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 27 | 10 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 201 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 1 | 201 / 185 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/0` |
| `scneventsSocket` | 15 | 10 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 12
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, socket_signal: 2
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `49465af1dde20e6ebf9a18efd113faec209bdafe3642981c2a810c268454a847`. Binary SHA-256: `a6013fab0b6588425c3259d42201b2a2ec62261641fa2011ed2ce2d404eb8b24`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_bomb_interaction.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_client_meeting.scene`

138 graph nodes, 180 edges; 45 event-bearing sections, 286 events; 86 screenplay lines, 22 screenplay options, 9 choice nodes.

Actors: Nele (actor 0, community); johnny (actor 1, spawnDespawn); agent (actor 2, community); Player (actor 3, findInContext).

Entries: `Before_start` → 1.

Exits: `Before_end` → 2; `Kill signal` → 126.

End nodes: 2: `NonTerminating`; 126: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 39 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/13` |
| `scnChangeIdleAnimEvent` | 7 | 28 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 70 | 28 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 39 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/14` |
| `scnIKEvent` | 2 | 39 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnLookAtEvent` | 80 | 28 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 55 | 28 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPoseCorrectionEvent` | 2 | 471 / 277 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/4` |
| `scnUnmountEvent` | 1 | 39 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/18` |
| `scneventsAttachPropToPerformer` | 8 | 39 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scneventsAttachPropToWorld` | 5 | 39 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/19` |
| `scneventsCameraParamsEvent` | 4 | 39 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 1 | 39 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scneventsSocket` | 48 | 28 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 10
- speech, skeletal_animation, gaze: 4
- speech, gaze: 4
- speech, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech: 2
- gaze: 2
- skeletal_animation: 2
- camera: 2
- speech, skeletal_animation, gaze, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1

Raw SHA-256: `397b3bc5562025c9b905c1fa3894cc02abeb129548c3d26b764ef3e39138e312`. Binary SHA-256: `a79b7af260fbeb38c9d3df8e5213573ad941c36593fabc988f0a423776876caa`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_client_meeting.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_enemies_chats.scene`

42 graph nodes, 60 edges; 9 event-bearing sections, 22 events; 22 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: enemy_elevator_01 (actor 0, community); enemy_elevator_03 (actor 1, community); pool_worker_01 (actor 2, community); pool_worker_02 (actor 3, community); pool_guard_01 (actor 4, community); deal_soldier_01 (actor 5, community); deal_ganger_01 (actor 6, community); shooting_range_01 (actor 7, community); shooting_range_02 (actor 8, community); minotaur (actor 9, community); ganger_elevator (actor 10, community).

Entries: `Elevator_start` → 1; `Workers_pool_start` → 9; `shooting_range_start` → 65; `Deal I enter` → 28; `Wraiths_gone` → 202.

Exits: `Elevator_end` → 2; `Pool_end` → 11; `shooting_range_end` → 68; `Deal I exit` → 29; `wraiths_gone` → 205.

End nodes: 2: `<omitted>`; 11: `<omitted>`; 29: `<omitted>`; 68: `<omitted>`; 205: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 22 | 19 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9

Raw SHA-256: `3b30bc6ed9cb6c54f04b239695ed34cdfcfabd94bed5d4d04c408b8978f01286`. Binary SHA-256: `ce4c0a6752bc6de414aafe28dbccd26e9cd15b51a52c13298e893dcf74572b45`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_enemies_chats.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_final_meeting.scene`

308 graph nodes, 363 edges; 51 event-bearing sections, 495 events; 93 screenplay lines, 18 screenplay options, 8 choice nodes.

Actors: Nele (actor 0, community); agent_01 (actor 1, community); agent_02 (actor 2, community); agent_03 (actor 3, community); johnny (actor 4, spawnDespawn); agent_04 (actor 5, community); agents_car (actor 6, spawnSet); nele_car (actor 7, spawnSet); agents_car_02 (actor 8, spawnSet); Player (actor 9, findInContext).

Entries: `Start 0` → 1; `nele_thanks` → 674; `Start 7` → 2489; `Start 5` → 1998; `Start 3` → 1164.

Exits: `nele_prisoner` → 2; `combat` → 617; `agents mounted scene kill` → 2746; `nele_thanks_end` → 678; `End 7` → 2662.

End nodes: 2: `NonTerminating`; 617: `NonTerminating`; 678: `NonTerminating`; 2662: `<omitted>`; 2746: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 363 / 252 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/7` |
| `scnChangeIdleAnimEvent` | 14 | 166 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnDialogLineEvent` | 64 | 8 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 1174 / 645 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/3` |
| `scnGameplayTransitionEvent` | 14 | 131 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/12` |
| `scnIKEvent` | 28 | 131 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scnLookAtAdvancedEvent` | 2 | 1174 / 670 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/20` |
| `scnLookAtEvent` | 114 | 34 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnPlaySkAnimEvent` | 103 | 8 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 3 | 131 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/28` |
| `scnUnmountEvent` | 13 | 131 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/16` |
| `scneventsAttachPropToPerformer` | 5 | 586 / 375 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/5` |
| `scneventsAttachPropToWorld` | 1 | 2861 / 1998 | `/Data/RootChunk/sceneGraph/Data/graph/244/Data/events/4` |
| `scneventsEquipItemToPerformer` | 1 | 2343 / 1442 | `/Data/RootChunk/sceneGraph/Data/graph/158/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 22 | 131 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/13` |
| `scneventsSocket` | 100 | 8 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 2 | 131 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/48` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 13
- speech, skeletal_animation, gaze: 4
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, socket_signal: 2
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- gaze: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- idle_animation, gameplay_action: 1

Raw SHA-256: `6f61d6ce49be87a34ab46f4409217274a49edbe5bd81f71ced23f2dbc7da3ab8`. Binary SHA-256: `9e0188bd4918737b33261b8a5c0bfbdbf1cd0a7dc96f75ce5257eae482870687`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_final_meeting.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_holocall_debrief.scene`

30 graph nodes, 38 edges; 5 event-bearing sections, 8 events; 8 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 72.

End nodes: 2: `<omitted>`; 72: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 8 | 119 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5

Raw SHA-256: `e429057d1e14cdd387ebd75fc528418778d92ec67341ff6bf72a4dbb54eeb9ce`. Binary SHA-256: `0f95f556d67bb141f4d65c4f51a8a35eee421ccdcc13df30664b73e0887c054f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_holocall_debrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_holocall_prebrief.scene`

21 graph nodes, 24 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 92.

End nodes: 2: `<omitted>`; 92: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 138 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `e50fb7c3689d91c3aaf88b93c1c71bcd2b3f45d6dd45e68b30f6ac69099b817d`. Binary SHA-256: `7c62dd56e00c72eda27f4a6b0f6c64f31ee94d4e1dd702a18253bbae1769208b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_07\scenes\sts_ep1_07_holocall_prebrief.scene" --events
```

