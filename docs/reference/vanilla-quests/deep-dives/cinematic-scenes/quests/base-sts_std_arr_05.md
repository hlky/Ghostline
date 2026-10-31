# Gig: Breaking News: scene presentation

Journal identity: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_05`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_std_arr_05.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_fox_talk.scene`

116 graph nodes, 151 edges; 14 event-bearing sections, 119 events; 37 screenplay lines, 13 screenplay options, 7 choice nodes.

Actors: Fox (actor 0, community); Fox_phone (actor 1, findInContext); fox_car (actor 2, community); truck (actor 3, community); Player (actor 4, findInContext).

Entries: `arr_05_fox_talk_start` → 1; `truck` → 609.

Exits: `arr_05_fox_talk_end` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 65 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnDialogLineEvent` | 29 | 35 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 34 | 35 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 17 | 46 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnPoseCorrectionEvent` | 3 | 404 / 371 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/7` |
| `scneventsAttachPropToPerformer` | 3 | 457 / 379 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 2 | 404 / 361 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/3` |
| `scneventsSocket` | 27 | 46 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- props_equipment: 2
- speech, gaze: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- props_equipment, socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state: 1
- gaze: 1

Raw SHA-256: `d5f57002585808c151475b96003da5b771d058512d55f7f37b0c446bf17d0689`. Binary SHA-256: `f3c5d523b4889ca9f7f5480598414159299dc8a7657c603791acb9f42ce43158`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_fox_talk.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_holocall_debriefs.scene`

28 graph nodes, 37 edges; 3 event-bearing sections, 7 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `Start1` → 105.

Exits: `rejected_out` → 287; `End1` → 106.

End nodes: 106: `<omitted>`; 287: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 7 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `4b824d058d2a1bf8c3ee98c7c85ef7a224b35775b291dc3ea1a56b3ca428a3b1`. Binary SHA-256: `9c798c8d9548a7c39b3b115133dcdb7f2c966b9f80985dfda4ac8dea0e84a217`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `Start1` → 105.

Exits: `rejected_out` → 270; `End1` → 106.

End nodes: 106: `<omitted>`; 270: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 25 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `67def9a513a897ae0179c160116de8754cd59bea42d6e82111c7e8c850443e17`. Binary SHA-256: `cbd81810bf106dc4ef51160f6491f70564ac2cf87e52f30c85d360894766f827`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_05\scenes\sts_std_arr_05_holocall_prebrief.scene" --events
```

