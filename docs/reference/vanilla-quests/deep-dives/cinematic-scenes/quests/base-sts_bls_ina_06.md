# Gig: No Fixers: scene presentation

Journal identity: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_06`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_bls_ina_06.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\scenes\sts_bls_ina_06_01_hostage.scene`

47 graph nodes, 46 edges; 12 event-bearing sections, 125 events; 36 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: hostage (actor 0, findInWorld); guard (actor 1, findInWorld); V (actor 2, findInContext).

Entries: `car_chit_chat` → 30; `meeting_tanner` → 1; `fear_in` → 153; `ganger_and_trevor` → 15.

Exits: `meeting_tanner_out` → 2; `ganger_and_trevor_out` → 50.

End nodes: 2: `<omitted>`; 50: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 32 | 3 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 16 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/30` |
| `scnIKEvent` | 6 | 16 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/25` |
| `scnLookAtEvent` | 23 | 16 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 24 | 3 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 3 | 16 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/29` |
| `scneventsSetAnimFeatureEvent` | 3 | 16 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/28` |
| `scneventsSocket` | 22 | 3 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, gaze: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- idle_animation: 1
- gaze: 1

Raw SHA-256: `ff86d1f630f4f9c37eb18b18c07d86b3e36436d333c3f9e350a1c67a8199d018`. Binary SHA-256: `e11b883d3b3f73b34253f02fe4ea4e2c814fe55ef5555792b072ffc9ee343283`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\scenes\sts_bls_ina_06_01_hostage.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\scenes\sts_bls_ina_06_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: dakota (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 285.

End nodes: 2: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 74 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `5d2df8b8dab1c25897f4cf71dcd695522ffdf45fc50a780c25d8f2784aa548c5`. Binary SHA-256: `d8f3e22bafbe934da7d655eb07e8a6d304ed00aac29acf541857dab4d4aa4ace`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\scenes\sts_bls_ina_06_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\scenes\sts_bls_ina_06_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: dakota (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 68 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `cf1d0002c690dbf8d8cec87b5059f7f52ae775e4ae24a3486b14651e45f67874`. Binary SHA-256: `39160dfb0e795a909e940dd7a2ca172a10262772fd25d90f7ef2d39777d00c27`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\scenes\sts_bls_ina_06_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\scenes\sts_bls_ina_06_meeting_dakota.scene`

47 graph nodes, 50 edges; 12 event-bearing sections, 116 events; 23 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: dakota (actor 0, spawnSet); tanner (actor 1, findInWorld); v (actor 2, findInContext).

Entries: `dakota_chat` → 6.

Exits: `dakota_chat_out` → 25.

End nodes: 25: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 15 | 9 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnDialogLineEvent` | 20 | 9 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 22 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/24` |
| `scnIKEvent` | 4 | 22 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/16` |
| `scnLookAtEvent` | 30 | 9 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 18 | 9 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scnUnmountEvent` | 2 | 22 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/23` |
| `scneventsEquipItemToPerformer` | 2 | 22 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/32` |
| `scneventsSetAnimFeatureEvent` | 2 | 22 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/21` |
| `scneventsSocket` | 19 | 9 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scneventsVFXEvent` | 2 | 40 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech: 2
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- socket_signal: 1
- skeletal_animation, socket_signal: 1
- gaze: 1

Raw SHA-256: `0f68a45ea8c9c240e67df9a8c296d6c7aaacbeb335bcd75f3a45d174475f7ed7`. Binary SHA-256: `10d68773e582132d707ac4ca3f58f0b9349eeb6e6b943e35a598f5c767e8f8a9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_06\scenes\sts_bls_ina_06_meeting_dakota.scene" --events
```

