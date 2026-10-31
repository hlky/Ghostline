# Gig: Psychofan: scene presentation

Journal identity: `quests/street_stories/heywood/glen/sts_hey_gle_03`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_hey_gle_03.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: padre (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 283.

End nodes: 2: `<omitted>`; 283: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 16 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `7f537167ee9c7e8e10da9b11e5ef52c04a4e207606cc06107a52683459587868`. Binary SHA-256: `7272d22d4b6a36303b6b12c8a35e124d5b649103936e3f89094683d8b9aeb147`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: padre (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 254.

End nodes: 2: `<omitted>`; 254: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 29 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `3823a22dbef2f3cec6d4d6ff05c3c820b1425462ae2c0157a9baa3176742da8a`. Binary SHA-256: `73f6ddffa559752bccc1e3cbf0f97a26e301e9529688244d8af19031926a5b42`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene`

133 graph nodes, 147 edges; 17 event-bearing sections, 167 events; 39 screenplay lines, 7 screenplay options, 7 choice nodes.

Actors: ma_rec_001 (actor 0, community); ma_rec_002 (actor 1, community); security (actor 2, community); silverhand (actor 3, spawnDespawn); Player (actor 4, findInContext).

Entries: `rec_fluff` → 1; `security` → 6; `Start 3` → 38; `johnny_comments_in` → 158.

Exits: `rec_fluff_o` → 2; `security_o` → 7; `End 2` → 39; `Johnny_end` → 273.

End nodes: 2: `NonTerminating`; 7: `NonTerminating`; 39: `<omitted>`; 273: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 3 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 38 | 3 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtEvent` | 31 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 51 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsEquipItemToPerformer` | 5 | 3 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scneventsSocket` | 23 | 3 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scneventsUnequipItemFromPerformer` | 3 | 3 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsVFXEvent` | 11 | 16 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, vfx, socket_signal: 8
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `9b086caba8cbbcf7c57e0132ebfe83fbfe0cc3717b9a19ab75ef19fb5c2b5801`. Binary SHA-256: `bc6ce8d87cad3c2fbb3645ad7319e18d224a0fe55f660fccd9c6e082080d420a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\glenn\sts_hey_gle_03\scenes\sts_hey_gle_03_scene.scene" --events
```

