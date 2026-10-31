# Pyramid Song: scene presentation

Journal identity: `quests/side_quest/sq030_judy_romance`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq030_judy_romance.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\holocalls\judy\judy_holocall.scene`

203 graph nodes, 230 edges; 2 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: judy (actor 0, spawnSet).

Entries: `holo_judy_calls_v_start` → 4; `holo_judy_calls_v_end` → 6; `holo_v_calls_judy_start` → 7; `holo_v_calls_judy_end` → 8; `audio_judy_calls_v_start` → 476; `audio_judy_calls_v_end` → 478; `audio_v_calls_judy_start` → 479; `audio_v_calls_judy_end` → 480.

Exits: `holo_judy_out` → 5; `audio_judy_out` → 477; `holo_judy_out_non` → 594.

End nodes: 5: `<omitted>`; 477: `<omitted>`; 594: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnLookAtEvent` | 2 | 65 / 303 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2

Raw SHA-256: `64ebc3e0ecb477b554a57fcdd003f671dc22ed11654b05a874a0bd1eeb3f5432`. Binary SHA-256: `53269b5e9eb17d056fee2730aad93cea84278e6e1caef145c76b16083ac01637`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\holocalls\judy\judy_holocall.scene" --events
```

## `base\quest\secondary_characters\default_dialogues\judy_default.scene`

281 graph nodes, 361 edges; 53 event-bearing sections, 438 events; 122 screenplay lines, 44 screenplay options, 15 choice nodes.

Actors: Judy (actor 0, spawnSet); Judy_holocall (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `in` → 1; `holocall_in` → 1326; `sq030_lake` → 1570; `q105_cardrive` → 594.

Exits: `out` → 2; `holocall_out` → 1331; `sq030_lake_done` → 1568; `holo_to_ftf_out` → 1380; `q105_cardrive_done` → 595.

End nodes: 2: `<omitted>`; 595: `<omitted>`; 1331: `<omitted>`; 1380: `NonTerminating`; 1568: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 77 | 50 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnDialogLineEvent` | 115 | 47 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 268 / 429 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/7` |
| `scnIKEvent` | 2 | 268 / 420 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/3` |
| `scnLookAtEvent` | 65 | 47 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 94 | 47 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 1 | 268 / 435 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 1 | 268 / 431 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/9` |
| `scneventsSocket` | 82 | 47 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 28
- speech, idle_animation, socket_signal: 6
- speech, idle_animation: 4
- gaze: 4
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze, socket_signal: 1
- idle_animation, gaze: 1

Raw SHA-256: `371fe7fc185c757fdf76e62236678a1f9f25e65c62d1a849b496119cfc02a306`. Binary SHA-256: `fba396f17b3d174d22ff82bf5d67ef71cd342dd44f4bee1fc2611ec392f746f6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\secondary_characters\default_dialogues\judy_default.scene" --events
```

## `base\quest\side_quests\sq030\scenes\sq030_00_holocall.scene`

56 graph nodes, 68 edges; 23 event-bearing sections, 70 events; 56 screenplay lines, 14 screenplay options, 5 choice nodes.

Actors: Judy (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1; `Start 1` → 366.

Exits: `accept` → 2; `refuse` → 249.

End nodes: 2: `<omitted>`; 249: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 141 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 55 | 141 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 1 | 485 / 269 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/0` |
| `scnPlaySkAnimEvent` | 6 | 144 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scneventsSocket` | 1 | 237 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, idle_animation: 4
- speech, skeletal_animation: 4
- speech, skeletal_animation, idle_animation: 2
- speech, socket_signal: 1
- gaze: 1

Raw SHA-256: `a41f99034b571b047c585f4b8e717d14c16d3f658902a0d35dbcae7b27c3dc90`. Binary SHA-256: `02f5a6ca1f0327b4704da132ea32999767003bad10ed0ea61bb8280f097da049`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq030\scenes\sq030_00_holocall.scene" --events
```

## `base\quest\side_quests\sq030\scenes\sq030_01_dam_meetup.scene`

153 graph nodes, 201 edges; 26 event-bearing sections, 220 events; 59 screenplay lines, 14 screenplay options, 7 choice nodes.

