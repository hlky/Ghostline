# Spray Paint: scene presentation

Journal identity: `quests/minor_quest/mq037_brendan_hooligan001`. Stored type: **MinorQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-mq037_brendan_hooligan001.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene`

295 graph nodes, 312 edges; 85 event-bearing sections, 769 events; 270 screenplay lines, 51 screenplay options, 28 choice nodes.

Actors: Technician (actor 0, community); Brendan (actor 1, community); Girlfriend (actor 2, community); Hooligan (actor 3, community); Clerk (actor 4, community); Brendan_1 (actor 5, community); Player (actor 6, findInContext).

Entries: `technician_in` → 1; `post_kids_dial_in` → 37; `dumpster_help_in` → 46; `dump_dial_start_in` → 58; `help_plz_in` → 65; `obj_moved_in` → 79; `post_dump_dial_in` → 84; `girl_dial_in` → 92; `cineStart` → 1330; `clerk_in` → 590; `post_girl_dial_in` → 104; `hooligan_stop_in` → 111; `clerk_aggro_in` → 617; `intervene_dial_in` → 127; `brandan_saved_in` → 140; `brendan_gone_in` → 145; `brendan_found_in` → 152; `bad_news_in` → 157; `use_pc_in` → 169; `dumpster_help_closer_in` → 669; `do not connect 001` → 680; `hooligan_setup_in` → 1673; `hooligan_attacked_in` → 955; `CYB-661474_kill_signal_in` → 1716.

Exits: `technician_out` → 2; `brendan_gone_terminating` → 1027; `post_kids_dial_out` → 44; `dumpster_help_out` → 47; `bad_news_terminating` → 1292; `clerk_threat_terminating` → 1048; `dump_dial_start_out` → 62; `help_plz_out` → 66; `obj_moved_out` → 80; `interrupt_hooligan_loop` → 826; `post_dump_dial_out` → 85; `catch_you_non_term` → 1328; `hooligan_run_terminate` → 836; `clerk_out` → 591; `girl_dial_out` → 102; `hooligan_terminating` → 1344; `post_girl_dial_out` → 109; `hooligan_stop_out` → 114; `clerk_aggro_out` → 618; `threaten_out` → 136; `combat_out` → 138; `brandan_saved_out` → 141; `brendan_gone_out` → 146; `brendan_found_out` → 153; `bad_news_out` → 158; `use_pc_out` → 170; `dumpster_help_closer_out` → 671; `girl_dial_terminate` → 709; `hooligan_attacked_out` → 957; `CYB-661474_kill_signal__out` → 1717; `brendan_asked_for_help` → 1227.

End nodes: 2: `<omitted>`; 44: `<omitted>`; 47: `<omitted>`; 62: `<omitted>`; 66: `<omitted>`; 80: `<omitted>`; 85: `<omitted>`; 102: `NonTerminating`; 109: `<omitted>`; 114: `NonTerminating`; 136: `NonTerminating`; 138: `NonTerminating`; 141: `<omitted>`; 146: `NonTerminating`; 153: `<omitted>`; 158: `NonTerminating`; 170: `<omitted>`; 591: `NonTerminating`; 618: `<omitted>`; 671: `<omitted>`; 709: `<omitted>`; 826: `NonTerminating`; 836: `<omitted>`; 957: `<omitted>`; 1027: `NonTerminating`; 1048: `<omitted>`; 1227: `NonTerminating`; 1292: `NonTerminating`; 1328: `NonTerminating`; 1344: `<omitted>`; 1717: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 42 | 93 / 110 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/7` |
| `scnDialogLineEvent` | 251 | 3 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 9 | 99 / 183 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/22` |
| `scnIKEvent` | 18 | 99 / 176 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/16` |
| `scnLookAtEvent` | 71 | 93 / 99 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/0` |
| `scnPlaySkAnimEvent` | 111 | 93 / 101 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/2` |
| `scnUnmountEvent` | 9 | 99 / 182 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/21` |
| `scneventsEquipItemToPerformer` | 1 | 604 / 1193 | `/Data/RootChunk/sceneGraph/Data/graph/130/Data/events/9` |
| `scneventsSetAnimFeatureEvent` | 9 | 99 / 180 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/20` |
| `scneventsSocket` | 121 | 42 / 27 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/5` |
| `scneventsUnequipItemFromPerformerByItem` | 4 | 99 / 168 | `/Data/RootChunk/sceneGraph/Data/graph/31/Data/events/12` |
| `scneventsVFXDurationEvent` | 121 | 3 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/2` |
| `scneventsVFXEvent` | 2 | 422 / 799 | `/Data/RootChunk/sceneGraph/Data/graph/100/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, vfx, socket_signal: 31
- speech, vfx: 18
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 7
- speech: 5
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 5
- speech, skeletal_animation, idle_animation, gaze, props_equipment, socket_signal: 3
- speech, skeletal_animation, idle_animation, gaze, vfx, socket_signal: 2
- idle_animation, socket_signal: 2
- socket_signal: 2
- speech, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, ik, props_equipment, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, idle_animation: 1
- skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- gaze, socket_signal: 1
- speech, idle_animation, vfx, socket_signal: 1

Raw SHA-256: `799a1a7b10fe8aa81450f536927a316eff7237a53680e5b679c57501ab3f3184`. Binary SHA-256: `4ed7f040bfbe1f424825aff57c33fbb1c007d52d19243475c9543bd84a3514d2`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene" --events
```

