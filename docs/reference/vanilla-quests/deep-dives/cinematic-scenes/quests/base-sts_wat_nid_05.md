# Gig: Rite of Passage: scene presentation

Journal identity: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_05`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_nid_05.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 1 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 285.

End nodes: 2: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `428a13e3c9425763facdbba595427bbfb1c35c541d036d3f46baffd2ad38134d`. Binary SHA-256: `d58b02e125ceb2824d062bdaf8250a6cdc101bf98b2bd80a4c6a717beb4f75d0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_debrief.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 25 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `6bd151595c5bf7e29124a990c348b4c2f7a4e5ac9a87356302a839e9ec7053bc`. Binary SHA-256: `dde8374005e816b16b5bb032b855a72a447fb7cfe4bf9e490ca26d63eef0b0cc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_scene.scene`

21 graph nodes, 26 edges; 4 event-bearing sections, 16 events; 21 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Enemy4 (actor 0, community); Enemy6 (actor 1, community); Enemy7 (actor 2, community); Enemy8 (actor 3, community); Enemy3 (actor 4, community); V (actor 5, findInContext).

Entries: `nid_05_bottom_dialogue_start` → 77; `nid_05_top_floor_dialogue_start` → 22; `nid_05_smoke_reaction_1_start` → 263.

Exits: `nid_05_smoke_reaction_1_end` → 264; `nid_05_top_floor_dialogue_end` → 24; `nid_05_bottom_dialogue_end` → 80.

End nodes: 24: `<omitted>`; 80: `<omitted>`; 264: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 16 | 21 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `2cc49150be32d36034362c984f827f976fd0261a487c0d4ecd2d83b484265210`. Binary SHA-256: `00b35f8433449d439d5bee954f796a58d9a091261948b55416ea03064a2f8d82`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_05\scenes\sts_wat_nid_05_scene.scene" --events
```

