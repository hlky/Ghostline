# Fool on the Hill: scene presentation

Journal identity: `quests/minor_quest/mq033_tarot`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq033_tarot.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq033\scenes\mq033_1_first_grafitti.scene`

440 graph nodes, 587 edges; 10 event-bearing sections, 70 events; 33 screenplay lines, 27 screenplay options, 25 choice nodes.

Actors: Misty (actor 0, spawnSet); Victor (actor 1, spawnSet); Johnny (actor 2, spawnSet); Victor_holocall (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `mq033_1_misty_about_grafitti_in` → 1; `mq033_1_v_comments_grafitti_in` → 10; `mq033_1_victor_about_grafitti_in` → 16; `mq033_1_johnny_grafitti_in` → 43; `mq033_1_ch_clues_in` → 49; `ep1` → 1952; `from_mq033_ep1_tarot` → 1974; `q115_q201_tarots_in` → 1116.

Exits: `mq033_1_misty_about_grafitti_out` → 2; `mq033_1_v_comments_grafitti_out` → 14; `mq033_1_victor_about_grafitti_out` → 17; `mq033_1_johnny_grafitti_out` → 44; `mq033_1_misty_to_all_tarots` → 517; `mq033_ep1_tarot` → 1966; `End 8` → 1986; `q115_q201_tarots_out` → 1119.

End nodes: 2: `<omitted>`; 14: `<omitted>`; 17: `<omitted>`; 44: `<omitted>`; 517: `NonTerminating`; 1119: `<omitted>`; 1966: `NonTerminating`; 1986: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 32 | 7 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 12 | 7 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnPlaySkAnimEvent` | 17 | 7 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scneventsSocket` | 7 | 7 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/4` |
| `scneventsVFXEvent` | 2 | 7 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, gaze: 1
- socket_signal: 1

Raw SHA-256: `e988ffd9e736a3795c139579f17646b46d66d729c1df6c0994aae62e208b9153`. Binary SHA-256: `de01cfd112251f6251aab6d3ecbd2fcfbc1e89946762da4f30e6c65d21eb1f2e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq033\scenes\mq033_1_first_grafitti.scene" --events
```

## `base\quest\minor_quests\mq033\scenes\mq033_2_all_grafitti.scene`

39 graph nodes, 44 edges; 10 event-bearing sections, 60 events; 34 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: misty (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1; `from_ep1_tarot` → 148.

Exits: `End 0` → 2; `mq033_to_ep1_tarot` → 146.

End nodes: 2: `<omitted>`; 146: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 32 | 5 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 1 | 5 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnPlaySkAnimEvent` | 14 | 17 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/5` |
| `scneventsAttachPropToNode` | 1 | 83 / 231 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/3` |
| `scneventsAttachPropToPerformer` | 1 | 22 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/10` |
| `scneventsSocket` | 9 | 5 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsVFXEvent` | 2 | 17 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation: 3
- speech: 2
- speech, skeletal_animation, props_equipment, socket_signal: 2
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `ccd58217108110f27d09e64fafc2428c79dc58eac9cd785ceec242a68709cf28`. Binary SHA-256: `871099a72491b9da3fcaaf297bc895900d068b3317b9a849180a5ed71a6109ba`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq033\scenes\mq033_2_all_grafitti.scene" --events
```

## `base\quest\minor_quests\mq033\scenes\mq033_ep1_grafitti.scene`

161 graph nodes, 202 edges; 20 event-bearing sections, 260 events; 69 screenplay lines, 16 screenplay options, 7 choice nodes.

Actors: misty (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `in king of the cups` → 1; `in king of the pentacles` → 25; `in king of the swords` → 27; `in king of the wands` → 29; `in misty` → 40; `misty_ep_1_prev` → 564.

Exits: `out king of the cups` → 4; `out king of the pentacles` → 31; `out king of the swords` → 33; `out king of the wands` → 35; `to_mq033_first_scene` → 875; `End1` → 425; `fortune told` → 427.

End nodes: 4: `<omitted>`; 31: `<omitted>`; 33: `<omitted>`; 35: `<omitted>`; 425: `<omitted>`; 427: `<omitted>`; 875: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 44 | 431 / 413 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/4` |
| `scnDialogLineEvent` | 66 | 431 / 407 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 698 / 919 | `/Data/RootChunk/sceneGraph/Data/graph/127/Data/events/4` |
| `scnIKEvent` | 2 | 698 / 916 | `/Data/RootChunk/sceneGraph/Data/graph/127/Data/events/1` |
| `scnLookAtEvent` | 44 | 431 / 408 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/1` |
| `scnPlaySkAnimEvent` | 69 | 431 / 410 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/3` |
| `scnUnmountEvent` | 1 | 698 / 924 | `/Data/RootChunk/sceneGraph/Data/graph/127/Data/events/8` |
| `scneventsCameraParamsEvent` | 1 | 698 / 918 | `/Data/RootChunk/sceneGraph/Data/graph/127/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 1 | 698 / 920 | `/Data/RootChunk/sceneGraph/Data/graph/127/Data/events/5` |
| `scneventsSocket` | 31 | 431 / 409 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- speech, skeletal_animation, idle_animation, gaze: 6
- speech, gaze, socket_signal: 1
- socket_signal: 1
- gaze: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `c01fa1ecc85785eb4439f095ff33e5d6e296bd242a47bea41957a2d9ab4d24f5`. Binary SHA-256: `b9582091c8543e32dd997962f49fc8984bf1bbea8cfc1f3fc6fb8d9eb8294dc7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq033\scenes\mq033_ep1_grafitti.scene" --events
```

