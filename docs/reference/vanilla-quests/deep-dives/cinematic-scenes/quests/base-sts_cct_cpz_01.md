# Gig: Serial Suicide: scene presentation

Journal identity: `quests/street_stories/city_center/corpo_plaza/sts_cct_cpz_01`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_cct_cpz_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 286.

End nodes: 2: `<omitted>`; 286: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 18 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `c0cbf36cece53f5b44747fb448544a3ae2285698ddd56e4fc01dbdae917e82bb`. Binary SHA-256: `6796ec6af19c45c3a7dfb745086c2b8a98fe595fc8bc766d9f267c724d635073`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_debrief.scene" --events
```

## `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_prebrief.scene`

23 graph nodes, 26 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 268.

End nodes: 2: `<omitted>`; 268: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 27 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `bd330cfba01299bb89adffa152f4d2da082be6a2523029cc4467871e673ac461`. Binary SHA-256: `13f54c2f177d0966285810888a43111f57b21da7dd5252526b8495cc6138c701`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_prisoner_chat.scene`

60 graph nodes, 69 edges; 13 event-bearing sections, 114 events; 29 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: prisoner_001 (actor 0, community); guard_004 (actor 1, community); Player (actor 2, findInContext).

Entries: `cpz_01_prisoner_chat_start` → 1; `CineStart02` → 149.

Exits: `Scene interrupted` → 64.

End nodes: 64: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnDialogLineEvent` | 20 | 3 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scnGameplayTransitionEvent` | 3 | 189 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/8` |
| `scnIKEvent` | 6 | 189 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/2` |
| `scnLookAtEvent` | 12 | 3 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 32 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 3 | 189 / 297 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/7` |
| `scneventsEquipItemToPerformer` | 2 | 3 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/31` |
| `scneventsSetAnimFeatureEvent` | 3 | 189 / 295 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/6` |
| `scneventsSocket` | 27 | 3 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scneventsUnequipItemFromPerformer` | 1 | 248 / 430 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `967737558ac7c12887b0869fd3bc7b15e75567eeaa074fc9910a94398696644f`. Binary SHA-256: `9730ee61a82f903ae5dd3b00ec64ece8655b3d0f3c0586c1af0a079dc43b8295`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\city_center\corpo_plaza\sts_cct_cpz_01\scenes\sts_cct_cpz_01_prisoner_chat.scene" --events
```

