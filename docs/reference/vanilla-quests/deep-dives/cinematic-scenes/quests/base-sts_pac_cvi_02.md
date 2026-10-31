# Gig: Two Wrongs Makes Us Right: scene presentation

Journal identity: `quests/street_stories/pacifica/coastview/sts_pac_cvi_02`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_pac_cvi_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_gangers.scene`

8 graph nodes, 8 edges; 2 event-bearing sections, 8 events; 8 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: ganger_001 (actor 0, community); ganger_003 (actor 1, community); ganger_012 (actor 2, community); Player (actor 3, findInContext).

Entries: `cvi_02_star_talk_002` → 48; `cvi_02_star_talk_001` → 9.

Exits: `cvi_02_end_talk_001` → 2; `cvi_02_end_talk_002` → 47.

End nodes: 2: `<omitted>`; 47: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 8 | 13 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `b7460c6ce2615368c8167f12900b4db05a1645fc1e5dde4a5748acb95a2a2e78`. Binary SHA-256: `c491fd8a2be24ce9e7ce76542de221565c283eeb3921dc639c368eee75ae1346`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_gangers.scene" --events
```

## `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene`

46 graph nodes, 60 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `debrief_perfect` → 1; `debrief_failed` → 35.

Exits: `debrief_perfect_end` → 2; `rejected_failed_out` → 380; `debrief_failed_end` → 36; `rejected_perfect_out` → 367.

End nodes: 2: `<omitted>`; 36: `<omitted>`; 367: `<omitted>`; 380: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 17 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `63959c2c5f4cb0b4509a6a42a106d83c9aec2f9890f48bf18bdaab0e8d8c3ae7`. Binary SHA-256: `e4f11222550f4c9e81141ba1d31c8c614321cc9fe1cf1b7112c10f4008da13eb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 285.

End nodes: 2: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `bee633a4456e106417d38b9cbe5137b3de8a2ced5afe65ba6795343a75ce7530`. Binary SHA-256: `87b8e206fd98d5ad2b4e98fcee1607369894f1ed665dd60b44ff824b83b8b83c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_johnny.scene`

8 graph nodes, 7 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `cvi_02_talk_johnny_start_001` → 1.

Exits: `cvi_02_talk_johnny_end_001` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `d3e3cc7e73e113a7aa73caeda9e0417c370d1af12f84f763015b17dae16183e2`. Binary SHA-256: `46bb6fd3314d536f41563fa4e46c4be862e81350d753a92328c685e82b2438d1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_johnny.scene" --events
```

## `ep1\openworld\fixers\mr_hands\scenes\mr_hands_combat_zone_introduction.scene`

18 graph nodes, 20 edges; 6 event-bearing sections, 18 events; 18 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: mr_hands (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 18 | 16 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6

Raw SHA-256: `d95478acc7e75b29a7327a98e880d7df459c453ce845afd004a5e692f8ed87ce`. Binary SHA-256: `4648c2c589390d5587d7e4e44540cea3f0497967b07570464a88d8cf0765f69a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\fixers\mr_hands\scenes\mr_hands_combat_zone_introduction.scene" --events
```

