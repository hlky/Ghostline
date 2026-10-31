# The Rescue: scene presentation

Journal identity: `quests/main_quest/prologue/q001_intro`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q001_intro.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q115\scenes\q115_00_johnny.scene`

175 graph nodes, 235 edges; 50 event-bearing sections, 331 events; 122 screenplay lines, 25 screenplay options, 7 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `Start 15` → 3120; `Start 16` → 3122; `Start 0` → 2969; `Start 13` → 2628; `q000_car_line_reuse` → 2841; `elevator_in` → 1779.

Exits: `q000_car_line_reuse_end` → 2843; `elevator_out` → 1780.

End nodes: 1780: `<omitted>`; 2843: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 2243 / 484 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/3` |
| `scnChangeIdleAnimEvent` | 26 | 1818 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnDialogLineEvent` | 99 | 1782 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 2218 / 469 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/15` |
| `scnIKEvent` | 8 | 2218 / 466 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/12` |
| `scnLookAtEvent` | 28 | 1826 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/15` |
| `scnPlaySkAnimEvent` | 54 | 1822 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnUnmountEvent` | 4 | 2218 / 468 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/14` |
| `scneventsAttachPropToNode` | 2 | 2243 / 483 | `/Data/RootChunk/sceneGraph/Data/graph/45/Data/events/2` |
| `scneventsAttachPropToPerformer` | 4 | 2409 / 547 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/2` |
| `scneventsCameraParamsEvent` | 3 | 2218 / 462 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 4 | 2218 / 463 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/10` |
| `scneventsSocket` | 84 | 1818 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scneventsVFXEvent` | 3 | 2218 / 449 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 11
- speech: 5
- speech, idle_animation, socket_signal: 4
- speech, idle_animation: 3
- speech, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- skeletal_animation, socket_signal: 3
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- speech, skeletal_animation, socket_signal: 2
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- gaze, socket_signal: 2
- skeletal_animation, ik, camera, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `9b6ce12f5753742524ff7b6e7533bca1f515afb1977ce975c26a41de6bfc8dcd`. Binary SHA-256: `aee544c6cc434ac5af2256f8b73db5bee8ec3b5d9502d0d1a25ab1c2483f1b23`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_00_johnny.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_corpo_01_security_gate.scene`

208 graph nodes, 260 edges; 36 event-bearing sections, 184 events; 54 screenplay lines, 9 screenplay options, 6 choice nodes.

Actors: arasaka_m_security_01 (actor 0, community); arasaka_f_corporate_01_right_line (actor 1, findInWorld); arasaka_m_corporate_01_right_line (actor 2, findInWorld); arasaka_f_corporate_02_right_line (actor 3, findInWorld); arasaka_m_security_02 (actor 4, findInWorld); arasaka_f_security_01 (actor 5, findInWorld); arasaka_m_corporate_05_reception (actor 6, findInWorld); Jackie (actor 7, spawnSet); arasaka_m_corporate_walk_in (actor 8, community); player_tpp_male (actor 9, spawnDespawn); player_tpp_female (actor 10, spawnDespawn); Player (actor 11, findInContext).

Entries: `in` → 1; `Start 6` → 875; `chat_preview` → 715; `Start 8` → 3299; `Start 7` → 965; `line_oneliners_01_in` → 321; `line_oneliners_02_in` → 323; `line_oneliners_03_in` → 325; `DisconnectedChoices` → 837.

Exits: `out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 11 | 272 / 129 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/5` |
| `scnDialogLineEvent` | 34 | 72 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 263 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/7` |
| `scnIKEvent` | 8 | 263 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |
| `scnLookAtEvent` | 13 | 110 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 34 | 110 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnUnmountEvent` | 4 | 263 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/11` |
| `scneventsCameraParamsEvent` | 11 | 263 / 94 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 4 | 263 / 98 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/10` |
| `scneventsSocket` | 51 | 217 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/2` |
| `scneventsVFXEvent` | 10 | 272 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- speech, socket_signal: 7
- skeletal_animation: 4
- speech, skeletal_animation: 3
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- camera, socket_signal: 2
- skeletal_animation, gaze, camera, audio, vfx, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- gaze: 1

Raw SHA-256: `5aaa70097099acb183257da86b7b56530b8202cddaf4125d2aa6569a5be72bc4`. Binary SHA-256: `75fb71fab723784911b45b2979d4ac430585678f82a3e13eb0f6db6e2f6a3d9a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_corpo_01_security_gate.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_corpo_01a_lobby_chats.scene`

48 graph nodes, 50 edges; 11 event-bearing sections, 71 events; 33 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: arasaka_m_corporate_06_divorce_chat (actor 0, community); arasaka_m_corporate_07_divorce_chat (actor 1, community); arasaka_f_corporate_04_stocks_chat (actor 2, community); arasaka_m_corporate_08_stocks_chat (actor 3, community); arasaka_f_corporate_05_phone_chat (actor 4, community); arasaka_f_corporate_06_overdose_chat (actor 5, community); arasaka_f_corporate_07_overdose_chat (actor 6, community); arasaka_f_corporate_08_war_chat (actor 7, findInWorld); arasaka_m_corporate_09_war_chat (actor 8, findInWorld); arasaka_m_corporate_10_phone_chat (actor 9, community); stall_occupant_01 (actor 10, community); stall_occupant_02 (actor 11, community); stall_occupant_03 (actor 12, community); Player (actor 13, findInContext).

Entries: `in` → 1; `SingleScene` → 95.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 28 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 1 | 12 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/17` |
| `scnIKEvent` | 2 | 12 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |
| `scnLookAtEvent` | 22 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 10 | 8 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/5` |
| `scnUnmountEvent` | 1 | 12 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/16` |
| `scneventsSetAnimFeatureEvent` | 1 | 12 / 61 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/13` |
| `scneventsSocket` | 6 | 12 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- skeletal_animation, socket_signal: 2
- gaze: 2
- speech, gaze: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `e375ef157b7557d21e0c9719496380e09de7e695e0f2606d193afa17de67a354`. Binary SHA-256: `d3c591c472f80c06f103eb7f18bc1a5b5b27de47d961135a5eaf235fdc75ab8e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_corpo_01a_lobby_chats.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_corpo_02_to_elevators.scene`

263 graph nodes, 323 edges; 39 event-bearing sections, 169 events; 71 screenplay lines, 8 screenplay options, 4 choice nodes.

Actors: corpo_friend (actor 0, community); agent_jenkins (actor 1, spawnSet); arasaka_ai (actor 2, community); corpo_01_elevator (actor 3, community); corpo_02_elevator (actor 4, community); corpo_03_elevator (actor 5, community); corpo_04_elevator (actor 6, community); arasaka_ai_2 (actor 7, community); arasaka_ai_voice (actor 8, findInContext); Player (actor 9, findInContext).

Entries: `in` → 1; `q000_corpo_02_arasaka_propaganda_in` → 1067; `q113_q115_elevator_in` → 377; `Start 3` → 666; `Start 5` → 687; `q000_corpo_02_frank_in` → 1239; `Start 8` → 1294.

Exits: `out` → 2; `q000_corpo_02_arasaka_propaganda_out` → 1069; `q113_q115_elevator_out` → 1420; `PrepareJenkinsFloor` → 683; `ad_over_out` → 437.

End nodes: 2: `NonTerminating`; 437: `NonTerminating`; 683: `NonTerminating`; 1069: `<omitted>`; 1420: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 5 | 59 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnDialogLineEvent` | 41 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 541 / 367 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/13` |
| `scnIKEvent` | 2 | 541 / 347 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/4` |
| `scnLookAtEvent` | 34 | 57 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnPlaySkAnimEvent` | 31 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnUnmountEvent` | 1 | 541 / 366 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 1 | 541 / 362 | `/Data/RootChunk/sceneGraph/Data/graph/43/Data/events/9` |
| `scneventsSocket` | 53 | 3 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- gaze: 8
- skeletal_animation, gaze, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- socket_signal: 3
- skeletal_animation, socket_signal: 3
- gaze, socket_signal: 3
- speech, skeletal_animation, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation: 1

Raw SHA-256: `75394ac2bbf2bb2f829819facc7bb0a3778932cfdcc50cc6f44722b312e01a01`. Binary SHA-256: `adad2c0437680fc474d1e648844f569a210d0866597fb82b82085a1e28a7e8d7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_corpo_02_to_elevators.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_corpo_03_jenkins.scene`

377 graph nodes, 425 edges; 56 event-bearing sections, 580 events; 120 screenplay lines, 19 screenplay options, 10 choice nodes.

Actors: Jenkins (actor 0, findInWorld); Abernathy (actor 1, spawnDespawn); Netrunner (actor 2, findInContext); Jackie (actor 3, spawnSet); AI (actor 4, spawnDespawn); euro_council_f_001 (actor 5, community); euro_council_f_002 (actor 6, community); euro_council_f_003 (actor 7, community); euro_council_f_004 (actor 8, community); euro_council_m_001 (actor 9, community); euro_council_m_002 (actor 10, community); euro_council_m_003 (actor 11, community); euro_council_m_004 (actor 12, community); euro_council_m_005 (actor 13, community); euro_council_m_006 (actor 14, community); euro_council_m_007 (actor 15, community); euro_council_m_008 (actor 16, community); euro_council_f_005 (actor 17, community); euro_council_f_006 (actor 18, community); euro_council_f_007 (actor 19, community); euro_council_m_009 (actor 20, community); euro_council_m_010 (actor 21, community); flyby_av (actor 22, spawner); Player (actor 23, findInContext).

Entries: `office_in` → 1; `Start 5` → 1647; `Start 6` → 1731; `council_recording_cam1` → 1755; `council_recording_cam2` → 1766; `council_recording_cam1_burnout` → 1789; `jenkins_default_fluff_in` → 186; `Start 2` → 1203; `old` → 1205; `q000_03_jackie_call_in` → 1594; `Start 1` → 644.

Exits: `office_out` → 2; `esc_recording_burnout_out` → 1806; `council_recording_cam1_out` → 1811; `council_recording_cam2_out` → 1813; `jenkins_default_fluff` → 201; `q000_03_jackie_call_out` → 1596; `PrefetchAssistant` → 3920.

