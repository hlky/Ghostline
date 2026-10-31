# I Don't Wanna Hear It: scene presentation

Journal identity: `quests/side_quest/sq017_01_riot_club`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq017_01_riot_club.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\side_quests\sq017\scenes\sq017_07_phone_call_2.scene`

24 graph nodes, 25 edges; 4 event-bearing sections, 36 events; 14 screenplay lines, 3 screenplay options, 1 choice nodes.

Actors: kerry (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 442.

End nodes: 2: `<omitted>`; 442: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 3 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 14 | 3 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 10 | 3 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsSocket` | 4 | 3 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, socket_signal: 4

Raw SHA-256: `5ce0e8a2725e54fc1530e71714d9e3089a3ad411d5908a0748b5e0e3ca7f27ac`. Binary SHA-256: `323c0b6f94feb24a73fd6f0ab51172cb822fecb97e16d94c7edb3daf01c95f96`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_07_phone_call_2.scene" --events
```

## `base\quest\side_quests\sq017\scenes\sq017_08_club_outside.scene`

348 graph nodes, 424 edges; 61 event-bearing sections, 561 events; 129 screenplay lines, 21 screenplay options, 10 choice nodes.

Actors: guard_main_entrance_2 (actor 0, spawnSet); vip1 (actor 1, community); vip2 (actor 2, community); ticket_seller (actor 3, community); cart_clerk (actor 4, community); guard_main_entrance_1 (actor 5, community); kerry (actor 6, spawnSet); guard_main_entrance_6 (actor 7, community); guard_main_entrance_7 (actor 8, community); buyer1 (actor 9, community); buyer2 (actor 10, community); v (actor 11, findInContext).

Entries: `Start_main_entrance` → 1; `Start_meet_kerry` → 15; `Start_concertgoer` → 22; `Start_drop_ladder` → 69; `Start_jump_down` → 72; `Start_further_into_club` → 77; `Start_no_ladder` → 82; `Start_ticket_seller` → 123; `Start 18` → 2212; `Ticket_scan` → 2257; `start_timelapse` → 1567; `look_for_badge_in` → 423; `Start 16` → 2079.

Exits: `End_main_entrance_yes` → 2; `End_main_entrance_no` → 7; `End_meet_kerry` → 16; `End_drop_ladder` → 67; `End_jump_down` → 74; `End_further_into_club` → 78; `End_no_ladder` → 83; `End_concertgoer` → 116; `End_ticket_seller` → 124; `kerry_stood_up` → 2454; `look_for_badge_out` → 424.

End nodes: 2: `NonTerminating`; 7: `<omitted>`; 16: `NonTerminating`; 67: `<omitted>`; 74: `<omitted>`; 78: `<omitted>`; 83: `<omitted>`; 116: `<omitted>`; 124: `<omitted>`; 424: `<omitted>`; 2454: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 21 | 100 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/8` |
| `scnDialogLineEvent` | 112 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 8 | 759 / 762 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/45` |
| `scnIKEvent` | 16 | 759 / 745 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/38` |
| `scnLookAtEvent` | 113 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 120 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 8 | 759 / 763 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/46` |
| `scneventsCameraParamsEvent` | 3 | 1736 / 1858 | `/Data/RootChunk/sceneGraph/Data/graph/218/Data/events/1` |
| `scneventsEquipItemToPerformer` | 1 | 100 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 8 | 759 / 760 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/44` |
| `scneventsSocket` | 146 | 3 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scneventsVFXEvent` | 5 | 133 / 251 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 15
- speech: 9
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 6
- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, idle_animation, gaze, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, gaze: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze: 2
- camera: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- skeletal_animation, camera, socket_signal: 1
- vfx, socket_signal: 1

Raw SHA-256: `a8c31e4aab4d81606f919ec1bda78d6377a5b92549e3d0bbcad49d7744a648d9`. Binary SHA-256: `ca22ab5d94d5b0a40a727b02cc37938e979ab9c9a96d2358274159daadaf1fc2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_08_club_outside.scene" --events
```

## `base\quest\side_quests\sq017\scenes\sq017_09_club_inside.scene`

439 graph nodes, 578 edges; 79 event-bearing sections, 539 events; 136 screenplay lines, 26 screenplay options, 11 choice nodes.

Actors: kerry (actor 0, spawnSet); guard_backstage (actor 1, community); bartender (actor 2, spawnSet); roadie (actor 3, community); makeup_girl1 (actor 4, community); makeup_girl2 (actor 5, community); lightning_guy (actor 6, community); roadie_girl (actor 7, community); v (actor 8, findInContext).

Entries: `Start_backstage_door` → 1; `Start_return_backstage_door` → 986; `Start_hack_or_force` → 2267; `Start_roadie` → 40; `kerry_to_rail_pissed` → 2921; `Start 20` → 2997; `Start_what_now` → 771; `Start_makeup_girls` → 158; `Start_lightning_guy` → 159; `Start 21` → 3040; `got_inside_in` → 800; `Kerry_to_rail` → 1466; `Start 10` → 889; `Start1` → 2813; `Kerry_to_rail_ladder` → 1590.

Exits: `End_backstage_no` → 2; `End_roadie` → 41; `End_backstage_roadie` → 102; `End_what_now` → 772; `End_makeup_girls` → 160; `got_inside_out` → 801; `End_lightning_guy` → 161; `backstage_loop_out` → 1786.

End nodes: 2: `NonTerminating`; 41: `NonTerminating`; 102: `NonTerminating`; 160: `NonTerminating`; 161: `NonTerminating`; 772: `NonTerminating`; 801: `<omitted>`; 1786: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 42 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnDialogLineEvent` | 97 | 42 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scnGameplayTransitionEvent` | 5 | 163 / 386 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/15` |
| `scnIKEvent` | 10 | 163 / 379 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/9` |
| `scnLookAtEvent` | 97 | 42 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 127 | 42 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnPoseCorrectionEvent` | 3 | 115 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/7` |
| `scnUnmountEvent` | 5 | 163 / 385 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/14` |
| `scneventsAttachPropToNode` | 1 | 100 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/8` |
| `scneventsAttachPropToPerformer` | 8 | 100 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scneventsAttachPropToWorld` | 7 | 115 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/23` |
| `scneventsCameraParamsEvent` | 3 | 1131 / 1310 | `/Data/RootChunk/sceneGraph/Data/graph/127/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 5 | 163 / 383 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/13` |
| `scneventsSocket` | 159 | 42 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scneventsVFXEvent` | 2 | 1644 / 1780 | `/Data/RootChunk/sceneGraph/Data/graph/207/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 17
- skeletal_animation, socket_signal: 13
- gaze: 9
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, socket_signal: 4
- skeletal_animation, props_equipment, socket_signal: 4
- skeletal_animation, gaze: 4
- speech, gaze, socket_signal: 3
- speech, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, socket_signal: 2
- camera: 2
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech: 1
- socket_signal: 1
- skeletal_animation, camera, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `d4d7259b44a7ac24442d926596a70d76f158493f4897c726bff346ec5215be5f`. Binary SHA-256: `1aee6891d9bd1304700133b552e3d8beb827a5bc3d67ccf49702e2936743f858`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_09_club_inside.scene" --events
```

