# base-ma-wat-kab-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\community\ma_wat_kab_08_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\community\ma_wat_kab_08_com_civ.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_def.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` | content candidate | 15 / 0 | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\scenes\ma_wat_kab_08_brief.scene; base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\scenes\ma_wat_kab_08_johnny_and_clues.scene |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_quest.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase; base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\scenes\ma_wat_kab_08_brief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\scenes\ma_wat_kab_08_johnny_and_clues.scene` | content candidate | 0 / 18 |  |
| `base\quest\bugfixing\minor_quests\ma_wat_kab_08\ma_wat_kab_08_quest_bugfixes.questphase` | repair | 2 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_wat_kab_08/00_msg_intro`
- `contacts/regina_jones/ma_wat_kab_08/00_msg_start`
- `contacts/regina_jones/ma_wat_kab_08/01_ch_info`
- `contacts/regina_jones/ma_wat_kab_08/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_wat_kab_08/01b_ch_info_lethal`
- `contacts/regina_jones/ma_wat_kab_08/01b_ch_info_lethal/01b_ch_info_lethal`
- `contacts/regina_jones/ma_wat_kab_08/02_msg_regina`
- `contacts/regina_jones/ma_wat_kab_08/02b_msg_regina_lethal`
- `onscreens/emails/quests/minor_activities/watson/kabuki/ma_wat_kab_08/onscreens/ma_wat_kab_08_onscreen_01`
- `onscreens/emails/quests/minor_activities/watson/kabuki/ma_wat_kab_08/onscreens/ma_wat_kab_08_onscreen_02`
- `points_of_interest/minor_quests/ma_wat_kab_08`
- `quests/minor_quest/ma_wat_kab_08`
- `quests/minor_quest/ma_wat_kab_08/description`
- `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/check_message`
- `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/check_shard`
- `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/clues`
- `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/find_psycho`
- `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/kill_psycho`
- `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/send_info`
- `quests/minor_quest/ma_wat_kab_08/ma_wat_kab_08/send_info/regina`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 5 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 10 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 7 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 2 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questTriggerCondition]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 7 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 5 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 13 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 11 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 21 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 17 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 27 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMiscAICommandNode` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 14 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 35 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 23 |
| `questPhaseNodeDefinition` | 16 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 7 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVisionModesManagerNodeDefinition[questSetFocusClueState_NodeType]` | 7 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 7 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 13 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 5 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 4 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `29c7ac4763cf8bc766bd` | 8 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h1771 / 7 -> 3 -> 4 |
| `8c7beb1704f04b204046` | 8 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h1771 / 4 -> 5 -> 6 |
| `ee4b344701c562aa4943` | 8 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h1771 / 3 -> 4 -> 5 |
| `19a5bfbc0b6690f905c3` | 5 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h371 / 12 -> 14 -> 15 |
| `bdc4a09bd60f9d407dcc` | 5 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h0 / 169 -> 171 -> 172 |
| `815c1815268f980fb912` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h1771 / 0 -> 8 -> 7 |
| `bfe95df47bd1ca67330f` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h217 / 24 -> 25 -> 27 |
| `003cfab274ec49874f34` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h0 / 132 -> 143 -> 265 |
| `0be8bca3ed2bc8b09a9e` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h371 / 3 -> 10 -> 27 |
| `0dd210d09f53d7243de6` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h0 / 53 -> 57 -> 174 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\scenes\ma_wat_kab_08_brief.scene` / scene / 419 -> 399 -> 405 |
| `1389e62364fbb2bc008f` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h1650 / 0 -> 2 -> 4 |
| `14f549ad402709e49be6` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h0 / 74 -> 57 -> 174 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h217 / 5 -> 12 -> 6 |
| `256f5695ecda8ef528d7` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h0 / 267 -> 268 -> 162 |
| `27ad2444f50fe5589786` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h371 / 6 -> 10 -> 27 |
| `2b97bbe6c4d61ccdc588` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h1650 / 4 -> 3 -> 1 |
| `3ba86c71a70bfb0620a5` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h1377 / 25 -> 26 -> 12 |
| `3e6f03030764fcc75954` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h1650 / 2 -> 4 -> 3 |
| `46832392e10cc5a581d6` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_08\ma_wat_kab_08_phase.questphase` / h217 / 14 -> 15 -> 16 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
