# Search and Destroy: scene presentation

Journal identity: `quests/main_quest/act_01/q112_04_hideout`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q112_04_hideout.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q112\scenes\q112_09_parade_abduction.scene`

147 graph nodes, 179 edges; 24 event-bearing sections, 172 events; 59 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Takemura (actor 0, spawnSet); Hanako (actor 1, spawnSet); Yorinobu (actor 2, spawnSet); Victim (actor 3, community); Arasaka_Soldier (actor 4, community); Injured_Man (actor 5, community); Injured_Woman (actor 6, community); Gillean_Jordan (actor 7, community); Johnny (actor 8, spawnDespawn); V (actor 9, findInContext).

Entries: `q112_09_abduction_in` → 1; `q112_09_victim_death_in` → 173; `q112_09_johnny_in` → 625; `q112_09_injured_man_in` → 526; `q112_09_news54_in` → 531; `arasaka_soldier_combat` → 1099.

Exits: `q112_09_abduction_out` → 2; `q112_09_victim_death_combat` → 1133; `End 9` → 737; `q112_09_victim_death_out` → 183; `q112_09_johnny_out` → 632; `End 10` → 772; `q112_09_injured_man_out` → 529; `q112_09_news54_out` → 540.

End nodes: 2: `NonTerminating`; 183: `<omitted>`; 529: `<omitted>`; 540: `<omitted>`; 632: `NonTerminating`; 737: `<omitted>`; 772: `<omitted>`; 1133: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 15 | 161 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/2` |
| `scnDialogLineEvent` | 52 | 17 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 167 / 207 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/16` |
| `scnIKEvent` | 6 | 167 / 197 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/7` |
| `scnLookAtAdvancedEvent` | 3 | 515 / 405 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/3` |
| `scnLookAtEvent` | 28 | 17 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 35 | 17 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnUnmountEvent` | 3 | 167 / 206 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/15` |
| `scneventsAttachPropToPerformer` | 1 | 161 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/14` |
| `scneventsAttachPropToWorld` | 1 | 161 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 3 | 167 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/12` |
| `scneventsSocket` | 20 | 17 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/36` |
| `scneventsVFXEvent` | 2 | 161 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/16` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, gaze: 2
- speech, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation: 1
- idle_animation: 1
- skeletal_animation, socket_signal: 1
- gaze, socket_signal: 1
- gaze: 1

Raw SHA-256: `1dddc38c64f51e725843407c28760074f24d225e38ac0d71d08a9dd863f647a9`. Binary SHA-256: `b8ce55852de19fa2382b1d05675314485914597d708709dba30edd1d1ee08fff`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_09_parade_abduction.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_10_safe_house.scene`

418 graph nodes, 577 edges; 64 event-bearing sections, 528 events; 107 screenplay lines, 19 screenplay options, 9 choice nodes.

Actors: Takemura (actor 0, spawnSet); Hanako (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); arasaka_01 (actor 3, community); arasaka_02 (actor 4, community); arasaka_03 (actor 5, community); Takemura_holo (actor 6, spawnSet); arasaka_04 (actor 7, community); adam_smasher (actor 8, spawnSet); arasaka_end_01 (actor 9, community); arasaka_end_02 (actor 10, community); arasaka_end_03 (actor 11, community); arasaka_victim (actor 12, spawnDespawn); arasaka_victim_02 (actor 13, spawnDespawn); arasaka_victim_03 (actor 14, spawnDespawn); arasaka_no_react_01 (actor 15, community); arasaka_no_react_02 (actor 16, community); arasaka_no_react_03 (actor 17, community); av (actor 18, spawner); V (actor 19, findInContext).

Entries: `q112_10_phone_in` → 25; `q112_10_safe_house_in` → 38; `johnny_sickness_in` → 2335; `backedup line` → 2431; `q112_safe_house_combat` → 1035; `q112_arasaka_patrol_chat_001_in` → 1073; `q112_arasaka_raport_in` → 1076.

Exits: `q112_10_phone_out` → 26; `door_shot` → 1187; `End 10` → 2338; `arasaka_soldiers_appear` → 137; `q112_arasaka_patrol_chat_001_out` → 2854; `q112_arasaka_raport_out` → 2856; `q112_10_safe_house_out` → 216; `ai_command_takemura` → 604; `checkpoint` → 607; `av_gunfire_start` → 3709; `av_gunfire_stop` → 3711.

