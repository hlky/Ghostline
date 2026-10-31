# Gig: Waiting for Dodger: scene presentation

Journal identity: `ep1/quests/street_stories/sts_ep1_10`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-sts_ep1_10.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_charles_and_guard_chat.scene`

16 graph nodes, 29 edges; 3 event-bearing sections, 7 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: charles (actor 0, community); nosy_guard (actor 1, community).

Entries: `Start 0` → 1; `door_close` → 56.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 45 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnDialogLineEvent` | 6 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- idle_animation: 1

Raw SHA-256: `b5eb08232db9095fcfcc99c2da00b144e7536dcecc0b460e63d6ec1f910a8cdc`. Binary SHA-256: `11561aa8cbf479c3976c8cab4c836120e8fdd0bcbaac7370ae8af26e5de5fa9f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_charles_and_guard_chat.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_dodger_garage_scene.scene`

359 graph nodes, 456 edges; 53 event-bearing sections, 613 events; 109 screenplay lines, 13 screenplay options, 7 choice nodes.

Actors: bill (actor 0, community); charles (actor 1, community); dodger (actor 2, community); goon1 (actor 3, community); goon2 (actor 4, community); dodger_car (actor 5, community); ncpd_car (actor 6, community); player (actor 7, findInContext).

Entries: `Start 0` → 1; `Start 5` → 2272; `combat` → 548.

Exits: `player_left` → 1054; `leave_car` → 773; `combat start` → 550.

End nodes: 550: `<omitted>`; 773: `NonTerminating`; 1054: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 14 | 128 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnChangeIdleAnimEvent` | 23 | 128 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnDialogLineEvent` | 93 | 128 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnGameplayTransitionEvent` | 5 | 1528 / 1598 | `/Data/RootChunk/sceneGraph/Data/graph/156/Data/events/12` |
| `scnIKEvent` | 10 | 1528 / 1586 | `/Data/RootChunk/sceneGraph/Data/graph/156/Data/events/3` |
| `scnLookAtAdvancedEvent` | 2 | 144 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/14` |
| `scnLookAtEvent` | 206 | 128 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 146 | 128 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 5 | 1528 / 1597 | `/Data/RootChunk/sceneGraph/Data/graph/156/Data/events/11` |
| `scneventsEquipItemToPerformer` | 2 | 1762 / 2005 | `/Data/RootChunk/sceneGraph/Data/graph/204/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 8 | 1528 / 1573 | `/Data/RootChunk/sceneGraph/Data/graph/156/Data/events/0` |
| `scneventsSocket` | 93 | 128 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |
| `scneventsUnequipItemFromPerformer` | 1 | 1762 / 2007 | `/Data/RootChunk/sceneGraph/Data/graph/204/Data/events/5` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 653 / 466 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/6` |
| `scneventsVFXEvent` | 4 | 320 / 258 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 7
- speech: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, gaze: 4
- speech, skeletal_animation, gaze: 3
- socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, gaze, vfx: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, audio: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- audio, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze: 1
- gaze: 1
- gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `bda7e631556ed5c109818d967404d0a1a7f43ad27d5ccc207d43bb4cb97311c9`. Binary SHA-256: `01752df043bb6f1a0a8e142e27a098541d7ea6bae4922b3a4ee7363e5b83d05b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_dodger_garage_scene.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_goons_garage.scene`

