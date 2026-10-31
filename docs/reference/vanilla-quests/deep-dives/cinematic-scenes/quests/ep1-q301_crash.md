# Dog Eat Dog: scene presentation

Journal identity: `ep1/quests/main_quest/q301_crash`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q301_crash.md) · [All cinematic studies](../README.md)

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

## `ep1\quest\main_quests\q301\scenes\q301_00_holocall_hook.scene`

477 graph nodes, 757 edges; 79 event-bearing sections, 906 events; 165 screenplay lines, 27 screenplay options, 9 choice nodes.

Actors: songbird_holo (actor 0, spawnDespawn); johnny (actor 1, spawnDespawn); songbird_hologram (actor 2, spawnDespawn); passerby_f_01 (actor 3, community); passerby_f_02 (actor 4, community); passerby_m_01 (actor 5, community); Player (actor 6, findInContext).

Entries: `After_quickhackin` → 7553; `HoloStart1` → 490; `HoloStart2` → 565; `Start1` → 5673; `Start 2` → 1519.

Exits: `quickhacked` → 7551; `HoloEnd1` → 492; `holocall_tutorial` → 5092; `HoloEnd2` → 628; `End 3` → 4799.

End nodes: 492: `<omitted>`; 628: `NonTerminating`; 4799: `NonTerminating`; 5092: `NonTerminating`; 7551: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 4. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 15 | 2066 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/7` |
| `scnChangeIdleAnimEvent` | 26 | 2066 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/0` |
| `scnDialogLineEvent` | 134 | 1086 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnGameplayTransitionEvent` | 10 | 2071 / 401 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/112` |
| `scnIKEvent` | 20 | 2071 / 378 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/94` |
| `scnLookAtAdvancedEvent` | 70 | 2069 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/10` |
| `scnLookAtEvent` | 122 | 2066 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/8` |
| `scnOverridePhantomParamsEvent` | 9 | 2066 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/5` |
| `scnPlaySkAnimEvent` | 187 | 2066 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scnPoseCorrectionEvent` | 13 | 2071 / 257 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/25` |
| `scnUnmountEvent` | 10 | 2071 / 403 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/114` |
| `scneventsCameraParamsEvent` | 30 | 2069 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/0` |
| `scneventsCameraPlacementEvent` | 5 | 4614 / 1514 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/7` |
| `scneventsEquipItemToPerformer` | 1 | 2066 / 141 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/15` |
| `scneventsPlayerLookAtEvent` | 3 | 3000 / 928 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 10 | 2071 / 399 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/111` |
| `scneventsSocket` | 148 | 1901 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 3 | 4614 / 1544 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/24` |
| `scneventsVFXDurationEvent` | 45 | 2071 / 285 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/47` |
| `scneventsVFXEvent` | 45 | 2069 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- speech, skeletal_animation, gaze, socket_signal: 6
- speech, skeletal_animation, gaze: 6
- speech, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, camera, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, gaze: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, vfx, socket_signal, animation_state: 2
- vfx: 2
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, camera, audio, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal, animation_state: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, vfx: 1

Raw SHA-256: `298ca5dc7af6e353fad13031227d0f1ff185417bd640c77f5e7d589a0750a210`. Binary SHA-256: `068782fe6060bda6af741976d637cba3a6b3bc6dc6d903f59d990b7fcfd643a2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_00_holocall_hook.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_00a_standalone_opening.scene`

11 graph nodes, 10 edges; 1 event-bearing sections, 7 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: kusanagi (actor 0, community); player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 6 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnChangeIdleAnimEvent` | 1 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 2 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 3 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, audio, socket_signal: 1