## `base\quest\side_quests\sq017\scenes\sq017_10_us_crack_intro.scene`

312 graph nodes, 357 edges; 49 event-bearing sections, 673 events; 100 screenplay lines, 13 screenplay options, 8 choice nodes.

Actors: kerry (actor 0, spawnSet); blue_moon (actor 1, community); purple_force (actor 2, community); red_menace (actor 3, community); johnny (actor 4, spawnDespawn); v (actor 5, findInContext).

Entries: `Start 0` → 1; `Start 6` → 2742; `Start 1` → 590.

Exits: `End 0` → 2; `cut_distance_pause` → 2798; `end_no_deal` → 380.

End nodes: 2: `<omitted>`; 380: `<omitted>`; 2798: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 41 | 32 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 81 | 32 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scnGameplayTransitionEvent` | 3 | 362 / 909 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/38` |
| `scnIKEvent` | 6 | 362 / 900 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/33` |
| `scnLookAtEvent` | 244 | 32 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 147 | 32 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 1 | 32 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/27` |
| `scnUnmountEvent` | 3 | 362 / 910 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/39` |
| `scneventsAttachPropToPerformer` | 4 | 41 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/45` |
| `scneventsSetAnimFeatureEvent` | 3 | 362 / 911 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/40` |
| `scneventsSocket` | 132 | 32 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/14` |
| `scneventsVFXEvent` | 8 | 362 / 869 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 10
- gaze: 8
- skeletal_animation, socket_signal: 4
- speech, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, socket_signal: 3
- skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze: 2
- speech: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, vfx: 1
- vfx: 1

Raw SHA-256: `0b7ce248b4d12865f7ed3afa98568b0de22f4664bdafa81103fa69860c2c57bf`. Binary SHA-256: `b4b55ee1eac2f0511a431373c01eb80412a622cf22c3c1c435c706687a5c76ce`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq017\scenes\sq017_10_us_crack_intro.scene" --events
```

