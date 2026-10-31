# Automatic Love: scene presentation

Journal identity: `quests/main_quest/act_01/q105_dollhouse`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q105_dollhouse.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q105\scenes\q105_00_holocall_judy.scene`

46 graph nodes, 54 edges; 8 event-bearing sections, 40 events; 19 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: Judy (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1; `Start 1` → 262.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 17 | 118 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnLookAtEvent` | 1 | 374 / 279 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/0` |
| `scnPlaySkAnimEvent` | 6 | 118 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsCameraEvent` | 1 | 263 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 263 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scneventsSocket` | 14 | 120 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation: 1
- camera: 1
- gaze: 1

Raw SHA-256: `5b00c10e026ec2a9a9829bb78fb2f286eaf369f021768df7a37f19f8c000bf0d`. Binary SHA-256: `8ad3132a9043ed7dcf8dbe079ae8256daf7aae982bdd48f2e97fa7517523b1ba`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_00_holocall_judy.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_01_lizzies.scene`

95 graph nodes, 132 edges; 21 event-bearing sections, 212 events; 55 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Lizzy_f_cellar (actor 0, findInWorld); Lizzy_m_cellar (actor 1, findInWorld); Lizzy_f_dance_01 (actor 2, findInWorld); Lizzy_f_dance_02 (actor 3, findInWorld); Prostitute (actor 4, findInWorld); Judy (actor 5, spawnSet); Johnny (actor 6, spawnSet); client (actor 7, community); Player (actor 8, findInContext).

Entries: `in` → 300.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 44 | 98 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 4 | 724 / 425 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/3` |
| `scnIKEvent` | 8 | 724 / 423 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/1` |
| `scnLookAtEvent` | 54 | 98 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 65 | 98 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 4 | 724 / 429 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 4 | 724 / 427 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/5` |
| `scneventsSocket` | 28 | 607 / 328 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 629 / 371 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 7
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, socket_signal: 4
- socket_signal: 3
- speech: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1

Raw SHA-256: `d600f71e13c6fb625d0ab0d570a94de19396dbc1cd12972e06e2aef0d49297ef`. Binary SHA-256: `a3dc66cf1f527dbb4c3ba26b7295e0544b120135081f1601491ef8f0d2e7ebb3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_01_lizzies.scene" --events
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

## `base\quest\main_quests\part1\q105\scenes\q105_01b_barman.scene`

38 graph nodes, 47 edges; 9 event-bearing sections, 67 events; 27 screenplay lines, 5 screenplay options, 1 choice nodes.

