# Shoot To Thrill: scene presentation

Journal identity: `quests/minor_quest/mq011_wilson`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq011_wilson.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene`

378 graph nodes, 445 edges; 54 event-bearing sections, 254 events; 81 screenplay lines, 14 screenplay options, 6 choice nodes.

Actors: wilson (actor 0, spawnSet); wilson_phone (actor 1, spawnSet); contestant_1 (actor 2, community); contestant_2 (actor 3, community); contestant_3 (actor 4, community); contestant_4 (actor 5, community); contestant_5 (actor 6, community); Player (actor 7, findInContext).

Entries: `mq011_start_in` → 1; `mq011_call_in` → 6; `chicken_in` → 1182; `Start 4` → 235.

Exits: `mq011_shooting_start_out` → 2; `mq011_call_out` → 7; `chicken_out` → 1183; `call_rejected` → 1679; `weapon_mgr` → 324; `mq011_01_competition_out` → 338.

End nodes: 2: `NonTerminating`; 7: `<omitted>`; 324: `NonTerminating`; 338: `<omitted>`; 1183: `<omitted>`; 1679: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 340 / 660 | `/Data/RootChunk/sceneGraph/Data/graph/74/Data/events/4` |
| `scnChangeIdleAnimEvent` | 4 | 326 / 542 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/6` |
| `scnDialogLineEvent` | 56 | 4 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnGameplayTransitionEvent` | 2 | 98 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/15` |
| `scnIKEvent` | 4 | 98 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/10` |
| `scnLookAtAdvancedEvent` | 20 | 869 / 1625 | `/Data/RootChunk/sceneGraph/Data/graph/212/Data/events/0` |
| `scnLookAtEvent` | 42 | 4 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnPlaySkAnimEvent` | 70 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 3 | 85 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/4` |
| `scnUnmountEvent` | 2 | 98 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/14` |
| `scneventsAttachPropToNode` | 2 | 342 / 683 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/6` |
| `scneventsAttachPropToPerformer` | 1 | 342 / 680 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 2 | 98 / 169 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/13` |
| `scneventsSocket` | 41 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 4 | 342 / 675 | `/Data/RootChunk/sceneGraph/Data/graph/76/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 12
- socket_signal: 6
- gaze: 6
- speech, skeletal_animation: 5
- skeletal_animation: 4
- speech, skeletal_animation, gaze: 3
- speech, gaze: 2
- skeletal_animation, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- vfx: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `d61b7e12faa809da93fa332496d3da77258e3e8ba81641912c14ad30cd3531a1`. Binary SHA-256: `d40f1e9f65c970a91cbf38c2a3ace5a9f48e8354decd24ee881b3446c3bbbd89`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene" --events
```

