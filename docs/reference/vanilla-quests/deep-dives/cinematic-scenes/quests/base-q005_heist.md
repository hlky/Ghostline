# The Heist: scene presentation

Journal identity: `quests/main_quest/prologue/q005_heist`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q005_heist.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q103\scenes\q103_02_afterlife_intro.scene`

34 graph nodes, 36 edges; 7 event-bearing sections, 27 events; 9 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: bouncer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `emmerick_entrance` → 440.

Exits: `End 0` → 2; `emmerick_entrance_out` → 449; `End_killer` → 504.

End nodes: 2: `NonTerminating`; 449: `<omitted>`; 504: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 346 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnLookAtEvent` | 7 | 346 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnPlaySkAnimEvent` | 5 | 346 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnPoseCorrectionEvent` | 1 | 424 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scneventsSocket` | 10 | 346 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- gaze, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `746913e5e8c2ad7bb9a669d85065438703c51835bd0242ebf6ace1e7504bb1c4`. Binary SHA-256: `3e8922e4a45d9f2c542be1489e6e558dea1aaeb4bcc19a7439c6446f81832587`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_02_afterlife_intro.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_01_plan.scene`

358 graph nodes, 502 edges; 79 event-bearing sections, 1142 events; 192 screenplay lines, 34 screenplay options, 15 choice nodes.

Actors: Jackie (actor 0, spawnSet); Dex (actor 1, spawnSet); TBug (actor 2, spawnSet); Dex_Bodyguard (actor 3, spawnSet); Emmerick (actor 4, spawnSet); Panam (actor 5, spawnSet); Rogue (actor 6, spawnSet); spiderbot (actor 7, community); V (actor 8, findInContext).

Entries: `briefing_in` → 1223; `preview` → 3970; `preview_02` → 4008; `ride_to_hotel` → 3312; `walk_from_bodyguard` → 9628; `script` → 4084.

Exits: `briefing_out` → 851; `looting_disguise` → 4531.

End nodes: 851: `NonTerminating`; 4531: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 17 | 2593 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnChangeIdleAnimEvent` | 51 | 2594 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnDialogLineEvent` | 169 | 2593 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnGameplayTransitionEvent` | 4 | 2593 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/20` |
| `scnIKEvent` | 8 | 2593 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 489 | 2593 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 211 | 2593 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 6 | 2594 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/16` |
| `scnUnmountEvent` | 4 | 2593 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/19` |
| `scneventsAttachPropToNode` | 2 | 2593 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/30` |
| `scneventsAttachPropToPerformer` | 6 | 2593 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scneventsCameraParamsEvent` | 2 | 2725 / 224 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 4 | 2593 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/16` |
| `scneventsSocket` | 160 | 2593 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsVFXDurationEvent` | 1 | 2846 / 754 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/2` |
| `scneventsVFXEvent` | 8 | 2725 / 267 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/41` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 16
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 12
- speech, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 4
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, gaze: 3
- speech, gaze: 3
- socket_signal: 3
- speech: 3
- speech, gaze, audio, socket_signal: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- camera: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `84f045b110b0d96c287602aa8028e4d9ca04871fa9eb4d746663062f60842055`. Binary SHA-256: `a7594ccc43cf7e26a703e11f5d8a81c897ef9f46233af210be627a4427612280`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_01_plan.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_01a_slice_of_afterlife.scene`

513 graph nodes, 665 edges; 125 event-bearing sections, 1141 events; 248 screenplay lines, 30 screenplay options, 17 choice nodes.

Actors: claire (actor 0, spawnSet); jackie (actor 1, spawnSet); weyland (actor 2, spawnSet); weyland_companion_m (actor 3, community); 8ug8ear (actor 4, findInWorld); 6_street_guy (actor 5, findInWorld); goon_01 (actor 6, community); goon_02 (actor 7, community); drinker_merc_01 (actor 8, community); drinker_merc_02 (actor 9, community); angry_merc (actor 10, community); desperate_corpo (actor 11, community); dex_bodyguard (actor 12, spawnSet); emmerick (actor 13, spawnSet); panam (actor 14, spawnSet); rogue (actor 15, spawnSet); nash (actor 16, community); V (actor 17, findInContext).

Entries: `q005_01a_weyland_in` → 7; `CYB-658964_retrofix_in` → 3056; `Start 31` → 3064; `q005_01a_rogue_scene_in` → 398; `q005_01a_panam_scene_in` → 403; `q005_01a_claire_chat_in` → 22; `q005_01a_merc_corpo_in` → 37; `q005_01a_drinkers_in` → 42; `pre_afterlife_in` → 1615; `Start 27` → 2799; `afterlife_bouncer_in` → 172; `afterlife_reaction_in` → 177; `q005_01a_back_to_nc_in` → 969; `afterlife_bouncer_oneliner_in` → 973; `preview_jackie` → 1738; `preview_by_the_bar` → 2888; `Preview_01` → 1380; `begin_preview` → 1782; `Start 29` → 2927; `q005_01a_bodyguard_arrives_in` → 263; `q005_01a_political_comment_in` → 688; `Start 24` → 1857.

Exits: `q005_01a_weyland_out` → 8; `q005_01a_panam_scene_out` → 404; `q005_01a_merc_corpo_out` → 39; `q005_01a_drinkers_out` → 44; `q005_01a_rogue_scene_out` → 1190; `afterlife_bouncer_out` → 173; `q005_01a_back_to_nc_out` → 970; `q005_01a_bodyguard_arrives_out` → 261; `q005_01a_political_comment_out` → 690; `rogue_mood_scene` → 2231; `End 20` → 1859.

End nodes: 8: `<omitted>`; 39: `<omitted>`; 44: `<omitted>`; 173: `NonTerminating`; 261: `<omitted>`; 404: `NonTerminating`; 690: `<omitted>`; 970: `<omitted>`; 1190: `NonTerminating`; 1859: `<omitted>`; 2231: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 4. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 472 / 925 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/7` |
| `scnChangeIdleAnimEvent` | 74 | 9 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 198 | 9 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 12 | 43 / 189 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/33` |
| `scnIKEvent` | 24 | 43 / 186 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/30` |
| `scnLookAtEvent` | 292 | 9 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 240 | 9 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 1 | 1319 / 2033 | `/Data/RootChunk/sceneGraph/Data/graph/181/Data/events/2` |
| `scnUnmountEvent` | 12 | 43 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/32` |
| `scneventsAttachPropToPerformer` | 17 | 164 / 374 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/7` |
| `scneventsAttachPropToWorld` | 15 | 472 / 965 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/32` |
| `scneventsCameraParamsEvent` | 4 | 503 / 1058 | `/Data/RootChunk/sceneGraph/Data/graph/73/Data/events/20` |
| `scneventsSetAnimFeatureEvent` | 12 | 43 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/28` |
| `scneventsSocket` | 211 | 9 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsUnequipItemFromPerformer` | 2 | 1559 / 2661 | `/Data/RootChunk/sceneGraph/Data/graph/248/Data/events/8` |
| `scneventsVFXEvent` | 20 | 219 / 457 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 17
- speech: 17
- gaze: 13
- speech, gaze: 10
- skeletal_animation, socket_signal: 10
- speech, skeletal_animation, gaze, socket_signal: 7
- skeletal_animation, gaze, socket_signal: 5
- socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- camera: 1
- idle_animation, socket_signal: 1

Raw SHA-256: `d03c27b74cd303d21f3c5460677c155b1951454983f9196b51fe80d5d3370114`. Binary SHA-256: `f743a2ad776177d42da7b2c8bec43c9583e02e396c75101d716a789f5a6bce72`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_01a_slice_of_afterlife.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_02_cab_ride.scene`

