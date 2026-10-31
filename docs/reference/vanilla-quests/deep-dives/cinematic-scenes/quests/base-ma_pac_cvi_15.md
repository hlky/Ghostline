# Cyberpsycho Sighting: Lex Talionis: scene presentation

Journal identity: `quests/minor_quest/ma_pac_cvi_15`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_pac_cvi_15.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `ma_pac_cvi_15_brief_in` → 1.

Exits: `ma_pac_cvi_15_brief_out` → 2; `rejected_out` → 399.

End nodes: 2: `<omitted>`; 399: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `5de5398c0fe58e5ac6b3e34793471d194ce0a8573e7916b228ee233aaa137dad`. Binary SHA-256: `da8426a39a5f9b31177b28e902e2e85dd5beae5b531fb886512c24d8a9e01b2d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene" --events
```