Raw SHA-256: `75916a2f301c7658c15a57da7858130db1081aa1c7b026aed30e1cce37a72dbe`. Binary SHA-256: `3cbd46c1e8bdbc9084118eaa610abb27f540d0689f479427cef4d4d033a01439`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_00a_standalone_opening.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_01_border.scene`

898 graph nodes, 1067 edges; 135 event-bearing sections, 915 events; 360 screenplay lines, 41 screenplay options, 16 choice nodes.

Actors: songbird_holo (actor 0, findInContext); guard_m_gate_corpo (actor 1, community); jago_gate_cargo (actor 2, spawnSet); corpo_gate_m (actor 3, community); johnny (actor 4, spawnDespawn); guard_m_gate_block (actor 5, community); guard_f_gate_cargo (actor 6, community); citizen_m_driver (actor 7, community); guard_m_front_ncpd (actor 8, community); guard_f_front_ncpd (actor 9, community); guard_f_gate_corpo (actor 10, community); guard_m_front_warning (actor 11, community); ncpd_f_01 (actor 12, community); ncpd_m_01 (actor 13, community); bree (actor 14, spawnSet); guard_f_side_argument (actor 15, community); guard_m_side_argument_01 (actor 16, community); guard_m_side_argument_02 (actor 17, community); citizen_argument_m (actor 18, community); citizen_argument_f (actor 19, community); guard_m_side_distract_01 (actor 20, community); guard_m_side_distract_02 (actor 21, community); guard_f_side_distract (actor 22, community); nl_patrole_01_m_01 (actor 23, community); nl_patrole_01_f_01 (actor 24, community); guard_f_front_push_civilian (actor 25, community); civilian_f_push_civilian (actor 26, community); citizen_passerby_f_01 (actor 27, community); citizen_passerby_f_02 (actor 28, community); citizen_passerby_m_01 (actor 29, community); kurt_krauser (actor 30, spawnDespawn); songbird_hologram (actor 31, spawnDespawn); songbird_catwalk (actor 32, spawnDespawn); cop_car (actor 33, community); car_distraction (actor 34, community); sf1 (actor 35, community); Player (actor 36, findInContext).

Entries: `border` → 14; `trash_container` → 4808; `entrance_songbird` → 74; `sb_entrance` → 75; `sb_ask_price` → 1064; `ncpd` → 4896; `Start 28` → 4898; `slide_platform` → 4907; `slide_platform_idle` → 4917; `sb_garage_bridge_wait` → 1117; `truck_inspection` → 4964; `sb_garage_elevator_ride` → 1144; `corpo_gate` → 5025; `sb_comment_success` → 4071; `citizen_argument` → 5045; `sb_reaction_techie_path` → 5048; `sb_reaction_netrunner_path` → 5049; `sb_power_alt` → 273; `sb_access_point` → 283; `gate_consequences_start` → 6032; `sb_garage_access` → 293; `border_sicknesss_start` → 8969; `sb_nl_friendly` → 4226; `slide_platform_preview_only` → 7156; `chat_nl_kurts` → 3344; `parking_lot_in` → 2430; `fx_test` → 4382; `sb_unstable_platforms` → 4411; `side_entrance_gate` → 7295; `sb_warning_ladder_bridge` → 4444; `push_platform` → 3522; `Push_Aside_Entry` → 5444; `q301_kurtz_rules_in` → 7365; `dead_access_point_start` → 6432; `Start 14` → 1666; `sb_garage_platform_collapse` → 3589; `sb_garage_elevator` → 720; `citizen_argument_f` → 9355; `passerby` → 5531; `sidewalk_warning` → 7450; `sb_garage_complain_climbing` → 3628; `side_gate_preview` → 7468; `questfail_warning_01` → 6517; `sb_garage_tunnel` → 780; `questfail_warning_02` → 6523; `questfail` → 6534; `failstate_preview` → 8454; `questfail_awake` → 6579; `border_offensive_path` → 6636; `Start 20` → 3814.

Exits: `border_done` → 18; `sb_comment_success_done` → 7721; `entrance_songbird_done` → 78; `sb_access_point_done` → 1039; `sb_ask_price_done` → 1068; `End1` → 7778; `sb_garage_bridge_wait_done` → 1127; `sb_garage_elevator_ride_done` → 1148; `sb_access_point_clear` → 4067; `sb_reaction_techie_path_done` → 5052; `sb_reaction_netrunner_path_done` → 5056; `sb_garage_access_platform_start` → 6987; `gate_consequences_end` → 6051; `border_sicknesss_end` → 8970; `sb_nl_friendly_done` → 4233; `chat_nl_kurts_done` → 3348; `parking_lot_out` → 2432; `push_platform_car_fell` → 4385; `garage_access_update_journal` → 7263; `sb_warning_ladder_bridge_done` → 4446; `sb_entrance_done` → 635; `push_platform_done` → 3524; `q301_kurtz_rules_out` → 7368; `dead_access_point_end` → 6438; `sb_garage_platform_collapse_done` → 3593; `sb_garage_elevator_done` → 722; `sb_garage_complain_climbing_done` → 3632; `questfail_warning_01_done` → 6518; `questfail_warning_02_done` → 6524; `sb_garage_tunnel_done` → 782; `questfail_done` → 6535; `questfail_awake_done` → 6603; `border_offensive_path_done` → 6637; `power_journal_update` → 9553.

End nodes: 18: `NonTerminating`; 78: `Terminating`; 635: `Terminating`; 722: `Terminating`; 782: `NonTerminating`; 1039: `NonTerminating`; 1068: `Terminating`; 1127: `NonTerminating`; 1148: `Terminating`; 2432: `Terminating`; 3348: `Terminating`; 3524: `NonTerminating`; 3593: `NonTerminating`; 3632: `Terminating`; 4067: `Terminating`; 4233: `Terminating`; 4385: `NonTerminating`; 4446: `Terminating`; 5052: `Terminating`; 5056: `Terminating`; 6051: `Terminating`; 6438: `Terminating`; 6518: `Terminating`; 6524: `Terminating`; 6535: `NonTerminating`; 6603: `Terminating`; 6637: `Terminating`; 6987: `NonTerminating`; 7263: `NonTerminating`; 7368: `Terminating`; 7721: `Terminating`; 7778: `Terminating`; 8970: `Terminating`; 9553: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 20 | 2074 / 574 | `/Data/RootChunk/sceneGraph/Data/graph/77/Data/events/7` |
| `scnChangeIdleAnimEvent` | 37 | 1084 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/0` |
| `scnDialogLineEvent` | 215 | 15 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayTransitionEvent` | 22 | 1669 / 456 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/86` |
| `scnIKEvent` | 45 | 1669 / 439 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/74` |
| `scnLookAtEvent` | 102 | 1180 / 163 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/1` |
| `scnPlaySkAnimEvent` | 208 | 15 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnUnmountEvent` | 22 | 1669 / 455 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/85` |
| `scneventsAttachPropToWorld` | 1 | 8767 / 4281 | `/Data/RootChunk/sceneGraph/Data/graph/683/Data/events/0` |
| `scneventsEquipItemToPerformer` | 7 | 1669 / 282 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 22 | 1669 / 451 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/82` |
| `scneventsSocket` | 186 | 15 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsVFXEvent` | 28 | 3542 / 888 | `/Data/RootChunk/sceneGraph/Data/graph/112/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 54
- skeletal_animation, socket_signal: 9
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 8
- speech, socket_signal: 7
- skeletal_animation, idle_animation: 6
- skeletal_animation, audio, socket_signal: 5
- skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- props_equipment, socket_signal: 3
- socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze: 2
- skeletal_animation, gaze, vfx, socket_signal: 2
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1
- idle_animation: 1
- idle_animation, audio: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, vfx, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- props_equipment: 1
- skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `7f48785e49cbb38bdabf85ed14e56bdf11b0e5d1dcb6d624ecbedfda2dcc7cc0`. Binary SHA-256: `345d9e40acefcd86da2a3ec439248c01389d64b6b414178a66341bd54f95a551`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_01_border.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_01a_border_investigation.scene`

51 graph nodes, 51 edges; 6 event-bearing sections, 11 events; 32 screenplay lines, 9 screenplay options, 3 choice nodes.

Actors: songbird_holo (actor 0, findInContext); johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `inv_dead_smuggler` → 1; `kurtz_outpost_inv` → 88; `smuggler_stash_map` → 361; `smuggler_spot_01` → 376; `smuggler_spot_03` → 1006; `inv_civilian_camp` → 63.

Exits: `inv_dead_smuggler_done` → 2; `kurtz_outpost_inv_done` → 90; `inv_civilian_camp_done` → 65.

