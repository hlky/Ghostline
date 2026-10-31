# I'm in Love with My Car: scene presentation

Journal identity: `quests/minor_quest/mq050_ken_block_tribute`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq050_ken_block_tribute.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq050\scenes\mq050_johnny_start.scene`

16 graph nodes, 18 edges; 2 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `ContinueQuest` → 7.

End nodes: 2: `<omitted>`; 7: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 65 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `adfd7b76b28308fa60ea8a0b8fb003ecd582daedf04babefaf8e9e9f5c568990`. Binary SHA-256: `0aa994296e3e1792aa3ea1e35fd1ca8441348a9b057f98d767e11519cc135eeb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq050\scenes\mq050_johnny_start.scene" --events
```

