# Beat on the Brat: scene presentation

Journal identity: `quests/minor_quest/mq025_psycho_brawl`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq025_psycho_brawl.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\prologue\q001\scenes\q001_02a_fistfight_tutorial.scene`

115 graph nodes, 139 edges; 22 event-bearing sections, 87 events; 27 screenplay lines, 5 screenplay options, 3 choice nodes.

Actors: fistfight_robot (actor 0, community); fistfight_human (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `Start 0` → 1; `after_fistfight_in` → 317; `q001_02a_robot_down_in` → 739.

Exits: `fistfight_out` → 315; `Cleanup` → 629.

End nodes: 315: `NonTerminating`; 629: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 15 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 537 / 268 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/7` |
| `scnIKEvent` | 4 | 537 / 261 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/1` |
| `scnLookAtEvent` | 15 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 28 | 32 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 2 | 537 / 267 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 2 | 537 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/5` |
| `scneventsSocket` | 17 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 7
- speech, skeletal_animation: 3
- speech: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze: 2
- skeletal_animation, gaze: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- gaze: 1

Raw SHA-256: `40fefc258b55c8ed0ecb399dc6cd5244fd7dea07670a7cbcabbdfec4f5eac470`. Binary SHA-256: `f315616211d560ad85834754418c270fd27f456e9afe5b65b8d26587f6e8d1d8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_02a_fistfight_tutorial.scene" --events
```

## `base\quest\minor_quests\mq025\scenes\mq025_02_kabuki_new.scene`

165 graph nodes, 191 edges; 38 event-bearing sections, 240 events; 61 screenplay lines, 8 screenplay options, 5 choice nodes.

Actors: Certo_Twin_01 (actor 0, community); Esquerdo_Twin_02 (actor 1, community); dynamic_man_01 (actor 2, community); dynamic_woman_01 (actor 3, community); dynamic_woman_02 (actor 4, community); static_man_01 (actor 5, community); static_man_02 (actor 6, community); static_man_03 (actor 7, community); static_man_04 (actor 8, community); static_man_05 (actor 9, community); static_woman_01 (actor 10, community); static_woman_02 (actor 11, community); static_woman_03 (actor 12, community); static_woman_04 (actor 13, community); static_woman_05 (actor 14, community); V (actor 15, findInContext).

Entries: `mq025_02_cheering_crowd_in` → 773; `mq025_02_start_in` → 7; `mq025_02_after_in` → 25; `mq025_02_down_in` → 99.

Exits: `mq025_02_fight` → 20; `fight prep` → 21; `mq025_02_cheering_crowd_out` → 792; `mq025_02_after_out` → 35; `mq025_02_down_out` → 207.

End nodes: 20: `NonTerminating`; 21: `NonTerminating`; 35: `NonTerminating`; 207: `<omitted>`; 792: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 12 | 28 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scnDialogLineEvent` | 53 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 1130 / 1211 | `/Data/RootChunk/sceneGraph/Data/graph/160/Data/events/14` |
| `scnIKEvent` | 4 | 1130 / 1190 | `/Data/RootChunk/sceneGraph/Data/graph/160/Data/events/1` |
| `scnLookAtEvent` | 38 | 9 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnPlaySkAnimEvent` | 106 | 6 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnUnmountEvent` | 2 | 1130 / 1210 | `/Data/RootChunk/sceneGraph/Data/graph/160/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 2 | 1130 / 1199 | `/Data/RootChunk/sceneGraph/Data/graph/160/Data/events/6` |
| `scneventsSocket` | 21 | 13 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 11
- speech: 7
- skeletal_animation, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, gaze: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, socket_signal: 2
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, idle_animation: 1
- skeletal_animation, gaze: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `f462e96f431cd0125622bf0ae870fb0ecf169c4c088bcf31a3414745f1d967a4`. Binary SHA-256: `399e2c992f30df5d6fcff880079c7d92d745db791d7d6385b75801b75cbd2f49`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq025\scenes\mq025_02_kabuki_new.scene" --events
```

## `base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene`

105 graph nodes, 117 edges; 25 event-bearing sections, 180 events; 51 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: Buck (actor 0, community); crowd_01 (actor 1, community); crowd_02 (actor 2, community); crowd_03 (actor 3, community); 6th (actor 4, community); mq025_arroyo_vehicle (actor 5, spawner); V (actor 6, findInContext).

Entries: `mq025_03_bottles_in` → 101; `mq025_03_start_in` → 7; `mq025_03_after_in` → 24; `mq025_03_post_in` → 144; `mq025_03_loot_in` → 88.

Exits: `mq025_03_bottles_out` → 104; `fight prep` → 20; `mq025_03_fight` → 23; `Cleanup` → 607; `mq025_03_after_out` → 129; `mq025_03_after_out_fight` → 34; `mq025_03_post_out` → 146; `mq025_03_loot_out` → 91.

End nodes: 20: `NonTerminating`; 23: `<omitted>`; 34: `<omitted>`; 91: `<omitted>`; 104: `<omitted>`; 129: `NonTerminating`; 146: `<omitted>`; 607: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 16 | 9 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 46 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |
| `scnGameplayTransitionEvent` | 2 | 466 / 495 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/11` |
| `scnIKEvent` | 4 | 466 / 488 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/5` |
| `scnLookAtEvent` | 30 | 6 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 60 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnUnmountEvent` | 2 | 466 / 494 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/10` |
| `scneventsEquipItemToPerformer` | 2 | 9 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 2 | 466 / 490 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/7` |
| `scneventsSocket` | 16 | 9 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, skeletal_animation, gaze: 4
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- idle_animation, gaze: 1

