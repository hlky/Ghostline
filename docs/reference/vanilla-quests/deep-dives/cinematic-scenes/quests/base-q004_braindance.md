# The Information: scene presentation

Journal identity: `quests/main_quest/prologue/q004_braindance`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q004_braindance.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\vendors\watson\kabuki\wat_kab_foodshop_02\wat_kab_foodshop_02.scene`

140 graph nodes, 255 edges; 36 event-bearing sections, 206 events; 70 screenplay lines, 14 screenplay options, 5 choice nodes.

Actors: wat_kab_foodshop_02 (actor 0, spawnSet); judy (actor 1, spawnSet); Evelyn (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `Start 1` → 686; `wat_kab_foodshop_02_start` → 95.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 30 | 23 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scnChangeIdleAnimEvent` | 9 | 27 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnDialogLineEvent` | 41 | 19 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 47 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/11` |
| `scnIKEvent` | 2 | 47 / 142 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scnLookAtEvent` | 17 | 23 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/11` |
| `scnPlaySkAnimEvent` | 46 | 23 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnUnmountEvent` | 1 | 47 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/10` |
| `scneventsAttachPropToPerformer` | 5 | 142 / 356 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/3` |
| `scneventsAttachPropToWorld` | 2 | 91 / 299 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/12` |
| `scneventsCameraParamsEvent` | 4 | 47 / 145 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scneventsEquipItemToPerformer` | 2 | 29 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 1 | 47 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/7` |
| `scneventsSocket` | 37 | 23 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 74 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/17` |
| `scneventsUnequipItemFromPerformerByItem` | 4 | 29 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/16` |
| `scneventsVFXEvent` | 3 | 78 / 208 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 9
- speech: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- props_equipment, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- camera: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- skeletal_animation, props_equipment, audio: 1
- props_equipment, vfx: 1
- idle_animation: 1

Raw SHA-256: `b7081becf0458935dde23e62c5cdbf8c1eaaa3bff0c3f26279aa4d8c12e31dd4`. Binary SHA-256: `7aa477e5821d6092a276533211dbd13a93023a3cac2ee2ac61071c7a86a1fa89`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\vendors\watson\kabuki\wat_kab_foodshop_02\wat_kab_foodshop_02.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_01a_bouncer.scene`

118 graph nodes, 148 edges; 25 event-bearing sections, 137 events; 47 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: bouncer_1 (actor 0, community); Johnny (actor 1, spawnSet); lizzies_bouncer_2 (actor 2, community); Player (actor 3, findInContext).

Entries: `exit fluff` → 880; `in` → 300; `in_club_closed` → 1049.

Exits: `exit fluff done` → 882; `clear` → 1302; `out` → 54.

End nodes: 54: `<omitted>`; 882: `NonTerminating`; 1302: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 14 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/5` |
| `scnDialogLineEvent` | 35 | 14 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnLookAtEvent` | 26 | 14 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnPlaySkAnimEvent` | 29 | 14 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scneventsAttachPropToNode` | 1 | 1198 / 661 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/1` |
| `scneventsAttachPropToPerformer` | 3 | 772 / 306 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 1160 / 601 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/0` |
| `scneventsEquipItemToPerformer` | 2 | 1198 / 669 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/4` |
| `scneventsSocket` | 32 | 14 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 1198 / 671 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/6` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 663 / 243 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/1` |
| `scneventsVFXDurationEvent` | 1 | 700 / 258 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- skeletal_animation, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, gaze: 2
- speech, gaze, socket_signal: 1
- socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- props_equipment, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- props_equipment: 1

Raw SHA-256: `d9e8a53cee9d3c212ab9480d5f0dcf9d03444e33306a285536f0124cb4a584bd`. Binary SHA-256: `229e690de1cd02bd17512b7fb1cf4a3e902ffe5fb33c85d2f6d2a831ab3e23fc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_01a_bouncer.scene" --events
```

## `base\quest\main_quests\prologue\q004\lizzies_club\scenes\q004_com_lizzies_scenes.scene`