End nodes: 2: `Terminating`; 65: `Terminating`; 90: `Terminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 11 | 70 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6

Raw SHA-256: `484bd0fd36dffcd1bfe71400e1930a1d9a6639d9413b46c73cfdc7797b460ec4`. Binary SHA-256: `13d88e7140b1b89937640a899d153f66a6594195c72878fa5605db0cbb5729e7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_01a_border_investigation.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_02a_stadium.scene`

393 graph nodes, 464 edges; 45 event-bearing sections, 903 events; 263 screenplay lines, 24 screenplay options, 0 choice nodes.

Actors: preacher (actor 0, community); junk_citizen_m_01 (actor 1, community); junk_citizen_m_02 (actor 2, community); preacher_citizen_m_01 (actor 3, community); preacher_citizen_m_02 (actor 4, community); preacher_citizen_f_01 (actor 5, community); constr_citizen_stadium_f_01 (actor 6, community); constr_citizen_crash_m_01 (actor 7, community); constr_citizen_crash_m_02 (actor 8, community); shop_supplier_f_01 (actor 9, community); shop_supplier_m_01 (actor 10, community); worker_door_m_01 (actor 11, community); worker_door_m_02 (actor 12, community); armsdeal_dealer_f (actor 13, community); armsdeal_client_m (actor 14, community); drugdeal_dealer_f (actor 15, community); drugdeal_client_f (actor 16, community); discussion_armsdealer_m_01 (actor 17, community); discussion_armsdealer_m_02 (actor 18, community); sweatshop_worker_m (actor 19, community); sweatshop_worker_f (actor 20, community); shoptalk_vendor_f_01 (actor 21, community); shoptalk_vendor_f_02 (actor 22, community); kurt_bribe_client_m (actor 23, community); kurt_bribe_soldier_m (actor 24, community); corp_deal_vendor_m_01 (actor 25, community); corp_deal_vendor_m_02 (actor 26, community); thief_m_01 (actor 27, community); kurt_guard_f_01 (actor 28, community); kurt_guard_m_01 (actor 29, community); Songbird_holo (actor 30, findInContext); kurt (actor 31, spawnSet); kurt_announcement_guard_m_01 (actor 32, community); kurt_announcement_guard_m_02 (actor 33, community); armsdeal_client_f (actor 34, community); follower_m_01 (actor 35, community); Player (actor 36, findInContext).

Entries: `preacher` → 1; `citizens_junk` → 8; `citizen_construction` → 390; `kurt_announcement_start` → 1733; `market_reveal` → 1739; `ow_armsdeal` → 1448; `ow_drugdeal` → 1449; `ow_discussion` → 1450; `ow_sweatshop` → 1453; `ow_shoptalk` → 1454; `shop_suppliers` → 467; `kurt_bribe` → 1476; `corp_deal` → 1478; `reveal_preview_only` → 2833; `thief_scene_start` → 1521; `workers_door` → 557; `preview` → 917; `opening_vendor_start` → 1632.

Exits: `citizens_junk_done` → 14; `kurt_announcement_end` → 1734; `End 27` → 1745; `citizen_construction_fail` → 435; `citizen_construction_clear` → 439; `ow_armsdeal_done` → 1461; `ow_drugdeal_done` → 1462; `ow_discussion_done` → 1463; `ow_sweatshop_done` → 1464; `ow_shoptalk_done` → 1465; `kurt_bribe_done` → 1482; `corp_deal_done` → 1483; `thief_scene_end` → 1522; `workers_door_done` → 558; `arms_dealer_start` → 4261; `opening_vendor_end` → 1633.

End nodes: 14: `NonTerminating`; 435: `NonTerminating`; 439: `Terminating`; 558: `Terminating`; 1461: `NonTerminating`; 1462: `NonTerminating`; 1463: `NonTerminating`; 1464: `NonTerminating`; 1465: `NonTerminating`; 1482: `NonTerminating`; 1483: `NonTerminating`; 1522: `NonTerminating`; 1633: `NonTerminating`; 1734: `Terminating`; 1745: `NonTerminating`; 4261: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1740 / 1553 | `/Data/RootChunk/sceneGraph/Data/graph/73/Data/events/9` |
| `scnChangeIdleAnimEvent` | 70 | 391 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnDialogLineEvent` | 114 | 391 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnGameplayTransitionEvent` | 11 | 546 / 209 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/87` |
| `scnIKEvent` | 22 | 546 / 204 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/83` |
| `scnLookAtAdvancedEvent` | 8 | 1731 / 1461 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/8` |
| `scnLookAtEvent` | 162 | 546 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 273 | 391 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scnPoseCorrectionEvent` | 7 | 1480 / 864 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/6` |
| `scnUnmountEvent` | 11 | 546 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/88` |
| `scneventsCameraParamsEvent` | 2 | 1740 / 1564 | `/Data/RootChunk/sceneGraph/Data/graph/73/Data/events/14` |
| `scneventsEquipItemToPerformer` | 17 | 546 / 98 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/29` |
| `scneventsPlayRidCameraAnimEvent` | 6 | 1731 / 1460 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 11 | 546 / 207 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/86` |
| `scneventsSocket` | 182 | 391 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 3 | 546 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/32` |
| `scneventsUnequipItemFromPerformerByItem` | 3 | 546 / 181 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/73` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, gaze: 3
- gaze: 3
- skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, props_equipment, socket_signal: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation, gaze: 1
- idle_animation, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, rid_camera, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- gaze, socket_signal: 1

Raw SHA-256: `f8b04549f3d0274125a46a4a7cefdfd79dd40bc1469710c8fdd5dcb39eb8df3e`. Binary SHA-256: `180bdd9566d8f497095b52b35793f87462b3621e7d5c1a8117f32b0714971809`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_02a_stadium.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_02b_stadium_gameplay.scene`

138 graph nodes, 142 edges; 25 event-bearing sections, 160 events; 51 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: songbird_holo (actor 0, findInContext); songbird (actor 1, spawnDespawn); passerby_04 (actor 2, community); Player (actor 3, findInContext).

Entries: `sb_wrong_way` → 399; `sb_stadium_blackmarket` → 1; `sb_stadium_inner_circle_choice` → 555; `Start 13` → 1089; `sb_stadium_construction` → 27; `sb_stadium_roof` → 53; `sb_stadium_inner_circle_vendor` → 1010; `sb_stadium_lift` → 79; `sb_stadium_loot` → 370; `sb_stadium_sell` → 371; `somi_balcony_preview_only` → 1305; `sb_stadium_inner_circle` → 132.

