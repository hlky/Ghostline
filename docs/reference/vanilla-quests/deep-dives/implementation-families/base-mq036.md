# base-mq036

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq036\mq036_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq036\mq036_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` | repair | 13 / 0 |  |
| `base\quest\minor_quests\mq036\communities\mq036_scavengers.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq036\communities\mq036_stefan.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq036\mq036_overload.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq036\mq036_overload.quest` | content candidate | 1 / 0 | base\quest\minor_quests\mq036\mq036_overload.questphase; base\quest\minor_quests\mq036\scenes\mq036_chicken_test.scene |
| `base\quest\minor_quests\mq036\mq036_overload.questphase` | content candidate | 5 / 0 | base\quest\minor_quests\mq036\phases\mq036_01_hook.questphase; base\quest\minor_quests\mq036\phases\mq036_02_scavengers.questphase; base\quest\minor_quests\mq036\phases\mq036_03_finale.questphase |
| `base\quest\minor_quests\mq036\phases\mq036_01_hook.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq036\scenes\mq036_stefan_dialogues.scene |
| `base\quest\minor_quests\mq036\phases\mq036_02_scavengers.questphase` | content candidate | 5 / 0 | base\quest\minor_quests\mq036\phases\mq036_02b_scavengers_combat.questphase; base\quest\minor_quests\mq036\scenes\mq036_scavengers.scene |
| `base\quest\minor_quests\mq036\phases\mq036_02b_scavengers_combat.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq036\phases\mq036_03_finale.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq036\scenes\mq036_stefan_dialogues.scene |
| `base\quest\minor_quests\mq036\scenes\mq036_chicken_test.scene` | test/debug | 0 / 5 |  |
| `base\quest\minor_quests\mq036\scenes\mq036_scavengers.scene` | content candidate | 0 / 54 |  |
| `base\quest\minor_quests\mq036\scenes\mq036_stefan_dialogues.scene` | content candidate | 0 / 118 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq036_overload`
- `quests/minor_quest/mq036_overload`
- `quests/minor_quest/mq036_overload/mq036_overload`
- `quests/minor_quest/mq036_overload/mq036_overload/00_talk_stefan`
- `quests/minor_quest/mq036_overload/mq036_overload/00_talk_stefan/description`
- `quests/minor_quest/mq036_overload/mq036_overload/01_experience_bd`
- `quests/minor_quest/mq036_overload/mq036_overload/02_ask_stefan`
- `quests/minor_quest/mq036_overload/mq036_overload/03_follow_stefan`
- `quests/minor_quest/mq036_overload/mq036_overload/04_use_stefan_player`
- `quests/minor_quest/mq036_overload/mq036_overload/05_escape_hideout`
- `quests/minor_quest/mq036_overload/mq036_overload/05_escape_hideout/elevator`
- `quests/minor_quest/mq036_overload/mq036_overload/05_escape_hideout/hideout_exit`
- `quests/minor_quest/mq036_overload/mq036_overload/05b_retrieve_equipment`
- `quests/minor_quest/mq036_overload/mq036_overload/05b_retrieve_equipment/stolen_equipment_area`
- `quests/minor_quest/mq036_overload/mq036_overload/05c_retrieve_equipment_2`
- `quests/minor_quest/mq036_overload/mq036_overload/05c_retrieve_equipment_2/stolen_equipment`
- `quests/minor_quest/mq036_overload/mq036_overload/06_confront_stefan`
- `quests/street_stories/badlands/inland_avenue/sts_bls_ina_11/find_the_robot/deliver_chip`
- `quests/street_stories/heywood/glen/sts_hey_gle_03/sts_hey_gle_03/drop`
- `quests/street_stories/heywood/glen/sts_hey_gle_05/sts_hey_gle_05/deliver`
- `quests/street_stories/heywood/vista_del_rey/sts_hey_rey_06/sts_hey_rey_06/drop`
- `quests/street_stories/santo_domingo/arroyo/sts_std_arr_01/sts_std_arr_01/drop`
- `quests/street_stories/santo_domingo/rancho_coronado/sts_std_rcr_05/sts_std_rcr_05/deliver`
- `quests/street_stories/watson/kabuki/sts_wat_kab_03/sts_wat_kab_03/retrieve`
- `quests/street_stories/watson/kabuki/sts_wat_kab_05/sts_wat_kab_05/deliver_shard`
- `quests/street_stories/watson/little_china/sts_wat_lch_05/sts_wat_lch_05/exit`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_04/sts_wat_nid_04/get_to_droppoint`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/deliver_files`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_01/sts_wbr_hil_01/drop_point`
- `quests/street_stories/wesbrook/charter_hill/sts_wbr_hil_07/sts_wbr_hil_07/drop_wallet`
- `quests/street_stories/wesbrook/japan_town/sts_wbr_jpn_12/sts_wbr_jpn_12/leave_device_in_droppoint`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 5 |
| `questCheckpointNodeDefinition` | 7 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 16 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 17 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questJournalEntry_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 46 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 2 |
| `questConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 23 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 25 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 23 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 22 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 2 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 2 |
| `questInputNodeDefinition` | 40 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 3 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 6 |
| `questInteractiveObjectManagerNodeDefinition[questElevator_ManageNPCAttachment_NodeType,questElevator_ManageNPCAttachment_NodeTypeParams]` | 1 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 34 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 5 |
| `questItemManagerNodeDefinition[questTransferItem_NodeType,questTransferItems_NodeTypeParams,questTransferItems_NodeTypeParams_OperationData,questTransferItems_NodeTypeParams_TransferAllOperationData,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questTransferItem_NodeType,questTransferItems_NodeTypeParams,questTransferItems_NodeTypeParams_TransferAllOperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 43 |
| `questLogicalAndNodeDefinition` | 10 |
| `questLogicalHubNodeDefinition` | 41 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMappinManagerNodeDefinition` | 8 |
| `questMiscAICommandNode` | 1 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 16 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 5 |
| `questOutputNodeDefinition` | 32 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questRealtimeDelay_ConditionType,questSystemCondition,questTimeCondition,questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterAim_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionFunctionParameter,questDevice_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 15 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questMenuState_ConditionType,questUICondition]` | 2 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 19 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 22 |
| `questPhaseNodeDefinition` | 29 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRandomizerNodeDefinition` | 1 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 5 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 2 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceReturnCondition,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 4 |
| `questSceneNodeDefinition[scnWorldMarker]` | 11 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 19 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 7 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 3 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 4 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 2 |
| `questUIManagerNodeDefinition[questSwitchToScenario_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 14 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 13 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 1 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 3 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questPrefetchStreaming_NodeTypeV2]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 8 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questPaymentBalanced_ConditionType,questPaymentCondition,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 5 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 29 |
| `scnHubNode[scnNodeId]` | 2 |
| `scnRandomizerNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 29 |
| `scnStartNode[scnNodeId]` | 21 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0cd7da0481a442b7cd51` | 15 | `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` / h870 / 200 -> 199 -> 197 |
| `98e7f962a722392aa561` | 15 | `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` / h870 / 199 -> 197 -> 314 |
| `9759ac67f805823706b1` | 13 | `base\quest\minor_quests\mq036\phases\mq036_02b_scavengers_combat.questphase` / h0 / 9 -> 15 -> 16 |
| `abbf46d00a7c0ae464b9` | 13 | `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` / h870 / 194 -> 195 -> 196 |
| `0da1ff18e32f4a5dcc23` | 12 | `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` / h870 / 313 -> 202 -> 205 |
| `552ee7279e2c9dd130fc` | 12 | `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` / h870 / 338 -> 340 -> 342 |
| `eaf5aab427d50e5598b6` | 11 | `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` / h30 / 0 -> 9 -> 2 |
| `4707f2292d1f47d1adec` | 6 | `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` / h361 / 29 -> 24 -> 25 |
| `f2a37207a30c59bac7f0` | 6 | `base\quest\minor_quests\mq036\phases\mq036_02_scavengers.questphase` / h0 / 66 -> 63 -> 177 |
| `f4c2b3190230913ea05b` | 6 | `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` / h120 / 8 -> 2 -> 9 |
| `08c4e4df359270c539b4` | 5 | `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` / h361 / 9 -> 29 -> 24 |
| `748959ebbbf9aeab3a8a` | 5 | `base\quest\minor_quests\mq036\scenes\mq036_stefan_dialogues.scene` / scene / 33 -> 121 -> 123 |
| `bf65a2fd4286a52947d7` | 5 | `base\quest\minor_quests\mq036\phases\mq036_01_hook.questphase` / h0 / 125 -> 159 -> 158 |
| `df2dac3276170dbea4eb` | 5 | `base\quest\minor_quests\mq036\scenes\mq036_chicken_test.scene` / scene / 1 -> 4 -> 2 |
| `047c21b89c4d882935bc` | 4 | `base\quest\minor_quests\mq036\scenes\mq036_stefan_dialogues.scene` / scene / 33 -> 121 -> 132 |
| `0873b5c19806fb9d629a` | 4 | `base\quest\minor_quests\mq036\scenes\mq036_stefan_dialogues.scene` / scene / 33 -> 121 -> 125 |
| `3fe0ae98a8cf5496b004` | 4 | `base\quest\bugfixing\minor_quests\mq036\mq036_quest_bugfixes.questphase` / h30 / 14 -> 12 -> 15 |
| `44e16681fbad62c8e945` | 4 | `base\quest\minor_quests\mq036\scenes\mq036_stefan_dialogues.scene` / scene / 463 -> 97 -> 85 |
| `77ba369444f661cae7b9` | 4 | `base\quest\minor_quests\mq036\phases\mq036_02b_scavengers_combat.questphase` / h0 / 40 -> 45 -> 37 |
| `79ff30ab7464b071eda5` | 4 | `base\quest\minor_quests\mq036\mq036_overload.questphase` / h147 / 2 -> 3 -> 4 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
