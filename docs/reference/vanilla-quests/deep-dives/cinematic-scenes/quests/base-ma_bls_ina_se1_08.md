# Cyberpsycho Sighting: House on a Hill: scene presentation

Journal identity: `quests/minor_quest/ma_bls_ina_se1_08`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_bls_ina_se1_08.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `ma_bls_ina_se1_08_brief_in` → 1.

Exits: `ma_bls_ina_se1_08_brief_out` → 2; `rejected_out` → 399.

End nodes: 2: `<omitted>`; 399: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `d5a942d828e09a443bb75550fda8da901f1a60d0eef387579555267cc9905a77`. Binary SHA-256: `f38b218bef2ffb86873d0cd03810b26acdc16bfbae59db595eb5651afc951ac1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_08\scenes\ma_bls_ina_se1_08_holocall.scene" --events
```

