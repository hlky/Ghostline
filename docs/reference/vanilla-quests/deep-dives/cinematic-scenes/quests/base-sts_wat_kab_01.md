# Gig: Concrete Cage Trap: scene presentation

Journal identity: `quests/street_stories/watson/kabuki/sts_wat_kab_01`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_kab_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_chat_003.scene`

16 graph nodes, 24 edges; 1 event-bearing sections, 14 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: enemy3 (actor 0, community); shopkeeper (actor 1, community).

Entries: `chat_start` → 1.

Exits: `chat_end` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 6 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 4 | 4 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 1

Raw SHA-256: `8ddda747c9c0400337f45c0e27b01dcb4d152f06fde511e1072bee5a9bac3101`. Binary SHA-256: `439d2a7fcb4c38c457e86a9132b882e0876d0a2c1e42951f1e8bc11c139c5d97`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_chat_003.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_chat_04.scene`

4 graph nodes, 4 edges; 1 event-bearing sections, 5 events; 5 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: civilian (actor 0, community); listener (actor 1, community).

Entries: `chat_04` → 1.

Exits: `chat_04_end` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `10fc0d36d1afc9b2d77228a129b7d8b1fa36f08803bd7ec5de95ddea56b90b35`. Binary SHA-256: `fbe284fd50c0ccbc3e670e91f90ad07372ce95684cf83c9d30614a43c34635ff`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_chat_04.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_chat_05.scene`

18 graph nodes, 21 edges; 1 event-bearing sections, 36 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: civilian_m (actor 0, community); civilian_f (actor 1, community).

Entries: `chat_05` → 1.

Exits: `chat_05_end` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 7 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 1 | 4 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/30` |
| `scnIKEvent` | 2 | 4 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/27` |
| `scnLookAtEvent` | 3 | 4 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnPlaySkAnimEvent` | 10 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 1 | 4 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/29` |
| `scneventsSetAnimFeatureEvent` | 1 | 4 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/25` |
| `scneventsSocket` | 11 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `7315ce15e50077afaed7bed0aea9bcb4aba6d77660452d5c6c7c35797730dd9e`. Binary SHA-256: `d825972cc6be5442249f9236138037c87d9ec03ce32cb6396e03e4ee7cef4c3d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_chat_05.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_dirtboys.scene`

78 graph nodes, 97 edges; 17 event-bearing sections, 145 events; 39 screenplay lines, 7 screenplay options, 4 choice nodes.

Actors: dirtboy_01 (actor 0, community); dirtboy_02 (actor 1, community); Player (actor 2, findInContext).

Entries: `dirtboys` → 1.

Exits: `dirtboys_end` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 35 | 7 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnLookAtEvent` | 42 | 7 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 25 | 7 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsEquipItemToPerformer` | 4 | 23 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/13` |
| `scneventsSocket` | 33 | 7 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsUnequipItemFromPerformer` | 2 | 23 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/19` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 10 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scneventsVFXDurationEvent` | 2 | 39 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 6
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, gaze: 2
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- gaze: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- socket_signal: 1
- speech: 1

Raw SHA-256: `7a1f65ef99d8bae4ef25db1ddeed1f1d21300a59367f6fbd89fe61d138d6df20`. Binary SHA-256: `fde35697ae23d77ef40a60a20546a08eb4587a3861f01a200b5214dbce29ce33`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_dirtboys.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_holocall_debriefs.scene`

25 graph nodes, 33 edges; 2 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 286.

End nodes: 2: `<omitted>`; 286: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 28 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `4e58f663691b93cf2bde604053192a86f222099197fcefb385dd28529725d3c8`. Binary SHA-256: `4d7333f7698ac07362826bc0ad9d316a1d91d5c9c5431e274457ae75ddea9bf6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 9 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start1` → 69.

Exits: `End1` → 70; `rejected_out` → 260.

End nodes: 70: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 26 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnLookAtEvent` | 1 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 6 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 1

