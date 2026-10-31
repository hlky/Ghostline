# Suspected Organized Crime Activity: No License, No Problem: scene presentation

Journal identity: `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_06`. Stored type: **Contract**. Attribution: **POI-linked; quest activation unresolved**.

[Full quest flow dossier](../../all-quests/base-ma_wat_nid_06.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\watson\northside\ma_wat_nid_06\scenes\ma_wat_nid_06_holocall_brief.scene`

15 graph nodes, 14 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

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

Raw SHA-256: `8b52babcf522c7c9f7d11b7e447f1644f54fe3174dbb7d1fe92ceae23a68be37`. Binary SHA-256: `6de8acf1da38fed5f324defa04bc4428c3e9ded31ca0bbd1182c342a010a988c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\northside\ma_wat_nid_06\scenes\ma_wat_nid_06_holocall_brief.scene" --events
```

