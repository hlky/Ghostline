# Gig: The Lord Giveth and Taketh Away: scene presentation

Journal identity: `quests/street_stories/heywood/wellsprings/sts_hey_spr_03`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_hey_spr_03.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_03\scene\sts_hey_spr_03_holocall_debriefs.scene`

28 graph nodes, 37 edges; 3 event-bearing sections, 5 events; 5 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `Start1` → 99.

Exits: `rejected_out` → 280; `End1` → 100.

End nodes: 100: `<omitted>`; 280: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `c232312b8d8c178a74a50d3d005d7b1303cc1a42d7e31252d03947f7e3f99463`. Binary SHA-256: `934c1ffe0f0919ab363043e3f623c91ee88404f8445d7e2623388b1c4395c175`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_03\scene\sts_hey_spr_03_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_03\scene\sts_hey_spr_03_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); player (actor 1, findInContext).

Entries: `Start1` → 87.

Exits: `End1` → 88; `rejected_out` → 254.

End nodes: 88: `<omitted>`; 254: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `5ac861ef385244b9850f23d41745aaeb3ff7ce0194f65502f7732ea7e45c701f`. Binary SHA-256: `371cbd0c17bad8243747c14921d687f0c8592f1b47bd99805c12d5f7d6e8e032`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_03\scene\sts_hey_spr_03_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_03\scene\sts_hey_spr_03_nomad_chat.scene`

8 graph nodes, 10 edges; 4 event-bearing sections, 20 events; 20 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: nomad (actor 0, community); nomad_truck (actor 1, community); Player (actor 2, findInContext).

Entries: `spr_03_nomad_chat_start` → 1.

Exits: `spr_03_nomad_chat_end` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 20 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `d5f1befcff79d14998ef801ed734b750d235f989ee7c3934716e8c26e0c48c2f`. Binary SHA-256: `ab16010afaa8b726696e11114d3298a93aa37d4449b0e46d56d3e9e03c8e8824`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\wellsprings\sts_hey_spr_03\scene\sts_hey_spr_03_nomad_chat.scene" --events
```

