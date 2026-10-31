# Gig: Catch a Tyger's Toe: scene presentation

Journal identity: `quests/street_stories/watson/little_china/sts_wat_lch_01`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_lch_01.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_enemies.scene`

25 graph nodes, 25 edges; 6 event-bearing sections, 24 events; 24 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: lch_01_tyger_claw_04 (actor 0, community); lch_01_tyger_claw_03 (actor 1, community); lch_01_tyger_claw_02 (actor 2, community); lch_01_tyger_claw_05 (actor 3, community); V (actor 4, findInContext).

Entries: `lch_01_sound_the_alarm_start` → 76; `lch_01_halon_start` → 81; `lch_01_halon_intro_start` → 86; `lch_01_graffiti_looking_001_start` → 62; `lch_01_sleeping_001_start` → 72; `lch_01_leaving_dialogue_start` → 98.

Exits: `lch_01_sound_the_alarm_end` → 79; `lch_01_halon_end` → 82; `lch_01_graffiti_looking_001_end` → 63; `lch_01_halon_intro_end` → 89; `lch_01_sleeping_001_end` → 73; `lch_01_leaving_dialogue_end` → 99.

End nodes: 63: `NonTerminating`; 73: `NonTerminating`; 79: `NonTerminating`; 82: `NonTerminating`; 89: `NonTerminating`; 99: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 24 | 47 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6

Raw SHA-256: `503c18612041d57e8c6a6461b4d455f214c23a755a0e3c89e225eb02ebc0089c`. Binary SHA-256: `f2aa7c8b2c659a5c9a842001f3c16a7a15f8a2ef88d8cef69ea9b23862fb17f5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_enemies.scene" --events
```

## `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene`

23 graph nodes, 30 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 285.

End nodes: 2: `<omitted>`; 285: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `3e89dd749c5909bcf42d7018e89e048a5b1553464903257669e2af056256c923`. Binary SHA-256: `4d4984a279ef9cebbb73904ec381cd79e1e2c0d6e4469034b5a3085faf763267`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_debrief.scene" --events
```

## `base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 28 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `b1decfcd025c985464a54b6ea357a451c88d96e85b074e634f6672402b485842`. Binary SHA-256: `a9310503097e83fe78df15a9a41a414a4c7b13041c561cf4943ca947ce592ada`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\little_china\sts_wat_lch_01\scenes\sts_wat_lch_01_holocall_prebrief.scene" --events
```

