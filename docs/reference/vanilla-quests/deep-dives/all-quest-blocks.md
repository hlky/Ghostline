# Expanded source-backed block contracts

These contracts were mined from the structural catalogue. A stored type is evidence for a candidate mechanism, not proof of a complete isolated block or runtime behavior. Counts include explicitly identified repair/dependency context; they are not counts of unique gameplay implementations. See the [cross-quest compositions](cross-quest-patterns.md) and the pilot's [12 lifecycle contracts](building-blocks.md).

## `actor_readiness`

Stored signature: `questCharacterSpawned_ConditionType`. Observed in 328 quest dependency contexts.

**Inputs:** community/entry or actor reference + count policy. **Outputs:** actor available.

Test already-spawned, delayed and missing actors before speech or commands.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h0 / 143 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_06_regroup.scene / scene / 1553; q115_06_regroup.scene / scene / 1688; q115_12b_tower_lobby.scene / scene / 1125 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_openworld.questphase / h1675 / 54 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `actor_route`

Stored signature: `questMovePuppetNodeDefinition`. Observed in 206 quest dependency contexts.

**Inputs:** actor + authored route/spline + movement policy. **Outputs:** movement output.

World navigation is a dependency; test blockage, combat and departure recovery.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_06_regroup.scene / scene / 1743; q115_06_regroup.scene / scene / 1744; q115_06_regroup.scene / scene / 2094 |
| [A Cool Metal Fire](all-quests/base-sq031_smack_my_bitch_up.md) | sq031_01d_smack_rogue.scene / scene / 530 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_end.scene / scene / 382; sa_ep1_courier_outro_end.scene / scene / 411; sa_ep1_courier_outro_end.scene / scene / 603 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `braindance`

Stored signature: `scnRewindableSectionNode`. Observed in 8 quest dependency contexts.

**Inputs:** recording/scene + RID and analysis-layer bindings. **Outputs:** playback/analysis outcomes.

RID, seek/rewind, layer events and replay cleanup require separate verification.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [Automatic Love](all-quests/base-q105_dollhouse.md) | q105_07_blackmarket_braindance.scene / scene / 1104; q105_12a_braindance_voodooqueen.scene / scene / 563; q105_12b_braindance_alt.scene / scene / 344 |
| [Disasterpiece](all-quests/base-q105_03_braindance_studio.md) | q105_07_blackmarket_braindance.scene / scene / 1104; q105_12a_braindance_voodooqueen.scene / scene / 563; q105_12b_braindance_alt.scene / scene / 344 |
| [You Know My Name](all-quests/ep1-q303_songbird.md) | q303_06_paradise.scene / scene / 4524 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `call_lifecycle`

Stored signature: `questPhoneManagerNodeDefinition`. Observed in 135 quest dependency contexts.

**Inputs:** contact + call operation + scene ownership. **Outputs:** connection/end state.

Audio filtering is not call connection; test busy, interrupted and ended calls.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_06_regroup.scene / scene / 1021; q115_06_regroup.scene / scene / 1022; q115_06_regroup.scene / scene / 1079 |
| [A Like Supreme](all-quests/base-sq011_concert.md) | sq011_09_nancy_call.scene / scene / 137 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_intro_scene.questphase / h0 / 47; sa_ep1_courier_outro_muammar_dam.scene / scene / 32 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `checkpoint`

Stored signature: `questCheckpointNodeDefinition`. Observed in 309 quest dependency contexts.

**Inputs:** checkpoint scope + save eligibility + debug identity. **Outputs:** checkpoint request.

Inspect SaveLock gates and never infer a successful persisted save from graph dispatch alone.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h0 / 137; ma_wbr_jpn_20_phase.questphase / h0 / 139 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_solo_lobby.questphase / h0 / 169; q115_solo_nest.questphase / h0 / 118; q115_solo_smasher.questphase / h0 / 35 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_intro_scene.questphase / h0 / 136; sa_ep1_courier_outro_openworld.questphase / h0 / 95; sa_ep1_courier_outro_openworld.questphase / h0 / 96 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `choice_gate`

Stored signature: `scnChoiceNode`. Observed in 250 quest dependency contexts.

**Inputs:** choice + eligibility predicates + commit effects. **Outputs:** selected option or defer/interruption.

