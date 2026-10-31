# Survive...Whatever the Cost

Journal: `quests/meta/10_survive` · `MainQuest` · hash `2468799200`.

**Coverage: journal-linked.** 2 exact journal-linked nodes in 2 resources; 2 resources in the inspected dependency context.

Resource roles in that context: 2 content candidate. Role labels describe path/name evidence, not proof of runtime reachability.

Root quest resources with additional journal references: none indexed. Roots remain activation context when a phase/scene anchor exists, to avoid importing sibling launch scaffolding.

Generated structural analysis from decoded resources. Shared resources are context, not exclusive quest ownership. The tables trace stored sockets and fact dependencies; they do not simulate runtime ordering, prove all branches reachable, or infer chronology from journal objective order. See [method](../all-quests-method.md).

## Journal objectives and implementation anchors

Objective labels come from the saved local journal export. They identify intent; the implementation transitions below establish graph evidence.

| Objective | Journal path |
| --- | --- |
| You're dying. The Relic is killing you, overwriting your mind... with me. You'll be wiped clean out soon and, hell, your body might even mutiny against you before then. It's getting worse each day, sure, but you're not out of time yet. Find a way to save yourself. And fast. (Primary) | `quests/meta/10_survive/01_survive/01_survive` |

## Exact journal transitions and neighboring signals

Locators are resource basename / graph handle / node ID, or scene / node ID. Full depot paths and exact JSON pointers are in the evidence. Scene quest-node input mappings are included so a raw stamp such as `0:3` can be read against its actual mapping.

| Source locator | Journal target | Connected signals |
| --- | --- | --- |
| `q115_00_hanako.questphase / h1024 / 103` (Journal) | `quests/meta/10_survive` | 107:Out → 103:In; 103:Out → 106:In |
| `q307_01_pickup.questphase / h119 / 103` (Journal) | `quests/meta/10_survive` | 107:Out → 103:In; 103:Out → 106:In |

## Phase calls and scene handoffs

Calls below come from journal-linked graph scopes and their forward resource dependencies. Incoming sockets select entries; outgoing sockets show the caller's actual consumers. An exposed but unwired output does not advance its parent.

| Call site | Resource / marker | Connected signals |
| --- | --- | --- |
| No external phase/scene call in selected graph context | Embedded graphs and scene-internal quest nodes remain in evidence | — |

## Parent orchestration and activation context

Only actual phase/scene call sites are followed here; references from scene-state conditions are not treated as calls. Parent resources can be shared master graphs. Neighboring predicates describe stored gates, not verified engine entry eligibility.

