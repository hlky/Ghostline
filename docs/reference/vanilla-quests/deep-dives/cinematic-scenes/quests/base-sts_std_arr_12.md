# Gig: Desperate Measures: scene presentation

Journal identity: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_12`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_std_arr_12.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_12\scenes\sts_std_arr_12_car.scene`

84 graph nodes, 81 edges; 16 event-bearing sections, 51 events; 45 screenplay lines, 6 screenplay options, 1 choice nodes.

Actors: pedro (actor 0, findInContext); sts12_car (actor 1, community); V (actor 2, findInContext).

Entries: `arr_12_v_in_truck_pedro_call` → 6; `Start 0` → 504; `arr_12_guards_dead_pedro_call` → 70; `Start1` → 541; `attack_diner` → 263; `after_combat_in_diner_start` → 362; `arr_12_guards_attacking_you_pedro_call` → 90; `after_fail_start` → 373.

Exits: `content lock off` → 477; `arr_12_v_in_truck_pedro_call_out` → 9; `cut_scene_after_fail` → 411; `arr_12_pedro_second_call_end` → 37; `e_control_back` → 243; `netrunner_attack` → 254; `combat_e` → 256; `amazing_e` → 258; `signal release` → 352; `it_worked_e` → 260; `after_combat_in_diner_end` → 364; `after_fail_end` → 375.

End nodes: 9: `NonTerminating`; 37: `NonTerminating`; 243: `NonTerminating`; 254: `NonTerminating`; 256: `NonTerminating`; 258: `NonTerminating`; 260: `NonTerminating`; 352: `<omitted>`; 364: `NonTerminating`; 375: `<omitted>`; 411: `<omitted>`; 477: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 55 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnDialogLineEvent` | 41 | 7 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 55 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/6` |
| `scnPlaySkAnimEvent` | 1 | 55 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scneventsAttachPropToPerformer` | 1 | 55 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scneventsDespawnEntityEvent` | 1 | 55 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 55 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scneventsSocket` | 4 | 55 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, socket_signal: 2
- speech, skeletal_animation, props_equipment, audio, socket_signal, animation_state, mount_workspot, entity_lifecycle: 1

Raw SHA-256: `1663b4ae022f2af03f6e1f5b3344e8f238bb8d38ee9d723be076f671cf83f3c9`. Binary SHA-256: `6630c7cc84de70fb09949185baaa2b1e3e226d5a1c682a3c737dc0fd6a3b6e92`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_12\scenes\sts_std_arr_12_car.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_12\scenes\sts_std_arr_12_diner_scene.scene`

40 graph nodes, 42 edges; 6 event-bearing sections, 25 events; 10 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Pedro (actor 0, findInContext); Worker (actor 1, community); Convoy (actor 2, community); Garbage_truck (actor 3, community); V (actor 4, findInContext).

Entries: `Start 0` → 1; `start_after_combat` → 394.

Exits: `signal release` → 324; `End 0` → 2.

End nodes: 2: `NonTerminating`; 324: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 204 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnDialogLineEvent` | 4 | 35 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 204 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scneventsSocket` | 5 | 204 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/3` |
| `scneventsVFXEvent` | 9 | 204 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, audio, vfx, socket_signal: 2
- speech: 1
- vfx, socket_signal: 1
- speech, skeletal_animation, audio: 1
- skeletal_animation: 1

Raw SHA-256: `29c5f8b7f757de4931729cd69e7deacf2b0e4a70c42fb83c95ddccd4c3d2e31d`. Binary SHA-256: `4084dd7e05eb060f54bb0b74907e51ce7182a92b32fa73b65ca72b75f1209ac9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_12\scenes\sts_std_arr_12_diner_scene.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_12\scenes\sts_std_arr_12_holocall_debriefs.scene`

33 graph nodes, 46 edges; 3 event-bearing sections, 5 events; 5 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: El_Capitan (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 15.

Exits: `rejected_out` → 308; `success` → 16; `fail` → 249.

End nodes: 16: `<omitted>`; 249: `<omitted>`; 308: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 19 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `9d098ffadfc57c9b7c76779628ee850fc8b3d1cf1d4b30e835a56832fc678fa8`. Binary SHA-256: `63b7b97b0146fa350aa9668e78af93fd25b5ef4be5887ccf2cae5595bd692184`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_12\scenes\sts_std_arr_12_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_12\scenes\sts_std_arr_12_holocall_prebrief.scene`

23 graph nodes, 26 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: El_Capitan (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 15.

Exits: `rejected_out` → 259; `End 0` → 16.

End nodes: 16: `<omitted>`; 259: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `b22303ee8fb1268031e1625ade37551451496ab64d780b2cf2ca3a3b82c12024`. Binary SHA-256: `90aed09d82242ada655fba26ad5a6ac185cb802a9e07e2b0f68abb0abc3cd325`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_12\scenes\sts_std_arr_12_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_12\scenes\sts_std_arr_12_pedro.scene`

157 graph nodes, 194 edges; 37 event-bearing sections, 339 events; 129 screenplay lines, 29 screenplay options, 10 choice nodes.

Actors: Pedro (actor 0, findInWorld); V (actor 1, findInContext).

Entries: `arr_12_pedro_talk_room` → 1.

Exits: `signal release` → 702; `End1` → 336.

End nodes: 336: `NonTerminating`; 702: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 20 | 308 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 122 | 306 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnLookAtEvent` | 70 | 306 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 43 | 306 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsSocket` | 84 | 306 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 12
- speech, skeletal_animation, gaze, socket_signal: 9
- speech, gaze, socket_signal: 5
- speech, idle_animation, gaze, socket_signal: 4
- gaze: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze: 1

Raw SHA-256: `653d4890801c96ba2828e1afb80aa6eb92c244fd0b758614904951e02f805cf6`. Binary SHA-256: `05908dd4a883e1d38c4e0f05d1edd5e598d18385794fa51eb4f20cccbf88e8fa`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_12\scenes\sts_std_arr_12_pedro.scene" --events
```

