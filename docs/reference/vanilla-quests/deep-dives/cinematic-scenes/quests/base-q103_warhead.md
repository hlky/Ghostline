# Ghost Town: scene presentation

Journal identity: `quests/main_quest/act_01/q103_warhead`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q103_warhead.md) · [All cinematic studies](../README.md)

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

## `base\quest\main_quests\part1\q103\scenes\q103_03_rogue.scene`

477 graph nodes, 575 edges; 88 event-bearing sections, 868 events; 178 screenplay lines, 33 screenplay options, 19 choice nodes.

Actors: rogue (actor 0, spawnSet); netrunner (actor 1, spawnSet); waitress (actor 2, spawnSet); johnny (actor 3, spawnDespawn); Panam (actor 4, spawnSet); weyland (actor 5, spawnSet); crowd_03 (actor 6, community); crowd_01 (actor 7, community); crowd_02 (actor 8, community); crowd_04 (actor 9, community); crowd_05 (actor 10, community); crowd_06 (actor 11, community); Player (actor 12, findInContext).

Entries: `Start 0` → 1; `Start 8` → 3873; `v_leaves_afterlife` → 1982; `Start 7` → 3784; `Start 4` → 2414.

Exits: `End 0` → 412; `v_leaves_afterlife_out` → 1981.

End nodes: 412: `NonTerminating`; 1981: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1247 / 875 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/7` |
| `scnChangeIdleAnimEvent` | 61 | 584 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scnDialogLineEvent` | 147 | 584 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 617 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/10` |
| `scnIKEvent` | 10 | 617 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnLookAtEvent` | 184 | 584 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnPlaySkAnimEvent` | 201 | 584 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnUnmountEvent` | 5 | 617 / 150 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/15` |
| `scneventsAttachPropToNode` | 7 | 918 / 594 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/3` |
| `scneventsAttachPropToPerformer` | 4 | 1162 / 712 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/26` |
| `scneventsAttachPropToWorld` | 4 | 1162 / 701 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/19` |
| `scneventsCameraParamsEvent` | 4 | 875 / 361 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/24` |
| `scneventsEquipItemToPerformer` | 1 | 849 / 301 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/9` |
| `scneventsPlayerLookAtEvent` | 1 | 1755 / 1224 | `/Data/RootChunk/sceneGraph/Data/graph/77/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 5 | 617 / 146 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |
| `scneventsSocket` | 197 | 584 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 31 | 584 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 16
- skeletal_animation, socket_signal: 12
- speech, skeletal_animation, gaze, socket_signal: 8
- speech: 5
- skeletal_animation: 5
- skeletal_animation, gaze, socket_signal: 4
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 3
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, camera, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, vfx: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, socket_signal: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `6cf80abe7c13f5a8eb346448e893cc40e5384e4edade1389df4c8f53c7907640`. Binary SHA-256: `7f4de2c6ce8581d261cc61268e27cf5a86b904ee7d0618b0c3bc8c95365b3556`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_03_rogue.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_05_panam_call.scene`

