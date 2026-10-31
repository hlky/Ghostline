# Machine Gun: scene presentation

Journal identity: `quests/minor_quest/mq007_smartgun`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq007_smartgun.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene`

73 graph nodes, 82 edges; 15 event-bearing sections, 59 events; 43 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: Skippy (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `mq007_01_in` → 1.

Exits: `mq007_01_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 40 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 3 | 161 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/0` |
| `scneventsSocket` | 16 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, socket_signal: 9
- speech: 3
- skeletal_animation: 2
- skeletal_animation, socket_signal: 1

Raw SHA-256: `715000fdc429624ae23544b84b8a388399c228d152d66a3f0544279f5c0890e0`. Binary SHA-256: `92410f8114062bc9f5e4918ca9655a655346b5931ce93faaef535dc28c6b37bc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene" --events
```

## `base\quest\minor_quests\mq007\scenes\mq007_02_skippy_reactions.scene`

111 graph nodes, 102 edges; 19 event-bearing sections, 19 events; 19 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Skippy (actor 0, findInContext).

Entries: `SkippyTaunts01` → 1; `old` → 120; `SkippyOnGore01` → 16; `Autofire` → 29; `FireDelay` → 38; `OnReload` → 47; `SkippyTaunts02` → 66; `SkippyTaunts03` → 67; `SkippyTaunts04` → 68; `SkippyTaunts05` → 69; `SkippyOnGore02` → 76; `SkippyOnGore03` → 77; `SkippyOnGore04` → 78; `SkippyOnGore05` → 79.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 19 | 6 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 19

Raw SHA-256: `c254e894a9934a7fdcc18330554d9de17e1de415efbb1f1a8bfc393adfc3e3fc`. Binary SHA-256: `63f3e759a55cb15c3fab95fa2fc5fd04aebbbf9c52b5de88018cb358db6509bb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq007\scenes\mq007_02_skippy_reactions.scene" --events
```

## `base\quest\minor_quests\mq007\scenes\mq007_03_skippy_about_killing.scene`

87 graph nodes, 100 edges; 16 event-bearing sections, 38 events; 27 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: Skippy (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `mq007_03_in` → 1.

Exits: `mq007_03_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 24 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 3 | 178 / 173 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/0` |
| `scneventsSocket` | 11 | 10 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, socket_signal: 7
- speech: 6
- skeletal_animation, socket_signal: 2
- skeletal_animation: 1

Raw SHA-256: `a736d09c508baf88eba354d0b380281b26a76f1b4f0b187d7bcb70dfc6270f79`. Binary SHA-256: `278c78e0249fe69958b416f87d23af4c2a5d082b31d6c4c6488a28a5f27a9a4c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq007\scenes\mq007_03_skippy_about_killing.scene" --events
```

## `base\quest\minor_quests\mq007\scenes\mq007_04_skippy_return.scene`

135 graph nodes, 158 edges; 25 event-bearing sections, 133 events; 51 screenplay lines, 9 screenplay options, 5 choice nodes.

Actors: Skippy (actor 0, spawnDespawn); Reggie (actor 1, spawnSet); Daisy (actor 2, spawnDespawn); SkippyVoice (actor 3, findInContext); Player (actor 4, findInContext).

Entries: `mq007_skippy_about_return_in` → 1; `mq007_mr_hands_in` → 29; `SkippyNoReturnOneliner` → 205.

Exits: `mq007_skippy_about_return_out` → 2; `TurnOffItemFailsafe` → 151; `mq007_mr_hands_out` → 56; `DisableScene` → 334.

End nodes: 2: `<omitted>`; 56: `NonTerminating`; 151: `NonTerminating`; 334: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 34 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scnChangeIdleAnimEvent` | 8 | 32 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnDialogLineEvent` | 41 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 16 | 32 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scnPlaySkAnimEvent` | 30 | 32 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/4` |
| `scnPoseCorrectionEvent` | 6 | 32 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/13` |
| `scneventsAttachPropToPerformer` | 1 | 34 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scneventsAttachPropToWorld` | 1 | 34 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |
| `scneventsSocket` | 27 | 10 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsVFXEvent` | 2 | 52 / 184 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze: 3
- skeletal_animation, socket_signal: 2
- gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 1
- gaze: 1
- skeletal_animation: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- animation_state: 1

Raw SHA-256: `a4ae147cad736bd3f121a4b6dce80c0fd6c31fd62156bef789b9475390da934f`. Binary SHA-256: `d50e87ea26c0cf56b806d94f627535ab78039b0214d064d8d174462e370263dd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq007\scenes\mq007_04_skippy_return.scene" --events
```

