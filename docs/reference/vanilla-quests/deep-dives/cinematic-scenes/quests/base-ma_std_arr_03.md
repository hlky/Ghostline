# NO_TITLE: scene presentation

Journal identity: `quests/minor_activities/santo_domingo/arroyo/ma_std_arr_03`. Stored type: **Contract**. Attribution: **POI-linked; quest activation unresolved**.

[Full quest flow dossier](../../all-quests/base-ma_std_arr_03.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene`

15 graph nodes, 14 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: NCPD_dispatcher (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 29 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `e6dec3375626b2c4ae83f1cc31cf3a552818be3739639bc8ac59d9f5dae77d02`. Binary SHA-256: `8399c974d762b15ceeedaa578f6064a44bff607cf61ceb37bc233864093be8fc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_03\scenes\ma_std_arr_03_holocall_brief.scene" --events
```