315 graph nodes, 380 edges; 63 event-bearing sections, 465 events; 122 screenplay lines, 18 screenplay options, 13 choice nodes.

Actors: Jackie (actor 0, spawnSet); Delamain (actor 1, spawnSet); TBug (actor 2, findInContext); Emmerick (actor 3, spawnSet); delamain_vehicle (actor 4, spawnSet); V (actor 5, findInContext).

Entries: `q005_02_cab_ride_in` → 6; `Start 18` → 4209; `Start 16` → 3073; `Start 14` → 2556; `loot_disguise_reminder_in` → 1399; `equip_disguise_reminder_in` → 1404; `Start 17` → 4071; `preview_e3_finale` → 2895.

Exits: `q005_02_cab_v_out` → 2445; `q005_02_cab_NEW_out` → 202; `loot_disguise_reminder_out` → 1400; `equip_disguise_reminder_out` → 1405.

End nodes: 202: `<omitted>`; 1400: `<omitted>`; 1405: `<omitted>`; 2445: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 26 | 1292 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnChangeIdleAnimEvent` | 49 | 1292 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnDialogLineEvent` | 100 | 1177 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 5 | 1896 / 760 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/3` |
| `scnGameplayTransitionEvent` | 2 | 2239 / 1183 | `/Data/RootChunk/sceneGraph/Data/graph/142/Data/events/12` |
| `scnIKEvent` | 6 | 1537 / 253 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/5` |
| `scnLookAtEvent` | 92 | 1292 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 2896 / 1727 | `/Data/RootChunk/sceneGraph/Data/graph/212/Data/events/3` |
| `scnPlaySkAnimEvent` | 85 | 1292 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 2 | 2239 / 1188 | `/Data/RootChunk/sceneGraph/Data/graph/142/Data/events/16` |
| `scneventsAttachPropToPerformer` | 1 | 1292 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 22 | 1517 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |
| `scneventsSocket` | 66 | 1292 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scneventsVFXDurationEvent` | 1 | 1556 / 272 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/0` |
| `scneventsVFXEvent` | 7 | 1526 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 10
- speech: 8
- speech, gaze: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, idle_animation, gaze, socket_signal: 2
- idle_animation, gameplay_action: 2
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 1
- skeletal_animation, ik, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, gaze, vfx: 1
- speech, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze: 1
- gaze, socket_signal: 1
- socket_signal, animation_state, mount_workspot: 1
- gaze: 1
- vfx, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation: 1

