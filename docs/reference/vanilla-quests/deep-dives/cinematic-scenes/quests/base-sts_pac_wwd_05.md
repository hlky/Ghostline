# Gig: For My Son: scene presentation

Journal identity: `quests/street_stories/pacifica/west_wind_estates/sts_pac_wwd_05`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_pac_wwd_05.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_bouncer.scene`

23 graph nodes, 33 edges; 9 event-bearing sections, 61 events; 18 screenplay lines, 4 screenplay options, 1 choice nodes.

Actors: bouncer (actor 0, community); Player (actor 1, findInContext).

Entries: `bouncer` → 1.

Exits: `End 1` → 100.

End nodes: 100: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 43 / 152 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scnDialogLineEvent` | 18 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scnLookAtEvent` | 13 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 28 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsSocket` | 1 | 4 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 5
- speech, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1

Raw SHA-256: `430f7b5ff6f0ec05979977b6aaec33a258819c7b6bdec6efce1798c2589afc1b`. Binary SHA-256: `0c1d5c672c4b5bc27ff4dab5293439aedcd04bfaa0a54b278461a1ab3f7a00db`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_bouncer.scene" --events
```

## `base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_fluff.scene`

7 graph nodes, 6 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: ganger (actor 0, findInWorld); Player (actor 1, findInContext).

Entries: `ganger_005_talk` → 1.

Exits: `ganger_005_talk_end` → 2; `End 1` → 19.

End nodes: 2: `<omitted>`; 19: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `73b832644ca4dfa65e6d271f133c98a34d7cff9f9a90f78a613c18790a27003f`. Binary SHA-256: `d02d3b231625bb3e049d19fe38d675b7dd917dad4fd176d8ce571b255cd8178a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_fluff.scene" --events
```

## `base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_gangers.scene`

5 graph nodes, 4 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: enemy_005 (actor 0, findInWorld); dirtgirl (actor 1, findInWorld); enemy_004 (actor 2, findInWorld); target (actor 3, findInWorld).

Entries: `fight_chat` → 1.

Exits: `fight_chat_end` → 2; `Interrupted` → 8.

End nodes: 2: `<omitted>`; 8: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `9c3d059b673ab8a71d82596d3e5beb9eee4d58bcf983505148176fcd4e640f55`. Binary SHA-256: `79a97ef10943453da102d3c284c8c63ed44bf7bcb7ede5fbf5c691857edba370`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_gangers.scene" --events
```

## `base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_gate_keeper.scene`

22 graph nodes, 29 edges; 6 event-bearing sections, 21 events; 11 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: gatekeeper (actor 0, community); Player (actor 1, findInContext).

Entries: `wwd_05_gatekeeper` → 4.

Exits: `wwd_05_gatekeeper_end` → 5; `End 1` → 131.

End nodes: 5: `<omitted>`; 131: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 9 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnDialogLineEvent` | 9 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 1 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 3 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 3 | 9 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scneventsVFXEvent` | 4 | 8 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, vfx: 1
- speech, idle_animation, socket_signal: 1
- speech: 1
- speech, skeletal_animation: 1
- vfx, socket_signal: 1

Raw SHA-256: `65b67b3c3ea17bff02c438bfcd8d5f3abe6312ba2e9f4a8e2fa534775a777971`. Binary SHA-256: `6e54d8d61414a32776329a0482cd50aa03d75decbd2d2c57717ba7a2597a5085`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_gate_keeper.scene" --events
```

## `base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_debriefs.scene`

46 graph nodes, 60 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `killed_start` → 4; `spared_start` → 35.

Exits: `debrief_killed` → 2; `rejected_spared_out` → 333; `debrief_pacifist` → 34; `rejected_killed_out` → 320.

End nodes: 2: `<omitted>`; 34: `<omitted>`; 320: `<omitted>`; 333: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 17 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `9dedd78617e24a969013d94c757774eee21c8b7c45de906ecc4f6083ad40b38a`. Binary SHA-256: `75bb035f0e864b43f7ea96aabba5598a3f47e7693ee8950594c47615e773354f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `f3f205abac446852ebfbece2232b4071a7404faa1370f93452397763280190a5`. Binary SHA-256: `90533c9d0cf2f10e0506ffcfe7dd80de0b04764b2e34c63f8d9bcf7c761c2755`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\pacifica\west_wind_estates\sts_pac_wwd_05\scenes\sts_pac_wwd_05_holocall_prebrief.scene" --events
```

