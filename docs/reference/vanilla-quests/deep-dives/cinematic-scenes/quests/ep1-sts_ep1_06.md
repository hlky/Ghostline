# Gig: Heaviest of Hearts: scene presentation

Journal identity: `ep1/quests/street_stories/sts_ep1_06`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-sts_ep1_06.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_bouncer.scene`

5 graph nodes, 5 edges; 1 event-bearing sections, 3 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: bouncer (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 1 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 1

Raw SHA-256: `f065a5ddb9821641377af03e7146a88f3a5c59a0471233f65db00cfe795db61c`. Binary SHA-256: `33f8a9b412fcf47240fe0e1c6de22e14e9ba62f8c66d15b3142246baa1d11fa6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_bouncer.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_chats.scene`

22 graph nodes, 22 edges; 5 event-bearing sections, 30 events; 20 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: actor_kurtz_001a (actor 0, community); actor_kurtz_001b (actor 1, community); actor_kurtz_002a (actor 2, community); actor_kurtz_002b (actor 3, community); actor_regular_001a (actor 4, community); actor_regular_001b (actor 5, community); actor_regular_002a (actor 6, community); actor_regular_002b (actor 7, community); actor_regular_003a (actor 8, community); actor_regular_003b (actor 9, community).

Entries: `Start 0` → 1; `Start1` → 6; `Start4` → 52; `Start2` → 11; `Start3` → 40.

Exits: `End 0` → 2; `End1` → 8; `End4` → 54; `End2` → 13; `End3` → 42.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 13: `<omitted>`; 42: `<omitted>`; 54: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 20 | 16 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnLookAtEvent` | 10 | 16 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 5

Raw SHA-256: `da36fb2e5b6332bf17e0c1d49b6f147c045f41fa51bc3f919ebaaa93fdd62c27`. Binary SHA-256: `8ddc25ceb0096da88453a199fc48394df5ff49db58eec93682fc09af59a11b56`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_chats.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_client.scene`

153 graph nodes, 169 edges; 37 event-bearing sections, 338 events; 85 screenplay lines, 19 screenplay options, 10 choice nodes.

Actors: Client (actor 0, community); gamer (actor 1, community); Player (actor 2, findInContext).

Entries: `gamer_start` → 1; `reminder_before_sts_start` → 850; `reminder_after_sts_start` → 1218; `micheal_remind_start` → 287; `micheal_bye_start` → 58; `Start 3` → 817.

Exits: `micheal_meet_stop` → 2; `reminder_before_sts_end` → 852; `reminder_after_sts_end` → 1220; `micheal_remind_stop` → 291; `micheal_bye_stop` → 60.

End nodes: 2: `NonTerminating`; 60: `NonTerminating`; 291: `<omitted>`; 852: `<omitted>`; 1220: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 48 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/11` |
| `scnChangeIdleAnimEvent` | 6 | 76 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/3` |
| `scnDialogLineEvent` | 64 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 1095 / 978 | `/Data/RootChunk/sceneGraph/Data/graph/104/Data/events/14` |
| `scnIKEvent` | 4 | 1095 / 968 | `/Data/RootChunk/sceneGraph/Data/graph/104/Data/events/5` |
| `scnLookAtEvent` | 84 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 83 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 2 | 1095 / 977 | `/Data/RootChunk/sceneGraph/Data/graph/104/Data/events/13` |
| `scneventsEquipItemToPerformer` | 8 | 25 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 2 | 1095 / 975 | `/Data/RootChunk/sceneGraph/Data/graph/104/Data/events/12` |
| `scneventsSocket` | 68 | 25 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsUnequipItemFromPerformer` | 3 | 25 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 65 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/5` |
| `scneventsVFXDurationEvent` | 5 | 83 / 210 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/5` |
| `scneventsVFXEvent` | 1 | 409 / 535 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 6
- speech, skeletal_animation, gaze: 4
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 4
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, audio, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation: 1
- skeletal_animation, gaze: 1
- props_equipment, socket_signal: 1
- idle_animation, gaze, vfx, socket_signal: 1
- gaze, vfx, socket_signal: 1