Raw SHA-256: `7dc6c68ca84cdd8d3420779eba44da768f7036923c16509d666b0f0ea98bec90`. Binary SHA-256: `2a4e5bdd96c40af1392c2984bdf3a824c90cf832c66db793ea0ccde89a928827`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq025\scenes\mq025_03_arroyo.scene" --events
```

## `base\quest\minor_quests\mq025\scenes\mq025_05_glen.scene`

162 graph nodes, 182 edges; 33 event-bearing sections, 222 events; 61 screenplay lines, 11 screenplay options, 5 choice nodes.

Actors: Cesar (actor 0, community); Micaela (actor 1, community); Johnny (actor 2, spawnDespawn); cesars_car (actor 3, spawner); V (actor 4, findInContext).

Entries: `Start 1` → 829; `mq025_05_approach` → 832; `mq025_05_start_in` → 4; `mq025_05_after_in` → 21; `mq025_05_fluff_02_in` → 38.

Exits: `Cesar_cin_out` → 838; `mq025_05_fight` → 16; `fight prep` → 17; `mq025_05_start_out` → 20; `mq025_05_cleanup` → 721; `mq025_05_after_out` → 31; `mq025_05_fluff_02_out` → 40; `Cesar_cin` → 890.

End nodes: 16: `NonTerminating`; 17: `NonTerminating`; 20: `<omitted>`; 31: `NonTerminating`; 40: `<omitted>`; 721: `<omitted>`; 838: `<omitted>`; 890: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 6 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/14` |
| `scnChangeIdleAnimEvent` | 16 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnDialogLineEvent` | 52 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |
| `scnGameplayTransitionEvent` | 4 | 6 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/45` |
| `scnIKEvent` | 8 | 6 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/34` |
| `scnLookAtEvent` | 20 | 3 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 75 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/5` |
| `scnPoseCorrectionEvent` | 2 | 258 / 573 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/3` |
| `scnUnmountEvent` | 4 | 6 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/43` |
| `scneventsEquipItemToPerformer` | 1 | 602 / 842 | `/Data/RootChunk/sceneGraph/Data/graph/105/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 4 | 6 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/42` |
| `scneventsSocket` | 31 | 6 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsVFXEvent` | 4 | 95 / 368 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation: 4
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, vfx: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `4e33433727d8d1ec7e1c8d75aa4da1b806e7719c73653e14f547c7e7169d8e7d`. Binary SHA-256: `c20bb29934c1bea092c832a3aec3363d47aef309037f702a3dca5f3dbaeef704`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq025\scenes\mq025_05_glen.scene" --events
```

## `base\quest\minor_quests\mq025\scenes\mq025_06_pacifica.scene`

84 graph nodes, 92 edges; 22 event-bearing sections, 129 events; 47 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: Ozob (actor 0, spawnSet); Announcer (actor 1, community); Clown_Car (actor 2, spawner); V (actor 3, findInContext).

Entries: `mq025_06_ozob_start_in` → 88; `mq025_06_ozob_after_in` → 105; `mq025_ozob_alive_outro_in` → 222.

Exits: `ozob_explosion` → 178; `mq025_06_ozob_fight` → 100; `fight prep_ozob` → 101; `mq025_06_ozob_start_out` → 104; `mq025_06_ozob_after_out` → 115.