Exits: `sb_stadium_inner_circle_done` → 134; `sb_stadium_blackmarket_done` → 2; `sb_wrong_way_done` → 403; `sb_stadium_inner_circle_choice_done` → 556; `sb_stadium_construction_construction` → 29; `sb_stadium_roof_done` → 55; `sb_stadium_inner_circle_vendor_done` → 1011; `sb_stadium_lift_done` → 81; `sb_stadium_loot_done` → 377; `sb_stadium_sell_done` → 380.

End nodes: 2: `<omitted>`; 29: `<omitted>`; 55: `<omitted>`; 81: `<omitted>`; 134: `<omitted>`; 377: `<omitted>`; 380: `<omitted>`; 403: `<omitted>`; 556: `<omitted>`; 1011: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 418 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/3` |
| `scnChangeIdleAnimEvent` | 8 | 655 / 386 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/7` |
| `scnDialogLineEvent` | 46 | 23 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 655 / 393 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/13` |
| `scnIKEvent` | 4 | 655 / 384 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/5` |
| `scnLookAtAdvancedEvent` | 2 | 870 / 534 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/20` |
| `scnLookAtEvent` | 25 | 655 / 375 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/0` |
| `scnPlaySkAnimEvent` | 37 | 418 / 141 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 872 / 575 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/8` |
| `scnUnmountEvent` | 2 | 655 / 392 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 2 | 655 / 388 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/9` |
| `scneventsSocket` | 23 | 415 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/3` |
| `scneventsVFXEvent` | 4 | 95 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, socket_signal: 2
- speech, skeletal_animation, audio, socket_signal: 2
- speech, vfx: 1
- skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1

Raw SHA-256: `eb3d30487381ac0caa4f991eea2e090a7de91e2daf6509e1d9d362b618f5b639`. Binary SHA-256: `fe801b8d68012a8cf04490db43ad68bbac960c0c717680a596e259798a2ad625`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_02b_stadium_gameplay.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_03_crash.scene`

224 graph nodes, 252 edges; 33 event-bearing sections, 199 events; 62 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: songbird (actor 0, spawnDespawn); johnny (actor 1, spawnDespawn); songbird_holo (actor 2, findInContext); rocket (actor 3, community); sf1 (actor 4, community); rocket2 (actor 5, community); ejecting_pod (actor 6, community); rocket_3 (actor 7, community); rocket_4 (actor 8, community); Player (actor 9, findInContext).

Entries: `Start 6` → 1564; `start` → 923; `chicken_test_wtc` → 2706; `fx_sf1_explosion` → 269; `Start 7` → 1644; `crash` → 335; `Start 9` → 3090.

Exits: `kurt_av_start` → 3115; `crash_done` → 116; `crash_clear` → 437.

End nodes: 116: `NonTerminating`; 437: `<omitted>`; 3115: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 13 | 1218 / 256 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/3` |
| `scnChangeIdleAnimEvent` | 7 | 452 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnDialogLineEvent` | 42 | 203 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 600 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/14` |
| `scnIKEvent` | 6 | 600 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/8` |
| `scnLookAtEvent` | 6 | 600 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scnPlaySkAnimEvent` | 26 | 452 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnUnmountEvent` | 3 | 600 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 3 | 600 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/10` |
| `scneventsSocket` | 48 | 452 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/6` |
| `scneventsVFXDurationEvent` | 11 | 1218 / 269 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/16` |
| `scneventsVFXEvent` | 31 | 600 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- skeletal_animation: 9
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- gaze: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, socket_signal: 1
- speech, audio, socket_signal: 1
- socket_signal: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `876250a66073d8805570ae273f73db18b267a82433fa790134b9e1b62ad52d43`. Binary SHA-256: `8d4768edcfc7114a4ecc1ff43d3b995e342d2cc1fc21554e01527b0a0eeb0b02`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_03_crash.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_04_way_to_crashsite.scene`

365 graph nodes, 420 edges; 52 event-bearing sections, 771 events; 151 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: kurt_speakers (actor 0, spawnDespawn); songbird (actor 1, findInContext); johnny (actor 2, spawnDespawn); debris_m_01 (actor 3, community); debris_m_02 (actor 4, community); debris_f_01 (actor 5, community); scavenger_m (actor 6, community); scavenger_f (actor 7, community); citizen_crashsite_m_01 (actor 8, community); citizen_crashsite_m_02 (actor 9, community); citizen_crashsite_f_01 (actor 10, community); citizen_crashsite_soldier_m (actor 11, community); citizen_crashsite_soldier_f (actor 12, community); kurtz_intro_m_01 (actor 13, community); kurtz_intro_m_02 (actor 14, community); kurtz_intro_m_03 (actor 15, community); kurtz_intro_f_01 (actor 16, community); kurtz_intro_f_02 (actor 17, community); kurtz_intro_soldier_m (actor 18, spawnSet); kurtz_intro_soldier_f (actor 19, spawnSet); discussion_soldier_m_01 (actor 20, community); discussion_soldier_m_02 (actor 21, community); discussion_soldier_f_01 (actor 22, community); discussion_soldier_f_02 (actor 23, community); youngster_m_01 (actor 24, community); youngster_m_02 (actor 25, community); history_m_01 (actor 26, community); history_f_01 (actor 27, community); history_f_02 (actor 28, community); loudspeaker_side (actor 29, spawnDespawn); citizen_cars_m_01 (actor 30, community); citizen_cars_m_02 (actor 31, community); citizen_landing_gear_f_01 (actor 32, community); citizen_landing_gear_m_01 (actor 33, community); citizen_landing_gear_m_02 (actor 34, community); doomsday_preacher (actor 35, community); doomsday_m_01 (actor 36, community); doomsday_m_02 (actor 37, community); doomsday_f_01 (actor 38, community); phone_m_01 (actor 39, community); blocked_car_driver (actor 40, community); blocked_car_soldier (actor 41, community); moving_car_driver_01 (actor 42, community); kurtz_truck (actor 43, community); kurtz_car (actor 44, community); blocked_car (actor 45, community); moving_car_01 (actor 46, community); Player (actor 47, findInContext).

