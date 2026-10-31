# Gig: Treating Symptoms: scene presentation

Journal identity: `ep1/quests/street_stories/sts_ep1_12`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-sts_ep1_12.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_after_sts_patrol_call_out.scene`

7 graph nodes, 6 edges; 3 event-bearing sections, 12 events; 12 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: VB_patrol_caller (actor 0, community); ALAN_NOEL (actor 1, community).

Entries: `alan_dead_milko_dead` → 8; `milko_alive` → 1; `alan_alive_milko_dead` → 18.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 12 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `bc700c77a62efe678670c8b59f4cf29f9b8c8644d98c12ac8dafcb1aea738d66`. Binary SHA-256: `8c4f1e27ea8eeb83687097d3e3abb94b82ae873274f568368b780bf07f60a9ae`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_after_sts_patrol_call_out.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_courier_scene.scene`

178 graph nodes, 236 edges; 39 event-bearing sections, 278 events; 75 screenplay lines, 30 screenplay options, 12 choice nodes.

Actors: Courier (actor 0, community); Voodoboy (actor 1, community); Player (actor 2, findInContext).

Entries: `Start` → 1; `pre run away` → 1009; `combat` → 202; `scream` → 346; `greeting` → 352; `courier_escape_line` → 974.

Exits: `success` → 2; `fail` → 301; `run_away_terminate` → 1019; `run_away` → 222; `ran_away_finally` → 1069; `courier_escapes` → 961; `End 5` → 968.

End nodes: 2: `NonTerminating`; 222: `NonTerminating`; 301: `<omitted>`; 961: `<omitted>`; 968: `<omitted>`; 1019: `<omitted>`; 1069: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 135 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/9` |
| `scnChangeIdleAnimEvent` | 10 | 47 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/2` |
| `scnDialogLineEvent` | 61 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 7 | 262 / 456 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/14` |
| `scnIKEvent` | 14 | 262 / 445 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/8` |
| `scnLookAtEvent` | 34 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 60 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnUnmountEvent` | 7 | 262 / 461 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/18` |
| `scneventsEquipItemToPerformer` | 2 | 176 / 250 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 7 | 262 / 457 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/15` |
| `scneventsSocket` | 67 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 1 | 176 / 253 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/4` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 329 / 583 | `/Data/RootChunk/sceneGraph/Data/graph/57/Data/events/9` |
| `scneventsVFXDurationEvent` | 1 | 137 / 206 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/3` |
| `scneventsVFXEvent` | 4 | 135 / 195 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- speech, skeletal_animation, gaze, socket_signal: 5
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze: 2
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `6478b9eca190f19146cc280c6ba96a8280b0904ad0f31f69c25710417ff03b10`. Binary SHA-256: `b1ce1f5abcc6dfcb1cd442295478207618b9475840126d3fd871c0508eee7a40`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_courier_scene.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_courier_scene_scolding_looped.scene`

