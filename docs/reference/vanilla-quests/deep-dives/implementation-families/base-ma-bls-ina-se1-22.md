# base-ma-bls-ina-se1-22

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\community\ma_bls_ina_se1_22_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase; base\quest\additional_game_elements.questphase |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` | content candidate | 9 / 0 | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_chicken_test.scene` | test/debug | 0 / 7 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_scene.scene` | content candidate | 0 / 3 |  |
| `base\quest\bugfixing\minor_quests\ma_bls_ina_se1_22\ma_bls_ina_se1_22_quest_bugfixes.questphase` | repair | 4 / 0 |  |

## Journal paths observed in these resources

- `contacts/player`
- `contacts/regina_jones`
- `contacts/regina_jones/ma_bls_ina_se1_22/00_msg_rejected`
- `contacts/regina_jones/ma_bls_ina_se1_22/00_msg_start`
- `contacts/regina_jones/ma_bls_ina_se1_22/01_ch_info`
- `contacts/regina_jones/ma_bls_ina_se1_22/01_ch_info/01_ch_info`
- `contacts/regina_jones/ma_bls_ina_se1_22/01_ch_info_lethal`
- `contacts/regina_jones/ma_bls_ina_se1_22/01_ch_info_lethal/01_ch_info_lethal`
- `contacts/regina_jones/ma_bls_ina_se1_22/02_msg_regina`
- `contacts/regina_jones/ma_bls_ina_se1_22/02_msg_regina_lethal`
- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_22/onscreens/ma_bls_ina_se1_22_eli`
- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_22/onscreens/ma_bls_ina_se1_22_loa`
- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_22/onscreens/ma_bls_ina_se1_22_wraith`
- `points_of_interest/minor_quests/ma_bls_ina_se1_22`
- `quests/minor_quest/ma_bls_ina_se1_22`
- `quests/minor_quest/ma_bls_ina_se1_22/description`
- `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/check_shard`
- `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/find`
- `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/kill`
- `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/scan_trail`
- `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/scan_trail/area_002`
- `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/scan_trail/area_003`
- `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/scan_trail/area_004`
- `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/search_for_clues`
- `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/search_for_clues/psycho_body`
- `quests/minor_quest/ma_bls_ina_se1_22/ma_bls_ina_se1_22/send_info`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_ShootAt]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 6 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questTriggerCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questPhoneMuted_ConditionType,questSystemCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questInventory_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 2 |
| `questConditionNodeDefinition[questPhone_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 13 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 17 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 29 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 3 |
| `questInputNodeDefinition` | 15 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 25 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 5 |
| `questLogicalXorNodeDefinition` | 9 |
| `questMappinManagerNodeDefinition` | 4 |
| `questMiscAICommandNode` | 1 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 3 |
| `questOutputNodeDefinition` | 18 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questObjectCondition,questScan_ConditionType,questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questUICondition,questUIElement_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 9 |
| `questPhaseNodeDefinition` | 13 |
| `questRandomizerNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUIManagerNodeDefinition[questToggleMinimapVisibility_NodeSubType]` | 2 |
| `questVehicleNodeDefinition[questToggleBrokenTire_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVisionModesManagerNodeDefinition[questSetFocusClueState_NodeType]` | 12 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 5 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 5 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `19a5bfbc0b6690f905c3` | 9 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h1058 / 9 -> 10 -> 11 |
| `9d0a5f5823d8edd550eb` | 6 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h804 / 61 -> 64 -> 8 |
| `61f09677c83cec936502` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h804 / 61 -> 64 -> 9 |
| `cf5704c4ca77d71989bb` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h1382 / 0 -> 2 -> 3 |
| `e7f4dab64cf88a718cc9` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h0 / 106 -> 164 -> 66 |
| `05da58ffa41a47aeb533` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h0 / 288 -> 287 -> 286 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene` / scene / 287 -> 269 -> 275 |
| `38e0d20737557467bb74` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h0 / 94 -> 97 -> 282 |
| `39df0491f389498c93b5` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h1514 / 3 -> 12 -> 1 |
| `3e6f03030764fcc75954` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h0 / 173 -> 175 -> 174 |
| `52a8e5957844bbdf81b2` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h0 / 94 -> 97 -> 98 |
| `6b1fcb4c46676ba8a912` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h0 / 77 -> 176 -> 11 |
| `7e7dbbc930b3717fd790` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h0 / 30 -> 210 -> 33 |
| `8bd54738c2c85f70192e` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h0 / 221 -> 14 -> 18 |
| `976bc36bef1c5ed71f92` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h0 / 92 -> 172 -> 173 |
| `9af8a87f20a910659fa8` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h0 / 176 -> 11 -> 35 |
| `9c5a553fb3484b812b1c` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h234 / 0 -> 2 -> 6 |
| `a909c836470d2b0e7fbc` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h1238 / 0 -> 5 -> 1 |
| `ac5b347c9518873a2790` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\scenes\ma_bls_ina_se1_22_brief.scene` / scene / 269 -> 275 -> 273 |
| `b12bd332fc204d21befb` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_22\ma_bls_ina_se1_22_phase.questphase` / h0 / 92 -> 172 -> 93 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
