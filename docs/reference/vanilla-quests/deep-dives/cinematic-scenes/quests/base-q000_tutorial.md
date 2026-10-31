# Practice Makes Perfect: scene presentation

Journal identity: `quests/main_quest/prologue/q000_tutorial`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q000_tutorial.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

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

