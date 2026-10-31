# Gig: Hippocratic Oath: scene presentation

Journal identity: `quests/street_stories/watson/kabuki/sts_wat_kab_02`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_kab_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_chats.scene`

4 graph nodes, 4 edges; 1 event-bearing sections, 6 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: ganger1 (actor 0, findInWorld); ganger2 (actor 1, findInWorld); player (actor 2, findInContext).

Entries: `kab_02_ganger_chat_start` → 1.

Exits: `kab_02_ganger_chat_start_end` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 3 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `74257761f26b802a9886825050350f6ea8a6c54b8b786c82bf4ced219196e979`. Binary SHA-256: `4d91bb2fcb085f4b4ad767ba82659c64814fa07dcd76b96317103963bc9aa494`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_chats.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_holocall_debriefs.scene`

26 graph nodes, 34 edges; 2 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 15.

Exits: `rejected_out` → 287; `End 0` → 16.

End nodes: 16: `<omitted>`; 287: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `c0da588f79cf2e7c2d020d32cb02d340236fd49c7e57f41e4517d4f8c7c42d0c`. Binary SHA-256: `5c9bae2e8e03d9268ca3e96ff2a543984afa41e29bafe36747b15b27f1c769d9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 13 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 15.

Exits: `End 0` → 16; `rejected_out` → 260.

End nodes: 16: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 18 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 5 | 18 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 6 | 18 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 1

Raw SHA-256: `8240d0121f2d8ca00fbe026b619e2d630d7a3c9cbb52a9f16db08a135b482f95`. Binary SHA-256: `022feaa82090debbbeab0ac4e79bf5008dec8e1db4da8a3a2cf42188c6f1b3ed`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene`

155 graph nodes, 195 edges; 43 event-bearing sections, 295 events; 212 screenplay lines, 38 screenplay options, 10 choice nodes.

Actors: Lucy (actor 0, community); Regina_Jones (actor 1, findInContext); Injured_Maelstrom (actor 2, community); V (actor 3, findInContext).

Entries: `kab_02_lucy_start` → 2; `kab_02_v_comments` → 559; `Start 22` → 1300; `kab_02_car_arrived` → 781; `kab_02_call_fixer` → 449; `kab_02_ending` → 450; `kab_02_killed` → 464.

Exits: `kab_02_lucy_e` → 367; `away_from_car` → 751; `signal release` → 1341; `kab_02_call_fixer_e` → 452; `kab_02_ending_e` → 453; `kab_02_lucy_e_patient_killed` → 466.

End nodes: 367: `NonTerminating`; 452: `NonTerminating`; 453: `NonTerminating`; 466: `NonTerminating`; 751: `<omitted>`; 1341: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 293 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnChangeIdleAnimEvent` | 12 | 293 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 116 | 293 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 6 | 335 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/17` |
| `scnIKEvent` | 12 | 335 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |
| `scnLookAtEvent` | 38 | 293 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnPlaySkAnimEvent` | 35 | 293 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnUnmountEvent` | 6 | 335 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/16` |
| `scneventsAttachPropToNode` | 1 | 898 / 461 | `/Data/RootChunk/sceneGraph/Data/graph/77/Data/events/9` |
| `scneventsAttachPropToPerformer` | 1 | 898 / 449 | `/Data/RootChunk/sceneGraph/Data/graph/77/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 6 | 335 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/15` |
| `scneventsSocket` | 53 | 293 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- speech, gaze: 6
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- socket_signal: 1
- speech, skeletal_animation: 1

Raw SHA-256: `1695c35c4ae3e6bb471e3663beedad3100928c7e8a4941d3b5b54d9ecb748c3f`. Binary SHA-256: `9dc7203ccaa4c2da25aa7481e6ea7bbf1de47072b2cd3d106d1fd3043b62b223`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene" --events
```

