# Cyberpsycho Sighting: Under the Bridge: scene presentation

Journal identity: `quests/minor_quest/ma_std_arr_06`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_std_arr_06.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `brief_call` → 4.

Exits: `brief_call_end` → 6; `rejected_out` → 255.

End nodes: 6: `<omitted>`; 255: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 5 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `9e83d0dab855d709b81ea1daffc8f66fe4481e092e499b80a8c1697026452170`. Binary SHA-256: `5729b252e4112144397d9949b35a190baf29eafd17eedebc74b6087da6e62a71`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_06\scenes\ma_std_arr_06_briefing.scene" --events
```

