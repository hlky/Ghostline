# Cyberpsycho Sighting: Where the Bodies Hit the Floor: scene presentation

Journal identity: `quests/minor_quest/ma_wat_nid_03`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_wat_nid_03-f6d2e608.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\scenes\ma_wat_nid_03_brief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `regina_brief_in` → 1.

Exits: `regina_brief_out` → 2; `rejected_out` → 271.

End nodes: 2: `<omitted>`; 271: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 39 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `f2337a3b5d42c23de048f3631f1e619786968cd90d4d23bf7dfc817e6c0d1f64`. Binary SHA-256: `2ca0bedd17dbf43a206f7847c3ae17d6d98c9d37e2511cd89d29b4e15345141e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\northside\ma_wat_nid_03\scenes\ma_wat_nid_03_brief.scene" --events
```

## `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\scenes\ma_wat_nid_03_scene.scene`

10 graph nodes, 7 edges; 1 event-bearing sections, 2 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: maelstrom_boomer (actor 0, community); ellis (actor 1, community); johnny (actor 2, spawnDespawn).

Entries: `maelstrom_inspects_corpse_in` → 44; `johnny_corpo_corpse_comment_in` → 64; `voiceset_in` → 70.

Exits: `johnny_corpo_corpse_comment_out` → 65; `voiceset_out` → 71.

End nodes: 65: `<omitted>`; 71: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scneventsSocket` | 2 | 67 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- socket_signal: 1

Raw SHA-256: `5aa446953536d0c475b2f3ba2e139d670d39cefe135c533cc96466609e3886f2`. Binary SHA-256: `66ed0c6c427df4171d6e8cb1ba37d23e7112b03690ff3d79960f12527c01f31e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\northside\ma_wat_nid_03\scenes\ma_wat_nid_03_scene.scene" --events
```

