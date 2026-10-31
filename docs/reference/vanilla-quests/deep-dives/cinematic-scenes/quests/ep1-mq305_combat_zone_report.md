# Shot by Both Sides: scene presentation

Journal identity: `ep1/quests/minor_quest/mq305_combat_zone_report`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-mq305_combat_zone_report.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\minor_quests\mq305\scenes\mq305_01_holocall_hook.scene`

25 graph nodes, 27 edges; 8 event-bearing sections, 17 events; 15 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: mr_hands_holo (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 45.

Exits: `out_rejected` → 338; `End 0` → 47.

End nodes: 47: `<omitted>`; 338: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 15 | 263 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsSocket` | 2 | 263 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, socket_signal: 2

Raw SHA-256: `fb183a5bdadc13e488a5de2ad9db148de4bb7786b1899ade980770a102501986`. Binary SHA-256: `d764ecc48277d105afe8e438b9ea0cb8e6e7402f97b0fccead60fc75d79857cf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq305\scenes\mq305_01_holocall_hook.scene" --events
```

## `ep1\quest\minor_quests\mq305\scenes\mq305_02_apartment_dante.scene`

63 graph nodes, 102 edges; 16 event-bearing sections, 87 events; 23 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: dante (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `in_meet_dante` → 355.

Exits: `out_meet_dante` → 357.

End nodes: 357: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 447 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 15 | 447 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtAdvancedEvent` | 6 | 447 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnLookAtEvent` | 21 | 447 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 17 | 447 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 4 | 447 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scneventsEquipItemToPerformer` | 2 | 1042 / 346 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/4` |
| `scneventsSocket` | 16 | 447 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsUnequipItemFromPerformer` | 1 | 1042 / 348 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- gaze, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1

Raw SHA-256: `9207a9fb0a67ce2773c661694c9989104485a64cc0708db3f54d204cd0bfc940`. Binary SHA-256: `1bfc57918fc329cb15f0fd59fb32a1a7eb89a8659f8880f412c442208a801e63`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq305\scenes\mq305_02_apartment_dante.scene" --events
```

## `ep1\quest\minor_quests\mq305\scenes\mq305_03_apartment_johnny.scene`

94 graph nodes, 120 edges; 8 event-bearing sections, 43 events; 9 screenplay lines, 6 screenplay options, 6 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start` → 1; `in_enter_apartment` → 295.

Exits: `out_johnny_talk` → 3; `out_enter_apartment` → 297; `End1` → 212; `out_got_keycard` → 404.

End nodes: 3: `<omitted>`; 212: `NonTerminating`; 297: `NonTerminating`; 404: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 417 / 332 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/0` |
| `scnDialogLineEvent` | 4 | 194 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/0` |
| `scnLookAtEvent` | 10 | 276 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/0` |
| `scnOverridePhantomParamsEvent` | 6 | 276 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/2` |
| `scnPlaySkAnimEvent` | 9 | 276 / 185 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/1` |
| `scneventsEquipItemToPerformer` | 1 | 330 / 285 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/0` |
| `scneventsSocket` | 11 | 276 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 1 | 330 / 295 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, gaze, socket_signal: 1
- gaze: 1
- audio: 1

Raw SHA-256: `9177db207d62a6def12241405a6690dda637569fbce1d2da6a7667770c0e708b`. Binary SHA-256: `64856fa51e16d86e53394fb0b0c0fe6ce097066fdf2608a52a5f42c82b92e4ad`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq305\scenes\mq305_03_apartment_johnny.scene" --events
```

## `ep1\quest\minor_quests\mq305\scenes\mq305_04_bunker.scene`

613 graph nodes, 835 edges; 106 event-bearing sections, 876 events; 171 screenplay lines, 35 screenplay options, 19 choice nodes.

Actors: dante (actor 0, spawnSet); bree (actor 1, spawnSet); johnny (actor 2, spawnDespawn); Player (actor 3, findInContext).

Entries: `Start 0` → 1; `in_dante_die` → 5036; `in_dante_killed` → 721; `in_bree_hides` → 3506; `in_johnny_max_jones` → 2408; `Kill_johnny` → 5746; `Start 4` → 5201; `in_bree_hides_stop_lookat` → 5210; `in_dante_reset_for_combat` → 5231; `in_johnny_all_dead` → 4719; `Start 5` → 5300; `Start 6` → 5323; `lean out` → 2643; `Start 2` → 4308; `Start 7` → 5427; `Start 8` → 5463.

Exits: `out_dante_die` → 5059; `End` → 118; `out_watch_video_1` → 1777; `out_watch_video_2` → 2909; `out_watch_video_3` → 2911; `out_dante_combat` → 718; `out_bree_hides` → 3510; `out_johnny_max_jones` → 2410; `out_bree_hides_stop_lookat` → 5212; `Back_to_combat` → 5766; `out_dante_reset_for_combat` → 5233; `out_failed` → 4161; `End3` → 3140; `out_johnny_all_dead` → 4837.

End nodes: 118: `NonTerminating`; 718: `<omitted>`; 1777: `NonTerminating`; 2410: `<omitted>`; 2909: `NonTerminating`; 2911: `NonTerminating`; 3140: `NonTerminating`; 3510: `NonTerminating`; 4161: `<omitted>`; 4837: `<omitted>`; 5059: `<omitted>`; 5212: `<omitted>`; 5233: `<omitted>`; 5766: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 7 | 1996 / 1022 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/27` |
| `scnChangeIdleAnimEvent` | 46 | 398 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnDialogLineEvent` | 122 | 278 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 11 | 328 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scnIKEvent` | 22 | 328 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnLookAtAdvancedEvent` | 31 | 442 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/15` |
| `scnLookAtEvent` | 229 | 328 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnOverridePhantomParamsEvent` | 6 | 4253 / 2598 | `/Data/RootChunk/sceneGraph/Data/graph/315/Data/events/4` |
| `scnPlaySkAnimEvent` | 164 | 328 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPoseCorrectionEvent` | 12 | 1810 / 692 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/2` |
| `scnUnmountEvent` | 11 | 328 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scneventsAttachPropToPerformer` | 6 | 777 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/0` |
| `scneventsAttachPropToWorld` | 7 | 777 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/5` |
| `scneventsEquipItemToPerformer` | 2 | 4733 / 3101 | `/Data/RootChunk/sceneGraph/Data/graph/385/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 11 | 328 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scneventsSocket` | 181 | 328 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsVFXEvent` | 8 | 919 / 293 | `/Data/RootChunk/sceneGraph/Data/graph/33/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 17
- speech, skeletal_animation, gaze, socket_signal: 10
- speech: 8
- gaze: 8
- gaze, socket_signal: 7
- skeletal_animation, gaze, socket_signal, animation_state: 5
- speech, skeletal_animation, idle_animation, gaze: 5
- speech, gaze: 4
- skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- props_equipment, socket_signal: 3
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, vfx, socket_signal: 2
- speech, gaze, socket_signal: 2
- skeletal_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, props_equipment, vfx: 1
- socket_signal: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `5a8c1dec7b2852854cb901f85651c664009dd89dd4b51ccedaca540798ee30c6`. Binary SHA-256: `7d7815aaefd3a6085eb4fa8125e105cdb29bac276dec6a96c8ee4512dd43a965`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq305\scenes\mq305_04_bunker.scene" --events
```

## `ep1\quest\minor_quests\mq305\scenes\mq305_04a_video_recordings.scene`

92 graph nodes, 96 edges; 4 event-bearing sections, 76 events; 12 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: scientist (actor 0, community); Player (actor 1, findInContext).

Entries: `camera_preview` → 706; `in_video_diary_1` → 7; `in_video_diary_2` → 298; `in_video_diary_3` → 300.

Exits: `out` → 18.

End nodes: 18: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 9 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnChangeIdleAnimEvent` | 5 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnDialogLineEvent` | 11 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/6` |
| `scnLookAtAdvancedEvent` | 21 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |
| `scnLookAtEvent` | 5 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnPlaySkAnimEvent` | 26 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scneventsCameraEvent` | 1 | 705 / 661 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 705 / 663 | `/Data/RootChunk/sceneGraph/Data/graph/87/Data/events/1` |
| `scneventsSocket` | 5 | 4 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- camera: 1

Raw SHA-256: `ed0c542ac5c249b21dfaafe56111fc1ba4fca278de4ee6e1f013c55e1afa8ac4`. Binary SHA-256: `5570545e8593f4a979fe8fff2c84b2e40e591513a411efbdc401164cd5aac16b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq305\scenes\mq305_04a_video_recordings.scene" --events
```

## `ep1\quest\minor_quests\mq305\scenes\mq305_04b_lab_exploration.scene`

560 graph nodes, 774 edges; 101 event-bearing sections, 454 events; 125 screenplay lines, 22 screenplay options, 11 choice nodes.

Actors: bree (actor 0, spawnSet); johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `in` → 39; `exploration` → 2937; `blocked door` → 2947; `Start 7` → 4065; `Start 3` → 3077; `Start 4` → 3079; `Start 6` → 3653; `Start 8` → 4251; `Start 9` → 4268; `Start 5` → 3184; `in_johnny` → 2661.

Exits: `out` → 41; `out_turret_combat_1` → 824; `out_turret_combat_2` → 827; `out_failed` → 1931; `out_johnny` → 2663.

End nodes: 41: `<omitted>`; 824: `NonTerminating`; 827: `NonTerminating`; 1931: `<omitted>`; 2663: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 122 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/5` |
| `scnChangeIdleAnimEvent` | 14 | 50 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 88 | 43 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 6 | 544 / 284 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/20` |
| `scnIKEvent` | 12 | 544 / 275 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/12` |
| `scnLookAtAdvancedEvent` | 13 | 43 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 43 | 43 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 1 | 2665 / 2196 | `/Data/RootChunk/sceneGraph/Data/graph/298/Data/events/1` |
| `scnPlaySkAnimEvent` | 106 | 43 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 6 | 303 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/3` |
| `scnUnmountEvent` | 6 | 544 / 283 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/19` |
| `scneventsAttachPropToPerformer` | 10 | 122 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |
| `scneventsAttachPropToWorld` | 9 | 122 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/10` |
| `scneventsEquipItemToPerformer` | 2 | 300 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 6 | 544 / 279 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/16` |
| `scneventsSocket` | 117 | 43 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 4 | 870 / 572 | `/Data/RootChunk/sceneGraph/Data/graph/67/Data/events/3` |
| `scneventsVFXDurationEvent` | 2 | 4365 / 3527 | `/Data/RootChunk/sceneGraph/Data/graph/552/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 27
- speech, skeletal_animation, socket_signal: 8
- skeletal_animation, socket_signal: 8
- speech, skeletal_animation, gaze, socket_signal: 7
- speech, socket_signal: 6
- speech, gaze: 4
- skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation: 4
- socket_signal: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 2
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 2
- speech, idle_animation: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- vfx: 1

Raw SHA-256: `023fa0a690a01339c26f13a24994464dcd6bb45f073f38a91754ea35a7739ee2`. Binary SHA-256: `158fe3aae53a1bbacd1c540ca07e928e3ebbe40f112ec803170612232d3bd37f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq305\scenes\mq305_04b_lab_exploration.scene" --events
```

## `ep1\quest\minor_quests\mq305\scenes\mq305_05_outcome_mr_hands.scene`

39 graph nodes, 38 edges; 8 event-bearing sections, 20 events; 17 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: mr_hands_holo (actor 0, spawnSet); johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `in_bree_sold_data` → 165; `in_johnny_sold_data` → 251; `in_bree_dead` → 64.

Exits: `out_bree_dead` → 119; `out_johnny_sold_data` → 253; `out_bree_sold_data` → 181.

End nodes: 119: `<omitted>`; 181: `<omitted>`; 253: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 3. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 17 | 12 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnLookAtEvent` | 1 | 255 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 255 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/0` |
| `scneventsSocket` | 1 | 255 / 116 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `87f11ef3ce1acee91c4d63e3df04df576365c2c386248af27434a88f6553db5f`. Binary SHA-256: `803698d0ccdd4c528abc72b3d35b53547681c0dc6af2da815a2675028484152b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq305\scenes\mq305_05_outcome_mr_hands.scene" --events
```

## `ep1\quest\minor_quests\mq305\scenes\mq305_06_netwatch_encounter.scene`

6 graph nodes, 5 edges; 1 event-bearing sections, 1 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: netwatch_soldier (actor 0, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 1 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `efc5c570b4297b58cc9a1cd35d707988584d4b1865630ef112f63ecc44e5919a`. Binary SHA-256: `ca51ef6d3f1f9a01a3f5c66911c6fac6b84d4229b151b74063719a588e247dbe`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\minor_quests\mq305\scenes\mq305_06_netwatch_encounter.scene" --events
```

