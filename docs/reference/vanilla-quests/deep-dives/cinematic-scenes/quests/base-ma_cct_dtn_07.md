# Cyberpsycho Sighting: Phantom of Night City: scene presentation

Journal identity: `quests/minor_quest/ma_cct_dtn_07`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_cct_dtn_07.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\scene\ma_cct_dtn_07_brief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `ma_cct_dtn_07_brief_in` → 1.

Exits: `ma_cct_dtn_07_brief_out` → 2; `rejected_out` → 399.

End nodes: 2: `<omitted>`; 399: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `abc98acf2f782ad3069a9feb847f967e1005e3baa28cfce9169e2f17eba0c82b`. Binary SHA-256: `90e24235ca307241a72534bebe0300c8729be93a26eecb46e5e74f26a457dc84`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_07\scene\ma_cct_dtn_07_brief.scene" --events
```

