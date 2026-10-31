# Gig: MIA: scene presentation

Journal identity: `quests/street_stories/badlands/inland_avenue/sts_bls_ina_09`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_bls_ina_09.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\scenes\sts_bls_ina_09_benedict.scene`

40 graph nodes, 41 edges; 11 event-bearing sections, 94 events; 37 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: ben (actor 0, community); dakota (actor 1, spawnSet); nomad (actor 2, community); v (actor 3, findInContext).

Entries: `meeting_ben` → 1; `ben_in_car` → 12; `interrupt_failsafe` → 178; `ben_idling` → 181.

Exits: `meeting_ben_out` → 2; `ben_in_car_out` → 15.

End nodes: 2: `<omitted>`; 15: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 70 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnDialogLineEvent` | 35 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 14 | 5 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 23 | 5 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 18 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation: 1
- speech: 1
- speech, skeletal_animation, gaze: 1
- socket_signal: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `74460603df2d90606e9613f366d1752aa792a53c559ccec13222067e123725bc`. Binary SHA-256: `d52f92948b9660926497cc79ff3441a5d54df8bb765989c57981198cf14f02fb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\scenes\sts_bls_ina_09_benedict.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\scenes\sts_bls_ina_09_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: dakota (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 285.

End nodes: 2: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 68 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `367262f47c9c6a4273e0fda5b06f0c0fbbee0fed6fd0f7ae8554acaf5cf0d53a`. Binary SHA-256: `bb6764d5b8528d50c82c3d58781d52bab323bf91c2c5f2f32a4b6e79d2fc34e7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\scenes\sts_bls_ina_09_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\scenes\sts_bls_ina_09_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: dakota (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 68 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `631233036c4cf6f800ca51a8daef8f43c16d16acccaf9cf8de3efb988c4f6f72`. Binary SHA-256: `8e21340c5a9b5831c14245e46be61d6001b53683581dc554ab2e951e32c80d9e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\scenes\sts_bls_ina_09_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\scenes\sts_bls_ina_09_meeting_nomad.scene`

55 graph nodes, 63 edges; 5 event-bearing sections, 49 events; 7 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: ben (actor 0, community); nomad (actor 1, community); Player (actor 2, findInContext).

Entries: `meeting_nomad` → 4.

Exits: `meeting_nomad_out` → 6.

End nodes: 6: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 7 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 1985 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/9` |
| `scnIKEvent` | 2 | 1985 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/4` |
| `scnLookAtEvent` | 10 | 5 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 12 | 5 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnUnmountEvent` | 1 | 1985 / 358 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/8` |
| `scneventsEquipItemToPerformer` | 1 | 1989 / 362 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 1985 / 356 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/7` |
| `scneventsSocket` | 11 | 5 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1985 / 346 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `84e99a0336d5e30d98a4ca98d7d8f924a7479782cc7955cc76db6bb1ef69cdea`. Binary SHA-256: `8d293a18894595abe51ba72877e7d91583328d7d1c21bcdaf2913d629b93037e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\badlands\inland_avenue\sts_bls_ina_09\scenes\sts_bls_ina_09_meeting_nomad.scene" --events
```