Entries: `debris` → 7; `scavengers` → 8; `citizens_crashsite` → 9; `sb_combat_reaction` → 508; `kurtz_intro` → 11; `citizens_cars` → 1051; `citizens_landing_gear` → 1061; `questfail_awake` → 1346; `citizen_history` → 373; `citizens_youngsters` → 374; `chute` → 389; `questfail_warning_01` → 1137; `questfail_warning_02` → 1138; `questfail` → 1139; `doomsday` → 1189; `talking_on_phone` → 1206; `blocked_car` → 1212; `sb_sideway` → 485; `moving_car` → 1982.

Exits: `while V in chute` → 2997; `debris_done` → 12; `sb_combat_reaction_done` → 511; `scavengers_done` → 13; `citizens_crashsite_done` → 14; `kurtz_intro_done` → 15; `citizens_cars_done` → 1054; `citizens_landing_gear_done` → 1063; `questfail_awake_done` → 1350; `citizen_history_done` → 379; `citizens_youngsters_done` → 381; `questfail_warning_01_done` → 1140; `questfail_warning_02_done` → 1141; `questfail_done` → 1142; `chute_done` → 433; `doomsday_out` → 1190; `talking_on_phone_done` → 1207; `blocked_car_done` → 1214; `sb_sideway_done` → 487; `moving_car_done` → 1984.

End nodes: 12: `NonTerminating`; 13: `NonTerminating`; 14: `NonTerminating`; 15: `NonTerminating`; 379: `NonTerminating`; 381: `NonTerminating`; 433: `NonTerminating`; 487: `<omitted>`; 511: `<omitted>`; 1054: `NonTerminating`; 1063: `NonTerminating`; 1140: `<omitted>`; 1141: `<omitted>`; 1142: `<omitted>`; 1190: `NonTerminating`; 1207: `NonTerminating`; 1214: `NonTerminating`; 1350: `<omitted>`; 1984: `NonTerminating`; 2997: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 10 | 1304 / 1141 | `/Data/RootChunk/sceneGraph/Data/graph/99/Data/events/1` |
| `scnChangeIdleAnimEvent` | 17 | 25 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/7` |
| `scnDialogLineEvent` | 119 | 25 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/11` |
| `scnGameplayTransitionEvent` | 42 | 25 / 185 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/92` |
| `scnIKEvent` | 84 | 25 / 145 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/70` |
| `scnLookAtEvent` | 79 | 25 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/6` |
| `scnPlaySkAnimEvent` | 142 | 25 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |
| `scnUnmountEvent` | 42 | 25 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/91` |
| `scneventsEquipItemToPerformer` | 5 | 25 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/37` |
| `scneventsPlayRidCameraAnimEvent` | 1 | 2754 / 2262 | `/Data/RootChunk/sceneGraph/Data/graph/254/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 45 | 25 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/88` |
| `scneventsSocket` | 175 | 25 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 2 | 25 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/41` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 376 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/17` |
| `scneventsVFXEvent` | 7 | 1151 / 908 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 10
- skeletal_animation, socket_signal: 7
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, audio, vfx, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- audio: 1
- skeletal_animation: 1
- skeletal_animation, camera, rid_camera, socket_signal, animation_state: 1

Raw SHA-256: `c3cdf6860f5f50c8e5b9bae75bb200abbbbad6e3600ceba8cb1ef3187d8dda38`. Binary SHA-256: `6fe789d965d8b8fdf8c57231d91d03a344cc177d5dab582b5c65096dc535a8c9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_04_way_to_crashsite.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_05a_crashsite.scene`

121 graph nodes, 154 edges; 19 event-bearing sections, 166 events; 53 screenplay lines, 8 screenplay options, 3 choice nodes.

Actors: songbird (actor 0, spawnDespawn); constr_citizen_crash_m_01 (actor 1, community); av_01 (actor 2, community); av_02 (actor 3, community); av_03 (actor 4, community); Player (actor 5, findInContext).

Entries: `Start 0` → 1; `Start1` → 1000; `nonlin_bottom` → 310; `limit_UI` → 1094.

Exits: `arrival_done` → 2; `End 0` → 1002; `nonlin_bottom_refused` → 386; `arrival_clear` → 51; `nonlin_bottom_clear` → 456; `nonlin_bottom_done` → 458.

End nodes: 2: `NonTerminating`; 51: `<omitted>`; 386: `<omitted>`; 456: `<omitted>`; 458: `NonTerminating`; 1002: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 239 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/9` |
| `scnChangeIdleAnimEvent` | 3 | 15 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnDialogLineEvent` | 49 | 15 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnGameplayTransitionEvent` | 4 | 239 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/20` |
| `scnIKEvent` | 8 | 239 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/17` |
| `scnLookAtAdvancedEvent` | 1 | 239 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/7` |
| `scnLookAtEvent` | 26 | 15 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnPlaySkAnimEvent` | 34 | 15 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnUnmountEvent` | 4 | 239 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/19` |
| `scneventsSetAnimFeatureEvent` | 4 | 239 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/15` |
| `scneventsSocket` | 29 | 15 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsVFXEvent` | 2 | 15 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1

Raw SHA-256: `ac54b981fb8d4733809f7f94436752c9b3f0d001e318bc339cac9a0c5e7362f7`. Binary SHA-256: `32202c7f1fe6ea8c666ceac0b10f4c7cabb7510c27c18a1fa01f6c52d6547260`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_05a_crashsite.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_05b_crashsite_gameplay.scene`

88 graph nodes, 111 edges; 11 event-bearing sections, 51 events; 42 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: songbird_holo (actor 0, findInContext); bottom_enemy_005 (actor 1, community); bottom_enemy_006 (actor 2, community); bottom_enemy_001 (actor 3, community); bottom_enemy_002 (actor 4, community); bottom_enemy_016 (actor 5, community); bottom_enemy_014 (actor 6, community); bottom_enemy_008 (actor 7, community); bottom_enemy_009 (actor 8, community); AV_003 (actor 9, community); AV_004 (actor 10, community); Player (actor 11, findInContext).

Entries: `sb_guidance_01` → 1; `blockade` → 6; `sb_guidance_02` → 9; `nonlin_reinforcements_chat` → 295; `sb_hack_mech` → 304; `sb_hack_av` → 305; `Kurtz_man_chat` → 337; `AVs_start` → 344.

Exits: `sb_guidance_01_done` → 2; `blockade_done` → 8; `sb_guidance_02_done` → 11; `nonlin_reinforcements_chat_done` → 296; `sb_hack_av_done` → 308; `sb_hack_mech_done` → 311; `Kurtz_man_chat_done` → 339; `AVs_start_done` → 345.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 11: `<omitted>`; 296: `<omitted>`; 308: `<omitted>`; 311: `<omitted>`; 339: `<omitted>`; 345: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 380 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |
| `scnChangeIdleAnimEvent` | 2 | 425 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/2` |
| `scnDialogLineEvent` | 39 | 27 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 380 / 141 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/1` |
| `scneventsVFXDurationEvent` | 2 | 380 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- skeletal_animation, audio, vfx: 2
- skeletal_animation, idle_animation: 1

Raw SHA-256: `d383504b084bb605921cf5a6651f13ff7d5c405acb1883331c031e2c6535e260`. Binary SHA-256: `f30b5e7cec08266e80b022c79c16aae4750588311e7151887de76f5ca67a9299`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_05b_crashsite_gameplay.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_05c_crashsite_combat.scene`

