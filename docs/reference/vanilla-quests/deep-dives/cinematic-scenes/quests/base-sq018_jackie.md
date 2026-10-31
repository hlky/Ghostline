# Heroes: scene presentation

Journal identity: `quests/side_quest/sq018_jackie`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq018_jackie.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq018\scenes\sq018_00_mama_welles_holocall.scene`

55 graph nodes, 69 edges; 14 event-bearing sections, 40 events; 35 screenplay lines, 8 screenplay options, 3 choice nodes.

Actors: mama_welles (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `in` → 1.

Exits: `out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 34 | 157 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scnLookAtEvent` | 1 | 465 / 336 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/1` |
| `scneventsSocket` | 5 | 157 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, socket_signal: 4
- gaze, socket_signal: 1

Raw SHA-256: `21c3ef0b093eeb0d09bce73544cc18845ae3eb534e388f4ffb2dbcd74d8fe9af`. Binary SHA-256: `9c272d6c2b540f8fff863ba35afd6f38e59e3e9ee8c5a163f0efa17a9fad6dd5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq018\scenes\sq018_00_mama_welles_holocall.scene" --events
```

## `base\quest\side_quests\sq018\scenes\sq018_01_mama_welles.scene`

153 graph nodes, 202 edges; 34 event-bearing sections, 239 events; 70 screenplay lines, 10 screenplay options, 6 choice nodes.

