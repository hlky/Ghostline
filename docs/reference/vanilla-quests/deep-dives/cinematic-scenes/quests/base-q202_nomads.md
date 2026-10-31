# All Along the Watchtower: scene presentation

Journal identity: `quests/main_quest/epilogues/q202_nomads`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q202_nomads.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene`

214 graph nodes, 265 edges; 54 event-bearing sections, 573 events; 126 screenplay lines, 22 screenplay options, 11 choice nodes.

Actors: panam (actor 0, spawnSet); Radio (actor 1, findInContext); Panam_vehicle (actor 2, spawnSet); v (actor 3, findInContext).

Entries: `cinedebug_bleeding` → 3488; `intro_radio` → 2765; `Start 1` → 2419; `CineDebug_LedgeTalk` → 2647; `Start 9` → 3749; `cinematic_debug_scenestart` → 2900; `Start 8` → 3648.

Exits: `intro_radio_out` → 2767; `End1` → 655.

End nodes: 655: `NonTerminating`; 2767: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 16 | 2263 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/16` |
| `scnChangeIdleAnimEvent` | 109 | 2263 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnDialogLineEvent` | 92 | 1702 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 2913 / 1224 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 2263 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/25` |
| `scnIKEvent` | 8 | 2263 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/13` |
| `scnLookAtEvent` | 91 | 2263 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 172 | 2263 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnUnmountEvent` | 3 | 2263 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/24` |
| `scneventsAttachPropToNode` | 1 | 2907 / 1222 | `/Data/RootChunk/sceneGraph/Data/graph/80/Data/events/0` |
| `scneventsCameraParamsEvent` | 8 | 2475 / 827 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 8 | 2263 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/21` |
| `scneventsSocket` | 58 | 2263 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/22` |
| `scneventsVFXEvent` | 2 | 3277 / 1431 | `/Data/RootChunk/sceneGraph/Data/graph/112/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 14
- gaze: 6
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 5
- skeletal_animation: 5
- socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze: 2
- skeletal_animation, idle_animation, camera, audio, socket_signal, animation_state: 2
- camera: 2
- vfx: 2
- speech: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- props_equipment: 1
- idle_animation, gameplay_action: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, audio, socket_signal, animation_state: 1
- idle_animation, gaze: 1

Raw SHA-256: `aef8ec3b81ad84273abe33b8a67c58e146df47c7d649efe78161b63f3c488fdf`. Binary SHA-256: `e5210eeb7945fe39034685e56a3753d524ebb8169565a4ff87393b5ff2c0b361`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene" --events
```

## `base\quest\main_quests\epilogue\q202\scenes\q202_04a_badlands_travel.scene`

116 graph nodes, 135 edges; 21 event-bearing sections, 348 events; 63 screenplay lines, 5 screenplay options, 2 choice nodes.

Actors: Panam (actor 0, spawnSet); Mitch (actor 1, spawnSet); Radio (actor 2, findInContext); Panam_Vehicle (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `Start 0` → 2; `CineDebug_drive` → 589; `travel_radio` → 689; `Start 4` → 1012; `Cinedebug_mitchtime` → 623.

Exits: `End 0` → 1; `travel_radio_out` → 690; `CineRadio_out` → 781.

End nodes: 1: `NonTerminating`; 690: `<omitted>`; 781: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 68 | 7 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnDialogLineEvent` | 51 | 7 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnIKEvent` | 36 | 7 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/23` |
| `scnLookAtEvent` | 56 | 7 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 70 | 7 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 27 | 7 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/25` |
| `scneventsSocket` | 40 | 7 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/26` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 9
- skeletal_animation: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 2
- ik, socket_signal, animation_state: 1
- socket_signal, animation_state: 1
- speech: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `0c04fe6a7a1b65a6c0c1114bdbc67fc8bc3df2742faa5273e96eb6229c249bf8`. Binary SHA-256: `b561c177ce0a8cdf18afec1d954383acd5a882bcc96532783f7acc5c527777af`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q202\scenes\q202_04a_badlands_travel.scene" --events
```

## `base\quest\main_quests\epilogue\q202\scenes\q202_05_convoy.scene`

1095 graph nodes, 1450 edges; 231 event-bearing sections, 1706 events; 380 screenplay lines, 54 screenplay options, 28 choice nodes.

Actors: Judy (actor 0, spawnSet); River (actor 1, spawnSet); Panam (actor 2, spawnSet); Bob (actor 3, spawnSet); Teddy (actor 4, spawnSet); Cassidy (actor 5, spawnSet); Carol (actor 6, spawnSet); judy_call (actor 7, findInContext); Kerry (actor 8, spawnSet); Mitch (actor 9, spawnSet); River_vehicle (actor 10, spawnSet); Kerry_vehicle (actor 11, spawnSet); Panam_vehicle (actor 12, spawnSet); Teddy_jammer_vehicle (actor 13, community); Cassidy_vehicle (actor 14, community); Panzer (actor 15, spawnSet); v (actor 16, findInContext).

Entries: `q202_convoy_panam_in` → 1; `q202_camp_drive` → 7697; `debug_camp_center` → 1971; `Start 20` → 7731; `cinedebug_judy` → 3282; `Cinedebug_Start` → 2364; `Cinedebug_Mitch` → 2386; `Start 22` → 8155; `Cinedebug_carol` → 2608; `cinedebug_kerry` → 3608; `kerry` → 2815; `river_ward` → 2817; `judy_carol` → 2818; `cassidy` → 2819.

Exits: `q202_camp_drive_out` → 7701; `q202_convoy_panam_out` → 314; `side_dialogues` → 2820.

End nodes: 314: `NonTerminating`; 2820: `NonTerminating`; 7701: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 1069 / 983 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/8` |
| `scnChangeIdleAnimEvent` | 353 | 414 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnDialogLineEvent` | 217 | 304 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayActionEvent` | 8 | 1030 / 674 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/0` |
| `scnGameplayTransitionEvent` | 10 | 1699 / 2446 | `/Data/RootChunk/sceneGraph/Data/graph/129/Data/events/25` |
| `scnIKEvent` | 26 | 1093 / 1017 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/9` |
| `scnLookAtEvent` | 298 | 414 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 476 | 414 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnUnmountEvent` | 10 | 1699 / 2445 | `/Data/RootChunk/sceneGraph/Data/graph/129/Data/events/24` |
| `scneventsAttachPropToWorld` | 1 | 1699 / 2435 | `/Data/RootChunk/sceneGraph/Data/graph/129/Data/events/15` |
| `scneventsCameraParamsEvent` | 14 | 1279 / 1444 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/3` |
| `scneventsEquipItemToPerformer` | 4 | 3134 / 3270 | `/Data/RootChunk/sceneGraph/Data/graph/239/Data/events/8` |
| `scneventsSetAnimFeatureEvent` | 33 | 1030 / 687 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/9` |
| `scneventsSocket` | 243 | 414 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsUnequipItemFromPerformer` | 2 | 1699 / 2436 | `/Data/RootChunk/sceneGraph/Data/graph/129/Data/events/16` |
| `scneventsUnequipItemFromPerformerByItem` | 2 | 3134 / 3272 | `/Data/RootChunk/sceneGraph/Data/graph/239/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 53
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 44
- gaze: 44
- skeletal_animation, socket_signal: 11
- skeletal_animation, gaze, socket_signal: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 6
- camera: 6
- speech: 5
- speech, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze: 5
- skeletal_animation, idle_animation: 4
- skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, gaze: 3
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 2
- idle_animation, gaze: 2
- skeletal_animation, socket_signal, animation_state: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, camera, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, idle_animation, camera, socket_signal, animation_state, gameplay_action: 1
- idle_animation, socket_signal, animation_state, gameplay_action: 1
- socket_signal: 1
- skeletal_animation, idle_animation, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, ik, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state, gameplay_action: 1

Raw SHA-256: `fdb9112848bd08b13c22717eddddd8303279fb893c4d69ab30278c92b8779b95`. Binary SHA-256: `b21a064d4583363bbb080195166a2257ff8107a55837020dfe5489fd77b9a9da`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q202\scenes\q202_05_convoy.scene" --events
```

