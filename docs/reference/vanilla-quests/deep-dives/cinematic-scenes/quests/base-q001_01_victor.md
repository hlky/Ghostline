# The Ripperdoc: scene presentation

Journal identity: `quests/main_quest/prologue/q001_01_victor`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q001_01_victor.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\wat_lch_gunsmith_01.scene`

107 graph nodes, 120 edges; 14 event-bearing sections, 42 events; 22 screenplay lines, 9 screenplay options, 5 choice nodes.

Actors: wilson (actor 0, spawnSet); v (actor 1, findInContext).

Entries: `wilson_default_in` → 0; `backup_lines` → 568.

Exits: .

End nodes: . Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 44 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 22 | 44 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnLookAtEvent` | 8 | 44 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 6 | 44 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsSocket` | 5 | 44 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, gaze: 4
- speech, skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1

Raw SHA-256: `230b4f7f142e3145266591392f5b305e6d0738c1736f652a886102504730a945`. Binary SHA-256: `a8cbd1b193cb051f42c300b28fd2cb6034daded9ba5a769a31563040c2abcd43`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\vendors\watson\little_china\wat_lch_gunsmith_01\wat_lch_gunsmith_01.scene" --events
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

## `base\quest\main_quests\prologue\q001\scenes\q001_03a_jackie_dex_intro.scene`

198 graph nodes, 222 edges; 33 event-bearing sections, 395 events; 102 screenplay lines, 27 screenplay options, 8 choice nodes.

Actors: dex (actor 0, spawnSet); dex_bdg (actor 1, spawnSet); dex_limo (actor 2, community); v (actor 3, findInContext).

Entries: `q001_meet_dex_in` → 97; `Start 6` → 2384; `Start 5` → 1870.

Exits: `q001_meet_dex_out` → 6.

End nodes: 6: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 12 | 624 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnChangeIdleAnimEvent` | 11 | 624 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnDialogLineEvent` | 74 | 635 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/1` |
| `scnGameplayActionEvent` | 1 | 1844 / 814 | `/Data/RootChunk/sceneGraph/Data/graph/54/Data/events/8` |
| `scnGameplayTransitionEvent` | 1 | 1176 / 315 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/5` |
| `scnIKEvent` | 6 | 1176 / 309 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/1` |
| `scnLookAtEvent` | 98 | 624 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 95 | 624 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/3` |
| `scnUnmountEvent` | 1 | 1176 / 320 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/9` |
| `scneventsAttachPropToPerformer` | 5 | 624 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scneventsAttachPropToWorld` | 2 | 856 / 220 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/11` |
| `scneventsSetAnimFeatureEvent` | 33 | 639 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/3` |
| `scneventsSocket` | 51 | 624 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scneventsVFXEvent` | 5 | 685 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/21` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal, animation_state: 7
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 4
- gaze: 3
- speech, skeletal_animation, gaze: 2
- skeletal_animation, gaze, socket_signal, animation_state: 2
- skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, gaze, props_equipment, audio, vfx, socket_signal, animation_state: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, idle_animation, gaze, ik, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, audio, socket_signal, animation_state, gameplay_action: 1
- skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- skeletal_animation, gaze, ik, audio, socket_signal, animation_state: 1
- speech, skeletal_animation: 1
- skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1

Raw SHA-256: `88c668accd399ee4a874080d6a6a70e05fe3e333dd42a6cc3737c93ce9710f1e`. Binary SHA-256: `953b074432cfefcbb41eb9542dc25652943fb2fdd3641b61122d0e459b778383`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_03a_jackie_dex_intro.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_03a_meet_jackie_downstairs.scene`

200 graph nodes, 243 edges; 42 event-bearing sections, 409 events; 76 screenplay lines, 16 screenplay options, 8 choice nodes.

Actors: jackie (actor 0, spawnSet); dex (actor 1, findInWorld); dex bodyguard (actor 2, findInWorld); militech_agent (actor 3, findInWorld); cook (actor 4, community); v_tec (actor 5, spawnSet); v (actor 6, findInContext).

Entries: `q001_jackie_mb_in` → 960; `Start 5` → 1732; `q001_arrived_to_rd_in` → 1193.

Exits: `q001_jackie_mb_out` → 961; `q001_jackie_left_out` → 1515; `prefab_prefetch` → 2071; `q001_arrived_to_rd_out` → 1194.

End nodes: 961: `NonTerminating`; 1194: `<omitted>`; 1515: `<omitted>`; 2071: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1519 / 1062 | `/Data/RootChunk/sceneGraph/Data/graph/94/Data/events/2` |
| `scnChangeIdleAnimEvent` | 35 | 967 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/2` |
| `scnDialogLineEvent` | 58 | 962 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 975 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/8` |
| `scnIKEvent` | 4 | 975 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/1` |
| `scnLookAtEvent` | 77 | 962 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 152 | 962 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnUnmountEvent` | 2 | 975 / 85 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/13` |
| `scneventsAttachPropToPerformer` | 4 | 967 / 33 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/11` |
| `scneventsAttachPropToWorld` | 4 | 967 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/9` |
| `scneventsCameraParamsEvent` | 3 | 1994 / 1617 | `/Data/RootChunk/sceneGraph/Data/graph/165/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 2 | 975 / 81 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/10` |
| `scneventsSocket` | 47 | 962 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scneventsVFXEvent` | 18 | 967 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/13` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 8
- skeletal_animation, gaze: 7
- skeletal_animation: 5
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 3
- camera: 3
- speech, skeletal_animation, idle_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, vfx: 1
- speech: 1
- speech, skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- skeletal_animation, gaze, audio, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, socket_signal: 1

Raw SHA-256: `ff48765cbfbb1a76a7c073b442105251af5a6ba690218eb362cf8fe678b38209`. Binary SHA-256: `7eaf22d94484cbddafa9984e110f005b18a8d88a1acf9ec0e3578dadbf177284`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_03a_meet_jackie_downstairs.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_04_ripperdoc.scene`

