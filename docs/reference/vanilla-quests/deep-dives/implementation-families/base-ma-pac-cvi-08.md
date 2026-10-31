# base-ma-pac-cvi-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\community\ma_pac_cvi_08_civ_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\community\ma_pac_cvi_08_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase; base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\test\ma_pac_cvi_08_00_chickentest.scene; base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` | content candidate | 8 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\scenes\ma_pac_cvi_08_01_briefing.scene |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\scenes\ma_pac_cvi_08_01_briefing.scene` | content candidate | 0 / 39 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\test\ma_pac_cvi_08_00_chickentest.scene` | test/debug | 0 / 3 |  |
| `base\quest\bugfixing\minor_quests\ma_pac_cvi_08\ma_pac_cvi_08_quest_bugfixes.questphase` | repair | 3 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_pac_cvi_08`
- `contacts/regina_jones/ma_pac_cvi_08/00_msg_intro`
- `contacts/regina_jones/ma_pac_cvi_08/00_msg_start`
- `contacts/regina_jones/ma_pac_cvi_08/01_ch_info`
- `contacts/regina_jones/ma_pac_cvi_08/03_msg_conclusion`
- `contacts/regina_jones/ma_pac_cvi_08/03a_ch_alive`
- `contacts/regina_jones/ma_pac_cvi_08/03a_ch_alive/03a_ch_alive`
- `contacts/regina_jones/ma_pac_cvi_08/03b_ch_dead`
- `contacts/regina_jones/ma_pac_cvi_08/03b_ch_dead/03b_ch_dead`
- `contacts/regina_jones/ma_pac_cvi_08/05a_msg_conclusion_alive`
- `contacts/regina_jones/ma_pac_cvi_08/05b_msg_conclusion_dead`
- `onscreens/emails/quests/minor_activities/pacifica/coastview/ma_pac_cvi_08/onscreens/ma_pac_cvi_08_shard_mobster`
- `onscreens/emails/quests/minor_activities/pacifica/coastview/ma_pac_cvi_08/onscreens/ma_pac_cvi_08_shard_psycho`
- `points_of_interest/minor_quests/ma_pac_cvi_08`
- `quests/minor_quest/ma_pac_cvi_08`
- `quests/minor_quest/ma_pac_cvi_08/description`
- `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/check_van`
- `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/find_psycho`
- `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/kill_psycho`
- `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/loot_psycho`
- `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/loot_psycho1`
- `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/read_shard_mobster`
- `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/read_shard_psycho`
- `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/search_clues`
- `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/send_info`
- `quests/minor_quest/ma_pac_cvi_08/ma_pac_cvi_08/send_info/contact`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 7 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 5 |
| `questCombatNodeDefinition` | 5 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_ControlCrowd]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 12 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 18 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 28 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questInputNodeDefinition` | 12 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 31 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 18 |
| `questLogicalXorNodeDefinition` | 7 |
| `questMiscAICommandNode` | 1 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 5 |
| `questOutputNodeDefinition` | 10 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 6 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 12 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 10 |
| `questPhaseNodeDefinition` | 10 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 5 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 11 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 12 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 10 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 3 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 3 |
| `scnXorNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `759c119f9bcd59ced56a` | 6 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h0 / 312 -> 74 -> 60 |
| `145293552c6182ec258e` | 5 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h1070 / 37 -> 42 -> 54 |
| `848895b700081f481a11` | 5 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h1070 / 35 -> 37 -> 64 |
| `86f3088bc0933750b2a9` | 5 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h1070 / 64 -> 59 -> 36 |
| `6c02e94c30ce1078be32` | 4 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h914 / 56 -> 55 -> 58 |
| `f2e8e66d552068335e40` | 4 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h914 / 6 -> 56 -> 55 |
| `0a0df9057e5523d5f8ab` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h0 / 254 -> 251 -> 255 |
| `9af8a87f20a910659fa8` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h0 / 46 -> 36 -> 268 |
| `0dc16e049fa28f95b55f` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h0 / 17 -> 18 -> 200 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\scenes\ma_pac_cvi_08_01_briefing.scene` / scene / 302 -> 284 -> 290 |
| `142602fb51c7097534c2` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h1488 / 14 -> 32 -> 36 |
| `19098ef4ea0455504efd` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h0 / 163 -> 178 -> 271 |
| `240148efc76953d1c5d4` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h0 / 111 -> 114 -> 115 |
| `3560b3719769da7fd9fe` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h0 / 22 -> 238 -> 8 |
| `7e96257d321df1ad0991` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h0 / 280 -> 211 -> 239 |
| `810443fba2ed6907db9b` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h1488 / 32 -> 36 -> 19 |
| `a0f32b652b7e50e9d29a` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h0 / 154 -> 110 -> 120 |
| `a909c836470d2b0e7fbc` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\ma_pac_cvi_08_phase.questphase` / h1380 / 0 -> 10 -> 1 |
| `ac5b347c9518873a2790` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\scenes\ma_pac_cvi_08_01_briefing.scene` / scene / 284 -> 290 -> 288 |
| `bbf9efd740881cf31a37` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_08\scenes\ma_pac_cvi_08_01_briefing.scene` / scene / 299 -> 302 -> 284 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
