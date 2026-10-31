# Big in Japan: scene presentation

Journal identity: `quests/minor_quest/mq038_neweridentity`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq038_neweridentity.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq038\scenes\mq038_01b_fisher_village.scene`

42 graph nodes, 38 edges; 9 event-bearing sections, 29 events; 18 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Tyger_claw_01 (actor 0, community); Tyger_claw_02 (actor 1, community); Tyger_claw_03 (actor 2, community); Tyger_claw_04 (actor 3, community); Denis (actor 4, spawnSet); Surgeon (actor 5, community); Player (actor 6, findInContext).

Entries: `body_seen` → 1; `mq038_surgeon_facial` → 129; `combat_01` → 18; `combat_02` → 20; `combat_03` → 22; `combat_04` → 24; `call` → 122.

Exits: `body_seen_out` → 2; `End1` → 263; `combat_01_out` → 19; `combat_02_out` → 21; `combat_03_out` → 23; `combat_04_out` → 25; `body_seen_out_cut` → 282; `call_out_cut` → 289; `call_out` → 123.

End nodes: 2: `<omitted>`; 19: `<omitted>`; 21: `<omitted>`; 23: `<omitted>`; 25: `<omitted>`; 123: `<omitted>`; 263: `<omitted>`; 282: `<omitted>`; 289: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 13 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 17 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 5 | 48 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/2` |
| `scneventsSocket` | 2 | 48 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, idle_animation: 1

Raw SHA-256: `e79377de48ae43c0c8820a6ad1252fbff1c4c23792aa62713c14ebfcf34e95dc`. Binary SHA-256: `380d9b176549975fefcc4d746848cb48cd1faf43706f25e073f3622d31b553ab`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq038\scenes\mq038_01b_fisher_village.scene" --events
```

## `base\quest\minor_quests\mq038\scenes\mq038_02_ending.scene`

46 graph nodes, 47 edges; 9 event-bearing sections, 97 events; 20 screenplay lines, 6 screenplay options, 3 choice nodes.

Actors: Surgeon (actor 0, community); Darryl (actor 1, community); Player (actor 2, findInContext).

Entries: `Start 0` → 1; `talk_loop` → 26.

Exits: `End 0` → 2; `talk_loop_out` → 27.

End nodes: 2: `NonTerminating`; 27: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 8 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnDialogLineEvent` | 17 | 8 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnLookAtEvent` | 34 | 8 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 16 | 8 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSocket` | 18 | 8 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/14` |
| `scneventsVFXDurationEvent` | 1 | 11 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- gaze: 1
- socket_signal: 1

Raw SHA-256: `3564da994fa7e1921cf147891e183d6b364f50d97809b55791a745d0e14c062c`. Binary SHA-256: `856f9d639df1beabae9e313a212353fa29053ebe0a170dc97762290eed65f8c4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq038\scenes\mq038_02_ending.scene" --events
```