| Parent call site | Called resource | Incoming gates and connected outputs |
| --- | --- | --- |
| `base\quest\main_quests\part1\q115\q115_afterlife.questphase` / h0 / 69 | `q115_00_hanako.questphase` | 62: Phase; 89: Input; 72: Input; 62:Out1 → 69:In1; 69:Out1 → 70:In1; 89:Out → 69:In2; 72:Out → 69:In3 |
| `ep1\quest\main_quests\q307\q307.questphase` / h0 / 21 | `q307_01_pickup.questphase` | 3: Input; 20: Phase: q307_00_opt_in.questphase; 3:Out → 21:chicken_in; 20:Out1 → 21:In1; 21:Out1 → 22:In1; 21:prefetech_out → 22:prefetch_in |
| `base\quest\main_quests\part1\act_1.questphase` / h329 / 4 | `q115_afterlife.questphase` | 0: Input; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 9: Phase; 0:Out → 4:In; 4:Out1 → 1:In; 9:Out1 → 4:In; 9:OutRestaurant → 4:InRestaurant; 9:OutElevator → 4:InElevator; 9:OutRipperdoc → 4:InRipperdoc; 4:q114_out → 5:In; 9:OutPills → 4:InPills; 4:q113_out → 6:In; 9:OutRipperRoof → 4:InRipperdocRoof; 4:death_out → 7:In; 9:OutQ114 → 4:InQ114; 4:mikoshi_out → 8:In; 9:OutQ113 → 4:InQ113; 9:OutSolo → 4:InSolo; 9:OutAfterlife → 4:InAfterlife; 9:OutAfterRogue → 4:InAfterSex; 9:OutBeforeAlt → 4:InBeforeAlt; 9:OutAfterAlt → 4:InAfterlifePlan; 9:OutAV → 4:InAfterlifeAV; 9:OutJungle → 4:InJungle; 9:OutAtrium → 4:InAtrium; 9:OutNetrunner → 4:InNetrunner |
| `base\quest\main_quests\part1\q115\q115_afterlife.quest` / h0 / 5 | `q115_afterlife.questphase` | 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91: Phase; 91:Out1 → 5:In; 5:Out1 → 73:In1; 91:OutRestaurant → 5:InRestaurant; 91:OutElevator → 5:InElevator; 91:OutRipperdoc → 5:InRipperdoc; 5:q114_out → 92:In1; 91:OutPills → 5:InPills; 5:q113_out → 115:In1; 91:OutRipperRoof → 5:InRipperdocRoof; 5:death_out → 116:In1; 91:OutQ114 → 5:InQ114; 5:mikoshi_out → 73:cyberspace_in; 91:OutQ113 → 5:InQ113; 91:OutSolo → 5:InSolo; 91:OutAfterlife → 5:InAfterlife; 91:OutAfterRogue → 5:InAfterSex; 91:OutBeforeAlt → 5:InBeforeAlt; 91:OutAfterAlt → 5:InAfterlifePlan; 91:OutAV → 5:InAfterlifeAV; 91:OutJungle → 5:InJungle; 91:OutAtrium → 5:InAtrium; 91:OutNetrunner → 5:InNetrunner |
| `ep1\quest\main_quests\ep1_main_quests.questphase` / h0 / 12 | `q307.questphase` | 26: Input; 33: LogicalHub; 26: Input; 32: CutControl; 26:Out → 12:debug_in; 12:Out1 → 34:Q307; 33:Out1 → 12:main_in; 26:Out → 12:main_in; 32:CutSource → 12:CutDestination |
| `ep1\quest\main_quests\q307\q307.quest` / h0 / 0 | `q307.questphase` | 3: LogicalHub; 15: Condition: q307_paused Equal RED default; 10: Switch: q307_00_opt_in_chicken; q307_01_pickup_chicken; q307_02_coma_chicken; q307_03_hospital_chicken; q307_04_cabride_chicken; q307_05_alley_chicken; q307_06_viktor_chicken; q307_07_thugs_chicken; q307_08_misty_chicken; q307_09_cutscene_chicken; q307_10_finalboards_chicken; q307_rooftop_chicken; 10: Switch: q307_00_opt_in_chicken; q307_01_pickup_chicken; q307_02_coma_chicken; q307_03_hospital_chicken; q307_04_cabride_chicken; q307_05_alley_chicken; q307_06_viktor_chicken; q307_07_thugs_chicken; q307_08_misty_chicken; q307_09_cutscene_chicken; q307_10_finalboards_chicken; q307_rooftop_chicken; 15: Condition: q307_paused Equal RED default; 10: Switch: q307_00_opt_in_chicken; q307_01_pickup_chicken; q307_02_coma_chicken; q307_03_hospital_chicken; q307_04_cabride_chicken; q307_05_alley_chicken; q307_06_viktor_chicken; q307_07_thugs_chicken; q307_08_misty_chicken; q307_09_cutscene_chicken; q307_10_finalboards_chicken; q307_rooftop_chicken; 10: Switch: q307_00_opt_in_chicken; q307_01_pickup_chicken; q307_02_coma_chicken; q307_03_hospital_chicken; q307_04_cabride_chicken; q307_05_alley_chicken; q307_06_viktor_chicken; q307_07_thugs_chicken; q307_08_misty_chicken; q307_09_cutscene_chicken; q307_10_finalboards_chicken; q307_rooftop_chicken; 10: Switch: q307_00_opt_in_chicken; q307_01_pickup_chicken; q307_02_coma_chicken; q307_03_hospital_chicken; q307_04_cabride_chicken; q307_05_alley_chicken; q307_06_viktor_chicken; q307_07_thugs_chicken; q307_08_misty_chicken; q307_09_cutscene_chicken; q307_10_finalboards_chicken; q307_rooftop_chicken; 10: Switch: q307_00_opt_in_chicken; q307_01_pickup_chicken; q307_02_coma_chicken; q307_03_hospital_chicken; q307_04_cabride_chicken; q307_05_alley_chicken; q307_06_viktor_chicken; q307_07_thugs_chicken; q307_08_misty_chicken; q307_09_cutscene_chicken; q307_10_finalboards_chicken; q307_rooftop_chicken; 10: Switch: q307_00_opt_in_chicken; q307_01_pickup_chicken; q307_02_coma_chicken; q307_03_hospital_chicken; q307_04_cabride_chicken; q307_05_alley_chicken; q307_06_viktor_chicken; q307_07_thugs_chicken; q307_08_misty_chicken; q307_09_cutscene_chicken; q307_10_finalboards_chicken; q307_rooftop_chicken; 10: Switch: q307_00_opt_in_chicken; q307_01_pickup_chicken; q307_02_coma_chicken; q307_03_hospital_chicken; q307_04_cabride_chicken; q307_05_alley_chicken; q307_06_viktor_chicken; q307_07_thugs_chicken; q307_08_misty_chicken; q307_09_cutscene_chicken; q307_10_finalboards_chicken; q307_rooftop_chicken; 10: Switch: q307_00_opt_in_chicken; q307_01_pickup_chicken; q307_02_coma_chicken; q307_03_hospital_chicken; q307_04_cabride_chicken; q307_05_alley_chicken; q307_06_viktor_chicken; q307_07_thugs_chicken; q307_08_misty_chicken; q307_09_cutscene_chicken; q307_10_finalboards_chicken; q307_rooftop_chicken; 10: Switch: q307_00_opt_in_chicken; q307_01_pickup_chicken; q307_02_coma_chicken; q307_03_hospital_chicken; q307_04_cabride_chicken; q307_05_alley_chicken; q307_06_viktor_chicken; q307_07_thugs_chicken; q307_08_misty_chicken; q307_09_cutscene_chicken; q307_10_finalboards_chicken; q307_rooftop_chicken; 10: Switch: q307_00_opt_in_chicken; q307_01_pickup_chicken; q307_02_coma_chicken; q307_03_hospital_chicken; q307_04_cabride_chicken; q307_05_alley_chicken; q307_06_viktor_chicken; q307_07_thugs_chicken; q307_08_misty_chicken; q307_09_cutscene_chicken; q307_10_finalboards_chicken; q307_rooftop_chicken; 1: CutControl; 3:Out1 → 0:debug_in; 15:True → 0:main_in; 10:Otherwise → 0:main_in; 0:Out1 → 14:Q307; 10:Case2943604129 → 0:opt_in_chicken; 15:False → 0:pickup_chicken; 10:Case196068612 → 0:pickup_chicken; 10:Case3092325849 → 0:coma_chicken; 10:Case4145565413 → 0:hospital_chicken; 10:Case4291212281 → 0:cabride_chicken; 10:Case1137937274 → 0:alley_chicken; 10:Case3336490887 → 0:viktor_chicken; 10:Case2623428973 → 0:thugs_chicken; 10:Case1046963116 → 0:misty_chicken; 10:Case1137708726 → 0:cutscene_chicken; 1:CutSource → 0:CutDestination |
| `base\quest\cyberpunk2077.questphase` / h0 / 33 | `act_1.questphase` | 32: Phase: prologue.questphase; 82: Phase; 57: Phase; 57: Phase; 57: Phase; 98: Condition: ep1_active Less 1; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 57: Phase; 102: PauseCondition: ep1_active GreaterOrEqual 1; 32:Out1 → 33:Q101; 82:CYB-656199_Out → 33:CYB-656199_In; 33:Q201 → 36:Q201; 33:Q202 → 36:Q202; 57:Q101 Out → 33:Q101; 33:Q203 → 36:Q203; 57:Q101 Vroom Out → 33:Q101 Vroom; 33:Q204 → 36:Q204; 57:Q103 Out → 33:Q103; 98:True → 33:Q103; 33:Q115 Final Boards → 91:In1; 57:Q104 Out → 33:Q104; 57:Q105 Out → 33:Q105; 57:Q108 Out → 33:Q108; 57:Q110 Out → 33:Q110; 57:Q112 Out → 33:Q112; 57:Q113 Out → 33:Q113; 57:Q114 Out → 33:Q114; 57:Q115 Out → 33:Q115; 57:Q116 Out → 33:Q116; 57:EP1_Standalone → 33:EP1_Standalone; 102:Out → 33:EP1_Standalone |
| `ep1\quest\ep1.questphase` / h0 / 9 | `ep1_main_quests.questphase` | 22: LogicalHub; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 12: Phase; 19: Phase; 86: LogicalHub; 87: LogicalHub; 22:Out1 → 9:Base; 12:q301 → 9:q301; 12:q302 → 9:q302; 12:q303 → 9:q303; 12:q304 → 9:q304; 12:q305 → 9:q305; 12:q306 → 9:q306; 12:q307 → 9:q307; 19:Out1 → 9:Standalone; 86:Out1 → 9:CP77-64292_in; 87:Out1 → 9:CP77-65722_Out |
| `base\quest\cyberpunk2077.quest` / h0 / 2 | `cyberpunk2077.questphase` | 0: Start; 0:Out → 2:Start |
| `base\quest\demos\handson_2020\handson_2020.quest` / h0 / 33 | `cyberpunk2077.questphase` | 34: FactsDBManager: e3_2020; 34:Out → 33:Start |
| `base\quest\demos\handson_2020\handson_2020_testing.quest` / h0 / 5 | `cyberpunk2077.questphase` | 6: FactsDBManager: e3_2020; 6:Out → 5:Testing |
| `ep1\quest\cyberpunk2077_ep1_standalone.quest` / h0 / 1 | `cyberpunk2077.questphase` | 2: Start; 2:Out → 1:EP1_Standalone |
| `ep1\quest\ep1.quest` / h0 / 0 | `ep1.questphase` | 27: FactsDBManager: ep1_installed; 27:Out → 0:Base |
| `ep1\quest\ep1_standalone.quest` / h0 / 2 | `ep1.questphase` | 14: FactsDBManager: ep1_installed; 14:Out → 2:Standalone |

