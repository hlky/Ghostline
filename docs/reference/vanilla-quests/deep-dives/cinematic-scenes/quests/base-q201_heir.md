# Where is My Mind?: scene presentation

Journal identity: `quests/main_quest/epilogues/q201_heir`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q201_heir.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\media\finalboards\scenes\fb_hanako_refused.scene`

21 graph nodes, 20 edges; 2 event-bearing sections, 32 events; 8 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: hanako (actor 0, spawnDespawn).

Entries: `Fb_hanako_refused` → 4.

Exits: `out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 10 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 7 | 10 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnLookAtEvent` | 3 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 14 | 10 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsCameraEvent` | 2 | 10 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsCameraParamsEvent` | 2 | 10 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 1 | 10 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- camera: 1

Raw SHA-256: `a0f057e6cd0d8132a1b038d22584f5de4dcac8a86ef6f924552b90669033879f`. Binary SHA-256: `2759be48d1f7aaf4a3e5eedf3dd4a8c9a4260715eef13b7ddcbe81d23b3ddf74`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_hanako_refused.scene" --events
```

## `base\media\finalboards\scenes\fb_judy.scene`

96 graph nodes, 95 edges; 10 event-bearing sections, 193 events; 35 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: judy (actor 0, spawnDespawn).

Entries: `Fb_judy_suicide` → 4; `Fb_judy_lover_afterlife` → 65; `Fb_judy_lover_johnny` → 66; `Fb_judy_stranger` → 67; `Fb_judy_friend` → 68.

Exits: `out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnChangeIdleAnimEvent` | 27 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 30 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnLookAtEvent` | 30 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 77 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsCameraEvent` | 10 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsCameraParamsEvent` | 10 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 7 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- camera: 5
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1

Raw SHA-256: `d6b146ecac79b5643826f0fa89ced7465e82df91dff78fdfcf731fa6b18b3a42`. Binary SHA-256: `8f67a7f7e33ef1e83de83fc57aff2e6badd6dcd09532b827e5d47bf5b0db81fa`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_judy.scene" --events
```

## `base\media\finalboards\scenes\fb_judy_nomads_hut.scene`