10 graph nodes, 13 edges; 0 event-bearing sections, 0 events; 0 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: angry_customer (actor 0, community).

Entries: `Start 0` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |

Presentation families coexisting in an event section (counts are sections, not durations):


Raw SHA-256: `4cde5ab8d1de249dfd8ea0eed5f24b32ef045d0eb903fa7679ed2716b6949068`. Binary SHA-256: `12fc571663fed6a015978a6689f15b39cee223b05e2fedf90f8832644e8a3f6f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q004\lizzies_club\scenes\q004_com_lizzies_scenes.scene" --events
```

## `base\quest\main_quests\prologue\q004\scenes\q004_00_lizzies_nightclub_mood_scenes.scene`

47 graph nodes, 44 edges; 7 event-bearing sections, 169 events; 38 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: prostitute_1 (actor 0, community); prostitute_2 (actor 1, community); prostitute_3 (actor 2, community); prostitute_4 (actor 3, community); patron_1 (actor 4, community); patron_2 (actor 5, community); patron_3 (actor 6, community); lizzie_solo (actor 7, community).

Entries: `mood_scene_1` → 4; `mood_scene_2` → 7; `mood_scene_3` → 10; `mood_scene_4` → 13.

Exits: `mood_scene_1_out` → 5; `mood_scene_2_out` → 8; `mood_scene_3_out` → 12; `mood_scene_4_out` → 14.

End nodes: 5: `<omitted>`; 8: `<omitted>`; 12: `<omitted>`; 14: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 9 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnDialogLineEvent` | 37 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 3 | 15 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/45` |
| `scnIKEvent` | 6 | 15 / 214 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/39` |
| `scnLookAtEvent` | 42 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 56 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 3 | 15 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/44` |
| `scneventsSetAnimFeatureEvent` | 3 | 15 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/41` |
| `scneventsSocket` | 17 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `6a00248a598307734c51f559c0c36a73bf51de40342fbc79fbc2b7edffce2ef9`. Binary SHA-256: `8987a546ad0cc1fec0eb1be1b9756dc7ac6e3a7f83e5407e48ef27f4aee88d27`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q004\scenes\q004_00_lizzies_nightclub_mood_scenes.scene" --events
```

## `base\quest\main_quests\prologue\q004\scenes\q004_01_meet_the_lizzies.scene`

157 graph nodes, 244 edges; 29 event-bearing sections, 204 events; 46 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: bouncer_1 (actor 0, community); bouncer_2 (actor 1, community); Player (actor 2, findInContext).

Entries: `lizzies_intro_in` → 1; `lizzies_intro_test` → 1058; `in_club_opened` → 1076; `lizzies_scene_setup` → 1202.

Exits: `lizzies_intro_out` → 2; `lizzies_intro_out_terminating` → 716; `lizzies_intro_left` → 1074; `out_club_opened` → 1081.