End nodes: 2: `NonTerminating`; 201: `NonTerminating`; 1596: `NonTerminating`; 1806: `<omitted>`; 1811: `<omitted>`; 1813: `<omitted>`; 3920: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 22 | 17 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnChangeIdleAnimEvent` | 24 | 17 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnDialogLineEvent` | 87 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 640 / 790 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/17` |
| `scnIKEvent` | 10 | 640 / 780 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/8` |
| `scnLookAtEvent` | 146 | 79 / 199 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |
| `scnPlaySkAnimEvent` | 150 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayVideoEvent` | 3 | 31 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPoseCorrectionEvent` | 1 | 371 / 547 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/17` |
| `scnUnmountEvent` | 2 | 640 / 789 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/16` |
| `scneventsAttachPropToNode` | 2 | 76 / 187 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/15` |
| `scneventsAttachPropToPerformer` | 4 | 76 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/9` |
| `scneventsAttachPropToWorld` | 2 | 274 / 348 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/9` |
| `scneventsCameraParamsEvent` | 4 | 76 / 171 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 2 | 640 / 785 | `/Data/RootChunk/sceneGraph/Data/graph/89/Data/events/13` |
| `scneventsSocket` | 109 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsVFXEvent` | 10 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 20
- speech, skeletal_animation, gaze, socket_signal: 7
- gaze: 4
- speech, video: 2
- speech, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- skeletal_animation, idle_animation, gaze, ik, socket_signal: 2
- speech, skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal, video: 1
- speech, skeletal_animation, idle_animation, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, camera, audio, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- skeletal_animation, gaze: 1
- skeletal_animation, gaze, audio, socket_signal: 1

Raw SHA-256: `f8ea4fd2377f3b8b5aba2d06bfc44df90fde757b98a1613e4760a913c7fd695f`. Binary SHA-256: `23b38a7768c6aefc593bcd451c11f7db661044954f37f0805282599a32b87bd9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_corpo_03_jenkins.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_corpo_03a_office_chats.scene`

284 graph nodes, 357 edges; 55 event-bearing sections, 348 events; 102 screenplay lines, 17 screenplay options, 11 choice nodes.

Actors: arasaka_f_corporate_01_reception_chat (actor 0, community); arasaka_f_corporate_02_reception_chat (actor 1, community); arasaka_m_corporate_01_reception_chat (actor 2, community); arasaka_f_corporate_03_office_gossip (actor 3, community); arasaka_m_corporate_02_office_gossip (actor 4, community); arasaka_f_corporate_04_meeting_chat (actor 5, community); arasaka_m_corporate_03_meeting_chat (actor 6, community); arasaka_m_corporate_04_meeting_chat (actor 7, community); arasaka_f_corporate_05_phone_chat (actor 8, community); arasaka_m_corporate_05_front_desk (actor 9, community); arasaka_coworker (actor 10, spawnSet); arasaka_m_corporate_7_big_room (actor 11, community); arasaka_f_corporate_7_big_room (actor 12, community); assistant (actor 13, community); ara_m_corpo_hangar_chat_01 (actor 14, community); ara_f_corpo_hangar_chat_02 (actor 15, community); sampson (actor 16, community); window_room_m (actor 17, community); window_room_f (actor 18, community); Player (actor 19, findInContext).

Entries: `Start 7` → 1719; `OLD` → 844; `assistant_in` → 366; `elevator_chat_in` → 368; `office_gossip_in` → 370; `meeting_chat_in` → 372; `phone_f_chat_in` → 374; `front_desk_in` → 376; `booster_in` → 378; `asking_input_in` → 380; `big_room_chat_in` → 382; `hangar_chat_in` → 383; `player_at_desk` → 388; `window_room_in` → 1180.

Exits: `assistant_out` → 748; `Drawer` → 2249.

End nodes: 748: `NonTerminating`; 2249: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 401 / 635 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/7` |
| `scnChangeIdleAnimEvent` | 21 | 52 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scnDialogLineEvent` | 69 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnGameplayTransitionEvent` | 8 | 9 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/14` |
| `scnIKEvent` | 16 | 9 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnLookAtEvent` | 57 | 6 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnPlaySkAnimEvent` | 63 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scnPoseCorrectionEvent` | 1 | 343 / 569 | `/Data/RootChunk/sceneGraph/Data/graph/66/Data/events/2` |
| `scnUnmountEvent` | 8 | 9 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/13` |
| `scneventsCameraParamsEvent` | 2 | 735 / 1078 | `/Data/RootChunk/sceneGraph/Data/graph/146/Data/events/3` |
| `scneventsEquipItemToPerformer` | 3 | 114 / 281 | `/Data/RootChunk/sceneGraph/Data/graph/26/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 8 | 9 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/12` |
| `scneventsSocket` | 86 | 9 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 549 / 745 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 7
- speech: 6
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- gaze: 4
- speech, gaze: 3
- skeletal_animation, idle_animation, audio, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- idle_animation, socket_signal: 2
- socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- gaze, socket_signal: 2
- speech, skeletal_animation, gaze: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- socket_signal, animation_state: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- idle_animation, props_equipment, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `9bb896fb7b475ecc2f043fe80ad09a3353f78a54bfdeb7fd75383b6758ef55c3`. Binary SHA-256: `72aa53afbb452a457eba9324698907375bf1feb63f0babe9502f415e1a225a35`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_corpo_03a_office_chats.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_corpo_03b_fly_to_lizzies.scene`

132 graph nodes, 149 edges; 25 event-bearing sections, 66 events; 45 screenplay lines, 9 screenplay options, 6 choice nodes.

Actors: AI (actor 0, spawnDespawn); Coach (actor 1, spawnSet); Radio (actor 2, findInContext); basket_player_01 (actor 3, community); basket_player_02 (actor 4, community); backet_player_03 (actor 5, community); jenkins_av (actor 6, spawner); Player (actor 7, findInContext).

Entries: `q000_corpo_03b_in` → 1; `old` → 1008; `coach_preview` → 860; `Start 3` → 416; `q000_corpo_03b_get_in_interaction_in` → 263; `Start 5` → 746; `NewsRadioSystemIn` → 748; `Start 4` → 588; `HangarAIMessageIn` → 158.

Exits: `q000_corpo_03b_out` → 2; `TowerCleanup` → 14; `Terminate` → 3870; `HangarAIMessageOut` → 234; `q000_corpo_lizzies_basket` → 600; `NewsRadioSystemOut` → 763.

End nodes: 2: `NonTerminating`; 14: `NonTerminating`; 234: `<omitted>`; 600: `NonTerminating`; 763: `<omitted>`; 3870: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 31 | 6 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnLookAtEvent` | 1 | 3882 / 651 | `/Data/RootChunk/sceneGraph/Data/graph/126/Data/events/1` |
| `scnPlaySkAnimEvent` | 3 | 54 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/1` |
| `scneventsAttachPropToPerformer` | 3 | 54 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 3 | 54 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scneventsSocket` | 12 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 7 | 54 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- speech, socket_signal: 3
- skeletal_animation, props_equipment, audio, vfx, socket_signal, animation_state: 2
- speech, audio, socket_signal: 1
- skeletal_animation, audio, vfx, socket_signal, animation_state: 1
- audio, socket_signal: 1
- props_equipment, vfx: 1
- gaze, socket_signal: 1

Raw SHA-256: `cee865b997de2c2731cb6fe6f1f834b3b80b8d0710bb4a29486e75e770ea6284`. Binary SHA-256: `1c0bb8fbd25df5143c7463208684b434156a6d9787fb36ea636c1a494d4f47c7`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_corpo_03b_fly_to_lizzies.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_corpo_04_lizzies_club.scene`

577 graph nodes, 688 edges; 116 event-bearing sections, 1065 events; 213 screenplay lines, 41 screenplay options, 18 choice nodes.

Actors: Jackie (actor 0, spawnSet); corpo_friend (actor 1, community); arasaka_m_corporate (actor 2, community); arasaka_m_security_01 (actor 3, community); arasaka_m_security_02 (actor 4, community); arasaka_m_security_03 (actor 5, community); lizzies_bouncer (actor 6, community); johnny (actor 7, findInContext); barman (actor 8, spawnSet); basket_player_01 (actor 9, community); basket_player_02 (actor 10, community); basket_player_03 (actor 11, community); waitress (actor 12, community); client (actor 13, community); lizzies_guard (actor 14, community); test (actor 15, community); AI (actor 16, spawnDespawn); flight_bg_m_001 (actor 17, spawnDespawn); flight_bg_m_002 (actor 18, spawnDespawn); flight_bg_m_003 (actor 19, spawnDespawn); flight_bg_f_004 (actor 20, spawnDespawn); av (actor 21, spawner); Player (actor 22, findInContext).

Entries: `q000_corpo_04_lizzies_in` → 1; `Start 19` → 3814; `in_the_club` → 1156; `Start 4` → 1288; `ending` → 3505; `Start 10` → 2440; `q000_corpo_04_lizzies_av_landing_in` → 2443; `q000_corpo_04_q112_clone_in` → 2481; `Start 2` → 863; `q000_corpo_04_q112_clone_02_in` → 2492; `q000_lizzies_chicken_test` → 1962; `q000_corpo_lizzies_basket` → 2043; `FAKE INPUT FOR LOCO2` → 2676; `FAKE INPUT FOR LOCO` → 2701.

Exits: `q000_corpo_04_lizzies_out` → 2; `MontagePreloadOut` → 3800; `q000_corpo_04_lizzies_av_landing_out` → 2444; `q000_corpo_04_q112_clone_out` → 2483; `q000_corpo_04_q112_clone_02_out` → 2494.

End nodes: 2: `<omitted>`; 2444: `NonTerminating`; 2483: `<omitted>`; 2494: `<omitted>`; 3800: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 94 | 14 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/10` |
| `scnChangeIdleAnimEvent` | 46 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 145 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnGameplayTransitionEvent` | 19 | 60 / 600 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/49` |
| `scnIKEvent` | 38 | 60 / 534 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/3` |
| `scnLookAtEvent` | 161 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 220 | 4 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPoseCorrectionEvent` | 10 | 14 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scnUnmountEvent` | 19 | 60 / 602 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/51` |
| `scneventsAttachPropToNode` | 3 | 14 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/17` |
| `scneventsAttachPropToPerformer` | 20 | 14 / 62 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scneventsAttachPropToWorld` | 11 | 14 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/32` |
| `scneventsCameraParamsEvent` | 10 | 67 / 639 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/5` |
| `scneventsEquipItemToPerformer` | 2 | 951 / 1748 | `/Data/RootChunk/sceneGraph/Data/graph/115/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 19 | 60 / 598 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/48` |
| `scneventsSocket` | 239 | 4 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/9` |
| `scneventsVFXDurationEvent` | 1 | 2073 / 3425 | `/Data/RootChunk/sceneGraph/Data/graph/348/Data/events/1` |
| `scneventsVFXEvent` | 8 | 22 / 233 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 14
- skeletal_animation, socket_signal: 12
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 7
- camera: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, socket_signal: 5
- socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 3
- gaze: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- gaze, socket_signal: 2
- speech, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio: 1
- speech, skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, audio, vfx: 1
- idle_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, vfx, socket_signal: 1
- skeletal_animation: 1
- speech, skeletal_animation: 1
- idle_animation: 1

Raw SHA-256: `10e70ec5c7c8da13b9c0b77003eb11519f172e3ee4a47326c4fa940e6af8c073`. Binary SHA-256: `a7b26ade6b37a4b65ec38dfda381aeacea257add915b1a83ec17ad026ec7610f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_corpo_04_lizzies_club.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_01a_bar_activities.scene`

113 graph nodes, 124 edges; 18 event-bearing sections, 151 events; 52 screenplay lines, 4 screenplay options, 2 choice nodes.

Actors: mercenary_01 (actor 0, community); mercenary_02 (actor 1, community); valentino1 (actor 2, community); valentino2 (actor 3, community); valentino3 (actor 4, community); valentino4 (actor 5, community); bar_bouncer (actor 6, community); drug_dealer (actor 7, community); mama_welles (actor 8, spawnSet); kirk_sawyer (actor 9, spawnSet); delivery_man_01 (actor 10, community); delivery_man_02 (actor 11, community); bar_staffer (actor 12, community); hobo1 (actor 13, community); hobo2 (actor 14, community); hobo3 (actor 15, community); hobo4 (actor 16, community); hobo5 (actor 17, community); hobo6 (actor 18, community); hooker (actor 19, community); patron_01_male (actor 20, community); patron_02_male (actor 21, community); woman (actor 22, community); patron_03_male (actor 23, community); q000_backalley_cat (actor 24, spawnDespawn); q000_balcony_smoker (actor 25, community); toilet_valentino (actor 26, community); Player (actor 27, findInContext).

Entries: `Bar_Activities_In` → 1; `hooker_preview` → 816; `HookerChat_In` → 858; `HomelessChat_In` → 862.

Exits: `End 3` → 497; `HookerChat_Out` → 860; `HomelessChat_End` → 864.

End nodes: 497: `NonTerminating`; 860: `NonTerminating`; 864: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 160 / 212 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/0` |
| `scnDialogLineEvent` | 49 | 20 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 72 / 109 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/18` |
| `scnIKEvent` | 4 | 72 / 103 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/13` |
| `scnLookAtEvent` | 44 | 20 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 28 | 20 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 2 | 72 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/17` |
| `scneventsSetAnimFeatureEvent` | 2 | 72 / 106 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/16` |
| `scneventsSocket` | 16 | 72 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 72 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/10` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 6
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, skeletal_animation, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, idle_animation, gaze: 1
- speech, gaze, socket_signal: 1
- speech: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `7f2fd8bd51d807aece19fcf31aab9adb6d8988de5bc3b40561a90eb5887e0cbf`. Binary SHA-256: `606aa4a9f6b194b2d0ebeb23e431a6e5835a404a0c75ef554e5c82a52a499e12`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_01a_bar_activities.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_01b_meet_your_fixer.scene`

