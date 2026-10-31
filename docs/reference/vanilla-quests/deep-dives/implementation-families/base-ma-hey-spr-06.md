# base-ma-hey-spr-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\community\ma_hey_spr_06_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_bugfixing.questphase; base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase; base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_bugfixing.questphase` | repair | 4 / 0 |  |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` | content candidate | 7 / 0 | base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\scenes\ma_hey_spr_06_brief.scene |
| `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\scenes\ma_hey_spr_06_brief.scene` | content candidate | 0 / 22 |  |
| `base\quest\bugfixing\minor_quests\ma_hey_spr_06\ma_hey_spr_06_quest_bugfixes.questphase` | repair | 2 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_hey_spr_06/00_msg_intro`
- `contacts/regina_jones/ma_hey_spr_06/00_msg_start`
- `contacts/regina_jones/ma_hey_spr_06/01_ch_info`
- `contacts/regina_jones/ma_hey_spr_06/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_hey_spr_06/01_ch_info_lethal`
- `contacts/regina_jones/ma_hey_spr_06/01_ch_info_lethal/01_ch_info_lethal`
- `contacts/regina_jones/ma_hey_spr_06/02_msg_regina`
- `contacts/regina_jones/ma_hey_spr_06/02_msg_regina_lethal`
- `onscreens/emails/quests/minor_activities/heywood/wellsprings/ma_hey_spr_06/onscreens/ma_hey_spr_06_onscreen_02`
- `points_of_interest/minor_quests/ma_hey_spr_06`
- `quests/minor_quest/ma_hey_spr_06`
- `quests/minor_quest/ma_hey_spr_06/ma_description`
- `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/check_shard`
- `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/check_shard1`
- `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/clues`
- `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/find_psycho`
- `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/kill_psycho`
- `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/send_info`
- `quests/minor_quest/ma_hey_spr_06/ma_hey_spr_04/send_info/contact`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 5 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 7 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 7 |
| `questEventManagerNodeDefinition` | 7 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 25 |
| `questInputNodeDefinition` | 13 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 24 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 6 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 12 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 13 |
| `questPhaseNodeDefinition` | 13 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `29c7ac4763cf8bc766bd` | 6 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h813 / 7 -> 3 -> 4 |
| `8c7beb1704f04b204046` | 6 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h813 / 4 -> 5 -> 6 |
| `ee4b344701c562aa4943` | 6 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h813 / 3 -> 4 -> 5 |
| `754bb5014790dc669c0d` | 4 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h0 / 136 -> 146 -> 135 |
| `815c1815268f980fb912` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h813 / 0 -> 8 -> 7 |
| `a3e5f861a4b71433135a` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h197 / 21 -> 11 -> 23 |
| `bb5f35239f984c46ce98` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h0 / 144 -> 135 -> 137 |
| `eaf5aab427d50e5598b6` | 3 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_bugfixing.questphase` / h9 / 0 -> 4 -> 2 |
| `0d4d0dac270dc158e66a` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h0 / 24 -> 122 -> 63 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\scenes\ma_hey_spr_06_brief.scene` / scene / 411 -> 414 -> 420 |
| `1814642825aef5741f77` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h0 / 144 -> 135 -> 143 |
| `3e6f03030764fcc75954` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h0 / 135 -> 137 -> 136 |
| `8bd54738c2c85f70192e` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h0 / 28 -> 29 -> 72 |
| `8dd3932a10644218e399` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h0 / 137 -> 136 -> 146 |
| `a25eb3764ff0bbe3572e` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h0 / 126 -> 156 -> 191 |
| `ac5b347c9518873a2790` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\scenes\ma_hey_spr_06_brief.scene` / scene / 414 -> 420 -> 418 |
| `bbf9efd740881cf31a37` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\scenes\ma_hey_spr_06_brief.scene` / scene / 408 -> 411 -> 414 |
| `bf65d680c627d4bbfc35` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\ma_hey_spr_06_phase.questphase` / h0 / 136 -> 146 -> 143 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\scenes\ma_hey_spr_06_brief.scene` / scene / 376 -> 377 -> 2 |
| `e5742f9794e6583c67cb` | 2 | `base\open_world\minor_activities\heywood\wellsprings\ma_hey_spr_06\scenes\ma_hey_spr_06_brief.scene` / scene / 381 -> 376 -> 377 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