243 graph nodes, 248 edges; 26 event-bearing sections, 100 events; 28 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Songbird (actor 0, findInContext); Kurtz_man (actor 1, community); reinf_001 (actor 2, community); reinf_002 (actor 3, community); reinf_003 (actor 4, community); reinf_028 (actor 5, community); reinf_029 (actor 6, community); reinf_030 (actor 7, community); reinf_004 (actor 8, community); reinf_005 (actor 9, community); reinf_006 (actor 10, community); reinf_025 (actor 11, community); reinf_026 (actor 12, community); reinf_027 (actor 13, community); reinf_010 (actor 14, community); reinf_011 (actor 15, community); reinf_012 (actor 16, community); reinf_020 (actor 17, community); reinf_022 (actor 18, community); reinf_023 (actor 19, community); reinf_031 (actor 20, community); reinf_032 (actor 21, community); Kurt_man_02 (actor 22, community); AV_001 (actor 23, community); AV_002 (actor 24, community); AV_003 (actor 25, community); AV_004 (actor 26, community); AV_005 (actor 27, community); AV_crushed (actor 28, community).

Entries: `sb_layout` → 1; `sb_reinforcements` → 16; `km_enemy_behind` → 22; `sb_fuel_tank` → 28; `sb_debris` → 54; `sb_reveal` → 58; `crane_preview` → 1544; `sb_close` → 64; `reinforcements_001_in` → 81; `reinforcements_001a_in` → 1310; `crane_falling_in` → 1318; `crane_idle_in` → 1322; `sb_wrong_direction` → 1352; `sb_enemies_roof_defeated_warning` → 1361; `sb_generator_hint` → 1373; `km_who_this` → 1381; `reinforcements_003_in` → 789; `AV_hacked_reinf_comin` → 1093; `reinforcements_002_in` → 544.

Exits: `reinforcements_reinf_004_done` → 594; `sb_layout_done` → 2; `km_enemy_behind_end` → 24; `reinforcements_reinf_005_done` → 620; `sb_fuel_tank_done` → 30; `reinforcements_reinf_006_done` → 626; `Crane_Variant_Change` → 1523; `sb_reveal_done` → 59; `sb_close_done` → 65; `reinforcements_reinf_025_done` → 660; `reinforcements_001_done` → 85; `reinforcements_reinf_026_done` → 686; `reinforcements_reinf_027_done` → 692; `reinforcements_reinf_028_done` → 412; `AV_hacked_reinf_comin_done` → 1307; `reinforcements_001a_done` → 1313; `reinforcements_reinf_029_done` → 438; `reinforcements_reinf_030_done` → 444; `crane_falling_out` → 1336; `crane_idle_out` → 1338; `sb_wrong_direction_done` → 1353; `reinforcements_reinf_001_done` → 165; `sb_enemies_roof_defeated_warning_done` → 1362; `sb_generator_hint_done` → 1374; `km_who_this_done` → 1382; `reinforcements_003_done` → 791; `AV_comin` → 1404; `reinforcements_reinf_002_done` → 232; `reinforcements_reinf_003_done` → 240; `reinforcements_reinf_010_done` → 839; `reinforcements_002_done` → 546; `reinforcements_reinf_011_done` → 865; `reinforcements_reinf_012_done` → 871.

End nodes: 2: `<omitted>`; 24: `<omitted>`; 30: `<omitted>`; 59: `<omitted>`; 65: `<omitted>`; 85: `<omitted>`; 165: `NonTerminating`; 232: `NonTerminating`; 240: `NonTerminating`; 412: `NonTerminating`; 438: `NonTerminating`; 444: `NonTerminating`; 546: `<omitted>`; 594: `NonTerminating`; 620: `NonTerminating`; 626: `NonTerminating`; 660: `NonTerminating`; 686: `NonTerminating`; 692: `NonTerminating`; 791: `<omitted>`; 839: `NonTerminating`; 865: `NonTerminating`; 871: `NonTerminating`; 1307: `<omitted>`; 1313: `<omitted>`; 1336: `NonTerminating`; 1338: `NonTerminating`; 1353: `<omitted>`; 1362: `<omitted>`; 1374: `<omitted>`; 1382: `<omitted>`; 1404: `NonTerminating`; 1523: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 13 | 144 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/1` |
| `scnChangeIdleAnimEvent` | 2 | 1316 / 890 | `/Data/RootChunk/sceneGraph/Data/graph/161/Data/events/6` |
| `scnDialogLineEvent` | 12 | 12 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 30 | 144 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/0` |
| `scneventsSocket` | 17 | 144 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/6` |
| `scneventsVFXDurationEvent` | 14 | 144 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/5` |
| `scneventsVFXEvent` | 12 | 1212 / 819 | `/Data/RootChunk/sceneGraph/Data/graph/148/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- skeletal_animation: 6
- skeletal_animation, audio, vfx, socket_signal: 5
- skeletal_animation, audio, vfx: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `dca2bad346e892d9d81c10cc32f37e961a39c4f603704f76af71b8b8704e540b`. Binary SHA-256: `e9449fb1a987b9131d7bb317caef75a45019e6caf1e0b69cd67b27b75498d652`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_05c_crashsite_combat.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_06a_shuttle_arrival.scene`

