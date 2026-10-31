# Raymond Chandler Evening: scene presentation

Journal identity: `quests/minor_quest/mq040_biosculpt`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq040_biosculpt.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq040\scenes\mq040_01_bar.scene`

185 graph nodes, 236 edges; 35 event-bearing sections, 309 events; 80 screenplay lines, 20 screenplay options, 6 choice nodes.

Actors: Corpo (actor 0, community); Valentino_01 (actor 1, community); Valentino_02 (actor 2, community); El_Coyote_Barman (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `bar_encounter_in` → 1; `Start 9` → 527; `fight_won` → 389.

Exits: `fight_out` → 35; `didnt_help_corpo_out` → 37; `bar_encounter_out` → 47; `refused_quest` → 113.

End nodes: 35: `NonTerminating`; 37: `<omitted>`; 47: `NonTerminating`; 113: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 26 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/23` |
| `scnChangeIdleAnimEvent` | 17 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnDialogLineEvent` | 75 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnGameplayTransitionEvent` | 5 | 26 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/33` |
| `scnIKEvent` | 10 | 26 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/28` |
| `scnLookAtEvent` | 59 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 54 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnUnmountEvent` | 5 | 26 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/36` |
| `scneventsAttachPropToPerformer` | 2 | 219 / 512 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/9` |
| `scneventsAttachPropToWorld` | 2 | 219 / 517 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 5 | 26 / 154 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/34` |
| `scneventsSocket` | 63 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsVFXEvent` | 10 | 60 / 239 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/21` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, idle_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, socket_signal: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `27d0ab7aaac2d4bde3a1b013f6f1a00176c419a1e2ff196a235f5641c12fb0b2`. Binary SHA-256: `b8fdf591f639b9d1ddb9e404dae9c6f15006358d7c71b175b250f9ddc53e89a3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq040\scenes\mq040_01_bar.scene" --events
```

## `base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene`

111 graph nodes, 111 edges; 15 event-bearing sections, 101 events; 31 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Wife (actor 1, community); Homeless_bum_mood (actor 2, community); Johnny_voice (actor 3, findInContext); V (actor 4, findInContext).

Entries: `arrival_in` → 1; `decoy_fluff_01` → 7; `decoy_fluff_02` → 9; `wife_scanned` → 11; `distance_warning_large` → 22; `distance_warning_mid` → 24; `distance_warning_final` → 25; `trail_mood_01` → 39; `trail_mood_02` → 41; `wrong_time` → 55; `bar_exit` → 72.

Exits: `arrival_out` → 2; `decoy_fluff_01_out` → 8; `decoy_fluff_02_out` → 10; `wife_scanned_out` → 12; `End 13` → 405; `End 14` → 411; `distance_warning_large_out` → 23; `distance_warning_mid_out` → 26; `distance_warning_final_out` → 27; `End 9` → 329; `trail_mood_01_out` → 40; `trail_mood_02_out` → 42; `wrong_time_out` → 56; `End 17` → 558; `End 18` → 560; `bar_exit_out` → 73; `End 11` → 369; `End 12` → 370.

End nodes: 2: `NonTerminating`; 8: `NonTerminating`; 10: `NonTerminating`; 12: `NonTerminating`; 23: `<omitted>`; 26: `<omitted>`; 27: `<omitted>`; 40: `NonTerminating`; 42: `NonTerminating`; 56: `<omitted>`; 73: `NonTerminating`; 329: `<omitted>`; 369: `<omitted>`; 370: `<omitted>`; 405: `<omitted>`; 411: `<omitted>`; 558: `<omitted>`; 560: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 31 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 15 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/8` |
| `scnIKEvent` | 2 | 15 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/5` |
| `scnLookAtEvent` | 25 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 14 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 15 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 1 | 15 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/9` |
| `scneventsSocket` | 18 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation, socket_signal: 2
- speech, gaze: 2
- speech: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `72dc8725d4966b3e72b7d4d1ab9c102383720ff7755140efa3468679e0cc2f5a`. Binary SHA-256: `9049f7a81b8d459846dbdb70d40f724005b65ae3c1174338b0a4a3092a7f870a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq040\scenes\mq040_02_trail_wife.scene" --events
```

## `base\quest\minor_quests\mq040\scenes\mq040_03_ripperdoc.scene`

137 graph nodes, 144 edges; 27 event-bearing sections, 257 events; 75 screenplay lines, 11 screenplay options, 5 choice nodes.

Actors: Corpo (actor 0, community); Wife (actor 1, community); Ripperdoc (actor 2, community); Johnny (actor 3, spawnDespawn); El_Coyote_Barman (actor 4, spawnSet); Johnny_voice (actor 5, findInContext); Wife_phonecall (actor 6, spawnSet); V (actor 7, findInContext).

Entries: `confront_wife` → 12; `report_findings` → 33; `Start 12` → 530; `wife_follow_up_thankful` → 150; `wife_follow_up_distraught` → 152.

Exits: `confront_wife_out` → 13; `wife_follow_up_thankful_out` → 151; `wife_follow_up_distraught_out` → 153; `report_findings_out` → 160.

End nodes: 13: `NonTerminating`; 151: `<omitted>`; 153: `<omitted>`; 160: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 14 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnDialogLineEvent` | 70 | 4 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 38 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/33` |
| `scnIKEvent` | 6 | 38 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/27` |
| `scnLookAtEvent` | 49 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnPlaySkAnimEvent` | 46 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnUnmountEvent` | 3 | 38 / 139 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/35` |
| `scneventsEquipItemToPerformer` | 8 | 40 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/19` |
| `scneventsSetAnimFeatureEvent` | 3 | 38 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/31` |
| `scneventsSocket` | 49 | 4 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 2 | 574 / 768 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/5` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 40 / 205 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/24` |
| `scneventsVFXEvent` | 2 | 40 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, gaze: 6
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation: 1
- gaze, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `8f33c6c3c5e32eb376cb336afbf0360c2664072d2d1282756b9439b83a290e89`. Binary SHA-256: `4500ac580c486baadd8d627eb83afe7d4e98e1b4fa8c6490ceadd42c36870432`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq040\scenes\mq040_03_ripperdoc.scene" --events
```

