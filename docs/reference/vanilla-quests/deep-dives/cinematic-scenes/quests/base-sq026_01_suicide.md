# Both Sides, Now: scene presentation

Journal identity: `quests/side_quest/sq026_01_suicide`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq026_01_suicide.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq026\scenes\sq026_00_holocall_judy.scene`

22 graph nodes, 21 edges; 2 event-bearing sections, 9 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: judy (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1; `Start 1` → 86.

Exits: `End 0` → 4.

End nodes: 4: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 2 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 4 | 2 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 1 | 2 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsCameraEvent` | 1 | 88 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 88 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsSocket` | 1 | 2 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal: 1
- camera: 1

Raw SHA-256: `7065f6a885b02d6a5bebd0ce83747fac73798b4a1e8d46414dbc3739582433e7`. Binary SHA-256: `b631dbfd1ab8bdd90ba6284f8405bee55818a47ab3b4e737a83680e307cc62df`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_00_holocall_judy.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_01a_suicide.scene`

200 graph nodes, 239 edges; 48 event-bearing sections, 320 events; 126 screenplay lines, 41 screenplay options, 14 choice nodes.

Actors: judy (actor 0, spawnSet); evelyn (actor 1, spawnSet); johnny (actor 2, spawnDespawn); Player (actor 3, findInContext).

Entries: `Start 0` → 1; `Start 1` → 555.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 123 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 171 / 339 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/9` |
| `scnIKEvent` | 4 | 171 / 330 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/1` |
| `scnLookAtEvent` | 34 | 8 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 71 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 2 | 171 / 338 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/8` |
| `scneventsEquipItemToPerformer` | 2 | 41 / 131 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scneventsMountEvent` | 1 | 450 / 654 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/15` |
| `scneventsRagdollEvent` | 1 | 453 / 678 | `/Data/RootChunk/sceneGraph/Data/graph/71/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 8 | 171 / 334 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/5` |
| `scneventsSetAnimsetWeight` | 10 | 450 / 636 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/1` |
| `scneventsSocket` | 49 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 41 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/24` |
| `scneventsVFXEvent` | 3 | 450 / 648 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 16
- speech, skeletal_animation, socket_signal: 9
- speech, skeletal_animation, gaze, socket_signal: 6
- speech: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, vfx, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal, animation_state, gameplay_action: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1
- gaze: 1
- vfx, socket_signal: 1

Raw SHA-256: `0cfccac7528ba81b28fcece4562cb99f4394d3a28021cfbdb7e91543d5e39715`. Binary SHA-256: `2ecaebf15cf88a61f325dd06e0b09401628b423156a3b06b06c5874a37a9078f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_01a_suicide.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_01b_roof.scene`

88 graph nodes, 104 edges; 28 event-bearing sections, 240 events; 62 screenplay lines, 14 screenplay options, 5 choice nodes.

Actors: judy (actor 0, spawnSet); johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `Start 4` → 493; `Start 5` → 504.

Exits: `End 1` → 108.

End nodes: 108: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 15 | 37 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 60 | 30 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 32 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/18` |
| `scnIKEvent` | 4 | 32 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnLookAtEvent` | 56 | 32 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 51 | 32 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPoseCorrectionEvent` | 4 | 208 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |
| `scnUnmountEvent` | 2 | 32 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/17` |
| `scneventsAttachPropToNode` | 1 | 323 / 371 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/11` |
| `scneventsAttachPropToPerformer` | 5 | 208 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/5` |
| `scneventsAttachPropToWorld` | 4 | 247 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/8` |
| `scneventsCameraParamsEvent` | 4 | 305 / 321 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 2 | 32 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/14` |
| `scneventsSocket` | 29 | 32 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsVFXEvent` | 1 | 526 / 574 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- gaze: 2
- speech: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, idle_animation, camera, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, gaze, camera, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- socket_signal: 1
- camera, vfx: 1

Raw SHA-256: `ee3653561a576838b78797afbbf3a13598c032a5a815acd38b7a1bdac5af6592`. Binary SHA-256: `c33c8f660ff5ac23b57f0e24a2ce7d2de3807a7b85934e1422f3b31dad1aeff5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_01b_roof.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_02_holocall_judy.scene`

51 graph nodes, 58 edges; 17 event-bearing sections, 60 events; 62 screenplay lines, 14 screenplay options, 5 choice nodes.

Actors: judy (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `Start 2` → 233; `after_refusal` → 150.

Exits: `accept` → 2; `refuse` → 33.

End nodes: 2: `<omitted>`; 33: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 57 | 5 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsCameraEvent` | 1 | 236 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 236 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/1` |
| `scneventsSocket` | 1 | 13 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, socket_signal: 1
- camera: 1

Raw SHA-256: `8eb4d0a7004cc4ba7e4e9cb4ad7bd461dfc5e5a3fa5fdaadc058d1a060708341`. Binary SHA-256: `0795a4fe8da673323650a28c25c423c47cbf729d959959048c2298b1db3f75ab`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_02_holocall_judy.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_07_judys.scene`

116 graph nodes, 138 edges; 18 event-bearing sections, 96 events; 46 screenplay lines, 15 screenplay options, 8 choice nodes.

Actors: judy (actor 0, spawnSet); tom (actor 1, spawnSet); johnny (actor 2, spawnDespawn); roxanne (actor 3, spawnSet); maiko (actor 4, spawnSet); V (actor 5, findInContext).

Entries: `apartment_exploration` → 1212; `wait` → 1257; `holocall` → 948.

Exits: `wait_clear` → 1564; `holocall_done` → 953; `wait_done` → 1301.

End nodes: 953: `<omitted>`; 1301: `NonTerminating`; 1564: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 141 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnDialogLineEvent` | 43 | 140 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 1263 / 264 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/6` |
| `scnIKEvent` | 2 | 1263 / 258 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/1` |
| `scnLookAtEvent` | 16 | 140 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnOverridePhantomParamsEvent` | 2 | 140 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnPlaySkAnimEvent` | 11 | 140 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnUnmountEvent` | 1 | 1263 / 263 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 1 | 1263 / 261 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/4` |
| `scneventsSocket` | 10 | 140 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `9d4016ef9ba7212e768fffe5233fe61870c9f7f4404629f20ffbd0a690bcd096`. Binary SHA-256: `b678b2d28405cb94717a693721a49de9adffc68acbfffe7e5800757a139ef865`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_07_judys.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_09_holocall_judy.scene`

16 graph nodes, 15 edges; 1 event-bearing sections, 8 events; 5 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: judy (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `rejected_out` → 255; `End 0` → 2.

End nodes: 2: `<omitted>`; 255: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 1 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSocket` | 1 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `107dd35c092df2aa39f63b80e5833a5e871311bc390a06cdc0727ab4b675bf09`. Binary SHA-256: `7c961df74b12d47388d62f93147d2e9b153fbf531bbdfddf1371ca2979344c94`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_09_holocall_judy.scene" --events
```