334 graph nodes, 408 edges; 60 event-bearing sections, 647 events; 101 screenplay lines, 29 screenplay options, 18 choice nodes.

Actors: kirk_sawyer (actor 0, spawnSet); bartender (actor 1, spawnSet); big_joe (actor 2, community); v_male_tpp (actor 3, spawnDespawn); v_female_tpp (actor 4, spawnDespawn); Player_fpp (actor 5, findInContext).

Entries: `Meet_Your_Fixer_In` → 1; `coyote_performance_test` → 1743; `q000_pepe_after_kirk` → 1302; `mq017_reminder_in` → 1831; `kirk_preview` → 371.

Exits: `Meet_Your_Fixer_Out` → 2; `activate_chats` → 364.

End nodes: 2: `NonTerminating`; 364: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 28 | 62 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnChangeIdleAnimEvent` | 43 | 62 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 101 | 60 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayTransitionEvent` | 5 | 179 / 351 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scnIKEvent` | 10 | 179 / 337 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 159 / 300 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/32` |
| `scnLookAtEvent` | 105 | 62 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 164 | 60 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnUnmountEvent` | 5 | 179 / 357 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/15` |
| `scneventsAttachPropToNode` | 1 | 848 / 1654 | `/Data/RootChunk/sceneGraph/Data/graph/135/Data/events/6` |
| `scneventsAttachPropToPerformer` | 16 | 159 / 275 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/15` |
| `scneventsAttachPropToWorld` | 14 | 62 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scneventsCameraParamsEvent` | 19 | 154 / 196 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scneventsSetAnimFeatureEvent` | 5 | 179 / 353 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/12` |
| `scneventsSocket` | 123 | 60 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsVFXEvent` | 6 | 197 / 378 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- gaze: 7
- camera: 6
- speech, gaze: 4
- speech, skeletal_animation, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal: 3
- speech, skeletal_animation, idle_animation, socket_signal: 3
- speech: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, ik, camera, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal: 2
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, camera, props_equipment, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `6fdc79f6cae99f93b73f2970fa5e5e18ed0d0a279763f8c5fa5a149bea4fe590`. Binary SHA-256: `afdad5ffee1d0b1535ec9cfac659e31622c0298d12a7fe6aaab299c8fa1bd855`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_01b_meet_your_fixer.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_01c_car.scene`

269 graph nodes, 337 edges; 59 event-bearing sections, 494 events; 105 screenplay lines, 12 screenplay options, 9 choice nodes.

Actors: Padre (actor 0, spawnSet); Marcus (actor 1, community); 6h_street_ganger (actor 2, community); 6th_street_trunk (actor 3, spawnDespawn); 6th_street_ganger_02 (actor 4, community); embers_worker (actor 5, community); embers_homeless (actor 6, community); padre_car (actor 7, spawnSet); 6th_street_car (actor 8, spawner); av_lux (actor 9, spawner); Player (actor 10, findInContext).

Entries: `Start 0` → 1; `Start 3` → 1215; `u_turn_test` → 1520; `preview_pt2` → 819; `Start 6` → 1536; `ck_begin_drive` → 362; `Start 7` → 1550; `Start 8` → 1849.

Exits: `End 1` → 39; `End FT` → 1885.

End nodes: 39: `NonTerminating`; 1885: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 61 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/5` |
| `scnChangeIdleAnimEvent` | 56 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnDialogLineEvent` | 76 | 5 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayActionEvent` | 7 | 61 / 172 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/10` |
| `scnIKEvent` | 18 | 61 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/12` |
| `scnLookAtEvent` | 106 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 10 | 61 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/30` |
| `scnPlaySkAnimEvent` | 98 | 5 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/6` |
| `scneventsAttachPropToNode` | 1 | 656 / 806 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/3` |
| `scneventsAttachPropToPerformer` | 3 | 186 / 523 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/4` |
| `scneventsAttachPropToWorld` | 1 | 223 / 630 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/11` |
| `scneventsCameraParamsEvent` | 5 | 223 / 624 | `/Data/RootChunk/sceneGraph/Data/graph/42/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 29 | 61 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scneventsSocket` | 73 | 5 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsVFXEvent` | 2 | 64 / 227 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/7` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- skeletal_animation: 8
- gaze: 7
- speech, gaze: 3
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state, gameplay_action: 3
- speech, skeletal_animation, socket_signal: 2
- speech, idle_animation, gaze: 2
- skeletal_animation, gaze: 2
- socket_signal, animation_state, mount_workspot: 2
- camera: 2
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, camera, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, ik, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, gaze, camera, audio, socket_signal, gameplay_action: 1
- idle_animation, gaze, socket_signal, animation_state: 1
- speech: 1
- skeletal_animation, idle_animation, gaze, socket_signal, gameplay_action: 1
- skeletal_animation, idle_animation, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `056e0b760e8d44a4e88b40562de4c0e910601d2a08690ff924d8a2a9de3f5bac`. Binary SHA-256: `7927e2da4f9645b7c1a54b67df3f21e29ad7fc03ca2436697e123373a55728b2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_01c_car.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_02_fixer_calls.scene`

64 graph nodes, 74 edges; 8 event-bearing sections, 71 events; 18 screenplay lines, 2 screenplay options, 1 choice nodes.

Actors: fixer_kirk (actor 0, spawnSet); parking_security_booth (actor 1, community); eric_dawson (actor 2, community); Player (actor 3, findInContext).

Entries: `Fixer_Calls_in` → 1.

Exits: `Fixer_Calls_Out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 13 | 10 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 17 | 10 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnLookAtEvent` | 13 | 10 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlaySkAnimEvent` | 9 | 10 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 6 | 297 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scneventsSocket` | 13 | 297 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `60ea7320f26d3b64f33446db5d45b6c60c54d95f708281407d30b7e15804821a`. Binary SHA-256: `db2f7865d711decdd4a8199750dc91650426273ddccecdfa5f4a35760a40dacb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_02_fixer_calls.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_02a_confront_jackie.scene`

180 graph nodes, 199 edges; 28 event-bearing sections, 480 events; 59 screenplay lines, 8 screenplay options, 5 choice nodes.

Actors: jackie (actor 0, spawnSet); Stints (actor 1, community); fujioka_kaoru (actor 2, community); police_officer_03 (actor 3, community); police_officer_02 (actor 4, community); police_officer_01 (actor 5, community); Kirk (actor 6, spawnSet); bodyguard_01 (actor 7, community); bodyguard_02 (actor 8, community); cop_vehicle_01 (actor 9, community); cop_vehicle_02 (actor 10, community); rayfield (actor 11, spawner); Player (actor 12, findInContext).

Entries: `Confront_Jackie_In` → 1; `Start 4` → 1444; `Police_Arrival_In` → 241.

