# Cyberpsycho Sighting: The Wasteland: scene presentation

Journal identity: `quests/minor_quest/ma_bls_ina_se1_07`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_bls_ina_se1_07.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene`

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

Raw SHA-256: `d43834035830e2c0025714f38f9e32afeca3802bb2a3673989c68f13afd0d9ae`. Binary SHA-256: `0f24d576f44520d85a99d6e13ef8c0cfb19d912fa9e9ca0dc1fda5c2ae6746bb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_07\scenes\ma_bls_ina_se1_07_brief.scene" --events
```