391 graph nodes, 386 edges; 45 event-bearing sections, 715 events; 119 screenplay lines, 36 screenplay options, 16 choice nodes.

Actors: viktor (actor 0, spawnSet); boxing_commentator (actor 1, spawner); v_tpp_fem (actor 2, spawner); v_tpp_male (actor 3, spawner); sdsd (actor 4, spawnSet); v (actor 5, findInContext).

Entries: `q001_ripperdoc_in` → 1; `Start 9` → 2614; `Start 7` → 2318; `Start 6` → 2018; `Start 8` → 2343; `Start 2` → 1407; `Start 4` → 1870.

Exits: `q001_rd_chat_done_out` → 1260; `q001_ripperdoc_out` → 2.

End nodes: 2: `NonTerminating`; 1260: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 120 | 3 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/11` |
| `scnChangeIdleAnimEvent` | 79 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnDialogLineEvent` | 90 | 3 / 41 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/17` |
| `scnGameplayTransitionEvent` | 2 | 313 / 485 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/19` |
| `scnIKEvent` | 7 | 3 / 64 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/40` |
| `scnLookAtAdvancedEvent` | 11 | 272 / 266 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/37` |
| `scnLookAtEvent` | 50 | 3 / 37 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/13` |
| `scnPlaySkAnimEvent` | 166 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnUnmountEvent` | 2 | 313 / 492 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/25` |
| `scneventsAttachPropToPerformer` | 7 | 297 / 320 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/11` |
| `scneventsAttachPropToWorld` | 7 | 52 / 100 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/14` |
| `scneventsCameraParamsEvent` | 7 | 272 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 2 | 313 / 488 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/22` |
| `scneventsSocket` | 141 | 3 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsVFXEvent` | 24 | 3 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 4
- speech: 4
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 4
- speech, skeletal_animation, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 3
- speech, skeletal_animation: 3
- speech, skeletal_animation, idle_animation, gaze, camera, audio, vfx, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, socket_signal: 2
- skeletal_animation, idle_animation, gaze, audio, socket_signal: 2
- skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, audio, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation: 1
- speech, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- skeletal_animation, idle_animation, props_equipment: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, audio: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, gaze: 1
- camera: 1

Raw SHA-256: `df11cdf0b327b2913ea6164b297cac045a4496c32c8a3b1dcb05d91c90e061fe`. Binary SHA-256: `42936da965ee84731061a69823ea91a150f6e7461dba8e27abdd65005431a671`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_04_ripperdoc.scene" --events
```

## `base\quest\main_quests\prologue\q001\scenes\q001_04a_rd_assistant.scene`

84 graph nodes, 112 edges; 24 event-bearing sections, 117 events; 36 screenplay lines, 2 screenplay options, 2 choice nodes.

Actors: assistant (actor 0, spawnSet); jackie (actor 1, spawnSet); kitty (actor 2, spawner); v (actor 3, findInContext).

Entries: `q001_kitty_in` → 869; `q001_kitty2_in` → 871; `for tests` → 975; `q001_04a_first_entry` → 551; `q001_jackie_goes_in` → 729; `q001_04a_after_victor` → 572.

Exits: `q001_jackie_goes_out` → 730; `q001_04a_first_entry_end` → 561.

End nodes: 561: `NonTerminating`; 730: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 355 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnChangeIdleAnimEvent` | 12 | 43 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnDialogLineEvent` | 18 | 44 / 18 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 594 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/14` |
| `scnIKEvent` | 2 | 594 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/6` |
| `scnLookAtEvent` | 24 | 43 / 15 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/6` |
| `scnPlaySkAnimEvent` | 31 | 43 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnPoseCorrectionEvent` | 5 | 620 / 119 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |
| `scnUnmountEvent` | 1 | 594 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/13` |
| `scneventsAttachPropToPerformer` | 2 | 43 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 594 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/10` |
| `scneventsSocket` | 18 | 43 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 2
- speech, skeletal_animation: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation: 2
- skeletal_animation, idle_animation: 2
- skeletal_animation, gaze: 2
- skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, audio: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, idle_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 1
- speech: 1
- skeletal_animation, idle_animation, gaze, socket_signal: 1
- idle_animation, audio: 1
- socket_signal: 1

Raw SHA-256: `7497c9d666b997c8cdb950a9add375decafc3a0fa24e4095fcb9e12720602782`. Binary SHA-256: `54f8971b0ae080532ddf8bf7ee7961a2a8f33f89be14d6462a9191a6741770e6`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\prologue\q001\scenes\q001_04a_rd_assistant.scene" --events
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

