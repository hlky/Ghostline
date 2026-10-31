# Gig: Nasty Hangover: scene presentation

Journal identity: `quests/street_stories/santo_domingo/arroyo/sts_std_arr_06`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_std_arr_06.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_06\scenes\sts_std_arr_06_holocall_debriefs.scene`

25 graph nodes, 33 edges; 2 event-bearing sections, 5 events; 5 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Rogue (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 316.

End nodes: 2: `<omitted>`; 316: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 30 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `5d8895eca659717ce55280390bd175217d8ebff5b7e30e678c4ae7007bc2361e`. Binary SHA-256: `82b44bde9e926b738a60cd116cdace5267a927676392730dcee13348faf71b62`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_06\scenes\sts_std_arr_06_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_06\scenes\sts_std_arr_06_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Rogue (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `e4cc94b4a67fa4d8b8c8a992b4a8e57ee802b53b58b133d8109e8db3a7689f85`. Binary SHA-256: `c34df95603fbdbfeded5a711f40eaa9b6f457b38adab8eaeed9fc0e23b09f345`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_06\scenes\sts_std_arr_06_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_06\scenes\sts_std_arr_06_scn.scene`

234 graph nodes, 345 edges; 18 event-bearing sections, 189 events; 60 screenplay lines, 9 screenplay options, 4 choice nodes.

Actors: Unknown (actor 0, findInContext); Karl_Ginsky (actor 1, community); Guard (actor 2, community); Azevedo (actor 3, community); Johnny (actor 4, spawnDespawn); Guard_2 (actor 5, community); Guard_3 (actor 6, community); car_ginsky (actor 7, community); car_avezado (actor 8, community); Player (actor 9, findInContext).

Entries: `phone call start` → 11; `Start 8` → 961; `meeting point start` → 53; `Start 7` → 756; `shard_preview` → 1030.

Exits: `End1` → 1400; `phone call end` → 14; `meeting point end` → 54.

End nodes: 14: `<omitted>`; 54: `<omitted>`; 1400: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 114 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/19` |
| `scnChangeIdleAnimEvent` | 10 | 114 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnDialogLineEvent` | 45 | 20 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 35 | 55 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 1143 / 1005 | `/Data/RootChunk/sceneGraph/Data/graph/144/Data/events/19` |
| `scnPlaySkAnimEvent` | 31 | 55 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsAttachPropToPerformer` | 3 | 142 / 182 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/22` |
| `scneventsAttachPropToWorld` | 1 | 142 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/23` |
| `scneventsDespawnEntityEvent` | 3 | 142 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/24` |
| `scneventsSetAnimFeatureEvent` | 2 | 1143 / 984 | `/Data/RootChunk/sceneGraph/Data/graph/144/Data/events/6` |
| `scneventsSocket` | 42 | 55 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 55 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/6` |
| `scneventsVFXDurationEvent` | 1 | 114 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/32` |
| `scneventsVFXEvent` | 5 | 114 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, gaze: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, entity_lifecycle: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state, mount_workspot, entity_lifecycle: 1
- skeletal_animation, audio: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state, mount_workspot, entity_lifecycle: 1

Raw SHA-256: `902a9b65b24933ddfbd5187b4520ca7e43108d5f0ce215e7674bea864aec43f1`. Binary SHA-256: `2a70f8517a3e4e14a858887208255af6c83d34f9c9021306e1ee2e9e856fc748`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\arroyo\sts_std_arr_06\scenes\sts_std_arr_06_scn.scene" --events
```