Keep knowledge, skill eligibility and persistent decision separate; test return to the choice.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q113_13_adam_smasher.scene / scene / 21; q115_06_regroup.scene / scene / 1608; q115_06_regroup.scene / scene / 270 |
| [A Cool Metal Fire](all-quests/base-sq031_smack_my_bitch_up.md) | sq031_00_johnny.scene / scene / 92; sq031_01a_smack_afterlife.scene / scene / 1069; sq031_01a_smack_afterlife.scene / scene / 1073 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_end.scene / scene / 129; sa_ep1_courier_outro_end.scene / scene / 296; sa_ep1_courier_outro_end.scene / scene / 94 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `combat_control`

Stored signature: `questCombatNodeDefinition`. Observed in 167 quest dependency contexts.

**Inputs:** actor + target + combat operation. **Outputs:** command result.

Separate hostility, threat injection, encounter completion and target cleanup.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_06_regroup.scene / scene / 1895; q115_06_regroup.scene / scene / 1896; q115_06_regroup.scene / scene / 2095 |
| [A Cool Metal Fire](all-quests/base-sq031_smack_my_bitch_up.md) | sq031_brawl.questphase / h0 / 50 |
| [Balls to the Wall](all-quests/ep1-mq301_bomb.md) | mq301.questphase / h419 / 22; mq301.questphase / h419 / 23; mq301.questphase / h862 / 23 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `community_lifecycle`

Stored signature: `questCommunityTemplate_NodeType`. Observed in 304 quest dependency contexts.

**Inputs:** community + named entries/phases + ownership. **Outputs:** activated/reactivated/deactivated entries.

Spawn, readiness and safe departure cleanup are separate steps.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h0 / 148; ma_wbr_jpn_20_phase.questphase / h0 / 2; ma_wbr_jpn_20_phase.questphase / h105 / 15 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_12b_tower_lobby.scene / scene / 306; q115_12b_tower_lobby.scene / scene / 415; q115_12b_tower_lobby.scene / scene / 592 |
| [Balls to the Wall](all-quests/ep1-mq301_bomb.md) | mq301_02_initiation.questphase / h43 / 10; mq301_02_initiation.scene / scene / 1732; mq301_02_initiation.scene / scene / 1735 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `conditional_route`

Stored signature: `questVarComparison_ConditionType`. Observed in 345 quest dependency contexts.

**Inputs:** fact + exact comparison + branch sockets. **Outputs:** selected branch.

Fact dependencies are not execution edges; identify producers and cancellation.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_holocall_brief.scene / scene / 258; ma_wbr_jpn_20_holocall_brief.scene / scene / 59; ma_wbr_jpn_20_holocall_brief.scene / scene / 61 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q113_13_adam_smasher.scene / scene / 100; q113_13_adam_smasher.scene / scene / 128; q113_13_adam_smasher.scene / scene / 134 |
| [Addicted To Chaos](all-quests/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 34; wst_ep1_04_bugfixing.questphase / h0 / 14; wst_ep1_04_bugfixing.questphase / h31 / 2 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `content_scope`

Stored signature: `questContentTokenManager_NodeType`. Observed in 241 quest dependency contexts.

**Inputs:** owned token source + block/unblock/spawn operation. **Outputs:** scope acquired/released.

Avoid copying broad UnblockAll behavior without an explicit ownership policy.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](all-quests/base-sq031_smack_my_bitch_up.md) | sq031_00_johnny.scene / scene / 331; sq031_motel.questphase / h0 / 292 |
| [A Day In The Life](all-quests/base-mq013_punks.md) | mq013.questphase / h1013 / 27; mq013.questphase / h1013 / 5; mq013.questphase / h695 / 3 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_openworld.questphase / h0 / 722 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `controller_event`

Stored signature: `questEventManagerNodeDefinition`. Observed in 305 quest dependency contexts.

**Inputs:** entity + controller/PS class + typed event. **Outputs:** event dispatched.

