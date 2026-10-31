# Gig: Sr. Ladrillo's Private Collection: scene presentation

Journal identity: `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_02`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_hey_rey_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene`

18 graph nodes, 18 edges; 4 event-bearing sections, 6 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: civilian_talk_001 (actor 0, community); civilian_talk_002 (actor 1, community); civilian_talk_004 (actor 2, community); civilian_talk_005 (actor 3, community).

Entries: `rey_02_distract_holograms_start` → 1; `rey_02_civilians_chat_004_start` → 22; `rey_02_civilians_chat_001_start` → 13; `rey_02_civilians_chat_002_start` → 14.

Exits: `rey_02_civilians_chat_001_end` → 41; `rey_02_civilians_chat_002_end` → 42; `rey_02_civilians_chat_004_end` → 44; `rey_02_distract_holograms_end` → 12.

End nodes: 12: `<omitted>`; 41: `<omitted>`; 42: `<omitted>`; 44: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 23 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnLookAtEvent` | 2 | 24 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, gaze: 1

Raw SHA-256: `d900eb7febe16c4960153dfe795723de6483f63fc2e2a4ca10620b032f490185`. Binary SHA-256: `c0ce7b7fab25a7925953d00129b1bbbe1c268bbe3b9027805fed3be6287ca38b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_civilians.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_gangers.scene`

29 graph nodes, 32 edges; 5 event-bearing sections, 34 events; 10 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: ganger_001 (actor 0, findInWorld); ganger_003 (actor 1, findInWorld); ganger_005 (actor 2, findInWorld); prostitute_001 (actor 3, findInWorld); prostitute_002 (actor 4, findInWorld); V (actor 5, findInContext).

Entries: `rey_02_entrence_start` → 1; `rey_02_ganger_chat_001_start` → 89; `rey_02_stippers_chat_001_start` → 98.

Exits: `rey_02_entrence_end` → 3; `rey_02_ganger_chat_001_end` → 90; `rey_02_stippers_chat_001_end` → 99.

End nodes: 3: `<omitted>`; 90: `<omitted>`; 99: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 10 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 5 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 11 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 3 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 2 | 12 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1

Raw SHA-256: `12c096ce8b2fc6dd509e2c59aff5f05883ecf5e221690636b6127b5749c1e1c8`. Binary SHA-256: `76e38cc3bf68c411f9b78c51d14a9887b6ce0ee4bc920ce75b283de1aac3f9f5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_gangers.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Padre (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 297.

End nodes: 2: `<omitted>`; 297: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 33 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `730a09aebcdaa788679f0a8dc63afbed820a74bc40b0edbe83f7617ec3223df1`. Binary SHA-256: `53d3197408685f0a6309a014b7896bf00527b0300195a00a0f256bd91f53babb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Padre (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `fc295fa647c5fef586e4c87f941082fb97fbf1f6edea50959b8849928059084c`. Binary SHA-256: `48f8054c646a20718b7168e6853d84443d7f7213a7a88b4b2b83429c3a29000b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_02\scenes\sts_hey_rey_02_holocall_prebrief.scene" --events
```

