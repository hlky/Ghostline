# Gig: A Shrine Defiled: scene presentation

Journal identity: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_03`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wbr_jpn_03.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene`

25 graph nodes, 33 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 285.

End nodes: 2: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 27 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `a71f392b18bb9b495afb5070855cb7ae7b0269f5079ad3bb298a838cea163c89`. Binary SHA-256: `a91d8ffb998542744fa00b03327af21251a2dceeb6d11e95846ac0f4c55df101`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_debrief.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 1 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `013c5ca8f8c2df005fed0481092340dc59d00f7ff35538e0a1d6de87c2a13f24`. Binary SHA-256: `5b42116e629f8f34868a3e893406a456c4e66b34ee678b34c31ca0a3589d29c9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_03\scenes\sts_wbr_jpn_03_holocall_prebrief.scene" --events
```

