# Expanded source-backed block contracts

These contracts were mined from the structural catalogue. A stored type is evidence for a candidate mechanism, not proof of a complete isolated block or runtime behavior. Counts include explicitly identified repair/dependency context; they are not counts of unique gameplay implementations. See the [cross-quest compositions](cross-quest-patterns.md) and the pilot's [12 lifecycle contracts](building-blocks.md).

## `actor_readiness`

Stored signature: `questCharacterSpawned_ConditionType`. Observed in 108 quest dependency contexts.

**Inputs:** community/entry or actor reference + count policy. **Outputs:** actor available.

Test already-spawned, delayed and missing actors before speech or commands.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_00_johnny.scene / scene / 369; sq031_00_johnny.scene / scene / 393; sq031_01b_smack_tatto.scene / scene / 346 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1013 / 30; mq013.questphase / h1013 / 31; mq013.questphase / h1013 / 32 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301.questphase / h419 / 67; mq301.questphase / h419 / 71; mq301.questphase / h419 / 87 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `actor_route`

Stored signature: `questMovePuppetNodeDefinition`. Observed in 91 quest dependency contexts.

**Inputs:** actor + authored route/spline + movement policy. **Outputs:** movement output.

World navigation is a dependency; test blockage, combat and departure recovery.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_01d_smack_rogue.scene / scene / 530 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1131 / 23; mq013_00_punks.scene / scene / 1116; mq013_00_punks.scene / scene / 1275 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301_02_initiation.scene / scene / 661; mq301_03_delivery.scene / scene / 10825; mq301_03_delivery.scene / scene / 10837 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `braindance`

Stored signature: `scnRewindableSectionNode`. Observed in 3 quest dependency contexts.

**Inputs:** recording/scene + RID and analysis-layer bindings. **Outputs:** playback/analysis outcomes.

RID, seek/rewind, layer events and replay cleanup require separate verification.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [I Fought the Law](catalogue/base-sq012_lost_girl.md) | sq012_02a_braindance.scene / scene / 20 |
| [The Hunt](catalogue/base-sq021_sick_dreams.md) | sq021_09_bd_school.scene / scene / 111; sq021_10_bd_farm.scene / scene / 219; sq021_10_bd_farm.scene / scene / 229 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `call_lifecycle`

Stored signature: `questPhoneManagerNodeDefinition`. Observed in 63 quest dependency contexts.

**Inputs:** contact + call operation + scene ownership. **Outputs:** connection/end state.

Audio filtering is not call connection; test busy, interrupted and ended calls.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Like Supreme](catalogue/base-sq011_concert.md) | sq011_09_nancy_call.scene / scene / 137 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301_03_delivery.scene / scene / 4634; mq301_03_delivery.scene / scene / 4636; mq301_03_delivery.scene / scene / 6154 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `choice_gate`

Stored signature: `scnChoiceNode`. Observed in 111 quest dependency contexts.

**Inputs:** choice + eligibility predicates + commit effects. **Outputs:** selected option or defer/interruption.

Keep knowledge, skill eligibility and persistent decision separate; test return to the choice.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_00_johnny.scene / scene / 92; sq031_01a_smack_afterlife.scene / scene / 1069; sq031_01a_smack_afterlife.scene / scene / 1073 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013_00_punks.scene / scene / 34; mq013_00_punks.scene / scene / 354; mq013_00_punks.scene / scene / 503 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301_01_fireplace.scene / scene / 1265; mq301_01_fireplace.scene / scene / 1524; mq301_01_fireplace.scene / scene / 219 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `combat_control`

Stored signature: `questCombatNodeDefinition`. Observed in 73 quest dependency contexts.

**Inputs:** actor + target + combat operation. **Outputs:** command result.

Separate hostility, threat injection, encounter completion and target cleanup.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_brawl.questphase / h0 / 50 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1131 / 25; mq013.questphase / h1131 / 26; mq013.questphase / h265 / 107 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301.questphase / h419 / 22; mq301.questphase / h419 / 23; mq301.questphase / h862 / 23 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `community_lifecycle`

Stored signature: `questCommunityTemplate_NodeType`. Observed in 104 quest dependency contexts.

**Inputs:** community + named entries/phases + ownership. **Outputs:** activated/reactivated/deactivated entries.

Spawn, readiness and safe departure cleanup are separate steps.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_01b_smack_tatto.scene / scene / 317; sq031_01b_smack_tatto.scene / scene / 319; sq031_01c_smack_striptease.scene / scene / 2184 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1013 / 19; mq013.questphase / h1013 / 7; mq013.questphase / h208 / 6 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301_02_initiation.questphase / h43 / 10; mq301_02_initiation.scene / scene / 1732; mq301_02_initiation.scene / scene / 1735 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `conditional_route`