Actors: Mama_Welles (actor 0, spawnSet); Pepe (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `in` → 1.

Exits: `out` → 37; `out_kill_scene` → 424.

End nodes: 37: `NonTerminating`; 424: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 12 | 31 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnDialogLineEvent` | 59 | 11 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 234 / 227 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/10` |
| `scnIKEvent` | 6 | 234 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/2` |
| `scnLookAtEvent` | 28 | 31 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 45 | 31 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/8` |
| `scnUnmountEvent` | 3 | 234 / 232 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/14` |
| `scneventsAttachPropToPerformer` | 7 | 31 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/17` |
| `scneventsAttachPropToWorld` | 6 | 31 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/19` |
| `scneventsCameraParamsEvent` | 3 | 818 / 852 | `/Data/RootChunk/sceneGraph/Data/graph/104/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 3 | 234 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/11` |
| `scneventsSocket` | 62 | 11 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsVFXEvent` | 2 | 489 / 529 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation: 2
- skeletal_animation, socket_signal: 2
- camera: 2
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- vfx: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `1f8812b45c4986a46645b2ecb7f2527564bb96349db11ddbd8c04db472ac8d12`. Binary SHA-256: `6a338861cd0a49783d4104e97a21ed4e275aa1b58a7b2259e04e8c12ea1ba37d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq018\scenes\sq018_01_mama_welles.scene" --events
```

## `base\quest\side_quests\sq018\scenes\sq018_02_storage.scene`

494 graph nodes, 744 edges; 83 event-bearing sections, 463 events; 191 screenplay lines, 36 screenplay options, 29 choice nodes.

Actors: Misty (actor 0, spawnSet); motorcycle (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `in` → 40; `Start1` → 2802; `in_garage` → 2119.

Exits: `out_clean_up` → 895; `out` → 336.

End nodes: 336: `NonTerminating`; 895: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 479 / 350 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/2` |
| `scnChangeIdleAnimEvent` | 12 | 42 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 168 | 42 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 932 / 737 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/6` |
| `scnIKEvent` | 2 | 932 / 732 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/1` |
| `scnLookAtEvent` | 108 | 42 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 63 | 254 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 447 / 310 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/9` |
| `scnUnmountEvent` | 1 | 932 / 742 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/10` |
| `scneventsAttachPropToNode` | 2 | 479 / 360 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/7` |
| `scneventsAttachPropToPerformer` | 2 | 479 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/3` |
| `scneventsCameraParamsEvent` | 4 | 901 / 703 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 1 | 932 / 738 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/7` |
| `scneventsSocket` | 94 | 42 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 21
- speech, skeletal_animation, gaze, socket_signal: 12
- speech, gaze: 11
- speech, gaze, socket_signal: 7
- skeletal_animation, socket_signal: 5
- skeletal_animation: 4
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, socket_signal: 3
- speech, idle_animation, gaze, socket_signal: 2
- camera: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, idle_animation: 1
- socket_signal, animation_state: 1

Raw SHA-256: `6624c388535ea2a16e8119c670f3042f9f70ebca22108c53faced76d15ddcb56`. Binary SHA-256: `c3c7aa37544f57080dfbce3043d6d649783d7401cc888d600c373c268c69f076`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq018\scenes\sq018_02_storage.scene" --events
```

## `base\quest\side_quests\sq018\scenes\sq018_03_funeral.scene`

359 graph nodes, 431 edges; 65 event-bearing sections, 528 events; 111 screenplay lines, 23 screenplay options, 10 choice nodes.

Actors: Mama_Welles (actor 0, spawnSet); Victor_Vector (actor 1, spawnSet); Padre (actor 2, spawnSet); Misty (actor 3, spawnSet); ma_ganger_01_talking (actor 4, community); ma_ganger_02 (actor 5, community); elcoyote_barman (actor 6, spawnSet); ma_ganger_03 (actor 7, community); fa_ganger_01 (actor 8, community); fa_ganger_02 (actor 9, community); rey_gustavo (actor 10, community); rey_gustavo_girlfriend (actor 11, community); gle_bouncer (actor 12, community); gle_dad (actor 13, community); gle_mom (actor 14, community); rey_01_ma_friend_01 (actor 15, community); rey_01_ma_friend_02 (actor 16, community); V (actor 17, findInContext).

Entries: `in_before` → 1; `preview` → 1882.

Exits: `out_ceremony` → 2; `Valentinos_out` → 2439; `out_optional_scenes` → 813.

End nodes: 2: `NonTerminating`; 813: `NonTerminating`; 2439: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 329 / 316 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/4` |
| `scnChangeIdleAnimEvent` | 18 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 90 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 10 | 196 / 204 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/9` |
| `scnIKEvent` | 20 | 196 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnLookAtEvent` | 141 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 94 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPoseCorrectionEvent` | 4 | 142 / 121 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnUnmountEvent` | 10 | 196 / 211 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/15` |
| `scneventsAttachPropToNode` | 3 | 136 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/12` |
| `scneventsAttachPropToPerformer` | 14 | 301 / 247 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/6` |
| `scneventsAttachPropToWorld` | 6 | 142 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/24` |
| `scneventsEquipItemToPerformer` | 1 | 1022 / 893 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 10 | 196 / 207 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/12` |
| `scneventsSocket` | 94 | 4 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsVFXEvent` | 12 | 329 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 5
- speech, idle_animation: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, props_equipment, socket_signal: 3
- speech, idle_animation, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze: 2
- skeletal_animation, gaze, socket_signal: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, socket_signal, animation_state: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1
- vfx: 1
- skeletal_animation: 1
- gaze, socket_signal: 1

Raw SHA-256: `c8dd34d720a40d2414a2bade84252f4169a1b64ffa58e04ef93bca01658689b8`. Binary SHA-256: `f9fb4978219a4cb589edd0a97681b4b8ad6bddf2295450f9d6b4ab103ea97b5a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq018\scenes\sq018_03_funeral.scene" --events
```

## `base\quest\side_quests\sq018\scenes\sq018_03a_misty.scene`

61 graph nodes, 68 edges; 10 event-bearing sections, 58 events; 26 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: Misty (actor 0, spawnSet); Mama_Welles (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `in_after_ofrenda` → 291; `in_chat_on_the_way` → 249; `in` → 204; `in_misty_stayed` → 314.

Exits: `out_misty_stayed` → 469; `out_after_ofrenda` → 363; `out` → 259; `out_el_coyote` → 207.

End nodes: 207: `<omitted>`; 259: `<omitted>`; 363: `<omitted>`; 469: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 25 | 205 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 552 / 342 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/10` |
| `scnIKEvent` | 2 | 552 / 332 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/1` |
| `scnLookAtEvent` | 7 | 205 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 9 | 205 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnUnmountEvent` | 1 | 552 / 341 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 1 | 552 / 337 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/6` |
| `scneventsSocket` | 12 | 235 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, skeletal_animation, socket_signal: 2
- speech, gaze: 2
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `0a13478263a3fb8f6b64f6cceaffbbdf45bc8a6edbb9108eb756d3ebc4105cf1`. Binary SHA-256: `04028c9e99bc2782c3d1a4ad72af665bc47400f1cb1d62965794270209a7ff45`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq018\scenes\sq018_03a_misty.scene" --events
```

## `base\quest\side_quests\sq018\scenes\sq018_03b_victor.scene`

44 graph nodes, 55 edges; 10 event-bearing sections, 88 events; 18 screenplay lines, 5 screenplay options, 4 choice nodes.

Actors: Victor_Vector (actor 0, spawnSet); barman (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `in` → 1.

Exits: `out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 13 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 51 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/7` |
| `scnIKEvent` | 4 | 51 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scnLookAtEvent` | 16 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 8 | 51 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnUnmountEvent` | 2 | 51 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/11` |
| `scneventsAttachPropToNode` | 1 | 76 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/9` |
| `scneventsAttachPropToPerformer` | 5 | 60 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scneventsAttachPropToWorld` | 4 | 60 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/11` |
| `scneventsCameraParamsEvent` | 5 | 51 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 2 | 51 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/8` |
| `scneventsSocket` | 24 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsVFXEvent` | 2 | 60 / 98 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- camera: 2
- socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1

Raw SHA-256: `b4cb2c64c72445f63d27d511750f1b512e337f9dd786271728782da191b88ac6`. Binary SHA-256: `4a6fe4d21811c2f9cdc63f7a79ec1591ec09f7b1951e80a4e18240af567a0d7b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq018\scenes\sq018_03b_victor.scene" --events
```

## `base\quest\side_quests\sq018\scenes\sq018_03c_padre.scene`

43 graph nodes, 59 edges; 12 event-bearing sections, 76 events; 23 screenplay lines, 6 screenplay options, 2 choice nodes.

Actors: Padre (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `in` → 1.

Exits: `out` → 2; `Kill_the_scene` → 223.

End nodes: 2: `NonTerminating`; 223: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 17 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnDialogLineEvent` | 17 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 84 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/7` |
| `scnIKEvent` | 2 | 84 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnLookAtEvent` | 14 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 11 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnUnmountEvent` | 1 | 84 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/11` |
| `scneventsCameraParamsEvent` | 4 | 84 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 1 | 84 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/8` |
| `scneventsSocket` | 20 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- camera: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- gaze: 1
- idle_animation: 1

Raw SHA-256: `0daf27e6feb545713af0b136e3a01ca014b170a27f154a366ceec83a424fffbc`. Binary SHA-256: `de9ab34b98443ebb926ac3b6008776cff06507f32ce4dc4f027cb6e8d23d9c91`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq018\scenes\sq018_03c_padre.scene" --events
```

## `base\quest\side_quests\sq018\scenes\sq018_03d_barman.scene`

43 graph nodes, 56 edges; 12 event-bearing sections, 81 events; 17 screenplay lines, 5 screenplay options, 1 choice nodes.

Actors: elcoyote_barman (actor 0, spawnSet); V (actor 1, findInContext).

Entries: `in` → 1.

Exits: `out` → 2; `out_victor` → 95.

End nodes: 2: `<omitted>`; 95: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 9 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnDialogLineEvent` | 12 | 9 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnGameplayTransitionEvent` | 1 | 112 / 181 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/5` |
| `scnIKEvent` | 2 | 112 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scnLookAtEvent` | 13 | 9 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnPlaySkAnimEvent` | 11 | 9 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 1 | 112 / 185 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/8` |
| `scneventsAttachPropToNode` | 2 | 9 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/14` |
| `scneventsAttachPropToPerformer` | 4 | 9 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |
| `scneventsAttachPropToWorld` | 2 | 9 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/12` |
| `scneventsCameraParamsEvent` | 4 | 9 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 1 | 112 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/7` |
| `scneventsSocket` | 18 | 9 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsVFXEvent` | 5 | 9 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx, socket_signal: 1
- gaze: 1

Raw SHA-256: `4ece601cc83f4e22ac60a84ea9d7dbe88693b94abae1f98089730b85ec5bd7c2`. Binary SHA-256: `a1e994142339d0606a820419fe5c800984a2650e77137a5ad9c6ec9076dc6e05`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq018\scenes\sq018_03d_barman.scene" --events
```

## `base\quest\side_quests\sq018\scenes\sq018_04b_valentinos_el_coyote.scene`

206 graph nodes, 226 edges; 25 event-bearing sections, 116 events; 61 screenplay lines, 10 screenplay options, 6 choice nodes.

Actors: fa_ganger_01 (actor 0, community); fa_ganger_02 (actor 1, community); gle_04_bouncer (actor 2, community); ma_ganger_01 (actor 3, community); ma_ganger_02 (actor 4, community); ma_ganger_03 (actor 5, community); rey_01_martha (actor 6, community); rey_01_gustavo (actor 7, community); rey_01_ma_friend_01 (actor 8, community); rey_01_ma_friend_02 (actor 9, community); gle_01_mom (actor 10, community); gle_01_dad (actor 11, community); V (actor 12, findInContext).

Entries: `in` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 2509 / 898 | `/Data/RootChunk/sceneGraph/Data/graph/133/Data/events/3` |
| `scnDialogLineEvent` | 49 | 8 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnLookAtEvent` | 29 | 8 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 13 | 14 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsAttachPropToPerformer` | 2 | 2509 / 896 | `/Data/RootChunk/sceneGraph/Data/graph/133/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 2509 / 899 | `/Data/RootChunk/sceneGraph/Data/graph/133/Data/events/4` |
| `scneventsEquipItemToPerformer` | 1 | 106 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scneventsSocket` | 15 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsVFXEvent` | 3 | 2509 / 897 | `/Data/RootChunk/sceneGraph/Data/graph/133/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, socket_signal: 4
- speech, gaze: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- skeletal_animation, props_equipment, audio, vfx: 2
- speech, skeletal_animation, props_equipment, socket_signal: 1
- socket_signal: 1
- vfx: 1

Raw SHA-256: `5e3bf1e55ec1987c36d5c14f7f645e67d6148b656abb69e53da582c6e1d65a2e`. Binary SHA-256: `9312434802aa452d76b52ad06310ae1658c5b036c01246b5340201798758d687`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq018\scenes\sq018_04b_valentinos_el_coyote.scene" --events
```

