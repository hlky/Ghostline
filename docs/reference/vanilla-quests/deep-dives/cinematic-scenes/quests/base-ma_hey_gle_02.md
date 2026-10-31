# Suspected Organized Crime Activity: Chapel: scene presentation

Journal identity: `quests/minor_activities/heywood/glen/ma_hey_gle_02`. Stored type: **Contract**. Attribution: **POI-linked; quest activation unresolved**.

[Full quest flow dossier](../../all-quests/base-ma_hey_gle_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene`

15 graph nodes, 14 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: NCPD_dispatcher (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 32 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `c7098a58777d0b44dea753d1ea6b47ed89deb446d16b45e417b5a8ca93dad0eb`. Binary SHA-256: `5d1fe722d3efe36ccb9a0aa02f0f8ea40fc6e6e24a55c2dc935a6bab7d4b5b27`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene" --events
```

