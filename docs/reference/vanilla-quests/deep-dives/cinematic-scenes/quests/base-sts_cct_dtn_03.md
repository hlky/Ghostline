# Gig: A Lack of Empathy: scene presentation

Journal identity: `quests/street_stories/city_center/downtown/sts_cct_dtn_03`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_cct_dtn_03.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\scenes\sts_cct_dtn_03_guard_scene_before_security_room.scene`

13 graph nodes, 11 edges; 2 event-bearing sections, 21 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: dtn_03_ws_enemy_002 (actor 0, community); Player (actor 1, findInContext).

Entries: `security gate warning` → 1; `security_gate_weapons_left` → 6.

Exits: `End 0` → 2; `End1` → 7.

End nodes: 2: `<omitted>`; 7: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 3. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 4 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 4 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 5 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 6 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2

Raw SHA-256: `6119bd92c9243a81471fa5652bc8d95f6f0b884e612f9d6a863287cdbebd5848`. Binary SHA-256: `119539407561a94a402b3b5cc062faf077daa640a5cfec6a89a146c8c188d1a5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\scenes\sts_cct_dtn_03_guard_scene_before_security_room.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\scenes\sts_cct_dtn_03_holocall_debriefs.scene`

25 graph nodes, 33 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 297.

End nodes: 2: `<omitted>`; 297: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `10ad1893aeb9102df103c1a12b45979a9b14aa0a17860e6a6916ec4e32439bc8`. Binary SHA-256: `82925ee6d772bba1d040d84872a5ad72bc8f31cb63a5bb0258b99254ac04902f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\scenes\sts_cct_dtn_03_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\scenes\sts_cct_dtn_03_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 262.

End nodes: 2: `<omitted>`; 262: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `4cf76349c76737a0fc45f99325465a9f86148988535a9fe2bb269697b54c2b16`. Binary SHA-256: `8a8c80f8c98f1fb58452d6e54c298e45404a58018e8e7dad98580a3b98f289ce`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\scenes\sts_cct_dtn_03_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\scenes\sts_cct_dtn_03_main_scene.scene`

39 graph nodes, 37 edges; 6 event-bearing sections, 53 events; 27 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: #dtn_03_ws_enemy_002 (actor 0, findInWorld); #dtn_03_ws_enemy_006 (actor 1, findInWorld); dtn_03_receptionist_slacker (actor 2, community); dtn_03_receptionist (actor 3, community); #dtn_03_ws_prostitute_006 (actor 4, findInWorld); #dtn_03_ws_prostitute_007 (actor 5, findInWorld); barman (actor 6, spawnSet); high_civilian_1 (actor 7, community); high_civilian_2 (actor 8, community); high_civilian_criminal (actor 9, community); manager (actor 10, community); Player (actor 11, findInContext).

Entries: `Start 15` → 109; `prostitute_start` → 73; `Start 16` → 111; `toilet_walker` → 42; `leave_weapons` → 7; `reception_fluff` → 65; `Start 14` → 107.

Exits: `End3` → 219; `End1` → 113; `End4` → 221; `End2` → 123; `toilet_walker_end` → 89; `End 3` → 99.

End nodes: 89: `<omitted>`; 99: `<omitted>`; 113: `<omitted>`; 123: `<omitted>`; 219: `<omitted>`; 221: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 3. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 66 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnDialogLineEvent` | 27 | 43 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnLookAtEvent` | 4 | 66 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnPlaySkAnimEvent` | 12 | 66 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/6` |
| `scneventsSocket` | 5 | 43 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, gaze: 1

Raw SHA-256: `1468d9c53aae769ad13f532f652b32adffc49ff9998ff5baf90b46340fce96e3`. Binary SHA-256: `ed42ea9fd560eca029d0eb6bd91790264c53b512a87323f6cb586d130e906680`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\downtown\sts_cct_dtn_03\scenes\sts_cct_dtn_03_main_scene.scene" --events
```