Raw SHA-256: `8138ace5a22f792bdf7a6576077a48ca8366659045335ffc8fabb6983113542f`. Binary SHA-256: `9d7b3aa3ea62f842e291755505f29faaf12034fa583a63ec9a2ebc1f82d2a926`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_02_cab_ride.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_03_entrance.scene`

326 graph nodes, 386 edges; 68 event-bearing sections, 506 events; 124 screenplay lines, 10 screenplay options, 6 choice nodes.

Actors: Jackie (actor 0, spawnSet); T-Bug (actor 1, spawnSet); Receptionist (actor 2, community); Security_gate_guard_01 (actor 3, community); Concierge (actor 4, community); Security_gate_guard_02 (actor 5, community); Receptionist_02 (actor 6, community); hotel_guest (actor 7, spawnDespawn); Waitress_01 (actor 8, community); leaving_female (actor 9, community); Doorman (actor 10, community); Delamain (actor 11, spawnSet); V (actor 12, findInContext).

Entries: `q005_03_looks_chat_in` → 1193; `preview_by_gate` → 2130; `q005_entrance_reminders` → 4211; `v_to_restaurant_alone_in` → 4228; `reception_done_in` → 1593; `arrived_in` → 1032; `sec_gates_in` → 1037; `player_inside_reception_booth_in` → 1650; `jackie_by_the_room_in` → 1654; `close_to_the_room_with_jackie_in` → 1659; `jackie_wait_a_in` → 1070; `jackie_wait_b_in` → 1084; `preview_reception` → 1996.

Exits: `v_to_restaurant_alone_out` → 4250; `arrived_out` → 1033; `sec_gates_out` → 1038; `player_inside_reception_booth_out` → 1652; `jackie_by_the_room_out` → 1655; `close_to_the_room_with_jackie_out` → 1660; `jackie_wait_a_out` → 1071; `q005_bar_out` → 2264; `jackie_wait_b_out` → 1085; `q005_elevator_talk_out` → 4056; `q005_elevator_arrived` → 4058.

End nodes: 1033: `<omitted>`; 1038: `NonTerminating`; 1071: `<omitted>`; 1085: `<omitted>`; 1652: `<omitted>`; 1655: `NonTerminating`; 1660: `<omitted>`; 2264: `NonTerminating`; 4056: `NonTerminating`; 4058: `NonTerminating`; 4250: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 4. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 1404 / 414 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/11` |
| `scnChangeIdleAnimEvent` | 21 | 1029 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnDialogLineEvent` | 94 | 1029 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnGameplayTransitionEvent` | 7 | 1404 / 451 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/31` |
| `scnIKEvent` | 14 | 1404 / 430 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/17` |
| `scnLookAtEvent` | 186 | 1029 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnPlaySkAnimEvent` | 77 | 1029 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnUnmountEvent` | 7 | 1404 / 450 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/30` |
| `scneventsAttachPropToNode` | 1 | 2142 / 1152 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/1` |
| `scneventsAttachPropToPerformer` | 1 | 2117 / 1114 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/10` |
| `scneventsEquipItemToPerformer` | 2 | 2117 / 1110 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 7 | 1404 / 447 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/28` |
| `scneventsSocket` | 77 | 1029 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/25` |
| `scneventsVFXEvent` | 7 | 1116 / 189 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- skeletal_animation, gaze, socket_signal: 7
- speech, skeletal_animation, gaze, socket_signal: 6
- speech, gaze: 6
- gaze: 6
- speech, skeletal_animation, gaze: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze, socket_signal: 2
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- speech, skeletal_animation, audio, vfx: 1
- skeletal_animation, idle_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- speech, skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `93584c0bdd3cd171a510628e3a292b42a404df40e813382932af078231ef7626`. Binary SHA-256: `45ade82e630f637e96901087c8652a1e105d551e6f08027e0890dd54ee86f677`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_03_entrance.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_04_spiderbot.scene`

584 graph nodes, 695 edges; 93 event-bearing sections, 566 events; 240 screenplay lines, 28 screenplay options, 19 choice nodes.

Actors: Jackie (actor 0, spawnSet); spiderbot (actor 1, community); TBug (actor 2, spawnSet); Yorinobu (actor 3, findInContext); Maid_01 (actor 4, community); Maid_02 (actor 5, community); Deputy_mayor (actor 6, community); Arasaka_representative (actor 7, community); Arasaka_assistant (actor 8, community); Security_chief (actor 9, community); Sec_room_guard_01 (actor 10, community); Mayor_Rhyne (actor 11, community); tpp_v_male (actor 12, spawnDespawn); tpp_v_female (actor 13, spawnDespawn); V (actor 14, findInContext).

Entries: `room_a_reached_in` → 1221; `room_b_reached_in` → 1226; `sec_room_reached_in` → 1231; `audio_test` → 2427; `cart_pushed_in` → 1241; `sec_cam_found_in` → 1256; `tbug_calls_in` → 1273; `flathead_prep_in` → 731; `flathead_done_in` → 790; `room_a_mid_grate_used_in` → 1434; `old` → 2045; `cctv_access_found_a_in` → 1472; `to_node_room_in` → 1478; `find_cctv_access_in` → 1491; `cam_found_react_a_in` → 1497; `cam_found_react_b_in` → 1499; `cctv_already_done_in` → 1505; `cam_already_found_in` → 1510; `cctv_access_already_found_in` → 1515; `q005_04_luring_in` → 923; `start_spiderbot_in` → 928; `room_a_maid_in_way_in` → 2157; `tech_shaft_in` → 2956.

Exits: `netrunner_hacked_out` → 1202; `room_a_reached_out` → 1222; `cart_pushed_out` → 1242; `sec_cam_found_out` → 1257; `tbug_calls_out` → 1274; `flathead_prep_out` → 732; `flathead_done_out` → 791; `room_b_done_out` → 1427; `room_a_mid_grate_used_out` → 1435; `cctv_access_found_a_out` → 1473; `to_node_room_out` → 1479; `find_cctv_access_out` → 1492; `cam_found_react_a_out` → 1498; `cam_found_react_b_out` → 1500; `cctv_already_done_out` → 1506; `cam_already_found_out` → 1511; `cctv_access_already_found_out` → 1517; `q005_04_luring_out` → 925; `start_spiderbot_out` → 931; `room_a_exit_grate_entered` → 2153; `killing_scene` → 4563; `tech_shaft_out` → 2957.

