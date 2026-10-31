# Forward to Death: scene presentation

Journal identity: `quests/main_quest/act_01/q114_02_maglev_line_assault`. Stored type: **MainQuest**. Attribution: **journal-linked**.

[Full quest flow dossier](../../all-quests/base-q114_02_maglev_line_assault.md) · [All cinematic studies](../README.md)

The scenes below belong to the existing selected forward context. Whole-scene inventory includes alternate entries and branches; it is not a claim that every event executes for this journal identity. Shared resources may also appear in other quests.

## `base\quest\main_quests\part1\q114\scenes\q114_08_morning.scene`

165 graph nodes, 172 edges; 32 event-bearing sections, 198 events; 70 screenplay lines, 6 screenplay options, 4 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); johnny (actor 2, spawnSet); Mitch (actor 3, spawnSet); Dakota (actor 4, community); Teddy (actor 5, spawnSet); Bob (actor 6, spawnSet); Carol (actor 7, spawnSet); Cassidy (actor 8, spawnSet); Aldecaldo_F_03 (actor 9, spawnDespawn); Aldecaldo_M_02 (actor 10, spawnDespawn); Aldecaldo_M_04 (actor 11, spawnDespawn); Aldecaldo_f_03_2chat (actor 12, spawnDespawn); Aldecaldo_m_04_2chat (actor 13, spawnDespawn); Aldecaldo_m_04_3chat (actor 14, spawnDespawn); Aldecaldo_m_02_3chat (actor 15, spawnDespawn); panzer (actor 16, spawnSet); cassidy (actor 17, community); panamcar (actor 18, spawnSet); multipla2 (actor 19, community); teddy (actor 20, community); bike1 (actor 21, community); bike2 (actor 22, community); car1 (actor 23, community); car2 (actor 24, community); car3 (actor 25, community); car4 (actor 26, community); bike3 (actor 27, community); decochar1 (actor 28, community); decocar2 (actor 29, community); decocar3 (actor 30, community); decocar4 (actor 31, community); decocar5 (actor 32, community); decocar6 (actor 33, community); decocar7 (actor 34, spawnSet); decocar8 (actor 35, spawnSet); dekobike (actor 36, community); dekobike2 (actor 37, community); dekobike3 (actor 38, community); dekobike4 (actor 39, community); dekovan1 (actor 40, community); dekonva2 (actor 41, community); jammer (actor 42, community); V (actor 43, findInContext).

Entries: `q114_08_panam_in` → 1; `q114_08_timelapsein_securing` → 1362; `Start 6` → 1209; `q114_08_drone_in` → 98; `q114_08_morning_planning_02_in` → 265; `Start 8` → 1887; `Start 9` → 2088.

Exits: `q114_08_panam_out` → 2; `mounting_out` → 1967; `q114_08_morning_planning_02_out` → 267; `q114_08_drone_out` → 120.

End nodes: 2: `<omitted>`; 120: `<omitted>`; 267: `<omitted>`; 1967: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 4 | 1067 / 352 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/7` |
| `scnChangeIdleAnimEvent` | 3 | 299 / 56 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/3` |
| `scnDialogLineEvent` | 66 | 6 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnGameplayTransitionEvent` | 4 | 962 / 264 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/23` |
| `scnIKEvent` | 8 | 962 / 254 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/14` |
| `scnLookAtEvent` | 20 | 299 / 53 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/0` |
| `scnPlaySkAnimEvent` | 28 | 299 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/4` |
| `scnUnmountEvent` | 3 | 962 / 263 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/22` |
| `scneventsAttachPropToNode` | 1 | 337 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/8` |
| `scneventsAttachPropToPerformer` | 2 | 337 / 74 | `/Data/RootChunk/sceneGraph/Data/graph/16/Data/events/3` |
| `scneventsEquipItemToPerformer` | 2 | 354 / 117 | `/Data/RootChunk/sceneGraph/Data/graph/19/Data/events/5` |
| `scneventsSetAnimFeatureEvent` | 6 | 962 / 259 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/19` |
| `scneventsSocket` | 42 | 299 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |
| `scneventsUnequipItemFromPerformer` | 1 | 962 / 257 | `/Data/RootChunk/sceneGraph/Data/graph/37/Data/events/17` |
| `scneventsVFXEvent` | 8 | 126 / 43 | `/Data/RootChunk/sceneGraph/Data/graph/12/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 15
- skeletal_animation, gaze, socket_signal: 2
- speech, vfx: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, props_equipment, vfx, socket_signal: 1
- speech, skeletal_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, props_equipment, vfx, socket_signal: 1
- speech, socket_signal: 1
- speech, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, ik, props_equipment, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, audio, vfx, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze: 1
- speech, gaze: 1
- skeletal_animation, props_equipment, socket_signal: 1
- skeletal_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1

Raw SHA-256: `34df0e8750efb4a4da2c91e5d0612fe8bec84f57eb795eae24493275271a5de1`. Binary SHA-256: `1d0f7fed260007c5f0e607dafbff3d99bdf1cab2e6c5d9744478fedc8d90d61e`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q114\scenes\q114_08_morning.scene" --events
```

## `base\quest\main_quests\part1\q114\scenes\q114_09_convoy.scene`

