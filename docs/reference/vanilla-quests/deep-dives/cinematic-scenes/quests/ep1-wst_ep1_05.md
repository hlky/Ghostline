# Go Your Own Way: scene presentation

Journal identity: `ep1/quests/minor_quest/wst_ep1_05`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-wst_ep1_05.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene`

92 graph nodes, 112 edges; 23 event-bearing sections, 297 events; 54 screenplay lines, 15 screenplay options, 6 choice nodes.

Actors: hasan (actor 0, community); hasan_squat (actor 1, community); v (actor 2, findInContext).

Entries: `Hasan_default_1st_meeting_start` → 1; `hasan_squat_talk_start` → 345; `Hasan_squat_start` → 11; `Hasan_default_apartment_start` → 30.

Exits: `End1` → 347; `Hasan_squat_end` → 13; `Hasan_default_1st_meeting_end` → 42.

End nodes: 13: `NonTerminating`; 42: `<omitted>`; 347: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 15 | 18 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnDialogLineEvent` | 54 | 18 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnLookAtEvent` | 78 | 18 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnPlaySkAnimEvent` | 107 | 18 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsEquipItemToPerformer` | 4 | 35 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/8` |
| `scneventsSocket` | 39 | 18 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, skeletal_animation, gaze, socket_signal: 5
- speech: 4
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1
- gaze: 1

Raw SHA-256: `0b14cdfaa00d321d0ee2cf6d4d50cf06dbd54b11749fed0642516b7aed06b52c`. Binary SHA-256: `c012281c26de9518db65c037dd2c676b10f10c2105a7e38f41beccfc3493d3a2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\tertiary_characters\default_dialogs\hasan_default\sts_04_hasan_default.scene" --events
```