End nodes: 732: `NonTerminating`; 791: `NonTerminating`; 925: `<omitted>`; 931: `NonTerminating`; 1202: `<omitted>`; 1222: `<omitted>`; 1242: `<omitted>`; 1257: `<omitted>`; 1274: `<omitted>`; 1427: `NonTerminating`; 1435: `<omitted>`; 1473: `<omitted>`; 1479: `<omitted>`; 1492: `<omitted>`; 1498: `<omitted>`; 1500: `<omitted>`; 1506: `<omitted>`; 1511: `<omitted>`; 1517: `<omitted>`; 2153: `<omitted>`; 2957: `<omitted>`; 4563: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 809 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/6` |
| `scnChangeIdleAnimEvent` | 63 | 754 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnDialogLineEvent` | 202 | 754 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnGameplayTransitionEvent` | 4 | 1441 / 593 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/25` |
| `scnIKEvent` | 8 | 1441 / 578 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/15` |
| `scnLookAtEvent` | 57 | 754 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnPlaySkAnimEvent` | 93 | 754 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/7` |
| `scnUnmountEvent` | 4 | 1441 / 592 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/24` |
| `scneventsAttachPropToNode` | 1 | 1958 / 1160 | `/Data/RootChunk/sceneGraph/Data/graph/163/Data/events/12` |
| `scneventsAttachPropToPerformer` | 3 | 906 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/8` |
| `scneventsAttachPropToWorld` | 2 | 906 / 173 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/17` |
| `scneventsSetAnimFeatureEvent` | 4 | 1441 / 588 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/21` |
| `scneventsSocket` | 107 | 754 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1441 / 570 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/11` |
| `scneventsVFXEvent` | 9 | 906 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 43
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- skeletal_animation, idle_animation, socket_signal: 6
- skeletal_animation, idle_animation: 5
- speech, skeletal_animation, idle_animation, socket_signal: 4
- skeletal_animation, socket_signal: 4
- speech, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1

Raw SHA-256: `16bb382df335cf1ffd84d7d06d0495456e8f9a0569bf983fe966be19c0d52c1b`. Binary SHA-256: `cdd03ce82fc5178739c622244ba4616348d9071dc93cd743542a36a3a4ae9379`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_04_spiderbot.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_05_hotel_fluff.scene`

192 graph nodes, 211 edges; 49 event-bearing sections, 552 events; 182 screenplay lines, 16 screenplay options, 7 choice nodes.

Actors: Jackie (actor 0, spawnSet); Schettino (actor 1, community); Akulov (actor 2, community); Nadezhda (actor 3, community); Doorman (actor 4, community); Escort_01 (actor 5, community); Escort_02 (actor 6, community); Zen_corpo_01 (actor 7, community); Zen_corpo_02 (actor 8, community); Zen_mother (actor 9, community); Waitress_01 (actor 10, community); guard_lobby_01 (actor 11, community); guard_lobby_02 (actor 12, community); Concierge_02 (actor 13, community); Schettino_friend (actor 14, community); schettino_escort (actor 15, community); Bartender_03 (actor 16, community); Bar_corpo_f_01 (actor 17, community); Bar_corpo_f_02 (actor 18, community); Bar_corpo_f_03 (actor 19, community); Bartender_01 (actor 20, community); Arasaka_coworker (actor 21, community); Hajime_Taki (actor 22, community); bar_corpo_m_03 (actor 23, community); Exalted_woman (actor 24, community); Male_prostitute (actor 25, community); hideo_kojima (actor 26, community); Fahrida (actor 27, community); Businessman (actor 28, community); Journalist (actor 29, community); kojima_listener_01 (actor 30, community); kojima_listener_02 (actor 31, community); V (actor 32, findInContext).

Entries: `schettiono_scene_in` → 1; `akulov_scene_in` → 11; `coworker_dead_in` → 152; `escorts_in` → 21; `coworker_alive_in` → 157; `zen_room_corpos_in` → 26; `kojima_dial_in` → 293; `bar_waitress_in` → 36; `guards_lobby_patrol_in` → 41; `kojima_loop_in` → 307; `guards_lobby_break_in` → 46; `restaurant_pep_talk_in` → 51; `farida_in` → 322; `bartender_story_1_in` → 67; `bartender_story_2_in` → 73; `q005_05_bar_corpos_in` → 217; `arasaka_coworker_corpo_in` → 96.

Exits: `schettiono_scene_out` → 2; `coworker_dead_out` → 153; `escorts_out` → 22; `coworker_alive_out` → 158; `zen_room_corpos_out` → 27; `bar_waitress_out` → 37; `guards_lobby_patrol_out` → 42; `guards_lobby_break_out` → 47; `restaurant_pep_talk_out` → 52; `farida_out` → 325; `bartender_story_1_out` → 68; `bartender_story_2_out` → 74; `q005_05_bar_corpos_out` → 218.

End nodes: 2: `<omitted>`; 22: `<omitted>`; 27: `<omitted>`; 37: `<omitted>`; 42: `<omitted>`; 47: `<omitted>`; 52: `<omitted>`; 68: `<omitted>`; 74: `<omitted>`; 153: `<omitted>`; 158: `<omitted>`; 218: `<omitted>`; 325: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 32 | 13 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 165 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 7 | 13 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/19` |
| `scnIKEvent` | 14 | 13 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnLookAtEvent` | 132 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 84 | 13 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnUnmountEvent` | 7 | 13 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/18` |
| `scneventsEquipItemToPerformer` | 9 | 260 / 557 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 7 | 13 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scneventsSocket` | 86 | 13 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 260 / 560 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/21` |
| `scneventsUnequipItemFromPerformerByItem` | 6 | 260 / 539 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/5` |
| `scneventsVFXEvent` | 2 | 298 / 830 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- speech, gaze: 7
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, vfx: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- idle_animation, gaze, socket_signal: 1
- socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `d997998c6d7db69dd62e725d8f0a1ae7b920ff133b2860dcd656d399db202417`. Binary SHA-256: `0ac745e1dc566eaa7ed38d45a2ce36d00a9285fe0e680117d38121cda0a95974`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_05_hotel_fluff.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_06_undercover.scene`

58 graph nodes, 79 edges; 9 event-bearing sections, 64 events; 16 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Jackie (actor 0, spawnSet); TBug (actor 1, spawnSet); q005_hotel_concierge (actor 2, community); V (actor 3, findInContext).

Entries: `walk_to_elevator` → 1444.

Exits: `scene_wrap_up` → 3906; `walk_from_elevator` → 1449.

End nodes: 1449: `NonTerminating`; 3906: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 1405 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/5` |
| `scnDialogLineEvent` | 9 | 1405 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 1500 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/6` |
| `scnIKEvent` | 2 | 1500 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnLookAtEvent` | 23 | 1405 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnPlaySkAnimEvent` | 14 | 1405 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnUnmountEvent` | 1 | 1500 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 1500 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |
| `scneventsSocket` | 9 | 1405 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, socket_signal: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `66c3ca2820dc3226a0049ccedc14e67b861104c3d68985ccc0e59968f851a8d1`. Binary SHA-256: `59c3513759139ddab5e320b4714d3f27b53e32f1cb48bd297ab06686b56f1ca2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_06_undercover.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_07_vip_apartment.scene`

