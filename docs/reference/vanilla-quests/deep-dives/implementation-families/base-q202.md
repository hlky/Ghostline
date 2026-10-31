# base-q202

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\epilogue\q202\q202_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\epilogue\q202\q202_quest_bugfixes.questphase` | repair | 4 / 0 |  |
| `base\quest\main_quests\epilogue\q202\community\q202_com_drones.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\epilogue\q202\community\q202_convoy_vehicles.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\epilogue\q202\phases\q202_01_one_for_the_road.questphase` | content candidate | 2 / 0 | base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene |
| `base\quest\main_quests\epilogue\q202\phases\q202_02_final_showdown.questphase` | content candidate | 1 / 0 | base\quest\main_quests\epilogue\q202\scenes\q202_04a_badlands_travel.scene; base\quest\main_quests\epilogue\q202\scenes\q202_05_convoy.scene |
| `base\quest\main_quests\epilogue\q202\phases\q202_04_convoy.questphase` | content candidate | 9 / 0 | base\quest\main_quests\epilogue\q202\scenes\q202_05_convoy.scene |
| `base\quest\main_quests\epilogue\q202\phases\q202_border_run.questphase` | content candidate | 6 / 0 | base\quest\main_quests\epilogue\q202\phases\q202_sandstorm_control.questphase; base\quest\main_quests\epilogue\q202\scenes\q202_06_border_running.scene |
| `base\quest\main_quests\epilogue\q202\phases\q202_sandstorm_control.questphase` | content candidate | 1 / 0 |  |
| `base\quest\main_quests\epilogue\q202\phases\q202_world_blocker.questphase` | content candidate | 1 / 0 |  |
| `base\quest\main_quests\epilogue\q202\q202.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\epilogue\q202\q202.quest` | content candidate | 2 / 0 | base\quest\additional_game_elements.questphase; base\quest\main_quests\epilogue\final_boards.questphase; base\quest\main_quests\epilogue\q202\q202.questphase; base\quest\main_quests\epilogue\q202\test\q202_chicken_test.questphase |
| `base\quest\main_quests\epilogue\q202\q202.questphase` | content candidate | 6 / 0 | base\quest\main_quests\epilogue\q202\phases\q202_01_one_for_the_road.questphase; base\quest\main_quests\epilogue\q202\phases\q202_02_final_showdown.questphase; base\quest\main_quests\epilogue\q202\phases\q202_04_convoy.questphase; base\quest\main_quests\epilogue\q202\phases\q202_border_run.questphase; base\quest\main_quests\epilogue\q202\phases\q202_world_blocker.questphase |
| `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` | content candidate | 0 / 214 |  |
| `base\quest\main_quests\epilogue\q202\scenes\q202_04a_badlands_travel.scene` | content candidate | 0 / 116 |  |
| `base\quest\main_quests\epilogue\q202\scenes\q202_05_convoy.scene` | content candidate | 0 / 1095 |  |
| `base\quest\main_quests\epilogue\q202\scenes\q202_06_border_running.scene` | content candidate | 0 / 307 |  |
| `base\quest\main_quests\epilogue\q202\test\q202_chicken_test.questphase` | test/debug | 4 / 0 | base\quest\main_quests\epilogue\q202\test\q202_chicken_test.scene |
| `base\quest\main_quests\epilogue\q202\test\q202_chicken_test.scene` | test/debug | 0 / 25 |  |

## Journal paths observed in these resources

- `contacts/judy`
- `contacts/player`
- `quests/main_quest/epilogues/q202_nomads`
- `quests/main_quest/epilogues/q202_nomads/motel/join_panam`
- `quests/main_quest/epilogues/q202_nomads/motel/join_panam/q202_description`
- `quests/main_quest/epilogues/q202_nomads/motel/motel`
- `quests/main_quest/epilogues/q202_nomads/motel/panams_car`
- `quests/main_quest/epilogues/q202_nomads/temp_river/badlands_drive`
- `quests/main_quest/epilogues/q202_nomads/temp_river/cross_border`
- `quests/main_quest/epilogues/q202_nomads/temp_river/cross_border/mp_middle`
- `quests/main_quest/epilogues/q202_nomads/temp_river/cross_border/mp_middle1`
- `quests/main_quest/epilogues/q202_nomads/temp_river/cross_border/mp_middle2`
- `quests/main_quest/epilogues/q202_nomads/temp_river/cross_border/mp_middle3`
- `quests/main_quest/epilogues/q202_nomads/temp_river/cross_border/mp_start`
- `quests/main_quest/epilogues/q202_nomads/temp_river/cross_border/mp_tunnel`
- `quests/main_quest/epilogues/q202_nomads/temp_river/follow_nomads`
- `quests/main_quest/epilogues/q202_nomads/temp_river/get_on_board`
- `quests/main_quest/epilogues/q202_nomads/temp_river/greet_mitch`
- `quests/main_quest/epilogues/q202_nomads/temp_river/prepare_plan`
- `quests/main_quest/epilogues/q202_nomads/temp_river/romance_surprise`
- `quests/main_quest/epilogues/q202_nomads/temp_river/romance_surprise/judy`
- `quests/main_quest/epilogues/q202_nomads/temp_river/romance_surprise/mp_kerry`
- `quests/main_quest/epilogues/q202_nomads/temp_river/romance_surprise/river`
- `quests/main_quest/epilogues/q202_nomads/temp_river/say_goodbye`
- `quests/main_quest/epilogues/q202_nomads/temp_river/talk_judy`
- `quests/main_quest/epilogues/q202_nomads/temp_river/talk_kerry`
- `quests/main_quest/epilogues/q202_nomads/temp_river/talk_panam`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 7 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 15 |
| `questAudioNodeDefinition[questAudioSetListenerOverrideNodeType]` | 2 |
| `questAudioNodeDefinition[questRadioAnnouncementNodeType,questRadioStationAnnouncementEventStruct]` | 2 |
| `questAudioNodeDefinition[questRadioSongNodeType]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 13 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 12 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 4 |
| `questCheckpointNodeDefinition` | 5 |
| `questCombatNodeDefinition` | 8 |
| `questConditionNodeDefinition[questCharacterBodyType_CondtionType,questCharacterCondition]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 56 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 13 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_ControlCrowd]` | 3 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 6 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 2 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_NodeType,questPlayEnv_NodeTypeParams]` | 5 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 5 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 13 |
| `questEventManagerNodeDefinition` | 13 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 10 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 121 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 3 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 19 |
| `questInputNodeDefinition` | 47 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 12 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 16 |
| `questItemManagerNodeDefinition[questTransferItem_NodeType,questTransferItems_NodeTypeParams,questTransferItems_NodeTypeParams_OperationData,questUniversalRef]` | 4 |
| `questItemManagerNodeDefinition[questTransferItem_NodeType,questTransferItems_NodeTypeParams,questTransferItems_NodeTypeParams_TransferAllOperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 36 |
| `questLogicalAndNodeDefinition` | 11 |
| `questLogicalHubNodeDefinition` | 9 |
| `questLogicalXorNodeDefinition` | 1 |
| `questLookAtDrivenTurnsNode` | 8 |
| `questMappinManagerNodeDefinition` | 14 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 11 |
| `questOutputNodeDefinition` | 40 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 33 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 61 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 17 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 45 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questLogicalCondition,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 12 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 183 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 44 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 7 |
| `questPhaseNodeDefinition` | 34 |
| `questPhoneManagerNodeDefinition[questCallContact_NodeType]` | 2 |
| `questRenderFxManagerNodeDefinition[questEnforceScreenSpaceReflectionsUberQuality_NodeType]` | 2 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 15 |
| `questSceneManagerNodeDefinition[questSetTier2Params_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 4 |
| `questSceneManagerNodeDefinition[questToggleEventExecutionTag_NodeType]` | 3 |
| `questSceneNodeDefinition` | 1 |
| `questSceneNodeDefinition[scnCheckFactInterruptCondition,scnCheckFactInterruptConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnVarComparison_FactConditionType,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnInterruptionScenarioId,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 5 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 10 |
| `questSpawnManagerNodeDefinition[questLegacy_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 53 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 9 |
| `questTimeManagerNodeDefinition[questPauseTime_NodeType]` | 8 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 8 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 1 |
| `questUIManagerNodeDefinition[questAddCombatLogMessage_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questHUDVideo_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 9 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 3 |
| `questUIManagerNodeDefinition[questShowOnscreen_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questSwitchToScenario_NodeType]` | 5 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 9 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 56 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 19 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 147 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 32 |
| `questVehicleNodeDefinition[questEnableVehicleSummon_NodeType]` | 4 |
| `questVehicleNodeDefinition[questMoveOnSplineAndKeepDistance_NodeType]` | 10 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType,scnMarker,scnVehicleMoveOnSpline_Overrides]` | 6 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 7 |
| `questVehicleNodeDefinition[questRequestVehicleCameraPerspective_NodeType]` | 5 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 18 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 24 |
| `questVehicleNodeDefinition[questToggleTankCustomFPPLockOff_NodeType]` | 4 |
| `questVehicleNodeDefinition[questToggleWeaponEnabled_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleWindow_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questPrefetchStreaming_NodeTypeV2]` | 2 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 8 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 27 |
| `scnAndNode[scnNodeId]` | 35 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAdaptiveLookAtReferencePoint,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questCharacterCondition,questCharacterGender_CondtionType,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questLifePath_ConditionType,questStatsCondition,questUniversalRef,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAdaptiveLookAtReferencePoint,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questLifePath_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAdaptiveLookAtReferencePoint,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questRealtimeDelay_ConditionType,questTimeCondition,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questTriggerCondition,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questTriggerCondition,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAdaptiveLookAtReferencePoint,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAdaptiveLookAtReferencePoint,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 6 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 6 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 4 |
| `scnCutControlNode[scnNodeId]` | 38 |
| `scnDeletionMarkerNode[scnNodeId]` | 4 |
| `scnEndNode[scnNodeId]` | 15 |
| `scnHubNode[scnNodeId]` | 206 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 3 |
| `scnRandomizerNode[scnNodeId]` | 85 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 344 |
| `scnStartNode[scnNodeId]` | 31 |
| `scnXorNode[scnNodeId]` | 18 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `43d1a3cdcdcb1d73aed9` | 102 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3332 -> 3327 -> 3326 |
| `6301eecf83656b7e9f6a` | 55 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3328 -> 3331 -> 3345 |
| `f1dc3e63bf5cc9e5aaca` | 38 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3339 -> 3342 -> 3345 |
| `75f2a2db67c95c4ed398` | 33 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3326 -> 3328 -> 3331 |
| `c4062ffedb36bf739c0b` | 32 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3325 -> 3333 -> 3327 |
| `0a00bd6805b0f812c475` | 31 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3325 -> 3332 -> 3327 |
| `715597e2ef84d7c2f287` | 31 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3327 -> 3326 -> 3328 |
| `7dc40c4a4f71dee751f4` | 31 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3327 -> 3326 -> 3329 |
| `c4474a851d9f493aa42d` | 31 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3326 -> 3329 -> 3331 |
| `43070478f7d2220e3840` | 30 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3327 -> 3326 -> 3330 |
| `6161899949641b1322f8` | 30 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3326 -> 3330 -> 3331 |
| `bf01b1069a83f57771e0` | 25 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3337 -> 3336 -> 3343 |
| `c981b41224718d1011ca` | 25 | `base\quest\main_quests\epilogue\q202\scenes\q202_04a_badlands_travel.scene` / scene / 909 -> 857 -> 989 |
| `389f3b0a5de025334dcd` | 22 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3350 -> 3346 -> 3324 |
| `8d8430682bd3063243cd` | 17 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3345 -> 3396 -> 3346 |
| `80691fc5857594ebf785` | 14 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3344 -> 3337 -> 3336 |
| `85f9b7369107e60259aa` | 14 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3344 -> 3337 -> 3335 |
| `a59db2d9257910e67dce` | 14 | `base\quest\main_quests\epilogue\q202\scenes\q202_01_motel.scene` / scene / 3344 -> 3337 -> 3334 |
| `3ed88ad23c24ed5ac9fe` | 12 | `base\quest\main_quests\epilogue\q202\phases\q202_04_convoy.questphase` / h48 / 11 -> 37 -> 50 |
| `44a09e38ff57db871987` | 12 | `base\quest\main_quests\epilogue\q202\phases\q202_01_one_for_the_road.questphase` / h191 / 15 -> 14 -> 28 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
