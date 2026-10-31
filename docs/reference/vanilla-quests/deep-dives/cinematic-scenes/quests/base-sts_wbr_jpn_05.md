# Gig: Wakako's Favorite: scene presentation

Journal identity: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_05`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wbr_jpn_05.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\scenes\sts_wbr_jpn_05_civilian_chats.scene`

5 graph nodes, 5 edges; 2 event-bearing sections, 8 events; 5 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: civilian_001 (actor 0, community); civilian_002 (actor 1, community).

Entries: `jpn_05_chats_civilian_001_start` → 4.

Exits: `jpn_05_chats_civilian_001_end` → 5.

End nodes: 5: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 4 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 1
- gaze: 1

Raw SHA-256: `93b8bc7ed5b3bd9658b136b809f7d449a81301700de9a2b234a775d557a6c503`. Binary SHA-256: `08732f41eafc871c4fbf7a795891e6513f0f496af8536a5b457373f2031e83ab`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\scenes\sts_wbr_jpn_05_civilian_chats.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\scenes\sts_wbr_jpn_05_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 3 events; 1 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Wakako (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 286.

End nodes: 2: `<omitted>`; 286: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 28 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 1 | 28 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 1 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation, gaze: 1

Raw SHA-256: `8d67998828747b7be026bbc5a324d8ba049a54b69406158808d184f02a104def`. Binary SHA-256: `cd7124a9fa31b58591ff83ec858d39fed541f8c7df2b10b3734371363798e68e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\scenes\sts_wbr_jpn_05_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\scenes\sts_wbr_jpn_05_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 4 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: wakako (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 28 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 2 | 28 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 1 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation, gaze: 1

Raw SHA-256: `5c1fb01b683d788eff7195157c7a1bcc44fab86ac13b16889aa820624925837b`. Binary SHA-256: `521a41e7c2d5587fa8d47a001f4e311388f98bb061ba1577ceb276b2a16581be`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\scenes\sts_wbr_jpn_05_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\scenes\sts_wbr_jpn_05_johnny.scene`

12 graph nodes, 13 edges; 2 event-bearing sections, 10 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 4 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 2 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 1
- gaze: 1

Raw SHA-256: `bf29d554d7627abe964c96b8e0c5fb1bbc29a7a51f5253c60f9097929c262625`. Binary SHA-256: `4bfb78bd6e670474bb055358d4189732f34901e3d03beed052edc4fb4c512946`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\scenes\sts_wbr_jpn_05_johnny.scene" --events
```

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\scenes\sts_wbr_jpn_05_ren_cheng.scene`

65 graph nodes, 79 edges; 16 event-bearing sections, 130 events; 33 screenplay lines, 8 screenplay options, 5 choice nodes.

Actors: Chang_Hoon_Nam (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `ren_talk_001_proper_talk_start` → 16; `cooldown` → 386.

Exits: `ren_talk_001_proper_talk_end` → 17.

End nodes: 17: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 108 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnDialogLineEvent` | 28 | 19 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 257 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/11` |
| `scnIKEvent` | 2 | 257 / 232 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/4` |
| `scnLookAtEvent` | 27 | 108 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 29 | 19 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 257 / 239 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/10` |
| `scneventsEquipItemToPerformer` | 1 | 282 / 296 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 1 | 257 / 237 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/9` |
| `scneventsSocket` | 30 | 108 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 6
- speech: 3
- gaze: 2
- speech, skeletal_animation: 1
- speech, socket_signal: 1
- idle_animation, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1

Raw SHA-256: `470d5b63006bae24a69a1b782d16bcce31a80b168d3748aa55f464597a325f7a`. Binary SHA-256: `62c1735c551152615aa1e0ec441149d57e143ed0670f90e7c88e3a79e84d5e77`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_05\scenes\sts_wbr_jpn_05_ren_cheng.scene" --events
```

