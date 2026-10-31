# Gig: On a Tight Leash: scene presentation

Journal identity: `quests/street_stories/heywood/wellsprings/sts_hey_spr_01`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_hey_spr_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_01\scenes\sts_hey_spr_01_chats.scene`

25 graph nodes, 35 edges; 5 event-bearing sections, 28 events; 27 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: enemy_007_patroling (actor 0, community); enemy_008_repairing (actor 1, community); enemy_004_chilling (actor 2, community); enemy_005_searching (actor 3, community); enemy_012_grill (actor 4, community); enemy_010_phone (actor 5, community).

Entries: `spr_01_phone_talk_start` → 25; `spr_01_entrance_talk_start` → 1; `sts_hey_spr_01_mili_car_start` → 29; `sts_hey_spr_01_start` → 34; `Start 2` → 18.

Exits: `spr_01_phone_talk_end` → 27; `spr_01_entrance_talk_end` → 2; `sts_hey_spr_01_mili_car_end` → 30; `sts_hey_spr_01_end` → 35; `End 2` → 19.

End nodes: 2: `NonTerminating`; 19: `NonTerminating`; 27: `NonTerminating`; 30: `NonTerminating`; 35: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 27 | 8 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 1 | 22 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, skeletal_animation: 1

Raw SHA-256: `9d02ae7470a9d4c9d7660b08aeffa382147a263e95b183f8865a6915a26879a3`. Binary SHA-256: `d8b3bf0a0b74fac1da54ac053e0734ac287886bfa9241fec21c2f1187f85a9a8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_01\scenes\sts_hey_spr_01_chats.scene" --events
```

## `base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_01\scenes\sts_hey_spr_01_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: padre (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 25 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `94102c25fe1b0e7f70f94679ee247706ad7e604c9195b95a5babea34d3d39313`. Binary SHA-256: `b363dbb3e7763b4f4856cf5736b8ee89955a8243d48b1dcecffd67362d094ec2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_01\scenes\sts_hey_spr_01_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_01\scenes\sts_hey_spr_01_johnny_clues.scene`

35 graph nodes, 41 edges; 3 event-bearing sections, 11 events; 11 screenplay lines, 4 screenplay options, 4 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `sts_hey_spr_01_truck_001_start` → 9.

Exits: `sts_hey_spr_01_truck_end` → 10; `sts_hey_spr_01_suits_end` → 15.

End nodes: 10: `<omitted>`; 15: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 11 | 6 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `eda3c54d8c2790d0d23adc8dc84c7280e27291ea3c03324e1794c7ea9416ba39`. Binary SHA-256: `469b9034d002a433544ba1ce42084884e8462c08588246de05dafcdce91c5bba`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_01\scenes\sts_hey_spr_01_johnny_clues.scene" --events
```

## `base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_01\scenes\sts_hey_spr_01_jose.scene`

9 graph nodes, 10 edges; 2 event-bearing sections, 13 events; 12 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: jose (actor 0, findInWorld); corpo (actor 1, spawner); Player (actor 2, findInContext).

Entries: `sts_hey_spr_01_interruped_start` → 63; `sts_hey_spr_01_corpo_start` → 48.

Exits: `sts_hey_spr_01_interruped_end` → 64; `sts_hey_spr_01_corpo_end` → 49.

End nodes: 49: `<omitted>`; 64: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 12 | 61 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 1 | 67 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1
- speech, skeletal_animation: 1

Raw SHA-256: `5792a210c0eb860a69b55167c5b2663a04dbf1ce609777cbe73d02467d283e62`. Binary SHA-256: `622f79f75a6e9eb28700bcf8ee018c9493a7e54bd624d27d409f1e30b9cde781`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_01\scenes\sts_hey_spr_01_jose.scene" --events
```

## `base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_01\scenes\sts_hey_spr_01_padre_fixer_conversation.scene`

46 graph nodes, 58 edges; 13 event-bearing sections, 38 events; 38 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: padre (actor 0, spawnSet); jose (actor 1, community); Player (actor 2, findInContext).

Entries: `spr_01_padre_start` → 10.

Exits: `End2` → 297; `End1` → 257.

End nodes: 257: `<omitted>`; 297: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 38 | 147 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13

Raw SHA-256: `9049db30b66f7d9171932e2a32da90e3936c9122b4df8dcf0a91f5cc20c2a4c4`. Binary SHA-256: `406be1e98c668651c6535b06a7f585f9b6119755d128685143fc727f8788da97`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_01\scenes\sts_hey_spr_01_padre_fixer_conversation.scene" --events
```