End nodes: 2: `NonTerminating`; 716: `<omitted>`; 1074: `<omitted>`; 1081: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 12 | 185 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnDialogLineEvent` | 44 | 161 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/3` |
| `scnGameplayTransitionEvent` | 1 | 363 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scnIKEvent` | 2 | 363 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |
| `scnLookAtEvent` | 36 | 161 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnPlaySkAnimEvent` | 58 | 161 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnUnmountEvent` | 1 | 363 / 169 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 1 | 363 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/5` |
| `scneventsSocket` | 47 | 185 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/7` |
| `scneventsVFXEvent` | 2 | 303 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation: 4
- speech, gaze: 3
- speech, skeletal_animation, gaze: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `7dffcb77295b9854a033a823c2755f76d394f060dff118fd1f00d745c7c13d5a`. Binary SHA-256: `7d0a61373afa7b8c3799d14bd32edcb52104e1695279b7881979ff35600bf2d5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q004\scenes\q004_01_meet_the_lizzies.scene" --events
```

## `base\quest\main_quests\prologue\q004\scenes\q004_02_meeting_evelyn.scene`

345 graph nodes, 450 edges; 96 event-bearing sections, 729 events; 234 screenplay lines, 50 screenplay options, 17 choice nodes.

Actors: Evelyn (actor 0, spawnSet); Mateo (actor 1, spawnSet); Judy (actor 2, spawnSet); holo_dancer (actor 3, spawnDespawn); Player (actor 4, findInContext).

Entries: `q004_04b_after_tutorial_tbug_call_reminder_1_in` → 2587; `q004_02_scene_followup_chat_in` → 1301; `walk_with_ev_prev` → 2611; `stop_on_stairs_prev` → 2642; `Start 6` → 2057; `q004_02_meeting_evelyn_in_test` → 2075; `sitting_with_evelyn` → 2423; `ev_talk_continued` → 2757; `ev_talk_last` → 2766; `ev_smoking` → 2793; `q004_02_meeting_evelyn_in` → 252; `holo_dancer_preview` → 2534; `stop_on_stairs` → 3182; `q004_02_chat_to_judy_in` → 1280.

Exits: `q004_04b_after_tutorial_tbug_call_reminder_1_out` → 2589; `q004_02_scene_followup_chat_out` → 1302; `q004_02_meeting_evelyn_out` → 14; `ev_move_on_spline` → 2785; `obj_loop_vip_room` → 2788; `obj_loop_sit_couch` → 2791; `prepare_judy_out` → 3160; `q004_02_chat_to_judy_out` → 1282.

End nodes: 14: `NonTerminating`; 1282: `<omitted>`; 1302: `NonTerminating`; 2589: `<omitted>`; 2785: `NonTerminating`; 2788: `NonTerminating`; 2791: `NonTerminating`; 3160: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 18 | 832 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnChangeIdleAnimEvent` | 53 | 823 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 172 | 823 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 7 | 832 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/7` |
| `scnIKEvent` | 14 | 832 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnLookAtEvent` | 114 | 826 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 170 | 823 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 2 | 915 / 506 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/8` |
| `scnUnmountEvent` | 7 | 832 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/10` |
| `scneventsAttachPropToNode` | 3 | 1196 / 731 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/43` |
| `scneventsAttachPropToPerformer` | 17 | 824 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsAttachPropToWorld` | 13 | 864 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scneventsCameraParamsEvent` | 4 | 898 / 433 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/1` |
| `scneventsEquipItemToPerformer` | 4 | 1196 / 755 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/58` |
| `scneventsSetAnimFeatureEvent` | 7 | 832 / 142 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/9` |
| `scneventsSocket` | 113 | 823 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsVFXDurationEvent` | 1 | 1196 / 714 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/30` |
| `scneventsVFXEvent` | 10 | 871 / 392 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 13
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze: 5
- gaze: 4
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- skeletal_animation, gaze, socket_signal: 3
- socket_signal: 3
- speech, socket_signal: 2
- speech, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- idle_animation, socket_signal: 2
- speech, props_equipment: 1
- speech, skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, camera, socket_signal: 1
- camera: 1
- props_equipment: 1