176 graph nodes, 220 edges; 35 event-bearing sections, 310 events; 69 screenplay lines, 21 screenplay options, 5 choice nodes.

Actors: myers (actor 0, spawnSet); fss_01 (actor 1, community); songbird (actor 2, spawnDespawn); kurt_m_01 (actor 3, community); kurt_m_02 (actor 4, community); kurt_m_03 (actor 5, community); songbird_holo (actor 6, findInContext); kurt_m_04_trailer (actor 7, community); kurt_m_05_trailer (actor 8, community); Player (actor 9, findInContext).

Entries: `fx_explosion_preview` → 399; `Start 0` → 1; `Start 3` → 439; `Start1` → 1500; `Start 4` → 530; `Start 5` → 1165; `sb_arrival` → 369.

Exits: `End 0` → 2; `clear` → 78; `End1` → 1502; `sb_arrival_done` → 370.

End nodes: 2: `NonTerminating`; 78: `<omitted>`; 370: `<omitted>`; 1502: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 26 | 451 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/4` |
| `scnChangeIdleAnimEvent` | 14 | 514 / 217 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/1` |
| `scnDialogLineEvent` | 38 | 185 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnGameplayTransitionEvent` | 6 | 811 / 482 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/21` |
| `scnIKEvent` | 14 | 811 / 459 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/2` |
| `scnLookAtAdvancedEvent` | 6 | 1196 / 895 | `/Data/RootChunk/sceneGraph/Data/graph/105/Data/events/3` |
| `scnLookAtEvent` | 6 | 568 / 268 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/12` |
| `scnPlaySkAnimEvent` | 72 | 30 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 6 | 811 / 491 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/28` |
| `scneventsAttachPropToNode` | 1 | 811 / 481 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/20` |
| `scneventsAttachPropToPerformer` | 1 | 811 / 470 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/9` |
| `scneventsCameraEvent` | 1 | 1196 / 891 | `/Data/RootChunk/sceneGraph/Data/graph/105/Data/events/0` |
| `scneventsCameraParamsEvent` | 17 | 568 / 266 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/10` |
| `scneventsEquipItemToPerformer` | 9 | 451 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 6 | 811 / 484 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/23` |
| `scneventsSocket` | 66 | 30 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scneventsVFXDurationEvent` | 5 | 451 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/6` |
| `scneventsVFXEvent` | 16 | 451 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- skeletal_animation, audio, socket_signal: 4
- skeletal_animation: 4
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- speech, audio, socket_signal: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, audio: 1
- speech, skeletal_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, camera, socket_signal: 1

Raw SHA-256: `35f030c088a3d930965700d78156de2c5107def1358e77b3203de4f3b265d46a`. Binary SHA-256: `cef238230e1689c692eb759ddada64b397093fb2c921b4b059702ce02a579ef1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_06a_shuttle_arrival.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_06b_shuttle_combat.scene`

19 graph nodes, 15 edges; 4 event-bearing sections, 10 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: myers (actor 0, spawnSet); Mech (actor 1, community); Player (actor 2, findInContext).

Entries: `myers_orders` → 9; `myers_situation` → 70; `Mech Spawn Debug` → 52; `myers_cover` → 75.

Exits: `myers_cover_done` → 76; `myers_orders_done` → 10; `myers_situation_done` → 71; `Mech Spawn Debug End` → 54.

End nodes: 10: `<omitted>`; 54: `<omitted>`; 71: `<omitted>`; 76: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 35 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnDialogLineEvent` | 5 | 72 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 35 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsSocket` | 1 | 35 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scneventsVFXEvent` | 1 | 35 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- skeletal_animation, audio, vfx, socket_signal: 1

Raw SHA-256: `4fbebbca4ecf1c56add31c848f2bc8ccceba1c02c0883f4bde8dff910ee09c41`. Binary SHA-256: `94c98707a68d2289190996cc9d9a72701aae29b08bf4aa5e0615cad57416160b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_06b_shuttle_combat.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_06c_shuttle_escape.scene`

