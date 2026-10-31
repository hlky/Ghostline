# The Space in Between: scene presentation

Journal identity: `quests/main_quest/act_01/q105_02_jigjig`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q105_02_jigjig.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\fixers\wakako\scenes\wakako_okada_default.scene`

120 graph nodes, 141 edges; 13 event-bearing sections, 96 events; 33 screenplay lines, 5 screenplay options, 1 choice nodes.

Actors: wakako_okada (actor 0, spawnSet); wakako_okada_holo (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `in` → 1; `holo_in` → 379; `welcome` → 48.

Exits: `out` → 2; `holo_out` → 403; `welcome_end` → 887.

End nodes: 2: `<omitted>`; 403: `NonTerminating`; 887: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 29 | 14 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnLookAtEvent` | 12 | 14 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 35 | 26 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnPoseCorrectionEvent` | 3 | 134 / 229 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/5` |
| `scneventsAttachPropToPerformer` | 4 | 89 / 195 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 134 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/4` |
| `scneventsSocket` | 11 | 26 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, gaze: 1
- speech: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `f0405500318e46f09bfc437363a382a7965c57ff486072e68893720aca3766e9`. Binary SHA-256: `bd588c87c7a060be5432015fd22d302b910ab17d00d6a9d3d14cff9744c90498`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\fixers\wakako\scenes\wakako_okada_default.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_03b_dollhouse_tom.scene`

176 graph nodes, 219 edges; 36 event-bearing sections, 253 events; 110 screenplay lines, 22 screenplay options, 10 choice nodes.

