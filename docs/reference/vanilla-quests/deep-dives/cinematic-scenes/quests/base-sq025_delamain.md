# Epistrophy: scene presentation

Journal identity: `quests/side_quest/sq025_delamain`. Stored type: **SideQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-sq025_delamain.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\primary_characters\default_dialogues\delamain_default.scene`

420 graph nodes, 598 edges; 37 event-bearing sections, 159 events; 179 screenplay lines, 13 screenplay options, 2 choice nodes.

Actors: Delamain (actor 0, spawnSet); Delamain_Sad (actor 1, findInContext); Skippy (actor 2, findInContext); Delamain_voice (actor 3, findInContext); Player (actor 4, findInContext).

Entries: `in` → 1; `sq025_aftermath_in` → 83; `facetoface_in` → 1489; `smalltalk_in` → 688; `already_spawned_in` → 2044; `delamain_damaged` → 2099; `delamain_breaks` → 2102; `delamain_swim` → 2104; `delamain_pedestrian` → 2106.

Exits: `holocall_out` → 2; `holo-to-face_out` → 1498; `smalltalk_out` → 693; `sq025_aftermath_out` → 838; `CYB-4604769_out` → 2641.

End nodes: 2: `<omitted>`; 693: `<omitted>`; 838: `<omitted>`; 1498: `NonTerminating`; 2641: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 157 | 38 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 1 | 38 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 1 | 38 / 17 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 36
- speech, skeletal_animation, socket_signal: 1

Raw SHA-256: `e5e73b29ece8895e8755a52fcb1f4acea11b2c1cf99726297dbab7177400a53a`. Binary SHA-256: `4e809ee3e562b2cb38c976d817a24505f6f96f412018ff68822d98a585f1bc36`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\primary_characters\default_dialogues\delamain_default.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_01_crash.scene`

20 graph nodes, 21 edges; 3 event-bearing sections, 28 events; 9 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Player (actor 1, findInContext).

Entries: `spawned_car_crash_in` → 60; `impact` → 146.

Exits: `spawned_car_crash_out` → 62; `exit` → 110; `impact_out` → 211.

End nodes: 62: `NonTerminating`; 110: `NonTerminating`; 211: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 2 | 253 / 107 | `/Data/RootChunk/sceneGraph/Data/graph/18/Data/events/0` |
| `scnDialogLineEvent` | 8 | 46 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scnLookAtEvent` | 7 | 46 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/3` |
| `scnPlaySkAnimEvent` | 4 | 46 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/7` |
| `scneventsSocket` | 7 | 46 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze, socket_signal: 1
- skeletal_animation: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1

Raw SHA-256: `194e55980697fb2943905f4104f84052517110dfac42608e28dfe8f29cbf5a26`. Binary SHA-256: `849b9598dc68f1b833c5901653513da4077ff06d9533e0c29f2d49302effbfd1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_01_crash.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_03_reception.scene`

219 graph nodes, 263 edges; 36 event-bearing sections, 245 events; 83 screenplay lines, 14 screenplay options, 7 choice nodes.

Actors: Delamain_receptionist (actor 0, spawnSet); Delamain (actor 1, spawnSet); Stripper (actor 2, community); Old_Lady (actor 3, community); Maid (actor 4, community); Homeless (actor 5, community); Slacker (actor 6, community); Regular (actor 7, community); Corpo (actor 8, community); Homeless_2 (actor 9, community); Homeless_3 (actor 10, community); Player (actor 11, findInContext).

Entries: `refused_in` → 222; `delamain_compensation_in` → 1; `sq025_03_looping_finale_for_maid` → 1107; `chicken_in` → 238.

Exits: `refused_out` → 223; `delamain_compensation_out` → 2; `End1` → 684; `refused_before_tour_out` → 298; `exit` → 312.

End nodes: 2: `NonTerminating`; 223: `<omitted>`; 298: `NonTerminating`; 312: `<omitted>`; 684: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 11 | 12 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/0` |
| `scnDialogLineEvent` | 56 | 5 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 6 | 12 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/24` |
| `scnIKEvent` | 12 | 12 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/13` |
| `scnLookAtEvent` | 47 | 5 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scnPlaySkAnimEvent` | 30 | 12 / 21 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/8` |
| `scnUnmountEvent` | 6 | 12 / 48 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/23` |
| `scneventsSetAnimFeatureEvent` | 6 | 12 / 44 | `/Data/RootChunk/sceneGraph/Data/graph/3/Data/events/20` |
| `scneventsSocket` | 70 | 5 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scneventsVFXEvent` | 1 | 391 / 441 | `/Data/RootChunk/sceneGraph/Data/graph/46/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 10
- speech, socket_signal: 5
- skeletal_animation, socket_signal: 3
- speech, gaze, socket_signal: 2
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, idle_animation, gaze, socket_signal: 2
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- idle_animation, gaze, socket_signal: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, vfx: 1
- gaze, socket_signal: 1
- speech, gaze: 1
- socket_signal: 1
- idle_animation, socket_signal: 1

Raw SHA-256: `78ad10eaa8899f4542b56898e9be2e52b0364eb5ff8fc074657f6f8b59da0cdd`. Binary SHA-256: `8a39725dfbf189273f51af61b74a0974d9259db677327dcc3729d07fb5445a53`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_03_reception.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_04_briefing.scene`