18 graph nodes, 17 edges; 2 event-bearing sections, 41 events; 8 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: judy (actor 0, spawnDespawn); v (actor 1, findInContext); Player (actor 2, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 7 | 4 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnLookAtEvent` | 8 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 13 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsCameraEvent` | 2 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraParamsEvent` | 2 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 1 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- camera: 1

Raw SHA-256: `2c899a9190b6b4e0b03c3c53c5e60c8ed9a3a97618feb8916fb82fe723d8a964`. Binary SHA-256: `a4ac8010521a421dbf5849ecfaa284a7fd7074041f0ffcfb2b216bd6ecc2c5d8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_judy_nomads_hut.scene" --events
```

## `base\media\finalboards\scenes\fb_kerry.scene`

86 graph nodes, 85 edges; 10 event-bearing sections, 318 events; 34 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: kerry (actor 0, spawnDespawn).

Entries: `Fb_kerry_suicide` → 4; `Fb_kerry_lover_nomad` → 54; `Fb_kerry_lover_afterlife` → 55; `Fb_kerry_lover_johnny` → 56; `Fb_kerry_friend` → 57.

Exits: `out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 22 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 29 | 6 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnLookAtEvent` | 23 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 219 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsCameraEvent` | 10 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsCameraParamsEvent` | 10 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 5 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 5
- camera: 5

Raw SHA-256: `846aea1ff182af7f8b4a2e81db3653aa5ade7b07511e989fa922a675968db732`. Binary SHA-256: `9f412161552246951b22f838227128a507a5db6239fb96c8db1af79152fa49ce`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_kerry.scene" --events
```

## `base\media\finalboards\scenes\fb_misty.scene`

87 graph nodes, 86 edges; 10 event-bearing sections, 154 events; 31 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: misty (actor 0, spawnDespawn).

Entries: `Fb_misty_suicide` → 1; `Fb_misty_nomads` → 40; `Fb_misty_afterlife` → 41; `Fb_misty_johnny` → 42; `Fb_misty_corpo` → 43.

Exits: `out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 26 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 26 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtEvent` | 24 | 4 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 59 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsCameraEvent` | 4 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraParamsEvent` | 10 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 5 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 5
- camera: 5

Raw SHA-256: `760fe882bebdbf922856d30428844295402e89fde5ff34c691dfffa2357d905b`. Binary SHA-256: `8b03af826e925c91c54ec175f183346ed9a412c38fefd686c4130c2b84ac9937`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_misty.scene" --events
```

## `base\media\finalboards\scenes\fb_mitch.scene`

49 graph nodes, 48 edges; 6 event-bearing sections, 185 events; 19 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: mitch (actor 0, spawnDespawn).

Entries: `Fb_mitch_grateful` → 47; `Fb_mitch_friend` → 48; `Fb_mitch_stranger` → 4.

Exits: `out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 8 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 16 | 8 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnLookAtEvent` | 4 | 8 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 139 | 8 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsCameraEvent` | 6 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraParamsEvent` | 6 | 8 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 3 | 8 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 3
- camera: 3

Raw SHA-256: `21abdb9fbd6b01874d19cc30d296d52840e1c4e857f2a98e61c0f5730c1af0d4`. Binary SHA-256: `3bf6c4804576e7144b023b490421a4d3cb736b908ff692f39673eabbd4676dcb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_mitch.scene" --events
```

## `base\media\finalboards\scenes\fb_panam.scene`

103 graph nodes, 102 edges; 12 event-bearing sections, 227 events; 40 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: panam (actor 0, spawnDespawn); mitch (actor 1, findInContext).

Entries: `Fb_panam_suicide` → 4; `Fb_panam_lover_nomad` → 64; `Fb_panam_lover_afterlife` → 65; `Fb_panam_lover_johnny` → 66; `Fb_panam_friend` → 67; `Fb_panam_stranger` → 68.

Exits: `out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 38 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 34 | 6 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scnLookAtEvent` | 24 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 101 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsCameraEvent` | 12 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsCameraParamsEvent` | 12 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 6 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 6
- camera: 6

Raw SHA-256: `66e9a7dd319c10a8f1cb6b29a013a77fbba1daf55309e1209c3ca2a2933d073c`. Binary SHA-256: `7343489367085e2c182d69b6c9187d38cd172509649564c7697d577f795be177`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_panam.scene" --events
```

## `base\media\finalboards\scenes\fb_peralez.scene`

35 graph nodes, 34 edges; 4 event-bearing sections, 77 events; 14 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: peralez (actor 0, spawnDespawn).

Entries: `Fb_peralez_happy` → 1; `Fb_peralez_paranoid` → 18.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 12 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnLookAtEvent` | 5 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 39 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsCameraEvent` | 4 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraParamsEvent` | 4 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 2 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 2
- camera: 2

Raw SHA-256: `a076831a01f96d9b9e2af0482f8568c950acb64e265120812b83aa6e4c93b527`. Binary SHA-256: `64d8dfbacc800803b9b18d585bf091cd06c0648f274fc07152b7723efaf19c9c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_peralez.scene" --events
```

## `base\media\finalboards\scenes\fb_river.scene`

101 graph nodes, 100 edges; 12 event-bearing sections, 346 events; 47 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: river (actor 0, spawnDespawn); Joss (actor 1, findInContext); Dorian (actor 2, findInContext); Randy (actor 3, findInContext).

Entries: `Fb_river_suicide` → 4; `Fb_river_lover_nomad` → 59; `Fb_river_lover_afterlife` → 60; `Fb_river_lover_johnny` → 61; `Fb_river_friend` → 62; `Fb_river_randy_dead` → 63.

Exits: `out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 21 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 41 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnLookAtEvent` | 23 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 231 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsCameraEvent` | 12 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraParamsEvent` | 12 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 6 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 6
- camera: 6

Raw SHA-256: `110dfa338c61aa4a83e6ac02ee80b07293ed8c1ceda0d0eeb5f1217e5218f684`. Binary SHA-256: `3d9160c49edbcfbfa7496d2e7517ea87287276f1a573b057d723425ef1566f95`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_river.scene" --events
```

## `base\media\finalboards\scenes\fb_rogue.scene`

53 graph nodes, 52 edges; 6 event-bearing sections, 89 events; 20 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: rogue (actor 0, spawnDespawn).

Entries: `Fb_rogue_friend` → 4; `Fb_rogue_johnny` → 47; `Fb_rogue_stranger` → 48.

Exits: `out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 12 | 10 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 17 | 10 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtEvent` | 14 | 10 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 31 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsCameraEvent` | 6 | 10 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraParamsEvent` | 6 | 10 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 3 | 10 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 3
- camera: 3

Raw SHA-256: `2e568ad8f64307c344690dd3ae8e98591308fac26e07d2dbad8f6c8c413c2b83`. Binary SHA-256: `5e4c8fc2f4302c5bdc443f0752a185682bd15d048d889eaa440c62837f674427`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_rogue.scene" --events
```

## `base\media\finalboards\scenes\fb_saul.scene`

49 graph nodes, 48 edges; 6 event-bearing sections, 162 events; 18 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: saul (actor 0, spawnDespawn).

Entries: `Fb_saul_grateful` → 46; `Fb_saul_friend` → 47; `Fb_saul_stranger` → 4.

Exits: `out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 15 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtEvent` | 16 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 112 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsCameraEvent` | 6 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsCameraParamsEvent` | 6 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsSocket` | 3 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 3
- camera: 3

Raw SHA-256: `c4e0665a73f3f0b38b69d5d98d5afc9ac8575352066716d8ec23cde6131b7be7`. Binary SHA-256: `1a6b57fa896e6c3ba7591c2b1c81e5e4e2723c4e4297266d23e7da5a70ccf85e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_saul.scene" --events
```

## `base\media\finalboards\scenes\fb_takemura.scene`

36 graph nodes, 35 edges; 4 event-bearing sections, 58 events; 13 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: takemura (actor 0, spawnDespawn).

Entries: `Fb_takemura_depressed` → 37; `Fb_takemura_bodyguard` → 4.

Exits: `out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 11 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnLookAtEvent` | 7 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 23 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsCameraEvent` | 4 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsCameraParamsEvent` | 4 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 2 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 2
- camera: 2

Raw SHA-256: `507bf7e49702bac3deddcf13014950b204e30ee723dd669e9757e476e58e7453`. Binary SHA-256: `3ff31883ede7cff5abdd5c8900641d16bbfd23eafbbea2c5414963fa7418aca5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_takemura.scene" --events
```

## `base\media\finalboards\scenes\fb_victor.scene`

82 graph nodes, 81 edges; 10 event-bearing sections, 266 events; 31 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: victor_vector (actor 0, spawnDespawn); misty (actor 1, findInContext).

Entries: `Fb_victor_suicide` → 4; `Fb_victor_nomad` → 29; `Fb_victor_afterlife` → 30; `Fb_victor_corpo` → 31; `Fb_victor_johnny` → 43.

Exits: `out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 21 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 26 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnLookAtEvent` | 22 | 6 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scnPlaySkAnimEvent` | 172 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsCameraEvent` | 10 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsCameraParamsEvent` | 10 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 5 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 5
- camera: 5

Raw SHA-256: `c9169511ad6124cdb31c9ceab7670a379c46cb1b686b4fed12876fe65783c621`. Binary SHA-256: `ee3bdaeea5d6dcd7568e450c9db36fcabe7b91f45ab57762baeaf37f6bd41d00`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_victor.scene" --events
```

## `base\media\finalboards\scenes\fb_welles.scene`

98 graph nodes, 97 edges; 8 event-bearing sections, 227 events; 25 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: mama_welles (actor 0, spawnDespawn).

Entries: `Fb_welles_suicide` → 4; `Fb_welles_nomad` → 47; `Fb_welles_afterlife` → 48; `Fb_welles_johnny` → 49.

Exits: `out` → 5.

End nodes: 5: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 18 | 6 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 21 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtEvent` | 8 | 6 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scnPlaySkAnimEvent` | 159 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsCameraEvent` | 8 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraParamsEvent` | 8 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 5 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 4
- camera: 4

Raw SHA-256: `a62be7df2cf513f6d1701812c249b78edc6be7e58622f0ec38f8cbab52452d19`. Binary SHA-256: `2c20b1e9951a7150affb1d8d325ef8206a3444b268a1fe237ba1b7b789e81fbf`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\media\finalboards\scenes\fb_welles.scene" --events
```

## `base\quest\main_quests\epilogue\q201\scenes\q201_01_cyberspace.scene`

197 graph nodes, 234 edges; 43 event-bearing sections, 410 events; 119 screenplay lines, 25 screenplay options, 8 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 51 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnChangeIdleAnimEvent` | 15 | 51 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scnDialogLineEvent` | 112 | 50 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 5 | 55 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/26` |
| `scnIKEvent` | 10 | 55 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/16` |
| `scnLookAtEvent` | 43 | 51 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scnPlaySkAnimEvent` | 105 | 51 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnUnmountEvent` | 5 | 55 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/25` |
| `scneventsAttachPropToPerformer` | 6 | 55 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/27` |
| `scneventsAttachPropToWorld` | 5 | 93 / 318 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 5 | 55 / 111 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/20` |
| `scneventsSocket` | 87 | 51 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/9` |
| `scneventsVFXEvent` | 7 | 93 / 305 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- skeletal_animation, socket_signal: 6
- speech, skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, props_equipment, vfx, socket_signal: 4
- speech, skeletal_animation, idle_animation, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, idle_animation, gaze, socket_signal: 3
- speech, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx, socket_signal: 1
- speech, idle_animation: 1

Raw SHA-256: `8efbe589d43985608e29777af0d262c27414294b779ae488f2be31a6b8c0dc8a`. Binary SHA-256: `4c9f19fc3d8c685820af684cee51b33a495121076dcfb0ff36c60fed9e3e7c58`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q201\scenes\q201_01_cyberspace.scene" --events
```

## `base\quest\main_quests\epilogue\q201\scenes\q201_02_operation_room.scene`

261 graph nodes, 312 edges; 53 event-bearing sections, 314 events; 90 screenplay lines, 16 screenplay options, 10 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Doctor_scientist (actor 1, community); Security_guard (actor 2, community); Hanako_Arasaka (actor 3, spawnSet); assistant (actor 4, community); v_tpp_female (actor 5, spawnDespawn); v_tpp_male (actor 6, spawnDespawn); V (actor 7, findInContext).

Entries: `day_0_start` → 1; `q201_mirror_start` → 1675; `Start 3` → 4929.

Exits: `day_0_nightmare_end` → 500; `q201_mirror_end` → 4911.

End nodes: 500: `<omitted>`; 4911: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 16 | 85 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/23` |
| `scnChangeIdleAnimEvent` | 3 | 85 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 64 | 85 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnGameplayTransitionEvent` | 6 | 85 / 82 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/45` |
| `scnIKEvent` | 12 | 85 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/14` |
| `scnLookAtEvent` | 56 | 85 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scnPlaySkAnimEvent` | 32 | 85 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 6 | 85 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/44` |
| `scneventsAttachPropToPerformer` | 3 | 85 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsAttachPropToWorld` | 3 | 85 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/19` |
| `scneventsCameraParamsEvent` | 18 | 85 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 6 | 85 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/43` |
| `scneventsSocket` | 73 | 85 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsVFXEvent` | 16 | 85 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, gaze: 5
- speech, gaze, socket_signal: 4
- skeletal_animation, gaze: 4
- skeletal_animation, audio, socket_signal: 3
- gaze, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- camera: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, audio: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, gaze, vfx: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- skeletal_animation, audio: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, camera, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- gaze: 1
- vfx, socket_signal: 1
- skeletal_animation, gaze, camera, audio, socket_signal: 1
- skeletal_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `394b17e5c60ce4a432e9c634b153e285d8eb716dd9aa9adfbe254ca3cfb7144e`. Binary SHA-256: `205ec7259ce1f40b3dcdeff220ea4781f4c5c5c26e807551b1d29e836b84e4fd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q201\scenes\q201_02_operation_room.scene" --events
```

## `base\quest\main_quests\epilogue\q201\scenes\q201_03_cabin_day_1.scene`

409 graph nodes, 511 edges; 113 event-bearing sections, 433 events; 128 screenplay lines, 47 screenplay options, 19 choice nodes.

Actors: Security_guard (actor 0, community); Doctor_scientist (actor 1, community); Haru_Kasai (actor 2, spawnSet); Kerry (actor 3, findInContext); River (actor 4, findInContext); Panam (actor 5, findInContext); Judy (actor 6, findInContext); Victor (actor 7, findInContext); jackie (actor 8, spawnDespawn); johnny (actor 9, spawnDespawn); Towfiq_Iqbal (actor 10, findInContext); V (actor 11, findInContext).

Entries: `day_1_start` → 12; `q201_reminder_connect_1` → 4797; `q201_reminder_connect_2` → 4798; `q201_reminder_test_1` → 4799; `q201_reminder_walk_1` → 4800; `Start 18` → 3760; `Start 19` → 3769; `Start 20` → 3799; `Start 17` → 3607; `day_1_nightmare_start` → 3241.

Exits: `day_1_nightmare_end` → 76; `day_1_end` → 3386.

End nodes: 76: `<omitted>`; 3386: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 28 | 182 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scnChangeIdleAnimEvent` | 18 | 182 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |
| `scnDialogLineEvent` | 105 | 14 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnIKEvent` | 4 | 1865 / 411 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/3` |
| `scnLookAtEvent` | 83 | 14 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 62 | 43 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPoseCorrectionEvent` | 6 | 281 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/19` |
| `scneventsAttachPropToPerformer` | 8 | 182 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scneventsAttachPropToWorld` | 4 | 2760 / 695 | `/Data/RootChunk/sceneGraph/Data/graph/108/Data/events/9` |
| `scneventsCameraParamsEvent` | 8 | 2763 / 715 | `/Data/RootChunk/sceneGraph/Data/graph/109/Data/events/7` |
| `scneventsSocket` | 91 | 14 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsVFXEvent` | 16 | 1865 / 410 | `/Data/RootChunk/sceneGraph/Data/graph/68/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 44
- speech, gaze: 10
- speech, gaze, socket_signal: 6
- speech, skeletal_animation, gaze: 6
- camera: 6
- speech, skeletal_animation, gaze, socket_signal: 5
- skeletal_animation, idle_animation, socket_signal: 5
- speech, skeletal_animation, socket_signal: 3
- skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 2
- vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, ik, vfx, socket_signal: 1
- skeletal_animation: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, vfx, socket_signal: 1
- speech, gaze, audio, socket_signal: 1
- idle_animation, vfx, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, ik, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, camera, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, gaze, audio: 1
- skeletal_animation, idle_animation, ik, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal: 1
- audio, vfx: 1
- gaze: 1

Raw SHA-256: `deffaa6d7e2a352b12a6e4dbb378b81b85ee96a36f576e2a113706340c9609cb`. Binary SHA-256: `2722379e7166d76c32662e91d745154ae095d5c17a2f0a86ef1f24aa8be96542`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q201\scenes\q201_03_cabin_day_1.scene" --events
```

## `base\quest\main_quests\epilogue\q201\scenes\q201_04_cabin_day_2.scene`

463 graph nodes, 583 edges; 122 event-bearing sections, 472 events; 128 screenplay lines, 56 screenplay options, 26 choice nodes.

Actors: Doctor_scientist (actor 0, community); Kerry (actor 1, findInContext); River (actor 2, findInContext); Panam (actor 3, findInContext); Judy (actor 4, findInContext); Victor (actor 5, findInContext); Gillean_Jordan (actor 6, findInContext); Player (actor 7, findInContext).

Entries: `day_2_start` → 78; `Start 20` → 4197; `Start 21` → 4284; `Start 22` → 5553; `day_2_nightmare_start` → 2679; `Start 23` → 5614; `Start 19` → 4055.

Exits: `q201_reminder_connect_1` → 5019; `q201_reminder_connect_2` → 5020; `q201_reminder_test_1` → 5021; `day_2_nightmare_end` → 2690; `day_2_end` → 1950.

End nodes: 1950: `<omitted>`; 2690: `<omitted>`; 5019: `NonTerminating`; 5020: `NonTerminating`; 5021: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 26 | 2121 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnChangeIdleAnimEvent` | 26 | 2121 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 85 | 2121 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 3976 / 1497 | `/Data/RootChunk/sceneGraph/Data/graph/215/Data/events/10` |
| `scnIKEvent` | 6 | 2313 / 194 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/4` |
| `scnLookAtEvent` | 81 | 2121 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnPlaySkAnimEvent` | 67 | 2121 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPoseCorrectionEvent` | 10 | 2121 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scnUnmountEvent` | 1 | 3976 / 1496 | `/Data/RootChunk/sceneGraph/Data/graph/215/Data/events/9` |
| `scneventsAttachPropToPerformer` | 14 | 2121 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsAttachPropToWorld` | 6 | 2397 / 479 | `/Data/RootChunk/sceneGraph/Data/graph/78/Data/events/10` |
| `scneventsCameraParamsEvent` | 19 | 2121 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 1 | 3976 / 1492 | `/Data/RootChunk/sceneGraph/Data/graph/215/Data/events/6` |
| `scneventsSocket` | 116 | 2121 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scneventsVFXEvent` | 13 | 2313 / 192 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 33
- camera: 12
- skeletal_animation, idle_animation, socket_signal: 10
- gaze: 8
- speech, gaze: 7
- speech, gaze, socket_signal: 6
- skeletal_animation, gaze: 6
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, gaze: 3
- speech, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, audio: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, ik, vfx, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, camera, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, socket_signal: 1
- speech, gaze, audio: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, camera, props_equipment, audio, socket_signal, animation_state: 1
- vfx, socket_signal: 1
- skeletal_animation, gaze, props_equipment, vfx, socket_signal: 1
- props_equipment: 1
- props_equipment, vfx, socket_signal: 1

Raw SHA-256: `4ce23e1f66d68c5b8ce9c1fbffc46a3ab741c5111ed5703fca53830a1d518a6c`. Binary SHA-256: `a2ebdb8221912ad888abbe56316bc91c119112719f11c4f3a106c83c730e26e6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q201\scenes\q201_04_cabin_day_2.scene" --events
```

## `base\quest\main_quests\epilogue\q201\scenes\q201_05_cabin_day_7.scene`

231 graph nodes, 251 edges; 41 event-bearing sections, 311 events; 166 screenplay lines, 29 screenplay options, 11 choice nodes.

Actors: Security_guard (actor 0, community); Doctor_scientist (actor 1, community); Haru_Kasai (actor 2, spawnSet); Kerry (actor 3, spawnSet); River (actor 4, spawnSet); Panam (actor 5, spawnSet); Judy (actor 6, spawnSet); Victor (actor 7, spawnSet); Player (actor 8, findInContext).

Entries: `q201_05_call_judy_IN` → 2285; `judy_not_in` → 2780; `q201_kerry_call_IN` → 2341; `kerry_no_in` → 2804; `Start 20` → 3041; `panam_no_in` → 2822; `q201_05_panam_call_IN` → 2377; `victor_no_in` → 2840; `river_call_in` → 2424; `victor_call_1_start` → 615; `hanako_call_in` → 2699; `river_not_in` → 2720.

Exits: `river_call_out` → 2770; `judy_not_out` → 2781; `q201_05_call_judy_OUT` → 2329; `kerry_no_out` → 2805; `panam_no_out` → 2823; `q201_kerry_call_OUT` → 2374; `victor_no_out` → 2841; `q203_05_panam_call_OUT` → 2422; `victor_call_1_end` → 617; `hanako_call_out` → 2701; `river_not_out` → 2721.

End nodes: 617: `<omitted>`; 2329: `<omitted>`; 2374: `<omitted>`; 2422: `<omitted>`; 2701: `<omitted>`; 2721: `<omitted>`; 2770: `<omitted>`; 2781: `<omitted>`; 2805: `<omitted>`; 2823: `<omitted>`; 2841: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 6. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 81 | 573 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnDialogLineEvent` | 161 | 573 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnPlaySkAnimEvent` | 46 | 585 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsSocket` | 23 | 573 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal: 17
- speech, skeletal_animation, idle_animation: 12
- speech, idle_animation: 5
- speech, idle_animation, socket_signal: 4
- speech, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech: 1

Raw SHA-256: `5c08c0f0e915fb2d650d548fb7a7f26a710f1d142892972a36d92e8b84f52d0d`. Binary SHA-256: `c351382e9b2b3e0ae9bf0672a2f09890e1bfa6b941d10f4660c11fc08d08e0c0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q201\scenes\q201_05_cabin_day_7.scene" --events
```

## `base\quest\main_quests\epilogue\q201\scenes\q201_06_cabin_day_8_to_29.scene`

339 graph nodes, 427 edges; 67 event-bearing sections, 408 events; 67 screenplay lines, 30 screenplay options, 16 choice nodes.

Actors: Doctor_scientist (actor 0, community); jackie (actor 1, spawnSet); Gillean_Jordan (actor 2, findInContext); Yorinobu (actor 3, findInContext); Player (actor 4, findInContext).

Entries: `day_8_29_start` → 1870; `Start 21` → 6445.

Exits: `day_29_end` → 2418.

End nodes: 2418: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 25 | 2405 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scnChangeIdleAnimEvent` | 51 | 2405 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnDialogLineEvent` | 38 | 2405 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnIKEvent` | 6 | 2694 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/8` |
| `scnLookAtEvent` | 49 | 2405 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/24` |
| `scnPlaySkAnimEvent` | 81 | 2405 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPoseCorrectionEvent` | 5 | 2405 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/15` |
| `scneventsAttachPropToNode` | 1 | 2409 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsAttachPropToPerformer` | 18 | 2405 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsAttachPropToWorld` | 13 | 2405 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/14` |
| `scneventsCameraParamsEvent` | 26 | 2405 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scneventsSocket` | 91 | 2405 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scneventsVFXEvent` | 4 | 4678 / 934 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/17` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- skeletal_animation, gaze: 6
- camera: 6
- speech, gaze: 4
- speech, skeletal_animation, idle_animation, audio, socket_signal: 4
- skeletal_animation, idle_animation, socket_signal: 4
- skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, socket_signal: 2
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 2
- gaze: 2
- speech, camera, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, camera, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, socket_signal: 1
- skeletal_animation, audio: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment, vfx, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, socket_signal: 1
- vfx, socket_signal: 1

Raw SHA-256: `aed22248e9888f64bd47d082aa023d4bef4633626a6d15ad6108154a1f371433`. Binary SHA-256: `3854a8c1697fdae5aefb255c691c584032df0716eae42bb2eb781ae60f405ccb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q201\scenes\q201_06_cabin_day_8_to_29.scene" --events
```

## `base\quest\main_quests\epilogue\q201\scenes\q201_07_cabin_day_30.scene`

410 graph nodes, 576 edges; 98 event-bearing sections, 1027 events; 156 screenplay lines, 29 screenplay options, 16 choice nodes.

Actors: Security_guard (actor 0, community); Doctor_scientist (actor 1, community); Hellman (actor 2, spawnSet); Kerry (actor 3, findInContext); River (actor 4, findInContext); Panam (actor 5, findInContext); Judy (actor 6, findInContext); Victor (actor 7, findInContext); Doctor_assistant (actor 8, community); assistant_male (actor 9, community); player_end_female (actor 10, spawnDespawn); player_end_male (actor 11, spawnDespawn); V (actor 12, findInContext).

Entries: `Start 18` → 3540; `Start 19` → 3584; `day_30_start` → 149.

Exits: `day_30_end` → 158.

End nodes: 158: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 64 | 972 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/7` |
| `scnChangeIdleAnimEvent` | 81 | 957 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scnDialogLineEvent` | 105 | 637 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 2925 / 1426 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/28` |
| `scnIKEvent` | 8 | 2925 / 1413 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/18` |
| `scnLookAtEvent` | 139 | 637 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlayRidAnimEvent` | 42 | 2436 / 719 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/6` |
| `scnPlaySkAnimEvent` | 398 | 637 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scnUnmountEvent` | 4 | 2925 / 1425 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/27` |
| `scneventsAttachPropToPerformer` | 11 | 972 / 118 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/2` |
| `scneventsAttachPropToWorld` | 5 | 2399 / 673 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/7` |
| `scneventsCameraParamsEvent` | 13 | 2275 / 629 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/7` |
| `scneventsPlayRidCameraAnimEvent` | 42 | 2436 / 733 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 4 | 2925 / 1423 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/26` |
| `scneventsSocket` | 103 | 957 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/3` |
| `scneventsVFXEvent` | 4 | 957 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- skeletal_animation, gaze: 11
- camera: 9
- skeletal_animation, idle_animation: 8
- speech: 6
- speech, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 3
- gaze: 3
- skeletal_animation, idle_animation, socket_signal: 3
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 2
- skeletal_animation, rid_actor, camera, rid_camera, audio, vfx, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 2
- skeletal_animation, audio, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, rid_actor, camera, rid_camera, audio, socket_signal: 2
- speech, skeletal_animation, gaze: 1
- speech, idle_animation, gaze, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, idle_animation, gaze, audio, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, props_equipment, audio: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, audio: 1
- idle_animation: 1
- socket_signal: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1

Raw SHA-256: `d2fd4e14b3ecfcee4c528d39bfa67162c99cb677f99386267614173e3c2500e3`. Binary SHA-256: `33bbd8b3fdaf99bd4ccb92ba6380a2ddd481b3b6b037588a93b3cb39b4d0e87c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q201\scenes\q201_07_cabin_day_30.scene" --events
```

## `base\quest\main_quests\epilogue\q201\scenes\q201_08_cabin_day_30_takemura.scene`

418 graph nodes, 605 edges; 99 event-bearing sections, 1038 events; 159 screenplay lines, 28 screenplay options, 16 choice nodes.

Actors: Security_guard (actor 0, community); Doctor_scientist (actor 1, community); Takemura (actor 2, spawnSet); Doctor_assistant (actor 3, community); Assistant_male (actor 4, community); player_end_female (actor 5, spawnDespawn); player_end_male (actor 6, spawnDespawn); V (actor 7, findInContext).

Entries: `day_30_start` → 4; `Start 4` → 5037; `Start 3` → 4896.

Exits: `day_30_end` → 137.

End nodes: 137: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 66 | 13 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/7` |
| `scnChangeIdleAnimEvent` | 82 | 7 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 105 | 7 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 239 / 1135 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/8` |
| `scnIKEvent` | 6 | 239 / 1127 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/1` |
| `scnLookAtEvent` | 130 | 7 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlayRidAnimEvent` | 42 | 4987 / 2806 | `/Data/RootChunk/sceneGraph/Data/graph/378/Data/events/1` |
| `scnPlaySkAnimEvent` | 422 | 12 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scnUnmountEvent` | 3 | 239 / 1134 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/7` |
| `scneventsAttachPropToPerformer` | 11 | 13 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |
| `scneventsAttachPropToWorld` | 6 | 29 / 396 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/7` |
| `scneventsCameraParamsEvent` | 12 | 49 / 642 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/10` |
| `scneventsPlayRidCameraAnimEvent` | 42 | 4987 / 2840 | `/Data/RootChunk/sceneGraph/Data/graph/378/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 3 | 239 / 1130 | `/Data/RootChunk/sceneGraph/Data/graph/90/Data/events/4` |
| `scneventsSocket` | 101 | 7 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsVFXEvent` | 4 | 7 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, gaze: 15
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- camera: 9
- skeletal_animation, idle_animation: 8
- speech: 5
- speech, gaze: 5
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 4
- skeletal_animation, idle_animation, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze: 3
- skeletal_animation, audio, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 3
- gaze: 3
- speech, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, rid_actor, camera, rid_camera, audio, vfx, socket_signal: 2
- skeletal_animation, rid_actor, camera, rid_camera, audio, socket_signal: 2
- speech, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 1
- idle_animation, props_equipment, vfx, socket_signal: 1
- gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, audio: 1
- skeletal_animation, socket_signal: 1
- idle_animation: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1

Raw SHA-256: `f1dd18bb9628bdfa78d15625f18845d134ea619e46a40189dccad6ab1508fc58`. Binary SHA-256: `5d75485510d52645b29f26614e542fad4bddf810566e83fd909b160fdec292bd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q201\scenes\q201_08_cabin_day_30_takemura.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\final_boards\q307_ending_01_rogue.scene`

47 graph nodes, 51 edges; 9 event-bearing sections, 66 events; 15 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: rogue (actor 0, spawnDespawn); iguana (actor 1, spawnDespawn); nibbles (actor 2, spawnDespawn); iguanatogether (actor 3, spawnDespawn).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 6 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/17` |
| `scnDialogLineEvent` | 9 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 11 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 29 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsCameraEvent` | 1 | 114 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scneventsCameraParamsEvent` | 2 | 86 / 125 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scneventsSocket` | 4 | 96 / 141 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- camera: 1
- camera, socket_signal: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `e45a5be1362092bf77a0f423d16b243e5b43d9b71b1a0e70dd29f2fa2a9c7ed5`. Binary SHA-256: `66f26958ea73ecdf16bf13b7571943f65c395dbaf316f9697a22af1d01fef08f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\final_boards\q307_ending_01_rogue.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\final_boards\q307_ending_02_takemura.scene`

23 graph nodes, 22 edges; 3 event-bearing sections, 44 events; 8 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: takemura (actor 0, spawnDespawn).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 35 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 6 | 35 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnLookAtEvent` | 13 | 35 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnPlaySkAnimEvent` | 15 | 35 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraEvent` | 1 | 108 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |
| `scneventsCameraParamsEvent` | 2 | 78 / 141 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scneventsSocket` | 2 | 35 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- camera: 1
- camera, socket_signal: 1

Raw SHA-256: `60924d00d7c2217b2cbf42693fe6b3eec11bb9086caa31096ce34ba95f528bea`. Binary SHA-256: `ebee315e64b70ae14e9c7b70765b2852eb045b8217b68cb8e0b145ac4b765cdb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\final_boards\q307_ending_02_takemura.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\final_boards\q307_ending_03_mitch.scene`

21 graph nodes, 20 edges; 3 event-bearing sections, 48 events; 8 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: mitch (actor 0, spawnDespawn); rogue (actor 1, spawnDespawn); mitch_vehicle (actor 2, spawner).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 35 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 6 | 35 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 7 | 35 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 29 | 35 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsCameraEvent` | 1 | 109 / 203 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/2` |
| `scneventsCameraParamsEvent` | 2 | 69 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 109 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/0` |
| `scneventsSocket` | 1 | 109 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 1
- camera: 1
- camera, socket_signal, animation_state: 1

Raw SHA-256: `4b2010a2a89c7b44e06a2788a4c2d4fd2922d082f900d7b1feb72d4f158916d7`. Binary SHA-256: `8c057658441330eaa19aa3321173b6afe79fd7e3116d102394a9b16de811754c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\final_boards\q307_ending_03_mitch.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\final_boards\q307_ending_04_reed.scene`

117 graph nodes, 113 edges; 10 event-bearing sections, 119 events; 32 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: reed (actor 0, spawnDespawn); reed_car (actor 1, spawner).

Entries: `reed_fb_q307_q305_in` → 1; `reed_fb_q307_q306_in` → 87; `reed_fb_q306_in` → 88; `reed_fb_305_somi_fia_in` → 89; `reed_fb_305_somi_dead_in` → 93.

Exits: `reed_fb_q307_q305_out` → 2; `reed_fb_q307_q306_out` → 95; `reed_fb_305_somi_fia_out` → 96; `reed_fb_305_somi_dead_out` → 97; `reed_fb_q306_out` → 98.

End nodes: 2: `<omitted>`; 95: `<omitted>`; 96: `<omitted>`; 97: `<omitted>`; 98: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 35 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 22 | 35 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 31 | 35 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 39 | 35 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsCameraEvent` | 5 | 434 / 705 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/1` |
| `scneventsCameraParamsEvent` | 5 | 434 / 707 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/2` |
| `scneventsSocket` | 7 | 35 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/19` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 3
- camera, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- gaze, camera, socket_signal: 2

Raw SHA-256: `71ddd6663e53677c129e5151a8ee2c231ec6cd266773f867be06e0a4aa1763d8`. Binary SHA-256: `b8982d22d72aae3fc2c1cda4798c60c6373a83e5b3a1c74c842fc90f1e03f38e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\final_boards\q307_ending_04_reed.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\final_boards\q307_ending_05_viktor.scene`

21 graph nodes, 20 edges; 3 event-bearing sections, 34 events; 8 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: viktor (actor 0, spawnDespawn).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 35 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 6 | 35 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 7 | 35 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 15 | 35 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsCameraEvent` | 1 | 98 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/1` |
| `scneventsCameraParamsEvent` | 2 | 69 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scneventsSocket` | 1 | 98 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 1
- camera: 1
- camera, socket_signal: 1

Raw SHA-256: `2b50d5bcb67147f7ec1ab831d2bf59bcd86a0ebcea0d5dbea17c14b6108aac31`. Binary SHA-256: `a827e60e23810ffb38b518dc13f5f4c71f7bc11625c395dbc73f0ba717af94d5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\final_boards\q307_ending_05_viktor.scene" --events
```

