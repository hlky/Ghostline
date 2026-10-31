# Gig: Race to the Top: scene presentation

Journal identity: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_03`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_std_arr_03.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_debriefs.scene`

25 graph nodes, 30 edges; 1 event-bearing sections, 2 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `debrief_perfect` → 1; `debrief_optional_failed_afterwards` → 64; `debrief_no_optional` → 35.

Exits: `debrief_perfect_end` → 2; `rejected_out` → 285.

End nodes: 2: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 18 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `5f74a5366ffaa828a3b6ece84bf4e9e257593e60b2a0b7a8f1321bb18de9bac7`. Binary SHA-256: `bb5b58ed66fbcb9c1172665643359a6c2623b50042ddb0e2133340a7053afc92`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `4ceacdb3a498c2beb2b775116e5528de7f11af52a78a7a076d6cdd0d4bb70217`. Binary SHA-256: `f63b0043d4e5d2d3fabc3dd98cf200384376eed026f87fc4cc40e0a57655421e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_03\scenes\sts_std_arr_03_holocall_prebrief.scene" --events
```