212 graph nodes, 195 edges; 40 event-bearing sections, 229 events; 133 screenplay lines, 1 screenplay options, 1 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); Teddy (actor 2, spawnSet); Bob (actor 3, spawnSet); Carol (actor 4, spawnSet); Cassidy (actor 5, spawnSet); Mitch (actor 6, spawnSet); Crash_Drone_001 (actor 7, community); Crash_Drone_002 (actor 8, community); Militech_Security_Broadcast (actor 9, spawnDespawn); DRONETOWER (actor 10, spawner); Panam_Panzer (actor 11, spawnSet); Truck (actor 12, community); V (actor 13, findInContext).

Entries: `q114_09_panzer_ciritical_cond_in` → 1785; `q114_09_militech_attacks_in` → 1791; `q114_09_sniper_rifle2_in` → 1813; `q114_09_bobs_dead_in` → 806; `q114_09_fix_panzer_start_in` → 568; `q114_09_santiago_shot_in` → 97; `q114_09_gate_in` → 135; `DO NOT ATTACH - PANZER ENTRY` → 1923; `q114_09_gate_destroyed_in` → 140; `q114_09_jammer_detach_in` → 412; `q114_09_patrolled_area_in` → 417; `q114_09_entrance_drones_defeated_in` → 422; `q114_09_follow_002_in` → 946; `q114_09_fluff_chat_001_in` → 453; `Start 55` → 2251; `DO_NOT_ATTACH_001` → 1748; `q114_09_follow_001_in` → 480; `q114_09_follow_003_in` → 485; `q114_09_mitch_about_combat_in` → 1768; `q114_09_militech_warning_in` → 1770; `q114_09_sniper_rifle_banter1_in` → 1772; `q114_09_barrier_crossed_in` → 497; `q114_09_fluff_chat_002_in` → 1013; `Start 56` → 2544; `q114_09_fluff_chat_003_in` → 1015; `DO_NOT_CONNECT` → 2036; `q114_09_drones_approach2_in` → 1782; `q114_09_drones_approach1_in` → 1783; `fx_test` → 3059; `q114_09_bridge_blockade_info_in` → 1784.

Exits: `q114_09_militech_attacks_out` → 1792; `q114_09_sniper_rifle_banter_out` → 1796; `q114_09_drones_approach1_out` → 1798; `q114_09_drones_approach2_out` → 1799; `q114_09_bridge_blockade_info_out` → 1800; `q114_09_panzer_ciritical_cond_out` → 1801; `q114_09_sniper_rifle2_out` → 1814; `q114_09_bobs_dead_out` → 809; `q114_09_fix_end_out` → 598; `q114_09_santiago_shot_out` → 99; `q114_09_gate_out` → 138; `q114_09_gate_destroyed_out` → 143; `q114_09_jammer_detach_out` → 414; `q114_09_patrolled_area_out` → 419; `q114_09_entrance_drones_defeated_out` → 424; `q114_09_follow_001_out` → 944; `q114_09_fluff_chat_001_out` → 454; `q114_09_follow_002_out` → 481; `q114_09_follow_003_out` → 487; `q114_09_barrier_crossed_out` → 498; `q114_09_mitch_about_combat_out` → 1778; `q114_09_fluff_chat_002_out` → 1014; `q114_09_militech_warning_out` → 1780; `q114_09_fluff_chat_003_out` → 1016.

End nodes: 99: `<omitted>`; 138: `<omitted>`; 143: `<omitted>`; 414: `<omitted>`; 419: `<omitted>`; 424: `<omitted>`; 454: `<omitted>`; 481: `<omitted>`; 487: `<omitted>`; 498: `<omitted>`; 598: `NonTerminating`; 809: `<omitted>`; 944: `<omitted>`; 1014: `<omitted>`; 1016: `<omitted>`; 1778: `<omitted>`; 1780: `<omitted>`; 1792: `<omitted>`; 1796: `<omitted>`; 1798: `<omitted>`; 1799: `<omitted>`; 1800: `<omitted>`; 1801: `<omitted>`; 1814: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 6 | 1058 / 271 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/7` |
| `scnChangeIdleAnimEvent` | 4 | 1058 / 265 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/4` |
| `scnDialogLineEvent` | 125 | 98 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 1058 / 262 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/3` |
| `scnGameplayTransitionEvent` | 1 | 1917 / 522 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/31` |
| `scnIKEvent` | 2 | 1917 / 500 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/10` |
| `scnLookAtEvent` | 1 | 557 / 83 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/4` |
| `scnPlaySkAnimEvent` | 12 | 557 / 79 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/2` |
| `scneventsAttachPropToPerformer` | 1 | 1058 / 260 | `/Data/RootChunk/sceneGraph/Data/graph/65/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 4 | 1917 / 518 | `/Data/RootChunk/sceneGraph/Data/graph/117/Data/events/28` |
| `scneventsSocket` | 26 | 557 / 88 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/7` |
| `scneventsVFXEvent` | 46 | 557 / 78 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 31
- speech, socket_signal: 2
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, skeletal_animation, idle_animation, props_equipment, audio, vfx, socket_signal, gameplay_action: 1
- speech, skeletal_animation, socket_signal: 1
- speech, vfx: 1
- speech, skeletal_animation, idle_animation, ik, audio, vfx, gameplay_transition, socket_signal, animation_state: 1
- skeletal_animation, idle_animation, audio, vfx, socket_signal, animation_state: 1
- socket_signal, animation_state: 1

Raw SHA-256: `ce16c3679761b083e5248dca2827563354530c963da2190ea2189f3021299af9`. Binary SHA-256: `96e3955417878bba92fb0a6b36e89af622d0c3417f1072cada28fc71ccb55e71`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q114\scenes\q114_09_convoy.scene" --events
```