Stored signature: `questVarComparison_ConditionType`. Observed in 122 quest dependency contexts.

**Inputs:** fact + exact comparison + branch sockets. **Outputs:** selected branch.

Fact dependencies are not execution edges; identify producers and cancellation.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_00_johnny.scene / scene / 528; sq031_00_johnny.scene / scene / 588; sq031_00_johnny.scene / scene / 611 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1013 / 25; mq013.questphase / h1131 / 16; mq013.questphase / h1131 / 17 |
| [Addicted To Chaos](catalogue/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 34; wst_ep1_04_bugfixing.questphase / h0 / 14; wst_ep1_04_bugfixing.questphase / h31 / 2 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `content_scope`

Stored signature: `questContentTokenManager_NodeType`. Observed in 106 quest dependency contexts.

**Inputs:** owned token source + block/unblock/spawn operation. **Outputs:** scope acquired/released.

Avoid copying broad UnblockAll behavior without an explicit ownership policy.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_00_johnny.scene / scene / 331; sq031_motel.questphase / h0 / 292 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1013 / 27; mq013.questphase / h1013 / 5; mq013.questphase / h695 / 3 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301.questphase / h139 / 45; mq301_01_fireplace.questphase / h0 / 30; mq301_01_fireplace.questphase / h0 / 32 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `device_action`

Stored signature: `questDeviceManager_NodeType`. Observed in 95 quest dependency contexts.

**Inputs:** controller class + object + action. **Outputs:** action dispatched.

Bind the matching device completion predicate; dispatch alone is not success.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_00_johnny.scene / scene / 312; sq031_00_johnny.scene / scene / 327; sq031_01c_smack_striptease.scene / scene / 2558 |
| [A Like Supreme](catalogue/base-sq011_concert.md) | sq011_07a_royce.scene / scene / 1104; sq011_07a_royce.scene / scene / 1179; sq011_07a_royce.scene / scene / 1244 |
| [Addicted To Chaos](catalogue/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 11; wst_ep1_04.questphase / h0 / 25; wst_ep1_04.questphase / h0 / 27 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `device_state`

Stored signature: `questDevice_ConditionType`. Observed in 65 quest dependency contexts.

**Inputs:** controller class + object + condition function. **Outputs:** device predicate.

Check already-satisfied state and controller persistence across save/load.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Like Supreme](catalogue/base-sq011_concert.md) | sq011_07a_royce.scene / scene / 2774; sq011_07a_royce.scene / scene / 279; sq011_07a_royce.scene / scene / 511 |
| [Addicted To Chaos](catalogue/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 37; wst_ep1_04.questphase / h0 / 50 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `elapsed_time`

Stored signature: `questGameTimeDelay_ConditionType`. Observed in 89 quest dependency contexts.

**Inputs:** clock domain + duration + start/reset condition. **Outputs:** elapsed signal.

Compose objective/contact behavior separately; test time skip and save/load.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Like Supreme](catalogue/base-sq011_concert.md) | sq011_concert.questphase / h0 / 146; sq011_concert.questphase / h0 / 178; sq011_messages.questphase / h0 / 61 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301_02_initiation.questphase / h114 / 13; mq301_02_initiation.questphase / h114 / 6; mq301_02_initiation.questphase / h114 / 8 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `item_state`

Stored signature: `questInventory_ConditionType`. Observed in 62 quest dependency contexts.

**Inputs:** item ID + entity + quantity/comparison. **Outputs:** ownership predicate.

Ownership alone does not prove reading, device interaction or reward delivery.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_01b_smack_tatto.scene / scene / 680; sq031_01b_smack_tatto.scene / scene / 685 |
| [A Like Supreme](catalogue/base-sq011_concert.md) | sq011_10_concert.scene / scene / 5008; sq011_10_concert.scene / scene / 5019; sq011_10_concert.scene / scene / 5025 |
| [Addicted To Chaos](catalogue/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 24 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `journal_read`

Stored signature: `questJournalEntryVisited_ConditionType`. Observed in 43 quest dependency contexts.

**Inputs:** full journal entry path + visited state. **Outputs:** entry visited.

Verify the actual UI read event in game; keep inventory pickup distinct.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301_04_frame.scene / scene / 2381 |
| [Career Opportunities](catalogue/base-mws_wat_08_trauma_drama.md) | mws_wat_08.questphase / h0 / 27; mws_wat_08.questphase / h0 / 33 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `mount_state`

Stored signature: `questCharacterMount_ConditionType`. Observed in 70 quest dependency contexts.

**Inputs:** parent vehicle/puppet + child + role/event. **Outputs:** mount/unmount condition.

Match seat/role and OnMount/OnUnmount semantics; do not confuse assignment with readiness.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_01c_smack_striptease.scene / scene / 3205; sq031_01c_smack_striptease.scene / scene / 491; sq031_01c_smack_striptease.scene / scene / 562 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1131 / 3; mq013.questphase / h265 / 99 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301.questphase / h139 / 35; mq301.questphase / h139 / 36; mq301.questphase / h139 / 52 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `parallel_join`

Stored signature: `questLogicalAndNodeDefinition`. Observed in 96 quest dependency contexts.

**Inputs:** named branch completion signals + reset policy. **Outputs:** all required inputs observed.

Test either completion order, early events, interruption and save/load at the join.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_afterlife.questphase / h0 / 203 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1013 / 10; mq013.questphase / h1013 / 33; mq013.questphase / h1013 / 9 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301.questphase / h419 / 14; mq301_01_fireplace.questphase / h0 / 17; mq301_07_ending.questphase / h0 / 101 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `persistent_decision`

Stored signature: `questSetVar_NodeType`. Observed in 122 quest dependency contexts.

**Inputs:** namespaced fact + explicit write mode/value. **Outputs:** durable state update.

Separate scene-local presentation facts from public outcome state and review omitted defaults.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_00_johnny.scene / scene / 463; sq031_00_johnny.scene / scene / 504; sq031_00_johnny.scene / scene / 524 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1013 / 3; mq013.questphase / h1013 / 4; mq013.questphase / h12 / 3 |
| [Addicted To Chaos](catalogue/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 1; wst_ep1_04.questphase / h0 / 20; wst_ep1_04.questphase / h0 / 22 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `race_resolution`

Stored signature: `questLogicalXorNodeDefinition`. Observed in 100 quest dependency contexts.

**Inputs:** competing outcome signals + retirement policy. **Outputs:** converged signal.

Review actual graph wiring; an XOR class alone does not prove loser cancellation.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1131 / 33; mq013.questphase / h265 / 6 |
| [A Like Supreme](catalogue/base-sq011_concert.md) | sq011_concert.questphase / h0 / 220; sq011_messages.questphase / h0 / 58; sq011_messages.questphase / h0 / 67 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301.questphase / h139 / 38; mq301.questphase / h139 / 67; mq301.questphase / h139 / 69 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `realtime_delay`

Stored signature: `questRealtimeDelay_ConditionType`. Observed in 118 quest dependency contexts.

**Inputs:** real-time duration + cancellation owner. **Outputs:** elapsed signal.

Do not substitute game time for real time; retire delayed effects after cancellation.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_00_johnny.scene / scene / 472; sq031_01b_smack_tatto.scene / scene / 365; sq031_01b_smack_tatto.scene / scene / 372 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1131 / 20; mq013.questphase / h1131 / 4; mq013.questphase / h265 / 101 |
| [Addicted To Chaos](catalogue/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 28; wst_ep1_04.questphase / h0 / 36 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `retire_branch`

Stored signature: `questCutControlNodeDefinition`. Observed in 98 quest dependency contexts.

**Inputs:** owned target branch(es) + permanent/reset policy. **Outputs:** branch retired.

Trace every CutSource destination; cancellation must not commit success.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h695 / 22; mq013.questphase / h91 / 86; mq013.questphase / h91 / 89 |
| [A Like Supreme](catalogue/base-sq011_concert.md) | sq011_concert.questphase / h0 / 148; sq011_concert.questphase / h329 / 8 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301_01_fireplace.questphase / h0 / 29; mq301_05_drive.questphase / h0 / 80; mq301_06_contacts.questphase / h0 / 336 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `reward_commit`

Stored signature: `questGiveReward_NodeType`. Observed in 104 quest dependency contexts.

**Inputs:** reward record + eligibility + once-only commit. **Outputs:** reward delivered/committed.

Verify inventory/currency and objective state; prevent repeated awards after load.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_afterlife.questphase / h0 / 191; sq031_motel.questphase / h0 / 274 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h91 / 78 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301_04_frame.questphase / h0 / 110; mq301_05_run.scene / scene / 3075; mq301_06_contacts.questphase / h0 / 158 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `scan_evidence`

Stored signature: `questScan_ConditionType`. Observed in 30 quest dependency contexts.

**Inputs:** clue reference + exact scan event + required-set policy. **Outputs:** clue observed.

Preserve Started versus Finished, ordering, bypass and reaction joins.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [Dream On](catalogue/base-sq006_dream_on.md) | sq006_02b_investigation.scene / scene / 266; sq006_02b_investigation.scene / scene / 275; sq006_02b_investigation.scene / scene / 276 |
| [Following the River](catalogue/base-sq029_sobchak_romance.md) | sq029_02a_arrival.scene / scene / 2474 |
| [Money For Nothing](catalogue/ep1-sts_ep1_08_loot_pickup.md) | sts_ep1_08_target_meeting.scene / scene / 1459; wst_ep1_21.questphase / h0 / 36 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `scene_interface`

Stored signature: `questSceneNodeDefinition`. Observed in 113 quest dependency contexts.

**Inputs:** scene + entry + actor/marker bindings. **Outputs:** named exits and cancellation.

Validate every consumed entry/exit and distinguish terminating from notification outputs.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_afterlife.questphase / h0 / 122; sq031_afterlife.questphase / h0 / 143; sq031_brawl.questphase / h0 / 51 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h265 / 81; mq013.questphase / h91 / 14; mq013.questphase / h91 / 76 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301_01_fireplace.questphase / h0 / 3; mq301_02_initiation.questphase / h0 / 3; mq301_02_initiation.questphase / h114 / 5 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `target_resolution`

Stored signature: `questCharacterKilled_ConditionType`. Observed in 75 quest dependency contexts.

**Inputs:** target set + lethal/unconscious/defeated policy. **Outputs:** target resolved.

Review RED defaults, early defeat and per-target deduplication before counter joins.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_brawl.questphase / h0 / 15 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1131 / 7; mq013.questphase / h1131 / 8; mq013.questphase / h265 / 71 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301.questphase / h862 / 116; mq301_03_delivery.scene / scene / 10007; mq301_03_delivery.scene / scene / 10011 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `vehicle_control`

Stored signature: `questVehicleNodeDefinition`. Observed in 92 quest dependency contexts.

**Inputs:** vehicle reference + typed operation + world route. **Outputs:** operation-specific result.

Vehicle spawning, seats, driving, arrival and cleanup have separate owners.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_01c_smack_striptease.scene / scene / 2592; sq031_01c_smack_striptease.scene / scene / 560; sq031_01c_smack_striptease.scene / scene / 561 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1131 / 2; mq013.questphase / h208 / 7; mq013_00_punks.scene / scene / 1481 |
| [Addicted To Chaos](catalogue/ep1-wst_ep1_04.md) | wst_ep1_04.questphase / h0 / 19 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `workspot_performance`

Stored signature: `questUseWorkspotNodeDefinition`. Observed in 112 quest dependency contexts.

**Inputs:** actor + workspot + entry/exit policy. **Outputs:** work started/success/failure.

Wait for actor/spot readiness and restore AI ownership on interruption.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_00_johnny.scene / scene / 321; sq031_00_johnny.scene / scene / 322; sq031_00_johnny.scene / scene / 323 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1131 / 18; mq013_00_punks.scene / scene / 1097; mq013_00_punks.scene / scene / 1155 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301.questphase / h419 / 12; mq301.questphase / h419 / 13; mq301.questphase / h862 / 13 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.

## `world_variant`

Stored signature: `questTogglePrefabVariant_NodeType`. Observed in 103 quest dependency contexts.

**Inputs:** prefab + variant + desired state + restore policy. **Outputs:** world presentation changed.

Resolve world ownership and restore only this quest's overrides.

Before promotion: isolate bindings and state ownership; review normal, alternate and cut exits; test already-satisfied predicates, interruption/re-entry, save/load and once-only completion. Structural serialization checks do not replace an installed acceptance run.

| Example quest | Source locations |
| --- | --- |
| [A Cool Metal Fire](catalogue/base-sq031_smack_my_bitch_up.md) | sq031_01b_smack_tatto.scene / scene / 726; sq031_01c_smack_striptease.scene / scene / 3256; sq031_01c_smack_striptease.scene / scene / 3258 |
| [A Day In The Life](catalogue/base-mq013_punks.md) | mq013.questphase / h1013 / 22; mq013.questphase / h1013 / 29; mq013.questphase / h91 / 73 |
| [Balls to the Wall](catalogue/ep1-mq301_bomb.md) | mq301.questphase / h139 / 18; mq301_02_initiation.scene / scene / 1919; mq301_02_initiation.scene / scene / 3958 |

The complete occurrence list is in `reference/quests/deep-dives/catalogue/block-occurrences.json`.
