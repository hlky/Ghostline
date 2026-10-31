# Gig: Flight of the Cheetah: scene presentation

Journal identity: `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_03`. Stored type: **StreetStory**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sts_wat_nid_03.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_03\scenes\sts_wat_nid_03_haruo.scene`

105 graph nodes, 113 edges; 26 event-bearing sections, 109 events; 48 screenplay lines, 9 screenplay options, 5 choice nodes.

Actors: Hwangbo_Dong_Gun (actor 0, community); V (actor 1, findInContext).

Entries: `nid_03_haruo_talk` → 6; `nid_03_haruo_panic` → 18; `nid_03_haruo_extracted` → 23; `nid_03_car` → 28; `nid_03_nomads_in_car` → 33; `nid_03_nomads_command` → 45; `Sts_wrongfully_finished` → 513; `nid_03_car_dialogue_start` → 60.

Exits: `nid_03_haruo_talk_end` → 7; `nid_03_haruo_panic_end` → 21; `nid_03_haruo_extracted_end` → 26; `nid_03_car_end` → 29; `nid_03_nomads_in_car_end` → 34; `nid_03_nomads_command_end` → 48; `brakes` → 504; `Scene_kill` → 515; `nid_03_car_dialogue_end` → 61; `interupted_by_combat` → 521; `sms` → 210; `Hwangbo_exit` → 111.

End nodes: 7: `NonTerminating`; 21: `NonTerminating`; 26: `NonTerminating`; 29: `NonTerminating`; 34: `<omitted>`; 48: `NonTerminating`; 61: `NonTerminating`; 111: `NonTerminating`; 210: `NonTerminating`; 504: `NonTerminating`; 515: `<omitted>`; 521: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 6 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 33 | 8 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnGameplayTransitionEvent` | 2 | 108 / 179 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/14` |
| `scnIKEvent` | 4 | 108 / 169 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/5` |
| `scnLookAtEvent` | 14 | 8 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 19 | 12 / 20 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/4` |
| `scnPoseCorrectionEvent` | 2 | 12 / 26 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnUnmountEvent` | 2 | 108 / 178 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/13` |
| `scneventsSetAnimFeatureEvent` | 2 | 108 / 174 | `/Data/RootChunk/sceneGraph/Data/graph/38/Data/events/10` |
| `scneventsSocket` | 25 | 8 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 6
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation: 2
- speech, skeletal_animation, socket_signal: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- socket_signal: 2
- speech, skeletal_animation, idle_animation, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal: 1
- gaze: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1

Raw SHA-256: `648a6fe641f3e7c2349749a0cce96fde326ac4393e7398267276e106eaae1b50`. Binary SHA-256: `2c940fb0cb86ca1dabe46d748553159e3d633fb0466267bf4ac1fe1863d2c54c`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_03\scenes\sts_wat_nid_03_haruo.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_03\scenes\sts_wat_nid_03_holocall_debriefs.scene`

46 graph nodes, 60 edges; 2 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `debrief_not_perfect` → 1; `debrief_perfect` → 153.

Exits: `debrief_not_perfect_end` → 2; `rejected_perfect_out` → 333; `debrief_perfect_end` → 154; `rejected_not perfect_out` → 320.

End nodes: 2: `<omitted>`; 154: `<omitted>`; 320: `<omitted>`; 333: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2

Raw SHA-256: `e0dcebce5375356b51f1b026f3825036a97faec3355bdc85127e9aa82142deb0`. Binary SHA-256: `895caa52151303348706531c47a29ad810285c44083a572bb1ba4abf6e52eadb`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_03\scenes\sts_wat_nid_03_holocall_debriefs.scene" --events
```

## `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_03\scenes\sts_wat_nid_03_holocall_prebrief.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 2 events; 2 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: fixer (actor 0, spawnSet).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 260.

End nodes: 2: `<omitted>`; 260: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 2 | 26 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `4ee4b6ffe4b8fca2270d1e771ff8bb17de90b7e84903f2b37d670ede67fd60dc`. Binary SHA-256: `0bec0eb452fe747ed0e62d1c1687f44721a6234e9426e23da5946e0fff026b97`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_03\scenes\sts_wat_nid_03_holocall_prebrief.scene" --events
```

## `ep1\quest\main_quests\q305\scenes\q305_02d_chang.scene`

141 graph nodes, 181 edges; 32 event-bearing sections, 302 events; 89 screenplay lines, 13 screenplay options, 9 choice nodes.

Actors: chang (actor 0, community); Johnny (actor 1, spawnDespawn); V (actor 2, findInContext).

Entries: `q305_02d_chang_in` → 1; `Start 0` → 591; `wait_chang_in` → 322; `Start 1` → 538.

Exits: `q305_02d_chang_terminate_out` → 2; `End 0` → 593; `wait_chang_out` → 324; `time_change` → 348; `q305_02d_chang_out` → 270.

End nodes: 2: `<omitted>`; 270: `NonTerminating`; 324: `NonTerminating`; 348: `NonTerminating`; 593: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 14 | 6 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnDialogLineEvent` | 51 | 6 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 3 | 6 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/22` |
| `scnIKEvent` | 6 | 6 / 42 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/15` |
| `scnLookAtEvent` | 63 | 6 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scnOverridePhantomParamsEvent` | 1 | 416 / 893 | `/Data/RootChunk/sceneGraph/Data/graph/80/Data/events/1` |
| `scnPlaySkAnimEvent` | 103 | 6 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPoseCorrectionEvent` | 6 | 32 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/7` |
| `scnUnmountEvent` | 3 | 6 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/21` |
| `scneventsAttachPropToWorld` | 2 | 130 / 441 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/0` |
| `scneventsEquipItemToPerformer` | 4 | 130 / 460 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/10` |
| `scneventsSetAnimFeatureEvent` | 3 | 6 / 45 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/18` |
| `scneventsSocket` | 41 | 6 / 22 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scneventsUnequipItemFromPerformer` | 2 | 130 / 462 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal, animation_state: 3
- skeletal_animation, socket_signal: 3
- speech: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- speech, gaze: 2
- skeletal_animation: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, socket_signal: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, gaze, socket_signal, animation_state: 1
- gaze, socket_signal: 1
- gaze: 1
- skeletal_animation, gaze: 1

Raw SHA-256: `e4473b2e906691bedbe0bc63d3a63314f46add8ce8062ba0a0abf535033da34f`. Binary SHA-256: `6cc9aeaaa224643dadb06f610884ac333fa7b7127754ea99b2015382ebe68ee8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q305\scenes\q305_02d_chang.scene" --events
```