## `base\quest\main_quests\part1\q114\scenes\q114_09a_construction.scene`

378 graph nodes, 364 edges; 65 event-bearing sections, 215 events; 153 screenplay lines, 5 screenplay options, 3 choice nodes.

Actors: Saul (actor 0, spawnSet); Panam (actor 1, spawnSet); Mitch (actor 2, spawnSet); Cassidy (actor 3, spawnSet); Carol (actor 4, spawnSet); Teddy (actor 5, spawnSet); Johnny (actor 6, spawnSet); Bob (actor 7, spawnSet); mech_001 (actor 8, community); mech_002 (actor 9, community); mech_003 (actor 10, community); mech_004 (actor 11, community); response_av_guard_001 (actor 12, community); response_av_guard_002 (actor 13, community); response_av_guard_003 (actor 14, community); response_av_guard_004 (actor 15, community); response_av_guard_005 (actor 16, community); drop_av_001 (actor 17, community); drop_av_002 (actor 18, community); construction_drop_av_001 (actor 19, spawner); panzer (actor 20, spawnSet); V (actor 21, findInContext).

Entries: `____tanks_unused` → 1666; `q114_09_av_in` → 7; `q114_09_civilian_in` → 13; `q114_09_civilian_dead_in` → 16; `q114_09_av_squad_in` → 19; `q114_09_tunnel_shot_in` → 35; `DONOTUSE__01` → 872; `DONOTUSE__02` → 879; `DONOTUSE__03` → 885; `q114_09a_parked_in` → 62; `q114_09a_hackers_in_place_in` → 69; `q114_09a_response_team_in` → 74; `q114_09a_response_beta_in` → 80; `q114_09a_response_gamma_in` → 86; `q114_missiles_in` → 101; `q114_09a_all_done_in` → 107; `q114_09_av_close_in` → 1772; `q114_09a_response_inbound_in` → 957; `q114_09a_gate_destruction_in` → 984; `q114_09a_tanks_approach_in` → 593; `q114_09a_tanks_drilling_update_in` → 611; `q114_09a_tank_downed_in` → 620; `q114_09a_tanks_defeated_in` → 638; `q114_09a_leaving_construction_in` → 650; `q114_09a_panzer_hit_in` → 659; `q114_09a_panzer_imminent_failure_in` → 676; `q114_mech_death_anims` → 3593; `q114_09a_chat_on_return_in` → 688; `q114_09a_entering_construction_in` → 693; `q114_09a_enter_prompt_in` → 705; `q114_09a_panzer_repairs_start_in` → 743; `q114_09a_panam_panzer_repair_update_in` → 751; `q114_09a_tank_squadron_prompt_in` → 753; `q114_09a_ThorDrop_in` → 1182; `q114_09_breached_in` → 413.

Exits: `q114_09a_gate_destruction_out` → 1664; `q114_09_av_out` → 9; `q114_09_civilian_out` → 15; `q114_09_civilian_dead_out` → 17; `q114_09_av_squad_out` → 21; `q114_09_tunnel_shot_out` → 37; `q114_09a_parked_out` → 64; `q114_09a_hackers_in_place_out` → 71; `q114_09a_response_team_out` → 76; `q114_09a_response_beta_out` → 83; `q114_09a_response_gamma_out` → 88; `q114_09a_all_done_out` → 109; `q114_09a_response_inbound_out` → 958; `q114_guard_02_done_out` → 3502; `q114_guard_03_done_out` → 3503; `q114_guard_04_done_out` → 3504; `q114_guard_05_done_out` → 3505; `q114_09a_tanks_approach_out` → 595; `q114_09a_tanks_drilling_update_out` → 613; `q114_09a_tank_downed_out` → 622; `q114_09a_tanks_defeated_out` → 640; `q114_09a_leaving_construction_out` → 652; `q114_09a_panzer_hit_out` → 661; `q114_09a_panzer_imminent_failure_out` → 678; `q114_09a_chat_on_return_out` → 689; `q114_09a_entering_construction_out` → 694; `q114_09a_enter_prompt_out` → 706; `q114_09a_ThorDrop_out` → 1561; `q114_09a_panzer_repairs_start_out` → 744; `q114_09a_leaving_construction_boarded_out` → 3657; `q114_09a_panam_panzer_repair_update_out` → 752; `q114_09a_tank_squadron_prompt_out` → 754.

