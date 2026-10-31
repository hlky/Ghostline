# Gig: Hothead: scene presentation

Journal identity: `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_09`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wbr_jpn_09.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene`

60 graph nodes, 63 edges; 21 event-bearing sections, 122 events; 47 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: netrunner (actor 0, findInWorld); netrunner_truck (actor 1, community); v (actor 2, findInContext).

Entries: `before` → 1; `damage` → 149; `enemy_seen` → 53; `almost_done` → 54; `done` → 55.

Exits: `before_end` → 2; `final_end` → 78.

End nodes: 2: `<omitted>`; 78: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 81 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnDialogLineEvent` | 44 | 59 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 100 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/11` |
| `scnIKEvent` | 2 | 100 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/3` |
| `scnLookAtEvent` | 15 | 81 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnPlaySkAnimEvent` | 37 | 81 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnUnmountEvent` | 1 | 100 / 199 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 1 | 100 / 195 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/7` |
| `scneventsSocket` | 15 | 74 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `41be0f48721d7252038abf05e2cf814cad5524d6f9efc2a90023abc27b8f03e3`. Binary SHA-256: `7c8502076dfd09413caccb74446d5f51ccc05567019610d4b486087bca60e956`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\westbrook\japantown\sts_wbr_jpn_09\scenes\sts_wbr_jpn_09_netrunner.scene" --events
```

