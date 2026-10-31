# LocKey39425: scene presentation

Journal identity: `quests/minor_activities/pacifica/west_wind_estate/ma_pac_wwd_02`. Stored type: **Contract**. Attribution: **POI-linked; quest activation unresolved**.

[Full quest flow dossier](../../all-quests/base-ma_pac_wwd_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\scene\ma_pac_wwd_02_holocall_brief.scene`

15 graph nodes, 14 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: NCPD_dispatcher (actor 0, spawnSet).

Entries: `Start1` → 4.

Exits: `rejected_out` → 260; `End1` → 5.

End nodes: 5: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 18 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `70e4b94e21e40061467afa8c3d809fd733a1d5ce82598569a1bb68e19edf0c91`. Binary SHA-256: `680263c2f6bbb193ace7ff2c27b5f41c91234501fd906ceaaa9751db98ec4a94`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\scene\ma_pac_wwd_02_holocall_brief.scene" --events
```