End nodes: 9: `NonTerminating`; 15: `<omitted>`; 17: `<omitted>`; 21: `<omitted>`; 37: `<omitted>`; 64: `<omitted>`; 71: `NonTerminating`; 76: `<omitted>`; 83: `<omitted>`; 88: `<omitted>`; 109: `<omitted>`; 595: `<omitted>`; 613: `<omitted>`; 622: `<omitted>`; 640: `<omitted>`; 652: `<omitted>`; 661: `<omitted>`; 678: `<omitted>`; 689: `<omitted>`; 694: `<omitted>`; 706: `<omitted>`; 744: `<omitted>`; 752: `<omitted>`; 754: `<omitted>`; 958: `<omitted>`; 1561: `NonTerminating`; 1664: `<omitted>`; 3502: `NonTerminating`; 3503: `NonTerminating`; 3504: `NonTerminating`; 3505: `NonTerminating`; 3657: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 3 | 731 / 503 | `/Data/RootChunk/sceneGraph/Data/graph/113/Data/events/6` |
| `scnChangeIdleAnimEvent` | 11 | 256 / 203 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/1` |
| `scnDialogLineEvent` | 126 | 241 / 193 | `/Data/RootChunk/sceneGraph/Data/graph/44/Data/events/0` |
| `scnGameplayActionEvent` | 1 | 256 / 200 | `/Data/RootChunk/sceneGraph/Data/graph/47/Data/events/0` |
| `scnGameplayTransitionEvent` | 1 | 731 / 505 | `/Data/RootChunk/sceneGraph/Data/graph/113/Data/events/8` |
| `scnIKEvent` | 2 | 731 / 496 | `/Data/RootChunk/sceneGraph/Data/graph/113/Data/events/1` |
| `scnLookAtEvent` | 12 | 293 / 247 | `/Data/RootChunk/sceneGraph/Data/graph/52/Data/events/0` |
| `scnPlaySkAnimEvent` | 23 | 259 / 209 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/0` |
| `scnUnmountEvent` | 1 | 731 / 510 | `/Data/RootChunk/sceneGraph/Data/graph/113/Data/events/12` |
| `scneventsSetAnimFeatureEvent` | 2 | 419 / 280 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/1` |
| `scneventsSocket` | 23 | 259 / 219 | `/Data/RootChunk/sceneGraph/Data/graph/48/Data/events/5` |
| `scneventsVFXEvent` | 10 | 419 / 279 | `/Data/RootChunk/sceneGraph/Data/graph/58/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 44
- skeletal_animation: 4
- speech, socket_signal: 3
- speech, gaze: 2
- skeletal_animation, socket_signal: 2
- skeletal_animation, idle_animation, audio, vfx, socket_signal: 2
- idle_animation: 2
- speech, idle_animation, gameplay_action: 1
- speech, skeletal_animation, idle_animation, socket_signal: 1
- speech, skeletal_animation, idle_animation, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- vfx: 1

Raw SHA-256: `0d6f6fff85c7d529a33b418fa7dc02b41d3e8d404f74491b7c6f1cde72d57dec`. Binary SHA-256: `e232b1af5ceb914c780474e3e7c83a705c97aee559a72bc0eae2e24293267826`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q114\scenes\q114_09a_construction.scene" --events
```

## `base\quest\main_quests\part1\q114\scenes\q114_10_tunnel.scene`

31 graph nodes, 36 edges; 14 event-bearing sections, 116 events; 57 screenplay lines, 8 screenplay options, 3 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); Johnny (actor 2, spawnSet); Bob (actor 3, spawnSet); Teddy (actor 4, spawnSet); Cassidy (actor 5, spawnSet); Mitch (actor 6, spawnSet); Carol (actor 7, findInContext); panzer (actor 8, spawnSet); V (actor 9, findInContext).

Entries: `q114_10_tunnel_start_in` → 109; `q114_10_tunnel_talk_in` → 207.

Exits: `q114_10_tunnel_talk_out` → 387; `q114_10_tunnel_start_out` → 112.

End nodes: 112: `NonTerminating`; 387: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnChangeIdleAnimEvent` | 10 | 212 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/6/Data/events/4` |
| `scnDialogLineEvent` | 56 | 110 / 5 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/0` |
| `scnLookAtEvent` | 20 | 208 / 35 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/7` |
| `scnPlaySkAnimEvent` | 15 | 208 / 25 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scneventsSetAnimFeatureEvent` | 3 | 110 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/2` |
| `scneventsSocket` | 11 | 110 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/3` |
| `scneventsVFXEvent` | 1 | 110 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/1/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze: 4
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 3
- speech: 2
- speech, skeletal_animation: 2
- speech, vfx, socket_signal, animation_state: 1
- speech, skeletal_animation, gaze, socket_signal, animation_state: 1
- speech, skeletal_animation, socket_signal: 1