449 graph nodes, 607 edges; 64 event-bearing sections, 592 events; 192 screenplay lines, 8 screenplay options, 6 choice nodes.

Actors: Jackie (actor 0, spawnSet); Tbug (actor 1, spawnSet); Saburo (actor 2, spawnSet); Yorinobu (actor 3, spawnSet); Takemura (actor 4, spawnSet); AI (actor 5, findInContext); Smasher (actor 6, spawnSet); drone_01 (actor 7, spawner); drone_02 (actor 8, spawner); Iguana (actor 9, community); q005_saburo_av (actor 10, spawner); V (actor 11, findInContext).

Entries: `smasher_kill_preview` → 4192; `landing_pad_a_in` → 4279; `in_front_of_rented_room` → 3039; `alarm_message_in` → 2591; `q005_07_chippin_in` → 1221; `smasher_kills_v_in` → 3064; `Start 24` → 4922; `q005_07_yorinobu_in` → 1251; `Start1` → 4943.

Exits: `to_the_ledge` → 3263; `scene_wrap` → 4240; `q005_chppin_in_terminating` → 4803; `alarm_message_out` → 2592; `q005_07_chippin_out` → 1222; `smasher_kills_v_out` → 3065.

End nodes: 1222: `NonTerminating`; 2592: `<omitted>`; 3065: `<omitted>`; 3263: `NonTerminating`; 4240: `<omitted>`; 4803: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 25 | 1315 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnChangeIdleAnimEvent` | 68 | 1220 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnDialogLineEvent` | 148 | 1220 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 6 | 2358 / 1049 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/19` |
| `scnIKEvent` | 13 | 1592 / 175 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/10` |
| `scnLookAtEvent` | 101 | 1268 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnPlayRidAnimEvent` | 4 | 2000 / 641 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/133` |
| `scnPlaySkAnimEvent` | 120 | 1220 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnUnmountEvent` | 6 | 2358 / 1053 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/22` |
| `scneventsCameraParamsEvent` | 1 | 3066 / 1699 | `/Data/RootChunk/sceneGraph/Data/graph/171/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 6 | 2358 / 1051 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/21` |
| `scneventsSocket` | 76 | 1220 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/5` |
| `scneventsVFXEvent` | 18 | 1592 / 169 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- skeletal_animation, gaze, socket_signal: 5
- gaze: 3
- speech, gaze: 3
- speech, idle_animation: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, socket_signal: 1
- speech, skeletal_animation: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, rid_actor, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, camera, audio, vfx, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1

Raw SHA-256: `de50cc30e905b615199048397d23602bd9b57aae9e50b456ae56537a7ab6a4a9`. Binary SHA-256: `45ed2ecd82e09100e24e100c49ac25ef1def1094a629a3d857f347415ac7598b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_07_vip_apartment.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_09_attack.scene`

447 graph nodes, 670 edges; 90 event-bearing sections, 441 events; 145 screenplay lines, 10 screenplay options, 7 choice nodes.

Actors: Jackie (actor 0, spawnSet); Arasaka_Kill_Squad_1 (actor 1, findInWorld); Arasaka_Kill_Squad_2 (actor 2, findInWorld); Arasaka_Kill_Squad_3 (actor 3, findInWorld); Battle_drone (actor 4, spawnDespawn); Saburo_AV_voice (actor 5, findInContext); Rooftop_Guard_01 (actor 6, community); Rooftop_Guard_02 (actor 7, community); q005_spn_flathead (actor 8, spawner); Evelyn (actor 9, spawnSet); Delamain (actor 10, spawnSet); trauma_drone_1 (actor 11, spawner); trauma_drone_2 (actor 12, spawner); trauma_drone_3 (actor 13, spawner); Trauma__AV (actor 14, spawner); Military__AV (actor 15, spawner); AV_drone (actor 16, spawner); saburo_av (actor 17, spawner); Player (actor 18, findInContext).

Entries: `q005_09_attack_in` → 1; `preview_taking_the_chip` → 1743; `preview_jump` → 1751; `open_av_in` → 1780; `Start 19` → 4003; `q005_09_get_in_appratment_in` → 118; `q005_09_leave_appartment_in` → 132; `q005_09_leave_in` → 137; `unauthorized_access_in` → 1452; `open_saburo_av_in` → 1457; `q005_09_kill_suticase_squad_in` → 166; `q005_09_to_balcony_in` → 176; `q005_09_to_balcony_call_in` → 181; `q005_09_taking_the_chip` → 667; `Start1` → 4615; `noticing_rooftop_guards_in` → 377; `rooftop_guard_done_in` → 382; `no_steering_wheel_in` → 387; `hack_av_pda_in` → 392; `rooftop_drone_arrives_in` → 400; `preview_case_in` → 2566; `rooftop_guards_chat_in` → 414.

Exits: `q005_09_attack_out` → 2; `drone_kills_V` → 3919; `open_av_out` → 1782; `q005_09_get_in_appratment_out` → 119; `q005_09_leave_appartment_out` → 133; `q005_09_leave_out` → 138; `unauthorized_access_out` → 1453; `open_saburo_av_out` → 1458; `q005_09_kill_suticase_squad_out` → 167; `q005_09_to_balcony_out` → 177; `q005_09_to_balcony_call_out` → 182; `q005_09_attack_terminate_out` → 4219; `noticing_rooftop_guards_out` → 378; `rooftop_guard_done_out` → 383; `no_steering_wheel_out` → 388; `hack_av_pda_out` → 393; `rooftop_drone_arrives_out` → 401; `rooftop_guards_chat_out` → 415.

End nodes: 2: `NonTerminating`; 119: `<omitted>`; 133: `<omitted>`; 138: `<omitted>`; 167: `<omitted>`; 177: `<omitted>`; 182: `<omitted>`; 378: `<omitted>`; 383: `<omitted>`; 388: `<omitted>`; 393: `<omitted>`; 401: `<omitted>`; 415: `<omitted>`; 1453: `<omitted>`; 1458: `<omitted>`; 1782: `<omitted>`; 3919: `<omitted>`; 4219: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 14 | 157 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/5` |
| `scnChangeIdleAnimEvent` | 16 | 157 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnDialogLineEvent` | 93 | 117 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 1456 / 1049 | `/Data/RootChunk/sceneGraph/Data/graph/155/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 1232 / 893 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/8` |
| `scnIKEvent` | 4 | 1232 / 885 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/1` |
| `scnLookAtEvent` | 46 | 157 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/8` |
| `scnPlaySkAnimEvent` | 75 | 157 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnUnmountEvent` | 2 | 1232 / 898 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/12` |
| `scneventsAttachPropToPerformer` | 4 | 498 / 418 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/5` |
| `scneventsAttachPropToWorld` | 4 | 226 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/3` |
| `scneventsCameraParamsEvent` | 4 | 157 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 2 | 1232 / 894 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/9` |
| `scneventsSocket` | 67 | 157 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/16` |
| `scneventsVFXEvent` | 107 | 157 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 33
- speech: 27
- speech, gaze: 3
- skeletal_animation, idle_animation: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, audio, vfx, socket_signal: 1
- skeletal_animation, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, audio, vfx: 1
- skeletal_animation: 1
- skeletal_animation, gaze: 1
- speech, gaze, audio, socket_signal: 1
- speech, idle_animation, gaze: 1

Raw SHA-256: `4fc7930ee13df757f03b55af987ae82cc687bead83d08e7d6ad397b05343f598`. Binary SHA-256: `4e187143edb98deef7bd8a1b8e7945b7f27265eb3b5330bd111c6f522382de1b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_09_attack.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_10_taking_the_chip.scene`

106 graph nodes, 80 edges; 33 event-bearing sections, 84 events; 79 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Jackie (actor 0, spawnSet); Evelyn (actor 1, spawnDespawn); Delamain (actor 2, findInContext); KillSquadBoss (actor 3, community); KillSquadSoldier (actor 4, community); FirstEncounterGuard_01 (actor 5, community); FirstEncounterGuard_02 (actor 6, community); ArasakaHotelOfficer (actor 7, community); ElevatorSceneGuard01 (actor 8, community); ArasakaHotelGuard04 (actor 9, community); ArasakaHotelGuard05 (actor 10, community); ArasakaHotelguard06 (actor 11, community); ArasakaHotelguard10 (actor 12, community); ArasakaHotelguard11 (actor 13, community); ArasakaHotelGuard07 (actor 14, community); ArasakaHotelGarage01 (actor 15, community); ArasakaHotelGarage02 (actor 16, community); WalkieTalkie (actor 17, findInContext); Mech (actor 18, community); V (actor 19, findInContext).

Entries: `lets_look_around_in` → 1078; `q005_10_entered_lobby_in` → 545; `q005_10_find_killers_in` → 554; `q005_10_kill_them_in` → 559; `q005_11_jackie_about_loot_in` → 778; `q005_12_jackie_about_cameras_in` → 783; `q005_10_first_encounter_guards_chat_in` → 678; `q005_13_jackie_about_officer_in` → 788; `q005_10_first_enc_intro_in` → 685; `q005_14_office_raport_in` → 794; `q005_10_jackie_outdoor_in` → 903; `q005_10_first_encounter_guards_chat_smoke_in` → 908; `q005_15_rifle04_reporting_out` → 804; `after_first_combat_in` → 913; `q005_16_rifle06_elevator_status_in` → 809; `utility_room_in` → 918; `first_encounter_done_in` → 704; `q005_10_q005_24_garage_arasaka_in` → 1026; `q005_17_rifle11_door_scene_in` → 814; `lift_to_lobby_in` → 923; `q005_18_officer_report2_in` → 819; `floor_halfway_done_in` → 933; `conf_room_in` → 938; `another_ledge_in` → 943; `q005_20_elevetor_down_in` → 840; `q005_21_elevetor2_status_in` → 845; `q005_10_scanned_broken_suitcase_in` → 524; `Start 14` → 1069; `q005_23_jackie_got_card_in` → 855.

Exits: `q005_23_jackie_got_card_out` → 856; `End 15` → 1071; `lets_look_around_out` → 1079; `q005_10_entered_lobby_out` → 546; `q005_10_find_killers_out` → 555; `q005_10_kill_them_out` → 560; `q005_11_jackie_about_loot_out` → 779; `q005_12_jackie_about_cameras_out` → 784; `q005_10_first_encounter_guards_chat_out` → 679; `q005_13_jackie_about_officer_out` → 789; `q005_10_first_enc_jakie_reaction_out` → 683; `q005_10_first_enc_intro_out` → 686; `q005_14_office_raport_out` → 795; `q005_10_jackie_outdoor_out` → 904; `q005_10_first_encounter_guards_chat_smoke_out` → 909; `q005_15_rifle04_reporting` → 805; `after_first_combat_out` → 914; `q005_16_rifle06_elevator_status_out` → 810; `utility_room_out` → 919; `first_encounter_done_out` → 705; `q005_10_q005_24_garage_arasaka_out` → 1027; `q005_17_rifle11_door_scene_out` → 815; `lift_to_lobby_out` → 924; `q005_18_officer_report2_out` → 820; `floor_halfway_done_out` → 934; `conf_room_out` → 939; `another_ledge_out` → 944; `q005_20_elevetor_down_out` → 841; `q005_21_elevetor2_status_out` → 846; `q005_10_scanned_broken_suitcase_out` → 525.

End nodes: 525: `<omitted>`; 546: `<omitted>`; 555: `<omitted>`; 560: `<omitted>`; 679: `<omitted>`; 683: `NonTerminating`; 686: `<omitted>`; 705: `<omitted>`; 779: `<omitted>`; 784: `<omitted>`; 789: `<omitted>`; 795: `<omitted>`; 805: `<omitted>`; 810: `<omitted>`; 815: `<omitted>`; 820: `<omitted>`; 841: `<omitted>`; 846: `<omitted>`; 856: `<omitted>`; 904: `<omitted>`; 909: `<omitted>`; 914: `<omitted>`; 919: `<omitted>`; 924: `<omitted>`; 934: `<omitted>`; 939: `<omitted>`; 944: `<omitted>`; 1027: `<omitted>`; 1071: `<omitted>`; 1079: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1192 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/2` |
| `scnDialogLineEvent` | 78 | 526 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 1192 / 214 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/0` |
| `scneventsSocket` | 2 | 680 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |
| `scneventsVFXEvent` | 1 | 1192 / 223 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 31
- speech, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1

Raw SHA-256: `d4d4d239dc1d2dbbea46e5d89dc36298a2978c94ed40c1c7f71c09ec4aee4d15`. Binary SHA-256: `61131d9375b8a7cc04e0bd664644925bcfcd13b98e52e8c27b2302a3d15b45e9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_10_taking_the_chip.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_14_after_escape.scene`

420 graph nodes, 507 edges; 73 event-bearing sections, 464 events; 138 screenplay lines, 20 screenplay options, 10 choice nodes.

Actors: Jackie (actor 0, spawnSet); Delamain_holocall (actor 1, spawnSet); Smasher (actor 2, spawnSet); Arasaka_corp_01 (actor 3, spawner); Arasaka_corp_02 (actor 4, spawner); arasaka_soldier_01 (actor 5, spawnDespawn); arasaka_soldier_02 (actor 6, spawnDespawn); Delamain (actor 7, spawnSet); blockade_vehicle_01 (actor 8, spawner); blockade_vehicle_02 (actor 9, spawner); blockade_columbus_01 (actor 10, spawner); blockade_columbus_02 (actor 11, spawner); V (actor 12, findInContext).

Entries: `preview_start` → 3806; `preview_del` → 2155; `q005_14_drones_around_building_in` → 1367; `q005_14_back_to_motel_in` → 165; `q005_14_ps_floor_corridor_half_way_in` → 1407; `q005_14_ps_floor_corridor_about_enemies_in` → 1417; `q005_14_ps_floor_spotted_in` → 1428; `q005_14_elevator_in_lobby_in` → 606; `q005_14_ps_floor_elevator_in` → 1433; `q005_14_lobby_enemies_comment_in` → 1444; `q005_14_ps_floor_key_card_looted_in` → 1472; `scene_preview` → 3546; `Start 21` → 4373; `q005_first_elevator_preview` → 3990; `barricade_chase_in` → 1130; `chase_1_start_in` → 1135; `chase_1_done_in` → 1140; `barricade_chase_done_in` → 1150.

Exits: `q005_14_drones_around_building_out` → 1368; `q005_14_ps_floor_corridor_half_way_out` → 1408; `q005_14_back_to_motel_out` → 173; `q005_14_ps_floor_corridor_about_enemies_out` → 1421; `q005_14_ps_floor_spotted_out` → 1429; `q005_14_ps_floor_elevator_out` → 1434; `q005_14_lobby_enemies_comment_out` → 1451; `drone_fight` → 1867; `q005_14_ps_floor_key_card_looted_out` → 1473; `back_to_notell` → 1901; `barricade_chase_out` → 1131; `q005_14_ps_floor_elevator_down` → 4025; `chase_1_start_out` → 1136; `chase_1_done_out` → 1141; `barricade_chase_done_out` → 1151.

End nodes: 173: `<omitted>`; 1131: `<omitted>`; 1136: `<omitted>`; 1141: `<omitted>`; 1151: `<omitted>`; 1368: `<omitted>`; 1408: `<omitted>`; 1421: `<omitted>`; 1429: `<omitted>`; 1434: `<omitted>`; 1451: `<omitted>`; 1473: `<omitted>`; 1867: `NonTerminating`; 1901: `NonTerminating`; 4025: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 24 | 1377 / 610 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/12` |
| `scnChangeIdleAnimEvent` | 25 | 609 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 114 | 609 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayActionEvent` | 1 | 2141 / 1338 | `/Data/RootChunk/sceneGraph/Data/graph/183/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 1127 / 421 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/7` |
| `scnIKEvent` | 12 | 640 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnLookAtEvent` | 51 | 614 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 88 | 614 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 2 | 3308 / 1888 | `/Data/RootChunk/sceneGraph/Data/graph/270/Data/events/9` |
| `scneventsAttachPropToPerformer` | 1 | 937 / 343 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/8` |
| `scneventsAttachPropToWorld` | 1 | 937 / 346 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/11` |
| `scneventsCameraParamsEvent` | 5 | 687 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 24 | 640 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scneventsSocket` | 77 | 635 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/16` |
| `scneventsVFXEvent` | 36 | 769 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 24
- speech, skeletal_animation, gaze: 8
- speech, skeletal_animation: 5
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- idle_animation: 2
- speech, skeletal_animation, socket_signal, animation_state: 2
- speech, idle_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, socket_signal: 2
- speech, idle_animation: 1
- skeletal_animation, idle_animation, ik, socket_signal, animation_state: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, camera, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state: 1
- speech, skeletal_animation, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, audio: 1
- idle_animation, gaze: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1