Actors: tom (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `tom_in` → 57; `hostile` → 876.

Exits: `friendly_done` → 664; `hostile_done` → 877; `tom_lays` → 1545.

End nodes: 664: `NonTerminating`; 877: `NonTerminating`; 1545: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 652 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnChangeIdleAnimEvent` | 7 | 652 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnDialogLineEvent` | 88 | 646 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnLookAtAdvancedEvent` | 2 | 1060 / 494 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/3` |
| `scnLookAtEvent` | 55 | 646 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 62 | 646 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsSocket` | 38 | 646 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 13
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, gaze: 3
- socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, gaze, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1

Raw SHA-256: `c5387fd80bd7ec6b4695b4e7eab691b1b8fc7396a75f5291f722d79b06abe2e4`. Binary SHA-256: `b43d43501a1f84fd0e5d098c6cca5ca4d709e949f472f9509849bea8ecd5723c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_03b_dollhouse_tom.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_04_jigjig_street.scene`

195 graph nodes, 222 edges; 36 event-bearing sections, 146 events; 61 screenplay lines, 3 screenplay options, 3 choice nodes.

Actors: holo_01 (actor 0, findInWorld); holo_02 (actor 1, findInWorld); offer_f (actor 2, findInWorld); offer_m (actor 3, findInWorld); Judy (actor 4, spawnSet); gutter_01 (actor 5, findInWorld); gutter_02 (actor 6, findInWorld); sex_m (actor 7, findInWorld); sex_f (actor 8, findInWorld); scan_f_01 (actor 9, findInWorld); scan_f_02 (actor 10, findInWorld); scan_m_01 (actor 11, findInWorld); scan_m_02 (actor 12, findInWorld); Johnny (actor 13, spawnDespawn); peep_client_f_01 (actor 14, findInWorld); peep_client_m_01 (actor 15, findInWorld); peep_prostitute_m_01 (actor 16, findInWorld); stand_client_m_01 (actor 17, findInWorld); stand_client_m_02 (actor 18, findInWorld); shop_vendor_m (actor 19, findInWorld); shop_client_m_01 (actor 20, findInWorld); street_dealer_m_unicorn (actor 21, findInWorld); shop_client_m_02 (actor 22, community); peep_client_m_02 (actor 23, community); Player (actor 24, findInContext).

Entries: `in_wbr_jpn_medicstore_02` → 1; `in_holograms` → 1419; `in_sex_scene` → 1421; `in_offer_m` → 1425; `in_window` → 1458; `in_stand` → 1460; `in_shop_scene` → 1473; `in_johnny` → 600; `in_scan` → 1490; `in_gutter` → 1492; `johnny_jig_01` → 1496.

Exits: `out_sex_scene` → 1446; `out_offer_m` → 1448; `out_johnny` → 598; `out_shop_scene` → 1480; `out_stand` → 1482; `out_04_implants` → 618.

End nodes: 598: `NonTerminating`; 618: `NonTerminating`; 1446: `NonTerminating`; 1448: `NonTerminating`; 1480: `NonTerminating`; 1482: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 638 / 224 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/0` |
| `scnDialogLineEvent` | 51 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 26 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 34 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 2 | 1055 / 622 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/2` |
| `scneventsSocket` | 27 | 506 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 538 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/7` |
| `scneventsVFXEvent` | 1 | 716 / 271 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 8
- speech: 7
- socket_signal: 6
- speech, skeletal_animation, gaze: 3
- speech, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, vfx, socket_signal: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `b561c5db03b7be010edc14961f6431158b43c0a54ddb19ecbd0dec2559ae158f`. Binary SHA-256: `2baaf144851009698a9a47aa47a852b21a76ae5c4f2f1d92960b0685dbe00932`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_04_jigjig_street.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_04a_judy_holocall.scene`

58 graph nodes, 67 edges; 10 event-bearing sections, 29 events; 24 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: judy (actor 0, spawnSet); johnny (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `in_after_dollhouse` → 256; `in_after_jigjig` → 463.

Exits: `out_failed_call` → 585; `out_after_jigjig` → 482; `out_after_dollhouse` → 287.

End nodes: 287: `<omitted>`; 482: `<omitted>`; 585: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 24 | 262 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 2 | 265 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 317 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |
| `scneventsSocket` | 2 | 265 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, gaze, socket_signal: 2
- speech, skeletal_animation: 1

Raw SHA-256: `6d931e420ecb46568a508d7c74244e639794fe3e8be5e87e2dd94b7a88fd96a0`. Binary SHA-256: `4129461a9f63730d6e6be0dea280477c19302ad61ef3f7ffc4a41b46d809a6a6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_04a_judy_holocall.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_05_fingers_enter.scene`

422 graph nodes, 632 edges; 77 event-bearing sections, 849 events; 197 screenplay lines, 36 screenplay options, 13 choice nodes.

Actors: goon_01 (actor 0, community); goon_02 (actor 1, community); goon_03 (actor 2, community); prostitute_trip (actor 3, community); Mitzi (actor 4, community); queue_02 (actor 5, community); Judy (actor 6, spawnSet); goon_upstairs (actor 7, community); prostitute_upstairs (actor 8, community); queue_04 (actor 9, community); V (actor 10, findInContext).

Entries: `enter` → 1; `goons_otside_prev` → 3747; `judy` → 3750; `Start 16` → 3780; `prostitute_goon_fight_prev` → 3483; `prostitutes_preview` → 3532; `Start 17` → 3881.

Exits: `end_window_break` → 2006; `out_combat` → 1398; `clear` → 1102; `end_queue` → 3072; `End_wait` → 1879; `End_computer` → 1900; `End_doors_breaking` → 1909.

End nodes: 1102: `<omitted>`; 1398: `NonTerminating`; 1879: `NonTerminating`; 1900: `NonTerminating`; 1909: `NonTerminating`; 2006: `NonTerminating`; 3072: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 1963 / 980 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/4` |
| `scnChangeIdleAnimEvent` | 63 | 147 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 168 | 147 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 10 | 1963 / 981 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/5` |
| `scnIKEvent` | 20 | 1963 / 977 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 2049 / 1176 | `/Data/RootChunk/sceneGraph/Data/graph/93/Data/events/3` |
| `scnLookAtEvent` | 211 | 147 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 185 | 147 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnUnmountEvent` | 10 | 1963 / 985 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/8` |
| `scneventsEquipItemToPerformer` | 6 | 2196 / 1348 | `/Data/RootChunk/sceneGraph/Data/graph/108/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 10 | 1963 / 983 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/7` |
| `scneventsSocket` | 150 | 147 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 6 | 643 / 462 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 3485 / 2606 | `/Data/RootChunk/sceneGraph/Data/graph/293/Data/events/3` |
| `scneventsVFXDurationEvent` | 1 | 2457 / 1545 | `/Data/RootChunk/sceneGraph/Data/graph/146/Data/events/3` |
| `scneventsVFXEvent` | 3 | 1956 / 960 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 14
- speech, skeletal_animation, gaze, socket_signal: 10
- speech: 10
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, gaze: 3
- skeletal_animation, socket_signal: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation: 2
- skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `a8c3c0cb48efbd45fe40c9e23cb0b5e6da0b62900f163c10cdf4bd469ac8ea27`. Binary SHA-256: `d744a147b5bce8bb4d10fc6307f97ac96732e3ac833cde5afc8894814203bf61`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_05_fingers_enter.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_06a_fingers_escape.scene`

236 graph nodes, 290 edges; 39 event-bearing sections, 372 events; 100 screenplay lines, 17 screenplay options, 6 choice nodes.

Actors: Fingers (actor 0, spawnSet); Prostitute (actor 1, community); Judy (actor 2, spawnSet); Johnny (actor 3, spawnDespawn); queue_01 (actor 4, community); queue_02 (actor 5, community); V (actor 6, findInContext).

Entries: `Fingers_wait` → 1226; `Fingers_computer` → 1252; `Fingers_door` → 1255; `fingers_window` → 1279; `Start 18` → 1906; `Fingers_queue` → 1908.

Exits: `interrogation` → 309.

End nodes: 309: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 23 | 247 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/5` |
| `scnChangeIdleAnimEvent` | 42 | 247 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnDialogLineEvent` | 70 | 247 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/6` |
| `scnGameplayTransitionEvent` | 3 | 1365 / 704 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/8` |
| `scnIKEvent` | 6 | 1365 / 697 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/2` |
| `scnLookAtEvent` | 70 | 247 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnPlaySkAnimEvent` | 67 | 247 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnUnmountEvent` | 3 | 1365 / 703 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/7` |
| `scneventsAttachPropToPerformer` | 4 | 591 / 175 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 635 / 349 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/19` |
| `scneventsSetAnimFeatureEvent` | 3 | 1365 / 701 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/6` |
| `scneventsSocket` | 76 | 247 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/16` |
| `scneventsUnequipItemFromPerformer` | 2 | 635 / 338 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/8` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 2363 / 1432 | `/Data/RootChunk/sceneGraph/Data/graph/180/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 4
- speech: 4
- speech, socket_signal: 3
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `24204a421aae5345c83214950e67e2beefc211aa4b23f78188d9a5adfef75c27`. Binary SHA-256: `892ef1311e147605cf5b1992e93448a176c873ad3f92dc00aa7ede8e88407e96`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_06a_fingers_escape.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_06b_fingers_interrogation.scene`

317 graph nodes, 404 edges; 72 event-bearing sections, 669 events; 129 screenplay lines, 34 screenplay options, 13 choice nodes.

Actors: Fingers (actor 0, spawnSet); Judy (actor 1, spawnSet); Johnny (actor 2, spawnSet); Wakako (actor 3, findInContext); V (actor 4, findInContext).

Entries: `judy sliding` → 3440; `judy_to_office_walk` → 3443; `Start 11` → 2894; `Start 18` → 3819; `in` → 1570.

Exits: `out` → 1568.

End nodes: 1568: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 13 | 1424 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scnChangeIdleAnimEvent` | 42 | 1417 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 123 | 1417 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 7 | 1781 / 927 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/13` |
| `scnIKEvent` | 14 | 1781 / 910 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 1558 / 765 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/13` |
| `scnLookAtEvent` | 142 | 1417 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 160 | 1417 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnUnmountEvent` | 7 | 1781 / 931 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/16` |
| `scneventsAttachPropToPerformer` | 4 | 1497 / 586 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/9` |
| `scneventsAttachPropToWorld` | 4 | 1424 / 102 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/7` |
| `scneventsCameraParamsEvent` | 1 | 1464 / 447 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 7 | 1781 / 929 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/15` |
| `scneventsSocket` | 140 | 1417 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scneventsVFXEvent` | 3 | 1781 / 923 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 21
- speech, skeletal_animation, gaze, socket_signal: 8
- speech: 8
- speech, gaze: 6
- skeletal_animation, socket_signal: 4
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, audio, vfx: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `ee69d213dcbedfa6ded7d453c770c2e29eabaaa44d8fbf9c6ff37f4a1d90955b`. Binary SHA-256: `49e016e87b2dbe60b6ec4022aa6a69f36beac1df77d6d2f6a7f850aa574177c9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_06b_fingers_interrogation.scene" --events
```

