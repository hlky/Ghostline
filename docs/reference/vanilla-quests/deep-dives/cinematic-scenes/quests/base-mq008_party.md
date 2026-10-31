# Stadium Love: scene presentation

Journal identity: `quests/minor_quest/mq008_party`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq008_party.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq008\scenes\mq008_01_party_chats.scene`

39 graph nodes, 50 edges; 3 event-bearing sections, 55 events; 17 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: party_female1 (actor 0, community); party_female2 (actor 1, community); party_female3 (actor 2, community); party_male1 (actor 3, community); party_male2 (actor 4, community); party_male3 (actor 5, community); Fanboy1 (actor 6, community); Fanboy_Join (actor 7, community); 40_arb_Fangirl (actor 8, community); Fanboy2 (actor 9, community).

Entries: `party1_in` → 1; `civ_talk_in` → 98; `fanboy_in` → 77.

Exits: `party1_out` → 2; `End 3` → 174.

End nodes: 2: `<omitted>`; 174: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 7 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 17 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 12 | 7 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scneventsEquipItemToPerformer` | 6 | 7 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scneventsSocket` | 12 | 7 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- speech: 1

Raw SHA-256: `a5ef5e3ebc43b5aa8aedf347f6115acd06e377d5c9b64f9c1aeba0961c60a8b9`. Binary SHA-256: `ae3fc1942478d0b7d251d6bda52ee299397fb0bbc1c20867b12c3dafcd387f3f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq008\scenes\mq008_01_party_chats.scene" --events
```

## `base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene`

606 graph nodes, 709 edges; 84 event-bearing sections, 915 events; 134 screenplay lines, 16 screenplay options, 9 choice nodes.

Actors: representative (actor 0, community); competitor1 (actor 1, community); competitor2 (actor 2, community); competitor3 (actor 3, community); competitor4 (actor 4, community); judge1 (actor 5, community); judge2 (actor 6, community); judge3 (actor 7, community); judge4 (actor 8, community); aggressive_6th (actor 9, community); competitor_scene1 (actor 10, community); female_gun (actor 11, community); Civilian_Judge_1 (actor 12, community); Civilian_Judge_2 (actor 13, community); Civilian_Judge_3 (actor 14, community); Civilian_Judge_4 (actor 15, community); Player (actor 16, findInContext).

Entries: `contest_begin_soon_in` → 1; `rep_ab_contest_in` → 19; `drink_3` → 954; `drink_spot1_in` → 74; `Start 11` → 4307; `rep_count_points_in` → 168; `vfx_end_in` → 1123; `comp_scene2_in` → 280; `drink_2_in` → 788; `drink4` → 841.

Exits: `rep_ab_contest_out` → 20; `no_competition_out` → 57; `shooting3` → 144; `rep_count_points_out` → 169; `vfx_end_out` → 1121; `shooting1` → 697; `shooting2` → 714; `shooting4` → 749; `start_with_combat_out` → 366; `quest_cheated_out` → 1365.

End nodes: 20: `NonTerminating`; 57: `NonTerminating`; 144: `NonTerminating`; 169: `NonTerminating`; 366: `<omitted>`; 697: `NonTerminating`; 714: `NonTerminating`; 749: `NonTerminating`; 1121: `<omitted>`; 1365: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 498 / 1708 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/1` |
| `scnChangeIdleAnimEvent` | 85 | 25 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scnDialogLineEvent` | 114 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 70 / 263 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/9` |
| `scnIKEvent` | 10 | 70 / 260 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/6` |
| `scnLookAtEvent` | 180 | 25 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnPlaySkAnimEvent` | 244 | 25 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnPoseCorrectionEvent` | 9 | 33 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/27` |
| `scnUnmountEvent` | 5 | 70 / 262 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/8` |
| `scneventsAttachPropToPerformer` | 4 | 498 / 1709 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/2` |
| `scneventsAttachPropToWorld` | 6 | 29 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/10` |
| `scneventsEquipItemToPerformer` | 19 | 85 / 305 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 5 | 70 / 257 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/4` |
| `scneventsSocket` | 183 | 25 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/14` |
| `scneventsSpawnEntityEvent` | 2 | 29 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/11` |
| `scneventsUnequipItemFromPerformer` | 13 | 29 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/9` |
| `scneventsUnequipItemFromPerformerByItem` | 8 | 161 / 536 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/16` |
| `scneventsVFXDurationEvent` | 4 | 766 / 2252 | `/Data/RootChunk/sceneGraph/Data/graph/188/Data/events/6` |
| `scneventsVFXEvent` | 15 | 170 / 557 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 9
- speech: 8
- socket_signal: 7
- speech, skeletal_animation, gaze, socket_signal: 6
- speech, skeletal_animation: 5
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 4
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 4
- skeletal_animation, props_equipment, socket_signal: 4
- skeletal_animation, props_equipment, audio, vfx: 3
- skeletal_animation, socket_signal: 3
- vfx: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, entity_lifecycle: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `c9248226689bd82784bad50b09d28e45c9f30e2e4a72212957a37662f072436b`. Binary SHA-256: `03a7ee9ddbe0029c1196e42235e4be8961d843bd027e18cedae45c8b026956c2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq008\scenes\mq008_02_shooting_contest.scene" --events
```

