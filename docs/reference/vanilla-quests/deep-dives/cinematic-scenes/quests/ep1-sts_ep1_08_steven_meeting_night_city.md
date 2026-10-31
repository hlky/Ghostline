# The Show Must Go On: scene presentation

Journal identity: `ep1/quests/minor_quest/sts_ep1_08_steven_meeting_night_city`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-sts_ep1_08_steven_meeting_night_city.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\sts_08_steven_default_new_biomonitor_not_destroyed.scene`

38 graph nodes, 39 edges; 6 event-bearing sections, 75 events; 18 screenplay lines, 5 screenplay options, 3 choice nodes.

Actors: steven_1 (actor 0, community); player (actor 1, findInContext).

Entries: `Start 1` → 120; `Start 2` → 154; `Start 3` → 227.

Exits: `End 2` → 145; `End 3` → 155.

End nodes: 145: `NonTerminating`; 155: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 124 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/10` |
| `scnDialogLineEvent` | 17 | 118 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnLookAtAdvancedEvent` | 4 | 130 / 98 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/8` |
| `scnLookAtEvent` | 12 | 118 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 17 | 118 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scneventsAttachPropToPerformer` | 2 | 128 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |
| `scneventsAttachPropToWorld` | 1 | 124 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scneventsSocket` | 16 | 124 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsVFXEvent` | 2 | 124 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/18` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `162f23cd12f15c878a959aa7c77a0f41db9af0b58500da4ecfae6aae9edd66ab`. Binary SHA-256: `1ed6c14866308cfe5d54d0f77d59b825528dc321f9619b17bc6ae5710fc2cf02`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\tertiary_characters\default_dialogs\steven_santos_default\sts_08_steven_default_new_biomonitor_not_destroyed.scene" --events
```

