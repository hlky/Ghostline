# Gig: Family Heirloom: scene presentation

Journal identity: `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_06`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wbr_hil_06.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\scenes\sts_characters\dan_default.scene`

16 graph nodes, 18 edges; 7 event-bearing sections, 42 events; 16 screenplay lines, 4 screenplay options, 1 choice nodes.

Actors: dan (actor 0, community); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 8 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 14 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 8 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 15 | 5 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 2 | 92 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 3
- speech, skeletal_animation, gaze: 2
- socket_signal: 2

Raw SHA-256: `fa3e6910cd47e6f34b721e774f6765c5ca0ffe5c3d6278693cb627ddba56321b`. Binary SHA-256: `3563dd2ad3668ad1e912d4c774222de5213c95d600a1e55e66c672909d2626ff`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\scenes\sts_characters\dan_default.scene" --events
```

## `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\scenes\sts_wbr_hil_06_holocall_debriefs.scene`

27 graph nodes, 35 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: rogue (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 286.

End nodes: 2: `<omitted>`; 286: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `fc5bfb68b9e2af8f3424f9675d7c4f4601ac975f04357acc11c945936f952b1b`. Binary SHA-256: `cec02fc0c1c06a163f2dc75d9b9817ea4e01b5f4a6459cf04f3cb08e063ff5dd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\scenes\sts_wbr_hil_06_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\scenes\sts_wbr_hil_06_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: rogue (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 24 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `dba4e6654dfe1f5e4c90bb5dd30b06a0765519627aab5edfa527fbd3474f2d4d`. Binary SHA-256: `901012a6ab5065fe6e22dc0a14294d38fe762934e14c250f39c6055f3764e036`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\scenes\sts_wbr_hil_06_holocall_prebrief.scene" --events
```

## `base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\scenes\sts_wbr_hil_06_johnny.scene`

6 graph nodes, 5 edges; 1 event-bearing sections, 6 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 2 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 1

Raw SHA-256: `63f300a9f77e66c5eeb926add413b0c7968165ec1ce3424057a823ad62a557b9`. Binary SHA-256: `2dd19f2ec948168df0071613692a851decf022564b275fdefaa9322dc17bd392`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\charter_hill\sts_wbr_hil_06\scenes\sts_wbr_hil_06_johnny.scene" --events
```

