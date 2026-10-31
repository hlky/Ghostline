# Gig: Big Pete's Got Big Problems: scene presentation

Journal identity: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_02`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_bls_ina_02.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene`

47 graph nodes, 51 edges; 10 event-bearing sections, 63 events; 26 screenplay lines, 4 screenplay options, 1 choice nodes.

Actors: big_pete (actor 0, community); Player (actor 1, findInContext).

Entries: `big_pete_door` → 1.

Exits: `big_pete_spared` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 9 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 20 | 9 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 1 | 386 / 285 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/7` |
| `scnIKEvent` | 2 | 386 / 278 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/1` |
| `scnLookAtEvent` | 3 | 9 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 10 | 9 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 1 | 386 / 284 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 1 | 386 / 282 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/5` |
| `scneventsSocket` | 21 | 9 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 2 | 24 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech: 1
- socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `efed258fe11c7007709a294efbdc78e6b450544be89508c0874211ef0a15890e`. Binary SHA-256: `da6d996583879fdd664bdab5ac8f3e027894e39a81ba1341fc92f6aeab61d6f9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_big_pete_scene.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene`

25 graph nodes, 33 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: dakota (actor 0, spawnSet).

Entries: `Start 0` → 38.

Exits: `rejected_out` → 286; `End 0` → 39.

End nodes: 39: `<omitted>`; 286: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 66 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `64f93aeb1bb3821ab4c979e687c77cb483de7779c23400312a735aa58e7d5e99`. Binary SHA-256: `6074e24de6ae339f4fa649777e9d344add3eace25fd8b26160d1a2af1eb0bc0a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: dakota (actor 0, spawnSet).

Entries: `Start 0` → 21.

Exits: `rejected_out` → 269; `End 0` → 43.

End nodes: 43: `<omitted>`; 269: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 45 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `92ed51e2b81dc96492fcc785cf4208256b1e52d4ca0314dd15ddf8ca4701f186`. Binary SHA-256: `1034ad33698c1af6dc1ab40a57cb5805cb476ca74d8f8b6a8b1b41629da7cda1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_02\scenes\sts_bls_ina_02_holocall_prebrief.scene" --events
```