134 graph nodes, 184 edges; 21 event-bearing sections, 50 events; 45 screenplay lines, 7 screenplay options, 2 choice nodes.

Actors: Delamain (actor 0, community); Delamain_holo (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `tour_in` → 10; `Start 2` → 687.

Exits: `tour_out` → 12; `End 1` → 658; `sq025_03_looping_ending` → 678.

End nodes: 12: `NonTerminating`; 658: `<omitted>`; 678: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 30 | 8 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnPlaySkAnimEvent` | 18 | 8 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |
| `scneventsSocket` | 2 | 89 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 10
- speech: 5
- speech, skeletal_animation: 4
- speech, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1

Raw SHA-256: `e5ce178f9303150700979e36b8d95da414dfe76b047a318a471def227b8d7516`. Binary SHA-256: `213ae44bf9573c06861e2ea4b3ea1cb9919ef57ffbe400f4d4471d2fd075dffd`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_04_briefing.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_05_scan.scene`

1710 graph nodes, 2004 edges; 75 event-bearing sections, 235 events; 189 screenplay lines, 28 screenplay options, 14 choice nodes.

Actors: Delamain (actor 0, spawnSet); Angry (actor 1, spawnSet); Sad (actor 2, spawnSet); Manic (actor 3, spawnSet); Mean (actor 4, spawnSet); Suicidal (actor 5, spawnSet); Deep (actor 6, spawnSet); Scared (actor 7, spawnSet); GANG_MLS_F_02_ENUS_25 (actor 8, community); GANG_MLS_F_03_ENUS_20 (actor 9, community); GANG_MLS_F_01_ENUS_30 (actor 10, community); GANG_MLS_F_04_ENUS_25 (actor 11, community); cyberpsycho (actor 12, community); Sad_voice (actor 13, findInContext); Deep_vehicle (actor 14, community); Angry_vehicle (actor 15, community); Suicidal_vehicle (actor 16, community); Mean_vehicle (actor 17, community); Scared_vehicle (actor 18, community); Sad_vehicle (actor 19, community); Manic_vehicle (actor 20, community); Player (actor 21, findInContext).

Entries: `angry_in` → 4; `sad_in` → 6; `suicidal_in` → 7; `deep_in` → 8; `scared_in` → 10; `manic_in` → 11; `mean_in` → 12; `Start 12` → 3670; `Start 13` → 3689; `Start 14` → 3706; `Start 15` → 3723; `Start 16` → 3737; `Start 18` → 3758; `Start 26` → 7546; `mobile1` → 7677; `Start 28` → 7801; `beep_in` → 4549; `blasphemer_in` → 6383; `sad_in_talk` → 2926; `angry_in_talk` → 2954; `suicidal_in_talk` → 2955; `deep_in_talk` → 2956; `scared_in_talk` → 2957; `manic_in_talk` → 2958; `mean_in_talk` → 2959; `Start 23` → 6960; `Start 24` → 6967; `Start 25` → 6992.

Exits: `angry_out` → 131; `suicidal_out` → 132; `deep_out` → 133; `scared_out` → 134; `mean_out` → 135; `reward_out` → 136; `manic_out` → 137; `sad_out` → 138; `sad_damage` → 7771; `sad_water` → 7775; `sad_crowd` → 7798; `sad_death` → 7802; `End 9` → 6391.

End nodes: 131: `<omitted>`; 132: `<omitted>`; 133: `<omitted>`; 134: `<omitted>`; 135: `<omitted>`; 136: `<omitted>`; 137: `<omitted>`; 138: `<omitted>`; 6391: `<omitted>`; 7771: `NonTerminating`; 7775: `NonTerminating`; 7798: `NonTerminating`; 7802: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 4 | 91 / 38 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/1` |
| `scnDialogLineEvent` | 169 | 79 / 19 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 7933 / 7717 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/4` |
| `scnIKEvent` | 2 | 7933 / 7715 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/2` |
| `scnLookAtEvent` | 17 | 79 / 23 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/4` |
| `scnPlaySkAnimEvent` | 4 | 1503 / 1464 | `/Data/RootChunk/sceneGraph/Data/graph/245/Data/events/1` |
| `scnUnmountEvent` | 1 | 7933 / 7721 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/7` |
| `scneventsCameraParamsEvent` | 3 | 6997 / 6162 | `/Data/RootChunk/sceneGraph/Data/graph/1023/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 1 | 7933 / 7719 | `/Data/RootChunk/sceneGraph/Data/graph/1279/Data/events/6` |
| `scneventsSocket` | 33 | 79 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/9` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 40
- speech, socket_signal: 19
- speech, gaze, socket_signal: 2
- speech, gaze: 2
- speech, skeletal_animation, gaze, socket_signal: 2
- idle_animation, gaze, socket_signal: 2
- speech, idle_animation, gaze: 1
- speech, skeletal_animation: 1
- idle_animation, gaze: 1
- gaze: 1
- gaze, socket_signal: 1
- camera: 1
- camera, socket_signal: 1
- skeletal_animation, ik, camera, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `249ac0c15568c48faedb121c325c5b673bfe319ccda854d8b28d8ee49cb8859d`. Binary SHA-256: `728ee318df921d11651256032dd465e82c0c8169ddf91bcf326349d842b2366a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_05_scan.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_06_reward.scene`

35 graph nodes, 37 edges; 4 event-bearing sections, 13 events; 12 screenplay lines, 3 screenplay options, 2 choice nodes.

Actors: Delamain (actor 0, community); Delamain_main (actor 1, spawnSet); Player (actor 2, findInContext).

Entries: `Start 1` → 169; `reward_in` → 1.

Exits: `reward_out` → 2.

End nodes: 2: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 10 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 1 | 42 / 28 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scneventsSocket` | 2 | 4 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 2
- speech, socket_signal: 1
- speech, gaze, socket_signal: 1

Raw SHA-256: `d96efed961a57870cba1340be0408603fdcd1b58894d3f3f495b1c7615319739`. Binary SHA-256: `b54dfb91d2c7a078cbe6ce9573af4933807fc63af7064a4718f9fef02e96683f`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_06_reward.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_06b_reward_holocall.scene`

45 graph nodes, 58 edges; 1 event-bearing sections, 4 events; 4 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Delamain (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `continue_talk` → 268.

End nodes: 2: `<omitted>`; 268: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 4 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `e39c07bf002d623c8d52589fc86ee0359880993c526871f670566ff5438ebd60`. Binary SHA-256: `aa60741a78f8221cecb73416a677ae8b572cf74d8b7475a23b3d9eb3bb1d9895`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_06b_reward_holocall.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_07_resurgence.scene`

55 graph nodes, 60 edges; 3 event-bearing sections, 10 events; 7 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Delamain (actor 1, spawnSet); sq025_resurgence_truck_01 (actor 2, spawner); sq025_resurgence_delamain_broken_04 (actor 3, spawner); sq025_resurgence_delamain_broken_03 (actor 4, spawner); Player (actor 5, findInContext).

Entries: `resurgence_in` → 1; `Start 1` → 136.

Exits: `resurgence_out` → 2; `exit` → 97.

End nodes: 2: `NonTerminating`; 97: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 7 | 4 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 2 | 4 / 13 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |
| `scneventsSocket` | 1 | 171 / 124 | `/Data/RootChunk/sceneGraph/Data/graph/20/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, gaze: 1
- speech, socket_signal: 1
- speech: 1

Raw SHA-256: `cacdd871cb515af924a647c1a6f41066c7875366050fc7f0f77eaf91cabd10f8`. Binary SHA-256: `7874e068ffcb83180daa16e94e0db4d6547f0d1d56c0026c20629ef6b60accec`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_07_resurgence.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_08_backoffice.scene`

17 graph nodes, 14 edges; 5 event-bearing sections, 7 events; 7 screenplay lines, 3 screenplay options, 3 choice nodes.

Actors: Delamain (actor 0, spawnSet); Johnny (actor 1, spawnSet); Business (actor 2, community); Player (actor 3, findInContext).

Entries: `reception_in` → 1; `backoffice_in` → 40; `corrdidor_in` → 163.

Exits: `reception_out` → 2; `backoffice_out` → 165.

End nodes: 2: `<omitted>`; 165: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 5 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 2 | 170 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/8/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 3
- speech, socket_signal: 2

Raw SHA-256: `e50dd8831566708ec04e83b2fea340694e7d1c7160591862915b7b81cfa147fe`. Binary SHA-256: `f3c1273f2759ebec58907911f3e61d709257d523acfef75de025f5e7ed926182`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_08_backoffice.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_09_labyrinth.scene`

80 graph nodes, 76 edges; 15 event-bearing sections, 88 events; 42 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Johnny (actor 0, spawnDespawn); Delamain_distorted (actor 1, findInContext); Delamain_angry (actor 2, findInContext); Delamain_sad (actor 3, findInContext); Delamain_manic (actor 4, findInContext); Delamain_mean (actor 5, findInContext); Delamain_scared (actor 6, findInContext); Delamain_deep (actor 7, findInContext); Delamain_suicidal (actor 8, findInContext); sq025_spwn_delamain_garage_push_cab (actor 9, spawner); Player (actor 10, findInContext).

Entries: `banter01_in` → 90; `banter02_in` → 91; `push_cab_in` → 11; `Start 11` → 332; `hangar_in` → 99; `q115_reuse__in` → 115; `Start 9` → 122; `Start 12` → 373; `workshop_intro_in` → 64; `sq025_09_custom_arms` → 388; `Start 10` → 239.

Exits: `q115_reuse__out` → 116; `workshop_intro_out` → 65.

End nodes: 65: `NonTerminating`; 116: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 1 | 106 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/3` |
| `scnDialogLineEvent` | 24 | 66 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnGameplayTransitionEvent` | 1 | 173 / 165 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/5` |
| `scnIKEvent` | 2 | 173 / 160 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/1` |
| `scnLookAtEvent` | 1 | 66 / 16 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/5` |
| `scnPlaySkAnimEvent` | 48 | 106 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |
| `scnUnmountEvent` | 1 | 173 / 164 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/4` |
| `scneventsCameraParamsEvent` | 2 | 106 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/2` |
| `scneventsSetAnimFeatureEvent` | 1 | 173 / 162 | `/Data/RootChunk/sceneGraph/Data/graph/30/Data/events/3` |
| `scneventsSocket` | 7 | 66 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- skeletal_animation: 7
- speech: 3
- speech, socket_signal: 2
- speech, gaze, socket_signal: 1
- skeletal_animation, idle_animation, camera: 1
- ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `c28f6a9e09a6688edcd70946f2ad7a510d3a91026fdf5b13e543d7f83878e4fb`. Binary SHA-256: `1645cbcd9a4f6b7915fa416f5451dfe683ad975b6467926a406100067662dab1`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_09_labyrinth.scene" --events
```

## `base\quest\side_quests\sq025\scenes\sq025_10_resolution.scene`

685 graph nodes, 808 edges; 58 event-bearing sections, 218 events; 143 screenplay lines, 13 screenplay options, 6 choice nodes.

Actors: Delamain (actor 0, spawnDespawn); Drone03 (actor 1, community); Drone04 (actor 2, community); Drone05 (actor 3, community); Drone06 (actor 4, community); Drone07 (actor 5, community); Johnny (actor 6, spawnDespawn); Delamain_Merged (actor 7, spawnDespawn); Delamain_Angry (actor 8, spawnDespawn); Delamain_Mean (actor 9, spawnDespawn); Delamain_Sad (actor 10, spawnDespawn); Delamain_Suicidal (actor 11, spawnDespawn); Delamain_Scared (actor 12, spawnDespawn); Delamain_Deep (actor 13, spawnDespawn); Delamain_Manic (actor 14, spawnDespawn); Delamain_Shy (actor 15, spawnDespawn); del_r1_l1 (actor 16, spawner); del_r1_l2 (actor 17, spawner); del_r1_l3 (actor 18, spawner); del_r1_l4 (actor 19, spawner); del_r1_l5 (actor 20, spawner); del_r2_l1 (actor 21, spawner); del_r2_l2_SAD (actor 22, spawner); del_r2_l3 (actor 23, spawner); del_r2_l4 (actor 24, spawner); del_r2_l5 (actor 25, spawner); del_player (actor 26, spawner); Player (actor 27, findInContext).

Entries: `resolution_in` → 1; `Start 3` → 1625; `Start 4` → 1687; `Start 5` → 1689; `Start 11` → 3253; `Start 6` → 1724; `rec` → 3355; `Start 8` → 2761; `suicidal_only` → 2031; `Start 13` → 3659; `controlroom_in` → 580; `Start 9` → 3000; `Start 10` → 3060; `Start 2` → 1538.

Exits: `controlroom_out` → 581; `resolution_out` → 586.

End nodes: 581: `NonTerminating`; 586: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1270 / 346 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/3` |
| `scnChangeIdleAnimEvent` | 31 | 31 / 39 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scnDialogLineEvent` | 98 | 25 / 31 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/0` |
| `scnGameplayActionEvent` | 2 | 1627 / 877 | `/Data/RootChunk/sceneGraph/Data/graph/118/Data/events/8` |
| `scnIKEvent` | 2 | 2993 / 2089 | `/Data/RootChunk/sceneGraph/Data/graph/315/Data/events/3` |
| `scnLookAtEvent` | 10 | 1264 / 314 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/2` |
| `scnPlaySkAnimEvent` | 32 | 1264 / 323 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/10` |
| `scneventsCameraParamsEvent` | 4 | 1270 / 345 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/2` |
| `scneventsEquipItemToPerformer` | 3 | 1264 / 319 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/7` |
| `scneventsSocket` | 34 | 25 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/5/Data/events/4` |
| `scneventsUnequipItemFromPerformer` | 1 | 1264 / 329 | `/Data/RootChunk/sceneGraph/Data/graph/51/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- idle_animation: 14
- speech, socket_signal: 11
- speech, gaze: 3
- speech, gaze, socket_signal: 2
- speech, idle_animation, socket_signal: 1
- speech, skeletal_animation, gaze, props_equipment, socket_signal: 1
- speech, skeletal_animation, idle_animation, camera, audio, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- skeletal_animation: 1
- skeletal_animation, idle_animation, gameplay_action: 1
- skeletal_animation, idle_animation: 1
- skeletal_animation, idle_animation, socket_signal: 1
- socket_signal: 1
- skeletal_animation, ik, camera, socket_signal: 1
- props_equipment, socket_signal: 1

Raw SHA-256: `a458a34e3f140486010e42ca35d64584133da5667c05bd81842f50239f2912d7`. Binary SHA-256: `6c1c965b2557b8ada4372b226f3702c93362e73076b7bbe368b780f57c880aee`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\side_quests\sq025\scenes\sq025_10_resolution.scene" --events
```

## `ep1\quest\main_quests\q307\scenes\q307_04_cabride.scene`

273 graph nodes, 417 edges; 76 event-bearing sections, 290 events; 221 screenplay lines, 44 screenplay options, 18 choice nodes.

Actors: delamain (actor 0, spawnSet); radio_host1 (actor 1, findInContext); radio_host2 (actor 2, findInContext); junior_delamain (actor 3, findInContext); delamain_cab (actor 4, spawner); av1 (actor 5, spawner); av2 (actor 6, spawner); Player (actor 7, findInContext).

Entries: `Start 0` → 1; `av_landing_in` → 1799.

Exits: `End 0` → 2; `End1` → 1059.

End nodes: 2: `NonTerminating`; 1059: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 1783 / 1177 | `/Data/RootChunk/sceneGraph/Data/graph/216/Data/events/1` |
| `scnChangeIdleAnimEvent` | 1 | 1783 / 1178 | `/Data/RootChunk/sceneGraph/Data/graph/216/Data/events/2` |
| `scnDialogLineEvent` | 203 | 22 / 36 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/0` |
| `scnGameplayTransitionEvent` | 2 | 1085 / 655 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/8` |
| `scnIKEvent` | 4 | 1085 / 646 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/1` |
| `scnPlaySkAnimEvent` | 16 | 210 / 114 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/0` |
| `scnUnmountEvent` | 2 | 1085 / 659 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/11` |
| `scneventsAttachPropToPerformer` | 5 | 1085 / 649 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/4` |
| `scneventsAttachPropToWorld` | 2 | 1085 / 654 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/7` |
| `scneventsCameraParamsEvent` | 11 | 210 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 4 | 1085 / 657 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/10` |
| `scneventsSocket` | 37 | 210 / 120 | `/Data/RootChunk/sceneGraph/Data/graph/17/Data/events/1` |
| `scneventsVFXEvent` | 2 | 1783 / 1179 | `/Data/RootChunk/sceneGraph/Data/graph/216/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 56
- speech, socket_signal: 7
- skeletal_animation, camera, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, ik, camera, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- skeletal_animation, camera, props_equipment, socket_signal: 2
- speech, skeletal_animation, camera, socket_signal: 1
- skeletal_animation, camera, props_equipment, socket_signal, animation_state: 1
- skeletal_animation: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 1

Raw SHA-256: `ae5ecffe9e87b13df061de1b891e2b24a280ec411ca8198e8a9638ab4d262ae6`. Binary SHA-256: `a8a0e38d8ba90b4f35bfb879dafdaee51dbd6598194e4e561ed80004a9e98b37`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "ep1\quest\main_quests\q307\scenes\q307_04_cabride.scene" --events
```

