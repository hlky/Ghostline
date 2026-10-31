# Cyberpsycho Sighting: Discount Doc: scene presentation

Journal identity: `quests/minor_quest/ma_std_rcr_11`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_std_rcr_11.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_01_briefing.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 255.

End nodes: 2: `<omitted>`; 255: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 29 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `0a73b32d4ac33209fa74c5cdeed5bfb7cee5d7693f26ea303639a38b22e3a378`. Binary SHA-256: `8d22d854099b1bf31b233e76c0f27501d21022eeff95a626f17e21405e41aa61`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_01_briefing.scene" --events
```

## `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_02_carthrow.scene`

33 graph nodes, 33 edges; 1 event-bearing sections, 38 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Jackie (actor 0, community); Royce (actor 1, community).

Entries: `Start 0` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 18 | 14 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnChangeIdleAnimEvent` | 1 | 14 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnPlaySkAnimEvent` | 3 | 14 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 5 | 14 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsVFXEvent` | 11 | 14 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1

Raw SHA-256: `b6b80cffd9a57f543cc023da67fafbe99b55c6ffa3ac2cf8e4f5e8830df1303d`. Binary SHA-256: `c20d47fca102197c0e4cb95a0be03a2bc23e2f60dd1d1029bcc71ae7c9fe8e38`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_02_carthrow.scene" --events
```

