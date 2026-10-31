# Ex-Factor: scene presentation

Journal identity: `quests/side_quest/sq026_02_maiko`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq026_02_maiko.md) · [All cinematic studies](../README.md)

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

## `base\quest\side_quests\sq026\scenes\sq026_04_maiko.scene`

290 graph nodes, 355 edges; 55 event-bearing sections, 488 events; 121 screenplay lines, 27 screenplay options, 14 choice nodes.

Actors: maiko (actor 0, spawnSet); judy (actor 1, spawnSet); johnny (actor 2, spawnSet); V (actor 3, findInContext).

Entries: `Start 6` → 2465; `deal` → 1; `wait` → 1895; `Start 5` → 2345; `office` → 1459.

Exits: `deal_clear` → 2; `reset` → 1636; `End 6` → 2385; `deal_complete` → 1281; `End 5` → 1994.

End nodes: 2: `<omitted>`; 1281: `NonTerminating`; 1636: `<omitted>`; 1994: `NonTerminating`; 2385: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 568 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnDialogLineEvent` | 114 | 568 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnGameplayTransitionEvent` | 5 | 1259 / 707 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/13` |
| `scnIKEvent` | 10 | 1259 / 698 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/5` |
| `scnLookAtEvent` | 128 | 568 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 90 | 568 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnUnmountEvent` | 5 | 1259 / 706 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/12` |
| `scneventsAttachPropToPerformer` | 8 | 660 / 170 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/6` |
| `scneventsAttachPropToWorld` | 9 | 568 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/8` |
| `scneventsDespawnEntityEvent` | 1 | 568 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsEquipItemToPerformer` | 7 | 660 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/17` |
| `scneventsSetAnimFeatureEvent` | 5 | 1259 / 704 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/11` |
| `scneventsSocket` | 94 | 568 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |
| `scneventsUnequipItemFromPerformer` | 7 | 660 / 206 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/22` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1337 / 790 | `/Data/RootChunk/sceneGraph/Data/graph/60/Data/events/5` |
| `scneventsVFXEvent` | 1 | 1182 / 665 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/20` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 12
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, gaze: 5
- speech: 5
- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 4
- speech, gaze: 3
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, entity_lifecycle: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1

Raw SHA-256: `cf56585c2e0c266bdc55d82d5f9721b6584c66817043be566555004c5b5aeed0`. Binary SHA-256: `f33b01afccb36747a106b184382a7d6fed12b2db100e228e7318a94b8cdb9a52`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_04_maiko.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_05a_leave.scene`

424 graph nodes, 520 edges; 69 event-bearing sections, 406 events; 133 screenplay lines, 20 screenplay options, 9 choice nodes.

