# base-ma-cct-dtn-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\community\ma_cct_dtn_03.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase; base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` | content candidate | 7 / 0 | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene; base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_scenes.scene |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_scenes.scene` | content candidate | 0 / 27 |  |
| `base\quest\bugfixing\minor_quests\ma_cct_dtn_03\ma_cct_dtn_03_quest_bugfixes.questphase` | repair | 7 / 0 | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_cct_dtn_03/00_msg_rejected`
- `contacts/regina_jones/ma_cct_dtn_03/00_msg_start`
- `contacts/regina_jones/ma_cct_dtn_03/01_ch_info`
- `contacts/regina_jones/ma_cct_dtn_03/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_cct_dtn_03/01_ch_info_lethal`
- `contacts/regina_jones/ma_cct_dtn_03/01_ch_info_lethal/01_ch_info_lethal`
- `contacts/regina_jones/ma_cct_dtn_03/02_msg_regina`
- `contacts/regina_jones/ma_cct_dtn_03/02_msg_regina_lethal`
- `onscreens/emails/quests/minor_activities/city_center/downtown/ma_cct_dtn_03/onscreens/ma_cct_dtn_03_onscreen_01`
- `onscreens/emails/quests/minor_activities/city_center/downtown/ma_cct_dtn_03/onscreens/ma_cct_dtn_03_onscreen_02`
- `points_of_interest/minor_quests/ma_cct_dtn_03`
- `quests/minor_quest/ma_cct_dtn_03`
- `quests/minor_quest/ma_cct_dtn_03/description`
- `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/check_shard`
- `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/check_shard_02`
- `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/find`
- `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/kill`
- `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/search_for_clues`
- `quests/minor_quest/ma_cct_dtn_03/ma_cct_dtn_03/send_info`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 2 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_NodeType,questCharacterManagerCombat_SetDeathDirection]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questConditionNodeDefinition[questInventory_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 15 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 9 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 31 |
| `questInputNodeDefinition` | 16 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 40 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMiscAICommandNode` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 12 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 9 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 9 |
| `questPhaseNodeDefinition` | 15 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 4 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVisionModesManagerNodeDefinition[questSetFocusClueState_NodeType]` | 4 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 9 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 4 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c4cc47f1088342201da5` | 6 | `base\quest\bugfixing\minor_quests\ma_cct_dtn_03\ma_cct_dtn_03_quest_bugfixes.questphase` / h172 / 9 -> 10 -> 11 |
| `eaf5aab427d50e5598b6` | 6 | `base\quest\bugfixing\minor_quests\ma_cct_dtn_03\ma_cct_dtn_03_quest_bugfixes.questphase` / h7 / 0 -> 8 -> 2 |
| `1526ac8e177a8e5ae1f0` | 3 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 46 -> 177 -> 8 |
| `bfe95df47bd1ca67330f` | 3 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 38 -> 63 -> 97 |
| `07849c56858881bd3628` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_scenes.scene` / scene / 6 -> 56 -> 32 |
| `0cdd2c68dd0540694e6c` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 64 -> 158 -> 157 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_brief.scene` / scene / 285 -> 267 -> 273 |
| `17ff4f352843f7f881cf` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 73 -> 79 -> 80 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h300 / 5 -> 10 -> 6 |
| `19a3ccd25879b7f6c119` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 78 -> 79 -> 80 |
| `1a87b7d33597a8406eb7` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h1051 / 12 -> 11 -> 13 |
| `38e0d20737557467bb74` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 85 -> 88 -> 150 |
| `3b3957b73704ef86857f` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 78 -> 243 -> 231 |
| `3e6f03030764fcc75954` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 108 -> 110 -> 109 |
| `424df8c2dc45bf3e2ace` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\scenes\ma_cct_dtn_03_scenes.scene` / scene / 59 -> 61 -> 92 |
| `52a8e5957844bbdf81b2` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 85 -> 88 -> 89 |
| `539abdcbe41456286e59` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 79 -> 125 -> 94 |
| `5f87aab4c9e224d399e4` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 230 -> 229 -> 92 |
| `7e7dbbc930b3717fd790` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h0 / 190 -> 8 -> 9 |
| `81560ce7cbff639ccdd3` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_03\ma_cct_dtn_03_phase.questphase` / h1051 / 10 -> 12 -> 11 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