## Scene interfaces and actors

| Scene | Entries → exits | Actors; graph size |
| --- | --- | --- |
| No resolved scene dependency in this scope | This does not prove the quest has no dialogue | — |

## Choice labels, eligibility and outgoing branches

Text is joined from screenplay option IDs to the embedded localization store. An option-level predicate is only one layer of eligibility; parent graph routes can impose additional gates.

| Scene / node / option | Embedded label and caption | Authored option gate | Outgoing signal |
| --- | --- | --- | --- |
| No choice option in resolved scene context | — | — | — |

## Persistent state dependencies

A writer/reader pairing is a data dependency, not proof of an execution edge or exclusive ownership. RED defaults remain omitted in the evidence. `done`/cleanup facts are not assumed to mean successful journal outcome.

| Fact | Writers in context | Readers and other fact bindings in context |
| --- | --- | --- |
| No named fact uses in selected graph context | — | — |

## Exact gates, joins and cancellation

<details><summary>4 stored control nodes in the selected context</summary>

Only stored fields are shown. Missing comparison, clock or boolean fields retain RED defaults; no value is invented. This exposes the actual wait predicates, join counts and cut destinations behind the proposed blocks.

| Locator | Type and authored fields | Connected signals |
| --- | --- | --- |
| `q115_00_hanako.questphase / h1024 / 106` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":35}}}` | 103:Out → 106:In; 106:Out → 104:In |
| `q115_00_hanako.questphase / h1024 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":35}}}` | 107:Out → 103:In; 115:Out → 107:In |
| `q307_01_pickup.questphase / h119 / 106` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":35}}}` | 103:Out → 106:In; 106:Out → 104:In |
| `q307_01_pickup.questphase / h119 / 107` | `questPauseConditionNodeDefinition` `{"condition":{"$type":"questTimeCondition","type":{"$type":"questRealtimeDelay_ConditionType","miliseconds":35}}}` | 107:Out → 103:In; 115:Out → 107:In |

