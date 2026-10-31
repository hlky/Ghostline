# Cyberpsycho Sighting: Bloody Ritual: scene presentation

Journal identity: `quests/minor_quest/ma_wat_nid_15`. Stored type: **CyberPsycho**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-ma_wat_nid_15.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_01_briefing.scene`

22 graph nodes, 25 edges; 1 event-bearing sections, 3 events; 3 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: regina (actor 0, spawnSet); Player (actor 1, findInContext).

Entries: `Start 0` → 1.

Exits: `End 0` → 2; `rejected_out` → 252.

End nodes: 2: `<omitted>`; 252: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 2. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 3 | 30 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 1

Raw SHA-256: `7ba52dbf46b7df7870aed06673ab7c3c34ad8d915d0e4ecb74acc82fa4b71ebb`. Binary SHA-256: `639831604f96ae8d666c2887b84612948d6686d98dd2ee37f9f9c097fd33f5fc`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_01_briefing.scene" --events
```

## `base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene`

381 graph nodes, 450 edges; 12 event-bearing sections, 27 events; 12 screenplay lines, 13 screenplay options, 12 choice nodes.

Actors: johnny (actor 0, spawnDespawn); maelstrom_dying (actor 1, community); cyberpsycho (actor 2, community); cyberpsycho_02 (actor 3, community); cyberpsycho_03 (actor 4, community); Player (actor 5, findInContext).

Entries: `Start 0` → 1; `test` → 3058.

Exits: `End 0` → 2; `maelstrom_dying_out` → 234; `blasephemer_out` → 2155.

End nodes: 2: `<omitted>`; 234: `NonTerminating`; 2155: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnLookAtEvent` | 11 | 1981 / 335 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/2` |
| `scnPlaySkAnimEvent` | 4 | 1981 / 331 | `/Data/RootChunk/sceneGraph/Data/graph/64/Data/events/0` |
| `scneventsSocket` | 12 | 1909 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/53/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- gaze: 7
- skeletal_animation, gaze, socket_signal: 2
- socket_signal: 1
- skeletal_animation, socket_signal: 1
- gaze, socket_signal: 1

Raw SHA-256: `b976d1e82f22ecd9f00f9b717e771c8e00a94da6cc9f318c9d4e66bedfb66667`. Binary SHA-256: `c8d50aa7036e1edf0f09284750618fd848f5d42720b87155b6d3db938d02379a`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\open_world\minor_activities\watson\northside\ma_wat_nid_15\scenes\ma_wat_nid_15_investigation.scene" --events
```

## `base\quest\minor_quests\mq026\scenes\mq026_04_smuggler.scene`

314 graph nodes, 369 edges; 23 event-bearing sections, 120 events; 41 screenplay lines, 7 screenplay options, 4 choice nodes.

Actors: MIB01 (actor 0, community); MIB02 (actor 1, community); GangRifle01 (actor 2, community); GangMelee01 (actor 3, community); GangHandgun01 (actor 4, community); GangMachete02 (actor 5, community); GangShotgun (actor 6, community); Johnny (actor 7, spawnDespawn); GangTank01 (actor 8, community); maelstrom_dying (actor 9, community); mq026_van (actor 10, spawner); mq026_mal_01 (actor 11, spawner); mq026_mal_02 (actor 12, spawner); Player (actor 13, findInContext).

Entries: `Start 0` → 725; `cyberpsycho_line` → 2016.

Exits: `cyberpsycho_out` → 2025; `cleanup_out` → 518.

End nodes: 518: `<omitted>`; 2025: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 7 | 525 / 716 | `/Data/RootChunk/sceneGraph/Data/graph/102/Data/events/0` |
| `scnDialogLineEvent` | 31 | 40 / 87 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/2` |
| `scnGameplayTransitionEvent` | 4 | 1283 / 1465 | `/Data/RootChunk/sceneGraph/Data/graph/199/Data/events/11` |
| `scnIKEvent` | 8 | 1283 / 1458 | `/Data/RootChunk/sceneGraph/Data/graph/199/Data/events/5` |
| `scnLookAtEvent` | 10 | 495 / 691 | `/Data/RootChunk/sceneGraph/Data/graph/97/Data/events/4` |
| `scnPlaySkAnimEvent` | 28 | 40 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/0` |
| `scnUnmountEvent` | 4 | 1283 / 1464 | `/Data/RootChunk/sceneGraph/Data/graph/199/Data/events/10` |
| `scneventsEquipItemToPerformer` | 2 | 1139 / 1328 | `/Data/RootChunk/sceneGraph/Data/graph/181/Data/events/4` |
| `scneventsSetAnimFeatureEvent` | 4 | 1283 / 1460 | `/Data/RootChunk/sceneGraph/Data/graph/199/Data/events/7` |
| `scneventsSocket` | 21 | 40 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/11/Data/events/3` |
| `scneventsUnequipItemFromPerformerByItem` | 1 | 1139 / 1330 | `/Data/RootChunk/sceneGraph/Data/graph/181/Data/events/6` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation: 3
- skeletal_animation, socket_signal: 3
- speech, skeletal_animation, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze: 1
- speech, idle_animation, socket_signal: 1
- speech, idle_animation, gaze: 1
- speech, idle_animation: 1
- skeletal_animation, gaze, props_equipment, socket_signal: 1
- skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze: 1

Raw SHA-256: `9b91c01394fd8b88126c22871e9a17c7ec483205ae055cda31b765bb94ca3e60`. Binary SHA-256: `436d0517bb59a9c654cd640dedf7a5659f5a5af558f58280476a03f2d86bee79`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq026\scenes\mq026_04_smuggler.scene" --events
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