End nodes: 100: `NonTerminating`; 101: `NonTerminating`; 104: `<omitted>`; 115: `<omitted>`; 178: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 87 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnDialogLineEvent` | 42 | 87 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 122 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/8` |
| `scnIKEvent` | 2 | 122 / 208 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/1` |
| `scnLookAtEvent` | 14 | 96 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 48 | 87 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnUnmountEvent` | 1 | 122 / 215 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 1 | 122 / 213 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/6` |
| `scneventsSocket` | 13 | 87 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 6
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, gaze: 2
- speech: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `3e01462c4f8bbfa6375b8364a3a3b7095be16565adbeb51fc6fdf8323bb455c1`. Binary SHA-256: `8d4c8f0cff236842cc1e20cb97a532e655dcbd3c39573ce631d35be300035788`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq025\scenes\mq025_06_pacifica.scene" --events
```

## `base\quest\minor_quests\mq025\scenes\mq025_07_fight_club.scene`

64 graph nodes, 71 edges; 21 event-bearing sections, 146 events; 51 screenplay lines, 12 screenplay options, 5 choice nodes.

Actors: Rhino (actor 0, community); V (actor 1, findInContext).

Entries: `mq025_07_outro_in` → 123; `mq025_07_start_in` → 7; `mq025_07_after_in` → 22.

Exits: `mq025_07_fight` → 18; `fight prep` → 19; `mq025_07_start_out` → 21; `mq025_07_after_out` → 31; `mq025_07_outro_out` → 120.

End nodes: 18: `NonTerminating`; 19: `NonTerminating`; 21: `<omitted>`; 31: `<omitted>`; 120: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 9 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnChangeIdleAnimEvent` | 11 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnDialogLineEvent` | 49 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnLookAtEvent` | 11 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnPlaySkAnimEvent` | 65 | 6 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scneventsSocket` | 8 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech: 2
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, idle_animation: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze: 1
- gaze: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `6ca0d0d4f479ac7a82f8eb772503c5c90e3c56d8cb6c2889ca8ad7ed5e7c19b7`. Binary SHA-256: `527b0887a6798db4840908383fb84b5ad7348e4d8c4605d0b24d527097a0b953`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq025\scenes\mq025_07_fight_club.scene" --events
```

## `base\quest\minor_quests\mq025\scenes\mq025_08_finale.scene`

324 graph nodes, 374 edges; 101 event-bearing sections, 477 events; 182 screenplay lines, 30 screenplay options, 20 choice nodes.

Actors: Trainer (actor 0, spawnSet); Kid (actor 1, community); Razor (actor 2, community); El_Cesar (actor 3, community); Rhino (actor 4, community); Creole_Guard (actor 5, community); Certo_Twin_01 (actor 6, community); Esquerdo_Twin_02 (actor 7, community); Victor (actor 8, community); Johnny (actor 9, spawnDespawn); V (actor 10, findInContext).

Entries: `mq025_08_razor_fluff_in` → 4; `mq025_08_start_in` → 7; `mq025_08_ending_in` → 346; `mq025_08_victor_fluff_tips_in` → 668; `mq025_08_ending_fluff_in` → 391; `Start 9` → 1629; `Start 10` → 1632; `mq025_fighters_fluff_in` → 167; `mq025_08_wait_in` → 770.

Exits: `mq025_08_fight_finale` → 306; `fight prep` → 307; `mq025_08_finale_out` → 308; `mq025_08_ending_out` → 389; `mq025_08_wait_out` → 773; `mq025_08_wait_spawn_everything` → 774; `mq025_08_finale_loser_out` → 234; `mq025_08_wait_cleanup` → 828.

End nodes: 234: `NonTerminating`; 306: `NonTerminating`; 307: `NonTerminating`; 308: `<omitted>`; 389: `<omitted>`; 773: `NonTerminating`; 774: `NonTerminating`; 828: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 772 / 1215 | `/Data/RootChunk/sceneGraph/Data/graph/150/Data/events/1` |
| `scnChangeIdleAnimEvent` | 21 | 106 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 146 | 106 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnGameplayTransitionEvent` | 9 | 257 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/9` |
| `scnIKEvent` | 18 | 257 / 181 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/3` |
| `scnLookAtEvent` | 53 | 106 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 151 | 106 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnUnmountEvent` | 9 | 257 / 187 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/8` |
| `scneventsCameraParamsEvent` | 8 | 1038 / 1753 | `/Data/RootChunk/sceneGraph/Data/graph/225/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 9 | 257 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/5` |
| `scneventsSocket` | 47 | 106 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 22
- speech, skeletal_animation: 12
- speech, skeletal_animation, gaze: 9
- skeletal_animation, socket_signal: 9
- camera: 8
- speech, skeletal_animation, idle_animation, gaze: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation: 4
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- gaze: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, socket_signal: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, audio, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `c5bd7ff9fb3ccc54b292b7e224b8c3fd30049b8a54cbd08e172c0488e2acba04`. Binary SHA-256: `dad236cc847fc85f785b5ddedf6d87f538f439571686ca66df6f667748b32def`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq025\scenes\mq025_08_finale.scene" --events
```

