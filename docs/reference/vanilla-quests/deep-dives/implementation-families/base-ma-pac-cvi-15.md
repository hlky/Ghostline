# base-ma-pac-cvi-15

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\community\ma_pac_cvi_15_after_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\community\ma_pac_cvi_15_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15.quest` | content candidate | 1 / 0 | base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_bugfixing.questphase` | repair | 5 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` | content candidate | 9 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` | content candidate | 0 / 22 |  |
| `base\quest\bugfixing\minor_quests\ma_pac_cvi_15\ma_pac_cvi_15_quest_bugfixes.questphase` | repair | 2 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_pac_cvi_15/00_msg_intro`
- `contacts/regina_jones/ma_pac_cvi_15/00_msg_start`
- `contacts/regina_jones/ma_pac_cvi_15/01_ch_info`
- `contacts/regina_jones/ma_pac_cvi_15/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_pac_cvi_15/01_ch_info_lethal`
- `contacts/regina_jones/ma_pac_cvi_15/01_ch_info_lethal/01_ch_info_lethal`
- `contacts/regina_jones/ma_pac_cvi_15/02_msg_regina`
- `contacts/regina_jones/ma_pac_cvi_15/02_msg_regina_lethal`
- `points_of_interest/minor_quests/ma_pac_cvi_15`
- `quests/minor_quest/ma_pac_cvi_15`
- `quests/minor_quest/ma_pac_cvi_15/description`
- `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/check_shard`
- `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/clues`
- `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/find_psycho`
- `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/kill_psycho`
- `quests/minor_quest/ma_pac_cvi_15/ma_pac_cvi_15/send_info`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 9 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 7 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 6 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questDevice_ConditionType,questFactsDBCondition,questLogicalCondition,questObjectCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questDevice_ConditionType,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 11 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 25 |
| `questInputNodeDefinition` | 16 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 8 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 20 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 11 |
| `questLogicalXorNodeDefinition` | 11 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 14 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 11 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 12 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 12 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 16 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 13 |
| `questPhaseNodeDefinition` | 14 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
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
| `29c7ac4763cf8bc766bd` | 8 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h1352 / 7 -> 3 -> 4 |
| `8c7beb1704f04b204046` | 8 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h1352 / 4 -> 5 -> 6 |
| `ee4b344701c562aa4943` | 8 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h1352 / 3 -> 4 -> 5 |
| `0a31874be03936c47839` | 4 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h543 / 158 -> 161 -> 198 |
| `16f8bf926e07bf03f59e` | 4 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h543 / 178 -> 162 -> 166 |
| `612a8ffd896770032a4a` | 4 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h543 / 76 -> 161 -> 198 |
| `740223c71bf2a34ef9e6` | 4 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h543 / 177 -> 159 -> 161 |
| `754bb5014790dc669c0d` | 4 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 115 -> 125 -> 114 |
| `815c1815268f980fb912` | 4 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h1352 / 0 -> 8 -> 7 |
| `97ab1e5f09067b30dcbd` | 4 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h543 / 177 -> 158 -> 161 |
| `a909c836470d2b0e7fbc` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h1352 / 0 -> 11 -> 1 |
| `bb5f35239f984c46ce98` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 123 -> 114 -> 116 |
| `eaf5aab427d50e5598b6` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_bugfixing.questphase` / h9 / 0 -> 10 -> 2 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\scenes\ma_pac_cvi_15_brief.scene` / scene / 413 -> 416 -> 422 |
| `1814642825aef5741f77` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 123 -> 114 -> 122 |
| `235ed1f97cea566186b0` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 105 -> 37 -> 22 |
| `3e6f03030764fcc75954` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 114 -> 116 -> 115 |
| `7b2ab61e3019d0b44817` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h543 / 197 -> 112 -> 143 |
| `8bd54738c2c85f70192e` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 5 -> 6 -> 7 |
| `8dd3932a10644218e399` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_15\ma_pac_cvi_15_phase.questphase` / h0 / 116 -> 115 -> 125 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
