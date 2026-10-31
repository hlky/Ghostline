# Gig: Shark in the Water: scene presentation

Journal identity: `quests/street_stories/watson/kabuki/sts_wat_kab_06`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_kab_06.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_halocall_debrief.scene`

25 graph nodes, 33 edges; 2 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start1` → 66.

Exits: `rejected_out` → 290; `End1` → 67.

End nodes: 67: `<omitted>`; 290: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `c371de795e984a1f3a417794333f11c9ac7d0a30a485648274758294813c1c3e`. Binary SHA-256: `ffe16a888c61a86efa3c5eb0a24648a6d5356b16a0b07edf67dcaca25cd4ad8c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_halocall_debrief.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 76 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `f54bc87ee61a40c428c1aed7bb0a10c2a135cb1c1ddb891d069a3fa240f881b5`. Binary SHA-256: `280fb97e0eb8aa5bc2dc8c6fada00a94c9aa1965430e0f7dac554eca6c42375a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_scene.scene`

9 graph nodes, 6 edges; 3 event-bearing sections, 17 events; 17 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: kab_06_animals_front_01 (actor 0, findInWorld); kab_06_animals_truck (actor 1, community); kab_06_animals_patrol (actor 2, community); kab_06_animals_standing (actor 3, community); kab_06_Blake (actor 4, community); player (actor 5, findInContext).

Entries: `kab_06_maelstrom_phoen_call_start` → 126; `kab_06_animals_joking_start` → 176; `kab_06_maelstrom_talking_001_start` → 68.

Exits: `kab_06_maelstrom_phoen_call_end` → 127; `kab_06_maelstrom_talking_001_end` → 69; `kab_06_animals_joking_end` → 178.

End nodes: 69: `<omitted>`; 127: `<omitted>`; 178: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 17 | 67 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `f7b65b02ed3e9c4c43e32f947661a963914f0a1fd611b90b2a5589086686ca3d`. Binary SHA-256: `0b7ba33b509e0d994cb54b57d144ce921bfa6532b47c9f39ecbfa6108d201b03`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_scene.scene" --events
```