Raw SHA-256: `dca4d1d8dae94c596138a2328638f0ac6d9eca473e97390b481fe6defa3c84e2`. Binary SHA-256: `4ce8cfc8be5c8beb2bd28d53a00abfe678339af8e2b67b478f2e20cf2bcb4b05`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_14_after_escape.scene" --events
```

## `base\quest\main_quests\prologue\q005\scenes\q005_15_no_tell_motel.scene`

249 graph nodes, 318 edges; 50 event-bearing sections, 306 events; 82 screenplay lines, 19 screenplay options, 13 choice nodes.

Actors: Jackie (actor 0, spawnSet); Dex (actor 1, spawnSet); Dex_bodyguard_01 (actor 2, spawnSet); tbug (actor 3, spawnSet); v_tpp_mirror_male (actor 4, spawnDespawn); v_tpp_mirror_female (actor 5, spawnDespawn); Delamain (actor 6, spawnSet); V (actor 7, findInContext).

Entries: `Start 12` → 4691; `q005_15_room_in` → 520; `Start 6` → 1607; `q005_01_plan_got_it_here_in` → 1652; `Start 11` → 4426.

Exits: `q005_15_room_out` → 530; `q005_01_plan_got_it_here_out` → 1653.

End nodes: 530: `NonTerminating`; 1653: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 543 / 131 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/4` |
| `scnChangeIdleAnimEvent` | 7 | 458 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 60 | 458 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 4 | 1758 / 1084 | `/Data/RootChunk/sceneGraph/Data/graph/136/Data/events/11` |
| `scnIKEvent` | 8 | 1758 / 1066 | `/Data/RootChunk/sceneGraph/Data/graph/136/Data/events/1` |
| `scnLookAtEvent` | 41 | 458 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scnPlaySkAnimEvent` | 61 | 440 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlayVideoEvent` | 4 | 1466 / 695 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/1` |
| `scnUnmountEvent` | 4 | 1758 / 1091 | `/Data/RootChunk/sceneGraph/Data/graph/136/Data/events/17` |
| `scneventsAttachPropToPerformer` | 2 | 900 / 328 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/5` |
| `scneventsCameraParamsEvent` | 10 | 542 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 4 | 1758 / 1089 | `/Data/RootChunk/sceneGraph/Data/graph/136/Data/events/16` |
| `scneventsSocket` | 72 | 440 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scneventsVFXEvent` | 25 | 543 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- vfx, socket_signal, video: 4
- speech, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, camera, audio, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, gaze: 1
- props_equipment: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, idle_animation: 1
- skeletal_animation, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1
- skeletal_animation, gaze, vfx: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1

Raw SHA-256: `18300fcb44cb89a19b1b19e45d214bb2e23ac0f20e94ddf8a8af9eb54fc657f5`. Binary SHA-256: `135060656c73525378b54e1fdbff2d2698a06e7c23cc2cef1b10b308d307a387`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q005\scenes\q005_15_no_tell_motel.scene" --events
```

## `base\quest\tertiary_characters\default_dialogues\claire_default.scene`

49 graph nodes, 66 edges; 16 event-bearing sections, 99 events; 36 screenplay lines, 6 screenplay options, 1 choice nodes.

Actors: Claire (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `claire_pissed` → 156; `claire_default_start` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 34 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnDialogLineEvent` | 33 | 5 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 8 | 24 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 29 | 5 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsEquipItemToPerformer` | 2 | 97 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scneventsSocket` | 16 | 6 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsUnequipItemFromPerformer` | 2 | 99 / 238 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation: 2
- speech, skeletal_animation, socket_signal: 2
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- idle_animation, gaze: 1

Raw SHA-256: `cee6a7889fd0d7741b7e496c890521c03646b1546da41b79793011958ca06f57`. Binary SHA-256: `099b148dbf823778464d7aedb290af2a7c4ba472e654d3e021d354a6fd9880dd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\tertiary_characters\default_dialogues\claire_default.scene" --events
```

