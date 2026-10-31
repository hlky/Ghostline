# Cyberpsycho Sighting: Letter of the Law: scene presentation

Journal identity: `quests/minor_quest/ma_hey_spr_06`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_hey_spr_06.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\scenes\ma_hey_spr_06_brief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `ma_hey_spr_06_brief_in` → 1.

Exits: `ma_hey_spr_06_brief_out` → 2; `rejected_out` → 399.

End nodes: 2: `<omitted>`; 399: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `45cd33033d99eee44ce599e13fe494e6923764748075f288ecb2a929e744dc78`. Binary SHA-256: `b62d13ae42424857ccd18e32ed7a34c1e35c3827c15d5d73ad1c49608c73e977`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\scenes\ma_hey_spr_06_brief.scene" --events
```