## `base\quest\side_quests\sq023\scenes\sq023_04_glorias_house.scene`

535 graph nodes, 742 edges; 95 event-bearing sections, 935 events; 181 screenplay lines, 35 screenplay options, 17 choice nodes.

Actors: Gloria (actor 0, spawnSet); Rachel (actor 1, spawnSet); Joshua (actor 2, spawnSet); Vasquez (actor 3, spawnSet); Zuleikha (actor 4, spawnSet); Johnny (actor 5, spawnDespawn); Emperor (actor 6, spawnSet); V (actor 7, findInContext).

Entries: `porch_in` → 1; `test2` → 4680; `rach_stays_in` → 552; `Start 9` → 5219; `Start 10` → 5223; `Start 11` → 5227; `Start 7` → 1918; `Start 12` → 5231.

Exits: `mariah_talk_out_end` → 415; `quest_failed_out` → 2970; `End 11` → 5062; `End 12` → 5078; `End 13` → 5093; `rach_stays_out` → 553; `End 14` → 5111; `mariah_talk_out` → 381.

End nodes: 381: `NonTerminating`; 415: `NonTerminating`; 553: `<omitted>`; 2970: `<omitted>`; 5062: `NonTerminating`; 5078: `NonTerminating`; 5093: `NonTerminating`; 5111: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 715 / 1125 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/3` |
| `scnChangeIdleAnimEvent` | 78 | 372 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 142 | 372 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scnGameplayActionEvent` | 2 | 3447 / 3187 | `/Data/RootChunk/sceneGraph/Data/graph/403/Data/events/2` |
| `scnGameplayTransitionEvent` | 8 | 738 / 1164 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/19` |
| `scnIKEvent` | 20 | 738 / 1135 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/3` |
| `scnLookAtEvent` | 241 | 372 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnPlaySkAnimEvent` | 144 | 372 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPoseCorrectionEvent` | 4 | 372 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/17` |
| `scnUnmountEvent` | 8 | 738 / 1165 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/20` |
| `scneventsAttachPropToPerformer` | 8 | 385 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/22` |
| `scneventsAttachPropToWorld` | 11 | 449 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/6` |
| `scneventsEquipItemToPerformer` | 1 | 3447 / 3191 | `/Data/RootChunk/sceneGraph/Data/graph/403/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 17 | 738 / 1162 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/18` |
| `scneventsSocket` | 236 | 372 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 3455 / 3221 | `/Data/RootChunk/sceneGraph/Data/graph/406/Data/events/5` |
| `scneventsVFXEvent` | 2 | 539 / 924 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 13
- speech: 10
- gaze: 10
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 8
- skeletal_animation, gaze, socket_signal: 7
- speech, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal, animation_state, gameplay_action: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, audio, socket_signal, animation_state: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, audio: 1
- skeletal_animation, socket_signal, animation_state: 1
- speech, idle_animation: 1
- skeletal_animation, props_equipment, socket_signal: 1
- idle_animation, gaze: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, socket_signal, animation_state: 1
- speech, idle_animation, socket_signal: 1

Raw SHA-256: `f59db831a0805dbdbca3112fc7be04a5a6847f84c89476e73bb2e2c627f13dcc`. Binary SHA-256: `d847e40b8967ffc3faaa6d15313999639b93445fada6337e4e51c807b4235127`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq023\scenes\sq023_04_glorias_house.scene" --events
```

