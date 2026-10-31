# Gig: Jeopardy: scene presentation

Journal identity: `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_hey_rey_06.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_civilians.scene`

15 graph nodes, 15 edges; 3 event-bearing sections, 6 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: prayer_001 (actor 0, findInWorld); priest (actor 1, findInWorld); prayer_002 (actor 2, findInWorld); V (actor 3, findInContext).

Entries: `rey_06_hologram_start` → 243; `rey_06_priest_chat_start` → 186; `rey_06_civilian_002_chat_start` → 193.

Exits: `rey_06_priest_chat_end` → 244; `rey_06_hologram_end` → 205; `rey_06_civilian_002_chat_end` → 194.

End nodes: 194: `NonTerminating`; 205: `NonTerminating`; 244: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 149 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3

Raw SHA-256: `c91526861c6f060869a09da9365f7694d6baf491e35cd0678f079bac5801f073`. Binary SHA-256: `3f1bed0c42cf1912280f6b6de4181bb84eb79e56c458a182616f97d44adaa393`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_civilians.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `Start1` → 96.

Exits: `rejected_out` → 281; `End1` → 97.

End nodes: 97: `<omitted>`; 281: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `cd33b33cd1b3bb07a2fc5135f18c9f02bc0c30ab565e10e022209426188748ed`. Binary SHA-256: `8b5869234f99290763648b9357031ea2a5868fd3309cfc4946aba966278011ab`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `Start1` → 94.

Exits: `End1` → 95; `rejected_out` → 254.

End nodes: 95: `<omitted>`; 254: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 26 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `af3b3ae5d929bbca2a35813f63a19cf5fd3f2ad79529e2657eae5ce83c3c6cb7`. Binary SHA-256: `3892f20285fa456b9717e3f21e30b5b256c978c6583df1faf50925d8d89643b2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_receptionist.scene`

14 graph nodes, 15 edges; 3 event-bearing sections, 36 events; 9 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: receptionist (actor 0, community); V (actor 1, findInContext).

Entries: `rey_06_receptionist_talk_start` → 172.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 79 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnDialogLineEvent` | 9 | 79 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnLookAtEvent` | 6 | 79 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnPlaySkAnimEvent` | 6 | 79 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/8` |
| `scneventsSocket` | 8 | 79 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3

Raw SHA-256: `bc46540a7b8c1c71726ab2c5218507aebe9126866aa8fb6449cac7f8f7dfe5d9`. Binary SHA-256: `b3cd4e737aa9b839fefa2ea2293741c493b101843f6801f441dca78f92a279ac`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\heywood\vista_del_rey\sts_hey_rey_06\scenes\sts_hey_rey_06_receptionist.scene" --events
```