Raw SHA-256: `168d5fb2212b4d8922d7791f9a384fde1ed752e6886d55dd6de001fc9bb7d0b0`. Binary SHA-256: `6bdb9e7c75495acb4c6aa2e18428983dc80d1b5318c4d2dd9448649ea36ad480`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_client.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_drug_dealer.scene`

93 graph nodes, 117 edges; 23 event-bearing sections, 206 events; 60 screenplay lines, 11 screenplay options, 4 choice nodes.

Actors: drug_dealer (actor 0, community); drug_dealer_friend (actor 1, community); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `Start1` → 237; `Start 3` → 730; `dealing` → 859.

Exits: `dealer friend leaves` → 315; `fear_001` → 250; `fear_002` → 255; `End 2` → 274.

End nodes: 250: `<omitted>`; 255: `<omitted>`; 274: `NonTerminating`; 315: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 110 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scnDialogLineEvent` | 39 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnGameplayTransitionEvent` | 3 | 4 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/23` |
| `scnIKEvent` | 6 | 4 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/15` |
| `scnLookAtEvent` | 48 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnPlaySkAnimEvent` | 60 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 3 | 4 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/22` |
| `scneventsEquipItemToPerformer` | 3 | 610 / 355 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 3 | 4 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/19` |
| `scneventsSocket` | 29 | 4 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/17` |
| `scneventsUnequipItemFromPerformer` | 1 | 637 / 421 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/20` |
| `scneventsVFXEvent` | 7 | 110 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 5
- speech: 5
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation: 1
- gaze, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, vfx: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `4c9e0b56918b78a1c5b25c1ac2ae470a1ba394b1b3e2038da98bd550c2062329`. Binary SHA-256: `3204e7fa8141d0692f8e939423bd934fcec813078088f6bf3de6888fdc64eea5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_drug_dealer.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_george.scene`

196 graph nodes, 225 edges; 40 event-bearing sections, 440 events; 117 screenplay lines, 17 screenplay options, 10 choice nodes.

Actors: Hank (actor 0, community); Georgina (actor 1, community); Johnny (actor 2, spawnDespawn); Maldonaldo (actor 3, findInContext); Georgina_TV (actor 4, findInContext); Player (actor 5, findInContext).

Entries: `main_scene_start` → 1; `reminder_start` → 922; `BACKUP` → 1851.

Exits: `reminder_end` → 923; `scene_end` → 442.

End nodes: 442: `NonTerminating`; 923: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 828 / 389 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/20` |
| `scnDialogLineEvent` | 96 | 13 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scnGameplayTransitionEvent` | 4 | 571 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |
| `scnIKEvent` | 8 | 571 / 169 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnLookAtEvent` | 139 | 13 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnPlaySkAnimEvent` | 98 | 13 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 4 | 571 / 177 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/8` |
| `scneventsAttachPropToPerformer` | 4 | 13 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scneventsAttachPropToWorld` | 4 | 13 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 4 | 571 / 173 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/5` |
| `scneventsSocket` | 74 | 13 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 13
- speech, skeletal_animation, gaze: 9
- speech: 4
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, audio: 1
- socket_signal: 1

Raw SHA-256: `6e98bece0b7ecfb57000106884ac2908ce4c54f5d942ca3577f9db4df2d7bff8`. Binary SHA-256: `fdc9745062d7de81f22ca44dc2ddb118297f7c531ccef8aa2e4ff8642cba816c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_george.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_holocall_debrief.scene`

34 graph nodes, 42 edges; 8 event-bearing sections, 10 events; 10 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `start` → 49.

Exits: `end` → 2; `rejected_out` → 115.

End nodes: 2: `<omitted>`; 115: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 10 | 45 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8

Raw SHA-256: `7d4841863a26a1a8a3e6a14c6ae343c7098641414ff46e68747795f8aaa77186`. Binary SHA-256: `ebd01b647766a82721dc107b73de0a156424f594a35fa3998f3830d23af769fa`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_holocall_debrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_holocall_prebrief.scene`