Raw SHA-256: `167626ee11720b25421f4debe4e76239e33f4d557b01f862f139d78391c33894`. Binary SHA-256: `58ad0dd9d38b815989b3b8a865b55b1c3e3383fd30f7a28287502f0b4457c1c0`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q114\scenes\q114_10_tunnel.scene" --events
```

## `base\quest\main_quests\part1\q114\scenes\q114_10_tunnel_driller.scene`

237 graph nodes, 258 edges; 31 event-bearing sections, 456 events; 82 screenplay lines, 5 screenplay options, 4 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); Johnny (actor 2, spawnSet); Bob (actor 3, spawnSet); Teddy (actor 4, spawnSet); Cassidy (actor 5, spawnSet); Mitch (actor 6, spawnSet); Carol (actor 7, spawnDespawn); panzer (actor 8, spawnSet); V (actor 9, findInContext).

Entries: `q114_10_intersection_in` → 260; `Start 33` → 1673; `Start 29` → 1520; `Start 37` → 2162; `Start 36` → 2005; `ALWAYS CONNECT NODES WITH TXT TO SOME INPUT` → 1603; `q114_10_reminder_haul_ass_in` → 1605.

Exits: `q114_10_reminder_haul_ass_out` → 1608; `q114_10_to_droid_spawn_out` → 2268; `q114_10_enter_hole_out` → 288; `q114_driller_end_terminatig` → 1587.

End nodes: 288: `NonTerminating`; 1587: `<omitted>`; 1608: `<omitted>`; 2268: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 5 | 733 / 202 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/20` |
| `scnChangeIdleAnimEvent` | 29 | 343 / 10 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/4` |
| `scnDialogLineEvent` | 76 | 343 / 9 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/3` |
| `scnGameplayTransitionEvent` | 9 | 343 / 65 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/34` |
| `scnIKEvent` | 18 | 343 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/28` |
| `scnLookAtEvent` | 60 | 343 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnPlaySkAnimEvent` | 94 | 343 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/6` |
| `scnUnmountEvent` | 9 | 343 / 70 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/38` |
| `scneventsSetAnimFeatureEvent` | 9 | 343 / 67 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/36` |
| `scneventsSocket` | 81 | 343 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/5` |
| `scneventsVFXDurationEvent` | 12 | 733 / 166 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/0` |
| `scneventsVFXEvent` | 54 | 733 / 167 | `/Data/RootChunk/sceneGraph/Data/graph/9/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8
- speech, skeletal_animation, idle_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 4
- skeletal_animation, socket_signal: 4
- speech, skeletal_animation, idle_animation, audio, vfx, socket_signal: 1
- speech, skeletal_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, audio, vfx, socket_signal: 1
- speech, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, gaze: 1
- speech, skeletal_animation, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- speech, skeletal_animation, gaze, vfx, socket_signal: 1
- speech, socket_signal: 1
- skeletal_animation, gaze: 1
- skeletal_animation: 1
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, idle_animation: 1

Raw SHA-256: `42e8d865054b6657f5d49956b799953da7c7b474673ca3f9c8726c13945895dd`. Binary SHA-256: `217662812e309db9915c9271e16ed6bfb9091d501e69e2ef024b70826cc5bc64`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q114\scenes\q114_10_tunnel_driller.scene" --events
```

## `base\quest\main_quests\part1\q114\scenes\q114_10a_dampening_area.scene`