</details>


## Candidate Ghostline blocks

These candidates are supported by the listed stored node types. They are reduction proposals, not implemented compiler types or claims that a node's presence proves a complete reusable lifecycle. Review topology, bindings and cancellation before promotion.

| Candidate | Concrete evidence | Inputs → outputs; reduction boundary |
| --- | --- | --- |
| `journal_transition` | q115_00_hanako.questphase / h1024 / 103; q307_01_pickup.questphase / h119 / 103 | typed journal operation + exact path + state socket → journal operation output. Read Active/Succeeded/Failed/Inactive from the wired input; output alone does not establish success. |
| `realtime_delay` | q115_00_hanako.questphase / h1024 / 106; q115_00_hanako.questphase / h1024 / 107; q307_01_pickup.questphase / h119 / 106; q307_01_pickup.questphase / h119 / 107 | real-time duration + cancellation owner → elapsed signal. Do not substitute game time for real time; retire delayed effects after cancellation. |

## Dependencies and coverage limits

| Resource | Role | Evidence family |
| --- | --- | --- |
| `base\quest\main_quests\part1\q115\phases\q115_00_hanako.questphase` | content candidate; journal anchor | `base-q115` |
| `ep1\quest\main_quests\q307\phases\q307_01_pickup.questphase` | content candidate; journal anchor | `ep1-q307` |

Evidence shards for this dossier (including parent context): [base-q115](../../../../../reference/quests/deep-dives/all-quests/evidence/base-q115.json.gz), [base-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/base-shared.json.gz), [ep1-q307](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-q307.json.gz), [ep1-shared](../../../../../reference/quests/deep-dives/all-quests/evidence/ep1-shared.json.gz).

World NodeRef definitions/streaming owners, full actor and animation closure, numeric TweakDB names, spoken subtitle/VO payload joins and installed/save behavior have not been validated by this structural pass. Raw direct references, actor bindings, choices, event locstrings and community entries remain in the evidence shards.

