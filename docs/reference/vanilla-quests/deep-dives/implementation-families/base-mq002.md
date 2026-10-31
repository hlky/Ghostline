# base-mq002

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq002\mq002_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq002\mq002_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq002\mq002_quest_bugfixes.questphase` | repair | 5 / 0 |  |
| `base\quest\minor_quests\mq002\communities\mq002_nomads.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq002\communities\mq002_scavengers.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq002\communities\mq002_vehicles.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq002\mq002.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq002\mq002.quest` | content candidate | 3 / 0 | base\quest\minor_quests\mq002\mq002.questphase; base\quest\minor_quests\mq002\test\mq002_00_chicken.scene |
| `base\quest\minor_quests\mq002\mq002.questphase` | content candidate | 7 / 0 | base\quest\minor_quests\mq002\phases\mq002_beginning.questphase; base\quest\minor_quests\mq002\phases\mq002_combat.questphase; base\quest\minor_quests\mq002\phases\mq002_ending.questphase; base\quest\minor_quests\mq002\scenes\mq002_04_nomads_fluff.scene |
| `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` | content candidate | 3 / 0 | base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene |
| `base\quest\minor_quests\mq002\phases\mq002_combat.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene; base\quest\minor_quests\mq002\scenes\mq002_02_combat.scene |
| `base\quest\minor_quests\mq002\phases\mq002_ending.questphase` | content candidate | 3 / 0 | base\quest\minor_quests\mq002\scenes\mq002_03_summary.scene |
| `base\quest\minor_quests\mq002\scenes\mq002_00_chicken.scene` | content candidate | 0 / 8 |  |
| `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` | content candidate | 0 / 130 |  |
| `base\quest\minor_quests\mq002\scenes\mq002_02_combat.scene` | content candidate | 0 / 6 |  |
| `base\quest\minor_quests\mq002\scenes\mq002_03_summary.scene` | content candidate | 0 / 85 |  |
| `base\quest\minor_quests\mq002\scenes\mq002_04_nomads_fluff.scene` | content candidate | 0 / 11 |  |
| `base\quest\minor_quests\mq002\test\mq002_00_chicken.scene` | test/debug | 0 / 8 |  |

## Journal paths observed in these resources

- `contacts/carol/mq002_escaped`
- `contacts/carol/mq002_post_veterans/02_ch_response`
- `contacts/carol/mq002_post_veterans/mq002_escaped`
- `points_of_interest/minor_quests/mq002_veterans`
- `quests/minor_quest/mq002_veterans`
- `quests/minor_quest/mq002_veterans/mq002_veterans/01_intro`
- `quests/minor_quest/mq002_veterans/mq002_veterans/01_intro/mq002_description`
- `quests/minor_quest/mq002_veterans/mq002_veterans/02_deal`
- `quests/minor_quest/mq002_veterans/mq002_veterans/03_fight`
- `quests/minor_quest/mq002_veterans/mq002_veterans/04_summary`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 6 |
| `questCheckpointNodeDefinition` | 1 |
| `questCombatNodeDefinition` | 33 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 9 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterEquippedItem_ConditionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterWorkspot_ConditionType]` | 1 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 16 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 4 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 16 |
| `questEndNodeDefinition` | 1 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 17 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 32 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 6 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 30 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 20 |
| `questLogicalAndNodeDefinition` | 14 |
| `questLogicalHubNodeDefinition` | 28 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 12 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 3 |
| `questOutputNodeDefinition` | 33 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 13 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 11 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 6 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 7 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPhaseNodeDefinition` | 20 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questPhoneManagerNodeDefinition[questSendMessage_NodeType]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 17 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 7 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 5 |
| `questSceneNodeDefinition[scnInterruptionScenarioId,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 8 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 34 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 27 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 3 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 19 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 52 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 4 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 12 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 4 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 8 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questFactsDBCondition,questStatsCondition,questUniversalRef,questVarComparison_ConditionType,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questFactsDBCondition,questLifePath_ConditionType,questLogicalCondition,questStatsCondition,questUniversalRef,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questLifePath_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnCutControlNode[scnNodeId]` | 3 |
| `scnEndNode[scnNodeId]` | 15 |
| `scnHubNode[scnNodeId]` | 12 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 55 |
| `scnStartNode[scnNodeId]` | 14 |
| `scnXorNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `823a73d0d8c112114e81` | 8 | `base\quest\minor_quests\mq002\phases\mq002_combat.questphase` / h0 / 120 -> 104 -> 102 |
| `4d1758f6af749c29869c` | 7 | `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` / h0 / 0 -> 60 -> 43 |
| `5b352309f96e054e8092` | 7 | `base\quest\bugfixing\minor_quests\mq002\mq002_quest_bugfixes.questphase` / h154 / 6 -> 7 -> 8 |
| `020a1995079767c97be8` | 6 | `base\quest\minor_quests\mq002\phases\mq002_combat.questphase` / h0 / 0 -> 40 -> 9 |
| `42886fac8a6b1431d294` | 6 | `base\quest\minor_quests\mq002\phases\mq002_beginning.questphase` / h0 / 46 -> 67 -> 73 |
| `69d06609dcd8afcc35b1` | 6 | `base\quest\minor_quests\mq002\mq002.quest` / h32 / 53 -> 54 -> 55 |
| `85ba174646d56b45d66c` | 6 | `base\quest\minor_quests\mq002\mq002.questphase` / h16 / 29 -> 39 -> 41 |
| `b0722b45aabfb4633e6b` | 6 | `base\quest\minor_quests\mq002\phases\mq002_ending.questphase` / h81 / 31 -> 32 -> 43 |
| `19665e3783f6f51a7337` | 5 | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` / scene / 395 -> 385 -> 387 |
| `20a77143a898bc753a26` | 5 | `base\quest\minor_quests\mq002\mq002.questphase` / h16 / 27 -> 29 -> 39 |
| `53fcc8df7d3d3f5e7e49` | 4 | `base\quest\minor_quests\mq002\scenes\mq002_03_summary.scene` / scene / 229 -> 232 -> 45 |
| `8cd3b647ae3f592ad947` | 4 | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` / scene / 311 -> 305 -> 312 |
| `e385c6fc9436a3c9f7d2` | 4 | `base\quest\minor_quests\mq002\phases\mq002_ending.questphase` / h81 / 18 -> 15 -> 39 |
| `045316bbf4dc2ccf8aca` | 3 | `base\quest\minor_quests\mq002\phases\mq002_ending.questphase` / h81 / 7 -> 11 -> 14 |
| `146d03d186468f0e231d` | 3 | `base\quest\minor_quests\mq002\phases\mq002_ending.questphase` / h81 / 6 -> 10 -> 14 |
| `27faccd7b30abbc3add2` | 3 | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` / scene / 116 -> 121 -> 125 |
| `3bfe06739d5bfa31d0df` | 3 | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` / scene / 136 -> 37 -> 89 |
| `3f413cd7823887ad5c9d` | 3 | `base\quest\minor_quests\mq002\mq002.questphase` / h295 / 15 -> 39 -> 21 |
| `4518cc0fb86e98005539` | 3 | `base\quest\minor_quests\mq002\scenes\mq002_01_deal.scene` / scene / 395 -> 385 -> 389 |
| `687d05e5eba3e370dbfc` | 3 | `base\quest\minor_quests\mq002\phases\mq002_combat.questphase` / h0 / 24 -> 36 -> 129 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
