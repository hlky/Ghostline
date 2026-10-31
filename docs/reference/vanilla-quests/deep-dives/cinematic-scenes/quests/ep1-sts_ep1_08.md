# Gig: Spy in the Jungle: scene presentation

Journal identity: `ep1/quests/street_stories/sts_ep1_08`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-sts_ep1_08.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_client_ending.scene`

166 graph nodes, 195 edges; 27 event-bearing sections, 280 events; 62 screenplay lines, 14 screenplay options, 11 choice nodes.

Actors: Ana (actor 0, community); steven (actor 1, community); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `Start 2` → 1082; `Start 1` → 672; `Start 3` → 1280.

Exits: `End 0` → 2; `fast` → 579.

End nodes: 2: `NonTerminating`; 579: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 12 | 491 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |
| `scnDialogLineEvent` | 49 | 448 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtAdvancedEvent` | 5 | 492 / 146 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/5` |
| `scnLookAtEvent` | 64 | 448 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 70 | 448 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnPoseCorrectionEvent` | 7 | 557 / 376 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/14` |
| `scneventsAttachPropToPerformer` | 9 | 450 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scneventsAttachPropToWorld` | 10 | 491 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/7` |
| `scneventsEquipItemToPerformer` | 3 | 492 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/44` |
| `scneventsSocket` | 51 | 448 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 4
- speech, skeletal_animation, props_equipment, socket_signal: 3
- speech: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze, socket_signal: 1
- speech, gaze: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation: 1
- props_equipment: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal, animation_state: 1

Raw SHA-256: `28a06f8c7080e58f823dc11b7ddaf6181a04e08f13b2d1218d80d0fdf5045e1d`. Binary SHA-256: `6fa4dbe1be6237f9c46e2f6377c6c346899a55946022227bdc2ddfb3a111b265`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_client_ending.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_client_meeting.scene`

268 graph nodes, 310 edges; 51 event-bearing sections, 509 events; 98 screenplay lines, 22 screenplay options, 11 choice nodes.

Actors: Steven (actor 0, community); Ana (actor 1, community); Bana (actor 2, findInContext); Ana_voice (actor 3, findInContext); V (actor 4, findInContext).

Entries: `Start 0` → 1; `Start 3` → 1539.

Exits: `End 0` → 2; `kill` → 409.

End nodes: 2: `NonTerminating`; 409: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 25 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 75 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnLookAtAdvancedEvent` | 26 | 38 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnLookAtEvent` | 150 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 91 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 6 | 4 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |
| `scneventsAttachPropToNode` | 1 | 227 / 239 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/4` |
| `scneventsAttachPropToPerformer` | 2 | 4 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsAttachPropToWorld` | 1 | 4 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scneventsEquipItemToPerformer` | 3 | 1640 / 1999 | `/Data/RootChunk/sceneGraph/Data/graph/251/Data/events/5` |
| `scneventsSocket` | 125 | 4 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsUnequipItemFromPerformer` | 1 | 1640 / 2001 | `/Data/RootChunk/sceneGraph/Data/graph/251/Data/events/7` |
| `scneventsVFXDurationEvent` | 1 | 524 / 429 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/3` |
| `scneventsVFXEvent` | 2 | 35 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 12
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- skeletal_animation: 4
- skeletal_animation, gaze, socket_signal: 3
- gaze, socket_signal: 3
- speech, gaze: 2
- speech: 2
- skeletal_animation, props_equipment, socket_signal, animation_state: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- gaze: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `e0ecef2a5a2603ae3f4ea4aeb5570261e234f4f060acc7421de63cbafddaacbb`. Binary SHA-256: `8b740ef961ec0cc03b2852d1a995506b5a4db03d8312b9fd1c907e0ec42711f1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_client_meeting.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_enemies_chats.scene`

27 graph nodes, 26 edges; 4 event-bearing sections, 14 events; 7 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: enemy_001 (actor 0, community); enemy_002 (actor 1, community); enemy_003 (actor 2, community); enemy_004 (actor 3, community); enemy_005 (actor 4, community); enemy_006 (actor 5, community); enemy_007 (actor 6, community); kgb_boss (actor 7, community); johnny (actor 8, spawnDespawn); enemy_front_01 (actor 9, community); enemy_frony_02 (actor 10, community); Player (actor 11, findInContext).

