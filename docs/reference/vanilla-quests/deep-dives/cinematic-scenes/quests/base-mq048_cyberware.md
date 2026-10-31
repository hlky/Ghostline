# Upgrade U: scene presentation

Journal identity: `quests/minor_quest/mq048_cyberware`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq048_cyberware.md) · [All cinematic studies](../README.md)

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

## `base\quest\main_quests\prologue\q001\scenes\q001_00a_before_mission.scene`

182 graph nodes, 257 edges; 28 event-bearing sections, 132 events; 43 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: tbug (actor 0, findInContext); jackie (actor 1, spawnSet); old_lady (actor 2, community); tbug_holo (actor 3, spawnSet); v (actor 4, findInContext).

Entries: `q001_bef_mission_in` → 1; `q001_jackie_elevator_in` → 1817; `TEST` → 2429; `Q001_digital_sickness` → 2163; `backup_lines` → 1764; `backup_lines2` → 1766; `backup_lines3` → 1768.

Exits: `q001_bef_mission_out` → 6; `q001_jackie_elevator_out` → 1824; `Q001_digital_sickness_kill` → 2212.

End nodes: 6: `NonTerminating`; 1824: `NonTerminating`; 2212: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 10 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnChangeIdleAnimEvent` | 6 | 147 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnDialogLineEvent` | 18 | 2 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 10 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scnIKEvent` | 2 | 10 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnLookAtEvent` | 32 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 31 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 1 | 10 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 1 | 10 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scneventsSocket` | 24 | 4 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 11 | 10 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- skeletal_animation: 4
- skeletal_animation, gaze: 4
- vfx: 3
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- gaze: 1

Raw SHA-256: `4f15d3f5bb90c117d6b544d349eedcf183220092a1c401f7d29394583ca82da5`. Binary SHA-256: `11d27d0fe59bdbd76ea0d5ccfa23ab1d9cc877b7866999d350c91382df5e6e3c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00a_before_mission.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00aa_jackie_hide_body_tutorial.scene`

60 graph nodes, 69 edges; 10 event-bearing sections, 36 events; 18 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: jackie (actor 0, spawnSet); tbug (actor 1, findInContext); scavenger_takedown (actor 2, community); Player (actor 3, findInContext).

Entries: `disposal_tutorial` → 1; `room_04` → 8; `takedown_tutorial` → 14; `takedown_npc_work` → 139; `dialogue_tutorial` → 18; `Start 6` → 222; `finished_talking` → 41; `hide_body_2_in` → 109.

Exits: `takedown` → 72; `disposal` → 77; `finished_talking_out` → 96; `End 2` → 37; `dialogue_tutorial_end` → 100; `room_04_end` → 103; `hide_body_2_out` → 110.

End nodes: 37: `<omitted>`; 72: `<omitted>`; 77: `<omitted>`; 96: `<omitted>`; 100: `<omitted>`; 103: `<omitted>`; 110: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 15 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnChangeIdleAnimEvent` | 3 | 15 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnDialogLineEvent` | 12 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 15 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/16` |
| `scnIKEvent` | 2 | 15 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |
| `scnLookAtEvent` | 2 | 15 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 4 | 15 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnUnmountEvent` | 1 | 15 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 1 | 15 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |
| `scneventsSocket` | 9 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, socket_signal: 1
- idle_animation: 1

Raw SHA-256: `337bb1c8c076fe2ab11bd1f7971bd531bc9ae7d84268289ace60917ce6136d1e`. Binary SHA-256: `bf2ccb2288911c0d5d9768cc93ebd779712b7f278783f37e479e2215abbbf41c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00aa_jackie_hide_body_tutorial.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00ab_jackie_double_takedown.scene`

26 graph nodes, 23 edges; 6 event-bearing sections, 11 events; 11 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: jackie (actor 0, spawnSet); tbug (actor 1, findInContext); scav_7_wheelchair (actor 2, community); scav_5_following_wheelchair (actor 3, community); Player (actor 4, findInContext).

Entries: `initiate_takedown` → 1; `jackie_stealth` → 31; `after_takedown` → 8; `wheelchair_accident` → 38; `jackie_another_one` → 43; `tbug_stealth` → 26.

Exits: `jackie_another_one_end` → 54; `tbug_stealth_end` → 28; `jackie_stealth_end` → 33; `after_takedown_out` → 9; `wheelchair_accident_end` → 41; `initiate_takedown_end` → 52.

End nodes: 9: `<omitted>`; 28: `<omitted>`; 33: `<omitted>`; 41: `<omitted>`; 52: `<omitted>`; 54: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 11 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6

Raw SHA-256: `d295a6ac0579b3970a088e184261971351aad52ab4ffcb6d2e81ce6a5c0244c3`. Binary SHA-256: `0c5a84b81977c3c3586128eb20a12356e901ed93c1cd1a203e35fdba3f570ff9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00ab_jackie_double_takedown.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00b_dead_girl.scene`

96 graph nodes, 143 edges; 10 event-bearing sections, 45 events; 12 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: tbug (actor 0, findInContext); jackie (actor 1, spawnSet); v (actor 2, findInContext).

Entries: `Start 8` → 711; `q001_dead_girl_in` → 59; `Start_bakap` → 739; `q001_came_back_in` → 640; `not_her_in` → 649.

Exits: `q001_dead_girl_out` → 60; `not_her_out` → 651.

End nodes: 60: `NonTerminating`; 651: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 812 / 267 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/1` |
| `scnDialogLineEvent` | 8 | 61 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 824 / 294 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/8` |
| `scnIKEvent` | 2 | 824 / 286 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/1` |
| `scnLookAtEvent` | 18 | 77 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 5 | 77 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnUnmountEvent` | 1 | 824 / 293 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 1 | 824 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/6` |
| `scneventsSocket` | 7 | 82 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, skeletal_animation, gaze: 2
- speech, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `11b3e3c625d30bce3cf7052e1f60c73f5d19d13d57d2e9e436ef93125afe4aed`. Binary SHA-256: `f036221cbde19d8f863600dba85984f766ba0022bb7312c41ea9049b4187055f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00b_dead_girl.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00b_shooting.scene`

