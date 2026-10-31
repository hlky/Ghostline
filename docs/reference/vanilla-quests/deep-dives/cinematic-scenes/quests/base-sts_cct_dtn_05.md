# Gig: The Frolics of Councilwoman Cole: scene presentation

Journal identity: `quests/street_stories/city_center/downtown/sts_cct_dtn_05`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_cct_dtn_05.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_guards.scene`

6 graph nodes, 4 edges; 2 event-bearing sections, 6 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: guard_003 (actor 0, community); guard_005 (actor 1, community); guard_006 (actor 2, community).

Entries: `dtn_05_chat_001_start` → 1; `dtn_05_chat_002_start` → 2.

Exits: `dtn_05_chat_001_end` → 3; `dtn_05_chat_002_end` → 41.

End nodes: 3: `<omitted>`; 41: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 3. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `aa3a9298ee524c870e238ef90234f1a1c114348e1e1bb6deb459e65a337aa97b`. Binary SHA-256: `724c9dd49de0e3ac378dcbed9564103050de9b8fe55d45a6c2814527655857d7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_guards.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene`

25 graph nodes, 33 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); player (actor 1, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 288.

End nodes: 2: `<omitted>`; 288: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `b8f188766b2db708ecc08a7637fa06aaeecdb22657de455cdcd17ceea1c55475`. Binary SHA-256: `cb9af938cab9912eb5ddc19465be99d58cb36a4d30aa60951118a7b7e6459b1d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `093bfd5fd7f74941d090cea506246ee776a438c94cca65411d086ba01f6e8b22`. Binary SHA-256: `46adf903033b0b03b6abc312604b47a15865e46077a9b22394521d51a1a4c810`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_johnny.scene`

6 graph nodes, 5 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `946dcc3634b8ce0f90afd9e97100c76e4dd11951412eb455f6aef31811545da1`. Binary SHA-256: `f4512fb62cec79306146f26679f11d7e981e048d0584c010f2ddbed29f7bf0ec`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_05\scenes\sts_cct_dtn_05_johnny.scene" --events
```

