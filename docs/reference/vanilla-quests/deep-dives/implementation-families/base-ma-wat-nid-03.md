# base-ma-wat-nid-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\communities\ma_wat_nid_03.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase; base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` | content candidate | 6 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_03\scenes\ma_wat_nid_03_brief.scene; base\open_world\minor_activities\watson\northside\ma_wat_nid_03\scenes\ma_wat_nid_03_scene.scene |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\scenes\ma_wat_nid_03_brief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\scenes\ma_wat_nid_03_scene.scene` | content candidate | 0 / 10 |  |
| `base\quest\bugfixing\minor_quests\ma_wat_nid_03\ma_wat_nid_03_quest_bugfixes.questphase` | repair | 5 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase |

## Journal paths observed in these resources

- `contacts/regina_jones/ma_wat_nid_03/00_msg_rejected`
- `contacts/regina_jones/ma_wat_nid_03/00_msg_start`
- `contacts/regina_jones/ma_wat_nid_03/01_ch_info`
- `contacts/regina_jones/ma_wat_nid_03/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_wat_nid_03/01_ch_info_lethal`
- `contacts/regina_jones/ma_wat_nid_03/01_ch_info_lethal/02_ch_info_lethal`
- `contacts/regina_jones/ma_wat_nid_03/02_msg_regina`
- `contacts/regina_jones/ma_wat_nid_03/03_msg_regina_lethal`
- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_03/onscreens/ma_wat_nid_03_brick_and_elly`
- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_03/onscreens/ma_wat_nid_03_go_clean_after_elly`
- `points_of_interest/minor_quests/ma_wat_nid_03`
- `quests/minor_quest/ma_wat_nid_03`
- `quests/minor_quest/ma_wat_nid_03/description`
- `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03`
- `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/check_shard`
- `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/check_shard_02`
- `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/find`
- `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/kill`
- `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/search_for_clues`
- `quests/minor_quest/ma_wat_nid_03/ma_wat_nid_03/send_info`
- `quests/side_quest/sq011_johnny/04_nancy/01_get_to_totentanz`
- `quests/side_quest/sq011_johnny/04_nancy/02_talk_to_dumdum`
- `quests/side_quest/sq011_johnny/04_nancy/02_talk_to_gangsters`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 5 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questConditionNodeDefinition[questInventory_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 12 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 15 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 27 |
| `questInputNodeDefinition` | 13 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 3 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questSetLootInteractionAccess_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 36 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 11 |
| `questLogicalXorNodeDefinition` | 8 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 10 |
| `questPauseConditionNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 10 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 13 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questUIManagerNodeDefinition[questToggleMinimapVisibility_NodeSubType]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 1 |
| `questVisionModesManagerNodeDefinition[questSetFocusClueState_NodeType]` | 12 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 2 |
| `scnStartNode[scnNodeId]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `19a5bfbc0b6690f905c3` | 8 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h996 / 8 -> 14 -> 15 |
| `c4cc47f1088342201da5` | 6 | `base\quest\bugfixing\minor_quests\ma_wat_nid_03\ma_wat_nid_03_quest_bugfixes.questphase` / h63 / 9 -> 10 -> 11 |
| `13455132e6fe4cc4bf73` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 50 -> 51 -> 182 |
| `eaf5aab427d50e5598b6` | 3 | `base\quest\bugfixing\minor_quests\ma_wat_nid_03\ma_wat_nid_03_quest_bugfixes.questphase` / h7 / 0 -> 8 -> 2 |
| `0dc16e049fa28f95b55f` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 12 -> 16 -> 17 |
| `0dd59783fd2ca881c5e4` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 99 -> 100 -> 102 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\scenes\ma_wat_nid_03_brief.scene` / scene / 296 -> 278 -> 284 |
| `17ff4f352843f7f881cf` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 99 -> 108 -> 109 |
| `19a3ccd25879b7f6c119` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 107 -> 108 -> 109 |
| `1a87b7d33597a8406eb7` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h996 / 20 -> 22 -> 23 |
| `38e0d20737557467bb74` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 116 -> 119 -> 175 |
| `3e6f03030764fcc75954` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 115 -> 117 -> 116 |
| `52a8e5957844bbdf81b2` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 116 -> 119 -> 120 |
| `539abdcbe41456286e59` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 108 -> 109 -> 111 |
| `6b1fcb4c46676ba8a912` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 206 -> 47 -> 35 |
| `7e7dbbc930b3717fd790` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 206 -> 198 -> 90 |
| `81560ce7cbff639ccdd3` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h996 / 19 -> 20 -> 22 |
| `90a682b6a67b92013949` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 99 -> 100 -> 103 |
| `976bc36bef1c5ed71f92` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 114 -> 143 -> 144 |
| `9af8a87f20a910659fa8` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_03\ma_wat_nid_03.questphase` / h0 / 47 -> 35 -> 46 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
