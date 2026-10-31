# Suspected Organized Crime Activity: Just Say No: scene presentation

Journal identity: `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_02`. Stored type: **Contract**. Attribution: **POI-linked; quest activation unresolved**.

[Full quest flow dossier](../../all-quests/base-ma_wat_nid_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_holocall_brief.scene`

15 graph nodes, 14 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: ncpd_dispatcher (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `4037b7f133e9c42be0ad7027107a286c38c20d1f56b45cca55e08308306e3297`. Binary SHA-256: `eb7b7f0f5753a5c9018c559cf18f192cdf38ebc908797389ec1ab717b1834347`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_holocall_brief.scene" --events
```