39 graph nodes, 44 edges; 9 event-bearing sections, 27 events; 23 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: panam (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End3` → 3871.

End nodes: 3871: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 23 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnLookAtEvent` | 1 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 1 | 3962 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/0` |
| `scneventsSocket` | 2 | 3962 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, gaze: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `ab0b4b154e48e1004c1ff23b4903f2de88467586090d4a69f49583968e2f0c66`. Binary SHA-256: `8ea7eac8952c6801bf2d2f08dd88484ca7ac082f08062371f11d1aad4fc213ff`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_05_panam_call.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_06_meet_panam.scene`

185 graph nodes, 237 edges; 36 event-bearing sections, 416 events; 120 screenplay lines, 25 screenplay options, 11 choice nodes.

Actors: panam (actor 0, spawnSet); rogue (actor 1, findInContext); Johnny (actor 2, spawnDespawn); stolen_vehicle (actor 3, community); Player (actor 4, findInContext).

Entries: `Start 0` → 1; `Start 2` → 1407; `Start 1` → 1235; `idles` → 1049; `Start 6` → 1493.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 18 | 238 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scnChangeIdleAnimEvent` | 38 | 238 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 112 | 238 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayActionEvent` | 2 | 356 / 426 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/10` |
| `scnIKEvent` | 2 | 326 / 244 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/17` |
| `scnLookAtEvent` | 49 | 238 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnPlaySkAnimEvent` | 84 | 238 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsAttachPropToNode` | 1 | 336 / 309 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/35` |
| `scneventsAttachPropToPerformer` | 1 | 336 / 258 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 356 / 441 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/20` |
| `scneventsEquipItemToPerformer` | 3 | 336 / 274 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 3 | 326 / 213 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scneventsSocket` | 101 | 238 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 336 / 297 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/23` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 3
- speech: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, gameplay_action: 1
- speech, idle_animation, socket_signal: 1
- gaze: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1

Raw SHA-256: `3100611357a3d6eb4e6d15a3a37271097e5e7b00c37761e93a4fc209e5be5237`. Binary SHA-256: `2f2f81ab4bc978926801064cbf26229b90125cfa95871aba4bda95e2774b914c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_06_meet_panam.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_06a_camp_drive.scene`

73 graph nodes, 100 edges; 17 event-bearing sections, 212 events; 63 screenplay lines, 12 screenplay options, 5 choice nodes.

Actors: panam (actor 0, spawnSet); stolen_car (actor 1, community); Player (actor 2, findInContext).

Entries: `to_camp` → 4; `Start 1` → 603.

Exits: `to_camp_out` → 233.

End nodes: 233: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 17 | 41 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnDialogLineEvent` | 61 | 41 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnIKEvent` | 8 | 41 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/27` |
| `scnLookAtEvent` | 62 | 41 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 206 / 311 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/0` |
| `scnPlaySkAnimEvent` | 48 | 41 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 7 | 41 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/23` |
| `scneventsSocket` | 8 | 41 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/25` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 7
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- speech, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, ik, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- ik, socket_signal, animation_state: 1

Raw SHA-256: `8fb4188a688313248aa17dad1985b25286513ba28367a68f6d2222254ac6c50a`. Binary SHA-256: `d212bad25c863dc1dc60d234bf8ad4104f864fdbb8f7607346940c579ec1621b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_06a_camp_drive.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_06b_nomad_camp.scene`

186 graph nodes, 217 edges; 38 event-bearing sections, 485 events; 86 screenplay lines, 11 screenplay options, 10 choice nodes.

Actors: Panam (actor 0, spawnSet); Mitch (actor 1, spawnSet); Scorpion (actor 2, spawnSet); nomad_01 (actor 3, community); nomad_02 (actor 4, community); nomad_03 (actor 5, community); nomad_04 (actor 6, community); nomad_05 (actor 7, community); nomad_06 (actor 8, community); stolen_vehicle (actor 9, community); Player (actor 10, findInContext).

Entries: `cinedebug_box` → 1536; `mitch_scorpion_talk` → 18; `Start 7` → 1549; `Start 2` → 1396; `Start 3` → 1409; `mitchandscorpmove` → 1177; `Start 4` → 1497; `Start 5` → 1521.

Exits: `leaving_camp_out` → 47.

End nodes: 47: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 1459 / 1651 | `/Data/RootChunk/sceneGraph/Data/graph/165/Data/events/4` |
| `scnChangeIdleAnimEvent` | 48 | 21 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |
| `scnDialogLineEvent` | 74 | 21 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scnGameplayActionEvent` | 2 | 340 / 467 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scnGameplayTransitionEvent` | 6 | 102 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/75` |
| `scnIKEvent` | 14 | 102 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/67` |
| `scnLookAtEvent` | 143 | 21 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 95 | 21 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnPoseCorrectionEvent` | 1 | 833 / 1058 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/3` |
| `scnUnmountEvent` | 6 | 102 / 197 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/76` |
| `scneventsAttachPropToNode` | 6 | 102 / 142 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/40` |
| `scneventsAttachPropToPerformer` | 9 | 102 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/27` |
| `scneventsSetAnimFeatureEvent` | 8 | 102 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/74` |
| `scneventsSocket` | 65 | 21 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/27` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 102 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/34` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, gaze: 6
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- gaze: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- socket_signal: 1
- skeletal_animation, audio, socket_signal, animation_state: 1

Raw SHA-256: `f0022afd753b12c3f737f63c633ac31938e4adcb10b28406eafd60317f96a04b`. Binary SHA-256: `95504d8f50b58f9bacbd5e0b435b7973149ca2f83183c48b0ca3f568648f3750`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_06b_nomad_camp.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_07_ghost_town_drive.scene`

393 graph nodes, 434 edges; 36 event-bearing sections, 404 events; 94 screenplay lines, 15 screenplay options, 6 choice nodes.

Actors: panam (actor 0, spawnSet); stolen_car (actor 1, community); Player (actor 2, findInContext).

Entries: `to_ghost_town` → 50; `scouting` → 127; `Start 2` → 1578; `Start 5` → 2304; `Start 3` → 1596; `Start 4` → 1996; `preview` → 717.

Exits: `scouting_out` → 51; `cleanup_out` → 148.

End nodes: 51: `NonTerminating`; 148: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 1970 / 2345 | `/Data/RootChunk/sceneGraph/Data/graph/293/Data/events/4` |
| `scnChangeIdleAnimEvent` | 46 | 70 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 83 | 70 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 10 | 191 / 354 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/24` |
| `scnIKEvent` | 24 | 179 / 293 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scnLookAtEvent` | 65 | 70 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 752 / 825 | `/Data/RootChunk/sceneGraph/Data/graph/77/Data/events/0` |
| `scnPlaySkAnimEvent` | 73 | 70 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnPoseCorrectionEvent` | 2 | 191 / 324 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/5` |
| `scnUnmountEvent` | 10 | 191 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/23` |
| `scneventsSetAnimFeatureEvent` | 15 | 179 / 295 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/4` |
| `scneventsSocket` | 68 | 70 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/30` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- skeletal_animation, socket_signal: 5
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, socket_signal: 2
- speech, ik, socket_signal, animation_state: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, idle_animation, gaze, socket_signal: 1
- socket_signal, animation_state, mount_workspot: 1
- speech: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, audio: 1

Raw SHA-256: `38661d133a12e7c0178e94bea8a261a3add8ac50752273e4b2dba561bde000dd`. Binary SHA-256: `51595029a037954785c535dee64587509dd8bf2d387938ab30543be3faed4f97`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_07_ghost_town_drive.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_08_ghost_town_plan.scene`

149 graph nodes, 167 edges; 20 event-bearing sections, 124 events; 31 screenplay lines, 7 screenplay options, 6 choice nodes.

Actors: Panam (actor 0, spawnSet); panam_holocall (actor 1, spawnDespawn); stolen_car (actor 2, community); Player (actor 3, findInContext).

Entries: `Start_arrival` → 1; `Start 5` → 1516; `Start 4` → 648; `start_timelapse` → 249; `Start 3` → 579.

Exits: `End_arrival` → 2; `end_timelapse` → 253.

End nodes: 2: `NonTerminating`; 253: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 6 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnChangeIdleAnimEvent` | 11 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 23 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayActionEvent` | 1 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 3 | 364 / 258 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/13` |
| `scnIKEvent` | 8 | 364 / 246 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/3` |
| `scnLookAtEvent` | 7 | 6 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnPlaySkAnimEvent` | 20 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 3 | 364 / 263 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/17` |
| `scneventsAttachPropToNode` | 1 | 755 / 729 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 581 / 618 | `/Data/RootChunk/sceneGraph/Data/graph/74/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 4 | 364 / 259 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/14` |
| `scneventsSocket` | 25 | 6 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsVFXEvent` | 7 | 364 / 250 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- vfx, socket_signal: 2
- skeletal_animation, idle_animation, vfx: 2
- skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, gameplay_action: 1
- speech, skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- props_equipment: 1
- socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- ik, socket_signal, animation_state: 1

Raw SHA-256: `fe15b0016973f995b2b09015d88b5112b3093a60b09ed601fcfd6b148b2608cb`. Binary SHA-256: `e6c97754ce04ca603dc644050eea32e7e1d4f0531d0883f6f36e6c9b1e4ba42d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_08_ghost_town_plan.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_09_raffen_shiv.scene`

70 graph nodes, 66 edges; 19 event-bearing sections, 99 events; 43 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: raffen_shiv_A2 (actor 0, community); raffen_shiv_A3 (actor 1, community); raffen_shiv_B1 (actor 2, community); raffen_shiv_B2 (actor 3, community); raffen_shiv_b4_squad_leader (actor 4, community); raffen_shiv_C1 (actor 5, community); raffen_shiv_C2 (actor 6, community); panam (actor 7, spawnSet); panam_holocall (actor 8, spawnDespawn); panam_vehicle (actor 9, spawnSet); raffen_1_veh (actor 10, community); raffen_2_veh (actor 11, community); Player (actor 12, findInContext).

Entries: `Start_squad_A` → 1; `Start_squad_B` → 4; `Start_squad_C` → 5; `Start_panam_arrival` → 18; `Start_detected` → 25; `raffens_reaction` → 160; `lights_on` → 95; `Start_all_dead` → 33; `car_approach_takedown` → 104; `Start_key` → 39; `start_energy_comment` → 125.

Exits: `End_squad_A` → 2; `End_squad_B` → 7; `End_squad_C` → 8; `End_key_terminate` → 281; `End_panam_arrival` → 19; `raffens_reaction_out` → 161; `lights_on_out` → 96; `End_detected` → 31; `End_all_dead` → 34; `car_approach_double_out` → 105; `End_key` → 40; `car_approach_single_out` → 117; `end_energy_comment` → 126; `lights_out_terminate` → 193.

End nodes: 2: `<omitted>`; 7: `<omitted>`; 8: `<omitted>`; 19: `NonTerminating`; 31: `<omitted>`; 34: `<omitted>`; 40: `NonTerminating`; 96: `NonTerminating`; 105: `<omitted>`; 117: `<omitted>`; 126: `<omitted>`; 161: `NonTerminating`; 193: `<omitted>`; 281: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 20 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scnChangeIdleAnimEvent` | 3 | 20 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scnDialogLineEvent` | 39 | 9 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 170 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/7` |
| `scnIKEvent` | 4 | 170 / 186 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/2` |
| `scnLookAtEvent` | 14 | 271 / 242 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/0` |
| `scnPlaySkAnimEvent` | 12 | 20 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnUnmountEvent` | 2 | 170 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 2 | 170 / 192 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/8` |
| `scneventsSocket` | 13 | 20 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/6` |
| `scneventsVFXEvent` | 3 | 307 / 302 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, socket_signal: 3
- vfx: 3
- speech, skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `a31c37b9447f8c03da4c7f764d86e48be378eeacbc553a48d521b4983a579e52`. Binary SHA-256: `af100631fdaa175e4de4485a57bf0b10ce0ebc2a16f27a31bcac788db98b370e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_09_raffen_shiv.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_10_escape.scene`

71 graph nodes, 72 edges; 13 event-bearing sections, 85 events; 22 screenplay lines, 7 screenplay options, 4 choice nodes.

Actors: panam (actor 0, spawnSet); panam_holocall (actor 1, spawnDespawn); panam_vehicl (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `pickup_panam` → 4; `out_of_area` → 160; `Start 5` → 540; `go_rendez_vous` → 43; `enter_panam_car` → 1470; `go_directly_rendez` → 360; `panam_driver` → 146.

Exits: `enter_panam_car_out` → 1482; `pickup_panam_out` → 5; `go_eliminate` → 228; `out_of_area_out` → 161; `go_rendez_vous_out` → 44; `panam_driver_out` → 147.

End nodes: 5: `NonTerminating`; 44: `<omitted>`; 147: `<omitted>`; 161: `<omitted>`; 228: `<omitted>`; 1482: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 7 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnChangeIdleAnimEvent` | 11 | 7 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 19 | 7 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnGameplayActionEvent` | 4 | 7 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnIKEvent` | 2 | 13 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/24` |
| `scnLookAtEvent` | 6 | 7 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 12 | 7 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsPlayerLookAtEvent` | 1 | 7 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 3 | 302 / 226 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/0` |
| `scneventsSocket` | 16 | 7 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, audio, socket_signal, animation_state, gameplay_action: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, socket_signal, gameplay_action: 1
- speech, skeletal_animation: 1
- skeletal_animation, audio, socket_signal, animation_state: 1

Raw SHA-256: `847f4f689f1491297341aa5dbc71ed8117b8d651cee4f15a55252f761d57f1c3`. Binary SHA-256: `1df9d9648fc990f2fc2460ad56430515a67daa88d2ff0c3b890e1aadf4b1322a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_10_escape.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_11_tunnel_drive.scene`

30 graph nodes, 34 edges; 9 event-bearing sections, 149 events; 40 screenplay lines, 8 screenplay options, 3 choice nodes.

Actors: panam (actor 0, spawnSet); panam_vechicle (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `go_tunnel` → 2; `go_roadhouse` → 79.

End nodes: 2: `NonTerminating`; 79: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 19 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 39 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayActionEvent` | 2 | 58 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/9` |
| `scnIKEvent` | 4 | 58 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/11` |
| `scnLookAtEvent` | 33 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 38 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 2 | 58 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scneventsSocket` | 12 | 4 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state, gameplay_action: 2

Raw SHA-256: `7d43b4d44c2a1199482359b9386a580309093e101c6dabc22ff44d56bf9377c0`. Binary SHA-256: `78b4380aa569d60580acf7a2d05f3b0c1b7dc05f27593f2c59dc17207ea5b77e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_11_tunnel_drive.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_12_tunnel_ambush.scene`

100 graph nodes, 105 edges; 21 event-bearing sections, 201 events; 52 screenplay lines, 9 screenplay options, 5 choice nodes.

Actors: panam (actor 0, spawnSet); raffen_shiv_boss (actor 1, findInWorld); rogue (actor 2, spawnDespawn); Johnny (actor 3, spawnDespawn); panam_vehicle (actor 4, spawnSet); Player (actor 5, findInContext).

Entries: `Start_intro` → 1; `Start_fight` → 8; `Start_victory` → 12; `cin_drivein` → 826; `reinforcement_coming` → 217; `Start 3` → 585; `panam_nash_banter` → 225; `panam_v_banter` → 230.

Exits: `End_intro` → 2; `End_fight` → 9; `End_victory` → 13; `reinforcement_coming_out` → 218; `panam_nash_banter_out` → 226; `panam_v_banter_out` → 231.

End nodes: 2: `NonTerminating`; 9: `NonTerminating`; 13: `NonTerminating`; 218: `NonTerminating`; 226: `NonTerminating`; 231: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 595 / 519 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/4` |
| `scnChangeIdleAnimEvent` | 15 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 47 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 759 / 646 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/2` |
| `scnGameplayTransitionEvent` | 5 | 99 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/14` |
| `scnIKEvent` | 12 | 99 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/8` |
| `scnLookAtEvent` | 35 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 35 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 5 | 99 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/13` |
| `scneventsAttachPropToNode` | 1 | 56 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/22` |
| `scneventsAttachPropToPerformer` | 1 | 279 / 322 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 7 | 99 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/10` |
| `scneventsSocket` | 33 | 4 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsVFXDurationEvent` | 1 | 238 / 293 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 1

Raw SHA-256: `e0af27f441a175ce4ad50a0d47e2a5efb98d1f3edb1af59413084b6a976c13d3`. Binary SHA-256: `2ebbf438f5eae04f42f3ff734fbe8fc4db21cc7b110855624bddfe92d37c3add`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_12_tunnel_ambush.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_13_roadhouse_drive.scene`

59 graph nodes, 68 edges; 16 event-bearing sections, 147 events; 43 screenplay lines, 11 screenplay options, 4 choice nodes.

Actors: panam (actor 0, spawnSet); maelstromer (actor 1, findInContext); panam_car (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `Start_drive` → 1.

Exits: `End_drive` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 14 | 18 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnDialogLineEvent` | 38 | 7 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnIKEvent` | 10 | 42 / 97 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/4` |
| `scnLookAtEvent` | 39 | 7 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 25 | 7 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsAttachPropToPerformer` | 2 | 42 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |
| `scneventsAttachPropToWorld` | 2 | 42 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/17` |
| `scneventsSetAnimFeatureEvent` | 5 | 42 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scneventsSocket` | 12 | 18 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 3
- speech, idle_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 3
- speech: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, socket_signal, animation_state: 2
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze, ik, socket_signal, animation_state: 1

Raw SHA-256: `dc9f124793f954e0a92258843664a8676479e346f697db57c3d7261379ee4c77`. Binary SHA-256: `d275c36e8893478696644fc87f59c42e02fdc769e9b99017e6c5689f97e2a5ce`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_13_roadhouse_drive.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_14_maelstrom.scene`

129 graph nodes, 150 edges; 27 event-bearing sections, 286 events; 56 screenplay lines, 6 screenplay options, 5 choice nodes.

Actors: panam (actor 0, spawnSet); maelstromer01 (actor 1, findInWorld); maestromer02 (actor 2, findInWorld); maestromer03 (actor 3, findInWorld); maestromer04 (actor 4, findInWorld); rogue (actor 5, spawnDespawn); Johnny (actor 6, spawnDespawn); bartender (actor 7, spawnSet); panam_vehicle (actor 8, spawnSet); 6th_street_vehicle (actor 9, community); Player (actor 10, findInContext).

Entries: `Start 0` → 13; `Start 2` → 1440; `Start 4` → 1662.

Exits: `End 0` → 14; `6th_leave` → 1286.

End nodes: 14: `NonTerminating`; 1286: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 15 | 30 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/26` |
| `scnDialogLineEvent` | 52 | 30 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/23` |
| `scnGameplayActionEvent` | 2 | 584 / 283 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |
| `scnGameplayTransitionEvent` | 5 | 30 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/16` |
| `scnIKEvent` | 14 | 30 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 71 | 30 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 38 / 192 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/52` |
| `scnPlaySkAnimEvent` | 56 | 30 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 5 | 30 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scneventsAttachPropToNode` | 3 | 38 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/49` |
| `scneventsAttachPropToPerformer` | 4 | 30 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/19` |
| `scneventsSetAnimFeatureEvent` | 10 | 30 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |
| `scneventsSocket` | 47 | 30 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 38 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 6
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal, animation_state, gameplay_action: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, gaze, socket_signal: 1
- socket_signal, animation_state: 1
- skeletal_animation, ik, socket_signal, animation_state: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `7e6b573a7f112ed6e51d5fec39ed708217673f8f748dca23613d8a1ee5caf055`. Binary SHA-256: `3cbf1d83421ebca8732c844e6c7e25a99cd48a55e9f557781b640738ebda4371`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_14_maelstrom.scene" --events
```

## `base\quest\main_quests\part1\q103\scenes\q103_15_roadhouse_bar.scene`

360 graph nodes, 465 edges; 66 event-bearing sections, 877 events; 151 screenplay lines, 42 screenplay options, 28 choice nodes.

Actors: Panam (actor 0, spawnSet); bartender (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `Start 6` → 2354; `preview` → 1615; `Start 7` → 2912; `Start 4` → 1714; `chicken_bar` → 1235.

Exits: `roadhouse_slept` → 2; `roadhouse_left` → 849.

End nodes: 2: `<omitted>`; 849: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 56 | 14 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scnChangeIdleAnimEvent` | 86 | 12 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 130 | 12 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 13 | 14 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/23` |
| `scnIKEvent` | 26 | 14 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnLookAtEvent` | 128 | 14 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnPlaySkAnimEvent` | 159 | 12 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnUnmountEvent` | 13 | 14 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/22` |
| `scneventsAttachPropToNode` | 2 | 238 / 482 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/13` |
| `scneventsAttachPropToPerformer` | 41 | 14 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scneventsAttachPropToWorld` | 43 | 14 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scneventsCameraParamsEvent` | 3 | 1293 / 1604 | `/Data/RootChunk/sceneGraph/Data/graph/123/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 13 | 14 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/19` |
| `scneventsSocket` | 160 | 12 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsVFXEvent` | 4 | 1144 / 1528 | `/Data/RootChunk/sceneGraph/Data/graph/112/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, props_equipment, audio, socket_signal: 13
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 11
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- gaze: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `9fc30c02402c7924a3473a2c9c05e49c262c69e538e1c19b2213b6d04f9d3ea2`. Binary SHA-256: `a2e44f93910dc8ee83ebf635ae0bfa595b7e5a1d6f8fa96f75aac8fa1a96a75e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q103\scenes\q103_15_roadhouse_bar.scene" --events
```

## `base\quest\minor_quests\mq038\scenes\mq038_01_briefing.scene`

31 graph nodes, 38 edges; 6 event-bearing sections, 65 events; 20 screenplay lines, 5 screenplay options, 3 choice nodes.

Actors: Darryl (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `quest_ends` → 2; `quest_begins` → 38.

End nodes: 2: `<omitted>`; 38: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 20 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 5 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 25 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSocket` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `97ad515bea983c312a3a742e717ec1af8d0dce6d3c04f3c2c96711097efc4ef8`. Binary SHA-256: `c6f424249c63fd39bba97df5b78193f7431e8f7e7b1f31793b0d02125c363796`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq038\scenes\mq038_01_briefing.scene" --events
```

