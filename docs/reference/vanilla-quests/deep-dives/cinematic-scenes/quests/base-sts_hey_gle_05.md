# Gig: Going Up or Down?: scene presentation

Journal identity: `quests/street_stories/heywood/glen/sts_hey_gle_05`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_hey_gle_05.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene`

71 graph nodes, 81 edges; 15 event-bearing sections, 118 events; 43 screenplay lines, 9 screenplay options, 4 choice nodes.

Actors: gallo (actor 0, community); Player (actor 1, findInContext).

Entries: `gle_05_gallo_vision_start` → 1; `gle_05_gallo_non_vision_start` → 14; `gle_05_gallo_lights_start` → 98; `gle_05_gallo_spotted_start` → 106.

Exits: `gle_05_gallo_combat_end` → 2; `gle_05_gallo_no_combat_end` → 10; `gle_05_gallo_lights_end` → 101; `gle_05_gallo_spotted_end` → 103; `gle_05_gallo_escape_end` → 125.

End nodes: 2: `<omitted>`; 10: `NonTerminating`; 101: `<omitted>`; 103: `<omitted>`; 125: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 77 / 279 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scnChangeIdleAnimEvent` | 7 | 5 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 30 | 5 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnLookAtEvent` | 9 | 5 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 46 | 5 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsSocket` | 25 | 5 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, socket_signal: 1
- speech: 1
- speech, audio: 1
- speech, skeletal_animation, gaze: 1
- gaze: 1

Raw SHA-256: `639c106f407e2daa5dfc109211484216d39674aaedb15c09d4f7c0af2466805b`. Binary SHA-256: `683bcd521162c39a5157a9657a3797b6040f29fa9c805890127b81cfa99fb76b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_conversation.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_scene.scene`

8 graph nodes, 8 edges; 3 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: #gle_05_ws_gallo (actor 0, findInWorld); Player (actor 1, findInContext).

Entries: `sequence_start` → 43.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 8 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `03105ae53359765d13d5fe6548575ebb119909df9f43185cc78f9d33aa9e3d55`. Binary SHA-256: `2bc09b163c6bd3a4e0e2c9383199d364cf04805418a520d73a2a2435f2e3af02`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_el_gallo_scene.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: padre (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 286.

End nodes: 2: `<omitted>`; 286: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 25 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `3940dcea0bf0893a57b69782abfea86d3500111e724d824d39c2bcab9f36725b`. Binary SHA-256: `4131c63d8e3c1a27f40c7c6ed5edf4b079bf82e4bcb6d5659dbd284cf353792e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: padre (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `c5632d9e987499adaf8b54282afa9452dc98860dbdc785ef412d53056df383a1`. Binary SHA-256: `4a5ca57bf7eea5a7d57076453b638cdabb5439d33a29f0f52e0754b219405bb4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_opening_scene.scene`

3 graph nodes, 2 edges; 1 event-bearing sections, 1 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: homeless_001 (actor 0, community); Player (actor 1, findInContext).

Entries: `homeless_start` → 21.

Exits: `homeless_end` → 25.

End nodes: 25: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 22 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `3cf22e92b808772dc0f2560795316da42c6715b98db6ecf342ca0c4db08937e6`. Binary SHA-256: `fd774e97aa0d37ee57993916b8e47ae8bd36e4ffe5a903f1643c13b1733be62f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_05\scenes\sts_hey_gle_05_opening_scene.scene" --events
```

