# Cyberpsycho Sighting: Six Feet Under: scene presentation

Journal identity: `quests/minor_quest/ma_wat_nid_22`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_wat_nid_22.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\watson\northside\ma_wat_nid_22\scenes\ma_wat_nid_22_clues.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `brief_call` → 36.

Exits: `rejected_out` → 255; `brief_call_end` → 38.

End nodes: 38: `<omitted>`; 255: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 37 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `40497323d38f97cac49075f2d3e0d3a003e0854eaf7302795cdec02bb6b45d3f`. Binary SHA-256: `820770e82736a73a0e933df8fcc1b378df101e9e1c0fbace29a3fb9fe63db64f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\northside\ma_wat_nid_22\scenes\ma_wat_nid_22_clues.scene" --events
```

