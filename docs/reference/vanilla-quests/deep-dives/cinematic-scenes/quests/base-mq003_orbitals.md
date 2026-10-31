# Space Oddity: scene presentation

Journal identity: `quests/minor_quest/mq003_orbitals`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq003_orbitals.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq003\scenes\mq003_01_homeless.scene`

176 graph nodes, 192 edges; 32 event-bearing sections, 348 events; 55 screenplay lines, 14 screenplay options, 7 choice nodes.

Actors: Homeless_Leader (actor 0, community); Homeless_Fat (actor 1, community); Homeless_Suitcase (actor 2, community); Player (actor 3, findInContext).

Entries: `suitcase_activate` → 157; `suitcase_unlock` → 165; `homeless_unlock_reaction` → 173; `homeless_question` → 39; `activation_reaction` → 178; `shard_comment` → 199; `Start 16` → 879; `return_in` → 221; `Start 17` → 896; `suitcase_examine` → 98.

Exits: `suitcase_activate_out` → 158; `suitcase_unlock_out` → 166; `homeless_unlock_reaction_out` → 174; `homeless_question_out` → 40; `activation_reaction_out` → 179; `suitcase_hacked_out` → 183; `shard_found_early_out` → 193; `shard_comment_out` → 200; `attacked_homeless_out` → 736; `leave_out` → 72; `hack_kill_out` → 1043; `homeless_post_talk_out` → 119.

End nodes: 40: `NonTerminating`; 72: `NonTerminating`; 119: `<omitted>`; 158: `<omitted>`; 166: `NonTerminating`; 174: `NonTerminating`; 179: `<omitted>`; 183: `NonTerminating`; 193: `NonTerminating`; 200: `NonTerminating`; 736: `<omitted>`; 1043: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 16 | 17 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 48 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnGameplayTransitionEvent` | 3 | 68 / 446 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/72` |
| `scnIKEvent` | 6 | 68 / 421 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/60` |
| `scnLookAtEvent` | 70 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnPlaySkAnimEvent` | 124 | 6 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnUnmountEvent` | 3 | 68 / 447 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/73` |
| `scneventsEquipItemToPerformer` | 3 | 48 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 3 | 68 / 444 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/71` |
| `scneventsSocket` | 70 | 13 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsVFXEvent` | 2 | 150 / 568 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, skeletal_animation, gaze, socket_signal: 7
- skeletal_animation, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, vfx: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `bdfa3af6a029528c308dd079c37a8fe041738a2f14087ea6def27deb39ee97fb`. Binary SHA-256: `709d6f39bc0d81fa85b716eabb1603bb1d1ab6d4e1eb5e1538bd0fd5764a1bfb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq003\scenes\mq003_01_homeless.scene" --events
```

## `base\quest\minor_quests\mq003\scenes\mq003_02_corpse.scene`

18 graph nodes, 13 edges; 5 event-bearing sections, 5 events; 5 screenplay lines, 3 screenplay options, 3 choice nodes.

Actors: Johnny (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `corpse_pile` → 20; `corpse_examine_in` → 25; `clue_blood_trail` → 9; `clue_spot` → 11; `shard_taken_in` → 87.

Exits: `corpse_pile_out` → 21; `corpse_examine_out` → 26; `clue_blood_trail_out` → 10; `clue_spot_out` → 12; `shard_taken_out` → 88.

End nodes: 10: `<omitted>`; 12: `<omitted>`; 21: `<omitted>`; 26: `<omitted>`; 88: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 14 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5

Raw SHA-256: `7e92110a6cb0c7a2dcc9eb0dd90573c37c73a5ab70503037dfeacc98be1bd02e`. Binary SHA-256: `3675fe597c08dd9c0870b8762ce9bffa9fe32b149d260b55fb6d1f0bb97e3f26`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq003\scenes\mq003_02_corpse.scene" --events
```

## `base\quest\minor_quests\mq003\scenes\mq003_03_orbital_pod.scene`

31 graph nodes, 26 edges; 9 event-bearing sections, 70 events; 18 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Soldier_2 (actor 0, community); Soldier_3 (actor 1, community); Soldier_4 (actor 2, community); Soldier_5 (actor 3, community); Johnny (actor 4, spawnDespawn); Player (actor 5, findInContext).

Entries: `soldier_retrieve_pod` → 28; `clear_enemies_first` → 4; `soldier_engage` → 30; `retrieve_pod` → 9; `retrieve_pod_reaction` → 41; `soldier_fluff` → 23.

Exits: `soldier_retrieve_pod_out` → 29; `clear_enemies_first_out` → 5; `soldier_engage_out` → 31; `retrieve_pod_out` → 10; `retrieve_pod_reaction_out` → 40; `johnny_disappear` → 68; `soldier_fluff_out` → 24.

End nodes: 5: `<omitted>`; 10: `<omitted>`; 24: `<omitted>`; 29: `<omitted>`; 31: `<omitted>`; 40: `NonTerminating`; 68: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 20 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/13` |
| `scnDialogLineEvent` | 17 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 12 | 20 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnPlaySkAnimEvent` | 28 | 20 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scneventsSocket` | 7 | 20 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- gaze: 1

Raw SHA-256: `86042cf15be56a4b3c7efc34435e049af7610777580de73534621e048713c34c`. Binary SHA-256: `e0b7270ce092a86d778c8482da219086b303adfe5a2b83f22a1be5048f8afc01`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq003\scenes\mq003_03_orbital_pod.scene" --events
```