## Required acceptance cases before reuse

Exercise normal completion and each named alternate outcome; interrupt and return at every scene handoff; start with spatial/item/actor predicates already satisfied; save/load across waits and joins; cancel parallel listeners; verify reward delivery once; and verify cleanup without changing the committed outcome. Apply the block-specific cases in the [expanded contracts](../all-quest-blocks.md). No installed playtest is claimed.

## Connected paths and supporting bindings

1 repeated typed/socket path signatures in this selected graph context; 0 distinct direct resource identities; 0 embedded graph handoffs. The full occurrence lists, concrete parameters, exact source pointers and external edges are retained in the checked evidence. Shared forward dependencies can serve several quests; these are context counts.

### Connected block candidates

These examples are ranked by breadth across resource families. Three nodes are a useful extraction seed, not a complete contract: retain all boundary ports and inspect surrounding setup, cancellation and cleanup.

| Pattern | Actual occurrence | Typed path and bound sockets |
| --- | --- | --- |
| `7bddf867454aa2f6773c` | `base\quest\main_quests\part1\q115\phases\q115_00_hanako.questphase` / h1024 / 107 -> 103 -> 106 | questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition] -> questJournalNodeDefinition[questJournalBulkUpdate_NodeType] -> questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]; Out -> In; Out -> In |

### Embedded phase interfaces

| Owning node | Child graph | Authored interface |
| --- | --- | --- |
| No embedded handoff in resolved context | — | External calls remain in the main dossier |

### Launch definition context

These definitions reference this quest context or a resolved ancestor. They can include test/debug launch configurations; their presence does not establish that the installed game selects them.

| Definition | Path role | Referenced context |
| --- | --- | --- |
| `base\quest\main_quests\part1\q115\q115_afterlife.gamedef` | content candidate | base\quest\main_quests\part1\q115\q115_afterlife.quest |
| `base\quest\cyberpunk2077.gamedef` | content candidate | base\quest\cyberpunk2077.quest |
| `base\quest\demos\handson_2020\handson_2020.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020.quest |
| `base\quest\demos\handson_2020\handson_2020_testing.gamedef` | content candidate | base\quest\demos\handson_2020\handson_2020_testing.quest |
| `ep1\quest\minor_quests\mq306\mq306.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\main_quests\q307\q307.gamedef` | content candidate | ep1\quest\main_quests\q307\q307.quest |
| `ep1\openworld\sandbox_activities\courier_spot\ep1_courier_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1.gamedef` | content candidate | base\quest\cyberpunk2077.quest; ep1\quest\ep1.quest |
| `ep1\quest\ep1_debug.gamedef` | content candidate | ep1\quest\ep1.quest |
| `ep1\quest\ep1_standalone.gamedef` | content candidate | ep1\quest\ep1_standalone.quest; ep1\quest\cyberpunk2077_ep1_standalone.quest |
| `ep1\quest\ep1_standalone_debug.gamedef` | content candidate | ep1\quest\cyberpunk2077_ep1_standalone.quest |

### Supporting resource ownership

Providers below are archive-index matches for exact depot hashes. Index presence establishes availability, not payload inspection or runtime load order. Phase/scene/community contents are structurally indexed when marked; other bindings require their own controller, world, performance or localization validation.

| Resource | Binding role | Providers / inspection |
| --- | --- | --- |
| No attributed direct resource binding | Attribution unresolved | — |

### Fact producers outside the forward context

These are indexed writer locations, not proof that they execute before this quest. Absence of a writer here does not establish that a fact is never produced: entity/engine/script producers may be outside the graph corpus.

| Fact | External writer examples |
| --- | --- |
| No external graph writer located | External engine/device/script production remains possible |

NodeRef uses: 2; TweakDB binding uses: 0. Uses retain exact pointers in resource evidence. A global alias alone is not a resolved streaming owner; numeric records are not guessed. See [all-quest analysis](../all-quest-findings.md) for extraction rules and proposed contracts.

## Scene performance events

Section event data retains actor/animation/audio bindings and authored time fields, with raw pointers. Events in different sections are not treated as one chronological timeline: parent routing, interruption and playback policy still apply. Animation/voice payloads and installed timing are not validated by this extraction.

| Scene | Event sections / events | Stored event types |
| --- | --- | --- |
| No resolved scene in this quest context | — | No performance inference |

Query full events with `tools/query_sidequest_evidence.py --root reference/quests/deep-dives/all-quests --quest <exact title or journal path> --events`; add `--resource`, `--graph scene --node <id>` or `--event-type <substring>` to narrow the output. Scene-global screenplay and interruption data remain in the performance shards.
