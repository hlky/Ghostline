# Gig: Going-away Party: scene presentation

Journal identity: `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_03`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_std_rcr_03.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_gangers.scene`

64 graph nodes, 73 edges; 13 event-bearing sections, 63 events; 25 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: ganger_01 (actor 0, community); ganger_02 (actor 1, community); ganger_03 (actor 2, community); ganger_04 (actor 3, community); js (actor 4, spawnDespawn); turret_guard_01 (actor 5, community); turret_guard_02 (actor 6, community); car_01 (actor 7, community); car_02 (actor 8, community); Player (actor 9, findInContext).

Entries: `js_on_cars_02` → 84; `js_on_reprimend_02` → 88; `ganger_phone_chat` → 32; `js_on_reprimend_01` → 36; `turret_scene` → 53; `turret_reaction` → 58; `js_on_cars_01` → 61.

Exits: `js_on_cars_out` → 64; `ganger_phone_chat_out` → 34; `js_on_reprimend_out` → 40; `turret_scene_out` → 56.

End nodes: 34: `<omitted>`; 40: `<omitted>`; 56: `<omitted>`; 64: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 122 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/1` |
| `scnDialogLineEvent` | 17 | 13 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnLookAtEvent` | 18 | 122 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/2` |
| `scnPlaySkAnimEvent` | 8 | 122 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/0` |
| `scneventsSocket` | 11 | 122 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- skeletal_animation, idle_animation, gaze, socket_signal: 4
- gaze: 4

Raw SHA-256: `078d60e104977f67991048bce47c5e36922a91b4eb1e2ef3f742943f923dd625`. Binary SHA-256: `320451dcf655bb5ae3b4a5f84fbc306fb2fd8341dc1474f497ee5ef09adc46ed`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_gangers.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_holocall_debriefs.scene`

25 graph nodes, 33 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: el_capitan (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 287.

End nodes: 2: `<omitted>`; 287: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `ca4d4f9f5f309273a891d29ac3d2107b9c8fae106bcde1b4d74fa9947b215c24`. Binary SHA-256: `ea01f68b14b7fd103b0506fde6f1f908b19d8bbba57cb77436f01f29f891d822`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: el_capitan (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `1ed4ae698c7f5fa6710da4a459154de62df4852f1a7d22b5256d5f426a6d2a13`. Binary SHA-256: `749fc0fbcc7b48bfb9d66815f4d4eadf68417ee7cee68590ca384d8383715714`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_investigation.scene`

151 graph nodes, 177 edges; 25 event-bearing sections, 146 events; 35 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: js (actor 0, spawnDespawn); dead_prostitutes_01 (actor 1, community); flavio (actor 2, community); Player (actor 3, findInContext).

Entries: `js_at_execution` → 1; `js_on_flavio` → 8; `v_at_execution` → 13; `js_on_6th_street_01` → 14; `body_downstairs_01` → 21; `js_on_systems_offline_02` → 26; `js_on_dismantled_turret` → 31; `body_downstairs_02` → 95; `body_downstairs_03` → 96; `js_on_6th_street_02` → 103; `js_on_systems_offline_01` → 107.

Exits: `js_on_flavio_out` → 11; `js_on_6th_street_out` → 19; `body_downstairs_out` → 24; `js_on_systems_offline_out` → 29; `js_on_dismantled_turret_out` → 34; `v_at_execution_out` → 77.

End nodes: 11: `<omitted>`; 19: `<omitted>`; 24: `<omitted>`; 29: `<omitted>`; 34: `<omitted>`; 77: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 19 | 5 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnDialogLineEvent` | 13 | 5 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnLookAtEvent` | 55 | 5 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 30 | 5 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 29 | 5 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 11
- skeletal_animation, idle_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech: 3

Raw SHA-256: `b1a0e9d20cf1bba31ca3fad398fccc06a6b874f83cb0890a1ff60e9287fa07ef`. Binary SHA-256: `00652d0ab5d25bbc31b6f9683aecf7e27d6656f6f15185cc2c584365a6a65794`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_investigation.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_meeting_hayashi.scene`

22 graph nodes, 21 edges; 7 event-bearing sections, 35 events; 18 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: flavio (actor 0, community); v (actor 1, findInContext).

Entries: `rcr_03_meeting_flavio` → 1; `rcr_03_flavio_in_car` → 169.

Exits: `flavio_standing` → 272; `rcr_03_meeting_hayashi_out` → 121; `rcr_03_flavio_in_car_out` → 172.

End nodes: 121: `NonTerminating`; 172: `<omitted>`; 272: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 181 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnDialogLineEvent` | 16 | 170 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnLookAtEvent` | 4 | 181 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/7` |
| `scnPlaySkAnimEvent` | 6 | 181 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scneventsSocket` | 4 | 181 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, idle_animation: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `4ab81a5fd675514a7cbd5621038e2712b7b4e86903d9e3c620f7f679a6866ede`. Binary SHA-256: `7cfb0ce63c986e37433aae4b783d300d90c6ca543c1878d1a4d83a89942d0d0f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_meeting_hayashi.scene" --events
```

## `base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_meeting_nomad.scene`

36 graph nodes, 43 edges; 7 event-bearing sections, 35 events; 14 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: hayashi (actor 0, community); nomad (actor 1, community); v (actor 2, findInContext).

Entries: `Start 0` → 1; `Start 4` → 269; `walk away` → 200; `preview` → 184; `Start 2` → 189.

Exits: `End 0` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 26 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnDialogLineEvent` | 8 | 21 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 26 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/19` |
| `scnIKEvent` | 2 | 26 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/14` |
| `scnLookAtEvent` | 8 | 26 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnPlaySkAnimEvent` | 5 | 26 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scnUnmountEvent` | 1 | 26 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 1 | 26 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/17` |
| `scneventsSocket` | 6 | 26 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `0a131d124193fb2c7452786c6b3576382b114ae39be242374565bd8fde9e5bd1`. Binary SHA-256: `35e6df056a123365d03883c309c9cc96d886892c67e89b94817df5bd4d18c9a6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\santo_domingo\rancho_corronado\sts_std_rcr_03\scenes\sts_std_rcr_03_meeting_nomad.scene" --events
```