6 graph nodes, 6 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Voodoboy (actor 0, community); Courier (actor 1, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `out_sts` → 40.

End nodes: 2: `<omitted>`; 40: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `27c5c674445a58261c208dcffa0a215647e2c627b574401fe01224af7171d535`. Binary SHA-256: `ad733f2cb1f313647e59b7b43627b33e1251955ff275dbd4d733f9d0a9e5f7f6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_courier_scene_scolding_looped.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_droid_den.scene`

25 graph nodes, 25 edges; 5 event-bearing sections, 11 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: droid_1 (actor 0, community); droid_4 (actor 1, community); droid_5 (actor 2, community); security_system (actor 3, spawnDespawn); miniboss (actor 4, community); Player (actor 5, findInContext).

Entries: `droid_den` → 1.

Exits: `term_sec_sys` → 46; `n_term_lookat` → 26; `n_term_sec_sys` → 42.

End nodes: 26: `NonTerminating`; 42: `NonTerminating`; 46: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnDialogLineEvent` | 4 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 3 | 99 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, audio: 1
- speech, audio: 1
- socket_signal: 1
- audio: 1
- speech, socket_signal: 1

Raw SHA-256: `a43f7f461aad7bdebea76cf19e2ab45da1269afa78c4b0207d9a78d17e872124`. Binary SHA-256: `97475003017511cdf96990a86aa172a171b9495711a873d123cd5d89840c2f61`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_droid_den.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_final_scene.scene`

173 graph nodes, 218 edges; 51 event-bearing sections, 357 events; 106 screenplay lines, 24 screenplay options, 9 choice nodes.

Actors: Alan_noel (actor 0, community); target (actor 1, community); droid_1 (actor 2, community); droid_4 (actor 3, community); droid_5 (actor 4, community); Johnny (actor 5, spawnDespawn); Player (actor 6, findInContext).

Entries: `Start 0` → 1; `gate_kick` → 1473; `vfx_bugfix` → 1659; `hurry_up` → 481; `camera_scan` → 506; `Start 7` → 1379.

Exits: `End peace` → 29; `combat` → 214; `gate_done` → 1487; `vfx_bugfix_o` → 1665; `hurry_up_o` → 482.

End nodes: 29: `NonTerminating`; 214: `<omitted>`; 482: `<omitted>`; 1487: `<omitted>`; 1665: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1476 / 1128 | `/Data/RootChunk/sceneGraph/Data/graph/132/Data/events/1` |
| `scnChangeIdleAnimEvent` | 11 | 2 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/7` |
| `scnDialogLineEvent` | 80 | 2 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 222 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/16` |
| `scnIKEvent` | 6 | 222 / 153 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/9` |
| `scnLookAtEvent` | 50 | 2 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 99 | 2 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnUnmountEvent` | 3 | 222 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 3 | 222 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/12` |
| `scneventsSocket` | 60 | 2 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsVFXDurationEvent` | 1 | 1179 / 891 | `/Data/RootChunk/sceneGraph/Data/graph/88/Data/events/0` |
| `scneventsVFXEvent` | 40 | 2 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 7
- speech, skeletal_animation, gaze, socket_signal: 6
- speech, skeletal_animation: 4
- vfx: 4
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 3
- speech, skeletal_animation, gaze, vfx, socket_signal: 3
- speech, gaze: 3
- speech, skeletal_animation, vfx, socket_signal: 3
- speech: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, vfx: 2
- speech, skeletal_animation, gaze: 2
- speech, skeletal_animation, idle_animation, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, vfx: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx: 1
- idle_animation, vfx: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1

Raw SHA-256: `dad7a4c984717525d892053b6d8d567b2187ecc43f900529aabce906a90d4d45`. Binary SHA-256: `843402a53fda4aaa804c669cfe6a2a080b137f2dd95f5ee721ee9899caa089f9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_final_scene.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_holocall_debrief.scene`

31 graph nodes, 36 edges; 2 event-bearing sections, 9 events; 9 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: MrHands (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `not_rejectable_q303_start` → 114.

Exits: `End 0` → 3; `not_rejectable_q303_end` → 119; `rejected_out` → 60.

End nodes: 3: `<omitted>`; 60: `<omitted>`; 119: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 9 | 30 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `0fc5701880094783862931d285da46050ad26b90d60268f0819196cf1d873872`. Binary SHA-256: `3939b4073da3832d4a6508d7e356b74b9f315e65aae1efc26c31507090a51bfa`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_holocall_debrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_holocall_prebrief.scene`

21 graph nodes, 24 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: MrHands (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start1` → 4.

Exits: `End 1` → 43; `rejected_out` → 75.

End nodes: 43: `<omitted>`; 75: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 33 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `2d75d32084f878308d5c40f5df85d004489720616a2596fb773992d1d2222dab`. Binary SHA-256: `9c97fc7ab7a402d7fbe63d2fa6af5a5e86599f3b91d0d49049f42477eddc378c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_holocall_prebrief.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_outside_voodoboys_chat.scene`

4 graph nodes, 4 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Voodoboy_2 (actor 0, community); Voodoboy_1 (actor 1, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `614e76e262f2132cb9a562b134b2e7cb778a31e22c1af1f937308f90c0948274`. Binary SHA-256: `8f7fa97b28704d44e41e1f25d4ea623b6a61c9348e5e9268c1fac7584d421a04`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_outside_voodoboys_chat.scene" --events
```

## `ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_voodoboys_reception_argue_scene.scene`

3 graph nodes, 2 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Voodoboy_upper (actor 0, community); Voodoboy_down (actor 1, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `89a117591dd76882782b60e0170c8ecc76f2d52431e12320b72901fc946ca249`. Binary SHA-256: `4e3954012b0bf1a30c54e2f10518f92883f6e27963dbdaa353f19dd13e7b6dc3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\openworld\street_stories\sts_ep1_12\scenes\sts_ep1_12_voodoboys_reception_argue_scene.scene" --events
```

