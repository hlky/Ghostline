# Gig: Until Death Do Us Part: scene presentation

Journal identity: `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wbr_hil_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_chats.scene`

8 graph nodes, 8 edges; 2 event-bearing sections, 19 events; 11 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: civilian_001 (actor 0, findInWorld); civilian_002 (actor 1, findInWorld); civilian_003 (actor 2, findInWorld); civilian_004 (actor 3, findInWorld).

Entries: `hil_01_civlians_chat_001_start` → 4; `hil_01_civlians_chat_002_start` → 6.

Exits: `hil_01_civlians_chat_001_end` → 5; `hil_01_civlians_chat_002_end` → 7.

End nodes: 5: `<omitted>`; 7: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 11 | 8 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnLookAtEvent` | 8 | 8 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 2

Raw SHA-256: `1462604585cd859df1a9d363a68b7b32f2c2845fc131760e367c2015bda8b1b2`. Binary SHA-256: `b49c4143d697afe82799b7099bd26d012649fe5eceda580104d5d0805cae5ab8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_chats.scene" --events
```

## `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene`

28 graph nodes, 38 edges; 2 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Wakako (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `optional` → 2; `rejected_out` → 286; `non_optional` → 76.

End nodes: 2: `<omitted>`; 76: `<omitted>`; 286: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `455b3c1024acea9d7155414f5a3f2824464cf6f00ac3083cfc23a4a19962bf41`. Binary SHA-256: `da214feecd620eca72fe1b922b5a3f4504a383535ad0eebc3eb5dbdeb2713dda`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Wakako (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `4a4768a586d5004cf269edbcfcc7182381170b8be123c714fae6d0de25079404`. Binary SHA-256: `e52f468092a857689abca1477cce06be8cd72ed32ab88d6f467b553c40d3eb1a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_01\scenes\sts_wbr_hil_01_holocall_prebrief.scene" --events
```