End nodes: 26: `<omitted>`; 137: `NonTerminating`; 216: `<omitted>`; 604: `NonTerminating`; 607: `NonTerminating`; 1187: `NonTerminating`; 2338: `<omitted>`; 2854: `<omitted>`; 2856: `<omitted>`; 3709: `NonTerminating`; 3711: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 41 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnChangeIdleAnimEvent` | 17 | 291 / 263 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/4` |
| `scnDialogLineEvent` | 96 | 27 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 6 | 366 / 506 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/20` |
| `scnIKEvent` | 12 | 366 / 498 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/13` |
| `scnLookAtEvent` | 102 | 27 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 99 | 69 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 406 / 548 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/3` |
| `scnUnmountEvent` | 6 | 366 / 505 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/19` |
| `scneventsAttachPropToPerformer` | 4 | 1132 / 1242 | `/Data/RootChunk/sceneGraph/Data/graph/147/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 1141 / 1256 | `/Data/RootChunk/sceneGraph/Data/graph/148/Data/events/1` |
| `scneventsCameraParamsEvent` | 3 | 982 / 1008 | `/Data/RootChunk/sceneGraph/Data/graph/112/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 6 | 366 / 501 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/16` |
| `scneventsSocket` | 110 | 69 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scneventsVFXEvent` | 55 | 406 / 550 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, skeletal_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- gaze: 5
- skeletal_animation, socket_signal: 4
- skeletal_animation, gaze, audio, vfx, socket_signal: 4
- socket_signal: 3
- speech, gaze: 2
- speech, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, camera, socket_signal: 2
- skeletal_animation, vfx, socket_signal: 2
- speech, gaze, audio: 1
- speech, gaze, vfx, animation_state: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx: 1
- skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, vfx, socket_signal: 1
- vfx: 1

Raw SHA-256: `511d509c4ff55d1f1ac495fd6517bafc2608654fe74c380e9d29c88b8313f24a`. Binary SHA-256: `327076165157bbfc1755a4e0df0b2d864493eefa83951d08ff9a2aa5c9f70ebb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_10_safe_house.scene" --events
```

## `base\quest\main_quests\part1\q112\scenes\q112_11_shotgun.scene`

283 graph nodes, 392 edges; 69 event-bearing sections, 501 events; 179 screenplay lines, 24 screenplay options, 11 choice nodes.

Actors: Hanako (actor 0, findInContext); Johnny (actor 1, spawnDespawn); Doll (actor 2, community); delamain (actor 3, spawner); V (actor 4, findInContext).

Entries: `q112_11_shotgun_in` → 16; `johnny_prev` → 2503; `q115_reuse_in` → 1183.

Exits: `q112_11_shotgun_out` → 17; `q112_11_shotgun_out_non_canceling` → 768; `q115_reuse_out` → 1184; `doll_leaves` → 717.

End nodes: 17: `<omitted>`; 717: `NonTerminating`; 768: `NonTerminating`; 1184: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 57 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnChangeIdleAnimEvent` | 22 | 20 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 153 | 20 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 4 | 509 / 728 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/15` |
| `scnIKEvent` | 8 | 509 / 713 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/1` |
| `scnLookAtEvent` | 103 | 20 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 108 | 20 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 509 / 720 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/8` |
| `scnUnmountEvent` | 4 | 509 / 727 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/14` |
| `scneventsAttachPropToPerformer` | 3 | 267 / 450 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/6` |
| `scneventsAttachPropToWorld` | 2 | 760 / 1091 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/4` |
| `scneventsCameraParamsEvent` | 2 | 699 / 970 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 4 | 509 / 725 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/13` |
| `scneventsSocket` | 71 | 20 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsVFXEvent` | 6 | 267 / 449 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 14
- speech, skeletal_animation, gaze: 7
- speech, skeletal_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, socket_signal: 5
- gaze: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, audio, socket_signal: 3
- speech, audio: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, socket_signal: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, gaze: 1
- speech, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- audio: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `071bedb0f3b6b5cfcce0a24a47f14c7010aa5639720fab4591a927ce66655c49`. Binary SHA-256: `ae66c50534b3fd58ae6f3736f63d4c78cf560105355b24c29351a50e3519cb1c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q112\scenes\q112_11_shotgun.scene" --events
```

