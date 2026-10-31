# Suspected Organized Crime Activity: Wipe the Gonk, Take the Implants: scene presentation

Journal identity: `quests/minor_activities/pacifica/coastview/ma_pac_cvi_12`. Stored type: **Contract**. Attribution: **POI-linked; quest activation unresolved**.

[Full quest flow dossier](../../all-quests/base-ma_pac_cvi_12.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\scenes\ma_pac_cvi_12_holocall_brief.scene`

15 graph nodes, 14 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: police_dispatcher (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 33 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `e73bdbd61edf86ad352acab66281d344bfe098336bede5db5180f426fa5166ea`. Binary SHA-256: `2ad8a676c2a0f388b7cfe264f967f4179c39c8bf8f6739f7d54e18b594e1210d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_12\scenes\ma_pac_cvi_12_holocall_brief.scene" --events
```

