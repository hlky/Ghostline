# base-mq014

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq014\mq014_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq014\mq014_quest_bugfixes.questphase` | repair | 6 / 0 |  |
| `base\quest\minor_quests\mq014\communities\mq014_com_zen.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq014\mq014.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq014\mq014.quest` | content candidate | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq014\mq014.questphase; base\quest\minor_quests\mq014\test\mq014_chicken_test.scene |
| `base\quest\minor_quests\mq014\mq014.questphase` | content candidate | 29 / 0 | base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene; base\quest\minor_quests\mq014\scenes\mq014_02_earth.scene; base\quest\minor_quests\mq014\scenes\mq014_03_second.scene; base\quest\minor_quests\mq014\scenes\mq014_04_water.scene; base\quest\minor_quests\mq014\scenes\mq014_05_third.scene; base\quest\minor_quests\mq014\scenes\mq014_06_fire.scene; base\quest\minor_quests\mq014\scenes\mq014_07_fourth.scene; base\quest\minor_quests\mq014\scenes\mq014_08_air.scene |
| `base\quest\minor_quests\mq014\phases\mq014_altar.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene` | content candidate | 0 / 121 |  |
| `base\quest\minor_quests\mq014\scenes\mq014_02_earth.scene` | content candidate | 0 / 27 |  |
| `base\quest\minor_quests\mq014\scenes\mq014_03_second.scene` | content candidate | 0 / 107 |  |
| `base\quest\minor_quests\mq014\scenes\mq014_04_water.scene` | content candidate | 0 / 30 |  |
| `base\quest\minor_quests\mq014\scenes\mq014_05_third.scene` | content candidate | 0 / 109 |  |
| `base\quest\minor_quests\mq014\scenes\mq014_06_fire.scene` | content candidate | 0 / 26 |  |
| `base\quest\minor_quests\mq014\scenes\mq014_07_fourth.scene` | content candidate | 0 / 106 |  |
| `base\quest\minor_quests\mq014\scenes\mq014_08_air.scene` | content candidate | 0 / 30 |  |
| `base\quest\minor_quests\mq014\test\mq014_chicken_test.scene` | test/debug | 0 / 19 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq014_first`
- `points_of_interest/minor_quests/mq014_fourth`
- `points_of_interest/minor_quests/mq014_second`
- `points_of_interest/minor_quests/mq014_third`
- `quests/minor_quest/mq014_02_second`
- `quests/minor_quest/mq014_02_second/02_second/01_approach_master`
- `quests/minor_quest/mq014_02_second/02_second/01_approach_master/description`
- `quests/minor_quest/mq014_02_second/02_second/02_talk_sranger`
- `quests/minor_quest/mq014_02_second/02_second/03_come_back`
- `quests/minor_quest/mq014_02_second/02_second/04_earth`
- `quests/minor_quest/mq014_03_third`
- `quests/minor_quest/mq014_03_third/03_third/01_approach_master`
- `quests/minor_quest/mq014_03_third/03_third/01_approach_master/description`
- `quests/minor_quest/mq014_03_third/03_third/02_talk_sranger`
- `quests/minor_quest/mq014_03_third/03_third/03_come_back`
- `quests/minor_quest/mq014_03_third/03_third/04_earth`
- `quests/minor_quest/mq014_04_fourth`
- `quests/minor_quest/mq014_04_fourth/04_fourth/01_approach_master`
- `quests/minor_quest/mq014_04_fourth/04_fourth/01_approach_master/description`
- `quests/minor_quest/mq014_04_fourth/04_fourth/02_talk_sranger`
- `quests/minor_quest/mq014_04_fourth/04_fourth/03_come_back`
- `quests/minor_quest/mq014_04_fourth/04_fourth/04_earth`
- `quests/minor_quest/mq014_04_fourth/04_fourth/05_talk_johhny`
- `quests/minor_quest/mq014_zen`
- `quests/minor_quest/mq014_zen/01_hook/01_approach_master`
- `quests/minor_quest/mq014_zen/01_hook/01_approach_master/description`
- `quests/minor_quest/mq014_zen/01_hook/02_talk_sranger`
- `quests/minor_quest/mq014_zen/01_hook/03_come_back`
- `quests/minor_quest/mq014_zen/01_hook/04_earth`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 12 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 8 |
| `questCheckpointNodeDefinition` | 19 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 6 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 20 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 12 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 5 |
| `questConditionNodeDefinition[questTimeCondition,questTimePeriod_ConditionType]` | 96 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_ControlCrowd]` | 8 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 9 |
| `questEndNodeDefinition` | 1 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 9 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 155 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 38 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 4 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 17 |
| `questInputNodeDefinition` | 50 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 12 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 46 |
| `questLogicalAndNodeDefinition` | 16 |
| `questLogicalHubNodeDefinition` | 20 |
| `questLogicalXorNodeDefinition` | 9 |
| `questOutputNodeDefinition` | 33 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 8 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 14 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questTriggerCondition]` | 8 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 54 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 9 |
| `questPhaseNodeDefinition` | 23 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 13 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 9 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 18 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 4 |
| `questSceneManagerNodeDefinition[questCameraClippingPlane_NodeType]` | 8 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 10 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceReturnCondition,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 4 |
| `questSceneNodeDefinition[scnWorldMarker]` | 9 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 15 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 14 |
| `questTimeManagerNodeDefinition[questPauseTime_NodeType]` | 8 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 100 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 8 |
| `questUIManagerNodeDefinition[questSwitchNameplate_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 9 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 24 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 17 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 11 |
| `questWorldDataManagerNodeDefinition[questPrefetchStreaming_NodeTypeV2]` | 8 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 13 |
| `scnAndNode[scnNodeId]` | 9 |
| `scnChoiceNode[questPaymentCondition,questPaymentFixedAmount_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[questPaymentCondition,questPaymentFixedAmount_ConditionType,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 6 |
| `scnCutControlNode[scnNodeId]` | 7 |
| `scnDeletionMarkerNode[scnNodeId]` | 7 |
| `scnEndNode[scnNodeId]` | 20 |
| `scnHubNode[scnNodeId]` | 17 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 13 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 129 |
| `scnStartNode[scnNodeId]` | 22 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `8770a8afded2e6b76c8d` | 84 | `base\quest\minor_quests\mq014\mq014.questphase` / h254 / 8 -> 10 -> 11 |
| `c4a2d3eb05576951cf29` | 72 | `base\quest\minor_quests\mq014\mq014.questphase` / h254 / 8 -> 10 -> 12 |
| `c6a14c1e0b6c546be649` | 20 | `base\quest\minor_quests\mq014\mq014.questphase` / h643 / 12 -> 38 -> 50 |
| `b50ef97634bf3be1b794` | 14 | `base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene` / scene / 289 -> 244 -> 221 |
| `77b88fc2cf6dc1bce649` | 12 | `base\quest\bugfixing\minor_quests\mq014\mq014_quest_bugfixes.questphase` / h30 / 26 -> 30 -> 31 |
| `cfd5544f57c93f1b3982` | 12 | `base\quest\bugfixing\minor_quests\mq014\mq014_quest_bugfixes.questphase` / h30 / 2 -> 54 -> 24 |
| `296177e0447538f90b69` | 8 | `base\quest\minor_quests\mq014\mq014.questphase` / h254 / 16 -> 50 -> 18 |
| `3cf8a288506529068bc4` | 8 | `base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene` / scene / 1718 -> 1712 -> 1716 |
| `55731392862de80e5f85` | 8 | `base\quest\minor_quests\mq014\mq014.questphase` / h254 / 50 -> 18 -> 20 |
| `79bd1f6c32d5067e568c` | 8 | `base\quest\minor_quests\mq014\mq014.questphase` / h254 / 14 -> 16 -> 50 |
| `840152ea8e30e28cf9bc` | 8 | `base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene` / scene / 1714 -> 1710 -> 1712 |
| `9e580ecab33f42d59794` | 8 | `base\quest\bugfixing\minor_quests\mq014\mq014_quest_bugfixes.questphase` / h30 / 30 -> 31 -> 28 |
| `b411afa897665cf92c49` | 8 | `base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene` / scene / 98 -> 100 -> 198 |
| `c473d9785eacb6f771eb` | 8 | `base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene` / scene / 1718 -> 1710 -> 1712 |
| `d2be64f1c87d382cdba6` | 8 | `base\quest\bugfixing\minor_quests\mq014\mq014_quest_bugfixes.questphase` / h30 / 28 -> 29 -> 30 |
| `d573cf2903db5ea7bf9e` | 8 | `base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene` / scene / 1567 -> 303 -> 305 |
| `d8eec3a204d6109b3f0f` | 8 | `base\quest\minor_quests\mq014\mq014.questphase` / h254 / 50 -> 18 -> 19 |
| `e5528a16e3da41d6e43d` | 8 | `base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene` / scene / 1710 -> 1712 -> 1716 |
| `e5ea308bac4111527171` | 8 | `base\quest\bugfixing\minor_quests\mq014\mq014_quest_bugfixes.questphase` / h30 / 31 -> 28 -> 29 |
| `5bad1fe50183293cd1dd` | 7 | `base\quest\minor_quests\mq014\scenes\mq014_01_hook.scene` / scene / 1737 -> 1718 -> 1712 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