Actors: Lizzies_Barman (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `in` → 300.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 360 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scnDialogLineEvent` | 26 | 56 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnLookAtEvent` | 9 | 56 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 20 | 56 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsSocket` | 11 | 56 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 2
- speech, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech: 1
- socket_signal: 1

Raw SHA-256: `15985682db5699b53382f3eb218546e930b3ace90cd1b0d3c665ca227f006c26`. Binary SHA-256: `d1748760a403343cbf4cdefefa2de8c6471e22811297308d1d622ba04b903b2b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_01b_barman.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_01c_lizzies_boss.scene`

56 graph nodes, 96 edges; 12 event-bearing sections, 78 events; 34 screenplay lines, 7 screenplay options, 4 choice nodes.

Actors: lizzies_boss (actor 0, community); Player (actor 1, findInContext).

Entries: `in` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 8 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnChangeIdleAnimEvent` | 6 | 8 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnDialogLineEvent` | 34 | 8 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnLookAtEvent` | 12 | 8 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 18 | 8 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 8 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scneventsSocket` | 4 | 8 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation: 1

Raw SHA-256: `b1d862c94f87bdbe50730b40a3e16829f9e928aa659b66964f3925bf75c5f016`. Binary SHA-256: `67795373bee02d9a007f077fefb320693c11ac2fc8dba013c869f19f531f5d69`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_01c_lizzies_boss.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_02_lizzy_meet_judy.scene`

320 graph nodes, 432 edges; 73 event-bearing sections, 553 events; 156 screenplay lines, 33 screenplay options, 13 choice nodes.

Actors: judy (actor 0, spawnSet); Lizzy_boss (actor 1, community); johnny (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `meetup` → 858; `Start 8` → 3556; `Start 9` → 3559; `Start 5` → 3104.

Exits: `meetup_done` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 1031 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scnChangeIdleAnimEvent` | 26 | 1062 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scnDialogLineEvent` | 137 | 863 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 6 | 1095 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/14` |
| `scnIKEvent` | 12 | 1095 / 246 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/3` |
| `scnLookAtEvent` | 130 | 863 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 101 | 863 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 6 | 1095 / 264 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/13` |
| `scneventsAttachPropToNode` | 1 | 1075 / 229 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/7` |
| `scneventsAttachPropToPerformer` | 3 | 2144 / 951 | `/Data/RootChunk/sceneGraph/Data/graph/105/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 2438 / 1089 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/5` |
| `scneventsEquipItemToPerformer` | 8 | 1040 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 6 | 1095 / 260 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/10` |
| `scneventsSocket` | 109 | 863 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 3 | 1040 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 16
- speech, skeletal_animation, gaze, socket_signal: 11
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, gaze: 6
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 2
- socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `05e7bcd885a869c14ef2e3b72938c02289cceaf8f128b7c2c67d62a7f5586843`. Binary SHA-256: `f254a6a3ea81c0303e558f7ce824cf8122db4c820253af54f70b12a31af3d717`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_02_lizzy_meet_judy.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_02c_to_dollhouse.scene`

89 graph nodes, 117 edges; 10 event-bearing sections, 82 events; 26 screenplay lines, 6 screenplay options, 2 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); vendor (actor 1, community); tc_01 (actor 2, community); tc_02 (actor 3, community); Player (actor 4, findInContext).

Entries: `to_dollhouse` → 1; `wait` → 822; `to_dollhouse_fluff` → 1119.

Exits: `to_dollhouse_done` → 2; `wait_clear` → 3965; `End 2` → 614; `to_dollhouse_fluff_done` → 1122.

End nodes: 2: `NonTerminating`; 614: `<omitted>`; 1122: `<omitted>`; 3965: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 526 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnDialogLineEvent` | 21 | 143 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 655 / 215 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/27` |
| `scnIKEvent` | 4 | 655 / 204 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/21` |
| `scnLookAtEvent` | 10 | 143 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnPlaySkAnimEvent` | 16 | 143 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnUnmountEvent` | 2 | 655 / 214 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/26` |
| `scneventsCameraParamsEvent` | 2 | 1146 / 551 | `/Data/RootChunk/sceneGraph/Data/graph/78/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 2 | 655 / 212 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/25` |
| `scneventsSocket` | 19 | 143 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scneventsVFXEvent` | 2 | 1146 / 546 | `/Data/RootChunk/sceneGraph/Data/graph/78/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, camera, vfx: 1
- vfx: 1
- camera: 1

Raw SHA-256: `9d8a8689341fdd3e9812d33c52c476ac4afac71a0f2bf50a340bae054d02e346`. Binary SHA-256: `55ac67b75d2555c346d6c63dd19d3339e69ec0dfe6698fa1e98e417d791ad9f8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_02c_to_dollhouse.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_03_dollhouse_mood.scene`

195 graph nodes, 264 edges; 33 event-bearing sections, 300 events; 165 screenplay lines, 8 screenplay options, 2 choice nodes.

Actors: business_customer (actor 0, findInWorld); business_doll (actor 1, findInWorld); employees_fem (actor 2, findInWorld); employees_male (actor 3, findInWorld); Johnny (actor 4, spawnDespawn); guard_vipentrance_02_bathroom (actor 5, community); vip_guard (actor 6, findInWorld); guests_hint_01 (actor 7, findInWorld); guests_hint_02 (actor 8, findInWorld); guest_leaving (actor 9, findInWorld); bar_barkeeper (actor 10, community); bar_customer (actor 11, community); vip_customer_m (actor 12, community); vip_customer_f (actor 13, community); guard_patrole (actor 14, community); guard_door (actor 15, community); dollhouse_hologram_01 (actor 16, community); V (actor 17, findInContext).

Entries: `employees` → 3; `vip_guard` → 998; `guests_hint` → 1004; `hologram_entrance` → 1826; `customer` → 902; `vip_area` → 1390; `Start 14` → 1679.

Exits: `vip_guard_done` → 999; `End 11` → 1824; `employees_alert_guards` → 188; `customer_done` → 945.

End nodes: 188: `NonTerminating`; 945: `NonTerminating`; 999: `NonTerminating`; 1824: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 90 | 961 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnGameplayTransitionEvent` | 5 | 1528 / 537 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/18` |
| `scnIKEvent` | 10 | 1528 / 516 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/8` |
| `scnLookAtEvent` | 86 | 961 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnPlaySkAnimEvent` | 70 | 961 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnUnmountEvent` | 5 | 1528 / 538 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/19` |
| `scneventsSetAnimFeatureEvent` | 5 | 1528 / 535 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/17` |
| `scneventsSocket` | 29 | 977 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 10
- speech: 5
- speech, skeletal_animation, gaze, socket_signal: 4
- gaze: 4
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze: 2
- skeletal_animation, socket_signal: 2
- gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `db8e8cf45158248826e515fae4428fa606152bc862776e125f196eb83887503c`. Binary SHA-256: `4e130d82e6b40279d7bf4a17825d94b8c8e08bd4659522f192341483523600c4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_03_dollhouse_mood.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_03a_dollhouse_doll_01.scene`

428 graph nodes, 569 edges; 75 event-bearing sections, 564 events; 179 screenplay lines, 81 screenplay options, 41 choice nodes.

Actors: Doll (actor 0, community); V (actor 1, findInContext).

Entries: `Start 0` → 1; `Start 3` → 1990; `Start 5` → 2830; `Start 7` → 3301; `Start 8` → 3714; `Start 9` → 3760; `hostile` → 1507.

Exits: `clear` → 2; `hostile_done` → 1533; `clear2` → 2824; `doll_done` → 614.

End nodes: 2: `<omitted>`; 614: `NonTerminating`; 1533: `NonTerminating`; 2824: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1432 / 412 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/5` |
| `scnChangeIdleAnimEvent` | 11 | 1452 / 458 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/0` |
| `scnDialogLineEvent` | 157 | 619 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 2086 / 1286 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/7` |
| `scnIKEvent` | 2 | 2086 / 1279 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/1` |
| `scnLookAtAdvancedEvent` | 18 | 1448 / 446 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/3` |
| `scnLookAtEvent` | 123 | 621 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnPlaySkAnimEvent` | 137 | 619 / 92 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/3` |
| `scnUnmountEvent` | 1 | 2086 / 1285 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/6` |
| `scneventsCameraParamsEvent` | 7 | 1472 / 506 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/0` |
| `scneventsEquipItemToPerformer` | 4 | 1274 / 233 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/5` |
| `scneventsPlayRidCameraAnimEvent` | 1 | 1989 / 1253 | `/Data/RootChunk/sceneGraph/Data/graph/120/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 1 | 2086 / 1283 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/5` |
| `scneventsSocket` | 96 | 619 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scneventsUIAnimationBraindanceEvent` | 1 | 2133 / 1328 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/8` |
| `scneventsUnequipItemFromPerformer` | 2 | 1274 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/7` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1276 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 18
- speech, skeletal_animation, gaze, socket_signal: 12
- skeletal_animation, socket_signal: 7
- speech, skeletal_animation: 5
- speech: 4
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, gaze: 3
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, camera, socket_signal: 2
- gaze: 2
- gaze, socket_signal: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, gaze, camera, socket_signal: 1
- skeletal_animation, camera, rid_camera: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, bd_visibility_ui: 1

Raw SHA-256: `e363d2707ad87abc1a669cb611c88765711f4d2984030ff7346bfaf6fc10f84a`. Binary SHA-256: `1a254a6abc33dfd2584469d015e1fd012fff53e29f2eec7d3e22f6df621316be`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_03a_dollhouse_doll_01.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_03a_dollhouse_doll_02.scene`

437 graph nodes, 606 edges; 75 event-bearing sections, 578 events; 194 screenplay lines, 73 screenplay options, 34 choice nodes.

Actors: Doll (actor 0, community); V (actor 1, findInContext).

Entries: `Start 7` → 3862; `Start 8` → 3897; `Start 5` → 3287; `Start 6` → 3313; `hostile` → 684; `Start1` → 763.

Exits: `End1` → 764; `doll_done` → 777; `clear2` → 1261; `hostile_done` → 741.

End nodes: 741: `NonTerminating`; 764: `<omitted>`; 777: `NonTerminating`; 1261: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 809 / 603 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/10` |
| `scnChangeIdleAnimEvent` | 14 | 794 / 323 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/1` |
| `scnDialogLineEvent` | 168 | 712 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 1596 / 1947 | `/Data/RootChunk/sceneGraph/Data/graph/232/Data/events/7` |
| `scnIKEvent` | 2 | 1596 / 1940 | `/Data/RootChunk/sceneGraph/Data/graph/232/Data/events/1` |
| `scnLookAtAdvancedEvent` | 22 | 812 / 663 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/5` |
| `scnLookAtEvent` | 123 | 712 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnPlaySkAnimEvent` | 140 | 718 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/3` |
| `scnUnmountEvent` | 1 | 1596 / 1946 | `/Data/RootChunk/sceneGraph/Data/graph/232/Data/events/6` |
| `scneventsCameraParamsEvent` | 7 | 819 / 755 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/1` |
| `scneventsCameraPlacementEvent` | 1 | 1568 / 1867 | `/Data/RootChunk/sceneGraph/Data/graph/221/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 1 | 1596 / 1944 | `/Data/RootChunk/sceneGraph/Data/graph/232/Data/events/5` |
| `scneventsSocket` | 95 | 712 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scneventsVFXEvent` | 2 | 794 / 326 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 19
- speech, skeletal_animation, gaze: 11
- speech: 10
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, gaze, socket_signal: 3
- gaze: 3
- speech, gaze: 2
- speech, skeletal_animation, gaze, camera, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 2
- gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, gaze, camera, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `c2ac3503ec607aff5d43b2e1e95c30b4f3da887672a156a6dfb2a4d2e7da4647`. Binary SHA-256: `41d1a5362c052b311a0dd4367be0ef4ed9ad2c57ee9d5f67e13da0ffe9a1862f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_03a_dollhouse_doll_02.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_03a_dollhouse_manager.scene`

470 graph nodes, 581 edges; 73 event-bearing sections, 463 events; 159 screenplay lines, 36 screenplay options, 17 choice nodes.

Actors: manager (actor 0, community); Johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `friendly` → 1; `retrofix_manager_xor` → 2294; `unwelcome` → 1980; `weapons` → 787.

Exits: `friendly_done` → 2; `weapons_done` → 792.

End nodes: 2: `NonTerminating`; 792: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1575 / 1169 | `/Data/RootChunk/sceneGraph/Data/graph/157/Data/events/3` |
| `scnChangeIdleAnimEvent` | 20 | 124 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 131 | 124 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 983 / 762 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/5` |
| `scnIKEvent` | 6 | 983 / 756 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/1` |
| `scnLookAtAdvancedEvent` | 6 | 124 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnLookAtEvent` | 89 | 124 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 112 | 124 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnUnmountEvent` | 3 | 983 / 768 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/10` |
| `scneventsCameraParamsEvent` | 2 | 179 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 3 | 983 / 764 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/7` |
| `scneventsSocket` | 83 | 124 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXDurationEvent` | 1 | 540 / 426 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/1` |
| `scneventsVFXEvent` | 3 | 1515 / 1128 | `/Data/RootChunk/sceneGraph/Data/graph/154/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- speech, skeletal_animation, gaze: 10
- speech, skeletal_animation, gaze, socket_signal: 9
- speech: 9
- speech, skeletal_animation: 4
- speech, gaze: 4
- speech, socket_signal: 3
- socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- camera: 1
- skeletal_animation: 1

Raw SHA-256: `e7f48709a2509653a09e450303c435d69750475fb2a2e8ec5d17db93753f84c0`. Binary SHA-256: `1fed5242622bf5b1034adb19040afc0f20da025f816367a51758cfd54059a4ef`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_03a_dollhouse_manager.scene" --events
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

## `base\quest\main_quests\part1\q105\scenes\q105_03c_dollhouse_woodman.scene`

596 graph nodes, 779 edges; 87 event-bearing sections, 794 events; 341 screenplay lines, 81 screenplay options, 21 choice nodes.

Actors: Woodman (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `interrogation` → 1; `after_netrunner_defeat` → 3563; `after_kill` → 813; `win_preview` → 4191; `hostile` → 1573; `Start 13` → 5042.

Exits: `failed` → 749; `fight` → 2476; `hostile_spawn_01` → 4163; `hostile_spawn_02` → 4165; `killed` → 820; `after_kill_done` → 822; `success` → 828; `clear` → 4345.

End nodes: 749: `Terminating`; 820: `Terminating`; 822: `NonTerminating`; 828: `NonTerminating`; 2476: `Terminating`; 4163: `NonTerminating`; 4165: `NonTerminating`; 4345: `Terminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 709 / 344 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/6` |
| `scnChangeIdleAnimEvent` | 51 | 371 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 198 | 353 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 7 | 709 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/12` |
| `scnIKEvent` | 14 | 709 / 339 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 475 / 156 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/14` |
| `scnLookAtEvent` | 147 | 353 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnPlaySkAnimEvent` | 171 | 353 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnUnmountEvent` | 7 | 709 / 350 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/11` |
| `scneventsAttachPropToPerformer` | 10 | 371 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsAttachPropToWorld` | 9 | 632 / 279 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 7 | 709 / 346 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/8` |
| `scneventsSocket` | 164 | 353 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsVFXDurationEvent` | 1 | 632 / 283 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/19` |
| `scneventsVFXEvent` | 5 | 353 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 18
- speech, skeletal_animation, gaze, socket_signal: 16
- speech, skeletal_animation, gaze: 8
- speech, skeletal_animation, idle_animation, socket_signal: 6
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech: 2
- socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- gaze, props_equipment: 1
- skeletal_animation, gaze: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `a27a0cd58cfb0c2ac47e834ab0ae1921758059db26bb22bcd713899a527be7c2`. Binary SHA-256: `ba2561740b555d7de980118024186a7aef180caf82d55b9d93174ad04192ee37`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_03c_dollhouse_woodman.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_03d_dollhouse_evelyn_attack.scene`

11 graph nodes, 11 edges; 1 event-bearing sections, 15 events; 1 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Evelyn (actor 0, spawnDespawn); Client (actor 1, spawnDespawn).

Entries: `in` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnChangeIdleAnimEvent` | 2 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnPlaySkAnimEvent` | 4 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 5 | 4 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsVFXEvent` | 3 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1

Raw SHA-256: `71b244f9e8287317b818e935a0b481e0dd3188d8c6db6c7242129a71521b25ed`. Binary SHA-256: `d55509c3311e84a2ad5ed87cfa22744a22d95b35c7d08a5dd7675bba5f94a055`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_03d_dollhouse_evelyn_attack.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_03d_dollhouse_investigation.scene`

134 graph nodes, 146 edges; 18 event-bearing sections, 93 events; 37 screenplay lines, 9 screenplay options, 8 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `old` → 847; `fluff` → 859; `after_woodman` → 1015; `chamber` → 699.

Exits: `chamber_done` → 773.

End nodes: 773: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 36 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnLookAtEvent` | 24 | 26 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnPlaySkAnimEvent` | 15 | 26 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scneventsEquipItemToPerformer` | 1 | 1068 / 523 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/1` |
| `scneventsSocket` | 15 | 26 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scneventsVFXEvent` | 2 | 272 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 6
- speech, gaze: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, socket_signal: 1
- speech: 1
- gaze: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `2e67b0648d314be08d4d4c18310308b67e2f7f1dad7d964f37526385e20a2fbb`. Binary SHA-256: `081679afc7560f3fbb275f014562aa64dde7654595a7b584fe1c634c5f52b951`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_03d_dollhouse_investigation.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_03e_dollhouse_leave.scene`

99 graph nodes, 137 edges; 18 event-bearing sections, 88 events; 50 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Tom (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `elevator_johnny` → 1; `tom_phone` → 121; `Start 0` → 834.

Exits: `tom_phone_done` → 2; `elevator_johnny_done` → 122.

End nodes: 2: `<omitted>`; 122: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 33 | 156 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnLookAtAdvancedEvent` | 1 | 490 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/8` |
| `scnLookAtEvent` | 11 | 246 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnOverridePhantomParamsEvent` | 2 | 477 / 214 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/1` |
| `scnPlaySkAnimEvent` | 11 | 242 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scneventsAttachPropToPerformer` | 1 | 373 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/0` |
| `scneventsAttachPropToWorld` | 2 | 242 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/3` |
| `scneventsEquipItemToPerformer` | 3 | 717 / 453 | `/Data/RootChunk/sceneGraph/Data/graph/78/Data/events/0` |
| `scneventsSocket` | 19 | 156 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 717 / 461 | `/Data/RootChunk/sceneGraph/Data/graph/78/Data/events/3` |
| `scneventsVFXEvent` | 4 | 477 / 213 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, props_equipment, socket_signal: 2
- speech, gaze, vfx, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, vfx, socket_signal: 2
- speech, socket_signal: 1
- speech, gaze: 1
- props_equipment: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1

Raw SHA-256: `c1165fad14c4c2cf32246955e9946038b86a047e33244157f6e0d312c10b95e2`. Binary SHA-256: `61b81b0cf31bc97573756ea350a367eb56dde81b196046740d9940e173635da4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_03e_dollhouse_leave.scene" --events
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

## `base\quest\main_quests\part1\q105\scenes\q105_06c_finding_studio.scene`

237 graph nodes, 273 edges; 39 event-bearing sections, 326 events; 84 screenplay lines, 16 screenplay options, 8 choice nodes.

Actors: Judy (actor 0, spawnSet); Actor (actor 1, findInWorld); judys_van (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `in_decide` → 4; `in_after` → 236; `in_before_braindance` → 238; `in_judy_van` → 2402; `not_evelyn_comment` → 679; `scavs_comment` → 684; `Start 13` → 4056; `walk down` → 2507.

Exits: `alone_clear` → 3884; `out_judy_spline` → 987; `out_decided` → 228; `out_before_braindance` → 241; `with_judy` → 66; `leave_alone` → 67; `End 3` → 682; `End 4` → 688.

End nodes: 66: `NonTerminating`; 67: `NonTerminating`; 228: `NonTerminating`; 241: `<omitted>`; 682: `<omitted>`; 688: `<omitted>`; 987: `<omitted>`; 3884: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 14 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnChangeIdleAnimEvent` | 26 | 11 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 77 | 11 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnGameplayTransitionEvent` | 4 | 14 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scnIKEvent` | 10 | 13 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scnLookAtEvent` | 48 | 11 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 63 | 11 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnUnmountEvent` | 4 | 14 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scneventsAttachPropToPerformer` | 8 | 27 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/17` |
| `scneventsAttachPropToWorld` | 1 | 134 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 12 | 13 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsSocket` | 63 | 13 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scneventsVFXEvent` | 6 | 30 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech: 5
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, socket_signal: 1
- gaze, socket_signal, animation_state: 1
- gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `7040374385ea5e003f12685f0aac258907d08229f7f05fcd6e6f425c4d5fc401`. Binary SHA-256: `42065be5a139c6d94c40ac8114d1cfa5266336228154e34a4f3935a6c4c90bfd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_06c_finding_studio.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_06d_fixer_holocall.scene`

95 graph nodes, 119 edges; 16 event-bearing sections, 98 events; 52 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: Wakako (actor 0, spawnSet); wakako_holocall (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `in` → 1; `in_intro` → 538.

Exits: `out` → 2; `out_outside` → 463.

End nodes: 2: `NonTerminating`; 463: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 370 / 345 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/7` |
| `scnDialogLineEvent` | 50 | 32 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnLookAtEvent` | 4 | 361 / 254 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/2` |
| `scnPlaySkAnimEvent` | 29 | 32 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 361 / 257 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/5` |
| `scneventsEquipItemToPerformer` | 1 | 419 / 361 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/2` |
| `scneventsSocket` | 6 | 360 / 242 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/7` |
| `scneventsSpawnEntityEvent` | 2 | 361 / 258 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/6` |
| `scneventsUnequipItemFromPerformer` | 2 | 361 / 256 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 8
- speech: 2
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, entity_lifecycle: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal, entity_lifecycle: 1

Raw SHA-256: `4bff8d2d0886c2da06e1bb216516632c61d2138ddf188685e995f4d4d8249662`. Binary SHA-256: `9ce75807319776953317c7718d850daa5d43701eacbb158b7156cfc560abf3d1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_06d_fixer_holocall.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_07_blackmarket_braindance.scene`

313 graph nodes, 409 edges; 22 event-bearing sections, 105 events; 34 screenplay lines, 15 screenplay options, 14 choice nodes.

Actors: Judy (actor 0, spawnDespawn); Johnny (actor 1, findInContext); Actor_Netrunner (actor 2, spawnDespawn); Actor_Scavenger_01 (actor 3, spawnDespawn); Actor_Scavenger_Editor (actor 4, spawnDespawn); br_replacer (actor 5, spawnSet); Player (actor 6, findInContext).

Entries: `in` → 4.

Exits: `out` → 235.

End nodes: 235: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioDurationEvent` | 24 | 1104 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/16` |
| `scnChangeIdleAnimEvent` | 2 | 2310 / 1163 | `/Data/RootChunk/sceneGraph/Data/graph/208/Data/events/0` |
| `scnDialogLineEvent` | 32 | 85 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 15 | 1104 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/3` |
| `scneventsAttachPropToPerformer` | 1 | 1104 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/0` |
| `scneventsAttachPropToWorld` | 1 | 1753 / 746 | `/Data/RootChunk/sceneGraph/Data/graph/140/Data/events/0` |
| `scneventsBraindanceVisibilityEvent` | 2 | 1104 / 215 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/12` |
| `scneventsCameraParamsEvent` | 1 | 1104 / 189 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/1` |
| `scneventsClueEvent` | 15 | 1104 / 211 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/8` |
| `scneventsPlayRidCameraAnimEvent` | 3 | 1104 / 212 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/9` |
| `scneventsSocket` | 5 | 1104 / 217 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/14` |
| `scneventsVFXBraindanceEvent` | 2 | 1104 / 276 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/58` |
| `scneventsVFXEvent` | 2 | 85 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 18
- speech, vfx: 1
- skeletal_animation, camera, rid_camera, props_equipment, audio, vfx, socket_signal, clues, bd_visibility_ui: 1
- props_equipment: 1
- idle_animation: 1

Raw SHA-256: `7623dc28254bce2f4567563efe03d79c0e03711968131866fa124664e208b839`. Binary SHA-256: `639572b476c962abd1c724aacfb23881d6db4fe176c9750de2ec20675b14347c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_07_blackmarket_braindance.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_07_judy_braindance.scene`

566 graph nodes, 740 edges; 54 event-bearing sections, 215 events; 92 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: Judy (actor 0, spawnSet); Johnny (actor 1, spawnSet); judy_holo (actor 2, spawnSet); judy_vehicle (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `studio_start_judy` → 1; `to_studio` → 7; `studio_start_alone` → 18; `level_01_alt` → 3464; `Start 33` → 5174; `level_01` → 187; `Start 31` → 4177; `level_02` → 1989; `placeholder` → 3790; `old` → 3792; `Start 32` → 5004.

Exits: `studio_start_done` → 2; `to_studio_out` → 8; `level_02_done_combat` → 5135; `level_01_done` → 1799; `level_02_done` → 2008; `clear_bd_00` → 895.

End nodes: 2: `NonTerminating`; 8: `NonTerminating`; 895: `<omitted>`; 1799: `<omitted>`; 2008: `<omitted>`; 5135: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 2144 / 1023 | `/Data/RootChunk/sceneGraph/Data/graph/159/Data/events/6` |
| `scnChangeIdleAnimEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 86 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 178 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/11` |
| `scnIKEvent` | 12 | 48 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnLookAtEvent` | 30 | 41 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |
| `scnPlaySkAnimEvent` | 32 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 5 | 178 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scneventsEquipItemToPerformer` | 1 | 3693 / 2154 | `/Data/RootChunk/sceneGraph/Data/graph/351/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 7 | 48 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scneventsSocket` | 29 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 5011 / 3213 | `/Data/RootChunk/sceneGraph/Data/graph/532/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 25
- speech, gaze: 5
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `3564f259d523f111b31eb74892b62aba93dda73d01fe7645eefd428c9e362bfa`. Binary SHA-256: `a6e6a6456faa8fd5c61fefd26ac353d15d3220b095d9b7fb889cad5762940f20`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_07_judy_braindance.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_08a_braindance_investigation.scene`

106 graph nodes, 118 edges; 17 event-bearing sections, 76 events; 25 screenplay lines, 10 screenplay options, 10 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Judy (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `lvl_02` → 410; `Start 10` → 931; `lvl_01` → 434.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 20 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnDialogLineEvent` | 22 | 20 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnLookAtEvent` | 20 | 20 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/5` |
| `scnOverridePhantomParamsEvent` | 2 | 265 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnPlaySkAnimEvent` | 11 | 20 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |
| `scnPoseCorrectionEvent` | 1 | 265 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scneventsEquipItemToPerformer` | 2 | 820 / 355 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/1` |
| `scneventsSocket` | 14 | 20 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 1 | 820 / 358 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 4
- speech, gaze: 4
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- speech: 1

Raw SHA-256: `a4364574b62a4a7f809a83b79fc90a5d53bcc4242f9491dcc66af5df0b5f0073`. Binary SHA-256: `d00b2faf02e0baf41407cc747e2230b55a3ed7e3df787d274a6f3b97636c3f16`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_08a_braindance_investigation.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_08d_braindance_gameplay.scene`

134 graph nodes, 157 edges; 30 event-bearing sections, 197 events; 97 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnSet); 00_exterior_01 (actor 1, community); 00_exterior_02 (actor 2, community); 00_interior_01 (actor 3, community); 00_interior_02 (actor 4, community); 01_big_room_01 (actor 5, community); 01_big_room_02 (actor 6, community); 01_transition_01 (actor 7, community); 01_transition_02 (actor 8, community); 02_main_01 (actor 9, community); 02_main_02 (actor 10, community); 01_drugs_01 (actor 11, community); 01_drugs_02 (actor 12, community); 01_cagefights_01 (actor 13, community); 01_cagefights_02 (actor 14, community); V (actor 15, findInContext).

Entries: `chat_00_exterior` → 236; `chat_00_interior` → 237; `chat_01_big_room` → 238; `chat_02_main_room` → 239; `chat_01_transition_ventilation` → 490; `chat_01_transition_toilet` → 491; `chat_01_drugs` → 416; `chat_01_transition` → 317; `chat_01_cagefights` → 451.

Exits: `chat_01_big_room_done` → 936; `End1` → 953; `chat_00_exterior_done` → 867; `chat_01_drugs_done` → 884; `chat_01_transition_clear` → 660; `chat_01_cagefights_done` → 899; `chat_00_interior_done` → 914.

End nodes: 660: `<omitted>`; 867: `<omitted>`; 884: `<omitted>`; 899: `<omitted>`; 914: `<omitted>`; 936: `<omitted>`; 953: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 91 | 241 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnGameplayTransitionEvent` | 8 | 250 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |
| `scnIKEvent` | 16 | 250 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scnPlaySkAnimEvent` | 39 | 241 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 8 | 250 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 8 | 250 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |
| `scneventsSocket` | 27 | 249 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- speech, skeletal_animation: 3
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, socket_signal: 1

Raw SHA-256: `222371fe268919a3bccee6e8b54c801df209a14840d010020e6803278a7c9ec1`. Binary SHA-256: `023800b8ae3e6a24a797ca2797ef4f0af500372221a1123328a0ff2a2fb719df`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_08d_braindance_gameplay.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_09_braindance_evelyn.scene`

181 graph nodes, 205 edges; 32 event-bearing sections, 158 events; 45 screenplay lines, 8 screenplay options, 6 choice nodes.

Actors: Judy (actor 0, spawnSet); Evelyn (actor 1, spawnSet); Johnny (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `start` → 1; `Start 6` → 3798; `start_combat` → 3997; `get_up` → 2423.

Exits: `prefetch` → 2016; `end` → 611.

End nodes: 611: `NonTerminating`; 2016: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 1121 / 186 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/6` |
| `scnChangeIdleAnimEvent` | 8 | 150 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 32 | 150 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 826 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/22` |
| `scnIKEvent` | 4 | 826 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/13` |
| `scnLookAtEvent` | 25 | 150 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 25 | 150 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 2 | 826 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/21` |
| `scneventsAttachPropToPerformer` | 1 | 1720 / 327 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 3749 / 844 | `/Data/RootChunk/sceneGraph/Data/graph/118/Data/events/0` |
| `scneventsCameraParamsEvent` | 3 | 1121 / 187 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/7` |
| `scneventsMountEvent` | 1 | 1859 / 491 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/16` |
| `scneventsSetAnimFeatureEvent` | 6 | 826 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/18` |
| `scneventsSetAnimsetWeight` | 8 | 1859 / 476 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/2` |
| `scneventsSocket` | 31 | 150 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsVFXEvent` | 4 | 1334 / 217 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, gaze: 4
- speech, skeletal_animation, gaze: 3
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, vfx, socket_signal: 1
- props_equipment: 1
- animation_state: 1
- vfx: 1

Raw SHA-256: `ea2550a49cffc1e54e43caec4f2a8d059417d3221e1edf4a2ca66ffae35efa88`. Binary SHA-256: `d740f52c909664393dd4a06486f4ca075be25b4ccdfdb5b40bdbce072b4f03ce`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_09_braindance_evelyn.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_11_judys_evelyn.scene`

306 graph nodes, 359 edges; 66 event-bearing sections, 461 events; 152 screenplay lines, 34 screenplay options, 17 choice nodes.

Actors: judy (actor 0, spawnSet); evelyn (actor 1, spawnSet); johnny (actor 2, spawnDespawn); GirlUmbrella (actor 3, spawnDespawn); Player (actor 4, findInContext).

Entries: `Start 10` → 3822; `Start 8` → 2811; `Start 6` → 2580; `Start 2` → 703; `Start 7` → 2739; `in_watch_bd_vq` → 1991; `in_watch_bd_02` → 1993.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 1490 / 685 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/9` |
| `scnChangeIdleAnimEvent` | 15 | 572 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 137 | 491 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 7 | 576 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/9` |
| `scnIKEvent` | 14 | 576 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/7` |
| `scnLookAtEvent` | 53 | 491 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 2 | 1629 / 982 | `/Data/RootChunk/sceneGraph/Data/graph/98/Data/events/8` |
| `scnPlaySkAnimEvent` | 98 | 451 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 7 | 576 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/12` |
| `scneventsAttachPropToPerformer` | 7 | 1470 / 564 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/2` |
| `scneventsAttachPropToWorld` | 6 | 576 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scneventsCameraParamsEvent` | 2 | 2123 / 1217 | `/Data/RootChunk/sceneGraph/Data/graph/124/Data/events/3` |
| `scneventsEquipItemToPerformer` | 4 | 2090 / 1151 | `/Data/RootChunk/sceneGraph/Data/graph/119/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 9 | 576 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/11` |
| `scneventsSocket` | 80 | 451 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 4 | 576 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scneventsVFXEvent` | 13 | 1470 / 570 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation: 8
- speech, skeletal_animation, gaze, socket_signal: 6
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, gaze: 2
- gaze: 2
- speech, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze: 1
- speech, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, camera, props_equipment, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- animation_state: 1
- vfx: 1

Raw SHA-256: `49a5c9b6cf709ca45f4c748514b98bb83e22fb2a0e2dd4746e2085743e84fc7a`. Binary SHA-256: `254eb3ae86c70d84bf729cd785cf6ec36473924b0fdb5c3ada89bd976a70eb2e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_11_judys_evelyn.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_12a_braindance_voodooqueen.scene`

118 graph nodes, 139 edges; 9 event-bearing sections, 49 events; 34 screenplay lines, 3 screenplay options, 3 choice nodes.

Actors: evelyn (actor 0, spawnSet); voodooqueen (actor 1, community); judy (actor 2, spawnDespawn); bd_replacer (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 33 | 309 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 563 / 286 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/1` |
| `scneventsAttachPropToPerformer` | 1 | 563 / 285 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/0` |
| `scneventsAttachPropToWorld` | 1 | 378 / 160 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/1` |
| `scneventsBraindanceVisibilityEvent` | 2 | 563 / 297 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/6` |
| `scneventsCameraParamsEvent` | 1 | 563 / 294 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/3` |
| `scneventsClueEvent` | 3 | 563 / 300 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/9` |
| `scneventsPlayRidCameraAnimEvent` | 2 | 563 / 299 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/8` |
| `scneventsVFXEvent` | 2 | 563 / 295 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, props_equipment: 1
- speech, skeletal_animation, camera, rid_camera, props_equipment, vfx, clues, bd_visibility_ui: 1
- vfx: 1

Raw SHA-256: `4ea3f7c0c28a58490790d199fca4dab2371dc5b726faeb681c86ab04e9e03aef`. Binary SHA-256: `bc46e4c570e90f96275c75ae3a8a89556c569533055cf1a6c3b2e8934459c309`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_12a_braindance_voodooqueen.scene" --events
```

## `base\quest\main_quests\part1\q105\scenes\q105_12b_braindance_alt.scene`

123 graph nodes, 136 edges; 7 event-bearing sections, 55 events; 23 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: evelyn (actor 0, spawnSet); ti_neptune (actor 1, spawnSet); voodooqueen (actor 2, community); judy (actor 3, spawnDespawn); male_generic (actor 4, spawnDespawn); bd_replacer (actor 5, spawnSet); Player (actor 6, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioDurationEvent` | 12 | 344 / 365 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/16` |
| `scnDialogLineEvent` | 23 | 33 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnPlaySkAnimEvent` | 7 | 33 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scneventsAttachPropToPerformer` | 1 | 344 / 331 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/0` |
| `scneventsAttachPropToWorld` | 1 | 169 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/3` |
| `scneventsBraindanceVisibilityEvent` | 2 | 344 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/10` |
| `scneventsCameraParamsEvent` | 1 | 344 / 356 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/7` |
| `scneventsClueEvent` | 2 | 344 / 363 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/14` |
| `scneventsPlayRidCameraAnimEvent` | 1 | 344 / 358 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/9` |
| `scneventsSocket` | 2 | 344 / 362 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/13` |
| `scneventsVFXBraindanceEvent` | 1 | 344 / 367 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/18` |
| `scneventsVFXEvent` | 2 | 169 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, skeletal_animation: 1
- speech, props_equipment, vfx: 1
- speech, skeletal_animation, camera, rid_camera, props_equipment, audio, vfx, socket_signal, clues, bd_visibility_ui: 1

Raw SHA-256: `39b66793362ec846d79bebe3409b10739c59b56f3d7054bc3b7c0b4e84dce5fe`. Binary SHA-256: `c1d04928daf96a0f3ae9072feafdcb699fb1d13e1073029478f0685e93c3f1ef`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q105\scenes\q105_12b_braindance_alt.scene" --events
```

## `base\quest\secondary_characters\default_dialogues\judy_default.scene`

281 graph nodes, 361 edges; 53 event-bearing sections, 438 events; 122 screenplay lines, 44 screenplay options, 15 choice nodes.

Actors: Judy (actor 0, spawnSet); Judy_holocall (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `in` → 1; `holocall_in` → 1326; `sq030_lake` → 1570; `q105_cardrive` → 594.

Exits: `out` → 2; `holocall_out` → 1331; `sq030_lake_done` → 1568; `holo_to_ftf_out` → 1380; `q105_cardrive_done` → 595.

End nodes: 2: `<omitted>`; 595: `<omitted>`; 1331: `<omitted>`; 1380: `NonTerminating`; 1568: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 77 | 50 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnDialogLineEvent` | 115 | 47 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 268 / 429 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/7` |
| `scnIKEvent` | 2 | 268 / 420 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/3` |
| `scnLookAtEvent` | 65 | 47 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 94 | 47 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 1 | 268 / 435 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 1 | 268 / 431 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/9` |
| `scneventsSocket` | 82 | 47 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 28
- speech, idle_animation, socket_signal: 6
- speech, idle_animation: 4
- gaze: 4
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze, socket_signal: 1
- idle_animation, gaze: 1

Raw SHA-256: `371fe7fc185c757fdf76e62236678a1f9f25e65c62d1a849b496119cfc02a306`. Binary SHA-256: `fba396f17b3d174d22ff82bf5d67ef71cd342dd44f4bee1fc2611ec392f746f6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\secondary_characters\default_dialogues\judy_default.scene" --events
```

