# base-mq013

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq013\mq013_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq013\mq013_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq013\mq013_quest_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\minor_quests\mq013\communities\mq013_com_punks.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq013\mq013.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq013\mq013.quest` | content candidate | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq013\mq013.questphase; base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene |
| `base\quest\minor_quests\mq013\mq013.questphase` | content candidate | 9 / 0 | base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene |
| `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` | content candidate | 0 / 304 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq013_punks`
- `quests/minor_quest/mq013_punks`
- `quests/minor_quest/mq013_punks/00_punks/00_talk_shopkeep`
- `quests/minor_quest/mq013_punks/00_punks/00_talk_shopkeep/description`
- `quests/minor_quest/mq013_punks/00_punks/01_decide`
- `quests/minor_quest/mq013_punks/00_punks/02_deal_with_punks`
- `quests/minor_quest/mq013_punks/00_punks/03_defeat_punks`
- `quests/minor_quest/mq013_punks/00_punks/04_talk_shopkeep`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAnimset]` | 7 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 6 |
| `questCheckpointNodeDefinition` | 1 |
| `questCombatNodeDefinition` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_PrimaryWeapon]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questStatsCondition,questStreetCredTier_ConditionType,questUniversalRef,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 12 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 3 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 37 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 7 |
| `questInputNodeDefinition` | 19 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 3 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 6 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 26 |
| `questLogicalAndNodeDefinition` | 8 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 2 |
| `questLookAtDrivenTurnsNode` | 4 |
| `questMovePuppetNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 4 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 9 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 5 |
| `questOutputNodeDefinition` | 15 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterAim_ConditionType,questCharacterCondition,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 6 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 13 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questSensesCondition,questStimuli_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 20 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 13 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 4 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 2 |
| `questSceneManagerNodeDefinition[questToggleEventExecutionTag_NodeType]` | 2 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceInterruptConditionParams,scnCheckSpeakersDistanceReturnCondition,scnCheckSpeakersDistanceReturnConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 3 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 20 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 11 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 12 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 14 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 3 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 8 |
| `scnAndNode[scnNodeId]` | 3 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 7 |
| `scnHubNode[scnNodeId]` | 16 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 1 |
| `scnRandomizerNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 52 |
| `scnStartNode[scnNodeId]` | 9 |
| `scnXorNode[scnNodeId]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0b487c56874911c2ea72` | 3 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 587 -> 712 -> 4 |
| `14602f1d8e2176236ee9` | 3 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 1985 -> 1965 -> 2 |
| `1991838a3650aac559ff` | 3 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 587 -> 712 -> 1820 |
| `1b0fdb9a2829108b2482` | 3 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 1475 -> 1488 -> 1489 |
| `7c00a361ea6833882eaf` | 3 | `base\quest\minor_quests\mq013\mq013.questphase` / h1013 / 0 -> 30 -> 11 |
| `9c634ff27b9a7aa77918` | 3 | `base\quest\bugfixing\minor_quests\mq013\mq013_cinematic_bugfixes.questphase` / h0 / 0 -> 10 -> 5 |
| `c25844001203c3d943ee` | 3 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 587 -> 1172 -> 1176 |
| `e72f36ce1236ddc2fc95` | 3 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 989 -> 54 -> 36 |
| `005d784cd70728b8b3df` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 115 -> 109 -> 1560 |
| `0420eee8ee107d9bda02` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 10 -> 740 -> 15 |
| `0695ab0d2ae14d49a9f5` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 2207 -> 2211 -> 345 |
| `0c517c20542d5ebe8715` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 339 -> 10 -> 740 |
| `0e2a81ff74a9a8322515` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 458 -> 2084 -> 2087 |
| `114a422e294610bf1e07` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 522 -> 2204 -> 516 |
| `12f8e2c0e0a36c2e4d93` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 643 -> 354 -> 2207 |
| `1462affee152cfa98d7b` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 756 -> 15 -> 744 |
| `19665e3783f6f51a7337` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 2188 -> 1879 -> 1880 |
| `1cb0f263fe8f6f7af100` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 2207 -> 106 -> 345 |
| `1cf9adcdd8714d9f07e3` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 1276 -> 1537 -> 1546 |
| `1d33498ab6d9606224ae` | 2 | `base\quest\minor_quests\mq013\scenes\mq013_00_punks.scene` / scene / 522 -> 1166 -> 2019 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