61 graph nodes, 67 edges; 10 event-bearing sections, 30 events; 21 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: myers (actor 0, spawnSet); songbird (actor 1, findInContext); Player (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `End1` → 1078; `End 1` → 141.

End nodes: 141: `NonTerminating`; 1078: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 1115 / 367 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/2` |
| `scnDialogLineEvent` | 14 | 219 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnLookAtEvent` | 1 | 1051 / 282 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/3` |
| `scnPlaySkAnimEvent` | 5 | 95 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 1051 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/7` |
| `scneventsAttachPropToPerformer` | 2 | 1051 / 281 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/2` |
| `scneventsSocket` | 5 | 95 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, socket_signal: 2
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, animation_state: 1

Raw SHA-256: `04a7e5fad1328bcd43f8f459aae7300d46337f482cf220532e3dd301a775c19b`. Binary SHA-256: `29b7ed0bc428339bf0e29d0e3f71f8c173bfa2bf3b71593ea06105243bbce5b4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_06c_shuttle_escape.scene" --events
```

## `ep1\quest\main_quests\q301\scenes\q301_07_shuttle_myers.scene`

225 graph nodes, 292 edges; 44 event-bearing sections, 309 events; 156 screenplay lines, 25 screenplay options, 5 choice nodes.

Actors: songbird (actor 0, findInContext); myers (actor 1, spawnSet); johnny (actor 2, spawnDespawn); communication_device (actor 3, spawnDespawn); guard_m_search_01 (actor 4, community); guard_m_search_02 (actor 5, community); guard_m_search_03 (actor 6, community); guard_m_search_04 (actor 7, community); drone (actor 8, community); guard_car (actor 9, community); drone_carrier (actor 10, community); Player (actor 11, findInContext).

Entries: `Start 0` → 1; `tracker` → 2824; `break_bottle` → 2972.

Exits: `Drone_fight` → 4990; `End 1` → 440; `q302_elevator_line` → 4474; `q302_dialogue_starts` → 3969; `q301_spot_check_for_reaction` → 3977.

End nodes: 440: `NonTerminating`; 3969: `NonTerminating`; 3977: `NonTerminating`; 4474: `NonTerminating`; 4990: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 21 | 2719 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/2` |
| `scnChangeIdleAnimEvent` | 18 | 1913 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnDialogLineEvent` | 59 | 1319 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 2810 / 358 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/19` |
| `scnIKEvent` | 6 | 2810 / 333 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/1` |
| `scnLookAtEvent` | 62 | 1913 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnPlaySkAnimEvent` | 29 | 1913 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnUnmountEvent` | 3 | 2810 / 363 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/23` |
| `scneventsAttachPropToNode` | 7 | 2799 / 317 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/7` |
| `scneventsAttachPropToPerformer` | 9 | 2719 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 2743 / 255 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/18` |
| `scneventsCameraParamsEvent` | 9 | 2719 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/1` |
| `scneventsEquipItemToPerformer` | 6 | 2810 / 335 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 3 | 2810 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/20` |
| `scneventsSocket` | 64 | 1319 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 1 | 2897 / 389 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/5` |
| `scneventsVFXDurationEvent` | 1 | 2810 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/14` |
| `scneventsVFXEvent` | 7 | 2799 / 316 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, socket_signal: 5
- skeletal_animation, idle_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, gaze: 2
- speech, gaze, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 2
- speech, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 2
- skeletal_animation, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, idle_animation: 1
- props_equipment: 1
- skeletal_animation, props_equipment: 1
- gaze: 1
- skeletal_animation: 1

Raw SHA-256: `b87a57ee959081202c5f8a55ce1a70ecb9f906966b9e74c169484bb9ed0eed45`. Binary SHA-256: `21eaf43dd04f2cd256e90a8d58f7a2efeb125dd006e63388bbee68481baac052`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q301\scenes\q301_07_shuttle_myers.scene" --events
```

## `ep1\quest\main_quests\q302\scenes\q302_01_escape_the_cz.scene`

1231 graph nodes, 1768 edges; 117 event-bearing sections, 393 events; 180 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Myers (actor 0, spawnSet); Drone (actor 1, community); small_drone_1 (actor 2, spawnDespawn); small_drone_2 (actor 3, spawnDespawn); small_drone_3 (actor 4, spawnDespawn); small_drone_4 (actor 5, spawnDespawn); small_drone_5 (actor 6, spawnDespawn); small_drone_6 (actor 7, spawnDespawn); small_drone_7 (actor 8, spawnDespawn); small_drone_8 (actor 9, spawnDespawn); small_drone_9 (actor 10, spawnDespawn); small_drone_10 (actor 11, spawnDespawn); small_drone_11 (actor 12, spawnDespawn); small_drone_12 (actor 13, spawnDespawn); small_drone_13 (actor 14, spawnDespawn); small_drone_14 (actor 15, spawnDespawn); small_drone_15 (actor 16, spawnDespawn); small_drone_16 (actor 17, spawnDespawn); small_drone_17 (actor 18, spawnDespawn); small_drone_18 (actor 19, spawnDespawn); small_drone_19 (actor 20, spawnDespawn); q302_hotel_militia_1 (actor 21, community); q302_hotel_militia_2 (actor 22, community); q302_hotel_militia_5 (actor 23, community); q302_hotel_militia_8 (actor 24, community); q302_hotel_militia_7 (actor 25, community); Songbird_holo (actor 26, findInContext); q302_drone_flyby_1 (actor 27, spawnDespawn); q302_drone_flyby_2 (actor 28, spawnDespawn); q302_hotel_militia_10 (actor 29, community); q302_hotel_militia_4 (actor 30, community); q302_hotel_militia_3 (actor 31, community); q302_escape_car (actor 32, spawner); q302_escape_car_alt (actor 33, spawner); q302_hotel_av_01 (actor 34, community); q302_hotel_av_02 (actor 35, community); q302_hotel_av_03 (actor 36, community); q302_hotel_av_04 (actor 37, community); Player (actor 38, findInContext); Songbird (actor 39, findInContext).

Entries: `q302_01_escape_elevator_line` → 11028; `arrived_at_parking_prev` → 8652; `drone_surveillance_prev` → 2714; `drone_distract_prev` → 10101; `drone_intro_prev` → 1632; `Pre_drone` → 1664; `q302_01_escape_in` → 542; `on foot akebono` → 9385; `elevator_prev` → 8419; `upper_floor_prev` → 2336; `q302_01_escape_chat` → 10924; `get_into_car_prev` → 8521.

Exits: `Militia alerted after skybridge` → 2608; `Escape_chase` → 3231; `q302_01_escape_out` → 873; `patrols_cleanup` → 5778; `Player has entered the lobby` → 2176; `Combat trigerred from the restaurant` → 2195; `Player exit the vent` → 2201; `clear` → 5896.

End nodes: 873: `NonTerminating`; 2176: `NonTerminating`; 2195: `NonTerminating`; 2201: `NonTerminating`; 2608: `NonTerminating`; 3231: `NonTerminating`; 5778: `NonTerminating`; 5896: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 1625 / 288 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/6` |
| `scnChangeIdleAnimEvent` | 12 | 1360 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/0` |
| `scnDialogLineEvent` | 152 | 550 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 1563 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/14` |
| `scnIKEvent` | 6 | 1563 / 212 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/6` |
| `scnLookAtEvent` | 34 | 1360 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/2` |
| `scnPlaySkAnimEvent` | 87 | 1360 / 143 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/7` |
| `scnUnmountEvent` | 3 | 1563 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/13` |
| `scneventsAttachPropToPerformer` | 6 | 8643 / 4541 | `/Data/RootChunk/sceneGraph/Data/graph/675/Data/events/4` |
| `scneventsCameraParamsEvent` | 2 | 2475 / 688 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 4 | 1563 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/10` |
| `scneventsSocket` | 41 | 1360 / 139 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/3` |
| `scneventsVFXDurationEvent` | 1 | 1625 / 292 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/10` |
| `scneventsVFXEvent` | 35 | 1625 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 79
- gaze: 7
- skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, vfx: 2
- skeletal_animation: 2
- speech, socket_signal: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, camera, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- vfx, socket_signal: 1

Raw SHA-256: `4d1d3a21e6f0aaf3998300bc88e882a4ce5e3df546dea1a3ff1c6fb26474d4ff`. Binary SHA-256: `367734b0408cdb06d2f29b242279b0818994a49bc7ff32d5ee2c843d36eac1e5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q302\scenes\q302_01_escape_the_cz.scene" --events
```

