# Cyberpsycho Sighting: Smoke on the Water: scene presentation

Journal identity: `quests/minor_quest/ma_pac_cvi_08`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_pac_cvi_08.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\scenes\ma_pac_cvi_08_01_briefing.scene`

39 graph nodes, 44 edges; 2 event-bearing sections, 5 events; 5 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); johnny (actor 1, spawnDespawn); hidden02 (actor 2, community); Player (actor 3, findInContext).

Entries: `Start 0` → 1; `johnny_in` → 51.

Exits: `End 0` → 2; `rejected_out` → 277.

End nodes: 2: `<omitted>`; 277: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 25 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `4a75b34249eb87b31fc7fd71a8eba555bf19693cd1fd2f0bfdc628bbc6bbc0a0`. Binary SHA-256: `371cabe9b6e65f57a05a85302481b94761c82c3f97c2544a95f59fdf23afea3a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\scenes\ma_pac_cvi_08_01_briefing.scene" --events
```

