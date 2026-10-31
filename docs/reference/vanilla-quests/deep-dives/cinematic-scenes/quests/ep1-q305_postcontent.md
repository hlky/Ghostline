# This Corrosion: scene presentation

Journal identity: `ep1/quests/main_quest/q305_postcontent`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/ep1-q305_postcontent.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\vendors\watson\kabuki\wat_kab_netrunner_01\wat_kab_netrunner_01.scene`

257 graph nodes, 318 edges; 50 event-bearing sections, 527 events; 120 screenplay lines, 36 screenplay options, 13 choice nodes.

Actors: wat_kab_netrunner_01 (actor 0, spawnSet); Johnny (actor 1, spawnDespawn); Player (actor 2, findInContext).

Entries: `wat_kab_netrunner_01_start` → 4; `wait_yoko_in` → 453; `Start 1` → 1324.

Exits: `wait_yoko_out` → 455; `time_change` → 475.

End nodes: 455: `NonTerminating`; 475: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 30 | 137 / 135 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/14` |
| `scnChangeIdleAnimEvent` | 14 | 125 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/1` |
| `scnDialogLineEvent` | 103 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 3 | 167 / 293 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/7` |
| `scnIKEvent` | 9 | 167 / 285 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/1` |
| `scnLookAtAdvancedEvent` | 5 | 155 / 201 | `/Data/RootChunk/sceneGraph/Data/graph/22/Data/events/2` |
| `scnLookAtEvent` | 87 | 7 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/1` |
| `scnOverridePhantomParamsEvent` | 1 | 402 / 988 | `/Data/RootChunk/sceneGraph/Data/graph/81/Data/events/12` |
| `scnPlaySkAnimEvent` | 128 | 125 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/2` |
| `scnPoseCorrectionEvent` | 4 | 125 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/6` |
| `scnUnmountEvent` | 3 | 167 / 298 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/11` |
| `scneventsAttachPropToPerformer` | 7 | 167 / 307 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/15` |
| `scneventsAttachPropToWorld` | 7 | 167 / 309 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/17` |
| `scneventsEquipItemToPerformer` | 9 | 137 / 148 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/20` |
| `scneventsSetAnimFeatureEvent` | 3 | 167 / 294 | `/Data/RootChunk/sceneGraph/Data/graph/24/Data/events/8` |
| `scneventsSocket` | 105 | 125 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/8` |
| `scneventsUnequipItemFromPerformer` | 7 | 149 / 188 | `/Data/RootChunk/sceneGraph/Data/graph/21/Data/events/13` |
| `scneventsVFXEvent` | 2 | 1300 / 2177 | `/Data/RootChunk/sceneGraph/Data/graph/236/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, gaze: 5
- speech, skeletal_animation, gaze, socket_signal: 5
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 3
- skeletal_animation, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 2
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, audio, vfx, socket_signal: 2
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, audio, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, audio, socket_signal: 1
- socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- skeletal_animation, audio, socket_signal: 1
- skeletal_animation, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, socket_signal: 1

Raw SHA-256: `746ab3e3d81b9f2bdfe9a28eea401dabbfd4ceb580745a7b300704b452298d13`. Binary SHA-256: `3618c469468e73c67f6d1f9d8a4a85babda949fa1692a204dde7c732ee253104`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\vendors\watson\kabuki\wat_kab_netrunner_01\wat_kab_netrunner_01.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_16_haunted_weapons_reactions.scene`

140 graph nodes, 166 edges; 29 event-bearing sections, 29 events; 29 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Haunted_weapon (actor 0, findInContext); Haunted_deck (actor 1, findInContext); Haunted_deck_v2 (actor 2, findInContext); Player (actor 3, findInContext).

Entries: `Start 0` → 1; `random_whisper_01_in` → 149; `random_whisper_02_in` → 151; `Disobedience_02_in` → 322; `Death_in` → 54; `Disobedience_in` → 56; `Random_whisper_in` → 58; `Reload_in` → 60; `hack_in` → 62; `commentary_01_in` → 64; `Weapon_type` → 208; `death_android_in` → 73; `boss_in` → 103; `commentary_02_in` → 131.

Exits: `End 0` → 2.

End nodes: 2: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 29 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 29

Raw SHA-256: `3ffe319474a9436905545952f8fe317a5263542e178b6ebe88dec032d1a83539`. Binary SHA-256: `a77e5bc954c863badb0928b93082ad2bc8b2174346b19a778869669dc1cc9df2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_16_haunted_weapons_reactions.scene" --events
```

