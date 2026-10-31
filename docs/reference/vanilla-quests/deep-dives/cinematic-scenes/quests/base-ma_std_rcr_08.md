# LocKey39438: scene presentation

Journal identity: `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_08`. Stored type: **Contract**. Attribution: **POI-linked; quest activation unresolved**.

[Full quest flow dossier](../../all-quests/base-ma_std_rcr_08.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\scenes\ma_std_rcr_08_holocall_brief.scene`

15 graph nodes, 14 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: NCPD_dispatcher (actor 0, spawnSet).

Entries: `Start 0` → 44.

Exits: `End 0` → 45; `rejected_out` → 260.

End nodes: 45: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 47 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `12755c04bcfcb6d9a104dd8605b2c465ef340a0e23c6ec29fb76a1bdba566d23`. Binary SHA-256: `9a5eb0ad64c7a3d411a42b8bf9347519ccf9664a5dec6cddc0905cd665c8046a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_08\scenes\ma_std_rcr_08_holocall_brief.scene" --events
```

