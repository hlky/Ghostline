# Gig: Talent Academy: scene presentation

Journal identity: `ep1/quests/street_stories/sts_ep1_13`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-sts_ep1_13.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_chats.scene`

18 graph nodes, 22 edges; 2 event-bearing sections, 5 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: guard_008 (actor 0, community); guard_009 (actor 1, community); coach (actor 2, community); employee_006 (actor 3, community).

Entries: `Start 0` → 1; `Start1` → 13.

Exits: `End 0` → 2; `End1` → 15.

End nodes: 2: `<omitted>`; 15: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 1 | 18 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1
- speech, socket_signal: 1

Raw SHA-256: `aa4ec9e8caeb721f07970f46870693cdebfe30e097e34031cf4a70e614222586`. Binary SHA-256: `12e0c09b201b36b4320288aa6ce5375f0d0261435a71afafb8ce649ff168a3cc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_chats.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_children.scene`

32 graph nodes, 37 edges; 10 event-bearing sections, 70 events; 26 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Katie (actor 0, community); johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `Start2` → 118; `Start 1` → 6.

Exits: `End2` → 120; `End 1` → 7.

End nodes: 7: `<omitted>`; 120: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 182 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnChangeIdleAnimEvent` | 7 | 182 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |
| `scnDialogLineEvent` | 20 | 160 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnLookAtEvent` | 19 | 182 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 7 | 182 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scneventsAttachPropToPerformer` | 1 | 356 / 154 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/2` |
| `scneventsSocket` | 11 | 160 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- idle_animation, props_equipment, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech: 1

Raw SHA-256: `fcf4660a447e94b22f115f8167012584c1e98e30047a44f04b6c3d43504f3cc6`. Binary SHA-256: `0f74f32611bbef655211024b8ebb955fc9b496d7545776ba288c62752dd9a02f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_children.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_dolls.scene`

150 graph nodes, 155 edges; 24 event-bearing sections, 158 events; 27 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: consierge_for_androids (actor 0, community); doll_anteroom_001 (actor 1, community); doll_anteroom_002 (actor 2, community); doll_001 (actor 3, community); doll_002 (actor 4, community); doll_003 (actor 5, community); doll_004 (actor 6, community); doll_005 (actor 7, community); doll_006 (actor 8, community); doll_007 (actor 9, community); doll_008 (actor 10, community); doll_009 (actor 11, community); doll_anteroom_003 (actor 12, community); doll_anteroom_004 (actor 13, community); guard_008 (actor 14, community); employee_002_auction (actor 15, community); child (actor 16, community); consierge_for_humans (actor 17, community); doll_010 (actor 18, community); doll_011 (actor 19, community); doll_012 (actor 20, community); guest_001 (actor 21, community); guest_002 (actor 22, community); guest_003 (actor 23, community); guest_004 (actor 24, community); guest_005 (actor 25, community); guest_006 (actor 26, community); guest_007 (actor 27, community); guest_008 (actor 28, community); guest_009 (actor 29, community); guest_010 (actor 30, community); guest_011 (actor 31, community); guest_scene (actor 32, community); guest_012 (actor 33, community); guest_013 (actor 34, community); guest_014 (actor 35, community); guest_015 (actor 36, community); guest_016 (actor 37, community); guest_017 (actor 38, community); Player (actor 39, findInContext).

Entries: `dolls_setup_start` → 1; `doll_001_start` → 181; `dolls_chat_start` → 507.

Exits: `dolls_setup_end` → 2; `doll_001_before_connection_exit` → 420; `doll_001_exit_a` → 341; `dolls_chat_end` → 509.

End nodes: 2: `<omitted>`; 341: `NonTerminating`; 420: `<omitted>`; 509: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 13 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 6 | 16 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnLookAtEvent` | 10 | 16 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnPlaySkAnimEvent` | 49 | 13 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsEquipItemToPerformer` | 1 | 860 / 941 | `/Data/RootChunk/sceneGraph/Data/graph/121/Data/events/3` |
| `scneventsSocket` | 51 | 13 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 1 | 874 / 971 | `/Data/RootChunk/sceneGraph/Data/graph/125/Data/events/1` |
| `scneventsVFXEvent` | 39 | 13 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- vfx: 14
- skeletal_animation, socket_signal: 2
- skeletal_animation, gaze: 2
- skeletal_animation, props_equipment, socket_signal: 2
- skeletal_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- socket_signal: 1
- speech: 1