21 graph nodes, 24 edges; 1 event-bearing sections, 5 events; 5 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 75.

End nodes: 2: `<omitted>`; 75: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 45 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `92b9cb191bb7c3e94e08e4f87a37e27b104ae438b1996e79c7b5abbcf97e9986`. Binary SHA-256: `0fdad64071d224f4e833b6e7ae9117930daa17b727d7a9673540a428b6678d8a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_holocall_prebrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_johnny.scene`

36 graph nodes, 35 edges; 7 event-bearing sections, 24 events; 10 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `overhear` → 38; `prosecutors` → 131; `Start1` → 24.

Exits: `End 0` → 2; `End2` → 40; `End3` → 133; `End1` → 26.

End nodes: 2: `<omitted>`; 26: `<omitted>`; 40: `<omitted>`; 133: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 3 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 5 | 42 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scneventsSocket` | 10 | 29 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 2
- speech, gaze: 1
- socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `ba05fec519b0f14b9ccd29aea244862029bafd360a2dd8af90fba4cc7753924a`. Binary SHA-256: `c5ed3fa7596201e7a6fb3eb6ff22c19773358e5e4413622c73b4e80f8176e4ed`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_johnny.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_scavs.scene`

37 graph nodes, 46 edges; 6 event-bearing sections, 92 events; 26 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Prosecutor_001 (actor 0, community); Prosecutor_002 (actor 1, community); Clerk (actor 2, community); hooker_1 (actor 3, community); hooker_2 (actor 4, community); hooker_3 (actor 5, community); hooker_4 (actor 6, community); businessman (actor 7, community); hooker_5 (actor 8, community); Player (actor 9, findInContext).

Entries: `prosecutors_start` → 89.

Exits: `prosecutors_end` → 91.

End nodes: 91: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 93 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scnDialogLineEvent` | 14 | 93 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 48 | 93 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 14 | 93 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 14 | 93 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, gaze: 1
- gaze, socket_signal: 1

Raw SHA-256: `d22815d0527bdc2a29509fea46a5c61ffa7ccf7dd9756b845f46b9083ee582ed`. Binary SHA-256: `e9ec066acc4f834b279800c7926731da75504bf40ca2436d17cbd3eaea5dee3d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_scavs.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_violent_guy.scene`

41 graph nodes, 44 edges; 9 event-bearing sections, 67 events; 20 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: violent_guy (actor 0, community); angry_guard (actor 1, community); Player (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `End1` → 316; `fear` → 264.

End nodes: 264: `<omitted>`; 316: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 85 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scnChangeIdleAnimEvent` | 3 | 13 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 17 | 13 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 85 / 104 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/10` |
| `scnIKEvent` | 4 | 85 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scnLookAtEvent` | 3 | 13 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 18 | 16 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnUnmountEvent` | 2 | 85 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 2 | 85 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |
| `scneventsSocket` | 14 | 13 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 3
- speech, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, audio, socket_signal: 1
- speech, socket_signal: 1

Raw SHA-256: `90ee0296c3176cac97b43e0c371d24b734a81cc779bafd7a45c219cb2c2a7162`. Binary SHA-256: `dd39de97013ab004d4ba293ef7b04e6c5de251c7f1f0a3ab8cfa21c0aced1706`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_violent_guy.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_waitress.scene`

29 graph nodes, 31 edges; 6 event-bearing sections, 43 events; 13 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: waitress (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 1` → 21; `fear` → 148.

End nodes: 21: `<omitted>`; 148: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 9 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 8 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 8 | 6 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsEquipItemToPerformer` | 5 | 26 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scneventsSocket` | 12 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 6 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- gaze, props_equipment, socket_signal: 1
- props_equipment, socket_signal: 1
- gaze: 1

Raw SHA-256: `4271d6ba08aec3571afc7ef69c64f4240c70ee41451eddd7ec2dec659e18ec92`. Binary SHA-256: `c4b2757e822b6302c0cbd5d1d19b682a76a83029849d8dbe03ee696e8cc90a13`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_06_zembinsky\scenes\sts_ep1_06_waitress.scene" --events
```