Entries: `inside chat` → 1; `kgb_boss_taunt` → 16; `front entrance` → 25.

Exits: `front entrance end` → 28; `inside chat end` → 2; `End 6` → 67; `kgb_boss_end` → 19.

End nodes: 2: `<omitted>`; 19: `NonTerminating`; 28: `<omitted>`; 67: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 17 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 5 | 17 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 2 | 17 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsSocket` | 2 | 17 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, skeletal_animation, audio, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `219b1f02976af5ea47e98ff4ede4f70592d0d4c60c7baa2448ff60a556e7c3cf`. Binary SHA-256: `ca888522b34d88bba532762beb0d87e4fb9541f6f39129a88fceb141932aae58`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_enemies_chats.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_holocall_debrief.scene`

24 graph nodes, 29 edges; 2 event-bearing sections, 6 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `end` → 2; `reject` → 179.

End nodes: 2: `<omitted>`; 179: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 150 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `cfd5c24536a42320fa9ccd4503a6145bbb91ded9098a9e7e993fb637cba4a95f`. Binary SHA-256: `3e71fd5735c98fd194caa3c1931d6cc622059e0a3b92d9c0dcf1b9b82ea057a4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_holocall_debrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_holocall_prebrief.scene`

25 graph nodes, 29 edges; 4 event-bearing sections, 7 events; 7 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 64.

End nodes: 2: `<omitted>`; 64: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 7 | 32 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4

Raw SHA-256: `8c0a2a52a24d83b0e599110141cc15cccf4d17b65983963deeb2290b3a23a835`. Binary SHA-256: `160490f8ad20a95729d29c545a1fae391eabd309ca0fba363b47dd71c4d93bfb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_holocall_prebrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_target_meeting.scene`

248 graph nodes, 274 edges; 39 event-bearing sections, 184 events; 78 screenplay lines, 18 screenplay options, 10 choice nodes.

Actors: target (actor 0, spawnSet); bana_voice (actor 1, findInContext); Ana (actor 2, spawnSet); bana_impersonated (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `Bana intro` → 1; `fake input to keep lines alive` → 1971; `Start 11` → 2490; `Meeting` → 348; `eliminate enemies` → 890; `katya dead comment` → 1407; `enemies defeated` → 923.

Exits: `dead` → 24; `meeting_point` → 1293; `friendly` → 1073; `phone end 01` → 887; `eliminate enemies end` → 891; `End 12` → 1409; ` enemies defeated end` → 924; `katya killed before order` → 1416.

End nodes: 24: `<omitted>`; 887: `NonTerminating`; 891: `NonTerminating`; 924: `NonTerminating`; 1073: `NonTerminating`; 1293: `NonTerminating`; 1409: `NonTerminating`; 1416: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1344 / 609 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/4` |
| `scnChangeIdleAnimEvent` | 8 | 187 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 71 | 79 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 1109 / 485 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/20` |
| `scnIKEvent` | 2 | 1109 / 477 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/13` |
| `scnLookAtAdvancedEvent` | 3 | 201 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scnLookAtEvent` | 25 | 201 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnPlaySkAnimEvent` | 22 | 1027 / 302 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 187 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnUnmountEvent` | 1 | 1109 / 484 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/19` |
| `scneventsAttachPropToNode` | 1 | 1344 / 611 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/6` |
| `scneventsAttachPropToPerformer` | 1 | 1344 / 608 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 1 | 1109 / 480 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/16` |
| `scneventsSocket` | 39 | 187 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsVFXDurationEvent` | 3 | 201 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scneventsVFXEvent` | 3 | 1109 / 458 | `/Data/RootChunk/sceneGraph/Data/graph/72/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, skeletal_animation, socket_signal: 4
- speech, gaze: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, idle_animation, socket_signal: 2
- idle_animation, socket_signal, animation_state: 1
- speech, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `d05346023180176a807920783b4a3324e84f8174450439209b711238171eeba2`. Binary SHA-256: `81142f72b147e1e00ccdb0c897bafe3bc81660633dd38e01c88732227e79de82`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_08\scenes\sts_ep1_08_target_meeting.scene" --events
```