Actors: Judy (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `Start 0` → 1; `Start 3` → 962; `wait` → 523.

Exits: `accept` → 2; `content_block_loop` → 950; `loop_break` → 970; `wait_clear` → 879; `refuse` → 434; `refuse_done` → 907; `wait_done` → 564.

End nodes: 2: `NonTerminating`; 434: `NonTerminating`; 564: `NonTerminating`; 879: `<omitted>`; 907: `NonTerminating`; 950: `NonTerminating`; 970: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 112 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/11` |
| `scnChangeIdleAnimEvent` | 8 | 11 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scnDialogLineEvent` | 49 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 11 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/11` |
| `scnIKEvent` | 10 | 11 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnLookAtEvent` | 34 | 11 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/13` |
| `scnOverridePhantomParamsEvent` | 2 | 191 / 205 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnPlaySkAnimEvent` | 40 | 11 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 5 | 11 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scneventsCameraParamsEvent` | 8 | 11 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 5 | 11 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsSocket` | 51 | 11 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- camera: 3
- skeletal_animation, socket_signal: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1

Raw SHA-256: `6c25de09a3e6c48dfceab15e51924378f6e21e73b979e039b0f243cdc1512cf9`. Binary SHA-256: `8f77e0593bc23dd4eb619003c8cd515698c8448f3429a8235433869ed47cc33e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq030\scenes\sq030_01_dam_meetup.scene" --events
```

## `base\quest\side_quests\sq030\scenes\sq030_03_dam_equipment.scene`

131 graph nodes, 157 edges; 24 event-bearing sections, 126 events; 54 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Judy (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1; `refused_dam` → 1050; `refused` → 300.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 513 / 274 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/2` |
| `scnChangeIdleAnimEvent` | 3 | 513 / 288 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/6` |
| `scnDialogLineEvent` | 42 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 1079 / 781 | `/Data/RootChunk/sceneGraph/Data/graph/123/Data/events/6` |
| `scnIKEvent` | 2 | 1079 / 775 | `/Data/RootChunk/sceneGraph/Data/graph/123/Data/events/1` |
| `scnLookAtEvent` | 38 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 17 | 83 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/6` |
| `scnUnmountEvent` | 1 | 1079 / 780 | `/Data/RootChunk/sceneGraph/Data/graph/123/Data/events/5` |
| `scneventsAttachPropToPerformer` | 3 | 513 / 289 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/7` |
| `scneventsAttachPropToWorld` | 1 | 513 / 294 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 1 | 1079 / 778 | `/Data/RootChunk/sceneGraph/Data/graph/123/Data/events/4` |
| `scneventsSocket` | 16 | 83 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 8
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze: 4
- speech: 3
- skeletal_animation, idle_animation, socket_signal: 2
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `70dcdaae77a01782b797576f7644f3708360bf604aba78aa15610788039f827f`. Binary SHA-256: `ea067accbd0b8c5d1b32ce7136f79801fa5a3fa71e3d8db594fa50d0038db151`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq030\scenes\sq030_03_dam_equipment.scene" --events
```

## `base\quest\side_quests\sq030\scenes\sq030_04_lake_dive_start.scene`

35 graph nodes, 44 edges; 9 event-bearing sections, 42 events; 20 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: Judy (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1; `outdated` → 228.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 16 | 12 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 3 | 257 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/12` |
| `scnPlaySkAnimEvent` | 13 | 257 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scneventsSocket` | 9 | 257 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scneventsVFXEvent` | 1 | 270 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `706cfc5ef08ebcb5d998288e9b291b000d5a83a24c02bd786de5d824f9b26860`. Binary SHA-256: `d84d4d8424a7fd363257c15808cc8e0d1b5b5290e66eb56ec5380b09f8fd59e2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq030\scenes\sq030_04_lake_dive_start.scene" --events
```

## `base\quest\side_quests\sq030\scenes\sq030_05_lake_test.scene`

176 graph nodes, 233 edges; 46 event-bearing sections, 160 events; 72 screenplay lines, 18 screenplay options, 7 choice nodes.

Actors: Judy (actor 0, spawnSet); Johnny (actor 1, spawnSet); sq030_crane (actor 2, community); V (actor 3, findInContext).

Entries: `Start 0` → 1; `romance` → 227; `warning_02` → 970; `Start 3` → 980; `warning_01` → 870; `blend_to_swim_test` → 1241.

Exits: `explore` → 2; `warning_02_done` → 973; `warning_01_done` → 873.

End nodes: 2: `NonTerminating`; 873: `NonTerminating`; 973: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 60 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnDialogLineEvent` | 72 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 587 / 323 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/4` |
| `scnIKEvent` | 4 | 587 / 320 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/1` |
| `scnLookAtEvent` | 22 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 22 | 587 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/0` |
| `scnUnmountEvent` | 2 | 587 / 328 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 5 | 587 / 324 | `/Data/RootChunk/sceneGraph/Data/graph/56/Data/events/5` |
| `scneventsSocket` | 19 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 6 | 786 / 587 | `/Data/RootChunk/sceneGraph/Data/graph/95/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 23
- speech, gaze: 4
- speech, gaze, socket_signal: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation: 2
- gaze: 2
- speech, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `faf215e64749d0b5907dd0daf0aed6e4fefcb3fc3b1345e233f79af3a51afeff`. Binary SHA-256: `feaddac1b8664b6558d859ab6cc5c1e1964d0c03c0a1be8965de0e3f347986a4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq030\scenes\sq030_05_lake_test.scene" --events
```

## `base\quest\side_quests\sq030\scenes\sq030_06_lake_exploration.scene`

481 graph nodes, 644 edges; 66 event-bearing sections, 327 events; 172 screenplay lines, 40 screenplay options, 22 choice nodes.

Actors: Judy (actor 0, spawnSet); johnny (actor 1, spawnSet); memory_kid_m_01 (actor 2, spawnDespawn); memory_kid_f_01 (actor 3, spawnDespawn); memory_grandmother (actor 4, spawnDespawn); memory_kid_m_02 (actor 5, spawnDespawn); memory_kid_f_02 (actor 6, spawnDespawn); V (actor 7, findInContext).

Entries: `Start 0` → 1; `warning_02` → 4408; `Start 5` → 4591; `Start 6` → 4593; `warning_01` → 3579.

Exits: `End 1` → 1260; `warning_02_done` → 4409; `warning_01_done` → 3582.

End nodes: 1260: `<omitted>`; 3582: `<omitted>`; 4409: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 3878 / 1618 | `/Data/RootChunk/sceneGraph/Data/graph/227/Data/events/23` |
| `scnDialogLineEvent` | 135 | 735 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 31 | 1545 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scnPlaySkAnimEvent` | 57 | 1545 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnPoseCorrectionEvent` | 1 | 3833 / 1354 | `/Data/RootChunk/sceneGraph/Data/graph/217/Data/events/12` |
| `scneventsAttachPropToPerformer` | 11 | 3218 / 766 | `/Data/RootChunk/sceneGraph/Data/graph/129/Data/events/1` |
| `scneventsAttachPropToWorld` | 11 | 3218 / 774 | `/Data/RootChunk/sceneGraph/Data/graph/129/Data/events/5` |
| `scneventsSocket` | 56 | 1545 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scneventsVFXEvent` | 24 | 2318 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 38
- speech, socket_signal: 9
- speech, gaze: 5
- speech, skeletal_animation, gaze, socket_signal: 3
- gaze: 3
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, props_equipment, vfx, socket_signal: 1
- skeletal_animation, props_equipment, vfx, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1

Raw SHA-256: `2218a8e354aefad965250f46cb1a545c16b4fe93986193ba0148bbda62c17bfe`. Binary SHA-256: `f59a872ccaad8c49877b928a433b469902155a33d5aff79891ba1bd953f1d9ff`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq030\scenes\sq030_06_lake_exploration.scene" --events
```

## `base\quest\side_quests\sq030\scenes\sq030_09_pier.scene`

400 graph nodes, 469 edges; 96 event-bearing sections, 606 events; 225 screenplay lines, 61 screenplay options, 19 choice nodes.

Actors: Judy (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); EVELYN (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `Start 11` → 2870; `no_race` → 103; `pier` → 110; `Start 9` → 2138; `PLACEHOLDER_1` → 2223; `PLACEHOLDER_2` → 2224; `PLACEHOLDER_3` → 2228; `Start 7` → 1817; `race_v` → 401; `race_judy` → 402.

Exits: `stay` → 101; `left_before_morning` → 1541; `sex end` → 753; `no_stay` → 759.

End nodes: 101: `Terminating`; 753: `NonTerminating`; 759: `NonTerminating`; 1541: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 55 | 155 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnChangeIdleAnimEvent` | 31 | 155 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 137 | 155 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 6 | 155 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/11` |
| `scnIKEvent` | 12 | 155 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnLookAtEvent` | 70 | 156 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnOverridePhantomParamsEvent` | 1 | 678 / 247 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/6` |
| `scnPlayRidAnimEvent` | 9 | 2680 / 2211 | `/Data/RootChunk/sceneGraph/Data/graph/296/Data/events/2` |
| `scnPlaySkAnimEvent` | 122 | 155 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnUnmountEvent` | 6 | 155 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scneventsAttachPropToNode` | 2 | 631 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scneventsAttachPropToPerformer` | 1 | 1760 / 1439 | `/Data/RootChunk/sceneGraph/Data/graph/177/Data/events/7` |
| `scneventsAttachPropToWorld` | 2 | 1828 / 1497 | `/Data/RootChunk/sceneGraph/Data/graph/185/Data/events/6` |
| `scneventsCameraParamsEvent` | 8 | 155 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scneventsPlayRidCameraAnimEvent` | 8 | 2680 / 2227 | `/Data/RootChunk/sceneGraph/Data/graph/296/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 6 | 155 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsSocket` | 101 | 155 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsVFXDurationEvent` | 3 | 1227 / 707 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/5` |
| `scneventsVFXEvent` | 26 | 2204 / 2148 | `/Data/RootChunk/sceneGraph/Data/graph/282/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 21
- speech, skeletal_animation, gaze, socket_signal: 8
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech, skeletal_animation: 6
- speech, gaze: 4
- speech, skeletal_animation, gaze: 4
- vfx: 4
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, audio: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, idle_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, props_equipment: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- speech, gaze, props_equipment, socket_signal: 1
- skeletal_animation, camera, audio: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, rid_actor, camera, rid_camera, audio, vfx, socket_signal: 1
- skeletal_animation, rid_actor, camera, rid_camera, audio, vfx, socket_signal: 1
- skeletal_animation, rid_actor, camera, rid_camera, audio, vfx: 1
- idle_animation, gaze, socket_signal: 1

Raw SHA-256: `1eaa56654a65548ad2bc861524a95fdf52e941a2fafce8c6b5bc38e931361e13`. Binary SHA-256: `d5d2f12f679528a7b2f34981fae645c40ec1d0c4af633784aa1d885f7295a073`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq030\scenes\sq030_09_pier.scene" --events
```

## `base\quest\side_quests\sq030\scenes\sq030_11_morning.scene`

140 graph nodes, 161 edges; 35 event-bearing sections, 249 events; 89 screenplay lines, 22 screenplay options, 12 choice nodes.

Actors: Judy (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `Start 0` → 1; `clothes_bedroom` → 682; `clothes_outside` → 683.

Exits: `friendship` → 2; `romance` → 43; `broken_friendship` → 408; `clothes_bedroom_done` → 686; `clothes_outside_done` → 689.

End nodes: 2: `NonTerminating`; 43: `NonTerminating`; 408: `NonTerminating`; 686: `<omitted>`; 689: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 381 / 421 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/2` |
| `scnChangeIdleAnimEvent` | 8 | 117 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/9` |
| `scnDialogLineEvent` | 76 | 94 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |
| `scnGameplayTransitionEvent` | 5 | 348 / 364 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/13` |
| `scnIKEvent` | 10 | 348 / 344 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/1` |
| `scnLookAtEvent` | 32 | 94 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnPlaySkAnimEvent` | 44 | 94 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/9` |
| `scnUnmountEvent` | 5 | 348 / 363 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/12` |
| `scneventsAttachPropToNode` | 2 | 126 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/8` |
| `scneventsAttachPropToPerformer` | 3 | 94 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scneventsAttachPropToWorld` | 5 | 117 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/2` |
| `scneventsCameraParamsEvent` | 2 | 629 / 704 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 348 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/9` |
| `scneventsSocket` | 39 | 94 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |
| `scneventsVFXEvent` | 2 | 629 / 710 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze: 3
- speech: 3
- skeletal_animation, audio, socket_signal: 3
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, gaze: 2
- speech, gaze: 2
- skeletal_animation, camera, audio, vfx: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `e47292471f5c9054af7927a1c0dd3f0b72959419f20bb981c810d020a729e34b`. Binary SHA-256: `cafeac069c24f55df7199d97f656d721c0298fefcae45c44386a3bfd2231a1d3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq030\scenes\sq030_11_morning.scene" --events
```

