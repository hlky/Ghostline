# Gig: Many Ways to Skin a Cat: scene presentation

Journal identity: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_nid_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_debriefs.scene`

26 graph nodes, 34 edges; 2 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `rejected_out` → 286; `End 0` → 2.

End nodes: 2: `<omitted>`; 286: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 30 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `241db45a49e349438c92e625e20d9bdb4a244b1fbeee1e044b55dec0d8dde982`. Binary SHA-256: `0a41a20a9da81069c9bc26128aad5ab772042c0570e177736ccf24ea5164127c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 27 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `443330cff0341618afdbb3445349af2a395bb2a996c131a79ad1f2eb05fa11ab`. Binary SHA-256: `b5d7bd67ef9fd5f6f267693826987a011e4b3d61a23ad59fb5da6d200709c5e9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_prebrief.scene" --events
```