Resolve controller ownership and its completion predicate; an event send is not operation success.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h0 / 116; ma_wbr_jpn_20_phase.questphase / h0 / 117; ma_wbr_jpn_20_phase.questphase / h0 / 118 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_06_regroup.scene / scene / 1818; q115_06_regroup.scene / scene / 947; q115_06_regroup.scene / scene / 948 |
| [Addicted To Chaos](all-quests/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 32 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `device_action`

Stored signature: `questDeviceManager_NodeType`. Observed in 242 quest dependency contexts.

**Inputs:** controller class + object + action. **Outputs:** action dispatched.

Bind the matching device completion predicate; dispatch alone is not success.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h105 / 30; ma_wbr_jpn_20_phase.questphase / h105 / 31; ma_wbr_jpn_20_phase.questphase / h105 / 32 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q113_13_adam_smasher.scene / scene / 833; q113_13_adam_smasher.scene / scene / 834; q115_12b_tower_lobby.scene / scene / 961 |
| [Addicted To Chaos](all-quests/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 11; wst_ep1_04.questphase / h0 / 25; wst_ep1_04.questphase / h0 / 27 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `device_state`

Stored signature: `questDevice_ConditionType`. Observed in 198 quest dependency contexts.

**Inputs:** controller class + object + condition function. **Outputs:** device predicate.

Check already-satisfied state and controller persistence across save/load.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h500 / 34 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_12b_tower_lobby.scene / scene / 583; q115_12b_tower_lobby.scene / scene / 587; q115_12d_mikoshi.scene / scene / 3808 |
| [Addicted To Chaos](all-quests/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 37; wst_ep1_04.questphase / h0 / 50 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `elapsed_time`

Stored signature: `questGameTimeDelay_ConditionType`. Observed in 241 quest dependency contexts.

**Inputs:** clock domain + duration + start/reset condition. **Outputs:** elapsed signal.

Compose objective/contact behavior separately; test time skip and save/load.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h105 / 23; ma_wbr_jpn_20_phase.questphase / h105 / 68 |
| [A Like Supreme](all-quests/base-sq011_concert.md) | sq011_concert.questphase / h0 / 146; sq011_concert.questphase / h0 / 178; sq011_messages.questphase / h0 / 61 |
| [Balls to the Wall](all-quests/ep1-mq301_bomb.md) | mq301_02_initiation.questphase / h114 / 13; mq301_02_initiation.questphase / h114 / 6; mq301_02_initiation.questphase / h114 / 8 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `item_state`

Stored signature: `questInventory_ConditionType`. Observed in 173 quest dependency contexts.

**Inputs:** item ID + entity + quantity/comparison. **Outputs:** ownership predicate.

Ownership alone does not prove reading, device interaction or reward delivery.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_06_regroup.scene / scene / 781; q115_12b_tower_lobby.scene / scene / 926; q115_solo_lobby.questphase / h0 / 6 |
| [A Cool Metal Fire](all-quests/base-sq031_smack_my_bitch_up.md) | sq031_01b_smack_tatto.scene / scene / 680; sq031_01b_smack_tatto.scene / scene / 685 |
| [Addicted To Chaos](all-quests/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 24 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `journal_read`

Stored signature: `questJournalEntryVisited_ConditionType`. Observed in 63 quest dependency contexts.

**Inputs:** full journal entry path + visited state. **Outputs:** entry visited.

Verify the actual UI read event in game; keep inventory pickup distinct.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [Automatic Love](all-quests/base-q105_dollhouse.md) | q105_03d_dollhouse_investigation.scene / scene / 893; q105_03d_dollhouse_investigation.scene / scene / 903 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_openworld.questphase / h1675 / 16 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `journal_transition`

Stored signature: `questJournalNodeDefinition`. Observed in 388 quest dependency contexts.

**Inputs:** typed journal operation + exact path + state socket. **Outputs:** journal operation output.

Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | japantown_minor_activities.questphase / h0 / 61; ma_wbr_jpn_20_phase.questphase / h0 / 147; ma_wbr_jpn_20_phase.questphase / h0 / 26 |
| [!OBSOLETE](all-quests/base-tier1.md) | vehicles_metaquest_new.questphase / h3154 / 2; vehicles_metaquest_new.questphase / h3154 / 9; vehicles_metaquest_new.questphase / h3367 / 9 |
| [Addicted To Chaos](all-quests/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 10; wst_ep1_04.questphase / h0 / 14; wst_ep1_04.questphase / h0 / 21 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `loot_binding`

Stored signature: `questInjectLoot_NodeType`. Observed in 106 quest dependency contexts.

**Inputs:** spawned target + item record + operation. **Outputs:** loot injection dispatched.

Wait for target readiness; validate actual loot delivery, pickup and once-only restoration separately.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h0 / 135 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q116_combat_smasher_bossfight.questphase / h1267 / 324; q116_combat_smasher_bossfight.questphase / h1267 / 325; q116_combat_smasher_bossfight.questphase / h1267 / 327 |
| [Addicted To Chaos](all-quests/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 49 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `mount_state`

Stored signature: `questCharacterMount_ConditionType`. Observed in 219 quest dependency contexts.

**Inputs:** parent vehicle/puppet + child + role/event. **Outputs:** mount/unmount condition.

Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](all-quests/base-sq031_smack_my_bitch_up.md) | sq031_01c_smack_striptease.scene / scene / 3205; sq031_01c_smack_striptease.scene / scene / 491; sq031_01c_smack_striptease.scene / scene / 562 |
| [A Day In The Life](all-quests/base-mq013_punks.md) | mq013.questphase / h1131 / 3; mq013.questphase / h265 / 99 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_openworld.questphase / h0 / 552; sa_ep1_courier_outro_openworld.questphase / h2033 / 13; sa_ep1_courier_outro_openworld.questphase / h2033 / 32 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `parallel_join`

Stored signature: `questLogicalAndNodeDefinition`. Observed in 266 quest dependency contexts.

**Inputs:** named branch completion signals + reset policy. **Outputs:** all required inputs observed.

Test either completion order, early events, interruption and save/load at the join.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_combat_lobby.questphase / h26 / 202; q115_combat_lobby.questphase / h26 / 203; q115_combat_lobby.questphase / h26 / 204 |
| [A Cool Metal Fire](all-quests/base-sq031_smack_my_bitch_up.md) | sq031_afterlife.questphase / h0 / 203 |
| [Balls to the Wall](all-quests/ep1-mq301_bomb.md) | mq301.questphase / h419 / 14; mq301_01_fireplace.questphase / h0 / 17; mq301_07_ending.questphase / h0 / 101 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `persistent_decision`

Stored signature: `questSetVar_NodeType`. Observed in 362 quest dependency contexts.

**Inputs:** namespaced fact + explicit write mode/value. **Outputs:** durable state update.

Separate scene-local presentation facts from public outcome state and review omitted defaults.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_holocall_brief.scene / scene / 254; ma_wbr_jpn_20_holocall_brief.scene / scene / 256; ma_wbr_jpn_20_holocall_brief.scene / scene / 60 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q113_13_adam_smasher.scene / scene / 241; q113_13_adam_smasher.scene / scene / 381; q113_13_adam_smasher.scene / scene / 385 |
| [Addicted To Chaos](all-quests/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 1; wst_ep1_04.questphase / h0 / 20; wst_ep1_04.questphase / h0 / 22 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `race_resolution`

Stored signature: `questLogicalXorNodeDefinition`. Observed in 282 quest dependency contexts.

**Inputs:** competing outcome signals + retirement policy. **Outputs:** converged signal.

Review actual graph wiring; an XOR class alone does not prove loser cancellation.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_combat_netrunners_nest.questphase / h90 / 223; q115_combat_netrunners_nest.questphase / h90 / 277; q115_combat_netrunners_nest.questphase / h90 / 278 |
| [A Day In The Life](all-quests/base-mq013_punks.md) | mq013.questphase / h1131 / 33; mq013.questphase / h265 / 6 |
| [Am I Demon?](all-quests/ep1-sts_ep1_08_katya_data_shard.md) | wst_ep1_22.questphase / h0 / 44; wst_ep1_22.questphase / h0 / 45 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `realtime_delay`

Stored signature: `questRealtimeDelay_ConditionType`. Observed in 340 quest dependency contexts.

**Inputs:** real-time duration + cancellation owner. **Outputs:** elapsed signal.

Do not substitute game time for real time; retire delayed effects after cancellation.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h500 / 25; ma_wbr_jpn_20_phase.questphase / h500 / 31 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q113_13_adam_smasher.scene / scene / 141; q113_13_adam_smasher.scene / scene / 144; q113_13_adam_smasher.scene / scene / 152 |
| [Addicted To Chaos](all-quests/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 28; wst_ep1_04.questphase / h0 / 36 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `retire_branch`

Stored signature: `questCutControlNodeDefinition`. Observed in 262 quest dependency contexts.

**Inputs:** owned target branch(es) + permanent/reset policy. **Outputs:** branch retired.

Trace every CutSource destination; cancellation must not commit success.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h0 / 129 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_combat_netrunners_nest.questphase / h90 / 20; q115_combat_netrunners_nest.questphase / h90 / 219; q115_combat_netrunners_nest.questphase / h90 / 275 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_openworld.questphase / h2232 / 46 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `reward_commit`

Stored signature: `questGiveReward_NodeType`. Observed in 324 quest dependency contexts.

**Inputs:** reward record + eligibility + once-only commit. **Outputs:** reward delivered/committed.

Verify inventory/currency and objective state; prevent repeated awards after load.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h0 / 89 |
| [!OBSOLETE](all-quests/base-tier3.md) | vehicles_metaquest_new.questphase / h4724 / 11; vehicles_metaquest_new.questphase / h4921 / 11; vehicles_metaquest_new.questphase / h5118 / 11 |
| [Am I Demon?](all-quests/ep1-sts_ep1_08_katya_data_shard.md) | wst_ep1_22.questphase / h0 / 37; wst_ep1_22.questphase / h0 / 38 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `save_eligibility`

Stored signature: `questSaveLock_ConditionType`. Observed in 51 quest dependency contexts.

**Inputs:** save-lock predicate + fallback path. **Outputs:** save eligibility branch.

Separate blocked-save fallback from checkpoint creation and verify installed behavior.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h0 / 138; ma_wbr_jpn_20_phase.questphase / h0 / 140 |
| [Automatic Love](all-quests/base-q105_dollhouse.md) | ma_wbr_jpn_12_phase.questphase / h0 / 50; ma_wbr_jpn_12_phase.questphase / h0 / 51 |
| [Gig: Talent Academy](all-quests/ep1-sts_ep1_13.md) | sts_ep1_13_openworld.questphase / h2964 / 3; sts_ep1_13_openworld.questphase / h2964 / 6; sts_ep1_13_openworld.questphase / h2964 / 9 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `scan_evidence`

Stored signature: `questScan_ConditionType`. Observed in 123 quest dependency contexts.

**Inputs:** clue reference + exact scan event + required-set policy. **Outputs:** clue observed.

Preserve Started versus Finished, ordering, bypass and reaction joins.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [Automatic Love](all-quests/base-q105_dollhouse.md) | q105_03d_dollhouse_investigation.scene / scene / 876; q105_03d_dollhouse_investigation.scene / scene / 901; q105_04_jigjig_street.scene / scene / 1595 |
| [Belly of the Beast](all-quests/base-q114_03_attack_on_arasaka_tower.md) | q114_arasaka_basement.questphase / h1375 / 22; q114_arasaka_basement.questphase / h17 / 10 |
| [Birds with Broken Wings](all-quests/ep1-q304_stadium.md) | q304_02b_car_rental.questphase / h14 / 132; q304_02b_car_rental.questphase / h540 / 70 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `scene_interface`

Stored signature: `questSceneNodeDefinition`. Observed in 309 quest dependency contexts.

**Inputs:** scene + entry + actor/marker bindings. **Outputs:** named exits and cancellation.

Validate every consumed entry/exit and distinguish terminating from notification outputs.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h0 / 112 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_combat_lobby.questphase / h26 / 190; q115_combat_lobby.questphase / h26 / 192; q115_combat_lobby.questphase / h26 / 194 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | courier_sandbox_activity_bugfixing.questphase / h40 / 5; sa_ep1_courier_outro_ending_scene.questphase / h0 / 84; sa_ep1_courier_outro_intro_scene.questphase / h0 / 6 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `spatial_gate`

Stored signature: `questTriggerCondition`. Observed in 326 quest dependency contexts.

**Inputs:** trigger + activator + exact inside/outside event. **Outputs:** spatial predicate.

Resolve the registered NodeRef and test starting inside, exiting, actor activation and return.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h0 / 111; ma_wbr_jpn_20_phase.questphase / h0 / 29; ma_wbr_jpn_20_phase.questphase / h105 / 22 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q113_13_adam_smasher.scene / scene / 2554; q113_13_adam_smasher.scene / scene / 2583; q113_13_adam_smasher.scene / scene / 2586 |
| [Addicted To Chaos](all-quests/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 13; wst_ep1_04.questphase / h0 / 28 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `target_resolution`

Stored signature: `questCharacterKilled_ConditionType`. Observed in 240 quest dependency contexts.

**Inputs:** target set + lethal/unconscious/defeated policy. **Outputs:** target resolved.

Review RED defaults, early defeat and per-target deduplication before counter joins.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h0 / 115; ma_wbr_jpn_20_phase.questphase / h0 / 30 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q113_13_adam_smasher.scene / scene / 61; q115_06_regroup.scene / scene / 1157; q115_06_regroup.scene / scene / 780 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_openworld.questphase / h4068 / 3 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `vehicle_control`

Stored signature: `questVehicleNodeDefinition`. Observed in 268 quest dependency contexts.

**Inputs:** vehicle reference + typed operation + world route. **Outputs:** operation-specific result.

Vehicle spawning, seats, driving, arrival and cleanup have separate owners.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!OBSOLETE](all-quests/base-tier1.md) | vehicles_metaquest_new.questphase / h3154 / 3 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_06_regroup.scene / scene / 1516 |
| [Addicted To Chaos](all-quests/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 19 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `vehicle_ownership`

Stored signature: `questVehicleAvailable_ConditionType`. Observed in 8 quest dependency contexts.

**Inputs:** vehicle record + reconciliation policy. **Outputs:** availability predicate.

Do not equate purchase eligibility, vehicle availability and journal completion; preserve migration context.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [Blistering Love](all-quests/base-sq031_cinema.md) | sq031_06_rogue_call.scene / scene / 355; sq031_date.questphase / h0 / 472; sq031_date.questphase / h0 / 475 |
| [Burning Desire](all-quests/base-mq012_stud.md) | mq012_00_stud.scene / scene / 1830; mq012_00_stud.scene / scene / 1933 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `weather_scope`

Stored signature: `questPlayEnv_SetWeather`. Observed in 114 quest dependency contexts.

**Inputs:** weather operation + named source + reset policy. **Outputs:** weather request/reset dispatched.

Completion follows the caller's full restoration sequence, not an early cleanup fact.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](all-quests/base-sq031_smack_my_bitch_up.md) | sq031_01a_smack_afterlife.scene / scene / 1136; sq031_01d_smack_rogue.scene / scene / 913 |
| [All Along the Watchtower](all-quests/base-q202_nomads.md) | q202_01_one_for_the_road.questphase / h0 / 57 |
| [Balls to the Wall](all-quests/ep1-mq301_bomb.md) | mq301_02_initiation.scene / scene / 2482; mq301_02_initiation.scene / scene / 2485; mq301_02_initiation.scene / scene / 4330 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `weighted_branch`

Stored signature: `questRandomizerNodeDefinition`. Observed in 115 quest dependency contexts.

**Inputs:** ordered output weights + explicit route bindings. **Outputs:** one authored weighted output.

Preserve output ordering, reset scope and persistence; compose difficulty and timing as separate gates.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_death.questphase / h43 / 88 |
| [Alvarado V4F 570 Delegate](all-quests/base-villefort_alvarado.md) | vehicles_metaquest.questphase / h5186 / 15 |
| [Birds with Broken Wings](all-quests/ep1-q304_stadium.md) | q304_08_escape_both_combaat_reinforcements.questphase / h678 / 56; q304_08_escape_both_combaat_reinforcements.questphase / h7 / 106; q304_08_escape_both_combaat_reinforcements.questphase / h7 / 110 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `workspot_performance`

Stored signature: `questUseWorkspotNodeDefinition`. Observed in 247 quest dependency contexts.

**Inputs:** actor + workspot + entry/exit policy. **Outputs:** work started/success/failure.

Wait for actor/spot readiness and restore AI ownership on interruption.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h500 / 26; ma_wbr_jpn_20_phase.questphase / h500 / 32 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q113_13_adam_smasher.scene / scene / 2318; q113_13_adam_smasher.scene / scene / 2320; q113_13_adam_smasher.scene / scene / 2326 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_end.scene / scene / 379; sa_ep1_courier_outro_end.scene / scene / 386; sa_ep1_courier_outro_end.scene / scene / 388 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `world_variant`

Stored signature: `questTogglePrefabVariant_NodeType`. Observed in 270 quest dependency contexts.

**Inputs:** prefab + variant + desired state + restore policy. **Outputs:** world presentation changed.

Resolve world ownership and restore only this quest's overrides.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [!DUPLICATE](all-quests/base-ma_wbr_jpn_20.md) | ma_wbr_jpn_20_phase.questphase / h105 / 12; ma_wbr_jpn_20_phase.questphase / h105 / 13; ma_wbr_jpn_20_phase.questphase / h105 / 26 |
| [(Don't Fear) The Reaper](all-quests/base-09_solo.md) | q115_06_regroup.scene / scene / 1672; q115_06_regroup.scene / scene / 1691; q115_06_regroup.scene / scene / 1692 |
| [Baby Let Me Take You](all-quests/ep1-courier_outro_dock.md) | sa_ep1_courier_outro_end.scene / scene / 503; sa_ep1_courier_outro_end.scene / scene / 521; sa_ep1_courier_outro_openworld.questphase / h0 / 908 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.
