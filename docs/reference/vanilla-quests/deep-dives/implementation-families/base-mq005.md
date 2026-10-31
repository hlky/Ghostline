# base-mq005

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq005\mq005_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq005\mq005_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq005\mq005_quest_bugfixes.questphase` | repair | 5 / 0 |  |
| `base\quest\minor_quests\mq005\communities\mq005_alley.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq005\communities\mq005_corpo.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq005\mq005.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq005\mq005.quest` | content candidate | 2 / 0 | base\quest\minor_quests\mq005\mq005.questphase |
| `base\quest\minor_quests\mq005\mq005.questphase` | content candidate | 7 / 0 | base\quest\minor_quests\mq005\phases\mq005_combat.questphase; base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene |
| `base\quest\minor_quests\mq005\phases\mq005_combat.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` | content candidate | 0 / 156 |  |
| `base\quest\minor_quests\mq005\scenes\mq005_02_passout.scene` | content candidate | 0 / 88 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq005_alley`
- `quests/minor_quest/mq005_alley`
- `quests/minor_quest/mq005_alley/mq005_main/01_deal_with_cops`
- `quests/minor_quest/mq005_alley/mq005_main/01_deal_with_cops/description`
- `quests/minor_quest/mq005_alley/mq005_main/02_check_on_corpo`
- `quests/minor_quest/mq005_alley/mq005_main/03_talk_to_corpo`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 3 |
| `questConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 7 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 16 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerSetMeshAppearance_NodeType,questEntityManagerSetMeshAppearance_NodeTypeParams]` | 2 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 12 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 1 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 5 |
| `questInputNodeDefinition` | 18 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 10 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 9 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 5 |
| `questOutputNodeDefinition` | 20 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questSensesCondition,questStimuli_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 26 |
| `questPauseConditionNodeDefinition[questSensesCondition,questStimuli_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 8 |
| `questPhaseNodeDefinition` | 12 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 3 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 3 |
| `questSceneManagerNodeDefinition[questPlayerLookAt_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier2Params_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 3 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 7 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questTimeManagerNodeDefinition[questPauseTime_NodeType]` | 2 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 3 |
| `questTimeManagerNodeDefinition[questShiftTime_NodeType]` | 2 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Pause]` | 2 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 3 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Reset]` | 1 |
| `questUIManagerNodeDefinition[questBriefingSequencePlayer_NodeType]` | 4 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 4 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 10 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 15 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 4 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 3 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 4 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 8 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 6 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `scnAndNode[scnNodeId]` | 2 |
| `scnChoiceNode[questBuild_ConditionType,questFactsDBCondition,questLifePath_ConditionType,questStatsCondition,questUniversalRef,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questFactsDBCondition,questStatsCondition,questUniversalRef,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questLifePath_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 10 |
| `scnHubNode[scnNodeId]` | 15 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 34 |
| `scnStartNode[scnNodeId]` | 5 |
| `scnXorNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `d18fd8da12f6125e7cd7` | 4 | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 13 -> 763 -> 768 |
| `e6c034452fb22e1aa2ae` | 4 | `base\quest\minor_quests\mq005\mq005.questphase` / h155 / 55 -> 56 -> 38 |
| `016828d499c85128303c` | 3 | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 87 -> 146 -> 148 |
| `3d9b7b29af3679d956a5` | 3 | `base\quest\minor_quests\mq005\scenes\mq005_02_passout.scene` / scene / 443 -> 441 -> 102 |
| `4ab969b9b8dad9007c23` | 3 | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 13 -> 20 -> 28 |
| `5b8d468e40a9e8e44995` | 3 | `base\quest\minor_quests\mq005\scenes\mq005_02_passout.scene` / scene / 262 -> 134 -> 168 |
| `6b700e5d9619de6be7fd` | 3 | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 559 -> 561 -> 581 |
| `8ebefcfc9102e835a4ad` | 3 | `base\quest\bugfixing\minor_quests\mq005\mq005_quest_bugfixes.questphase` / h125 / 3 -> 4 -> 16 |
| `bbf9efd740881cf31a37` | 3 | `base\quest\minor_quests\mq005\scenes\mq005_02_passout.scene` / scene / 126 -> 427 -> 364 |
| `cbe76f380045051d4069` | 3 | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 13 -> 20 -> 26 |
| `d8b43a750106e00731cd` | 3 | `base\quest\minor_quests\mq005\scenes\mq005_02_passout.scene` / scene / 122 -> 427 -> 364 |
| `eb635bf47220523d375d` | 3 | `base\quest\minor_quests\mq005\phases\mq005_combat.questphase` / h0 / 8 -> 5 -> 11 |
| `0236274376628b1bf905` | 2 | `base\quest\minor_quests\mq005\mq005.questphase` / h47 / 28 -> 31 -> 33 |
| `02e694b495c585b442cb` | 2 | `base\quest\minor_quests\mq005\scenes\mq005_02_passout.scene` / scene / 128 -> 262 -> 134 |
| `10cb0db4b40119794b29` | 2 | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 702 -> 705 -> 707 |
| `1d98494813d573ece995` | 2 | `base\quest\minor_quests\mq005\scenes\mq005_02_passout.scene` / scene / 168 -> 102 -> 16 |
| `2db3e1661fe5804a07ae` | 2 | `base\quest\minor_quests\mq005\scenes\mq005_02_passout.scene` / scene / 86 -> 434 -> 452 |
| `2eb8a5936390411dacb1` | 2 | `base\quest\minor_quests\mq005\scenes\mq005_02_passout.scene` / scene / 168 -> 102 -> 237 |
| `3d623333f3ec65214dc8` | 2 | `base\quest\minor_quests\mq005\mq005.questphase` / h47 / 44 -> 28 -> 31 |
| `41f306702e7e11c219f4` | 2 | `base\quest\minor_quests\mq005\scenes\mq005_01_alley.scene` / scene / 158 -> 648 -> 649 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
