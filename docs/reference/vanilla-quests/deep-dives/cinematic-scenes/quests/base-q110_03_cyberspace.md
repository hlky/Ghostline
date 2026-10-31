# Transmission: scene presentation

Journal identity: `quests/main_quest/act_01/q110_03_cyberspace`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q110_03_cyberspace.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q110\scenes\q110_01_sermon.scene`

102 graph nodes, 123 edges; 16 event-bearing sections, 128 events; 45 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: sermon_leader (actor 0, spawnSet); Johnny (actor 1, spawnSet); voodoo_contact (actor 2, spawnSet); faithfull_interactive_01 (actor 3, findInWorld); faithfull_interactive_02 (actor 4, findInWorld); faithfull_interactive_03 (actor 5, findInWorld); faithfull_interactive_04 (actor 6, findInWorld); faithfull_synced_01 (actor 7, findInWorld); Player (actor 8, findInContext).

Entries: `ChapeGateAnimationIn` → 820; `q110_01_sermon_in` → 18; `WaitingForSermonIn` → 933.

Exits: `q110_01_cut_all_signal` → 453; `q110_01_sermon_out` → 19; `WaitingForSermonOut` → 964.

End nodes: 19: `NonTerminating`; 453: `<omitted>`; 964: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 27 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnChangeIdleAnimEvent` | 3 | 158 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/0` |
| `scnDialogLineEvent` | 39 | 25 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 265 / 269 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/7` |
| `scnIKEvent` | 4 | 265 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/3` |
| `scnLookAtEvent` | 13 | 25 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/28` |
| `scnPlaySkAnimEvent` | 36 | 25 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 1 | 25 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 2 | 265 / 276 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/13` |
| `scneventsCameraParamsEvent` | 2 | 27 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 2 | 265 / 272 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/10` |
| `scneventsSocket` | 21 | 25 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation: 1
- gaze: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `f02b4063ff0191f833165c7b22934639e818e7c5ffdd8cb9f1ae9f90d2b2bc06`. Binary SHA-256: `7dc322fca6ab9ae1fe33ff85dbc8c9b1a485fcb275f7195389fae8b23dce62a4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_01_sermon.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_08a_agent.scene`

545 graph nodes, 655 edges; 75 event-bearing sections, 593 events; 178 screenplay lines, 46 screenplay options, 18 choice nodes.