## `base\quest\primary_characters\vsets\vset_v.scene`

422 graph nodes, 365 edges; 171 event-bearing sections, 171 events; 171 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: vset_v (actor 0, findInContext).

Entries: `battlecry_curse` → 14; `scene_thanks` → 864; `scene_thanks_var_1` → 866; `scene_thanks_var_2` → 871; `scene_thanks_var_3` → 874; `battlecry_curse_var_1` → 29; `battlecry_curse_var_2` → 30; `interrupt` → 31; `scene_insult` → 879; `scene_insult_var_1` → 881; `interrupt_var_1` → 35; `interrupt_var_2` → 36; `scene_insult_var_2` → 886; `return` → 41; `follower_end_var_1` → 1311; `follower_end_var_2` → 1312; `scene_insult_var_3` → 889; `return_var_1` → 43; `follower_end_var_3` → 1313; `return_var_2` → 44; `follower_end` → 1314; `scene_insult_var_4` → 892; `scene_insult_var_5` → 895; `gp_vehicle_steal` → 481; `gp_vehicle_steal_var_1` → 483; `yelling_happy` → 1331; `gp_vehicle_steal_var_2` → 488; `gp_vehicle_steal_var_3` → 491; `yelling_happy_var_1` → 1340; `scene_holocall_start` → 917; `yelling_happy_var_2` → 1341; `yelling_happy_var_3` → 1342; `scene_holocall_start_var_1` → 919; `gp_vehicle_reckless` → 496; `gp_vehicle_reckless_var_1` → 498; `scene_holocall_start_var_2` → 924; `gp_vehicle_reckless_var_2` → 503; `scene_holocall_end` → 929; `gp_vehicle_reckless_var_3` → 506; `scene_holocall_end_var_1` → 931; `gp_vehicle_destroyed` → 511; `scene_holocall_end_var_2` → 936; `gp_vehicle_destroyed_var_1` → 513; `scene_crowd` → 940; `gp_vehicle_destroyed_var_2` → 518; `scene_crowd_var_1` → 942; `gp_vehicle_v_hit` → 522; `scene_crowd_var_2` → 947; `gp_vehicle_v_hit_var_1` → 524; `gp_vehicle_v_hit_var_2` → 529; `gp_vehicle_v_hit_var_3` → 532; `interrupt_phone` → 113; `interrupt_phone_var_1` → 117; `interrupt_phone_var_2` → 118; `timelapse` → 126; `reaction_wtf` → 974; `timelapse_var_1` → 128; `timelapse_var_2` → 129; `reaction_wtf_var_1` → 976; `reaction_wtf_var_2` → 981; `generic_7` → 1407; `reaction_wtf_var_3` → 984; `generic_9` → 1408; `interrupt_var_3` → 139; `generic_8` → 1409; `generic_3` → 1410; `generic_5` → 1411; `interrupt_var_4` → 142; `generic_6` → 1412; `reaction_inspect` → 989; `generic_10` → 1414; `reaction_inspect_var_1` → 991; `interrupt_var_5` → 145; `generic_1` → 1415; `generic_2` → 1416; `interrupt_var_6` → 148; `reaction_inspect_var_2` → 996; `interrupt_var_7` → 151; `reaction_inspect_var_3` → 999; `reaction_inspect_var_4` → 1002; `generic_4` → 1426; `generic_17` → 1427; `generic_19` → 1428; `reaction_inspect_var_5` → 1005; `generic_18` → 1429; `interrupt_var_8` → 160; `generic_13` → 1430; `generic_15` → 1431; `interrupt_var_9` → 162; `generic_16` → 1432; `generic_20` → 1433; `interrupt_var_10` → 164; `generic_11` → 1434; `generic_12` → 1435; `reaction_hostiles` → 1012; `generic_14` → 1436; `generic_27` → 1437; `reaction_hostiles_var_1` → 1014; `generic_29` → 1438; `generic_28` → 1439; `generic_23` → 1440; `generic_25` → 1441; `generic_26` → 1442; `reaction_hostiles_var_2` → 1019; `generic_30` → 1443; `interrupt_phone_var_3` → 174; `generic_21` → 1444; `interrupt_phone_var_4` → 175; `generic_22` → 1445; `reaction_hostiles_var_3` → 1022; `generic_24` → 1446; `generic_sickness_1` → 1447; `generic_sickness_3` → 1448; `reaction_hostiles_var_4` → 1025; `generic_sickness_2` → 1449; `interrupt_phone_var_5` → 180; `interrupt_phone_var_6` → 181; `reaction_hostiles_var_5` → 1028; `generic_sickness_4` → 1453; `interrupt_phone_var_7` → 185; `reaction_surprise` → 1035; `reaction_surprise_var_1` → 1037; `generic_sickness` → 1461; `return_var_3` → 196; `return_var_4` → 197; `return_var_5` → 202; `return_var_6` → 203; `return_var_7` → 207; `reaction_surprise_var_2` → 1056; `return_var_8` → 211; `return_var_9` → 212; `sts_wat_kab_04_distract_01` → 1905; `reaction_surprise_var_3` → 1059; `return_var_10` → 214; `reaction_curse` → 1064; `q112_parade_speech_sickness_in` → 1911; `reaction_curse_var_1` → 1066; `character_creation` → 1916; `reaction_curse_var_2` → 1071; `reaction_curse_var_3` → 1074; `battlecry_curse_var_3` → 228; `battlecry_curse_var_4` → 229; `reaction_curse_var_4` → 1077; `reaction_curse_var_5` → 1080; `battlecry_curse_var_5` → 234; `battlecry_curse_var_6` → 235; `battlecry_curse_var_7` → 238; `battlecry_curse_var_8` → 239; `reaction_happy` → 1087; `reaction_happy_var_1` → 1089; `battlecry_curse_var_9` → 246; `battlecry_curse_var_10` → 247; `reaction_happy_var_2` → 1094; `reaction_happy_var_3` → 1097; `generic_vendor_v1` → 1946; `reaction_shocked` → 1102; `generic_vendor_v2` → 1949; `reaction_shocked_var_1` → 1104; `generic_vendor_v3` → 1954; `reaction_shocked_var_2` → 1109; `reaction_shocked_var_3` → 1112; `generic_vendor_v4` → 1961; `reaction_sickness` → 1117; `reaction_sickness_01_var_1` → 1119; `reaction_sickness_01_var_2` → 1124; `hint_check` → 1136; `hint_check_var_1` → 1138; `hint_check_var_2` → 1143; `hint_check_var_3` → 1146; `hint_check_var_4` → 1149; `scene_johnny_move` → 1155; `scene_johnny_move_var_2` → 1162; `scene_johnny_move_var_3` → 1164; `scene_johnny_move_var_1` → 1170; `scene_johnny_shoot` → 1172; `scene_johnny_shoot_var_2` → 1175; `scene_johnny_shoot_var_3` → 1177; `scene_johnny_shoot_var_1` → 1179; `reaction_sickness_02_var_1` → 1195; `reaction_sickness_02_var_2` → 1196; `combat_ally_check` → 352; `combat_ally_check_var_1` → 354; `timelapse_var_3` → 780; `combat_ally_check_var_2` → 359; `timelapse_var_4` → 783; `combat_ally_check_var_3` → 362; `timelapse_var_5` → 786; `combat_ally_cover` → 367; `combat_ally_cover_var_1` → 369; `reaction_sickness_03_var_1` → 1219; `reaction_sickness_03_var_2` → 1220; `combat_ally_cover_var_2` → 374; `combat_ally_cover_var_3` → 377; `combat_ally_stealth` → 382; `combat_ally_stealth_var_1` → 384; `combat_ally_stealth_var_2` → 389; `combat_ally_stealth_var_3` → 392; `reaction_sickness_04_var_1` → 1242; `reaction_sickness_04_var_2` → 1243; `combat_ally_warning` → 397; `combat_ally_warning_var_1` → 399; `combat_ally_warning_var_2` → 410; `combat_ally_warning_var_3` → 413; `reaction_sickness_05_var_1` → 1265; `reaction_sickness_05_var_2` → 1266.

Exits: `timelapse_output` → 1297.

End nodes: 1297: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 171 | 16 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 171

Raw SHA-256: `a86e2b56dfac6fd163b0014605c3555f094870a69e0dc88b51809ee9d3e6c7dd`. Binary SHA-256: `816152da18c67c66bd850c38e721940f541c31737e689f287f3b0f09756a434a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\primary_characters\vsets\vset_v.scene" --events
```