Raw SHA-256: `ad1e7f956e9b6989990ddfce066358a4df3f59fcc0478bafe9607995f02fe266`. Binary SHA-256: `ffcd4410566e3d0d05118e93d0305e4a473c7fb4c146c2f04cfa058857b1f207`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q004\scenes\q004_02_meeting_evelyn.scene" --events
```

## `base\quest\main_quests\prologue\q004\scenes\q004_03_this_is_judy.scene`

184 graph nodes, 225 edges; 41 event-bearing sections, 477 events; 83 screenplay lines, 15 screenplay options, 6 choice nodes.

Actors: Evelyn (actor 0, spawnSet); Judy (actor 1, spawnSet); Tbug (actor 2, spawnDespawn); Player (actor 3, findInContext).

Entries: `judy_intro_in` → 1; `judy_attach_device_before_scene_in` → 1123; `sitting_on_bd_chair_preview` → 1150; `calibration_almost_finished_preview` → 1194; `putting_bd_on` → 1444; `judy_preview` → 1205.

Exits: `tut_scene_out` → 35.

End nodes: 35: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 16 | 17 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scnChangeIdleAnimEvent` | 49 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnDialogLineEvent` | 74 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnLookAtEvent` | 114 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnPlaySkAnimEvent` | 121 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsAttachPropToNode` | 1 | 123 / 311 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/15` |
| `scneventsAttachPropToPerformer` | 7 | 123 / 306 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/10` |
| `scneventsAttachPropToWorld` | 4 | 28 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/7` |
| `scneventsCameraParamsEvent` | 5 | 28 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsSocket` | 77 | 3 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |
| `scneventsVFXEvent` | 9 | 3 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech: 5
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation: 2
- skeletal_animation, gaze, audio, socket_signal: 2
- skeletal_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, idle_animation, gaze, audio: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, camera, vfx, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, vfx, socket_signal: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `e31df8f8dd130cdca0cb90aa4a7e774bdea3af93018a4b26283d509f97de71fa`. Binary SHA-256: `8bdd42a9ecacd8d923ffdc807f6107ba878cad79f649bd2f129ec275625b68e3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q004\scenes\q004_03_this_is_judy.scene" --events
```

## `base\quest\main_quests\prologue\q004\scenes\q004_04a_bd_tutorial_robbery.scene`

470 graph nodes, 527 edges; 27 event-bearing sections, 241 events; 77 screenplay lines, 6 screenplay options, 6 choice nodes.

Actors: thug_01 (actor 0, community); thug_02 (actor 1, community); clerk (actor 2, community); evelyn (actor 3, spawnSet); client_02 (actor 4, community); judy (actor 5, findInContext); client_01 (actor 6, community); clerk_02 (actor 7, community); female_pedestrian (actor 8, community); male_pedestrian (actor 9, community); bd_replacer (actor 10, community); bd_vehicle (actor 11, community); V (actor 12, findInContext).

Entries: `preview_scene_only` → 2226; `RID_FPP_ start` → 220; `fpp_robbery_preview` → 2775; `RID_TPP_start` → 842; `old` → 2460.

Exits: `prepare_bd_reaction_scene` → 3038; `BD_DEATH_END` → 562; `BD_FINISH` → 582.

End nodes: 562: `<omitted>`; 582: `NonTerminating`; 3038: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioDurationEvent` | 36 | 1349 / 999 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/28` |
| `scnAudioEvent` | 21 | 675 / 422 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/21` |
| `scnDialogLineEvent` | 66 | 3 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlayRidAnimEvent` | 20 | 675 / 401 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/11` |
| `scnPlaySkAnimEvent` | 52 | 675 / 357 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/0` |
| `scneventsAttachPropToPerformer` | 3 | 675 / 411 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/15` |
| `scneventsBraindanceVisibilityEvent` | 2 | 1349 / 983 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/22` |
| `scneventsCameraParamsEvent` | 1 | 1349 / 921 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/1` |
| `scneventsClueEvent` | 7 | 1349 / 1016 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/45` |
| `scneventsPlayRidCameraAnimEvent` | 6 | 675 / 420 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/19` |
| `scneventsSocket` | 21 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scneventsVFXBraindanceEvent` | 4 | 1349 / 996 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/25` |
| `scneventsVFXEvent` | 2 | 675 / 508 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/63` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, socket_signal: 9
- skeletal_animation, rid_actor, camera, rid_camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, rid_actor, camera, rid_camera, props_equipment, audio, vfx, socket_signal, clues, bd_visibility_ui: 1
- vfx: 1