Actors: johnny (actor 0, spawnDespawn); agent (actor 1, spawnSet); boss (actor 2, spawnSet); placide (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `q110_07_agent_in` → 1; `Holocall` → 1340; `q110_after_agent_test_in` → 510; `Start 14` → 2697; `FailsafeIn` → 4105; `q110_after_agent_deal_test_in` → 632; `take_chip` → 2438; `q110_08a_placide_calls_back_in` → 2078.

Exits: `q110_07_agent_out` → 2; `q110_08a_placide_calls_back_out` → 2083.

End nodes: 2: `<omitted>`; 2083: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 21 | 361 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scnChangeIdleAnimEvent` | 19 | 441 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/2` |
| `scnDialogLineEvent` | 158 | 361 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/3` |
| `scnGameplayTransitionEvent` | 2 | 2555 / 1971 | `/Data/RootChunk/sceneGraph/Data/graph/242/Data/events/4` |
| `scnIKEvent` | 4 | 2555 / 1968 | `/Data/RootChunk/sceneGraph/Data/graph/242/Data/events/1` |
| `scnLookAtAdvancedEvent` | 6 | 677 / 471 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/14` |
| `scnLookAtEvent` | 50 | 361 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scnPlaySkAnimEvent` | 110 | 361 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnUnmountEvent` | 2 | 2555 / 1975 | `/Data/RootChunk/sceneGraph/Data/graph/242/Data/events/7` |
| `scneventsAttachPropToNode` | 2 | 1227 / 996 | `/Data/RootChunk/sceneGraph/Data/graph/101/Data/events/8` |
| `scneventsAttachPropToPerformer` | 3 | 677 / 468 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/11` |
| `scneventsAttachPropToWorld` | 2 | 2592 / 2014 | `/Data/RootChunk/sceneGraph/Data/graph/250/Data/events/2` |
| `scneventsCameraParamsEvent` | 8 | 361 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 2 | 2555 / 1973 | `/Data/RootChunk/sceneGraph/Data/graph/242/Data/events/6` |
| `scneventsSocket` | 187 | 361 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scneventsVFXEvent` | 17 | 486 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/23/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 15
- speech: 13
- speech, skeletal_animation, gaze, socket_signal: 13
- speech, socket_signal: 4
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- gaze: 2
- speech, skeletal_animation, gaze, camera, audio, socket_signal: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- gaze, vfx, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal: 1
- speech, props_equipment, socket_signal: 1

Raw SHA-256: `1e0fcdb89d6583ae02f7f6a5dc7e98dca3f88be252c68bce6c7ddd7c039add54`. Binary SHA-256: `42ad02dacfb0b208a5d41f13d9a59b4c6c532a69dd67eb56c3d473483d92e903`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_08a_agent.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_08d_animals_stand_down.scene`

41 graph nodes, 47 edges; 19 event-bearing sections, 59 events; 48 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: animals_01_chat_01 (actor 0, spawnSet); animals_02_chat_01 (actor 1, spawnSet); animals_03_chat_02 (actor 2, spawnSet); animals_04_chat_02 (actor 3, spawnSet); animals_05_chat_03 (actor 4, spawnSet); animals_06_chat_03 (actor 5, spawnSet); animals_boss_chat_03 (actor 6, spawnSet); Player (actor 7, findInContext).

Entries: `Chat01In` → 189; `Chat02In` → 191; `Chat03In` → 193.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 206 / 174 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/2` |
| `scnDialogLineEvent` | 45 | 9 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnLookAtEvent` | 7 | 206 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- idle_animation, gaze: 3

Raw SHA-256: `4281433fbd38b7e567d0d14673e5a0bb8e25cc4d545b3fcfba624f05767742aa`. Binary SHA-256: `0dcfd5ee5a7d7daef470a384947c029e92d7bbfe3379e3576f4ecb0c3ffff0d3`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_08d_animals_stand_down.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_09a_lookout_intercept.scene`

151 graph nodes, 187 edges; 26 event-bearing sections, 117 events; 44 screenplay lines, 5 screenplay options, 3 choice nodes.

Actors: voodoo_boy_lookout (actor 0, spawnSet); vodoo_boy_lookout_02 (actor 1, spawnSet); galena (actor 2, spawnSet); Player (actor 3, findInContext).

Entries: `q110_09a_lookout_intercept_in` → 1; `LookoutCallsPlacideIn` → 1769.

Exits: `q110_09a_shortcut_out` → 2; `q110_09a_no_shortcut_out` → 26; `DriveAway` → 1738; `LookoutCallsPlacideOut` → 1773.

End nodes: 2: `<omitted>`; 26: `NonTerminating`; 1738: `<omitted>`; 1773: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 7 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 25 | 7 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 1802 / 769 | `/Data/RootChunk/sceneGraph/Data/graph/137/Data/events/6` |
| `scnIKEvent` | 2 | 1802 / 763 | `/Data/RootChunk/sceneGraph/Data/graph/137/Data/events/1` |
| `scnLookAtEvent` | 35 | 7 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 55 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/6` |
| `scnPlaySkAnimEvent` | 10 | 21 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnUnmountEvent` | 1 | 1802 / 768 | `/Data/RootChunk/sceneGraph/Data/graph/137/Data/events/5` |
| `scneventsEquipItemToPerformer` | 1 | 1822 / 795 | `/Data/RootChunk/sceneGraph/Data/graph/141/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 4 | 55 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/2` |
| `scneventsSocket` | 28 | 7 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsVFXEvent` | 4 | 1747 / 713 | `/Data/RootChunk/sceneGraph/Data/graph/129/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 6
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, gaze, socket_signal: 2
- socket_signal: 2
- speech, vfx: 2
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state, mount_workspot: 1
- speech: 1
- speech, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- gaze, socket_signal: 1
- socket_signal, animation_state: 1
- skeletal_animation, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `3387f7167120d8d6521a2c86954dc82a6a8d08aee5c932fc571d9aa5d8d2d942`. Binary SHA-256: `ec45891cc1e3538ce0a7ab22d1625c9e26142fb1479e06b9e20d64b4f7c77f0e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_09a_lookout_intercept.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_09b_guards.scene`

77 graph nodes, 100 edges; 10 event-bearing sections, 88 events; 20 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: guard_01 (actor 0, spawnSet); guard_02 (actor 1, spawnSet); guard_01_garage (actor 2, spawnSet); guard_02_garage (actor 3, spawnSet); Player (actor 4, findInContext).

Entries: `q110_09b_guards_in` → 1; `Start 1` → 959.

Exits: `q110_09b_guards_out` → 2; `TurnOffLookout` → 247.

End nodes: 2: `<omitted>`; 247: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 18 | 51 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnLookAtEvent` | 20 | 51 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 19 | 59 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scneventsAttachPropToPerformer` | 1 | 1007 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/2` |
| `scneventsSocket` | 28 | 59 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/8` |
| `scneventsVFXEvent` | 2 | 59 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 5
- speech, gaze: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- props_equipment, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `e2b1b9e346d49c4b29dffa55aa970be00b20ba62aa5c0af3aa89e57b8e849766`. Binary SHA-256: `3aa42d9f27fadd74ad8077ca2aca9101062b195d8f9cb64c8ea7e6dfb7024fdc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_09b_guards.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_09c_confrontation.scene`

393 graph nodes, 524 edges; 95 event-bearing sections, 627 events; 204 screenplay lines, 42 screenplay options, 18 choice nodes.

Actors: Placide (actor 0, spawnSet); quard_den_01 (actor 1, spawnSet); quard_den_02 (actor 2, spawnSet); quard_den_03 (actor 3, spawnSet); Briggite (actor 4, spawnSet); TiNeptune (actor 5, spawnSet); Player (actor 6, findInContext).

Entries: `q110_09c_confrontation_in` → 1; `q110_09c_confrontation_shortcut_in` → 108; `briggite_default` → 3754; `q110_09c_brigitte_come_on_in` → 2238.

Exits: `q110_09_fadeout_out` → 2; `NetrunnersDenEmpty` → 1307; `q110_09c_brigitte_come_on_out` → 2240.

End nodes: 2: `<omitted>`; 1307: `<omitted>`; 2240: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 751 / 248 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/5` |
| `scnChangeIdleAnimEvent` | 12 | 561 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnDialogLineEvent` | 165 | 561 / 90 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |
| `scnGameplayTransitionEvent` | 10 | 737 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/29` |
| `scnIKEvent` | 20 | 737 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/22` |
| `scnLookAtEvent` | 96 | 635 / 140 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |
| `scnPlaySkAnimEvent` | 104 | 561 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnPoseCorrectionEvent` | 3 | 728 / 173 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scnUnmountEvent` | 10 | 737 / 227 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/28` |
| `scneventsAttachPropToPerformer` | 2 | 1511 / 1002 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/1` |
| `scneventsAttachPropToWorld` | 2 | 1010 / 641 | `/Data/RootChunk/sceneGraph/Data/graph/62/Data/events/47` |
| `scneventsSetAnimFeatureEvent` | 10 | 737 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/27` |
| `scneventsSocket` | 179 | 561 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/3` |
| `scneventsVFXEvent` | 6 | 940 / 451 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 16
- skeletal_animation, gaze, socket_signal: 11
- speech, socket_signal: 9
- speech: 8
- speech, gaze, socket_signal: 7
- speech, skeletal_animation, gaze, socket_signal: 6
- speech, idle_animation, socket_signal: 5
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, vfx, socket_signal: 3
- speech, gaze: 3
- speech, skeletal_animation, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1
- props_equipment: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- gaze, socket_signal: 1
- socket_signal, animation_state: 1

Raw SHA-256: `d64e860a8fc273771cb23615a00040ac80cac8a6624da928c95904ebedac5919`. Binary SHA-256: `6808612d5cd81c54861ef0ef15be0f79a750e3a65414d1865a818af5c5d2f64c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_09c_confrontation.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_10_voodoo_queen_phonecall.scene`

34 graph nodes, 38 edges; 10 event-bearing sections, 12 events; 15 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: voodoo_queen (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `q110_10_phonecall_in` → 1.

Exits: `q110_10_phonecall_loop` → 2; `q110_10_phonecall_progress` → 32.

End nodes: 2: `<omitted>`; 32: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 11 | 11 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnLookAtEvent` | 1 | 194 / 136 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 9
- gaze: 1

Raw SHA-256: `f070f931da3e4458ebd3f6b8312d2b87afcf7eb6a2409ee5b03a91f9c19e8dca`. Binary SHA-256: `2af2290804f3819da443c74488ae9b9f9e425a1215e41937ce1ef707ead1c3c2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_10_voodoo_queen_phonecall.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_12_voodoo_queen.scene`

155 graph nodes, 186 edges; 25 event-bearing sections, 111 events; 40 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: voodoo_queen (actor 0, spawnSet); vdb_elder_1 (actor 1, spawnSet); vdb_elder_2 (actor 2, spawnSet); placide (actor 3, spawnSet); Johnny (actor 4, spawnSet); voodoo_boy01 (actor 5, community); voodoo_boy02 (actor 6, community); voodoo_boy03 (actor 7, community); voodoo_boy04 (actor 8, community); voodoo_boy06 (actor 9, community); vdb_elder_3 (actor 10, spawnSet); v (actor 11, findInContext).

Entries: `q110_12_way_to_maglev_chats_in` → 654; `Start 8` → 1696.

Exits: `q110_12_way_to_maglev_chats_out` → 655; `TurnSceneOff` → 2660; `q110_12_way_to_maglev_chats_out_terminating` → 1598.

End nodes: 655: `NonTerminating`; 1598: `NonTerminating`; 2660: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1672 / 372 | `/Data/RootChunk/sceneGraph/Data/graph/61/Data/events/4` |
| `scnChangeIdleAnimEvent` | 4 | 1585 / 303 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/1` |
| `scnDialogLineEvent` | 22 | 1106 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 1737 / 430 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/6` |
| `scnIKEvent` | 6 | 1737 / 424 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/1` |
| `scnLookAtEvent` | 29 | 1106 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnPlaySkAnimEvent` | 18 | 1106 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnUnmountEvent` | 3 | 1737 / 429 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 3 | 1737 / 427 | `/Data/RootChunk/sceneGraph/Data/graph/70/Data/events/4` |
| `scneventsSocket` | 22 | 1106 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 3
- gaze: 3
- speech, skeletal_animation, gaze: 2
- skeletal_animation, socket_signal: 2
- socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation: 1
- skeletal_animation: 1
- skeletal_animation, gaze: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- idle_animation: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- speech: 1

Raw SHA-256: `796fd68ea2d87f2a36f36e23d5ec523379108c6982c345581919c1a942f54d18`. Binary SHA-256: `bbb62f6fed648fb689d05c077d95ccb37a2819e604b13d451cb90b32d7d2c93f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_12_voodoo_queen.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_13_alt_intro.scene`

683 graph nodes, 799 edges; 72 event-bearing sections, 667 events; 154 screenplay lines, 30 screenplay options, 17 choice nodes.

Actors: Briggite (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Elder_1 (actor 2, spawnSet); Elder_2 (actor 3, spawnSet); Elder_3 (actor 4, spawnSet); Alt (actor 5, spawnSet); Elder_4 (actor 6, spawnSet); Elder_5 (actor 7, spawnSet); Placide (actor 8, spawnSet); V_tpp_male (actor 9, spawnDespawn); V_tpp_female (actor 10, spawnDespawn); TiNeptune (actor 11, spawnSet); johnny_replacer (actor 12, spawnSet); V (actor 13, findInContext).

Entries: `preview` → 3849; `q110_cyberspace_before_q108` → 3862; `bath_preview` → 2026; `cyberspace_preview` → 2052; `DebugStartTrainLights` → 3289; `cyberspace_recording` → 1509; `q110_13_before_q108_in` → 909; `q110_13_after_q108_in` → 914; `Start 9` → 2875; `Start 13` → 4777.

Exits: `cyberspace_recording_end` → 1522; `q110_13_before_q108_out` → 912; `q110_13_after_q108_out` → 917; `cyberspace_on` → 2847.

End nodes: 912: `<omitted>`; 917: `<omitted>`; 1522: `<omitted>`; 2847: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 45 | 1082 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/13` |
| `scnChangeIdleAnimEvent` | 28 | 1170 / 134 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |
| `scnDialogLineEvent` | 126 | 860 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 9 | 1082 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/23` |
| `scnIKEvent` | 18 | 1082 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/20` |
| `scnLookAtEvent` | 94 | 1170 / 133 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/2` |
| `scnPlaySkAnimEvent` | 109 | 860 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnPoseCorrectionEvent` | 4 | 1170 / 147 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/12` |
| `scnUnmountEvent` | 9 | 1082 / 93 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/22` |
| `scneventsAttachPropToNode` | 1 | 1667 / 613 | `/Data/RootChunk/sceneGraph/Data/graph/50/Data/events/3` |
| `scneventsAttachPropToPerformer` | 4 | 1355 / 341 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/13` |
| `scneventsAttachPropToWorld` | 1 | 1355 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/20` |
| `scneventsCameraParamsEvent` | 3 | 1082 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 9 | 1082 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/18` |
| `scneventsSocket` | 175 | 860 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/9` |
| `scneventsVFXEvent` | 32 | 1082 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 9
- speech: 8
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, socket_signal: 4
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, audio, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 3
- speech, skeletal_animation: 2
- skeletal_animation, gaze, socket_signal: 2
- gaze: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- socket_signal: 2
- speech, skeletal_animation, ik, camera, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, audio, vfx, socket_signal: 1
- idle_animation, props_equipment, socket_signal: 1
- speech, audio: 1
- speech, skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal: 1
- idle_animation, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, socket_signal: 1

Raw SHA-256: `a8db01eeec6c130696b01ccd33d26ecf7ac37519cc3721b25cfacf8da11bb191`. Binary SHA-256: `78ef65c267c826ba0796881b287a274992b25e2df1ad7ccb103af9b02a5b9df5`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_13_alt_intro.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_14_alt.scene`

195 graph nodes, 362 edges; 56 event-bearing sections, 360 events; 137 screenplay lines, 24 screenplay options, 9 choice nodes.

Actors: Alt (actor 0, spawnSet); johnny (actor 1, spawnDespawn); voodoo_queen (actor 2, spawnSet); Mosley (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `q110_14_alt_in` → 566.

Exits: `q110_14_alt_out` → 462.

End nodes: 462: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 915 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/4` |
| `scnDialogLineEvent` | 124 | 576 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 77 | 576 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/12` |
| `scnPlaySkAnimEvent` | 103 | 576 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsCameraParamsEvent` | 1 | 1111 / 671 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/3` |
| `scneventsSocket` | 50 | 576 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 1 | 1111 / 678 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 22
- skeletal_animation, socket_signal: 8
- speech: 7
- speech, skeletal_animation, gaze: 4
- speech, gaze: 3
- speech, skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze: 2
- gaze: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, camera, vfx, socket_signal: 1
- idle_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `1860d4bf184b7dafa95d68fd5b5d6dd24a5146d14b746dd142d27c57f9eea910`. Binary SHA-256: `e9f18b5a26beb061f6e8822b76b53f310867c90218e59eed181ab211bce3398f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_14_alt.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_15_vdb_fight.scene`

132 graph nodes, 135 edges; 30 event-bearing sections, 141 events; 52 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); voodoo_boy_001 (actor 1, community); voodoo_boy_002 (actor 2, community); voodoo_boy_003 (actor 3, community); voodoo_boy_004 (actor 4, community); voodoo_boy_010 (actor 5, community); voodoo_boy_009 (actor 6, community); placide (actor 7, spawnSet); vdb_elder_01 (actor 8, spawnSet); vdb_elder_02 (actor 9, spawnSet); vdb_elder_03 (actor 10, spawnSet); vdb_elder_04 (actor 11, spawnSet); vdb_elder_05 (actor 12, spawnSet); voodoo_boy_005 (actor 13, community); voodoo_boy_006 (actor 14, community); brigitte (actor 15, spawnSet); Player (actor 16, findInContext).

Entries: `q110_15_escape_fight_in` → 15; `PlacideChurchFightIn` → 294; `Old` → 308; `q110_15_placide_in_chapel_in` → 197; `q110_15_alerted_patrol_in` → 322; `q110_15_what_was_that` → 208; `q110_15_johnny_need_to_go_in` → 238.

Exits: `q110_15_johnny_need_to_go_out` → 245; `PlacideChurchFightOut` → 295; `placide_chapel_done` → 312; `CheckingOnNetrunnersStart` → 557; `q110_15_alerted_patrol_out` → 324; `StopScene` → 686; `dead_netrunners_spotted` → 327; `alert_start_walking_out` → 330.

End nodes: 245: `NonTerminating`; 295: `<omitted>`; 312: `NonTerminating`; 324: `<omitted>`; 327: `NonTerminating`; 330: `NonTerminating`; 557: `NonTerminating`; 686: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 339 / 369 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/2` |
| `scnChangeIdleAnimEvent` | 8 | 239 / 255 | `/Data/RootChunk/sceneGraph/Data/graph/34/Data/events/1` |
| `scnDialogLineEvent` | 45 | 54 / 137 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 209 / 228 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/19` |
| `scnIKEvent` | 8 | 209 / 216 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/10` |
| `scnLookAtEvent` | 21 | 209 / 199 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/1` |
| `scnPlaySkAnimEvent` | 14 | 209 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/0` |
| `scnUnmountEvent` | 4 | 209 / 227 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/18` |
| `scneventsCameraParamsEvent` | 2 | 339 / 368 | `/Data/RootChunk/sceneGraph/Data/graph/63/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 4 | 209 / 225 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/17` |
| `scneventsSocket` | 30 | 195 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 17
- speech, socket_signal: 4
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal: 1
- idle_animation, gaze: 1
- gaze: 1

Raw SHA-256: `71c546eaa420e82f9b05682bcb7e0df6c57b0f488db048361099db7a4e33c880`. Binary SHA-256: `e1d2657efaa925906343037c49a1fd51768998324a02a2e96c8960256cd50339`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_15_vdb_fight.scene" --events
```

## `base\quest\main_quests\part1\q110\scenes\q110_16b_closing_funeral.scene`

100 graph nodes, 109 edges; 24 event-bearing sections, 144 events; 44 screenplay lines, 10 screenplay options, 5 choice nodes.

Actors: placide (actor 0, spawnSet); voodoo_queen (actor 1, spawnSet); vdb_01 (actor 2, spawnSet); vdb_02 (actor 3, spawnSet); vdb_03 (actor 4, spawnSet); vdb_04 (actor 5, spawnSet); vdb_05 (actor 6, spawnSet); vdb_02_chapel (actor 7, community); Player (actor 8, findInContext).

Entries: `q110_16b_closing_funeral_in` → 1; `PlacideChatChapel` → 105.

Exits: `q110_16b_closing_funeral_out` → 2; `SwitchToEscape` → 69.

End nodes: 2: `NonTerminating`; 69: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 119 / 243 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/4` |
| `scnChangeIdleAnimEvent` | 4 | 25 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/6` |
| `scnDialogLineEvent` | 28 | 6 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 3 | 119 / 270 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/18` |
| `scnIKEvent` | 6 | 119 / 262 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/11` |
| `scnLookAtEvent` | 6 | 6 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 35 | 6 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 137 / 296 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/2` |
| `scnUnmountEvent` | 3 | 119 / 269 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/17` |
| `scneventsCameraParamsEvent` | 4 | 119 / 241 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 3 | 119 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/14` |
| `scneventsSocket` | 49 | 6 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, socket_signal: 5
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech: 2
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, socket_signal, animation_state: 1
- idle_animation, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `07050d795be87fa1ac31542dc3b6db8b34907951fb067c6b0a13ef3d6eef44a8`. Binary SHA-256: `4f656c230d846cf28b54b58dddbee57c3378b20472362c59adf5fde37b516404`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q110\scenes\q110_16b_closing_funeral.scene" --events
```