22 graph nodes, 30 edges; 7 event-bearing sections, 7 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: jackie (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `q001_scav_chase_in` → 66; `q001_jackie_battlecries_in` → 11.

Exits: `q001_scav_chase_out` → 67; `q001_jackie_battlecries_out` → 34.

End nodes: 34: `<omitted>`; 67: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 7 | 16 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7

Raw SHA-256: `745352cbd1331559dd51fbf0be9661edd1db8dbee5fb1200f536217467847fbd`. Binary SHA-256: `b0db2481585d61bb475f5973be9fb9d6021a872987c79dd996ae7ed5f44598a1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00b_shooting.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00b_tbug_reminder_secure_the_area.scene`

6 graph nodes, 4 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: tbug (actor 0, findInContext); Player (actor 1, findInContext).

Entries: `first_reminder_in` → 1; `second_reminder_in` → 8.

Exits: `first_reminder_out` → 2; `second_reminder_out` → 10.

End nodes: 2: `<omitted>`; 10: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `57a0f819c3ad5c10520a64d51c02b8de77862424797e3e9020044cd84a9c264e`. Binary SHA-256: `ed3aa8eea015c3466b18a4eda4370c120cf18bc970424abfc230ed7f1f1c44e1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00b_tbug_reminder_secure_the_area.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00c_rescuing_girl.scene`

294 graph nodes, 414 edges; 50 event-bearing sections, 579 events; 64 screenplay lines, 9 screenplay options, 9 choice nodes.

Actors: sandra_dorcet (actor 0, community); jackie (actor 1, spawnSet); tbug (actor 2, spawnDespawn); tt_soldier1 (actor 3, community); tt_soldier2 (actor 4, community); tt_medic1 (actor 5, community); tt_medic2 (actor 6, community); dead_man (actor 7, community); biomonitor (actor 8, spawnDespawn); av_speaker (actor 9, spawnDespawn); AV (actor 10, community); v (actor 11, findInContext).

Entries: `q001_get_girl_in` → 1; `q001_trauma_arrives_in` → 6; `Start 14` → 2350; `TEST` → 2351; `jackie_scav_flee_in` → 1904; `Reminder_jackie_after_boss` → 3433; `Jackie_balcony_lookat` → 2863; `q003_jackie_reaction_scavengers_van_in` → 1421; `Start 18` → 3466; `q001_jackie_comment_in` → 567.

Exits: `TO_Q001_DIGITAL_SICKNESS` → 2623; `q001_get_girl_out` → 4; `q001_trauma_arrives_out` → 13; `End_terminado` → 1765; `q001_jackie_came_out` → 1958; `q003_jackie_reaction_scavengers_van_out` → 1422; `q001_jackie_comment_out` → 568.

End nodes: 4: `NonTerminating`; 13: `NonTerminating`; 568: `<omitted>`; 1422: `NonTerminating`; 1765: `<omitted>`; 1958: `<omitted>`; 2623: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 79 | 2 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scnChangeIdleAnimEvent` | 26 | 2 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnDialogLineEvent` | 57 | 2 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/13` |
| `scnGameplayTransitionEvent` | 3 | 307 / 504 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/45` |
| `scnIKEvent` | 6 | 307 / 491 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/36` |
| `scnLookAtAdvancedEvent` | 11 | 738 / 701 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/16` |
| `scnLookAtEvent` | 64 | 2 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/21` |
| `scnPlaySkAnimEvent` | 160 | 2 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 3 | 307 / 506 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/47` |
| `scneventsAttachPropToNode` | 2 | 307 / 499 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/41` |
| `scneventsAttachPropToPerformer` | 2 | 1947 / 1200 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/4` |
| `scneventsAttachPropToWorld` | 2 | 110 / 173 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/60` |
| `scneventsCameraParamsEvent` | 4 | 297 / 421 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/9` |
| `scneventsMountEvent` | 2 | 307 / 507 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/48` |
| `scneventsRagdollEvent` | 1 | 110 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/23` |
| `scneventsSetAnimFeatureEvent` | 11 | 110 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsSetAnimsetWeight` | 18 | 110 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/22` |
| `scneventsSocket` | 85 | 2 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsVFXDurationEvent` | 1 | 2 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/15` |
| `scneventsVFXEvent` | 42 | 2 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- skeletal_animation, gaze, socket_signal: 6
- skeletal_animation: 4
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 3
- speech, gaze: 3
- camera: 3
- speech, skeletal_animation, idle_animation, audio, socket_signal: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- idle_animation: 2
- skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state, gameplay_action: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `650f777b34a94b8fa37cdfc6bc2054ab23d7e54590c88a7f9fc93ef4ff2038ba`. Binary SHA-256: `2ada0c29414034db08bd2705d13e21162af59efd56d712544aba35135d8ca896`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00c_rescuing_girl.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00cd_boss_clean.scene`

52 graph nodes, 49 edges; 6 event-bearing sections, 48 events; 11 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: jackie (actor 0, spawnSet); tbug (actor 1, findInContext); boss (actor 2, community); Player (actor 3, findInContext).

Entries: `boss_hidden` → 49; `room_clean` → 52; `jackie_through_wall_in` → 64; `after_him` → 27; `jackie_no_terminado` → 185.

Exits: `jackie_through_wall_out` → 251; `room_clean_end` → 55; `after_him_end` → 58; `boss_hidden_out` → 95.

End nodes: 55: `<omitted>`; 58: `<omitted>`; 95: `<omitted>`; 251: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 31 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 9 | 26 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 102 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/7` |
| `scnIKEvent` | 2 | 102 / 155 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/1` |
| `scnLookAtEvent` | 3 | 66 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/18` |
| `scnPlaySkAnimEvent` | 4 | 66 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnPlayVideoEvent` | 2 | 31 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 1 | 102 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/6` |
| `scneventsAttachPropToWorld` | 1 | 66 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 1 | 102 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/5` |
| `scneventsSocket` | 11 | 31 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsVFXEvent` | 5 | 66 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, audio, socket_signal, video: 1
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `0977818b635eb0edee810b1d69d0af7659a3d928fc9cea3a5bfcb39ca340b29c`. Binary SHA-256: `88c9e8e5db7402729c08d0c56c3807bdedb987ce79b2a8c04a3390ff8432b56f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00cd_boss_clean.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00d_leaving.scene`

298 graph nodes, 338 edges; 31 event-bearing sections, 109 events; 58 screenplay lines, 9 screenplay options, 3 choice nodes.

Actors: jackie (actor 0, spawnSet); tbug (actor 1, findInContext); V_tpp (actor 2, findInWorld); dex (actor 3, findInContext); wakako (actor 4, spawnSet); car_player (actor 5, spawnSet); v (actor 6, findInContext).

Entries: `q001_after_tt_left_in` → 335; `NCW_GUNS` → 3935; `NCW_GUNS_RECORDING` → 3951; `Start 8` → 1353; `Start 2` → 831.

Exits: `q001_after_tt_left_out` → 373.

End nodes: 373: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 903 / 453 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/2` |
| `scnChangeIdleAnimEvent` | 4 | 516 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnDialogLineEvent` | 24 | 425 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 516 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/11` |
| `scnIKEvent` | 8 | 516 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/5` |
| `scnLookAtEvent` | 34 | 516 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnPlaySkAnimEvent` | 13 | 516 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |
| `scnUnmountEvent` | 2 | 516 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 4 | 516 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/7` |
| `scneventsSocket` | 17 | 516 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 7
- skeletal_animation, gaze: 4
- speech: 3
- skeletal_animation, gaze, socket_signal: 3
- gaze: 3
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, idle_animation: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- gaze, socket_signal: 1
- socket_signal: 1
- gaze, ik, socket_signal, animation_state: 1

Raw SHA-256: `3d8f0ff26a22c4a9578767b55dbfd24372fa47538f9d0b29c95dbdf26c7e5744`. Binary SHA-256: `e05ee7f19f1ba3249ed998052019835d95090170d82d6673ade8d28c7909fc30`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00d_leaving.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00e_scavenger_conversation.scene`

56 graph nodes, 125 edges; 7 event-bearing sections, 22 events; 12 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: scav5 (actor 0, community); scav2 (actor 1, community); scav7 (actor 2, community); wheelchair (actor 3, community); dead_body (actor 4, community).

Entries: `q001_freezer_in` → 1; `q001_wheelchair_in` → 6.

Exits: `q001_freezer_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 83 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/0` |
| `scnDialogLineEvent` | 6 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 5 | 57 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scneventsSocket` | 3 | 78 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 2
- idle_animation: 2
- speech: 1
- skeletal_animation: 1
- idle_animation, socket_signal: 1

Raw SHA-256: `fe1ca5cc5b09a93711400a782c12203cd8d966f8459cf84c8250b052d79d5177`. Binary SHA-256: `04dd5d20931a498df80d38ff472ded625fa2618ce6a9f7f7a20554a29615400c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00e_scavenger_conversation.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00f_ride_with_jackie.scene`

210 graph nodes, 224 edges; 32 event-bearing sections, 244 events; 64 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: jackie (actor 0, spawnSet); police1 (actor 1, community); police2 (actor 2, community); pedestrian_01 (actor 3, community); pedestrian_02 (actor 4, community); scav_driver (actor 5, community); player_car (actor 6, spawnSet); police_car1 (actor 7, community); police_car2 (actor 8, community); Player (actor 9, findInContext).

Entries: `Start 7` → 650; `aft_blockade_in` → 1713; `scavs_chat_to_mb_01_in` → 33; `blockade_in` → 38; `scavs_car_appears_in` → 102; `scavs_intersection_in` → 112; `blackade_jackie_stops` → 326; `scavs_jackie_improvises_in` → 117; `scavs_pedestrians_in` → 122; `scavs_ramming_in` → 127; `scavs_chase_over_in` → 132; `OLD` → 349; `scavs_crash_in` → 138; `Start 8` → 774; `scavs_chat_to_mb_02_in` → 143.

Exits: `scavs_chat_to_mb_01_out` → 34; `arrived_mb_out` → 39; `scavs_car_appears_out` → 103; `scavs_intersection_out` → 113; `scavs_jackie_improvises_out` → 118; `scavs_pedestrians_out` → 123; `scavs_ramming_out` → 128; `scavs_chase_over_out` → 133; `scavs_crash_out` → 139; `scavs_chat_to_mb_02_out` → 144.

End nodes: 34: `<omitted>`; 39: `NonTerminating`; 103: `<omitted>`; 113: `<omitted>`; 118: `<omitted>`; 123: `<omitted>`; 128: `<omitted>`; 133: `<omitted>`; 139: `<omitted>`; 144: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 59 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/11` |
| `scnChangeIdleAnimEvent` | 12 | 35 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 55 | 35 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnGameplayTransitionEvent` | 3 | 40 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/15` |
| `scnIKEvent` | 20 | 35 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnLookAtAdvancedEvent` | 1 | 44 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnLookAtEvent` | 54 | 35 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 325 / 403 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/3` |
| `scnPlaySkAnimEvent` | 42 | 35 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 4 | 44 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/6` |
| `scnUnmountEvent` | 3 | 40 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 11 | 35 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 33 | 35 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 3 | 694 / 789 | `/Data/RootChunk/sceneGraph/Data/graph/123/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, vfx, socket_signal, animation_state: 1
- animation_state: 1
- gaze: 1
- vfx: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `5f1402d5a15686f599d4c1ed863da022e0bfbe838496ad2484dc2c2b516af22e`. Binary SHA-256: `1527da5af1765a74be20b0cd04fd1a4709d777b382380b130976ff3907b08536`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00f_ride_with_jackie.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00ff_max_tac.scene`

45 graph nodes, 80 edges; 6 event-bearing sections, 105 events; 15 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: jackie (actor 0, spawnSet); bandit_big (actor 1, community); bandit_male (actor 2, community); bandit_fem (actor 3, community); maxtac_fem (actor 4, community); maxtac_big (actor 5, community); victim (actor 6, community); av (actor 7, community); cortes (actor 8, community); hella (actor 9, spawnSet); Player (actor 10, findInContext).

Entries: `Start 0` → 1; `for_preeview` → 95; `MERCS for export` → 26.

Exits: `End 1` → 22.

End nodes: 22: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 4 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scnDialogLineEvent` | 14 | 4 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scnIKEvent` | 6 | 4 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 96 / 271 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/3` |
| `scnPlaySkAnimEvent` | 21 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 4 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/13` |
| `scneventsSocket` | 44 | 4 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/16` |
| `scneventsVFXEvent` | 13 | 4 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/17` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, ik, socket_signal, animation_state: 2
- speech, skeletal_animation, ik, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation: 1
- speech: 1
- socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `93c3663219c935e103853370a1c15182bb07880afca7650f1a9923eb1e1fe257`. Binary SHA-256: `91625b91dea63e444235d62cf89983564308e06b539780a9d2dfc274a75414fd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00ff_max_tac.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00g_broken_gate.scene`

19 graph nodes, 18 edges; 4 event-bearing sections, 51 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: mb_resident1 (actor 0, community); mb_resident2 (actor 1, community).

Entries: `gate_broken_in` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnDialogLineEvent` | 3 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnGameplayTransitionEvent` | 3 | 4 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/23` |
| `scnIKEvent` | 6 | 4 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/14` |
| `scnLookAtEvent` | 4 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 10 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 3 | 4 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/22` |
| `scneventsEquipItemToPerformer` | 2 | 7 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 3 | 4 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/20` |
| `scneventsSocket` | 14 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 1 | 7 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `6d1eb51c4d96c3451b831e64fc1297d7f675ec560f316b5fbf34d63e12a9a2fc`. Binary SHA-256: `ad1a1831b1244b67eeb31219a6fe67f13faa28b2a28b8101467a4bd68cd8cf5f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00g_broken_gate.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_01_wakeup.scene`

65 graph nodes, 66 edges; 9 event-bearing sections, 40 events; 22 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: stanley (actor 0, spawner); jackie (actor 1, spawnSet); v (actor 2, findInContext).

Entries: `q001_wakeup_in` → 0; `Start 8` → 885; `go_to_sleep_in` → 712; `wakeup_logo_bik` → 258; `Start 9` → 926.

Exits: `q001_wakeup_out` → 4; `go_to_sleep_out` → 717.

End nodes: 4: `<omitted>`; 717: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 726 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/1` |
| `scnDialogLineEvent` | 15 | 620 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnLookAtEvent` | 1 | 620 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnPlaySkAnimEvent` | 2 | 726 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/0` |
| `scneventsSocket` | 7 | 620 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scneventsVFXEvent` | 11 | 620 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- skeletal_animation, audio, vfx, socket_signal: 2
- speech, gaze, vfx, socket_signal: 1
- speech, vfx, socket_signal: 1
- speech, vfx: 1

Raw SHA-256: `32f72724274f6b53acd018444c783a9cdc45dd072d27aad06a92ad0cf3ee4928`. Binary SHA-256: `a38f2e8894a9f4acb92c8d3ac5e42ec9fbd1bedcbf5b0f7b99f58d82b02ba1e1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_01_wakeup.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_01aa_epilog_house_av.scene`

15 graph nodes, 15 edges; 0 event-bearing sections, 0 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: woman (actor 0, community); av (actor 1, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |

Presentation families coexisting in an event section (counts are sections, not durations):


Raw SHA-256: `bb2f1ef647f5ff252569f998814e7e33004967c6c1991ce8370c84bf96f1cc06`. Binary SHA-256: `e11c75691352e8d5a83912bb40d9ebe6ae8998918a3ed13e5b50c5e4b1616a0b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_01aa_epilog_house_av.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_03a_jackie_dex_intro.scene`

198 graph nodes, 222 edges; 33 event-bearing sections, 395 events; 102 screenplay lines, 27 screenplay options, 8 choice nodes.

Actors: dex (actor 0, spawnSet); dex_bdg (actor 1, spawnSet); dex_limo (actor 2, community); v (actor 3, findInContext).

Entries: `q001_meet_dex_in` → 97; `Start 6` → 2384; `Start 5` → 1870.

Exits: `q001_meet_dex_out` → 6.

End nodes: 6: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 624 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnChangeIdleAnimEvent` | 11 | 624 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnDialogLineEvent` | 74 | 635 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnGameplayActionEvent` | 1 | 1844 / 814 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/8` |
| `scnGameplayTransitionEvent` | 1 | 1176 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/5` |
| `scnIKEvent` | 6 | 1176 / 309 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/1` |
| `scnLookAtEvent` | 98 | 624 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 95 | 624 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnUnmountEvent` | 1 | 1176 / 320 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/9` |
| `scneventsAttachPropToPerformer` | 5 | 624 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsAttachPropToWorld` | 2 | 856 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 33 | 639 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scneventsSocket` | 51 | 624 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scneventsVFXEvent` | 5 | 685 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/21` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal, animation_state: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 4
- gaze: 3
- speech, skeletal_animation, gaze: 2
- skeletal_animation, gaze, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, audio, socket_signal, animation_state: 1
- speech, skeletal_animation: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1

Raw SHA-256: `88c668accd399ee4a874080d6a6a70e05fe3e333dd42a6cc3737c93ce9710f1e`. Binary SHA-256: `953b074432cfefcbb41eb9542dc25652943fb2fdd3641b61122d0e459b778383`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_03a_jackie_dex_intro.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_03a_meet_jackie_downstairs.scene`

200 graph nodes, 243 edges; 42 event-bearing sections, 409 events; 76 screenplay lines, 16 screenplay options, 8 choice nodes.

Actors: jackie (actor 0, spawnSet); dex (actor 1, findInWorld); dex bodyguard (actor 2, findInWorld); militech_agent (actor 3, findInWorld); cook (actor 4, community); v_tec (actor 5, spawnSet); v (actor 6, findInContext).

Entries: `q001_jackie_mb_in` → 960; `Start 5` → 1732; `q001_arrived_to_rd_in` → 1193.

Exits: `q001_jackie_mb_out` → 961; `q001_jackie_left_out` → 1515; `prefab_prefetch` → 2071; `q001_arrived_to_rd_out` → 1194.

End nodes: 961: `NonTerminating`; 1194: `<omitted>`; 1515: `<omitted>`; 2071: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1519 / 1062 | `/Data/RootChunk/sceneGraph/Data/graph/94/Data/events/2` |
| `scnChangeIdleAnimEvent` | 35 | 967 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 58 | 962 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 975 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scnIKEvent` | 4 | 975 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnLookAtEvent` | 77 | 962 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 152 | 962 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 2 | 975 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/13` |
| `scneventsAttachPropToPerformer` | 4 | 967 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/11` |
| `scneventsAttachPropToWorld` | 4 | 967 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsCameraParamsEvent` | 3 | 1994 / 1617 | `/Data/RootChunk/sceneGraph/Data/graph/165/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 2 | 975 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/10` |
| `scneventsSocket` | 47 | 962 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsVFXEvent` | 18 | 967 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- skeletal_animation, gaze: 7
- skeletal_animation: 5
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 3
- camera: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, vfx: 1
- speech: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, socket_signal: 1

Raw SHA-256: `ff48765cbfbb1a76a7c073b442105251af5a6ba690218eb362cf8fe678b38209`. Binary SHA-256: `7eaf22d94484cbddafa9984e110f005b18a8d88a1acf9ec0e3578dadbf177284`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_03a_meet_jackie_downstairs.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_04_ripperdoc.scene`

391 graph nodes, 386 edges; 45 event-bearing sections, 715 events; 119 screenplay lines, 36 screenplay options, 16 choice nodes.

Actors: viktor (actor 0, spawnSet); boxing_commentator (actor 1, spawner); v_tpp_fem (actor 2, spawner); v_tpp_male (actor 3, spawner); sdsd (actor 4, spawnSet); v (actor 5, findInContext).

Entries: `q001_ripperdoc_in` → 1; `Start 9` → 2614; `Start 7` → 2318; `Start 6` → 2018; `Start 8` → 2343; `Start 2` → 1407; `Start 4` → 1870.

Exits: `q001_rd_chat_done_out` → 1260; `q001_ripperdoc_out` → 2.

End nodes: 2: `NonTerminating`; 1260: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 120 | 3 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scnChangeIdleAnimEvent` | 79 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 90 | 3 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/17` |
| `scnGameplayTransitionEvent` | 2 | 313 / 485 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/19` |
| `scnIKEvent` | 7 | 3 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/40` |
| `scnLookAtAdvancedEvent` | 11 | 272 / 266 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/37` |
| `scnLookAtEvent` | 50 | 3 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |
| `scnPlaySkAnimEvent` | 166 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 2 | 313 / 492 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/25` |
| `scneventsAttachPropToPerformer` | 7 | 297 / 320 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/11` |
| `scneventsAttachPropToWorld` | 7 | 52 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/14` |
| `scneventsCameraParamsEvent` | 7 | 272 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 2 | 313 / 488 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/22` |
| `scneventsSocket` | 141 | 3 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsVFXEvent` | 24 | 3 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 4
- speech: 4
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 4
- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- speech, skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, socket_signal: 2
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, audio: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, gaze: 1
- camera: 1

Raw SHA-256: `df11cdf0b327b2913ea6164b297cac045a4496c32c8a3b1dcb05d91c90e061fe`. Binary SHA-256: `42936da965ee84731061a69823ea91a150f6e7461dba8e27abdd65005431a671`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_04_ripperdoc.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_04a_rd_assistant.scene`

84 graph nodes, 112 edges; 24 event-bearing sections, 117 events; 36 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: assistant (actor 0, spawnSet); jackie (actor 1, spawnSet); kitty (actor 2, spawner); v (actor 3, findInContext).

Entries: `q001_kitty_in` → 869; `q001_kitty2_in` → 871; `for tests` → 975; `q001_04a_first_entry` → 551; `q001_jackie_goes_in` → 729; `q001_04a_after_victor` → 572.

Exits: `q001_jackie_goes_out` → 730; `q001_04a_first_entry_end` → 561.

End nodes: 561: `NonTerminating`; 730: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 355 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnChangeIdleAnimEvent` | 12 | 43 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnDialogLineEvent` | 18 | 44 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 594 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/14` |
| `scnIKEvent` | 2 | 594 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/6` |
| `scnLookAtEvent` | 24 | 43 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/6` |
| `scnPlaySkAnimEvent` | 31 | 43 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnPoseCorrectionEvent` | 5 | 620 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |
| `scnUnmountEvent` | 1 | 594 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/13` |
| `scneventsAttachPropToPerformer` | 2 | 43 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 594 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/10` |
| `scneventsSocket` | 18 | 43 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2
- speech, skeletal_animation: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation: 2
- skeletal_animation, idle_animation: 2
- skeletal_animation, gaze: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, audio: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- idle_animation, audio: 1
- socket_signal: 1

Raw SHA-256: `7497c9d666b997c8cdb950a9add375decafc3a0fa24e4095fcb9e12720602782`. Binary SHA-256: `54f8971b0ae080532ddf8bf7ee7961a2a8f33f89be14d6462a9191a6741770e6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_04a_rd_assistant.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_05_tbug_netrunner_tut.scene`

12 graph nodes, 11 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: tbug (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 26 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `1fb1d977b220e939604a8902aa10ac7b19ed7033347e64f8f58eb32f5a58a900`. Binary SHA-256: `0691a31a3994e2874ac2a19df96412186916cda46ef962f49035932947478534`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_05_tbug_netrunner_tut.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_00_call_jackie.scene`

96 graph nodes, 119 edges; 23 event-bearing sections, 98 events; 49 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: Jackie (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `q003_00_call_jackie_in` → 9; `after_evely_preview` → 397; `before_malestrom_preview` → 310; `linesforreuse` → 416; `q003_00_status_update_in` → 74.

Exits: `q003_00_call_jackie_out` → 10; `q003_00_status_update_out` → 75.

End nodes: 10: `<omitted>`; 75: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 21 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnDialogLineEvent` | 47 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnLookAtEvent` | 6 | 129 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/6` |
| `scnPlaySkAnimEvent` | 20 | 84 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scneventsCameraEvent` | 1 | 318 / 296 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/0` |
| `scneventsSocket` | 3 | 129 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation: 8
- speech, idle_animation: 7
- speech, skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, idle_animation, gaze, socket_signal: 1
- camera: 1
- gaze: 1

Raw SHA-256: `7627e4952b0a2ac1e07b6961383fceb58e9205847c7bb2cecbf9086bc05df746`. Binary SHA-256: `29a840ddd9b9a8669921a257b98b5152f551ab15af450b7969435f43dc221ddd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_00_call_jackie.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_01_call_militech.scene`

76 graph nodes, 91 edges; 11 event-bearing sections, 44 events; 16 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: Meredith (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `q003_01_at_place_in` → 2902; `meredith_holocall_prev` → 3067; `q003_01a_militech_call_in` → 2710; `sq011_wait_concert_in` → 3312.

Exits: `q003_01_at_place_out` → 2903; `Kill Signal` → 3139; `q003_01a_militech_call_out` → 2711; `sq011_wait_concert_out` → 3313; `q003_01_at_place_spawning_out` → 2955.

End nodes: 2711: `<omitted>`; 2903: `<omitted>`; 2955: `NonTerminating`; 3139: `<omitted>`; 3313: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 2824 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnChangeIdleAnimEvent` | 6 | 2709 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnDialogLineEvent` | 12 | 2709 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 2988 / 139 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/7` |
| `scnIKEvent` | 2 | 2988 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |
| `scnLookAtEvent` | 3 | 2713 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 6 | 2824 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnUnmountEvent` | 1 | 2988 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/6` |
| `scneventsAttachPropToPerformer` | 1 | 2713 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsCameraEvent` | 1 | 3063 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 3063 / 227 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 1 | 2988 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/3` |
| `scneventsSocket` | 6 | 2824 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |
| `scneventsVFXEvent` | 2 | 2910 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, idle_animation: 1
- speech, idle_animation, gaze, props_equipment: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- camera: 1
- vfx, socket_signal: 1

Raw SHA-256: `093bd08f6fd72c8d4f8fad8b3f3f0a21b71febdd01cc548e4671bb9abdb4c63a`. Binary SHA-256: `8c127724b75a30aea8e494832d10143a67043fccbaf77e7cac98a1d9b4e71d89`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_01_call_militech.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_01a_militech.scene`

266 graph nodes, 346 edges; 55 event-bearing sections, 457 events; 93 screenplay lines, 19 screenplay options, 7 choice nodes.

Actors: Jackie (actor 0, spawnSet); Meredith (actor 1, spawnSet); Bodyguard01 (actor 2, community); Bodyguard02 (actor 3, community); Anthony (actor 4, spawnSet); DRONE (actor 5, community); SUVwithDRONE (actor 6, community); suv (actor 7, community); Player (actor 8, findInContext).

Entries: `full_scene_prev` → 3684; `Start 16` → 3494; `q003_01a_militech_suv_idle` → 3500; `Start 19` → 3733; `Start 20` → 9975; `q003_malware_removed_in` → 2850; `q003_01a_militech_in` → 1470; `decision_preview` → 3350.

Exits: `q003_01a_militech_out` → 2337; `q003_malware_removed_out` → 2851.

End nodes: 2337: `<omitted>`; 2851: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 51 | 1097 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnChangeIdleAnimEvent` | 29 | 1097 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scnDialogLineEvent` | 74 | 1417 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/24` |
| `scnGameplayTransitionEvent` | 1 | 1448 / 415 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/32` |
| `scnIKEvent` | 2 | 1448 / 403 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/21` |
| `scnLookAtAdvancedEvent` | 1 | 3484 / 1562 | `/Data/RootChunk/sceneGraph/Data/graph/167/Data/events/3` |
| `scnLookAtEvent` | 77 | 1097 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 117 | 1097 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPoseCorrectionEvent` | 4 | 1417 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnUnmountEvent` | 1 | 1448 / 414 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/31` |
| `scneventsAttachPropToPerformer` | 1 | 1448 / 397 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/19` |
| `scneventsAttachPropToWorld` | 1 | 1844 / 469 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/7` |
| `scneventsCameraParamsEvent` | 7 | 1417 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/21` |
| `scneventsSetAnimFeatureEvent` | 1 | 1448 / 410 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/28` |
| `scneventsSocket` | 76 | 1097 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/18` |
| `scneventsVFXEvent` | 14 | 1097 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/16` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 14
- gaze: 11
- speech, skeletal_animation, idle_animation, gaze, audio: 4
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- speech, gaze: 2
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx: 1
- speech, skeletal_animation, gaze, audio: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- camera, vfx: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `60e98007c45d2b540c23888a855956e158f0f92ffbae28be40999ddaee8d4ab3`. Binary SHA-256: `273bc29a9cc23f202771fb4fe2f23234f7b7c81923ead6ef83df274438ef6393`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_01a_militech.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_01b_meat_factory.scene`

211 graph nodes, 318 edges; 33 event-bearing sections, 195 events; 62 screenplay lines, 12 screenplay options, 6 choice nodes.

Actors: Jackie (actor 0, spawnSet); Royce (actor 1, findInContext); DumDum (actor 2, spawnDespawn); Jackie_bike (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `q003_meet_jackie_in` → 1674; `q003_meet_jackie_interrupted_in` → 1873; `q003_bike_idle_in` → 2863; `q003_intercom_interrupted_in` → 1907; `walk_to_factory` → 2488; `Start 16` → 2499.

Exits: `q003_meet_jackie_out` → 1675; `q003_meet_jackie_interrupted_out` → 1871; `q003_intercom_interrupted_out` → 1900.

End nodes: 1675: `<omitted>`; 1871: `<omitted>`; 1900: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 2020 / 545 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/3` |
| `scnChangeIdleAnimEvent` | 22 | 1498 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 53 | 1498 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 2020 / 537 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/0` |
| `scnLookAtEvent` | 33 | 1498 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 36 | 1498 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 13 | 1679 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scneventsSocket` | 32 | 1550 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsVFXDurationEvent` | 3 | 1547 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 6
- speech: 3
- skeletal_animation, idle_animation: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, gaze: 2
- speech, gaze, vfx: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, gaze: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, gameplay_action: 1

Raw SHA-256: `74a05476eed334fc80183904fdefc56c2c28c67eed827629519d0f09a87b6fe8`. Binary SHA-256: `752c6909e56f25fe0f55915f5fb032071ce0d17cd7b57efbf2f67811a95203e4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_01b_meat_factory.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_02_maelstrom_corridor.scene`

177 graph nodes, 266 edges; 19 event-bearing sections, 70 events; 24 screenplay lines, 8 screenplay options, 8 choice nodes.

Actors: Jackie (actor 0, spawnSet); welding_maelstromer (actor 1, spawner); Player (actor 2, findInContext).

Entries: `q003_maelstrom_corridor_in` → 2; `jackie_enter_hall` → 1888; `CYB-657661_retrofix_in` → 2072.

Exits: `q003_maelstrom_corridor_out` → 43; `q003_no_deal_triggered_out` → 1352.

End nodes: 43: `NonTerminating`; 1352: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 188 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 17 | 51 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 4 | 1215 / 252 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/8` |
| `scnIKEvent` | 8 | 1215 / 244 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/1` |
| `scnLookAtEvent` | 6 | 51 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 11 | 51 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnUnmountEvent` | 4 | 1215 / 251 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 4 | 1215 / 247 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/4` |
| `scneventsSocket` | 15 | 194 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 4
- speech: 4
- speech, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `3d1a61881416b56e2464f9e9caef4a8125abcc05a7c71e54737a9380de1990e7`. Binary SHA-256: `2bc5d4d9d18861840350b7c33216fe263330ab09a3f473f1ff2f654d20ff9a8b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_02_maelstrom_corridor.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_02_maelstrom_corridor_part2.scene`

114 graph nodes, 169 edges; 23 event-bearing sections, 51 events; 28 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Jackie (actor 0, spawnSet); Kurt (actor 1, community); Ganger_Catwalk (actor 2, community); Ganger_Catwalk_Hall_01 (actor 3, community); Ganger_Catwalk_Hall_02 (actor 4, community); Lars (actor 5, community); Ganger_Catwalk_Scene_01 (actor 6, community); Ganger_Catwalk_Scene_02 (actor 7, community); Player (actor 8, findInContext).

Entries: `q003_maelstrom_corridor_p2_in` → 744; `q003_02_riding_elevator_in` → 976.

Exits: `q003_maelstrom_corridor_p2_out` → 43; `q003_02_riding_elevator_out` → 973.

End nodes: 43: `NonTerminating`; 973: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 252 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnChangeIdleAnimEvent` | 2 | 252 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scnDialogLineEvent` | 20 | 272 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnLookAtEvent` | 11 | 252 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 8 | 252 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsSocket` | 6 | 252 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scneventsVFXDurationEvent` | 1 | 252 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, gaze: 3
- gaze: 2
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, socket_signal: 1
- idle_animation, gaze: 1

Raw SHA-256: `3290c65fbc6eec8735fa04d81d92bc17f2eefc03afb4199337ef90468cb4cb58`. Binary SHA-256: `2ed9dd67db26ca530239ca899176a3f11927eee918ceacc302a1e514dd6bd8fb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_02_maelstrom_corridor_part2.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_02_no_deal.scene`

119 graph nodes, 117 edges; 20 event-bearing sections, 77 events; 35 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Jackie (actor 0, spawnSet); DumDum (actor 1, spawnSet); Royce (actor 2, spawnDespawn); Netrunner (actor 3, community); Executioner (actor 4, community); Player (actor 5, findInContext).

Entries: `q003_02_die_fuckers_in` → 1; `q003_02_dumdum_kill_intruders_in` → 7; `q005_01_plan_lets_see_in` → 342; `q003_02_mealstrom_dead_in` → 12; `q003_02_mealstrom_dead_elevator_in` → 17; `q003_02_mealstrom_more_office_in` → 22; `q003_02_royce_no_deal_in` → 27; `q003_02_open_world_mealstrom_attacked_in` → 270; `royce_footage_preview` → 396; `q003_02_jackie_shooting_dumdum_in` → 92.

Exits: `q003_02_die_fuckers_out` → 2; `q003_02_dumdum_kill_intruders_out` → 8; `q005_01_plan_lets_see_out` → 343; `q003_02_mealstrom_dead_out` → 13; `q003_02_mealstrom_dead_elevator_out` → 18; `q003_02_mealstrom_more_office_out` → 23; `q003_02_royce_no_deal_out` → 28; `q003_02_open_world_mealstrom_attacked_out` → 272; `q003_02_jackie_shooting_dumdum_out` → 93.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 13: `<omitted>`; 18: `<omitted>`; 23: `<omitted>`; 28: `<omitted>`; 93: `<omitted>`; 272: `<omitted>`; 343: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 134 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/2` |
| `scnChangeIdleAnimEvent` | 11 | 29 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scnDialogLineEvent` | 30 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 11 | 29 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/11` |
| `scnPlaySkAnimEvent` | 10 | 29 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scneventsCameraEvent` | 1 | 416 / 367 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 416 / 369 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/1` |
| `scneventsSocket` | 12 | 29 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation: 1
- idle_animation, gaze, camera, socket_signal: 1

Raw SHA-256: `8074335ed27c15e734f61cbfdf691178d02b63bd8d8558c80538fb15e4dbf8a9`. Binary SHA-256: `b3cb9997b0fa1ca3af0b33d7418debde728e8a2b40e8a59f104ef0e26649c1e3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_02_no_deal.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_03_deal.scene`

668 graph nodes, 853 edges; 96 event-bearing sections, 1377 events; 213 screenplay lines, 32 screenplay options, 14 choice nodes.

Actors: Royce (actor 0, spawnSet); Lars (actor 1, community); Jackie (actor 2, spawnSet); DumDum (actor 3, spawnSet); Kurt (actor 4, community); Netrunner (actor 5, community); spiderbot (actor 6, community); spiderbot_case (actor 7, community); Player (actor 8, findInContext).

Entries: `q003_03_deal_in` → 2771; `standoff_preview` → 8616; `Start 32` → 9144; `q003_03_brick_killed_in` → 8109; `royce_enters_preview` → 8639; `trailer_prev` → 10218; `post_deal_dialogue_preview` → 8660; `sitting_with_dum_prev` → 9229; `royce_backroom_prev` → 8890.

Exits: `q003_03_deal_peaceful_out` → 5809; `q003_03_deal_hostile_out` → 9019; `Kill Signal Peaceful` → 9034; `q003_03_deal_militech_chip_out` → 2792; `q003_03_brick_killed_out` → 8110; `Kill Signal Hostile` → 7233.

End nodes: 2792: `NonTerminating`; 5809: `NonTerminating`; 7233: `<omitted>`; 8110: `<omitted>`; 9019: `<omitted>`; 9034: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 101 | 3863 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/9` |
| `scnChangeIdleAnimEvent` | 79 | 3835 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnDialogLineEvent` | 175 | 3835 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scnGameplayTransitionEvent` | 29 | 3888 / 340 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/43` |
| `scnIKEvent` | 58 | 3888 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/5` |
| `scnLookAtAdvancedEvent` | 6 | 3863 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/59` |
| `scnLookAtEvent` | 197 | 3835 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnPlayRidAnimEvent` | 1 | 7322 / 2178 | `/Data/RootChunk/sceneGraph/Data/graph/146/Data/events/2` |
| `scnPlaySkAnimEvent` | 286 | 3835 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPoseCorrectionEvent` | 4 | 3835 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scnUnmountEvent` | 29 | 3888 / 341 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/44` |
| `scneventsAttachPropToNode` | 1 | 6476 / 1264 | `/Data/RootChunk/sceneGraph/Data/graph/74/Data/events/5` |
| `scneventsAttachPropToPerformer` | 20 | 3835 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsAttachPropToWorld` | 7 | 3863 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 29 | 3888 / 338 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/42` |
| `scneventsSocket` | 305 | 3835 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scneventsVFXDurationEvent` | 9 | 3863 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/17` |
| `scneventsVFXEvent` | 41 | 3835 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- speech, skeletal_animation: 6
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 5
- speech, skeletal_animation, socket_signal: 5
- idle_animation: 5
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- gaze: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, audio, vfx, socket_signal: 2
- skeletal_animation, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation: 2
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- idle_animation, audio: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- speech, audio: 1
- skeletal_animation, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, rid_actor, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal, animation_state: 1
- idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- idle_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- vfx: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `8cee04932d57d0b16dc65d5dd4fe0e6974baf97ac5f9528967b06e50316f90c2`. Binary SHA-256: `bdf35602e6e3b5ccca2f3a2c51a3a6deee48fa2a7239a2154a237f26a9729dd7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_03_deal.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_03a_militech_invades.scene`

334 graph nodes, 390 edges; 51 event-bearing sections, 299 events; 78 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Jackie (actor 0, spawnSet); Spiderbot_case (actor 1, findInWorld); spiderbot (actor 2, findInWorld); DumDum (actor 3, spawnSet); Ganger_Garage_Scene_01 (actor 4, community); Ganger_Garage_Scene_02 (actor 5, community); Ganger_Garage_Scene_03 (actor 6, community); Kurt (actor 7, community); Lars (actor 8, community); Player (actor 9, findInContext).

Entries: `Start 6` → 2112; `q003_03a_militech_invades_in` → 45; `walk_downstairs_preview` → 1875; `preview` → 2824; `inhaler_give_preview` → 1969; `linestoreuse` → 2639.

Exits: `q003_03a_militech_invades_out` → 46; `q003_03a_kill_signal_out` → 1044; `q003_03a_dumdum_walks_out_out` → 171; `Kill Signal` → 1461.

End nodes: 46: `NonTerminating`; 171: `NonTerminating`; 1044: `<omitted>`; 1461: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 118 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnDialogLineEvent` | 57 | 118 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/6` |
| `scnGameplayTransitionEvent` | 14 | 118 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/18` |
| `scnIKEvent` | 28 | 118 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnLookAtEvent` | 31 | 118 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnPlaySkAnimEvent` | 58 | 118 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scnUnmountEvent` | 14 | 118 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/19` |
| `scneventsAttachPropToNode` | 1 | 1594 / 968 | `/Data/RootChunk/sceneGraph/Data/graph/129/Data/events/5` |
| `scneventsAttachPropToPerformer` | 2 | 940 / 609 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 14 | 118 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/16` |
| `scneventsSocket` | 60 | 118 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/11` |
| `scneventsVFXEvent` | 14 | 124 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, skeletal_animation: 5
- skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze: 4
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, vfx: 1
- gaze: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `f3da32b37310bf4e0c56ab2a64b6d509ad70e0af719359a3fb5c172e5b704834`. Binary SHA-256: `500d73e1c984cd3aa75d70686d341dd185b1d4f85ca1213d27a3a018c5e8f742`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_03a_militech_invades.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_03b_escape_office.scene`

114 graph nodes, 136 edges; 16 event-bearing sections, 36 events; 21 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Jackie (actor 0, spawnSet); DumDum (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `q003_03b_escape_office_no_sit_in` → 2068; `q003_garage_enought_in` → 2194; `q003_03_kill_fuckers_in` → 1348; `q003_03b_escape_office_in` → 1354.

Exits: `q003_garage_enought_out` → 2195; `q003_03_kill_fuckers_out` → 1349; `q003_03b_escape_office_out` → 1355.

End nodes: 1349: `<omitted>`; 1355: `NonTerminating`; 2195: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 21 | 108 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsVFXEvent` | 15 | 1516 / 185 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, vfx: 1

Raw SHA-256: `d89d573d22b5235ebdb6e33d9e6304b267d335cc9095d5b7d4535ecc47dde86d`. Binary SHA-256: `48a7642cb053d29c36fc1d707e1c96cd44b441a1be7d85e8427c187f9d4c0060`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_03b_escape_office.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_04d_shootout_militech.scene`

264 graph nodes, 318 edges; 37 event-bearing sections, 81 events; 57 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: Jackie (actor 0, spawnSet); DumDum (actor 1, spawnSet); Militech1 (actor 2, community); Militech2 (actor 3, community); Militech3 (actor 4, community); Militech4 (actor 5, community); Militech5 (actor 6, findInWorld); Militech6 (actor 7, findInWorld); Militech7 (actor 8, findInWorld); Militech8 (actor 9, findInWorld); Militech9 (actor 10, findInWorld); Royce (actor 11, spawnSet); Militech10 (actor 12, findInWorld); Militech11 (actor 13, findInWorld); Militech12 (actor 14, findInWorld); Militech13 (actor 15, community); Militech14 (actor 16, community); MilitechMech1 (actor 17, community); MilitechMech2 (actor 18, community); Player (actor 19, findInContext).

Entries: `q003_04d_kill_militech_in` → 15; `q003_04d_militech_garage_secured_in` → 281; `q003_04d_militech_about_cargo_in` → 44; `q003_04d_militech_found_cargo_in` → 58; `q003_04d_militech_vs_royce_in` → 69; `approaching_exit_prev` → 1644; `giving_skeef_prev` → 995.

Exits: `q003_04d_kill_militech_out` → 16; `q003_04d_militech_garage_secured_out` → 282; `q003_04d_militech_about_cargo_Out` → 45; `q003_04d_militech_found_cargo_out` → 59; `q003_04d_militech_vs_royce_out` → 70.

End nodes: 16: `<omitted>`; 45: `<omitted>`; 59: `<omitted>`; 70: `NonTerminating`; 282: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 631 / 393 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/1` |
| `scnDialogLineEvent` | 53 | 17 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 852 / 620 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/7` |
| `scnIKEvent` | 2 | 852 / 613 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/1` |
| `scnLookAtEvent` | 2 | 631 / 401 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/4` |
| `scnPlaySkAnimEvent` | 7 | 631 / 394 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/2` |
| `scnUnmountEvent` | 1 | 852 / 619 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/6` |
| `scneventsAttachPropToPerformer` | 2 | 631 / 400 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 842 / 590 | `/Data/RootChunk/sceneGraph/Data/graph/119/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 852 / 617 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/5` |
| `scneventsSocket` | 10 | 17 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 31
- skeletal_animation, socket_signal: 2
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `6abf29d0e36b047a87e0c0425c634fefc255eef6ab722c6cc42860ab60b3c756`. Binary SHA-256: `2b5fc7f0f2002e77d5617e2f50c7796c9ac39c8c9e274c66c6fa9047e26bf30a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_04d_shootout_militech.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_04e_pre_combat_patrol_dialogues.scene`

27 graph nodes, 18 edges; 9 event-bearing sections, 22 events; 22 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: main_enemy_008_rifle (actor 0, community); main_enemy_007_rifle (actor 1, community); transition_enemy_014_shotgun (actor 2, community); transition_enemy_015_shotgun (actor 3, community); transition_enemy_officer_001_rifle (actor 4, community); lab_enemy_006_rifle (actor 5, community); lab_enemy_005_rifle (actor 6, community); Jackie (actor 7, spawnSet); Player (actor 8, findInContext).

Entries: `enemy_14_15_officer_01` → 1; `jackie_transition_hide` → 29; `enemy_07_08` → 6; `jackie_transition_double_takedown` → 34; `enemy_06_05` → 13; `enemy_015_looking_for_013` → 41; `enemy_015_raising_alarm` → 42; `jackie_avoids_routine_007_008` → 17; `jackie_lab_cleared` → 25.

Exits: `jackie_lab_cleared_out` → 27; `enemy_14_15_officer_01_out` → 2; `jackie_transition_hide_out` → 31; `enemy_07_08_out` → 7; `jackie_transition_double_takedown_out` → 36; `enemy_06_05_out` → 14; `enemy_015_looking_for_013_out` → 43; `enemy_015_raising_alarm_out` → 44; `jackie_avoids_routine_007_008_out` → 18.

End nodes: 2: `<omitted>`; 7: `<omitted>`; 14: `<omitted>`; 18: `<omitted>`; 27: `<omitted>`; 31: `<omitted>`; 36: `<omitted>`; 43: `<omitted>`; 44: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 22 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9

Raw SHA-256: `31ddddd8a393c6d4f03f27060abf84fcf2a720842086ca1b22a7ca6a04c74451`. Binary SHA-256: `4ae71f7f32a9f100d3e46929b28b56014ed23ddec62f01ca69175fc6bc0742ef`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_04e_pre_combat_patrol_dialogues.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_05_transition.scene`

223 graph nodes, 273 edges; 36 event-bearing sections, 217 events; 58 screenplay lines, 11 screenplay options, 6 choice nodes.

Actors: Jackie (actor 0, spawnSet); transition_enemy_014_shotgun (actor 1, community); transition_enemy_officer_001_rifle (actor 2, community); transition_enemy_013_shotgun (actor 3, findInWorld); Brick (actor 4, spawnSet); Player (actor 5, findInContext).

Entries: `q003_05_convoy_signatures_in` → 398; `q003_05_brick_prison_in` → 404; `brick_dialogue_preview` → 1246; `detonator_interaction` → 1248; `q003_03_tranisition_chat_in` → 298; `linestoreuse` → 1089; `q003_05_attack_in` → 326; `q003_05_enter_garage_in` → 350; `q003_05_come_on_in` → 385; `q003_05_close_to_exit_in` → 390.

Exits: `q003_05_convoy_signatures_out` → 399; `q003_03_tranisition_chat_out` → 354; `q003_05_brick_prison_out` → 564; `q003_05_attack_out` → 378; `q003_05_enter_garage_out` → 382; `q003_05_come_on_out` → 386; `q003_05_close_to_exit_out` → 391.

End nodes: 354: `<omitted>`; 378: `<omitted>`; 382: `<omitted>`; 386: `<omitted>`; 391: `<omitted>`; 399: `<omitted>`; 564: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 917 / 838 | `/Data/RootChunk/sceneGraph/Data/graph/111/Data/events/6` |
| `scnChangeIdleAnimEvent` | 7 | 467 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/4` |
| `scnDialogLineEvent` | 48 | 297 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnGameplayTransitionEvent` | 10 | 695 / 484 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/15` |
| `scnIKEvent` | 20 | 695 / 463 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/1` |
| `scnLookAtEvent` | 24 | 349 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 35 | 297 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnUnmountEvent` | 10 | 695 / 483 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/14` |
| `scneventsAttachPropToPerformer` | 1 | 680 / 446 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/5` |
| `scneventsAttachPropToWorld` | 3 | 909 / 810 | `/Data/RootChunk/sceneGraph/Data/graph/110/Data/events/10` |
| `scneventsCameraParamsEvent` | 3 | 680 / 437 | `/Data/RootChunk/sceneGraph/Data/graph/69/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 10 | 695 / 479 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/11` |
| `scneventsSocket` | 45 | 417 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 7
- speech: 5
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment: 1

Raw SHA-256: `bff1751d1d36ee82a4b3814f4fc8e35ad8eca3ff07724354e376b5cde947e383`. Binary SHA-256: `12ba4227d328e7421078165cda86b58d7d558ed7be6bba8f2b5777578318d528`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_05_transition.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_06a_boss_combat.scene`

89 graph nodes, 85 edges; 27 event-bearing sections, 80 events; 31 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Shotgunner_Maelstrommer (actor 0, community); Jackie (actor 1, spawnSet); Royce (actor 2, spawnSet); Cable_Maelstrommer (actor 3, community); Player (actor 4, findInContext).

Entries: `q003_06a_royce_dead_in` → 356; `q003_06a_boss_scene_in` → 1; `linestoreuse` → 546; `q003_06a_entering_arena_in` → 552; `royce_hp_comments` → 112; `q003_06a_leave_garage_in` → 394; `q003_06a_leave_fence_in` → 399; `royce_first_beam_attack` → 165; `royce_first_projectile` → 166; `royce_shield_broken` → 167; `royce_player_too_close` → 168; `royce_after_close_beam_attack` → 169; `royce_player_dead` → 170; `jackie_weak_spot` → 171; `q003_05_jackie_car_throw_in` → 172.

Exits: `q003_06a_royce_dead_out` → 357; `q003_06a_entering_arena_out` → 553; `royce_hp_comments_out` → 114; `q003_06a_leave_garage_out` → 395; `q003_06a_leave_fence_out` → 400; `royce_first_beam_attack_end` → 233; `royce_first_projectile_end` → 236; `royce_shield_broken_end` → 239; `royce_player_too_close_end` → 242; `royce_after_close_beam_attack_end` → 245; `royce_player_dead_end` → 248; `jackie_weak_spot_end` → 251; `q003_06a_boss_scene_out` → 260; `q003_05_jackie_car_throw_out` → 351.

End nodes: 114: `<omitted>`; 233: `<omitted>`; 236: `<omitted>`; 239: `<omitted>`; 242: `<omitted>`; 245: `<omitted>`; 248: `<omitted>`; 251: `<omitted>`; 260: `NonTerminating`; 351: `<omitted>`; 357: `<omitted>`; 395: `<omitted>`; 400: `<omitted>`; 553: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 19 | 3 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scnChangeIdleAnimEvent` | 4 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnDialogLineEvent` | 30 | 3 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnLookAtEvent` | 1 | 3 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/10` |
| `scnPlaySkAnimEvent` | 5 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 5 | 3 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scneventsVFXEvent` | 16 | 3 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 23
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, vfx: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `e21746ff4bb28d51693dbe166ab758b15b8402830ea7828fa655609ff5f5eb7d`. Binary SHA-256: `3c7cff197b7ea03e8ca015e70038bebca98aa3f0948a249cf4a865117cb7d1b2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_06a_boss_combat.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_07_final.scene`

70 graph nodes, 78 edges; 12 event-bearing sections, 95 events; 24 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Jackie (actor 0, spawnSet); jackie_bike (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `q003_07_final_in` → 1; `jackie_ride_off` → 223.

Exits: `q003_07_final_out` → 2; `KillSignal` → 44.

End nodes: 2: `NonTerminating`; 44: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 51 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/5` |
| `scnChangeIdleAnimEvent` | 10 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnDialogLineEvent` | 21 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 75 / 221 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/8` |
| `scnIKEvent` | 2 | 75 / 213 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/1` |
| `scnLookAtEvent` | 5 | 51 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 51 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/7` |
| `scnPlaySkAnimEvent` | 20 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnUnmountEvent` | 1 | 75 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 9 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSocket` | 22 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 5
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1

Raw SHA-256: `755616970d0ef8b1bf28724b5c10aff476690327609d2301d6d2911e9c0801f2`. Binary SHA-256: `8f6343bde45977f09a5298e1534bbaf226008f1870e6c5870d6587d75e7cfaa8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_07_final.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_07a_final_corp.scene`

301 graph nodes, 351 edges; 41 event-bearing sections, 310 events; 80 screenplay lines, 12 screenplay options, 6 choice nodes.

Actors: Jackie (actor 0, spawnSet); Meredith (actor 1, spawnSet); Bodyguard_01 (actor 2, community); Bodyguard_02 (actor 3, community); suv (actor 4, community); militech_soldier1 (actor 5, community); militech_soldier2 (actor 6, community); militech_soldier3 (actor 7, community); militech_soldier4 (actor 8, community); militech_soldier5 (actor 9, community); militech_soldier6 (actor 10, community); militech_drone (actor 11, community); Johnny (actor 12, spawnSet); Meredith_holocall (actor 13, spawnSet); jackie_bike (actor 14, spawnSet); av1 (actor 15, community); av2 (actor 16, community); Player (actor 17, findInContext).

Entries: `q003_07a_finale_in` → 1; `q003_07a_drone_in` → 1495; `jackie_bye_preview` → 2708; `q003_07a_stout_corpse_in` → 2152; `q003_07a_stout_sex_end_in` → 2197; `q003_militech_pushback_in` → 2560; `Start 14` → 2869; `q003_07a_stout_holocall_in` → 2286; `meredith_holocall_preview` → 2606; `Start 15` → 2936.

Exits: `q003_07a_finale_out` → 4; `KillSignal` → 2091; `q003_07a_stout_corpse_out` → 2153; `q003_07a_stout_sex_end_out` → 2200; `q003_07a_drone_jackie_out` → 2024; `q003_07a_stout_runn_off_out` → 2321.

End nodes: 4: `NonTerminating`; 2024: `NonTerminating`; 2091: `<omitted>`; 2153: `<omitted>`; 2200: `<omitted>`; 2321: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 31 | 319 / 115 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnChangeIdleAnimEvent` | 24 | 116 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnDialogLineEvent` | 65 | 105 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 1977 / 550 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/17` |
| `scnIKEvent` | 10 | 1977 / 541 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/9` |
| `scnLookAtEvent` | 32 | 105 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 70 | 105 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 5 | 1977 / 549 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/16` |
| `scneventsAttachPropToPerformer` | 6 | 505 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 1977 / 545 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/13` |
| `scneventsSocket` | 45 | 105 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXDurationEvent` | 2 | 319 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |
| `scneventsVFXEvent` | 10 | 319 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 6
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation: 4
- speech: 4
- speech, idle_animation, gaze: 3
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 2
- skeletal_animation, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `ca0cc3b04c5c44a13cb79e0d12ff6679c2f41e3b8a5dae28cb48bd1c1e61ade3`. Binary SHA-256: `d3435d0eae2d629a19021d10eee06fd77998321ee629c0d1cd1c319c6eb460d5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_07a_final_corp.scene" --events
```

## `base\quest\main_quests\prologue\q003\scenes\q003_07aa_final_traitor.scene`

364 graph nodes, 417 edges; 50 event-bearing sections, 406 events; 92 screenplay lines, 11 screenplay options, 5 choice nodes.

Actors: Anthony (actor 0, spawnSet); Jackie (actor 1, spawnSet); bodyguard1 (actor 2, community); bodyguard2 (actor 3, community); soldier1 (actor 4, community); soldier2 (actor 5, community); soldier3 (actor 6, community); soldier4 (actor 7, community); soldier5 (actor 8, community); soldier6 (actor 9, community); Johnny (actor 10, spawnSet); soldier7 (actor 11, community); soldier8 (actor 12, community); soldier9 (actor 13, community); soldier10 (actor 14, community); Anthony_holocall (actor 15, spawnSet); drone (actor 16, community); jackie_bike (actor 17, spawnSet); av1 (actor 18, community); av2 (actor 19, community); q003_suv (actor 20, community); Player (actor 21, findInContext).

Entries: `q003_07_traitor_in` → 1; `av_arrival_preview` → 1503; `Start 5` → 1580; `q003_07aa_gilchrist_holocall_in` → 1025; `jackie_talk_preview` → 1346; `gilchrist_holocall_preview` → 1373; `q003_07aa_gilchrist_corpse_in` → 799.

Exits: `q003_07_traitor_out` → 2; `q003_soldier_pushback_out` → 1290; `q003_07a_gilchrist_runn_off_out` → 1039; `KillSignal` → 754; `q003_07aa_gilchrist_corpse_out` → 800.

End nodes: 2: `NonTerminating`; 754: `<omitted>`; 800: `<omitted>`; 1039: `NonTerminating`; 1290: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 431 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/4` |
| `scnChangeIdleAnimEvent` | 17 | 3 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 69 | 3 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnGameplayActionEvent` | 2 | 1623 / 1978 | `/Data/RootChunk/sceneGraph/Data/graph/256/Data/events/2` |
| `scnGameplayTransitionEvent` | 7 | 381 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/9` |
| `scnIKEvent` | 14 | 381 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnLookAtAdvancedEvent` | 10 | 925 / 740 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/15` |
| `scnLookAtEvent` | 56 | 3 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 82 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 7 | 381 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |
| `scneventsAttachPropToPerformer` | 6 | 433 / 145 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 7 | 381 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scneventsSocket` | 111 | 3 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 6 | 431 / 130 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation: 2
- speech, gaze: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- idle_animation, gaze, socket_signal, gameplay_action: 1

Raw SHA-256: `489e8d61e95f85997d1be85ea1a0953b16746482c7b3f8e4b5aa2140ec6e2a12`. Binary SHA-256: `b7ebbe3e1c42af9b1ff0f9d08763973487101517857c130e6724add32000c79b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q003\scenes\q003_07aa_final_traitor.scene" --events
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

## `base\quest\minor_quests\mq048\scenes\mq048_01_hook.scene`

24 graph nodes, 26 edges; 7 event-bearing sections, 23 events; 12 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Victor_holo (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 137.

End nodes: 2: `<omitted>`; 137: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 22 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnDialogLineEvent` | 12 | 22 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnPlaySkAnimEvent` | 6 | 26 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 3
- speech, idle_animation: 2
- speech, skeletal_animation, idle_animation: 2

Raw SHA-256: `b1c2c2518de3f1ca9d4152ce90614f5584df91ffa29fff44dc89319e244fcf54`. Binary SHA-256: `dbf0fdc2c6c7e71034b5e8640be64c4cd6d9abc0203954f46bb4d622a6151674`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq048\scenes\mq048_01_hook.scene" --events
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

