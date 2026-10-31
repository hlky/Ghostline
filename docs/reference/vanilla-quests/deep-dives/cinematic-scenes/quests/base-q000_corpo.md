# The Corpo-Rat: scene presentation

Journal identity: `quests/main_quest/prologue/q000_corpo`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q000_corpo.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

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

