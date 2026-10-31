# Sweet Dreams: scene presentation

Journal identity: `quests/minor_quest/mq036_overload`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq036_overload.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq036\scenes\mq036_scavengers.scene`

54 graph nodes, 45 edges; 5 event-bearing sections, 51 events; 15 screenplay lines, 3 screenplay options, 3 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Scav_01 (actor 1, community); Scav_02 (actor 2, community); Scav_03 (actor 3, community); Scav_04 (actor 4, community); Player (actor 5, findInContext).

Entries: `waking_up_in` → 1; `pc1_hack_in` → 6; `gear_loot_in` → 11; `pc2_hack_in` → 16; `sucker_in` → 22; `payback_in` → 26; `scav_chat_1_in` → 31; `scav_chat_2_in` → 36; `elevator_in` → 1048.

Exits: `waking_up_out` → 2; `pc1_hack_out` → 7; `gear_loot_out` → 12; `waking_up_johnny_out` → 110; `pc2_hack_out` → 17; `sucker_out` → 23; `payback_johnny_out` → 121; `payback_out` → 27; `scav_chat_1_out` → 32; `sucker_johnny_out` → 129; `scav_chat_2_out` → 37; `elevator_out` → 1055.

End nodes: 2: `NonTerminating`; 7: `<omitted>`; 12: `<omitted>`; 17: `<omitted>`; 23: `NonTerminating`; 27: `NonTerminating`; 32: `<omitted>`; 37: `<omitted>`; 110: `<omitted>`; 121: `<omitted>`; 129: `<omitted>`; 1055: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 3 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scnChangeIdleAnimEvent` | 2 | 3 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 15 | 3 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnGameplayTransitionEvent` | 1 | 3 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/28` |
| `scnIKEvent` | 2 | 3 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/25` |
| `scnLookAtEvent` | 3 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 10 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnUnmountEvent` | 1 | 3 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/32` |
| `scneventsSetAnimFeatureEvent` | 1 | 3 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/29` |
| `scneventsSocket` | 9 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 5 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `c55e92a336ba6c46cc5722a9816b6c83dfd29f28c84e065f230a628cfecfe1d7`. Binary SHA-256: `4b28d9a78e352e73198a318a9833401de725da4b4de8f1366631b3c9ca69ed55`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq036\scenes\mq036_scavengers.scene" --events
```

## `base\quest\minor_quests\mq036\scenes\mq036_stefan_dialogues.scene`

118 graph nodes, 133 edges; 24 event-bearing sections, 204 events; 59 screenplay lines, 15 screenplay options, 8 choice nodes.

Actors: Stefan (actor 0, community); Player (actor 1, findInContext).

Entries: `hook_intro_in` → 1; `hook_loop_in` → 7; `didnt_play_bd_in` → 442; `deal_start_in` → 21; `deal_dial_in` → 43; `temp_play_bd_in` → 45; `bd_reaction_in` → 50; `preview` → 370; `stefans_place_in` → 70; `complaint_dial_in` → 77; `confront_in` → 84.

Exits: `hook_intro_out` → 2; `hook_loop_out` → 8; `deal_buy_out` → 22; `deal_pass_out` → 38; `deal_start_out` → 41; `temp_play_bd_out` → 46; `money_back_out_non_terminating` → 364; `bd_reaction_out` → 51; `stefan_kill_out` → 383; `follow_stefan_out` → 66; `money_back_out` → 68; `use_player_out` → 80; `stefan_forgive_out` → 85; `stefan_banish_out` → 420.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 22: `<omitted>`; 38: `<omitted>`; 41: `<omitted>`; 46: `<omitted>`; 51: `<omitted>`; 66: `NonTerminating`; 68: `<omitted>`; 80: `<omitted>`; 85: `<omitted>`; 364: `NonTerminating`; 383: `<omitted>`; 420: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 161 / 507 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/2` |
| `scnChangeIdleAnimEvent` | 14 | 33 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/7` |
| `scnDialogLineEvent` | 57 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 62 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/15` |
| `scnIKEvent` | 4 | 62 / 174 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/10` |
| `scnLookAtEvent` | 19 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 68 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 2 | 62 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/14` |
| `scneventsAttachPropToPerformer` | 2 | 161 / 506 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 2 | 62 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/13` |
| `scneventsSocket` | 19 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 14 | 33 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 4
- speech, gaze: 3
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 1
- speech, skeletal_animation: 1
- speech: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `125f3880ed66261329e05f14da7e41a1de9cfbb14d875ba6c69d7307cd9fcaed`. Binary SHA-256: `1c712e8ff01fdc46a942fb99622a0ee6f2f2096bfb780a897577bbfa7f670dce`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq036\scenes\mq036_stefan_dialogues.scene" --events
```

