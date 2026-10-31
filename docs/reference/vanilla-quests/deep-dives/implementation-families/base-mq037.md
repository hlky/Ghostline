# base-mq037

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq037\mq037_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq037\mq037_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq037\mq037_quest_bugfixes.questphase` | repair | 11 / 0 | base\quest\minor_quests\mq037\mq037_brendan.questphase |
| `base\quest\minor_quests\mq037\communities\mq037_characters.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq037\communities\mq037_hooligan.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq037\communities\mq037_service_com.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq037\mq037_brendan.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq037\mq037_brendan.quest` | content candidate | 2 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq037\mq037_brendan.questphase; base\quest\minor_quests\mq037\scenes\mq037_chicken_test.scene |
| `base\quest\minor_quests\mq037\mq037_brendan.questphase` | content candidate | 26 / 0 | base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene |
| `base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene` | content candidate | 0 / 295 |  |
| `base\quest\minor_quests\mq037\scenes\mq037_chicken_test.scene` | test/debug | 0 / 11 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq037_brendan`
- `points_of_interest/minor_quests/mq037_theo`
- `quests/minor_quest/mq037_brendan`
- `quests/minor_quest/mq037_brendan/mq037_brendan/01_go_to_service`
- `quests/minor_quest/mq037_brendan/mq037_brendan/01_go_to_service/description`
- `quests/minor_quest/mq037_brendan/mq037_brendan/02_find_brendan`
- `quests/minor_quest/mq037_brendan/mq037_brendan/02_find_brendan/service_point_door`
- `quests/minor_quest/mq037_brendan/mq037_brendan/02b_ask_clerk`
- `quests/minor_quest/mq037_brendan/mq037_brendan/02c_destroy_turret`
- `quests/minor_quest/mq037_brendan/mq037_brendan/03_talk_brendan`
- `quests/minor_quest/mq037_brendan/mq037_brendan/04_talk_theo`
- `quests/minor_quest/mq037_brendan_dumpster`
- `quests/minor_quest/mq037_brendan_dumpster/mq037_brendan_dumpster/00_push_dumpster`
- `quests/minor_quest/mq037_brendan_dumpster/mq037_brendan_dumpster/01_talk_brendan`
- `quests/minor_quest/mq037_brendan_hooligan001`
- `quests/minor_quest/mq037_brendan_hooligan001/mq037_brendan_hooligan`
- `quests/minor_quest/mq037_brendan_hooligan001/mq037_brendan_hooligan/00_deal_with_the_hooligan`
- `quests/minor_quest/mq037_brendan_hooligan001/mq037_brendan_hooligan/01_talk_with_brendan`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 19 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 1 |
| `questCheckpointNodeDefinition` | 15 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 7 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 24 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSceneCondition,questSceneTalking_ConditionType]` | 8 |
| `questConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 4 |
| `questConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 6 |
| `questCutControlNodeDefinition` | 15 |
| `questDeletionMarkerNodeDefinition` | 23 |
| `questEndNodeDefinition` | 1 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 3 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 30 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 22 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 6 |
| `questInputNodeDefinition` | 64 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 18 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 18 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 59 |
| `questLogicalAndNodeDefinition` | 6 |
| `questLogicalHubNodeDefinition` | 28 |
| `questLogicalXorNodeDefinition` | 12 |
| `questMappinManagerNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 7 |
| `questOutputNodeDefinition` | 54 |
| `questPauseConditionNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterAttack_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questCharacterQuickHacked_ConditionType,questCharacterStatusEffect_CondtionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 19 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 11 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questSceneCondition,questSceneTalking_ConditionType,questSectionNode_ConditionType,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 11 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 16 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 51 |
| `questPhaseNodeDefinition` | 43 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 3 |
| `questRandomizerNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceInterruptConditionParams,scnCheckSpeakersDistanceReturnCondition,scnCheckSpeakersDistanceReturnConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 8 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceInterruptConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 2 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceReturnCondition,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnInterruptionScenarioId,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 9 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 41 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questUIManagerNodeDefinition[questSwitchNameplate_NodeType]` | 7 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 18 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 43 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 9 |
| `scnChoiceNode[questBuild_ConditionType,questPaymentBalanced_ConditionType,questPaymentCondition,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questLifePath_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 15 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 5 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnEndNode[scnNodeId]` | 40 |
| `scnHubNode[scnNodeId]` | 4 |
| `scnRandomizerNode[scnNodeId]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 90 |
| `scnStartNode[scnNodeId]` | 25 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `31659d4f40198759d29d` | 12 | `base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene` / scene / 264 -> 1124 -> 44 |
| `95d4997362b664c5c23b` | 12 | `base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene` / scene / 42 -> 1012 -> 249 |
| `eb252b7e42db30cea85d` | 9 | `base\quest\minor_quests\mq037\mq037_brendan.questphase` / h207 / 12 -> 46 -> 54 |
| `3fe0ae98a8cf5496b004` | 8 | `base\quest\minor_quests\mq037\mq037_brendan.questphase` / h207 / 46 -> 54 -> 55 |
| `18be198845c90c6bb3c8` | 7 | `base\quest\minor_quests\mq037\mq037_brendan.questphase` / h12 / 11 -> 12 -> 13 |
| `78da945d8995f1b18ed6` | 7 | `base\quest\minor_quests\mq037\mq037_brendan.questphase` / h207 / 49 -> 56 -> 46 |
| `987122e5e2fcd167cf6c` | 7 | `base\quest\minor_quests\mq037\mq037_brendan.questphase` / h12 / 0 -> 7 -> 8 |
| `d7e61d8ce95df2f9827f` | 7 | `base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene` / scene / 132 -> 1034 -> 833 |
| `e53af017267e2b173704` | 7 | `base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene` / scene / 249 -> 177 -> 179 |
| `09efa3b5bc8b37b6f16a` | 6 | `base\quest\minor_quests\mq037\mq037_brendan.questphase` / h207 / 55 -> 49 -> 56 |
| `19665e3783f6f51a7337` | 6 | `base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene` / scene / 1 -> 1071 -> 1609 |
| `a74e6b7bff189c2dd431` | 6 | `base\quest\minor_quests\mq037\mq037_brendan.questphase` / h4084 / 2 -> 3 -> 4 |
| `c8ffdbcce8934d2d2ce4` | 6 | `base\quest\minor_quests\mq037\mq037_brendan.questphase` / h207 / 54 -> 55 -> 49 |
| `eaf5aab427d50e5598b6` | 6 | `base\quest\bugfixing\minor_quests\mq037\mq037_quest_bugfixes.questphase` / h52 / 0 -> 4 -> 5 |
| `9380dda43f90ecd62efb` | 5 | `base\quest\minor_quests\mq037\mq037_brendan.questphase` / h2298 / 154 -> 150 -> 152 |
| `cb387f9e924ae670d1e3` | 5 | `base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene` / scene / 1260 -> 1259 -> 1292 |
| `524f7d161de79c38cf96` | 4 | `base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene` / scene / 178 -> 264 -> 652 |
| `658fe17f8b47d2c016b7` | 4 | `base\quest\bugfixing\minor_quests\mq037\mq037_quest_bugfixes.questphase` / h1203 / 0 -> 12 -> 13 |
| `8cd3b647ae3f592ad947` | 4 | `base\quest\minor_quests\mq037\scenes\mq037_01_brendan_scenes.scene` / scene / 669 -> 1338 -> 671 |
| `b9ae1cbcc6435c2f556e` | 4 | `base\quest\minor_quests\mq037\mq037_brendan.questphase` / h2298 / 33 -> 8 -> 9 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
