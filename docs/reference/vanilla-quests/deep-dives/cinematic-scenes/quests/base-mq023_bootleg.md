# The Ballad of Buck Ravers: scene presentation

Journal identity: `quests/minor_quest/mq023_bootleg`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq023_bootleg.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

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

## `base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene`

41 graph nodes, 43 edges; 12 event-bearing sections, 105 events; 31 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: johnny (actor 0, spawnDespawn); performer (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `interrupt_in` → 83.

Exits: `End 0` → 2; `interrupt_out` → 85; `mq023_johnny_out` → 218.

End nodes: 2: `NonTerminating`; 85: `NonTerminating`; 218: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 26 | 11 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnDialogLineEvent` | 30 | 11 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnLookAtEvent` | 18 | 11 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 20 | 11 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsSocket` | 9 | 11 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsVFXEvent` | 2 | 225 / 309 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze: 4
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech: 1
- skeletal_animation, gaze, vfx, socket_signal: 1

Raw SHA-256: `fb943e8a5c6d2b4de9b9bc2f7dd973bbf5db4db7f152d3e20ceb6af52752ac49`. Binary SHA-256: `23d3a608acb36e7fb29121107e27b485c8d00860c5434101297d012befeb69a7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq023\scenes\mq023_01_johnny.scene" --events
```

## `base\quest\minor_quests\mq023\scenes\mq023_02_dinner.scene`

48 graph nodes, 54 edges; 9 event-bearing sections, 79 events; 24 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: johnny (actor 0, spawnDespawn); waiter (actor 1, spawnSet); Karim (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `content_token_control` → 113.

End nodes: 2: `<omitted>`; 113: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 23 | 5 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 21 | 5 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 15 | 5 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 3 | 151 / 243 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/1` |
| `scnPlaySkAnimEvent` | 13 | 5 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSocket` | 4 | 5 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/16` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 4
- skeletal_animation, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1

Raw SHA-256: `01853fb21c7054a3f9fe11a690c04023585b1f3f2cec196b9dd771a6abfe9edf`. Binary SHA-256: `9146aa6853d311cf015650969465bdee4d0e7fb312834cd2d08318386b92c3d4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq023\scenes\mq023_02_dinner.scene" --events
```

## `base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene`

221 graph nodes, 268 edges; 48 event-bearing sections, 336 events; 101 screenplay lines, 21 screenplay options, 11 choice nodes.

Actors: johnny (actor 0, spawnDespawn); karim (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `ow_vendor_in` → 1116; `cinedebug_start` → 772.

Exits: `End 0` → 2; `karim_content_manager_start` → 430.

End nodes: 2: `NonTerminating`; 430: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 83 | 7 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 81 | 7 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 28 | 7 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnOverridePhantomParamsEvent` | 2 | 443 / 686 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/1` |
| `scnPlaySkAnimEvent` | 99 | 7 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsEquipItemToPerformer` | 1 | 920 / 1162 | `/Data/RootChunk/sceneGraph/Data/graph/159/Data/events/5` |
| `scneventsSocket` | 40 | 23 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scneventsVFXEvent` | 2 | 920 / 1163 | `/Data/RootChunk/sceneGraph/Data/graph/159/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 9
- speech: 6
- skeletal_animation: 6
- speech, skeletal_animation, idle_animation, gaze: 5
- socket_signal: 5
- speech, skeletal_animation, idle_animation: 4
- skeletal_animation, idle_animation, gaze: 3
- speech, idle_animation: 2
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal, animation_state: 1
- vfx: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `5c07d7b98c7f485b7a70a0c96118282a429a49a98d268efb6ace84ebf60dcdb9`. Binary SHA-256: `e8e30658ac739fdbd4d796ffd3dbb0a04082e1cc2882a59656e500191d3d072b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq023\scenes\mq023_03_street_vendor.scene" --events
```

