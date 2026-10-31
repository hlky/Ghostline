# base-mq010

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq010\mq010_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq010\mq010_quest_bugfixes.questphase` | repair | 13 / 0 |  |
| `base\quest\minor_quests\mq010\communities\mq010_barry.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq010\communities\mq010_ncpd.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq010\mq010.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq010\mq010.quest` | content candidate | 1 / 0 | base\quest\minor_quests\mq010\mq010.questphase; base\quest\minor_quests\mq010\test\mq010_00_chicken_test.scene |
| `base\quest\minor_quests\mq010\mq010.questphase` | content candidate | 6 / 0 | base\quest\minor_quests\mq010\phases\mq010_01_start.questphase; base\quest\minor_quests\mq010\phases\mq010_02_barry_talk.questphase; base\quest\minor_quests\mq010\phases\mq010_03_columbarium.questphase; base\quest\minor_quests\mq010\phases\mq010_04_finale.questphase; base\quest\minor_quests\mq010\phases\mq010_cleanup.questphase |
| `base\quest\minor_quests\mq010\phases\mq010_01_start.questphase` | content candidate | 3 / 0 | base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene |
| `base\quest\minor_quests\mq010\phases\mq010_02_barry_talk.questphase` | content candidate | 4 / 0 | base\quest\minor_quests\mq010\scenes\mq010_02_barry_talk.scene |
| `base\quest\minor_quests\mq010\phases\mq010_03_columbarium.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq010\scenes\mq010_03_columbarium.scene |
| `base\quest\minor_quests\mq010\phases\mq010_04_barry_combat.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq010\phases\mq010_04_finale.questphase` | content candidate | 3 / 0 | base\quest\minor_quests\mq010\scenes\mq010_04_police_talk.scene; base\quest\minor_quests\mq010\scenes\mq010_05_barry_shot.scene |
| `base\quest\minor_quests\mq010\phases\mq010_cleanup.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` | content candidate | 0 / 148 |  |
| `base\quest\minor_quests\mq010\scenes\mq010_02_barry_talk.scene` | content candidate | 0 / 192 |  |
| `base\quest\minor_quests\mq010\scenes\mq010_03_columbarium.scene` | content candidate | 0 / 99 |  |
| `base\quest\minor_quests\mq010\scenes\mq010_04_police_talk.scene` | content candidate | 0 / 184 |  |
| `base\quest\minor_quests\mq010\scenes\mq010_05_barry_shot.scene` | content candidate | 0 / 56 |  |
| `base\quest\minor_quests\mq010\test\mq010_00_chicken_test.scene` | test/debug | 0 / 6 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq010_barry`
- `quests/minor_quest/mq010_barry`
- `quests/minor_quest/mq010_barry/desc`
- `quests/minor_quest/mq010_barry/mq010_barry/01_hook`
- `quests/minor_quest/mq010_barry/mq010_barry/02_wait_for_barry`
- `quests/minor_quest/mq010_barry/mq010_barry/03_talk_to_barry`
- `quests/minor_quest/mq010_barry/mq010_barry/03a_try_talking_to_barry`
- `quests/minor_quest/mq010_barry/mq010_barry/03a_try_talking_to_barry/barry_mp`
- `quests/minor_quest/mq010_barry/mq010_barry/03a_try_talking_to_barry/barry_person_mp`
- `quests/minor_quest/mq010_barry/mq010_barry/04_columbarium`
- `quests/minor_quest/mq010_barry/mq010_barry/04_columbarium/niche`
- `quests/minor_quest/mq010_barry/mq010_barry/04a_andrew_plaque`
- `quests/minor_quest/mq010_barry/mq010_barry/05_tell_police`
- `quests/minor_quest/mq010_barry/mq010_barry/05a_talk_to_barry`
- `quests/minor_quest/mq010_barry/mq010_barry/06_see_what_happened`
- `quests/minor_quest/mq010_barry/mq010_barry/07_defeat_barry`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 3 |
| `questCheckpointNodeDefinition` | 7 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 6 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterWorkspot_ConditionType]` | 2 |
| `questConditionNodeDefinition[questDevice_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 3 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 5 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 39 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 11 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 11 |
| `questConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 4 |
| `questConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 11 |
| `questCutControlNodeDefinition` | 9 |
| `questDeletionMarkerNodeDefinition` | 36 |
| `questEndNodeDefinition` | 1 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 2 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 89 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 25 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 3 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 2 |
| `questInputNodeDefinition` | 40 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 53 |
| `questInteractiveObjectManagerNodeDefinition[questSetInteractionState_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 47 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 24 |
| `questLogicalXorNodeDefinition` | 12 |
| `questMappinManagerNodeDefinition` | 5 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questObservableUniversalRef,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 7 |
| `questOutputNodeDefinition` | 36 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questMenuState_ConditionType,questObjectDistance,questSystemCondition,questUICondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questGameTimeDelay_ConditionType,questLogicalCondition,questMenuState_ConditionType,questSystemCondition,questTimeCondition,questUICondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questDevice_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questSensesCondition,questStimuli_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterQuickHackUploadBegin_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterQuickHacked_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterWorkspot_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questFactsDBCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 16 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 19 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 7 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 56 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 38 |
| `questPhaseNodeDefinition` | 27 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 5 |
| `questRandomizerNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 4 |
| `questSceneManagerNodeDefinition[questNPCLookAt_NodeType]` | 4 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 8 |
| `questSceneNodeDefinition[scnCheckPlayerTargetNodeDistanceInterruptCondition,scnCheckPlayerTargetNodeDistanceInterruptConditionParams,scnCheckPlayerTargetNodeDistanceReturnCondition,scnCheckPlayerTargetNodeDistanceReturnConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceReturnCondition,scnCheckSpeakersDistanceReturnConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceReturnCondition,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 29 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questTimeManagerNodeDefinition[questPauseTime_NodeType]` | 2 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 55 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 76 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 9 |
| `scnAndNode[scnNodeId]` | 19 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 9 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 7 |
| `scnDeletionMarkerNode[scnNodeId]` | 7 |
| `scnEndNode[scnNodeId]` | 20 |
| `scnHubNode[scnNodeId]` | 77 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 2 |
| `scnRandomizerNode[scnNodeId]` | 27 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 107 |
| `scnStartNode[scnNodeId]` | 12 |
| `scnXorNode[scnNodeId]` | 12 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `43d1a3cdcdcb1d73aed9` | 30 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 721 -> 711 -> 709 |
| `6301eecf83656b7e9f6a` | 18 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 713 -> 719 -> 747 |
| `f1dc3e63bf5cc9e5aaca` | 15 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 735 -> 741 -> 747 |
| `0a00bd6805b0f812c475` | 11 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 707 -> 721 -> 711 |
| `43070478f7d2220e3840` | 11 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 711 -> 709 -> 717 |
| `6161899949641b1322f8` | 11 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 709 -> 717 -> 719 |
| `715597e2ef84d7c2f287` | 11 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 711 -> 709 -> 713 |
| `75f2a2db67c95c4ed398` | 11 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 709 -> 713 -> 719 |
| `7dc40c4a4f71dee751f4` | 11 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 711 -> 709 -> 715 |
| `c4062ffedb36bf739c0b` | 11 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 707 -> 723 -> 711 |
| `c4474a851d9f493aa42d` | 11 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 709 -> 715 -> 719 |
| `eaf5aab427d50e5598b6` | 11 | `base\quest\bugfixing\minor_quests\mq010\mq010_quest_bugfixes.questphase` / h30 / 0 -> 8 -> 2 |
| `03b3408e98988baf6c1d` | 6 | `base\quest\minor_quests\mq010\phases\mq010_01_start.questphase` / h181 / 45 -> 47 -> 38 |
| `0590e39c0ff1cd51d807` | 6 | `base\quest\minor_quests\mq010\phases\mq010_01_start.questphase` / h181 / 25 -> 30 -> 20 |
| `389f3b0a5de025334dcd` | 6 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 747 -> 749 -> 705 |
| `451a7517ed2796785e1d` | 6 | `base\quest\minor_quests\mq010\phases\mq010_01_start.questphase` / h181 / 40 -> 47 -> 38 |
| `46635e7469c8efc9538e` | 6 | `base\quest\minor_quests\mq010\phases\mq010_01_start.questphase` / h181 / 46 -> 47 -> 38 |
| `5f90091008687c940696` | 6 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 933 -> 749 -> 705 |
| `69608e6a9dba0faa1d01` | 6 | `base\quest\minor_quests\mq010\phases\mq010_01_start.questphase` / h181 / 38 -> 25 -> 30 |
| `7ff0eae411231e617b77` | 6 | `base\quest\minor_quests\mq010\scenes\mq010_01_ncpd_door.scene` / scene / 48 -> 52 -> 966 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