Exits: `Confront_Jackie_Out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 27 | 55 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnChangeIdleAnimEvent` | 50 | 55 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 53 | 55 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/8` |
| `scnGameplayActionEvent` | 4 | 55 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnGameplayTransitionEvent` | 3 | 1312 / 1292 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/87` |
| `scnIKEvent` | 6 | 1312 / 1160 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/1` |
| `scnLookAtAdvancedEvent` | 2 | 55 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/11` |
| `scnLookAtEvent` | 98 | 55 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnPlaySkAnimEvent` | 114 | 55 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPoseCorrectionEvent` | 2 | 1312 / 1279 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/77` |
| `scnUnmountEvent` | 3 | 1312 / 1290 | `/Data/RootChunk/sceneGraph/Data/graph/103/Data/events/85` |
| `scneventsAttachPropToNode` | 2 | 897 / 551 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/12` |
| `scneventsAttachPropToPerformer` | 7 | 99 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scneventsAttachPropToWorld` | 1 | 1276 / 949 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/44` |
| `scneventsCameraParamsEvent` | 8 | 55 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 8 | 99 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scneventsSocket` | 76 | 55 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scneventsVFXDurationEvent` | 2 | 1276 / 888 | `/Data/RootChunk/sceneGraph/Data/graph/92/Data/events/12` |
| `scneventsVFXEvent` | 14 | 55 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation: 4
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 3
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, gameplay_action: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, props_equipment, audio, vfx, socket_signal, gameplay_action: 1
- idle_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, vfx, socket_signal, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, ik, camera, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `577510bc6c22ea37c819e1e794af6a0d0b730c5a3afa63f079e5c9e6e1479e48`. Binary SHA-256: `d8572d9e3661f66092c35d34e1c49f96be238e26081d3352fc830bdbc657e636`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_02a_confront_jackie.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_kid_03_back_to_bar.scene`

83 graph nodes, 94 edges; 18 event-bearing sections, 186 events; 45 screenplay lines, 9 screenplay options, 5 choice nodes.

Actors: jackie (actor 0, spawnSet); walker_01 (actor 1, community); police_officer_01 (actor 2, spawnDespawn); police_officer_02 (actor 3, spawnDespawn); q000_police_car_01 (actor 4, spawner); Player (actor 5, findInContext).

Entries: `Back_To_Bar_In` → 1.

Exits: `Back_To_Bar_Out` → 2; `MontagePreloadOut` → 390.

End nodes: 2: `<omitted>`; 390: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 90 / 249 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/10` |
| `scnChangeIdleAnimEvent` | 17 | 33 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 42 | 33 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 122 / 386 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/15` |
| `scnIKEvent` | 4 | 122 / 367 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/1` |
| `scnLookAtEvent` | 29 | 44 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlaySkAnimEvent` | 33 | 33 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 3 | 65 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/19` |
| `scnUnmountEvent` | 2 | 122 / 385 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/14` |
| `scneventsCameraParamsEvent` | 7 | 65 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/18` |
| `scneventsSetAnimFeatureEvent` | 2 | 122 / 381 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/11` |
| `scneventsSocket` | 40 | 33 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 3 | 90 / 235 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 10
- speech: 2
- camera: 2
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `4b097e755b1e6afb731298f99bb736c59d6f18b919069ebdb37287c5c424b569`. Binary SHA-256: `29de55aeaa65a6555f19570a6adfcbade714bd257ecc286c11b614b1850c4b3e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_kid_03_back_to_bar.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_01_garage.scene`

308 graph nodes, 387 edges; 51 event-bearing sections, 453 events; 89 screenplay lines, 25 screenplay options, 18 choice nodes.

Actors: Mechanic (actor 0, spawnSet); Sheriff (actor 1, spawnSet); player_tpp_female (actor 2, spawnDespawn); player_tpp_male (actor 3, spawnDespawn); player_galena (actor 4, spawnSet); Player (actor 5, findInContext).

Entries: `q000_kid_01_garage_in` → 1; `Start 4` → 2440.

Exits: `q000_kid_01_garage_out` → 2; `FT _Terminating_End` → 867.

End nodes: 2: `NonTerminating`; 867: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 23 | 27 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/3` |
| `scnChangeIdleAnimEvent` | 37 | 21 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 76 | 21 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnGameplayActionEvent` | 2 | 27 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/5` |
| `scnGameplayTransitionEvent` | 4 | 217 / 497 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/26` |
| `scnIKEvent` | 12 | 36 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnLookAtEvent` | 53 | 36 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/9` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 698 / 1026 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/10` |
| `scnPlaySkAnimEvent` | 79 | 27 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPoseCorrectionEvent` | 2 | 36 / 96 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/18` |
| `scnUnmountEvent` | 4 | 217 / 509 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/35` |
| `scneventsAttachPropToNode` | 7 | 217 / 495 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/24` |
| `scneventsAttachPropToPerformer` | 3 | 36 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scneventsAttachPropToWorld` | 6 | 36 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scneventsCameraParamsEvent` | 7 | 217 / 473 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/6` |
| `scneventsSetAnimFeatureEvent` | 8 | 27 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scneventsSocket` | 110 | 21 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scneventsVFXEvent` | 19 | 27 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, gaze: 5
- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- speech: 4
- gaze: 3
- camera: 3
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- skeletal_animation, idle_animation, gaze, camera, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 2
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal, animation_state, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, ik, camera, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 1
- speech, audio, vfx: 1
- speech, socket_signal: 1
- skeletal_animation, idle_animation, gaze, camera, props_equipment, audio, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, idle_animation, ik, props_equipment, audio, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1
- props_equipment: 1

Raw SHA-256: `71b794d483c71a81aaec848de3dcfb34824a1b69e6341f1cc8d6119ad780e43f`. Binary SHA-256: `4c801543f476b59f22861afc67c20b4a5e7560860c422841c623508069669dcd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_01_garage.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_01b_roadhouse_chats.scene`

121 graph nodes, 153 edges; 17 event-bearing sections, 90 events; 51 screenplay lines, 9 screenplay options, 3 choice nodes.

Actors: chat_01_man_001 (actor 0, community); chat_01_man_002 (actor 1, community); chat_02_man_001 (actor 2, community); chat_02_woman_001 (actor 3, community); chat_03_man_001 (actor 4, community); chat_03_man_002 (actor 5, community); sheriff (actor 6, spawnSet); mechanic (actor 7, spawnSet); chat_04_boxer (actor 8, community); chat_04_trainer (actor 9, community); chat_04_slacker (actor 10, community); chat_04_weightlifter (actor 11, community); chat_05_ramp_smoker_01 (actor 12, community); chat_05_ramp_smoker_02 (actor 13, community); chat_06_cart_vendor (actor 14, community); chat_07_drone_guy (actor 15, community); chat_08_basketball_player_01 (actor 16, community); chat_08_basketball_player_02 (actor 17, community); chat_09_walker_01 (actor 18, community); chat_08_basketball_player_03 (actor 19, community); chat_08_card_player_01 (actor 20, community); chat_08_card_player_02 (actor 21, community); drone_01 (actor 22, spawner); drone_02 (actor 23, spawner); drone_03 (actor 24, spawner); drone_04 (actor 25, spawner); roadhouse_drone (actor 26, spawner); chat_01_car (actor 27, spawner); chat_03_car (actor 28, spawner); galena (actor 29, spawnSet); Player (actor 30, findInContext).

Entries: `chat_08_cards_anim_in` → 4; `sheriff_and_mechanic` → 19; `drones_loop_in` → 535; `chat_01_in` → 300; `chat_03_in` → 302; `chat_04_boxing_in` → 304; `chat_05_ramp_anims_in` → 306; `chat_06_vendor_in` → 308; `chat_07_drone_in` → 310; `chat_02_in` → 212.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 19 | 11 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 11 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/20` |
| `scnIKEvent` | 4 | 11 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/14` |
| `scnLookAtEvent` | 34 | 11 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPlaySkAnimEvent` | 18 | 11 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnUnmountEvent` | 2 | 11 / 76 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/19` |
| `scneventsSetAnimFeatureEvent` | 2 | 11 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scneventsSocket` | 9 | 11 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 6
- skeletal_animation: 4
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, gaze: 2
- speech, skeletal_animation, gaze: 1
- speech: 1
- speech, skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `bae278cd8e802f60d2e91689dd22b20863d7ee26c93fabd38469b9613381e9c3`. Binary SHA-256: `e91bae1f26f1f0893df4808bb99a72de7f8fbdbab2cb5ed8b2e290f37d6e61b1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_01b_roadhouse_chats.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_02_fixer.scene`

87 graph nodes, 123 edges; 15 event-bearing sections, 116 events; 34 screenplay lines, 9 screenplay options, 7 choice nodes.

Actors: Fixer (actor 0, spawnDespawn); background_car_driver (actor 1, spawner); nomad_car_01 (actor 2, spawner); Player (actor 3, findInContext).

Entries: `q000_nomad_02_fixer_in` → 1; `SceneSkippedIdleOnly` → 335; `q000_nomad_Gate_in` → 362; `Start 3` → 394; `q000_nomad_02_fixer_gate_in` → 192.

Exits: `q000_nomad_02_fixer_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 28 | 11 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnChangeIdleAnimEvent` | 11 | 29 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnDialogLineEvent` | 23 | 11 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 1 | 48 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/8` |
| `scnIKEvent` | 4 | 29 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/6` |
| `scnPlaySkAnimEvent` | 11 | 29 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnUnmountEvent` | 1 | 48 / 112 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/12` |
| `scneventsAttachPropToPerformer` | 1 | 29 / 84 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scneventsAttachPropToWorld` | 1 | 48 / 108 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 1 | 48 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/11` |
| `scneventsSocket` | 32 | 11 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsVFXEvent` | 2 | 153 / 190 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, audio, socket_signal: 6
- idle_animation: 2
- skeletal_animation, idle_animation, ik, props_equipment, audio, socket_signal: 1
- skeletal_animation, idle_animation, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, audio, vfx: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation: 1

Raw SHA-256: `9a987b271b70eaae3aafdd09d9cef4307e048454ddad8419979081d4fd68f161`. Binary SHA-256: `11c2e70f04f2b58e3d49df8f5f062b8a2d9d186e2dcec36ed9c69ba5dc420da2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_02_fixer.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_03_jackie.scene`

138 graph nodes, 168 edges; 22 event-bearing sections, 221 events; 77 screenplay lines, 14 screenplay options, 5 choice nodes.