Raw SHA-256: `7890bfa59f4136ca18e8d4be6b24bbd58c4d08aca55117e2520bb6bab584d2f4`. Binary SHA-256: `92b65623089696326eeccc12f6d1761cf0b03e695a9cdc827ab8a99851d918ca`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q004\scenes\q004_04a_bd_tutorial_robbery.scene" --events
```

## `base\quest\main_quests\prologue\q004\scenes\q004_04b_after_tutorial.scene`

166 graph nodes, 203 edges; 28 event-bearing sections, 351 events; 74 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: Evelyn (actor 0, spawnSet); Judy (actor 1, spawnSet); Tbug (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `bd_first_reaction_in` → 636; `q004_04b_after_tutorial_in` → 39; `holocall` → 1158.

Exits: `bd_first_reaction_out` → 637; `q004_04b_after_tutorial_out` → 242; `tbug_call_reminders` → 1336.

End nodes: 242: `<omitted>`; 637: `<omitted>`; 1336: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 18 | 171 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scnChangeIdleAnimEvent` | 34 | 41 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnDialogLineEvent` | 60 | 41 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scnLookAtEvent` | 76 | 41 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 84 | 41 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scneventsAttachPropToPerformer` | 4 | 41 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsAttachPropToWorld` | 4 | 182 / 197 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/17` |
| `scneventsCameraParamsEvent` | 8 | 41 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsSocket` | 54 | 41 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsVFXEvent` | 9 | 41 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech: 4
- camera: 4
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1

Raw SHA-256: `cf37d6310fcda07f69a3e1c765f462c6aa74e33e52dc3ebda41c287d587cee17`. Binary SHA-256: `c2372774ef8d004fc071b5126848d3963fb4d85c8b0124192e3be7e17b22cb97`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q004\scenes\q004_04b_after_tutorial.scene" --events
```

## `base\quest\main_quests\prologue\q004\scenes\q004_05_bd_yorinobu.scene`

670 graph nodes, 977 edges; 47 event-bearing sections, 342 events; 120 screenplay lines, 37 screenplay options, 37 choice nodes.

Actors: Yorinobu (actor 0, spawnDespawn); Evelyn (actor 1, spawnDespawn); Anders_Hellman (actor 2, spawnDespawn); Tbug (actor 3, findInContext); Smasher (actor 4, spawnDespawn); bd_replacer (actor 5, community); invisible_npc_screen (actor 6, spawnDespawn); invisible_npc_phone (actor 7, spawnDespawn); Player (actor 8, findInContext).

Entries: `recording_only_preview` → 3116; `hellman_scene_preview` → 3146; `functional_test_Preview_in` → 1790; `q004_05_bd_yorinobu_in` → 551.

Exits: `q004_05_bd_yorinobu_out` → 552.