Raw SHA-256: `945854fa5f9c380961120d6db6a54a2d270272baa5238323795982de203364e6`. Binary SHA-256: `0f9d6dd494592364449cd6a88b69a995084af851524007a59a0e44d482c82275`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_tiny_mike.scene`

118 graph nodes, 148 edges; 25 event-bearing sections, 116 events; 43 screenplay lines, 9 screenplay options, 4 choice nodes.

Actors: tiny_mike (actor 0, community); V (actor 1, findInContext).

Entries: `welcome` → 1; `Start 6` → 339; `Start 9` → 719; `main_start` → 349; `disconnected_lines` → 375.

Exits: `welcome_end` → 2; `interrupted_by_combat` → 959; `End 8` → 727; `End 7` → 376.

End nodes: 2: `NonTerminating`; 376: `<omitted>`; 727: `<omitted>`; 959: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 187 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |
| `scnChangeIdleAnimEvent` | 5 | 187 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/8` |
| `scnDialogLineEvent` | 32 | 136 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 429 / 269 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/18` |
| `scnIKEvent` | 2 | 429 / 260 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/10` |
| `scnLookAtEvent` | 14 | 181 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnPlaySkAnimEvent` | 28 | 181 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 187 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/22` |
| `scnUnmountEvent` | 1 | 429 / 268 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/17` |
| `scneventsAttachPropToNode` | 1 | 187 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/17` |
| `scneventsAttachPropToPerformer` | 2 | 187 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 1 | 429 / 264 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/14` |
| `scneventsSocket` | 23 | 181 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scneventsVFXDurationEvent` | 1 | 429 / 249 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation: 4
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, animation_state: 1
- idle_animation, socket_signal: 1
- gaze: 1

Raw SHA-256: `c61e2b84f9f9d1918b48a5a69c2d005aaa7f338d43197cfee8e101d8ad4fc9cd`. Binary SHA-256: `78fb0308a70cc16650bea1baae9a89dfd61a82553751e897abbf0af12b02e5c3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_tiny_mike.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_tiny_mike_ground_floor.scene`

74 graph nodes, 90 edges; 21 event-bearing sections, 43 events; 33 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: tiny_mike (actor 0, community); V (actor 1, findInContext).

Entries: `ground_floor` → 282; `attacked` → 378; `ground_floor_new` → 398.

Exits: `ground_floor_end` → 350; `ground_floor_new_end` → 441.

End nodes: 350: `<omitted>`; 441: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 28 | 283 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 4 | 428 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/2` |
| `scnPlaySkAnimEvent` | 5 | 511 / 247 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/0` |
| `scneventsSocket` | 6 | 428 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- skeletal_animation, socket_signal: 3
- skeletal_animation: 2
- speech, gaze, socket_signal: 1
- speech, socket_signal: 1
- speech, gaze: 1

Raw SHA-256: `f862400128ad5279c1fd2e09209e326e5bf9372ef12f68e827357840bd781114`. Binary SHA-256: `894f446429f93232543f69ec27d291dae45e8e7fbb67e4568c099282d687ddda`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_tiny_mike_ground_floor.scene" --events
```

## `base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_tiny_mike_restaurant.scene`

87 graph nodes, 95 edges; 15 event-bearing sections, 121 events; 37 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: tiny_mike (actor 0, community); vehicle (actor 1, community); V (actor 2, findInContext).

Entries: `restaurant_door` → 53; `default dialogue farewell` → 417; `Start 8` → 600.

Exits: `FinishEnd` → 21; `clear` → 764; `default dialogzue farewell exit` → 421.

End nodes: 21: `NonTerminating`; 421: `<omitted>`; 764: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 330 / 138 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/8` |
| `scnChangeIdleAnimEvent` | 5 | 330 / 132 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scnDialogLineEvent` | 26 | 22 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayActionEvent` | 4 | 330 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 239 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/10` |
| `scnIKEvent` | 6 | 239 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnLookAtEvent` | 16 | 22 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlaySkAnimEvent` | 16 | 22 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scnPoseCorrectionEvent` | 4 | 330 / 142 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/12` |
| `scnUnmountEvent` | 3 | 239 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 8 | 22 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsSocket` | 25 | 22 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, skeletal_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `a3e38907adc37b61be12f057cc91a726eb57990430dd806b58d1d5edf51c95c9`. Binary SHA-256: `981faf7cf6a2d483966b53afe3fdc45b1337496e746c0afe6974279d5e4bc24a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\kabuki\sts_wat_kab_01\scenes\sts_wat_kab_01_tiny_mike_restaurant.scene" --events
```