Actors: judy (actor 0, spawnSet); johnny (actor 1, spawnDespawn); woodman (actor 2, spawnSet); van (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `to_ambush` → 1; `Start 6` → 2314; `to_van` → 20; `Start 7` → 2351; `Start 8` → 2357; `Start1` → 2374; `testdef_ambush` → 136.

Exits: `to_ambush_done` → 2; `to_van_done` → 27; `to_van_terminating` → 2161; `clear_ambush` → 1489; `run_off` → 2676.

End nodes: 2: `NonTerminating`; 27: `NonTerminating`; 1489: `<omitted>`; 2161: `<omitted>`; 2676: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 55 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnDialogLineEvent` | 117 | 55 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnGameplayTransitionEvent` | 10 | 659 / 301 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/7` |
| `scnIKEvent` | 20 | 659 / 294 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/1` |
| `scnLookAtEvent` | 61 | 247 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnPlaySkAnimEvent` | 68 | 55 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnPoseCorrectionEvent` | 4 | 828 / 647 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/7` |
| `scnUnmountEvent` | 10 | 659 / 300 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/6` |
| `scneventsEquipItemToPerformer` | 2 | 957 / 884 | `/Data/RootChunk/sceneGraph/Data/graph/120/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 10 | 659 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/5` |
| `scneventsSocket` | 95 | 55 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 2 | 957 / 886 | `/Data/RootChunk/sceneGraph/Data/graph/120/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 828 / 645 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 12
- speech: 9
- speech, skeletal_animation, socket_signal: 5
- speech, skeletal_animation: 5
- skeletal_animation, socket_signal: 5
- speech, gaze: 4
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, gaze, socket_signal: 3
- speech, socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- socket_signal: 2
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, animation_state: 1

Raw SHA-256: `6f7ee26e2ac24cd7add9d4b9b27bdd492928702e32c2afb19616b4be4f12b6ec`. Binary SHA-256: `56f324206d2bb78138f6844f4b0c750ea0653e09bee250244d851cbf58180e04`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_05a_leave.scene" --events
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

## `base\quest\side_quests\sq026\scenes\sq026_10_meetup.scene`

138 graph nodes, 155 edges; 16 event-bearing sections, 129 events; 25 screenplay lines, 7 screenplay options, 6 choice nodes.

Actors: judy (actor 0, spawnSet); johnny (actor 1, spawnDespawn); roxanne (actor 2, spawnSet); tom (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `wait` → 518; `Start 1` → 68.

Exits: `reset` → 373; `wait_clear` → 767; `clear` → 153; `wait_done` → 541; `progress` → 316.

End nodes: 153: `<omitted>`; 316: `NonTerminating`; 373: `<omitted>`; 541: `NonTerminating`; 767: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 20 | 71 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnGameplayTransitionEvent` | 4 | 95 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/14` |
| `scnIKEvent` | 8 | 95 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/9` |
| `scnLookAtEvent` | 39 | 71 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 26 | 71 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 4 | 95 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 4 | 95 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/12` |
| `scneventsSocket` | 24 | 71 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1

Raw SHA-256: `27fa9d54e631e3914bb0624dfdd3de4885268ad3e757fbb76854a6d1d11c95f0`. Binary SHA-256: `1f50548674459b0373dda38abb0a13b1c6e0e2b55711082ce4d18f2d9c997051`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_10_meetup.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_11_to_penthouse.scene`

107 graph nodes, 123 edges; 15 event-bearing sections, 72 events; 26 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: judy (actor 0, spawnSet); tom (actor 1, spawnSet); roxanne (actor 2, spawnSet); gunner_01 (actor 3, community); gunner_02 (actor 4, community); rifler_01 (actor 5, community); judy_holocall (actor 6, spawnSet); Player (actor 7, findInContext).

Entries: `recon` → 1; `Maintenance` → 506; `preparations` → 78; `Start 4` → 1998.

Exits: `recon_done` → 2; `preparations_done` → 79.

End nodes: 2: `NonTerminating`; 79: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 25 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 465 / 394 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/9` |
| `scnIKEvent` | 2 | 465 / 385 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/1` |
| `scnLookAtEvent` | 25 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 10 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 1 | 465 / 393 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 1 | 465 / 389 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/5` |
| `scneventsSocket` | 7 | 118 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, gaze: 3
- speech, gaze: 3
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1

Raw SHA-256: `773963fca1eb577a2e36d3aa7a3fcbca1decf084df81ddde3dd04bd14185a7a9`. Binary SHA-256: `066b43089f9e72dff7e097128da4c52c77aec59dc427ba7e92bb26aa4f7cc693`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_11_to_penthouse.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_12_penthouse_gameplay.scene`

51 graph nodes, 47 edges; 10 event-bearing sections, 40 events; 40 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: judy (actor 0, spawnSet); gunner_01 (actor 1, community); gunner_02 (actor 2, community); rifler_01 (actor 3, community); rifler_02 (actor 4, community); tom (actor 5, spawnDespawn); roxanne (actor 6, spawnDespawn); Player (actor 7, findInContext).

Entries: `elevator` → 1; `chat_exterior` → 4; `chat_main` → 7; `chat_preoffice` → 10; `status_update_01` → 13; `status_update_02` → 16; `status_update_03` → 19.

Exits: `elevator_done` → 2; `chat_exterior_done` → 5; `chat_main_done` → 8; `chat_preoffice_done` → 11; `status_update_01_done` → 14; `status_update_02_done` → 17; `status_update_03_done` → 20.

End nodes: 2: `<omitted>`; 5: `<omitted>`; 8: `<omitted>`; 11: `<omitted>`; 14: `<omitted>`; 17: `<omitted>`; 20: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 40 | 26 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10

Raw SHA-256: `888ade4fcad641f8ce99e1272e02c3177b782a2565d720439cb0811e24f3cd71`. Binary SHA-256: `5b156c2138aa05e23319ab54a61e34b34e88e1d3bedbcc43812b2fd3daa08f4c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_12_penthouse_gameplay.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_13_hiromi.scene`

479 graph nodes, 589 edges; 75 event-bearing sections, 601 events; 169 screenplay lines, 40 screenplay options, 17 choice nodes.

Actors: judy (actor 0, spawnSet); maiko (actor 1, spawnSet); hiromi (actor 2, community); tom (actor 3, spawnSet); roxanne (actor 4, spawnSet); boss_01 (actor 5, community); boss_02 (actor 6, community); Johnny (actor 7, spawnDespawn); doll_01 (actor 8, community); doll_02 (actor 9, community); doll_03 (actor 10, community); Player (actor 11, findInContext).

Entries: `meeting` → 1; `placeholder` → 1681; `girls_preview` → 2072.

Exits: `after_combat_maiko_alive` → 511; `maiko` → 157; `judy` → 162; `maiko_combat` → 282.

End nodes: 157: `<omitted>`; 162: `NonTerminating`; 282: `<omitted>`; 511: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 12 | 299 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/0` |
| `scnDialogLineEvent` | 133 | 15 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 11 | 475 / 641 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/24` |
| `scnIKEvent` | 22 | 475 / 634 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/18` |
| `scnLookAtEvent` | 128 | 15 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 1 | 870 / 903 | `/Data/RootChunk/sceneGraph/Data/graph/83/Data/events/2` |
| `scnPlaySkAnimEvent` | 109 | 15 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnUnmountEvent` | 11 | 475 / 640 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/23` |
| `scneventsAttachPropToPerformer` | 15 | 413 / 306 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/39` |
| `scneventsAttachPropToWorld` | 5 | 448 / 467 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/16` |
| `scneventsEquipItemToPerformer` | 10 | 413 / 246 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 11 | 475 / 636 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/20` |
| `scneventsSocket` | 118 | 15 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 2 | 413 / 300 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/33` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 413 / 305 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/38` |
| `scneventsVFXDurationEvent` | 1 | 907 / 943 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/4` |
| `scneventsVFXEvent` | 11 | 363 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 9
- speech, gaze: 7
- speech, skeletal_animation, gaze: 6
- skeletal_animation, socket_signal: 6
- speech: 5
- speech, skeletal_animation: 4
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze: 4
- skeletal_animation: 4
- skeletal_animation, props_equipment, socket_signal: 3
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze: 2
- speech, idle_animation, gaze: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1

Raw SHA-256: `36c48a478dadb0838300316e05ed0950ac0b9a8128e3885b88e8a1716bba8120`. Binary SHA-256: `aff390a98440a284e68f26cf0e3ff43ec2c1f160f8a4715337c5577668f79048`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_13_hiromi.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_13a_dolls.scene`

20 graph nodes, 19 edges; 1 event-bearing sections, 12 events; 0 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: roxanne (actor 0, spawnSet); tom (actor 1, spawnSet); security_01 (actor 2, community); security_02 (actor 3, community); security_03 (actor 4, community); security_04 (actor 5, community); dead1 (actor 6, spawnDespawn); dead2 (actor 7, spawnDespawn).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnLookAtEvent` | 3 | 105 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 4 | 105 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scneventsCameraEvent` | 1 | 105 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsCameraParamsEvent` | 1 | 105 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scneventsSocket` | 3 | 105 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze, camera, socket_signal: 1

Raw SHA-256: `c08df538ac0cfef88a1b4b92d6a009468d1f31c1bdde803d23db89030819463a`. Binary SHA-256: `3da17a89879364d9a63861bf88a987c21c1c4e84409c35ca15a5862c5ab04632`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_13a_dolls.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_14_leave.scene`

56 graph nodes, 62 edges; 4 event-bearing sections, 9 events; 9 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: judy (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `maiko` → 57; `judy` → 1.

Exits: `judy_done` → 2; `maiko_done` → 80.

End nodes: 2: `<omitted>`; 80: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 9 | 42 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `5b1cb1679b3a131233de5bcbeb602dc35c10f6b02e9074fb51ba7af51e8845d1`. Binary SHA-256: `d31b44d9efce084d0354927d38221f2fffb79119e2a7d131298684a38737245c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_14_leave.scene" --events
```

## `base\quest\side_quests\sq026\scenes\sq026_15_end.scene`

140 graph nodes, 167 edges; 34 event-bearing sections, 280 events; 66 screenplay lines, 17 screenplay options, 9 choice nodes.

Actors: judy (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `maiko` → 1; `judy` → 4.

Exits: `maiko_done` → 2; `judy_done` → 5; `clear` → 575; `judy_pissed` → 193.

End nodes: 2: `NonTerminating`; 5: `NonTerminating`; 193: `NonTerminating`; 575: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 24 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnDialogLineEvent` | 62 | 24 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scnGameplayTransitionEvent` | 10 | 53 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/10` |
| `scnIKEvent` | 20 | 53 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/4` |
| `scnLookAtEvent` | 32 | 29 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/6` |
| `scnPlaySkAnimEvent` | 64 | 24 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnUnmountEvent` | 10 | 53 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/9` |
| `scneventsCameraParamsEvent` | 2 | 206 / 468 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 10 | 53 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/8` |
| `scneventsSocket` | 63 | 24 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 2 | 123 / 328 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/5` |
| `scneventsVFXEvent` | 1 | 116 / 295 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 6
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- skeletal_animation: 1
- gaze: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `e8a0434bfbe4aea884121fd079c7a881667bda8e2fe2b54468e3ada0c4c6f2dc`. Binary SHA-256: `0379d823e4a6c86eaa64ebf11ae3e45a34044c342c443042c0190310a96a0f84`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq026\scenes\sq026_15_end.scene" --events
```

