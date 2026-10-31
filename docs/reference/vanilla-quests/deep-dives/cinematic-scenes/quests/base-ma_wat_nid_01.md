# Suspected Organized Crime Activity: Vice Control: scene presentation

Journal identity: `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_01`. Stored type: **Contract**. Attribution: **POI-linked; quest activation unresolved**.

[Full quest flow dossier](../../all-quests/base-ma_wat_nid_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\watson\northside\ma_wat_nid_01\scenes\ma_wat_nid_01_holocall_brief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: ncpd_dispatcher (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `e23da7da5a2d96fd7a18a0a26864eb685390c035679db01d423c79ba793f5c0b`. Binary SHA-256: `7806922cbc45a1a2be7c532bcb338991aafd6ec092150a8822fe47941e1e5c9c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\northside\ma_wat_nid_01\scenes\ma_wat_nid_01_holocall_brief.scene" --events
```

