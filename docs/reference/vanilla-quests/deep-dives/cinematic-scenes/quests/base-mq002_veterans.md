# Gun Music: scene presentation

Journal identity: `quests/minor_quest/mq002_veterans`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq002_veterans.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene`

130 graph nodes, 154 edges; 33 event-bearing sections, 262 events; 86 screenplay lines, 18 screenplay options, 8 choice nodes.

Actors: Carol (actor 0, spawnSet); Teddy (actor 1, spawnSet); Cassidy (actor 2, spawnSet); Scav_leader (actor 3, community); nomad_01 (actor 4, community); nomad_02 (actor 5, community); scav_sniper (actor 6, community); scav_02 (actor 7, community); scav_03 (actor 8, community); scav_04 (actor 9, community); scav_01 (actor 10, community); scav_05 (actor 11, community); van (actor 12, community); Player (actor 13, findInContext).

Entries: `Start 0` → 1; `background_overhead` → 4; `idles` → 395; `interruption_combat` → 311; `entered_area` → 66.

Exits: `background_overhead_out` → 5; `to_combat` → 10; `to_outcome` → 105; `interruption_combat_out` → 312; `entered_area_out` → 71.

End nodes: 5: `<omitted>`; 10: `<omitted>`; 71: `<omitted>`; 105: `<omitted>`; 312: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 13 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnChangeIdleAnimEvent` | 11 | 16 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scnDialogLineEvent` | 84 | 7 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 156 / 520 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/20` |
| `scnIKEvent` | 2 | 156 / 510 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/11` |
| `scnLookAtEvent` | 45 | 13 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnPlaySkAnimEvent` | 48 | 13 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnUnmountEvent` | 1 | 156 / 519 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/19` |
| `scneventsEquipItemToPerformer` | 1 | 13 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 1 | 156 / 515 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/16` |
| `scneventsSocket` | 54 | 13 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scneventsUnequipItemFromPerformer` | 1 | 56 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/5` |
| `scneventsVFXDurationEvent` | 2 | 156 / 504 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, skeletal_animation, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, audio: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, gaze: 2
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation: 1
- gaze, socket_signal: 1

Raw SHA-256: `820fa7e70deea1b685f3a2e4fbd9110285bce7678336aecac9870dc7ea41c00e`. Binary SHA-256: `d2020c4ffa9b231640945a26c1c4309aa24506a8fed192a125d8a7f5fd0ad603`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene" --events
```

## `base\quest\minor_quests\mq002\scenes\mq002_02_combat.scene`

6 graph nodes, 4 edges; 2 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Teddy (actor 0, spawnSet); Cassidy (actor 1, spawnSet); Carol (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `veterans_banter` → 6; `combat_starts` → 1.

Exits: `veterans_banter_out` → 7; `combat_starts_out` → 2.

End nodes: 2: `<omitted>`; 7: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `acb79c8b9554309026ada87d91e579060d85b1cc372ad6e6a221b952e9d404bd`. Binary SHA-256: `09306aecf3598b2f50523637f4986f7afaf0acaec0977c14a31964b95cc98496`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq002\scenes\mq002_02_combat.scene" --events
```

## `base\quest\minor_quests\mq002\scenes\mq002_03_summary.scene`

85 graph nodes, 94 edges; 14 event-bearing sections, 139 events; 25 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Carol (actor 0, spawnSet); Cassidy (actor 1, spawnSet); Teddy (actor 2, spawnSet); van (actor 3, community); nomad_car_1 (actor 4, community); nomad_car_2 (actor 5, community); Player (actor 6, findInContext).

Entries: `Start 0` → 1; `Start 2` → 192; `Start1` → 217; `Start 3` → 230.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 19 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnGameplayTransitionEvent` | 3 | 12 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/22` |
| `scnIKEvent` | 6 | 12 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/7` |
| `scnLookAtEvent` | 24 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 28 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPoseCorrectionEvent` | 4 | 12 / 80 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/16` |
| `scnUnmountEvent` | 3 | 12 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/21` |
| `scneventsEquipItemToPerformer` | 4 | 8 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 3 | 12 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/19` |
| `scneventsSocket` | 33 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsUnequipItemFromPerformer` | 1 | 257 / 543 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/6` |
| `scneventsUnequipItemFromPerformerByItem` | 3 | 27 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 2
- socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, props_equipment, socket_signal: 1
- animation_state: 1

Raw SHA-256: `c4e36074328f0353377f21e8edf48e7322d27b214e2ba339dc3593e3cc54a706`. Binary SHA-256: `e3cabed0257cd118e8a7d0967a3e397ad6613c1f9212752f70a5c1b7909f6eb7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq002\scenes\mq002_03_summary.scene" --events
```

## `base\quest\minor_quests\mq002\scenes\mq002_04_nomads_fluff.scene`

11 graph nodes, 13 edges; 6 event-bearing sections, 22 events; 10 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: Nomad_01 (actor 0, community); Nomad_02 (actor 1, community); Player (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 10 | 8 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnLookAtEvent` | 12 | 8 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 6

Raw SHA-256: `2cfde561e121f8121c0574134b4a9be24d8d91441898543497d2a5814c8b908a`. Binary SHA-256: `bb91baf729ac73fd03d7f621cf2d7c86d91545eb70784d2789fa7c1284a68fe5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq002\scenes\mq002_04_nomads_fluff.scene" --events
```