3 graph nodes, 2 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: goon1 (actor 0, community); goon2 (actor 1, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `5f043588ed3cf9cd9d61be27dedafa5d98116b1692f78620affe6082c51db670`. Binary SHA-256: `f5254906bfbec811ea0d3b4b723948fcca02cd3452cdb03531399b681f4bfdf2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_goons_garage.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_holocall_debrief.scene`

31 graph nodes, 40 edges; 4 event-bearing sections, 4 events; 4 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `not_rejectable_q303_start` → 157.

Exits: `End 0` → 2; `rejected_out` → 128; `not_rejectable_q303_end` → 159.

End nodes: 2: `<omitted>`; 128: `<omitted>`; 159: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `5b2edca2c7acc68d99733a198ece9c383c79fbf47eeba9b185bfd7da1fd89abe`. Binary SHA-256: `7cad16cdbba25aa4176c6f14c8795e50d5399b12ae777b91ba225cc7acdb726d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_holocall_debrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 56.

End nodes: 2: `<omitted>`; 56: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 46 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `c16705bc1c288794ee8576296d49ec63a58da7c55a15a33294d4ff24b5945d75`. Binary SHA-256: `19630324297c342ebeb84a59dc98194d8a0f69b66baed85fc17b5009953fa0ff`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_holocall_prebrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_informer.scene`

75 graph nodes, 91 edges; 18 event-bearing sections, 108 events; 42 screenplay lines, 9 screenplay options, 4 choice nodes.

Actors: Stella (actor 0, community); informers_car (actor 1, community); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `CP77-45269` → 580.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 245 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/4` |
| `scnChangeIdleAnimEvent` | 5 | 403 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/3` |
| `scnDialogLineEvent` | 31 | 74 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scnGameplayActionEvent` | 5 | 403 / 262 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 410 / 299 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/12` |
| `scnIKEvent` | 2 | 410 / 281 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/1` |
| `scnLookAtEvent` | 7 | 85 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnPlaySkAnimEvent` | 15 | 74 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPoseCorrectionEvent` | 7 | 74 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scnUnmountEvent` | 1 | 410 / 304 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/16` |
| `scneventsAttachPropToPerformer` | 2 | 74 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |
| `scneventsCameraParamsEvent` | 2 | 245 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 8 | 74 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scneventsSocket` | 16 | 74 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, socket_signal: 2
- idle_animation, audio, socket_signal, animation_state, gameplay_action: 2
- speech, skeletal_animation, props_equipment, socket_signal, animation_state: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, animation_state: 1
- skeletal_animation, idle_animation, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, idle_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, socket_signal, animation_state, gameplay_action: 1

Raw SHA-256: `f739e6185cb71b57dc80eb734d757731025a5ab7699a5e9d08228f4f72965d64`. Binary SHA-256: `c8168c3a47baab6096565189eef6f86d6e84550adee045ba294d7812b6e70f1a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_informer.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_interrogation_room_scene.scene`

181 graph nodes, 213 edges; 47 event-bearing sections, 313 events; 95 screenplay lines, 18 screenplay options, 10 choice nodes.

Actors: charles (actor 0, community); bill (actor 1, community); johnny (actor 2, spawnDespawn); dead_dealer_body (actor 3, community); player (actor 4, findInContext).

Entries: `Start 0` → 1; `chicken_test` → 615.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 649 / 747 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/3` |
| `scnChangeIdleAnimEvent` | 4 | 309 / 173 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/1` |
| `scnDialogLineEvent` | 82 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 1190 / 1354 | `/Data/RootChunk/sceneGraph/Data/graph/157/Data/events/5` |
| `scnIKEvent` | 2 | 1190 / 1349 | `/Data/RootChunk/sceneGraph/Data/graph/157/Data/events/1` |
| `scnLookAtEvent` | 56 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 88 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 1190 / 1353 | `/Data/RootChunk/sceneGraph/Data/graph/157/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 1 | 1190 / 1351 | `/Data/RootChunk/sceneGraph/Data/graph/157/Data/events/3` |
| `scneventsSocket` | 76 | 6 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 15
- speech: 13
- skeletal_animation, socket_signal: 6
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation, gaze: 1
- speech, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `6e6569f1ed9320c3ff8e999aa8f22ad9f857c5f2444fef4436effd64201a55ec`. Binary SHA-256: `51ea96023f40b9cc8a3765d837fb04f253868c868e48ca3efc9b1fcf2e3f12bf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_interrogation_room_scene.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_reception_chat.scene`

6 graph nodes, 5 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: goon1 (actor 0, community); goon2 (actor 1, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `399040e13f51a1229d6807a89c06b710d3238820357564e332c81b2903567a88`. Binary SHA-256: `14382a0aa9b252d085b0e3ef00a47f37685214c210311389f14cc89c9bb647c7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_reception_chat.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_tv_crew_follow.scene`

294 graph nodes, 344 edges; 29 event-bearing sections, 105 events; 64 screenplay lines, 1 screenplay options, 0 choice nodes.

Actors: bill (actor 0, community); charles (actor 1, community); archives_enemy_01 (actor 2, community); archives_enemy_02 (actor 3, community); enemy_cells (actor 4, community); Player (actor 5, findInContext).

Entries: `preview` → 3086; `Start 7` → 3854; `crouch_in` → 3863; `chicken_test` → 2808; `Start` → 1721.

Exits: `clear` → 3840; `crouch_out` → 3864; `End 1` → 2069.

End nodes: 2069: `NonTerminating`; 3840: `<omitted>`; 3864: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 2288 / 341 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/1` |
| `scnChangeIdleAnimEvent` | 2 | 3315 / 892 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/4` |
| `scnDialogLineEvent` | 35 | 252 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 15 | 252 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 18 | 747 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scneventsAttachPropToPerformer` | 2 | 2554 / 430 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 2554 / 432 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/3` |
| `scneventsCameraParamsEvent` | 2 | 3315 / 887 | `/Data/RootChunk/sceneGraph/Data/graph/122/Data/events/2` |
| `scneventsSocket` | 27 | 747 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- speech, gaze: 1
- socket_signal: 1
- speech, audio: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, camera, socket_signal: 1
- camera: 1
- skeletal_animation: 1
- speech, socket_signal: 1

Raw SHA-256: `fc35b8192a29161dd4923f09c3749d1a26c1462381ce399ad4e73a6d93a43d58`. Binary SHA-256: `2f073140430ed0eb0d7955c6d96a57ed5dffa94bdf451964fddf8b5478c96591`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_10\scenes\sts_ep1_10_tv_crew_follow.scene" --events
```