## `base\quest\main_quests\epilogue\q202\scenes\q202_06_border_running.scene`

307 graph nodes, 373 edges; 36 event-bearing sections, 264 events; 94 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: panam (actor 0, spawnSet); judy (actor 1, findInContext); Mitch (actor 2, spawnSet); Carol (actor 3, spawnSet); Cassidy (actor 4, spawnSet); V_TPP_male (actor 5, spawnDespawn); V_TPP_Female (actor 6, spawnDespawn); Panam_outro (actor 7, spawnDespawn); Panzer (actor 8, spawnSet); V (actor 9, findInContext).

Entries: `q202_to_tunnel_entrance` → 1508; `q202_to_starting_point` → 398; `cinedebug_chickentest_start` → 2518; `cinedebug_EndingCine` → 1388.

Exits: `q202_border_running_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 1094 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/10` |
| `scnChangeIdleAnimEvent` | 15 | 516 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/0` |
| `scnDialogLineEvent` | 76 | 184 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 5 | 516 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 2795 / 1931 | `/Data/RootChunk/sceneGraph/Data/graph/280/Data/events/0` |
| `scnPlayRidAnimEvent` | 36 | 1094 / 275 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/2` |
| `scnPlaySkAnimEvent` | 86 | 1081 / 241 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/3` |
| `scneventsPlayRidCameraAnimEvent` | 12 | 1094 / 297 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 7 | 1081 / 259 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/13` |
| `scneventsSocket` | 8 | 516 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/9` |
| `scneventsVFXDurationEvent` | 1 | 1094 / 299 | `/Data/RootChunk/sceneGraph/Data/graph/40/Data/events/11` |
| `scneventsVFXEvent` | 5 | 1081 / 240 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 19
- skeletal_animation: 4
- skeletal_animation, idle_animation: 2
- idle_animation: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, rid_actor, camera, rid_camera, audio, vfx: 1
- skeletal_animation, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, vfx: 1
- idle_animation, socket_signal, animation_state: 1
- animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal, animation_state: 1
- idle_animation, gaze: 1

Raw SHA-256: `946ae200601b04ea91ccc6c24a345cc5cd380cad5786fa00d9c7b759dc031f3f`. Binary SHA-256: `e6a6f2da5cbc9951dc986bddee238446a563a0f967670ef879f34983d80f0d3c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\epilogue\q202\scenes\q202_06_border_running.scene" --events
```

