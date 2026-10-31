# Cyberpsycho Sighting: On Deaf Ears: scene presentation

Journal identity: `quests/minor_quest/ma_cct_dtn_03`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_cct_dtn_03-df6be515.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `regina_brief_in` → 1.

Exits: `regina_brief_out` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 37 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `4fa300e6575029d92a10b954192569416cb94b4bb873114286556dd5ea3509dd`. Binary SHA-256: `f1d1ca536b121d75d7bb2112635b260edc9c2811147f2d3960a7e74a74a9900a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene" --events
```

## `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_scenes.scene`

27 graph nodes, 28 edges; 2 event-bearing sections, 9 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: worker (actor 0, community); car_driver (actor 1, community); car_passenger (actor 2, community); scavenger_van (actor 3, community).

Entries: `car_scavengers_in` → 59; `worker_escapes_in` → 1.

Exits: `worker_escapes_out` → 2; `worker_scream` → 43.

End nodes: 2: `<omitted>`; 43: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnGameplayTransitionEvent` | 1 | 6 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnIKEvent` | 2 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSocket` | 3 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1

Raw SHA-256: `af17d462d804ebbba27d24a1493b9d2a8315277e0ff13bd9cab3665958d7d4b4`. Binary SHA-256: `75eb8ce4811f4881edc9f31b596cce3fa4147a81561b528f1767e3e4340fe0eb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_scenes.scene" --events
```

