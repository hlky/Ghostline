# Talkin' 'bout a Revolution: scene presentation

Journal identity: `quests/side_quest/sq026_03_pizza`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq026_03_pizza.md) · [All cinematic studies](../README.md)

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

## `base\quest\side_quests\sq026\scenes\sq026_08_plan.scene`

595 graph nodes, 706 edges; 104 event-bearing sections, 1165 events; 211 screenplay lines, 54 screenplay options, 26 choice nodes.

Actors: judy (actor 0, spawnSet); maiko (actor 1, spawnSet); tom (actor 2, spawnSet); roxanne (actor 3, spawnSet); johnny (actor 4, spawnDespawn); V (actor 5, findInContext).

Entries: `Start 0` → 1; `Start 5` → 2991; `Start 6` → 3068; `end` → 1162; `placeholder2` → 3227; `post_sparring` → 4225; `Start 9` → 3770; `Start1` → 4274; `sickness` → 4328; `Start 4` → 2932; `plan` → 1465.

Exits: `accept` → 1027; `refused_quest` → 1138.

End nodes: 1027: `<omitted>`; 1138: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1770 / 2258 | `/Data/RootChunk/sceneGraph/Data/graph/163/Data/events/4` |
| `scnChangeIdleAnimEvent` | 54 | 98 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 199 | 96 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 12 | 800 / 486 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/9` |
| `scnIKEvent` | 24 | 800 / 473 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scnLookAtAdvancedEvent` | 16 | 2030 / 2461 | `/Data/RootChunk/sceneGraph/Data/graph/187/Data/events/2` |
| `scnLookAtEvent` | 396 | 96 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnOverridePhantomParamsEvent` | 3 | 1646 / 1923 | `/Data/RootChunk/sceneGraph/Data/graph/141/Data/events/20` |
| `scnPlaySkAnimEvent` | 216 | 96 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnUnmountEvent` | 12 | 800 / 491 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/13` |
| `scneventsAttachPropToPerformer` | 5 | 1118 / 806 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/3` |
| `scneventsAttachPropToWorld` | 4 | 775 / 349 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/32` |
| `scneventsCameraParamsEvent` | 9 | 1646 / 1902 | `/Data/RootChunk/sceneGraph/Data/graph/141/Data/events/11` |
| `scneventsEquipItemToPerformer` | 4 | 775 / 331 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/16` |
| `scneventsSetAnimFeatureEvent` | 12 | 800 / 487 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/10` |
| `scneventsSocket` | 172 | 96 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 2 | 775 / 333 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/18` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1646 / 1927 | `/Data/RootChunk/sceneGraph/Data/graph/141/Data/events/24` |
| `scneventsVFXEvent` | 23 | 105 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/39` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 16
- speech: 13
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- speech, skeletal_animation, gaze: 10
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 4
- speech, skeletal_animation: 4
- camera: 4
- speech, skeletal_animation, idle_animation, gaze: 3
- speech, gaze: 3
- skeletal_animation, socket_signal: 3
- gaze: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, camera, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1

Raw SHA-256: `bd75a5a3b4589af10e5f0b4dc2fc0df5a734d1582b955789382374e4b543af6d`. Binary SHA-256: `984ea5b1abc0ce8abc93697d8b66e469633a36ed4a06ea4add0212357a63c829`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_08_plan.scene" --events
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

