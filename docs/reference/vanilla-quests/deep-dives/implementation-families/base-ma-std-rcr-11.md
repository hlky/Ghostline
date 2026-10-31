# base-ma-std-rcr-11

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\communities\ma_std_rcr_11.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase; base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\test\mq_std_rcr_11_00_chickentest.scene; base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` | content candidate | 4 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_01_briefing.scene; base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_02_carthrow.scene |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_01_briefing.scene` | content candidate | 0 / 22 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_02_carthrow.scene` | content candidate | 0 / 33 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\test\mq_std_rcr_11_00_chickentest.scene` | test/debug | 0 / 3 |  |
| `base\quest\bugfixing\minor_quests\ma_std_rcr_11\ma_std_rcr_11_quest_bugfixes.questphase` | repair | 3 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_std_rcr_11/00_msg_intro`
- `contacts/regina_jones/ma_std_rcr_11/00_msg_start`
- `contacts/regina_jones/ma_std_rcr_11/01_ch_info`
- `contacts/regina_jones/ma_std_rcr_11/03_msg_conclusion`
- `contacts/regina_jones/ma_std_rcr_11/03a_ch_alive`
- `contacts/regina_jones/ma_std_rcr_11/03a_ch_alive/03a_ch_alive`
- `contacts/regina_jones/ma_std_rcr_11/03b_ch_dead`
- `contacts/regina_jones/ma_std_rcr_11/03b_ch_dead/03b_ch_dead`
- `contacts/regina_jones/ma_std_rcr_11/05a_msg_conclusion_alive`
- `contacts/regina_jones/ma_std_rcr_11/05b_msg_conclusion_dead`
- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_11/onscreens/ma_std_rcr_11_shard_psycho`
- `points_of_interest/minor_quests/ma_std_rcr_11`
- `quests/minor_quest/ma_std_rcr_11`
- `quests/minor_quest/ma_std_rcr_11/ma_description`
- `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/find_psycho`
- `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/kill_psycho`
- `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/loot_psycho`
- `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/read_shard_chase`
- `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/search_clues`
- `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/send_info`
- `quests/minor_quest/ma_std_rcr_11/ma_std_rcr_11/send_info/reggie`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 2 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 2 |
| `questCheckpointNodeDefinition` | 4 |
| `questCombatNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 3 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 13 |
| `questEndNodeDefinition` | 1 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 3 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 6 |
| `questEventManagerNodeDefinition` | 12 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 31 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 3 |
| `questInputNodeDefinition` | 7 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 3 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questSetLootInteractionAccess_NodeType]` | 1 |
| `questItemManagerNodeDefinition[questUniversalRef,questUseWeapon_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 23 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 14 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 6 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 9 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPhaseNodeDefinition` | 6 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 3 |
| `scnHubNode[scnNodeId]` | 4 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 3 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | 4 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 109 -> 108 -> 31 |
| `07b4a6fc5a4176a78fd6` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 105 -> 317 -> 214 |
| `0a0df9057e5523d5f8ab` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 177 -> 152 -> 181 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_01_briefing.scene` / scene / 265 -> 268 -> 274 |
| `806bcfb85ed5e3a580ad` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 152 -> 181 -> 149 |
| `a6cfcb2604abd505369f` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 200 -> 321 -> 202 |
| `ac5b347c9518873a2790` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_01_briefing.scene` / scene / 268 -> 274 -> 272 |
| `bbf9efd740881cf31a37` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_01_briefing.scene` / scene / 262 -> 265 -> 268 |
| `c938bc653820ee0e110f` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 332 -> 317 -> 214 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_01_briefing.scene` / scene / 253 -> 251 -> 255 |
| `e5742f9794e6583c67cb` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_01_briefing.scene` / scene / 249 -> 253 -> 251 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 293 -> 186 -> 75 |
| `02f1a1ecc108e1d384e8` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\test\mq_std_rcr_11_00_chickentest.scene` / scene / 1 -> 6 -> 2 |
| `05c992f8b920e82f8b9a` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 254 -> 255 -> 251 |
| `066acc9cc0b60d105ef2` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 147 -> 172 -> 254 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 118 -> 363 -> 364 |
| `07b02cf2fa5d7822c857` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 188 -> 257 -> 29 |
| `0dc16e049fa28f95b55f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 117 -> 118 -> 363 |
| `0ddeb36a5246f8e0c3b1` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\ma_std_rcr_11.questphase` / h0 / 321 -> 202 -> 146 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_11\scenes\ma_std_rcr_11_01_briefing.scene` / scene / 29 -> 67 -> 69 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