24 graph nodes, 20 edges; 5 event-bearing sections, 21 events; 14 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Panam (actor 0, spawnSet); Cassidy (actor 1, spawnSet); Mitch (actor 2, spawnSet); Saul (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `q114_10a_dampening_enter_in` → 1; `q114_10a_shaft_found_in` → 7; `q114_10a_drone_callouts_In` → 60; `q114_10a_shaft_mid_in` → 12; `q114_10a_sickness_after_ladder_in` → 161.

Exits: `q114_10a_dampening_enter_out` → 2; `q114_10a_shaft_found_out` → 8; `q114_10a_shaft_mid_out` → 13; `q114_10a_drone_callouts_Out` → 67; `q114_10a_sickness_after_ladder_out` → 166.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 13: `<omitted>`; 67: `<omitted>`; 166: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 14 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scnLookAtEvent` | 7 | 4 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, gaze: 1

Raw SHA-256: `38febc1e08dd652abe6345ae50fdae70ed0f7bbdfe26b6096acc11e405ceb945`. Binary SHA-256: `e4526441df5e72dad1f1bf5f73132f0984a952ad698351b217f536b08c7fd267`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q114\scenes\q114_10a_dampening_area.scene" --events
```

## `base\quest\main_quests\part1\q114\scenes\q114_11_arasaka_manufacturing_infiltration.scene`

219 graph nodes, 252 edges; 42 event-bearing sections, 291 events; 80 screenplay lines, 7 screenplay options, 3 choice nodes.

Actors: Panam (actor 0, spawnSet); Saul (actor 1, spawnSet); V (actor 2, findInContext).

Entries: `q114_11_orientation_in` → 7; `q114_11_combat_start_in` → 17; `q114_11_combat_cleared_in` → 22; `q114_11_rejoin_in_sluice_in` → 52; `q114_11_lockdown_lifted_in` → 57; `Debug_q114_11_arrived_in` → 481; `q114_11_reminder_kill_guards_in` → 485; `q114_11_arrived_in` → 67; `q114_11_dropping_fools_in` → 82; `q114_11_lockdown_console_prompt_in` → 295; `q114_11_disabling_lights_in` → 88; `q114_11_lockdown_console_scanned_in` → 300; `q114_11_distraction_prompt_in` → 93; `q114_11_everyones_dead_in` → 524; `q114_11_stealth_after_lockdown_in` → 106; `q114_11_reminder_proceed_to_nest_in` → 531; `q114_11_solo_door_in` → 155.

Exits: `q114_11_orientation_combat_out` → 8; `q114_11_combat_start_out` → 18; `q114_11_combat_cleared_out` → 23; `q114_11_rejoin_in_sluice_out` → 53; `q114_11_lockdown_lifted_out` → 58; `q114_11_arrived_out` → 68; `q114_11_orientation_stealth_out` → 292; `q114_11_dropping_fools_out` → 83; `q114_11_lockdown_console_prompt_out` → 296; `q114_11_disabling_lights_out` → 89; `q114_11_lockdown_console_scanned_out` → 301; `q114_11_distraction_prompt_out` → 94; `q114_11_everyones_dead_out` → 526; `q114_11_stealth_after_lockdown_out` → 107; `q114_11_solo_door_out` → 157.

End nodes: 8: `<omitted>`; 18: `<omitted>`; 23: `<omitted>`; 53: `<omitted>`; 58: `<omitted>`; 68: `NonTerminating`; 83: `<omitted>`; 89: `<omitted>`; 94: `<omitted>`; 107: `<omitted>`; 157: `<omitted>`; 292: `<omitted>`; 296: `<omitted>`; 301: `<omitted>`; 526: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 2 | 119 / 123 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/6` |
| `scnChangeIdleAnimEvent` | 5 | 69 / 30 | `/Data/RootChunk/sceneGraph/Data/graph/15/Data/events/1` |
| `scnDialogLineEvent` | 63 | 19 / 12 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/2` |
| `scnGameplayTransitionEvent` | 5 | 237 / 305 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/33` |
| `scnIKEvent` | 10 | 237 / 301 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/29` |
| `scnLookAtEvent` | 85 | 19 / 11 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/1` |
| `scnPlaySkAnimEvent` | 74 | 19 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/4/Data/events/0` |
| `scnUnmountEvent` | 5 | 237 / 309 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/36` |
| `scneventsCameraParamsEvent` | 2 | 1538 / 1317 | `/Data/RootChunk/sceneGraph/Data/graph/208/Data/events/0` |
| `scneventsSetAnimFeatureEvent` | 5 | 237 / 307 | `/Data/RootChunk/sceneGraph/Data/graph/41/Data/events/35` |
| `scneventsSocket` | 35 | 119 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/28/Data/events/5` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, gaze: 12
- speech, skeletal_animation, gaze, socket_signal: 6
- speech: 5
- skeletal_animation, gaze: 3
- speech, skeletal_animation, gaze, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- speech, skeletal_animation: 2
- skeletal_animation, gaze, socket_signal: 2
- skeletal_animation, ik, gameplay_transition, socket_signal, animation_state, mount_workspot: 2
- camera: 2
- speech, skeletal_animation, idle_animation: 1
- speech, skeletal_animation, idle_animation, gaze, audio, socket_signal: 1
- speech, gaze, socket_signal: 1
- skeletal_animation, gaze, ik, audio, gameplay_transition, socket_signal, animation_state, mount_workspot: 1
- skeletal_animation, socket_signal: 1
- skeletal_animation, idle_animation, gaze: 1

Raw SHA-256: `5a7865d49a3ffe8a34adde594f75e5ca4ffb6c28afb55dca354a2f238e9934e9`. Binary SHA-256: `8177fdda894e5febe631d376d8b6b9f747524aa8f598fc8b6c3f230167fa0908`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q114\scenes\q114_11_arasaka_manufacturing_infiltration.scene" --events
```

## `base\quest\main_quests\part1\q114\scenes\q114_11_arasaka_manufacturing_mood_scenes.scene`

25 graph nodes, 19 edges; 8 event-bearing sections, 28 events; 28 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: topfloor_guard_001 (actor 0, community); cargocrew_guard_001 (actor 1, community); pa_system (actor 2, findInContext); lockdown_guard (actor 3, community); topfloor_guard_002 (actor 4, community); cargocrew_guard_002 (actor 5, community); groundfloor_back_guard (actor 6, community); groundfloor_side_guard (actor 7, community); Player (actor 8, findInContext).

Entries: `q114_11_first_floor_ctrl_in` → 1; `q114_11_lockdown_reminder_in` → 27; `q114_11_cargo_group_in` → 7; `q114_11_cargo_leaving_in` → 37; `q114_11_mood_groundfloor_back_in` → 12; `q114_11_mood_groundfloor_side_in` → 17; `q114_11_lockdown_guard_in` → 47; `q114_11_lockdown_lifted_in` → 22.

Exits: `q114_11_first_floor_ctrl_out` → 2; `q114_11_lockdown_reminder_out` → 28; `q114_11_cargo_group_out` → 8; `q114_11_cargo_leaving_out` → 38; `q114_11_mood_groundfloor_back_out` → 13; `q114_11_mood_groundfloor_side_out` → 18; `q114_11_lockdown_guard_out` → 48; `q114_11_lockdown_lifted_out` → 23.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 13: `<omitted>`; 18: `<omitted>`; 23: `<omitted>`; 28: `<omitted>`; 38: `<omitted>`; 48: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 28 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 8

Raw SHA-256: `64ad26d6e9099ed8bfb0582d9a15ed443465e8f92e8608390adbb8df4b818608`. Binary SHA-256: `93eb2ad78982e8c4d283edccee7382fc07b95bc10a6ee7e36c5e408f6d86f9e8`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q114\scenes\q114_11_arasaka_manufacturing_mood_scenes.scene" --events
```

## `base\quest\main_quests\part1\q114\scenes\q114_12_netrunners_nest_infiltration.scene`

29 graph nodes, 20 edges; 8 event-bearing sections, 57 events; 27 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Panam (actor 0, spawnSet); Johnny (actor 1, spawnSet); Alt (actor 2, findInContext); Saul (actor 3, spawnSet); V (actor 4, findInContext).

Entries: `q114_12_car_comment_in` → 361; `DO_NOT_CONNECT` → 453; `q114_12_mech_shootout_comment_in` → 366; `q114_12_nest_mainchamber_addon_in` → 457; `q114_12_nest_outro_in` → 371; `q114_12_nest_mainchamber_in` → 376; `q114_12_reminder_open_door_in` → 380; `q114_12_netrunners_intro_in` → 353; `q114_12_drone_kill_comment_in` → 355.

Exits: `q114_12_car_comment_out` → 362; `q114_12_mech_shootout_comment_out` → 367; `q114_12_nest_mainchamber_addon_out` → 458; `q114_12_nest_outro_out` → 372; `q114_12_nest_mainchamber_out` → 377; `q114_12_netrunners_intro_out` → 354; `q114_12_drone_kill_comment_out` → 356.

End nodes: 354: `<omitted>`; 356: `<omitted>`; 362: `<omitted>`; 367: `<omitted>`; 372: `<omitted>`; 377: `<omitted>`; 458: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 25 | 350 / 7 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/1` |
| `scnLookAtEvent` | 22 | 350 / 8 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/2` |
| `scnPlaySkAnimEvent` | 10 | 350 / 4 | `/Data/RootChunk/sceneGraph/Data/graph/0/Data/events/0` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 5
- speech, skeletal_animation, gaze: 2
- speech, gaze: 1

Raw SHA-256: `b1108c9e97490489f1c964e9047dfdc3171967f773d37e6a63c7dec82a438484`. Binary SHA-256: `ab933456923a424b58951cdab7acb67995ccead309ef1229784b7900b7278866`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q114\scenes\q114_12_netrunners_nest_infiltration.scene" --events
```

## `base\quest\main_quests\part1\q114\scenes\q114_12_netrunners_nest_mood_scenes.scene`

16 graph nodes, 11 edges; 5 event-bearing sections, 19 events; 18 screenplay lines, 0 screenplay options, 0 choice nodes.

Actors: Scene_001_Grunt_001 (actor 0, community); Scene_001_Grunt_002 (actor 1, community); Scene_002_Grunt_001 (actor 2, community); Scene_002_Grunt_002 (actor 3, community); Scene_003_Tech_001 (actor 4, community); Scene_Shooting_Guard (actor 5, community); Scene_Shooting_Runner (actor 6, community).

Entries: `q114_12_operator_raises_alarm_in` → 17; `q114_12_mood_scene_001_in` → 1; `q114_12_mood_scene_002_in` → 7; `q114_12_covering_fire_in` → 28; `q114_12_mood_scene_003_in` → 12.

Exits: `q114_12_covering_run_out` → 48; `q114_12_operator_raises_alarm_out` → 18; `q114_12_mood_scene_001_out` → 2; `q114_12_mood_scene_002_out` → 8; `q114_12_covering_fire_out` → 29; `q114_12_mood_scene_003_out` → 13.

End nodes: 2: `<omitted>`; 8: `<omitted>`; 13: `<omitted>`; 18: `<omitted>`; 29: `<omitted>`; 48: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 18 | 4 / 6 | `/Data/RootChunk/sceneGraph/Data/graph/2/Data/events/0` |
| `scneventsSocket` | 1 | 30 / 34 | `/Data/RootChunk/sceneGraph/Data/graph/14/Data/events/1` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 4
- speech, socket_signal: 1

Raw SHA-256: `48fed0a3a856432309c2f093b2cf7bf4a31f7c61dfa64c50ba5dba24795a91d6`. Binary SHA-256: `e5c4b1d655e4dbf0ea74ea3acf824f161a962c92c5a1282a2bc3a8015b6a1b0d`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q114\scenes\q114_12_netrunners_nest_mood_scenes.scene" --events
```

## `base\quest\main_quests\part1\q114\scenes\q114_13_alt_plugged_in.scene`

44 graph nodes, 57 edges; 6 event-bearing sections, 71 events; 19 screenplay lines, 4 screenplay options, 3 choice nodes.

Actors: Panam (actor 0, spawnSet); Cassidy (actor 1, spawnSet); Mitch (actor 2, spawnSet); Alt (actor 3, findInContext); Net_01 (actor 4, community); Net_02 (actor 5, community); Net_03 (actor 6, community); Saul (actor 7, spawnSet); V (actor 8, findInContext).

Entries: `q114_12_alt_inside_in` → 4; `Start 3` → 568.

Exits: `q114_12_alt_inside_out` → 6; `q114_13_arasaka_destruction` → 82.

End nodes: 6: `<omitted>`; 82: `NonTerminating`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnAudioEvent` | 1 | 203 / 54 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/3` |
| `scnChangeIdleAnimEvent` | 6 | 203 / 58 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/7` |
| `scnDialogLineEvent` | 17 | 203 / 55 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/4` |
| `scnLookAtEvent` | 20 | 203 / 57 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/6` |
| `scnPlaySkAnimEvent` | 12 | 203 / 50 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/2` |
| `scneventsAttachPropToPerformer` | 1 | 203 / 47 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/0` |
| `scneventsAttachPropToWorld` | 1 | 203 / 59 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/8` |
| `scneventsSocket` | 11 | 203 / 49 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/1` |
| `scneventsVFXDurationEvent` | 2 | 203 / 63 | `/Data/RootChunk/sceneGraph/Data/graph/7/Data/events/12` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech, skeletal_animation, idle_animation, gaze, socket_signal: 2
- speech, skeletal_animation, idle_animation, gaze, props_equipment, audio, vfx, socket_signal: 1
- speech, idle_animation, gaze, socket_signal: 1
- speech, skeletal_animation, idle_animation, gaze: 1
- speech, skeletal_animation, gaze, socket_signal: 1

Raw SHA-256: `c7da86c2e8b8d9be26cc62e5a28bff923be8982876470b09e9e27306867478ff`. Binary SHA-256: `ef13197094e259cbad52a0945c0ded568e26da717f5f279eafeca394b08b6817`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q114\scenes\q114_13_alt_plugged_in.scene" --events
```

## `base\quest\main_quests\part1\q115\scenes\q115_11_netrunners_nest.scene`

138 graph nodes, 128 edges; 21 event-bearing sections, 65 events; 79 screenplay lines, 1 screenplay options, 0 choice nodes.

Actors: Rogue (actor 0, spawnSet); Weyland (actor 1, spawnSet); guard_008 (actor 2, community); operator (actor 3, community); alt (actor 4, spawnDespawn); netrunner_01 (actor 5, community); netrunner_02 (actor 6, community); netrunner_03 (actor 7, community); guard_009 (actor 8, community); arasaka_elevator_ai (actor 9, spawner); guard_shot (actor 10, spawner); V_POSESSED (actor 11, findInContext).

Entries: `q115_elevator_ai_in` → 589; `q115_01_af_nest_in` → 1; `q115_11_spooky_moment_01_in` → 600; `q115_11_spooky_moment_02_in` → 605; `q115_11_spooky_moment_03_in` → 607; `q115_11_spooky_moment_04_in` → 609; `q115_connect_alt_in` → 415; `q115_01_af_kill_in` → 220; `q115_solo_in` → 1204; `q115_01_rogue_start_brief` → 424; `q115_01_af_nest_brief_control_room` → 430; `q115_11_guard_shot_in` → 627; `q115_01_af_nest_brief_alt` → 437; `q115_01_af_nest_access_granted` → 443; `q115_rogue_nest_start_warning` → 448; `q115_get_to_nest_floor_in` → 454; `q115_nest_banter_walkway_in` → 459; `q115_nest_banter_room_in` → 465; `q115_nest_banter_turret_in` → 470; `q115_nest_banter_engineers_in` → 475; `q115_nest_banter_patrols_in` → 480; `q115_11_alt_in_elevator_in` → 687; `q115_nest_overheat_in` → 495; `q114_11_alt_reminder_in` → 897; `spotted_combat_in` → 507; `q115_11_riding_down_long_elevator_in` → 518; `q115_01_af_see_nest_in` → 136; `q115_nest_defeated_everyone_in` → 531; `q115_01_af_glass_in` → 164; `q115_11_NPC_to_gate_in` → 957; `q115_11_netrunners_in` → 568.

Exits: `q115_elevator_ai_out` → 590; `q115_11_spooky_moment_01_out` → 601; `q115_11_spooky_moment_02_out` → 606; `q115_11_spooky_moment_03_out` → 608; `q115_11_spooky_moment_04_out` → 610; `q115_solo_out` → 1205; `q115_11_guard_shot_out` → 631; `q115_rogue_nest_start_warning_end` → 452; `q115_get_to_nest_floor_out` → 455; `q115_nest_banter_walkway_out` → 460; `q115_11_alt_in_elevator_out` → 688; `q114_11_alt_reminder_out` → 898; `spotted_combat_out` → 508; `q115_11_riding_down_long_elevator_out` → 519; `solo_open_door` → 759; `q115_11_NPC_elevator_out` → 958.

End nodes: 452: `<omitted>`; 455: `<omitted>`; 460: `<omitted>`; 508: `<omitted>`; 519: `<omitted>`; 590: `NonTerminating`; 601: `<omitted>`; 606: `<omitted>`; 608: `<omitted>`; 610: `<omitted>`; 631: `<omitted>`; 688: `<omitted>`; 759: `NonTerminating`; 898: `<omitted>`; 958: `<omitted>`; 1205: `<omitted>`. Omitted types are not inferred.

Stored interruption scenarios: 1. Their presence alone does not prove a complete interruption/return lifecycle.

| Event type | Count | Example section / event handle | Raw source pointer |
| --- | ---: | --- | --- |
| `scnDialogLineEvent` | 43 | 450 / 14 | `/Data/RootChunk/sceneGraph/Data/graph/10/Data/events/0` |
| `scnLookAtEvent` | 7 | 522 / 66 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/0` |
| `scnPlaySkAnimEvent` | 9 | 522 / 68 | `/Data/RootChunk/sceneGraph/Data/graph/32/Data/events/2` |
| `scneventsSocket` | 4 | 588 / 126 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/7` |
| `scneventsVFXEvent` | 2 | 588 / 122 | `/Data/RootChunk/sceneGraph/Data/graph/39/Data/events/3` |

Presentation families coexisting in an event section (counts are sections, not durations):

- speech: 13
- speech, skeletal_animation, gaze: 2
- speech, socket_signal: 2
- skeletal_animation: 2
- speech, gaze, vfx, socket_signal: 1
- skeletal_animation, socket_signal: 1

Raw SHA-256: `3c95461441f6d97125fefa9442df054dcdc65eb9324f40382f5f64d44b30e43a`. Binary SHA-256: `d3f08ebe4b0138497a0f47c02719f45934fc494ee3efef21b986a784d2138b63`.

Query exact event payloads:

```powershell
py -B tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --resource "base\quest\main_quests\part1\q115\scenes\q115_11_netrunners_nest.scene" --events
```

