# Gig: Greed Never Pays: scene presentation

Journal identity: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wbr_jpn_12.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 1 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start1` → 56.

Exits: `rejected_out` → 285; `End1` → 57.

End nodes: 57: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 29 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `1db92eae11eb1a7fcc5cca72ef30aa431cd14e93b64fe28da5382bdcac147b4b`. Binary SHA-256: `e635a43e733275a2e42201456338e7fed586007747d77a67165398eb8dd0b61e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_debrief.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start1` → 56.

Exits: `End1` → 57; `rejected_out` → 260.

End nodes: 57: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 29 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `ddaa703b33117539f1483e6a9f0e76c2d26b5a76553ed24b9f022ab2d90c928c`. Binary SHA-256: `30335bee2aff92b9657d2f20fabcb65e01c78bd6f634a8a3c6799b340eaf0015`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wat_jpn_12_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wbr_jpn_12_silverhand.scene`

72 graph nodes, 80 edges; 9 event-bearing sections, 24 events; 25 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Silverhand (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `silverhand_first_location_start` → 1; `silverhand_second_location_start` → 46.

Exits: `silverhand_second_location_end` → 216; `silverhand_first_location_end` → 2.

End nodes: 2: `NonTerminating`; 216: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 24 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9

Raw SHA-256: `0e84389cfd26a432dda697a107de756899b244ad2407107465f2f12b47aace54`. Binary SHA-256: `d779ec443adb1d02518cb344c0009215ce65397f6e3e12b58518aa073da3d456`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_12\scenes\sts_wbr_jpn_12_silverhand.scene" --events
```