End nodes: 552: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioDurationEvent` | 48 | 1687 / 650 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/31` |
| `scnChangeIdleAnimEvent` | 2 | 1827 / 1272 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/1` |
| `scnDialogLineEvent` | 100 | 289 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnPlayRidAnimEvent` | 23 | 1687 / 575 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/4` |
| `scnPlaySkAnimEvent` | 105 | 1687 / 559 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/0` |
| `scnPlayVideoEvent` | 5 | 696 / 271 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/0` |
| `scneventsAttachPropToPerformer` | 3 | 1687 / 596 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/11` |
| `scneventsAttachPropToWorld` | 1 | 2170 / 1598 | `/Data/RootChunk/sceneGraph/Data/graph/177/Data/events/0` |
| `scneventsBraindanceVisibilityEvent` | 2 | 1687 / 624 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/20` |
| `scneventsCameraParamsEvent` | 2 | 1687 / 595 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/10` |
| `scneventsClueEvent` | 18 | 1687 / 648 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/29` |
| `scneventsPlayRidCameraAnimEvent` | 11 | 1687 / 635 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/21` |
| `scneventsSocket` | 15 | 1687 / 655 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/36` |
| `scneventsUIAnimationBraindanceEvent` | 2 | 1687 / 647 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/28` |
| `scneventsVFXBraindanceEvent` | 4 | 1687 / 813 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/102` |
| `scneventsVFXEvent` | 1 | 1687 / 1074 | `/Data/RootChunk/sceneGraph/Data/graph/107/Data/events/224` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 36
- video: 5
- props_equipment: 2
- speech, skeletal_animation, rid_actor, camera, rid_camera, props_equipment, audio, vfx, socket_signal, clues, bd_visibility_ui: 1
- speech, skeletal_animation, idle_animation: 1
- camera: 1
- skeletal_animation, idle_animation, camera, rid_camera: 1

Raw SHA-256: `96c33c1e799cfa2cbcff397b83d47808ceef61abd452ef6efc0326d7a4439161`. Binary SHA-256: `357c55647bef238e57487242095060b479d3939a5308d8e601b2af77be72795c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q004\scenes\q004_05_bd_yorinobu.scene" --events
```

## `base\quest\main_quests\prologue\q004\scenes\q004_06_see_you_later_evelyn.scene`

187 graph nodes, 225 edges; 38 event-bearing sections, 376 events; 119 screenplay lines, 21 screenplay options, 6 choice nodes.

Actors: Evelyn (actor 0, spawnSet); Judy (actor 1, spawnSet); Tbug (actor 2, spawnSet); Mateo (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `after_bd` → 1; `ending_preview` → 740; `talk_with_ev_prev` → 813; `q004_04b_after_tutorial_tbug_call_reminder_2_in` → 850.

Exits: `wayout_chat_out` → 17; `JudyGoodBye_out` → 36; `q004_04b_after_tutorial_tbug_call_reminder_2_out` → 849.

End nodes: 17: `NonTerminating`; 36: `<omitted>`; 849: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 10 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |
| `scnChangeIdleAnimEvent` | 35 | 2 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 85 | 2 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scnGameplayTransitionEvent` | 2 | 18 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scnIKEvent` | 4 | 18 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnLookAtEvent` | 49 | 2 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnPlaySkAnimEvent` | 85 | 2 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnPoseCorrectionEvent` | 9 | 33 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/18` |
| `scnUnmountEvent` | 2 | 18 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scneventsAttachPropToPerformer` | 4 | 436 / 637 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/10` |
| `scneventsAttachPropToWorld` | 1 | 558 / 788 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/20` |
| `scneventsCameraParamsEvent` | 6 | 33 / 205 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/21` |
| `scneventsSetAnimFeatureEvent` | 2 | 18 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsSocket` | 78 | 2 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsVFXEvent` | 6 | 10 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation: 3
- speech, gaze, socket_signal: 2
- speech: 2
- gaze: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal, animation_state: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, camera, props_equipment, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation: 1
- gaze, camera, vfx: 1

Raw SHA-256: `18c27ece0bb8f458a6aad885e1d929c7a37048c4b1a8a832026daf77efb9c24f`. Binary SHA-256: `9e5036e877234bc37f6f4ade092231522fd27adf7a6fb3cf230dc7052298139b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q004\scenes\q004_06_see_you_later_evelyn.scene" --events
```

## `base\quest\main_quests\prologue\q004\scenes\q004_07_lets_meet_dex.scene`

89 graph nodes, 111 edges; 27 event-bearing sections, 78 events; 65 screenplay lines, 7 screenplay options, 2 choice nodes.

Actors: dex (actor 0, spawnSet); jackie (actor 1, spawnSet); v (actor 2, findInContext).

Entries: `callin_dex` → 1; `q005_01_plan_and_flathead_in` → 416; `dex_holocall_preview` → 421; `linestobereused` → 725.

Exits: `callin_dex_out` → 2; `q005_01_plan_and_flathead_out` → 417.

End nodes: 2: `<omitted>`; 417: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 17 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 62 | 3 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 2 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 7 | 29 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scneventsAttachPropToPerformer` | 1 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraEvent` | 1 | 431 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/0` |
| `scneventsSocket` | 2 | 132 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- speech, skeletal_animation: 4
- speech, idle_animation: 2
- speech, gaze, props_equipment: 1
- idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, socket_signal: 1
- camera: 1

Raw SHA-256: `d38aae843999f93b05302e429c4d03e3bb0f814e041140850ed2270024089804`. Binary SHA-256: `f4d0d54e9a58978be46ca0579059e87266bc8af982fa1abd962bfe76777ab21a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q004\scenes\q004_07_lets_meet_dex.scene" --events
```