Actors: Jackie (actor 0, spawnSet); nomad_car (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `q000_nomad_03_jackie_in` → 1; `q000_nomad_03_jackie_from_failsafe` → 478; `q000_nomad_jackie_startsetu` → 990.

Exits: `q000_nomad_03_jackie_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 24 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |
| `scnChangeIdleAnimEvent` | 23 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 52 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtAdvancedEvent` | 4 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 32 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 37 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/12` |
| `scnPlaySkAnimEvent` | 49 | 3 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPoseCorrectionEvent` | 6 | 3 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsAttachPropToNode` | 3 | 31 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/11` |
| `scneventsAttachPropToPerformer` | 4 | 31 / 151 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 1 | 37 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/3` |
| `scneventsSocket` | 41 | 3 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- gaze: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `3979007b6969e43808d461f58d4a23a26d9ed03ea9135a3ff699309eb5d611f7`. Binary SHA-256: `c8502fc9aca6346bfa035c4193b66120022b874d7c8930102ac3e1071549b591`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_03_jackie.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_04_drive_to_border.scene`

28 graph nodes, 36 edges; 9 event-bearing sections, 49 events; 19 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Jackie (actor 0, spawnSet); vs_car (actor 1, spawnSet); helicopter (actor 2, spawner); Player (actor 3, findInContext).

Entries: `q000_nomad_04_drive_to_border_in` → 1; `HelicopterIdleIn` → 138; `Start 1` → 89.

Exits: `q000_nomad_04_drive_to_border_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 3 | 9 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnDialogLineEvent` | 17 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 139 / 158 | `/Data/RootChunk/sceneGraph/Data/graph/27/Data/events/0` |
| `scnLookAtEvent` | 20 | 3 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 80 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/0` |
| `scnPlaySkAnimEvent` | 3 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 2 | 80 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |
| `scneventsSocket` | 2 | 45 / 95 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 4
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, gaze, socket_signal: 1
- socket_signal, animation_state, mount_workspot: 1
- idle_animation, gameplay_action: 1

Raw SHA-256: `a45bde14fd905e80f00353f416ee26e9808e73853bd57ad339bbfeb70fa08ccf`. Binary SHA-256: `36e085db05ca7cd2a2c82b865997e8941dcd4f22b1dacf5283b86714e63d64f8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_04_drive_to_border.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_05_border_crossing.scene`

329 graph nodes, 393 edges; 60 event-bearing sections, 309 events; 87 screenplay lines, 17 screenplay options, 12 choice nodes.

Actors: Jackie (actor 0, spawnSet); Border_Loadspeaker (actor 1, spawnDespawn); Officer (actor 2, community); Guard (actor 3, community); guard_interior_walking (actor 4, community); guard_guide (actor 5, community); vs_car (actor 6, spawnSet); vs_car_chase (actor 7, spawnSet); Player (actor 8, findInContext).

Entries: `q000_nomad_05_border_crossing_in` → 1; `Start 11` → 1927; `IllegalCrossingWarningIn` → 370; `IllegalCrossingWithJackieIn` → 371; `IllegalCrossingAffterInterrogation` → 379; `q000_questioning_start` → 396; `q000_walk_out` → 518; `Start 8` → 1175; `Start 10` → 1203; `leaning_at_car` → 1904.

Exits: `q000_nomad_05_border_crossing_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 82 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |
| `scnChangeIdleAnimEvent` | 18 | 7 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnDialogLineEvent` | 65 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 511 / 1017 | `/Data/RootChunk/sceneGraph/Data/graph/128/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 249 / 506 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/9` |
| `scnIKEvent` | 8 | 249 / 497 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/1` |
| `scnLookAtEvent` | 46 | 7 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 515 / 1046 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/8` |
| `scnPlaySkAnimEvent` | 48 | 19 / 32 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scnUnmountEvent` | 2 | 249 / 505 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/8` |
| `scneventsAttachPropToNode` | 2 | 539 / 1106 | `/Data/RootChunk/sceneGraph/Data/graph/134/Data/events/9` |
| `scneventsAttachPropToPerformer` | 9 | 21 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/7` |
| `scneventsAttachPropToWorld` | 5 | 82 / 157 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/6` |
| `scneventsCameraParamsEvent` | 2 | 94 / 191 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 11 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 74 | 3 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 1 | 102 / 263 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 16
- gaze: 6
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, gaze, socket_signal: 3
- speech, gaze, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal: 2
- idle_animation, socket_signal: 2
- socket_signal: 2
- speech, socket_signal, animation_state: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- skeletal_animation, ik, camera, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal, gameplay_action: 1
- speech, skeletal_animation, idle_animation, ik, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, props_equipment, audio: 1
- skeletal_animation, props_equipment, audio, socket_signal: 1
- animation_state, mount_workspot: 1
- speech, gaze: 1
- skeletal_animation, socket_signal, animation_state: 1

Raw SHA-256: `696c9b4920183220e91659ce27afe9604d375a4d98a673053b874474624f49c1`. Binary SHA-256: `e5851647338dfa4de9c55aef7606535e8a52bf9a0e6123968419b2f2e597c132`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_05_border_crossing.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_05b_border_chats.scene`

66 graph nodes, 78 edges; 5 event-bearing sections, 37 events; 15 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: traveller_female (actor 0, community); traveller_male (actor 1, community); inspection_guard_01 (actor 2, community); guards_chat_01 (actor 3, community); inspection_guard_02 (actor 4, community); travellers_car (actor 5, spawner); player (actor 6, findInContext).

Entries: `q000_nomad_05b_chats_in` → 1; `ArrestScenePreview` → 222.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 6 | 28 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scnLookAtEvent` | 7 | 28 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnPlaySkAnimEvent` | 10 | 45 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scneventsSocket` | 14 | 45 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2
- speech, gaze: 1
- speech, skeletal_animation, socket_signal: 1
- socket_signal: 1

Raw SHA-256: `d08c4952618f71f043e7fb76e1232680b8d8186b5a37f0927e6009aa09268f32`. Binary SHA-256: `fe2ee0eb061a70a4dfa58c42498bbc3923d522723b6bf824e4ce64feac66312f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_05b_border_chats.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_06_chase.scene`

344 graph nodes, 369 edges; 28 event-bearing sections, 108 events; 42 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: Jackie (actor 0, spawnSet); Arasaka_Security (actor 1, community); vs_car (actor 2, spawnSet); ArasakaCar01 (actor 3, spawner); ArasakaCar02 (actor 4, spawner); ArasakaCar03 (actor 5, spawner); Player (actor 6, findInContext).

Entries: `q000_nomad_06_chase_in` → 1; `old_lines` → 567; `Start 2` → 1269; `Start 3` → 1296.

Exits: `q000_nomad_06_chase_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 695 / 456 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/6` |
| `scnChangeIdleAnimEvent` | 6 | 3 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 37 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnLookAtEvent` | 28 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 3 | 1280 / 1323 | `/Data/RootChunk/sceneGraph/Data/graph/219/Data/events/7` |
| `scnPlaySkAnimEvent` | 8 | 291 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 695 / 438 | `/Data/RootChunk/sceneGraph/Data/graph/75/Data/events/0` |
| `scneventsSocket` | 20 | 3 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 11
- speech, socket_signal: 4
- speech, idle_animation, gaze, socket_signal: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, gaze, socket_signal: 2
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, animation_state, mount_workspot: 1
- animation_state, mount_workspot: 1

Raw SHA-256: `6cff847dd6ff27709a74fbde2da4422e3ad7b59c7f1b32fae53273b671e62bf3`. Binary SHA-256: `9577de8413fde4f3c5d06e0e26d874de291440efaa8422cf0695faf4a70d8a04`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_06_chase.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_nomad_07_hideout.scene`

183 graph nodes, 230 edges; 40 event-bearing sections, 362 events; 82 screenplay lines, 18 screenplay options, 12 choice nodes.

Actors: Jackie (actor 0, spawnSet); galena (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `q000_nomad_07_hideout_in` → 1; `Start 5` → 888; `Start 3` → 762; `FAKE INPUT LOCO` → 1062; `q000_nomad_07_hideout_test_only_in` → 627; `Start 4` → 780; `Start 6` → 931; `Start 7` → 936; `Start 1` → 543; `Start 2` → 561.

Exits: `q000_nomad_07_hideout_out` → 2; `MontagePreloadOut` → 1159.

End nodes: 2: `<omitted>`; 1159: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 9 | 10 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scnChangeIdleAnimEvent` | 40 | 10 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnDialogLineEvent` | 68 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayActionEvent` | 3 | 276 / 418 | `/Data/RootChunk/sceneGraph/Data/graph/36/Data/events/5` |
| `scnGameplayTransitionEvent` | 1 | 692 / 866 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/6` |
| `scnIKEvent` | 4 | 301 / 489 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/5` |
| `scnLookAtEvent` | 70 | 10 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 2 | 483 / 665 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/0` |
| `scnPlaySkAnimEvent` | 78 | 10 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnPoseCorrectionEvent` | 1 | 281 / 457 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/5` |
| `scnUnmountEvent` | 1 | 692 / 870 | `/Data/RootChunk/sceneGraph/Data/graph/91/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 4 | 483 / 666 | `/Data/RootChunk/sceneGraph/Data/graph/59/Data/events/1` |
| `scneventsSocket` | 78 | 10 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsVFXEvent` | 3 | 10 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/14` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- speech, skeletal_animation, gaze, socket_signal: 6
- gaze: 4
- speech: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal, gameplay_action: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, ik, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio, socket_signal: 1
- skeletal_animation, idle_animation: 1
- animation_state, mount_workspot: 1
- idle_animation: 1
- skeletal_animation, idle_animation, vfx, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot, gameplay_action: 1
- skeletal_animation, idle_animation, socket_signal: 1
- speech, socket_signal: 1

Raw SHA-256: `cc6b544241043c5175c8c7a816dd9a317ed08ac57c0d6103ddcc497497781f07`. Binary SHA-256: `51bdf2c489882a73ecaac4066b8a91cb113b19c36e2936af5b25db8a16e89011`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_nomad_07_hideout.scene" --events
```

## `base\quest\main_quests\prologue\q000\scenes\q000_vr_tutorial.scene`

827 graph nodes, 876 edges; 92 event-bearing sections, 289 events; 124 screenplay lines, 27 screenplay options, 15 choice nodes.

Actors: Jackie (actor 0, spawnSet); Sarge (actor 1, spawnSet); TBugVoice (actor 2, spawnDespawn); replacer (actor 3, spawnSet); TBug (actor 4, spawnDespawn); archer_hella (actor 5, spawnSet); Player (actor 6, findInContext).

Entries: `START_TUTORIAL` → 1; `13_04_2020_NEW` → 1636; `replay_selection` → 10668; `q000_vr_tutorial_lobby_in` → 62; `q000_vr_start_course_selection` → 112; `Course1EnemyTaggedIn` → 932; `Course1EnemyTagIn` → 935; `Course1CoverIn` → 938; `Course1InCoverIn` → 943; `Course1GuardDoneIn` → 946; `Course1OnCameraIn` → 949; `Course2TargetsRound1DoneIn` → 952; `Course2Stage2HealIn` → 956; `Course2Stage2TakeCoverIn` → 962; `Course2Stage3StartWhenReadyIn` → 965; `Course2ShootTargetsIn` → 968; `Course3StartHackingIn` → 971; `Course3DistractionTriggeredIn` → 976; `Course3TakedownIn` → 979; `Course3AfterTakedownIn` → 982; `Course3EnvTakedownIn` → 985; `Course3Stage02WaitForWindowIn` → 988; `Course3Stage02TriggerGranadeIn` → 991; `Course3NPCAsDistractIn` → 994; `Course04AfterSkullIn` → 997; `q000_vr_after_tutorials_in` → 200; `Course01Exit` → 222; `Course1IntroIn` → 224; `Course2IntroIn` → 233; `Course3IntroIn` → 241; `Course4IntroIn` → 249; `Course1OutroIn` → 257; `Course2OutroIn` → 262; `Course3OutroIn` → 268; `Course4OutroIn` → 273; `CourseRemindersTbugIn` → 1256; `CourseFailedIn` → 441; `CourseTVScreenHacked` → 1261; `OLD` → 1396; `replay_start` → 10447; `Course2Stage2In` → 656; `Course2Stage3In` → 659; `Course3Stage2In` → 672; `Course4Stage2In` → 677; `Course4Stage3In` → 680; `Course02Exit` → 687; `Course03Exit` → 688; `Course4Stage2PlayerBlockingIn` → 1506; `Course04Exit` → 689; `Course4Stage2BlockAttackIn` → 1509; `Course4Stage2DodgeIn` → 1512; `Course4Stage2FullFight` → 1515; `Course4Stage2NPCBlockingIn` → 1518; `vr_replay_teleport` → 10519; `ScenePrev` → 1542.

Exits: `q000_vr_tutorial_start_tutorial_out` → 2; `enable_replay_selection` → 10645; `END_TUTORIAL` → 30; `gyro_End1` → 10670; `gyro_End2` → 10688; `gyor_End3` → 10690; `gyro_End4` → 10692; `End5` → 10698; `StartCourse01` → 113; `Course2TargetsRound1DoneOut` → 9946; `StartCourse02` → 152; `StartCourse03` → 154; `StartCourse04` → 156; `q000_vr_start_course_off` → 177; `EnableTutorialSelection` → 179; `Course04AfterSkullOut` → 999; `q000_vr_tutorial_lobby_exited` → 203; `CourseTVScreenHackedOut` → 1866; `Course3DistractionTriggeredOut` → 1868; `Course3TakedownOut` → 1870; `Course1OutroOut` → 260; `Course2OutroOut` → 264; `Course3OutroOut` → 270; `Course4OutroOut` → 275; `replay_tp_out_repeat` → 11017; `replay_tp_out_first` → 11020; `End6` → 11050; `CourseFailedOut` → 454; `Course3AfterTakedownOut` → 1410; `shard_out` → 10484; `CourseQuitOut` → 696; `Course4Stage3Out` → 1536; `SpawnReanimator` → 9737; `finish_replay` → 10602.

End nodes: 2: `<omitted>`; 30: `<omitted>`; 113: `NonTerminating`; 152: `NonTerminating`; 154: `NonTerminating`; 156: `NonTerminating`; 177: `<omitted>`; 179: `NonTerminating`; 203: `<omitted>`; 260: `<omitted>`; 264: `<omitted>`; 270: `<omitted>`; 275: `<omitted>`; 454: `NonTerminating`; 696: `<omitted>`; 999: `<omitted>`; 1410: `NonTerminating`; 1536: `<omitted>`; 1866: `<omitted>`; 1868: `<omitted>`; 1870: `<omitted>`; 9737: `NonTerminating`; 9946: `<omitted>`; 10484: `<omitted>`; 10602: `<omitted>`; 10645: `NonTerminating`; 10670: `NonTerminating`; 10688: `NonTerminating`; 10690: `NonTerminating`; 10692: `NonTerminating`; 10698: `<omitted>`; 11017: `NonTerminating`; 11020: `NonTerminating`; 11050: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 22 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/6` |
| `scnChangeIdleAnimEvent` | 13 | 15 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scnDialogLineEvent` | 105 | 15 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnGameplayTransitionEvent` | 3 | 1023 / 1413 | `/Data/RootChunk/sceneGraph/Data/graph/260/Data/events/20` |
| `scnIKEvent` | 6 | 1023 / 1403 | `/Data/RootChunk/sceneGraph/Data/graph/260/Data/events/11` |
| `scnLookAtEvent` | 29 | 15 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnPlaySkAnimEvent` | 51 | 15 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnUnmountEvent` | 3 | 1023 / 1412 | `/Data/RootChunk/sceneGraph/Data/graph/260/Data/events/19` |
| `scneventsAttachPropToNode` | 3 | 22 / 77 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/13` |
| `scneventsAttachPropToPerformer` | 6 | 15 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/20` |
| `scneventsCameraParamsEvent` | 1 | 2864 / 3072 | `/Data/RootChunk/sceneGraph/Data/graph/525/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 13 | 15 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 50 | 15 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 54
- speech, skeletal_animation: 8
- speech, socket_signal: 6
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 3
- socket_signal: 3
- gaze: 3
- speech, skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1
- camera: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal: 1

Raw SHA-256: `d24c7929cb29d347fe1f9cf4c878c4d548eb46d6ba6ab406847242783934c93e`. Binary SHA-256: `4637abe5b071c9643d071a11b846fc4034520e7117342ea404d91da213b2a62e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q000\scenes\q000_vr_tutorial.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00a_before_mission.scene`

182 graph nodes, 257 edges; 28 event-bearing sections, 132 events; 43 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: tbug (actor 0, findInContext); jackie (actor 1, spawnSet); old_lady (actor 2, community); tbug_holo (actor 3, spawnSet); v (actor 4, findInContext).

Entries: `q001_bef_mission_in` → 1; `q001_jackie_elevator_in` → 1817; `TEST` → 2429; `Q001_digital_sickness` → 2163; `backup_lines` → 1764; `backup_lines2` → 1766; `backup_lines3` → 1768.

Exits: `q001_bef_mission_out` → 6; `q001_jackie_elevator_out` → 1824; `Q001_digital_sickness_kill` → 2212.

End nodes: 6: `NonTerminating`; 1824: `NonTerminating`; 2212: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 10 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/6` |
| `scnChangeIdleAnimEvent` | 6 | 147 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnDialogLineEvent` | 18 | 2 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 10 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/16` |
| `scnIKEvent` | 2 | 10 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnLookAtEvent` | 32 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 31 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 1 | 10 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 1 | 10 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/12` |
| `scneventsSocket` | 24 | 4 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 11 | 10 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- skeletal_animation: 4
- skeletal_animation, gaze: 4
- vfx: 3
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, socket_signal: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal: 1
- gaze: 1

Raw SHA-256: `4f15d3f5bb90c117d6b544d349eedcf183220092a1c401f7d29394583ca82da5`. Binary SHA-256: `11d27d0fe59bdbd76ea0d5ccfa23ab1d9cc877b7866999d350c91382df5e6e3c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00a_before_mission.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00aa_jackie_hide_body_tutorial.scene`

60 graph nodes, 69 edges; 10 event-bearing sections, 36 events; 18 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: jackie (actor 0, spawnSet); tbug (actor 1, findInContext); scavenger_takedown (actor 2, community); Player (actor 3, findInContext).

Entries: `disposal_tutorial` → 1; `room_04` → 8; `takedown_tutorial` → 14; `takedown_npc_work` → 139; `dialogue_tutorial` → 18; `Start 6` → 222; `finished_talking` → 41; `hide_body_2_in` → 109.

Exits: `takedown` → 72; `disposal` → 77; `finished_talking_out` → 96; `End 2` → 37; `dialogue_tutorial_end` → 100; `room_04_end` → 103; `hide_body_2_out` → 110.

End nodes: 37: `<omitted>`; 72: `<omitted>`; 77: `<omitted>`; 96: `<omitted>`; 100: `<omitted>`; 103: `<omitted>`; 110: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 15 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnChangeIdleAnimEvent` | 3 | 15 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |
| `scnDialogLineEvent` | 12 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 15 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/16` |
| `scnIKEvent` | 2 | 15 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/9` |
| `scnLookAtEvent` | 2 | 15 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 4 | 15 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnUnmountEvent` | 1 | 15 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/15` |
| `scneventsSetAnimFeatureEvent` | 1 | 15 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/12` |
| `scneventsSocket` | 9 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- socket_signal: 1
- skeletal_animation, socket_signal: 1
- idle_animation: 1

Raw SHA-256: `337bb1c8c076fe2ab11bd1f7971bd531bc9ae7d84268289ace60917ce6136d1e`. Binary SHA-256: `bf2ccb2288911c0d5d9768cc93ebd779712b7f278783f37e479e2215abbbf41c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00aa_jackie_hide_body_tutorial.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00ab_jackie_double_takedown.scene`

26 graph nodes, 23 edges; 6 event-bearing sections, 11 events; 11 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: jackie (actor 0, spawnSet); tbug (actor 1, findInContext); scav_7_wheelchair (actor 2, community); scav_5_following_wheelchair (actor 3, community); Player (actor 4, findInContext).

Entries: `initiate_takedown` → 1; `jackie_stealth` → 31; `after_takedown` → 8; `wheelchair_accident` → 38; `jackie_another_one` → 43; `tbug_stealth` → 26.

Exits: `jackie_another_one_end` → 54; `tbug_stealth_end` → 28; `jackie_stealth_end` → 33; `after_takedown_out` → 9; `wheelchair_accident_end` → 41; `initiate_takedown_end` → 52.

End nodes: 9: `<omitted>`; 28: `<omitted>`; 33: `<omitted>`; 41: `<omitted>`; 52: `<omitted>`; 54: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 11 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6

Raw SHA-256: `d295a6ac0579b3970a088e184261971351aad52ab4ffcb6d2e81ce6a5c0244c3`. Binary SHA-256: `0c5a84b81977c3c3586128eb20a12356e901ed93c1cd1a203e35fdba3f570ff9`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00ab_jackie_double_takedown.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00b_dead_girl.scene`

96 graph nodes, 143 edges; 10 event-bearing sections, 45 events; 12 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: tbug (actor 0, findInContext); jackie (actor 1, spawnSet); v (actor 2, findInContext).

Entries: `Start 8` → 711; `q001_dead_girl_in` → 59; `Start_bakap` → 739; `q001_came_back_in` → 640; `not_her_in` → 649.

Exits: `q001_dead_girl_out` → 60; `not_her_out` → 651.

End nodes: 60: `NonTerminating`; 651: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 812 / 267 | `/Data/RootChunk/sceneGraph/Data/graph/49/Data/events/1` |
| `scnDialogLineEvent` | 8 | 61 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 824 / 294 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/8` |
| `scnIKEvent` | 2 | 824 / 286 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/1` |
| `scnLookAtEvent` | 18 | 77 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnPlaySkAnimEvent` | 5 | 77 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/3` |
| `scnUnmountEvent` | 1 | 824 / 293 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/7` |
| `scneventsSetAnimFeatureEvent` | 1 | 824 / 291 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/6` |
| `scneventsSocket` | 7 | 82 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, skeletal_animation, gaze: 2
- speech, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `11b3e3c625d30bce3cf7052e1f60c73f5d19d13d57d2e9e436ef93125afe4aed`. Binary SHA-256: `f036221cbde19d8f863600dba85984f766ba0022bb7312c41ea9049b4187055f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00b_dead_girl.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00b_shooting.scene`

22 graph nodes, 30 edges; 7 event-bearing sections, 7 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: jackie (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `q001_scav_chase_in` → 66; `q001_jackie_battlecries_in` → 11.

Exits: `q001_scav_chase_out` → 67; `q001_jackie_battlecries_out` → 34.

End nodes: 34: `<omitted>`; 67: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 7 | 16 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7

Raw SHA-256: `745352cbd1331559dd51fbf0be9661edd1db8dbee5fb1200f536217467847fbd`. Binary SHA-256: `b0db2481585d61bb475f5973be9fb9d6021a872987c79dd996ae7ed5f44598a1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00b_shooting.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00b_tbug_reminder_secure_the_area.scene`

6 graph nodes, 4 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: tbug (actor 0, findInContext); Player (actor 1, findInContext).

Entries: `first_reminder_in` → 1; `second_reminder_in` → 8.

Exits: `first_reminder_out` → 2; `second_reminder_out` → 10.

End nodes: 2: `<omitted>`; 10: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `57a0f819c3ad5c10520a64d51c02b8de77862424797e3e9020044cd84a9c264e`. Binary SHA-256: `ed3aa8eea015c3466b18a4eda4370c120cf18bc970424abfc230ed7f1f1c44e1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00b_tbug_reminder_secure_the_area.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00c_rescuing_girl.scene`

294 graph nodes, 414 edges; 50 event-bearing sections, 579 events; 64 screenplay lines, 9 screenplay options, 9 choice nodes.

Actors: sandra_dorcet (actor 0, community); jackie (actor 1, spawnSet); tbug (actor 2, spawnDespawn); tt_soldier1 (actor 3, community); tt_soldier2 (actor 4, community); tt_medic1 (actor 5, community); tt_medic2 (actor 6, community); dead_man (actor 7, community); biomonitor (actor 8, spawnDespawn); av_speaker (actor 9, spawnDespawn); AV (actor 10, community); v (actor 11, findInContext).

Entries: `q001_get_girl_in` → 1; `q001_trauma_arrives_in` → 6; `Start 14` → 2350; `TEST` → 2351; `jackie_scav_flee_in` → 1904; `Reminder_jackie_after_boss` → 3433; `Jackie_balcony_lookat` → 2863; `q003_jackie_reaction_scavengers_van_in` → 1421; `Start 18` → 3466; `q001_jackie_comment_in` → 567.

Exits: `TO_Q001_DIGITAL_SICKNESS` → 2623; `q001_get_girl_out` → 4; `q001_trauma_arrives_out` → 13; `End_terminado` → 1765; `q001_jackie_came_out` → 1958; `q003_jackie_reaction_scavengers_van_out` → 1422; `q001_jackie_comment_out` → 568.

End nodes: 4: `NonTerminating`; 13: `NonTerminating`; 568: `<omitted>`; 1422: `NonTerminating`; 1765: `<omitted>`; 1958: `<omitted>`; 2623: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 79 | 2 / 29 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scnChangeIdleAnimEvent` | 26 | 2 / 24 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnDialogLineEvent` | 57 | 2 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/13` |
| `scnGameplayTransitionEvent` | 3 | 307 / 504 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/45` |
| `scnIKEvent` | 6 | 307 / 491 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/36` |
| `scnLookAtAdvancedEvent` | 11 | 738 / 701 | `/Data/RootChunk/sceneGraph/Data/graph/29/Data/events/16` |
| `scnLookAtEvent` | 64 | 2 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/21` |
| `scnPlaySkAnimEvent` | 160 | 2 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 3 | 307 / 506 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/47` |
| `scneventsAttachPropToNode` | 2 | 307 / 499 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/41` |
| `scneventsAttachPropToPerformer` | 2 | 1947 / 1200 | `/Data/RootChunk/sceneGraph/Data/graph/106/Data/events/4` |
| `scneventsAttachPropToWorld` | 2 | 110 / 173 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/60` |
| `scneventsCameraParamsEvent` | 4 | 297 / 421 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/9` |
| `scneventsMountEvent` | 2 | 307 / 507 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/48` |
| `scneventsRagdollEvent` | 1 | 110 / 128 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/23` |
| `scneventsSetAnimFeatureEvent` | 11 | 110 / 86 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scneventsSetAnimsetWeight` | 18 | 110 / 127 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/22` |
| `scneventsSocket` | 85 | 2 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsVFXDurationEvent` | 1 | 2 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/15` |
| `scneventsVFXEvent` | 42 | 2 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 7
- skeletal_animation, gaze, socket_signal: 6
- skeletal_animation: 4
- gaze: 4
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 3
- speech, gaze: 3
- camera: 3
- speech, skeletal_animation, idle_animation, audio, socket_signal: 2
- speech, skeletal_animation, gaze, audio, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- idle_animation: 2
- skeletal_animation, idle_animation: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state, gameplay_action: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal: 1
- speech, idle_animation: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, audio: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `650f777b34a94b8fa37cdfc6bc2054ab23d7e54590c88a7f9fc93ef4ff2038ba`. Binary SHA-256: `2ada0c29414034db08bd2705d13e21162af59efd56d712544aba35135d8ca896`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00c_rescuing_girl.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00cd_boss_clean.scene`

52 graph nodes, 49 edges; 6 event-bearing sections, 48 events; 11 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: jackie (actor 0, spawnSet); tbug (actor 1, findInContext); boss (actor 2, community); Player (actor 3, findInContext).

Entries: `boss_hidden` → 49; `room_clean` → 52; `jackie_through_wall_in` → 64; `after_him` → 27; `jackie_no_terminado` → 185.

Exits: `jackie_through_wall_out` → 251; `room_clean_end` → 55; `after_him_end` → 58; `boss_hidden_out` → 95.

End nodes: 55: `<omitted>`; 58: `<omitted>`; 95: `<omitted>`; 251: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 8 | 31 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 9 | 26 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 102 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/7` |
| `scnIKEvent` | 2 | 102 / 155 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/1` |
| `scnLookAtEvent` | 3 | 66 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/18` |
| `scnPlaySkAnimEvent` | 4 | 66 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnPlayVideoEvent` | 2 | 31 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 1 | 102 / 161 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/6` |
| `scneventsAttachPropToWorld` | 1 | 66 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 1 | 102 / 159 | `/Data/RootChunk/sceneGraph/Data/graph/25/Data/events/5` |
| `scneventsSocket` | 11 | 31 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/7` |
| `scneventsVFXEvent` | 5 | 66 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, audio, socket_signal, video: 1
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `0977818b635eb0edee810b1d69d0af7659a3d928fc9cea3a5bfcb39ca340b29c`. Binary SHA-256: `88c9e8e5db7402729c08d0c56c3807bdedb987ce79b2a8c04a3390ff8432b56f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00cd_boss_clean.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00d_leaving.scene`

298 graph nodes, 338 edges; 31 event-bearing sections, 109 events; 58 screenplay lines, 9 screenplay options, 3 choice nodes.

Actors: jackie (actor 0, spawnSet); tbug (actor 1, findInContext); V_tpp (actor 2, findInWorld); dex (actor 3, findInContext); wakako (actor 4, spawnSet); car_player (actor 5, spawnSet); v (actor 6, findInContext).

Entries: `q001_after_tt_left_in` → 335; `NCW_GUNS` → 3935; `NCW_GUNS_RECORDING` → 3951; `Start 8` → 1353; `Start 2` → 831.

Exits: `q001_after_tt_left_out` → 373.

End nodes: 373: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 903 / 453 | `/Data/RootChunk/sceneGraph/Data/graph/84/Data/events/2` |
| `scnChangeIdleAnimEvent` | 4 | 516 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/0` |
| `scnDialogLineEvent` | 24 | 425 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 516 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/11` |
| `scnIKEvent` | 8 | 516 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/5` |
| `scnLookAtEvent` | 34 | 516 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/1` |
| `scnPlaySkAnimEvent` | 13 | 516 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/4` |
| `scnUnmountEvent` | 2 | 516 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 4 | 516 / 60 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/7` |
| `scneventsSocket` | 17 | 516 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/13/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 7
- skeletal_animation, gaze: 4
- speech: 3
- skeletal_animation, gaze, socket_signal: 3
- gaze: 3
- speech, idle_animation, gaze: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze, socket_signal: 1
- speech, idle_animation: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- gaze, socket_signal: 1
- socket_signal: 1
- gaze, ik, socket_signal, animation_state: 1

Raw SHA-256: `3d8f0ff26a22c4a9578767b55dbfd24372fa47538f9d0b29c95dbdf26c7e5744`. Binary SHA-256: `e05ee7f19f1ba3249ed998052019835d95090170d82d6673ade8d28c7909fc30`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00d_leaving.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00e_scavenger_conversation.scene`

56 graph nodes, 125 edges; 7 event-bearing sections, 22 events; 12 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: scav5 (actor 0, community); scav2 (actor 1, community); scav7 (actor 2, community); wheelchair (actor 3, community); dead_body (actor 4, community).

Entries: `q001_freezer_in` → 1; `q001_wheelchair_in` → 6.

Exits: `q001_freezer_out` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 8 | 83 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/0` |
| `scnDialogLineEvent` | 6 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 5 | 57 / 91 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/0` |
| `scneventsSocket` | 3 | 78 / 105 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 2
- idle_animation: 2
- speech: 1
- skeletal_animation: 1
- idle_animation, socket_signal: 1

Raw SHA-256: `fe1ca5cc5b09a93711400a782c12203cd8d966f8459cf84c8250b052d79d5177`. Binary SHA-256: `04dd5d20931a498df80d38ff472ded625fa2618ce6a9f7f7a20554a29615400c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00e_scavenger_conversation.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00f_ride_with_jackie.scene`

210 graph nodes, 224 edges; 32 event-bearing sections, 244 events; 64 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: jackie (actor 0, spawnSet); police1 (actor 1, community); police2 (actor 2, community); pedestrian_01 (actor 3, community); pedestrian_02 (actor 4, community); scav_driver (actor 5, community); player_car (actor 6, spawnSet); police_car1 (actor 7, community); police_car2 (actor 8, community); Player (actor 9, findInContext).

Entries: `Start 7` → 650; `aft_blockade_in` → 1713; `scavs_chat_to_mb_01_in` → 33; `blockade_in` → 38; `scavs_car_appears_in` → 102; `scavs_intersection_in` → 112; `blackade_jackie_stops` → 326; `scavs_jackie_improvises_in` → 117; `scavs_pedestrians_in` → 122; `scavs_ramming_in` → 127; `scavs_chase_over_in` → 132; `OLD` → 349; `scavs_crash_in` → 138; `Start 8` → 774; `scavs_chat_to_mb_02_in` → 143.

Exits: `scavs_chat_to_mb_01_out` → 34; `arrived_mb_out` → 39; `scavs_car_appears_out` → 103; `scavs_intersection_out` → 113; `scavs_jackie_improvises_out` → 118; `scavs_pedestrians_out` → 123; `scavs_ramming_out` → 128; `scavs_chase_over_out` → 133; `scavs_crash_out` → 139; `scavs_chat_to_mb_02_out` → 144.

End nodes: 34: `<omitted>`; 39: `NonTerminating`; 103: `<omitted>`; 113: `<omitted>`; 118: `<omitted>`; 123: `<omitted>`; 128: `<omitted>`; 133: `<omitted>`; 139: `<omitted>`; 144: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 59 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/11` |
| `scnChangeIdleAnimEvent` | 12 | 35 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnDialogLineEvent` | 55 | 35 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/8` |
| `scnGameplayTransitionEvent` | 3 | 40 / 75 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/15` |
| `scnIKEvent` | 20 | 35 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnLookAtAdvancedEvent` | 1 | 44 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnLookAtEvent` | 54 | 35 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/10` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 325 / 403 | `/Data/RootChunk/sceneGraph/Data/graph/55/Data/events/3` |
| `scnPlaySkAnimEvent` | 42 | 35 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPoseCorrectionEvent` | 4 | 44 / 89 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/6` |
| `scnUnmountEvent` | 3 | 40 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/14` |
| `scneventsSetAnimFeatureEvent` | 11 | 35 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 33 | 35 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 3 | 694 / 789 | `/Data/RootChunk/sceneGraph/Data/graph/123/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, socket_signal, animation_state: 1
- speech, idle_animation, socket_signal: 1
- skeletal_animation, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, vfx, socket_signal, animation_state: 1
- animation_state: 1
- gaze: 1
- vfx: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `5f1402d5a15686f599d4c1ed863da022e0bfbe838496ad2484dc2c2b516af22e`. Binary SHA-256: `1527da5af1765a74be20b0cd04fd1a4709d777b382380b130976ff3907b08536`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00f_ride_with_jackie.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00ff_max_tac.scene`

45 graph nodes, 80 edges; 6 event-bearing sections, 105 events; 15 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: jackie (actor 0, spawnSet); bandit_big (actor 1, community); bandit_male (actor 2, community); bandit_fem (actor 3, community); maxtac_fem (actor 4, community); maxtac_big (actor 5, community); victim (actor 6, community); av (actor 7, community); cortes (actor 8, community); hella (actor 9, spawnSet); Player (actor 10, findInContext).

Entries: `Start 0` → 1; `for_preeview` → 95; `MERCS for export` → 26.

Exits: `End 1` → 22.

End nodes: 22: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 4 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/9` |
| `scnDialogLineEvent` | 14 | 4 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/8` |
| `scnIKEvent` | 6 | 4 / 40 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/11` |
| `scnPlayDefaultMountedSlotWorkspotEvent` | 1 | 96 / 271 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/3` |
| `scnPlaySkAnimEvent` | 21 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 4 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/13` |
| `scneventsSocket` | 44 | 4 / 51 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/16` |
| `scneventsVFXEvent` | 13 | 4 / 52 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/17` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, ik, socket_signal, animation_state: 2
- speech, skeletal_animation, ik, audio, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation: 1
- speech: 1
- socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `93c3663219c935e103853370a1c15182bb07880afca7650f1a9923eb1e1fe257`. Binary SHA-256: `91625b91dea63e444235d62cf89983564308e06b539780a9d2dfc274a75414fd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00ff_max_tac.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_00g_broken_gate.scene`

19 graph nodes, 18 edges; 4 event-bearing sections, 51 events; 6 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: mb_resident1 (actor 0, community); mb_resident2 (actor 1, community).

Entries: `gate_broken_in` → 1.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scnDialogLineEvent` | 3 | 4 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/5` |
| `scnGameplayTransitionEvent` | 3 | 4 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/23` |
| `scnIKEvent` | 6 | 4 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/14` |
| `scnLookAtEvent` | 4 | 4 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |
| `scnPlaySkAnimEvent` | 10 | 4 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnUnmountEvent` | 3 | 4 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/22` |
| `scneventsEquipItemToPerformer` | 2 | 7 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 3 | 4 / 46 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/20` |
| `scneventsSocket` | 14 | 4 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 1 | 7 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `6d1eb51c4d96c3451b831e64fc1297d7f675ec560f316b5fbf34d63e12a9a2fc`. Binary SHA-256: `ad1a1831b1244b67eeb31219a6fe67f13faa28b2a28b8101467a4bd68cd8cf5f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_00g_broken_gate.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_01_wakeup.scene`

65 graph nodes, 66 edges; 9 event-bearing sections, 40 events; 22 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: stanley (actor 0, spawner); jackie (actor 1, spawnSet); v (actor 2, findInContext).

Entries: `q001_wakeup_in` → 0; `Start 8` → 885; `go_to_sleep_in` → 712; `wakeup_logo_bik` → 258; `Start 9` → 926.

Exits: `q001_wakeup_out` → 4; `go_to_sleep_out` → 717.

End nodes: 4: `<omitted>`; 717: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 726 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/1` |
| `scnDialogLineEvent` | 15 | 620 / 69 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnLookAtEvent` | 1 | 620 / 72 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |
| `scnPlaySkAnimEvent` | 2 | 726 / 113 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/0` |
| `scneventsSocket` | 7 | 620 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scneventsVFXEvent` | 11 | 620 / 71 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- skeletal_animation, audio, vfx, socket_signal: 2
- speech, gaze, vfx, socket_signal: 1
- speech, vfx, socket_signal: 1
- speech, vfx: 1

Raw SHA-256: `32f72724274f6b53acd018444c783a9cdc45dd072d27aad06a92ad0cf3ee4928`. Binary SHA-256: `a38f2e8894a9f4acb92c8d3ac5e42ec9fbd1bedcbf5b0f7b99f58d82b02ba1e1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_01_wakeup.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_01aa_epilog_house_av.scene`

15 graph nodes, 15 edges; 0 event-bearing sections, 0 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: woman (actor 0, community); av (actor 1, community).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |

Presentation families coexisting in an event section (counts are sections, not durations):


Raw SHA-256: `bb2f1ef647f5ff252569f998814e7e33004967c6c1991ce8370c84bf96f1cc06`. Binary SHA-256: `e11c75691352e8d5a83912bb40d9ebe6ae8998918a3ed13e5b50c5e4b1616a0b`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_01aa_epilog_house_av.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_05_tbug_netrunner_tut.scene`

12 graph nodes, 11 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: tbug (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 26 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `1fb1d977b220e939604a8902aa10ac7b19ed7033347e64f8f58eb32f5a58a900`. Binary SHA-256: `0691a31a3994e2874ac2a19df96412186916cda46ef962f49035932947478534`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_05_tbug_netrunner_tut.scene" --events
```

## `base\quest\side_quests\sq024\scenes\sq024_05b_trauma_team.scene`

250 graph nodes, 295 edges; 35 event-bearing sections, 365 events; 77 screenplay lines, 7 screenplay options, 5 choice nodes.

Actors: claire (actor 0, spawnSet); sampson (actor 1, spawnSet); sampson_gunner (actor 2, spawnSet); crash_car_driver (actor 3, spawner); crowd_driver_front (actor 4, spawner); crowd_driver_right_0 (actor 5, spawner); crowd_driver_right_1 (actor 6, spawner); crowd_driver_back (actor 7, spawner); crowd_driver_left_0 (actor 8, spawner); crowd_driver_left_1 (actor 9, spawner); crowd_helper_0 (actor 10, spawner); crowd_helper_1 (actor 11, spawner); crowd_bystander_0 (actor 12, spawner); crowd_bystander_1 (actor 13, spawner); crowd_bystander_2 (actor 14, spawner); crowd_bystander_3 (actor 15, spawner); crowd_bystander_4 (actor 16, spawner); crowd_bystander_5 (actor 17, spawner); sq024_05b_sampson_car (actor 18, spawnSet); sq024_05b_crash_car (actor 19, spawner); crowd_car_front (actor 20, spawner); crowd_car_right_0 (actor 21, spawner); crowd_car_right_1 (actor 22, spawner); crowd_car_back (actor 23, spawner); crowd_car_left_0 (actor 24, spawner); crowd_car_left_1 (actor 25, spawner); claire_car (actor 26, community); v (actor 27, findInContext).

Entries: `sq024_05b_tt_in` → 1; `q000_car_reuse` → 1233; `claire_kills` → 1161; `scene_pass_claire_spares` → 1170; `claire_kills_no_choice` → 1193.

Exits: `sq024_05b_sampson_dead_out` → 2; `q000_hijack_end` → 1236; `check_player_left` → 553.

End nodes: 2: `<omitted>`; 553: `NonTerminating`; 1236: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 506 / 514 | `/Data/RootChunk/sceneGraph/Data/graph/35/Data/events/5` |
| `scnChangeIdleAnimEvent` | 14 | 140 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 60 | 116 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 9 | 212 / 150 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/24` |
| `scnIKEvent` | 18 | 212 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |
| `scnLookAtEvent` | 76 | 206 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnPlaySkAnimEvent` | 70 | 206 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scnUnmountEvent` | 9 | 212 / 149 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/23` |
| `scneventsSetAnimFeatureEvent` | 9 | 212 / 144 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/19` |
| `scneventsSocket` | 94 | 140 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scneventsVFXEvent` | 4 | 212 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/11` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation, socket_signal: 8
- speech: 4
- speech, skeletal_animation, gaze, socket_signal: 4
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- skeletal_animation, gaze, socket_signal: 2
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, ik, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation, socket_signal: 1

Raw SHA-256: `565881eae525b90a9ec57983daf0ccc7135128f47a598b8c9685ab4484a601da`. Binary SHA-256: `9b5a455f8025a4bed7df122e700efe45c430ffef5562b39771acc8a568f11dd4`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq024\scenes\sq024_05b_trauma_team.scene" --events
```

