# Spellbound: scene presentation

Journal identity: `quests/minor_quest/mq015_wizardbook`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq015_wizardbook.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene`

61 graph nodes, 71 edges; 12 event-bearing sections, 94 events; 24 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: Nix (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `in` → 1; `Start 1` → 275.

Exits: `out` → 2; `out_clean` → 130.

End nodes: 2: `NonTerminating`; 130: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 14 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scnChangeIdleAnimEvent` | 19 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 23 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 14 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 17 | 14 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/6` |
| `scneventsSocket` | 15 | 14 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scneventsVFXEvent` | 2 | 18 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `d87d8225a82cc7d4e0c328edb9987993b34a6850c0b7bf5a967a335758a1b28d`. Binary SHA-256: `64a234c610860780848f32f6686cfc5b48ffe3fefc71d5f28568dc97842bb1eb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq015\scenes\mq015_01_hook.scene" --events
```

## `base\quest\minor_quests\mq015\scenes\mq015_02_seller_holocall.scene`

17 graph nodes, 16 edges; 3 event-bearing sections, 7 events; 6 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: Seller (actor 0, findInContext); Player (actor 1, findInContext).

Entries: `Start1` → 706; `Start 0` → 107.

Exits: `End 0` → 114.

End nodes: 114: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 8 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSocket` | 1 | 8 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, socket_signal: 1

Raw SHA-256: `722b679fa96c5c0d995b541bb8d6b14f8f6de70a0f22d694e3e73d04933fe03b`. Binary SHA-256: `3f19852c45592e667689e7e556f49d6d44d957fe5edb514c03b0a3fc05fad249`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq015\scenes\mq015_02_seller_holocall.scene" --events
```

## `base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene`

110 graph nodes, 142 edges; 21 event-bearing sections, 153 events; 41 screenplay lines, 12 screenplay options, 4 choice nodes.

Actors: Seller (actor 0, community); Player (actor 1, findInContext).

Entries: `in` → 1; `in_stealing_reaction` → 118; `in_hit_reaction` → 120; `in_grapple_reaction` → 898.

Exits: `out` → 2; `out_combat` → 20; `out_failed` → 308.

End nodes: 2: `<omitted>`; 20: `NonTerminating`; 308: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 28 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnDialogLineEvent` | 34 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 2 | 101 / 274 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/6` |
| `scnIKEvent` | 4 | 101 / 271 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/3` |
| `scnLookAtEvent` | 16 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 28 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnUnmountEvent` | 2 | 101 / 279 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 2 | 101 / 275 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/7` |
| `scneventsSocket` | 33 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 4 | 11 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- skeletal_animation: 4
- speech, idle_animation, gaze: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, socket_signal: 1
- gaze: 1
- idle_animation, gaze: 1

Raw SHA-256: `66a1a3adf04e0f8d04d224953f147520eb219808406df6824457b0710465721d`. Binary SHA-256: `bc4a9ff6ed87c54d8013cc9cc13c334c7a5294843455a8b5d264818d2ac74712`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq015\scenes\mq015_03_restaurant.scene" --events
```

## `base\quest\minor_quests\mq015\scenes\mq015_04_stash.scene`

40 graph nodes, 46 edges; 9 event-bearing sections, 22 events; 11 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `in` → 1.

Exits: `out` → 2; `out_clean_up` → 222.

End nodes: 2: `NonTerminating`; 222: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 9 | 14 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 7 | 14 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 4 | 89 / 73 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/1` |
| `scnPlaySkAnimEvent` | 1 | 269 / 187 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/0` |
| `scneventsSocket` | 1 | 269 / 195 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation: 4
- speech, idle_animation, gaze: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech: 1
- gaze: 1

Raw SHA-256: `0b4fa4c8c4aded88e3f4eff7cacfb285005102e83f683f3096e9a198cf832628`. Binary SHA-256: `995a7f03061d79fad7eb6fbd87a6588feedb36ee2ad2ed96e085cedfc78cfcd3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq015\scenes\mq015_04_stash.scene" --events
```

## `base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene`

78 graph nodes, 94 edges; 15 event-bearing sections, 137 events; 41 screenplay lines, 12 screenplay options, 5 choice nodes.

Actors: nix (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `in` → 1.

Exits: `out` → 2; `out_done` → 191.

End nodes: 2: `NonTerminating`; 191: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 45 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/7` |
| `scnChangeIdleAnimEvent` | 17 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 38 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 12 | 33 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scnPlaySkAnimEvent` | 26 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsEquipItemToPerformer` | 1 | 335 / 434 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/0` |
| `scneventsSocket` | 25 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 12 | 23 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, idle_animation, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, vfx: 1
- speech, idle_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- idle_animation, props_equipment, socket_signal: 1

Raw SHA-256: `9a62a54b1bff36fb3f5fc7648b7f7406dbc7575eda58671d206205bae7279eae`. Binary SHA-256: `2e9ce56c5500f80fbb31da423658769bad648af8ca642df7ef4ad26293208314`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq015\scenes\mq015_05_afterlife.scene" --events
```

