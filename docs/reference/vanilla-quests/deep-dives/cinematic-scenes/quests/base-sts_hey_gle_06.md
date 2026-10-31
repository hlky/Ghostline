# Gig: Life's Work: scene presentation

Journal identity: `quests/street_stories/heywood/glen/sts_hey_gle_06`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_hey_gle_06.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_debriefs.scene`

27 graph nodes, 35 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Padre (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 12.

Exits: `End 0` → 13; `rejected_out` → 295.

End nodes: 13: `<omitted>`; 295: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 31 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `79e15199f4fddd9782ce08dcb657423ac24766e3cdf4eda55b9e486433a13587`. Binary SHA-256: `c8b61df640ca4e6ff54dd9bf667c65701097a86b6a44768381e664eda7e925a6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Padre (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 15.

Exits: `End 0` → 16; `rejected_out` → 260.

End nodes: 16: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 17 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `177e269f504e2a602c655fd551b06732e164ba1912075ea561ce448b681b9342`. Binary SHA-256: `c14f88fa90056105114ff534327bc74de6090f8fb473e78b994840bf454f9d02`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_scene.scene`

21 graph nodes, 19 edges; 6 event-bearing sections, 45 events; 20 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: 6thStreet (actor 0, findInWorld); Repair (actor 1, findInWorld); Forklift (actor 2, findInWorld); 6thStreetGanger (actor 3, findInWorld); Estevez (actor 4, findInWorld); Jake_Car (actor 5, spawner); Player (actor 6, findInContext).

Entries: `Jake` → 58; `car_talk` → 95; `jake_comment` → 96.

Exits: `car_talk_e` → 97; `jake_comment_e` → 98; `JakeEnd` → 62; `SceneEnd` → 124.

End nodes: 62: `<omitted>`; 97: `<omitted>`; 98: `<omitted>`; 124: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 60 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 19 | 60 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 86 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/17` |
| `scnIKEvent` | 2 | 86 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnLookAtEvent` | 3 | 60 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnPlaySkAnimEvent` | 11 | 60 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 1 | 86 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scneventsSetAnimFeatureEvent` | 1 | 86 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scneventsSocket` | 5 | 60 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 60 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `7ea8909cf67962639464ae5c495a0554263580a743a5b93ab922b0165f554ea1`. Binary SHA-256: `4842b158c8f279287cfdbed34c30c6b769f1a4f692a4f4ecb6ae5636ad88cb7c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_06\scenes\sts_hey_gle_06_scene.scene" --events
```

