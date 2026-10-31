# Gig: Error 404: scene presentation

Journal identity: `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_04`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_std_rcr_04.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 1 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: muamar (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 287.

End nodes: 2: `<omitted>`; 287: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 16 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `0f1b59e52ea3b25b853e85246046ee5992b8ee294ce73b300d46542d4300d88b`. Binary SHA-256: `3393bbd1e5bdb534ef2b8ed6270dc4c10f5afbc58f0ebd063e241899a8f29f5b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: muamar (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 29 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `c2fb60e54fb3cdfd571d89c33527e180de20a774e11f05a740e6fc99208de048`. Binary SHA-256: `8a1c46a85e44df2eab7cad6288518009d3c3ab99f57e04a9b8c695e5ad61c594`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_johnny.scene`

6 graph nodes, 5 edges; 1 event-bearing sections, 10 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 4 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 2 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 3 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, audio: 1

Raw SHA-256: `5e3a7368768aeb96f8853650ec9b1cca482de908777a76ec53eff94d606c7075`. Binary SHA-256: `1ac894fc5640c8be691f7888e3d4b8ae30c071aacb4063afafe84919d0a6f350`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_04\scenes\sts_std_rcr_04_johnny.scene" --events
```