Raw SHA-256: `482caf8fc2cabc848f5127a8297ac2827a5850e8d170e5fd23e7b504a9883fc2`. Binary SHA-256: `30f8057bc88fa13b35ddfd0f95c3790dca7d949aa76a6f6d2506dcf935662e1a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_dolls.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_fiona.scene`

278 graph nodes, 346 edges; 72 event-bearing sections, 500 events; 152 screenplay lines, 40 screenplay options, 16 choice nodes.

Actors: Fiona (actor 0, community); Tommie (actor 1, community); Johnny (actor 2, spawnDespawn); V (actor 3, findInContext).

Entries: `fiona_start` → 1; `js_fiona_dead_start` → 2173; `Start 8` → 2428; `tommie` → 1065; `Start 9` → 2527; `reminder_Start` → 1820; `reminder_first_time` → 1837; `elevator_Start` → 2090.

Exits: `fiona_survive_end` → 2; `fiona_survive_end_deal_refuse` → 2149; `js_fiona_dead_end` → 2174; `reminder_end` → 1821; `tommie_end` → 1119; `fiona_dead_end` → 178; `deal_refused_end` → 2091; `reminder_defeated` → 1859.

End nodes: 2: `NonTerminating`; 178: `Terminating`; 1119: `NonTerminating`; 1821: `Terminating`; 1859: `Terminating`; 2091: `NonTerminating`; 2149: `NonTerminating`; 2174: `Terminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 420 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scnChangeIdleAnimEvent` | 11 | 420 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scnDialogLineEvent` | 126 | 19 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 6 | 1110 / 359 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/4` |
| `scnIKEvent` | 12 | 1110 / 356 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/1` |
| `scnLookAtEvent` | 83 | 19 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 1 | 1455 / 742 | `/Data/RootChunk/sceneGraph/Data/graph/85/Data/events/9` |
| `scnPlaySkAnimEvent` | 101 | 19 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 6 | 1110 / 364 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/8` |
| `scneventsAttachPropToNode` | 1 | 2412 / 1717 | `/Data/RootChunk/sceneGraph/Data/graph/226/Data/events/2` |
| `scneventsAttachPropToPerformer` | 9 | 420 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/11` |
| `scneventsAttachPropToWorld` | 9 | 420 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/12` |
| `scneventsEquipItemToPerformer` | 5 | 1432 / 668 | `/Data/RootChunk/sceneGraph/Data/graph/79/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 6 | 1110 / 360 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/5` |
| `scneventsSocket` | 113 | 19 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scneventsUnequipItemFromPerformer` | 3 | 1600 / 1009 | `/Data/RootChunk/sceneGraph/Data/graph/108/Data/events/11` |
| `scneventsVFXDurationEvent` | 3 | 1301 / 523 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/5` |
| `scneventsVFXEvent` | 4 | 909 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 10
- speech: 7
- speech, skeletal_animation, gaze: 5
- speech, skeletal_animation, socket_signal: 5
- speech, socket_signal: 4
- speech, skeletal_animation: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- gaze, socket_signal: 3
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- skeletal_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, props_equipment, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1
- gaze: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1

Raw SHA-256: `e37431e0aefc592edaaeb317ebc53ff22f3795c53c461317fe258f122f394697`. Binary SHA-256: `c7db645326d2413555671bd00a4f297a3e7925327e97e9b2e9b9a7177ff178b3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_fiona.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_holocall_prebrief.scene`

21 graph nodes, 24 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start1` → 246.

Exits: `rejected_out` → 274; `End1` → 248.

End nodes: 248: `<omitted>`; 274: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 64 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `509c37a2f760686ae731339dd4ecf36a06dd5eb397cda9ae5a8972815b34280b`. Binary SHA-256: `2675aaa5ee83751033b50aa26b87a905af716006e81904a1268fbde840f765d9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_holocall_prebrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_informer_deal.scene`

44 graph nodes, 51 edges; 20 event-bearing sections, 80 events; 42 screenplay lines, 12 screenplay options, 5 choice nodes.

Actors: Hands_guy (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `Start 1` → 409.

Exits: `End 0` → 2; `End 1` → 410.

End nodes: 2: `NonTerminating`; 410: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 33 | 74 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 18 | 74 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 18 | 74 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 9 | 74 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXDurationEvent` | 2 | 130 / 98 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- speech, skeletal_animation: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 2
- socket_signal: 2
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation: 1
- speech, gaze: 1

Raw SHA-256: `d1cd5c983e496e973380dfb97d7367e11f5e5a507f427b54af621d608e96648a`. Binary SHA-256: `e833fe0f777e2d056cdc60d264d62c58829dafd8516fd922d81c2ec202139e53`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_informer_deal.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_v_auction.scene`

332 graph nodes, 461 edges; 68 event-bearing sections, 419 events; 126 screenplay lines, 36 screenplay options, 9 choice nodes.

Actors: Receptionist (actor 0, community); Doll_009 (actor 1, community); Guest_010 (actor 2, community); Hands_guy (actor 3, community); bartender (actor 4, community); bar_scout (actor 5, community); guard (actor 6, community); auctioneer (actor 7, community); Johnny (actor 8, spawnDespawn); child_second_one (actor 9, community); child_first_one (actor 10, community); guard_not_scene (actor 11, community); V (actor 12, findInContext).

Entries: `bartender` → 306; `welcome` → 1; `Start1` → 18; `auction_start` → 64; `Start 4` → 2559; `bartender_walks_way_fail_state` → 2005; `Start 3` → 2088.

Exits: `End 0` → 2; `End1` → 14; `auction_end` → 62; `recepcionist_dead` → 2248.

End nodes: 2: `NonTerminating`; 14: `NonTerminating`; 62: `NonTerminating`; 2248: `Terminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 973 / 667 | `/Data/RootChunk/sceneGraph/Data/graph/73/Data/events/0` |
| `scnChangeIdleAnimEvent` | 3 | 2237 / 1708 | `/Data/RootChunk/sceneGraph/Data/graph/235/Data/events/7` |
| `scnDialogLineEvent` | 86 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 12 | 802 / 464 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/22` |
| `scnIKEvent` | 24 | 802 / 455 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/14` |
| `scnLookAtEvent` | 56 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 76 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 2 | 1156 / 831 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/9` |
| `scnUnmountEvent` | 12 | 802 / 463 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/21` |
| `scneventsAttachPropToNode` | 3 | 2477 / 1914 | `/Data/RootChunk/sceneGraph/Data/graph/273/Data/events/6` |
| `scneventsAttachPropToPerformer` | 6 | 363 / 173 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/11` |
| `scneventsAttachPropToWorld` | 2 | 363 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/15` |
| `scneventsCameraParamsEvent` | 4 | 327 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/6` |
| `scneventsEquipItemToPerformer` | 6 | 363 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 12 | 802 / 459 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/18` |
| `scneventsSocket` | 100 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsUnequipItemFromPerformerByItem` | 4 | 381 / 292 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/5` |
| `scneventsVFXDurationEvent` | 7 | 378 / 267 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/21` |
| `scneventsVFXEvent` | 3 | 2477 / 1912 | `/Data/RootChunk/sceneGraph/Data/graph/273/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- skeletal_animation, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation: 4
- speech, skeletal_animation, socket_signal: 4
- speech, gaze: 3
- socket_signal: 3
- skeletal_animation, props_equipment, socket_signal: 3
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, props_equipment, vfx, socket_signal: 3
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, socket_signal: 2
- idle_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, gaze, camera, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `c7c6c8b9b13842c4651173740b1b99a8ac644cf78aede14334fad726f91b9005`. Binary SHA-256: `04340ff3d7488f0f105ea8cc75bef5be2f2c391fe16b69b6234265798a887679`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_13\scenes\sts_ep1_13_v_auction.scene" --events
```

