# base-mq032

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq032\mq032_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq032\mq032_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq032\mq032_quest_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\minor_quests\mq032\characters\mq032_maelstrom.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq032\characters\mq032_monk_brother.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq032\characters\mq032_monk_cyberware.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq032\mq032_sacrum.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq032\mq032_sacrum.quest` | content candidate | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq032\mq032_sacrum.questphase; base\quest\minor_quests\mq032\scenes\mq032_00_chicken_test_setup.scene |
| `base\quest\minor_quests\mq032\mq032_sacrum.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase; base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase; base\quest\minor_quests\mq032\phases\mq032_03_epilogue.questphase |
| `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene |
| `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` | content candidate | 4 / 0 | base\quest\minor_quests\mq032\phases\mq032_combat.questphase; base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene; base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene |
| `base\quest\minor_quests\mq032\phases\mq032_03_epilogue.questphase` | content candidate | 4 / 0 | base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene |
| `base\quest\minor_quests\mq032\phases\mq032_combat.questphase` | content candidate | 3 / 0 |  |
| `base\quest\minor_quests\mq032\scenes\mq032_00_chicken_test_setup.scene` | test/debug | 0 / 10 |  |
| `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` | content candidate | 0 / 78 |  |
| `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene` | content candidate | 0 / 111 |  |
| `base\quest\minor_quests\mq032\scenes\mq032_03_epilogue.scene` | content candidate | 0 / 43 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq032_sacrum`
- `quests/minor_quest/mq032_sacrum`
- `quests/minor_quest/mq032_sacrum/description`
- `quests/minor_quest/mq032_sacrum/description_johnny`
- `quests/minor_quest/mq032_sacrum/mq032_alternative_title`
- `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook`
- `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook/description`
- `quests/minor_quest/mq032_sacrum/mq032_sacrum/01_hook/description_johnny`
- `quests/minor_quest/mq032_sacrum/mq032_sacrum/02_maelstrom`
- `quests/minor_quest/mq032_sacrum/mq032_sacrum/03_monk`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 11 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 36 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 9 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 28 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 3 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 2 |
| `questInputNodeDefinition` | 26 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questSetInteractionState_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 20 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 11 |
| `questMiscAICommandNode` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 24 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 9 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 16 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 31 |
| `questPhaseNodeDefinition` | 18 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 1 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 5 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceInterruptConditionParams,scnCheckSpeakersDistanceReturnCondition,scnCheckSpeakersDistanceReturnConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 5 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 3 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 14 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 6 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 11 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 14 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnAndNode[scnNodeId]` | 2 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnCutControlNode[scnNodeId]` | 3 |
| `scnEndNode[scnNodeId]` | 16 |
| `scnHubNode[scnNodeId]` | 4 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 76 |
| `scnStartNode[scnNodeId]` | 18 |
| `scnXorNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `016828d499c85128303c` | 5 | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene` / scene / 35 -> 105 -> 106 |
| `8cd3b647ae3f592ad947` | 5 | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene` / scene / 12 -> 13 -> 15 |
| `44fb8ec1826768134e0d` | 4 | `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` / h0 / 32 -> 27 -> 26 |
| `0fdad4c8a8b4964c866f` | 3 | `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` / scene / 65 -> 312 -> 197 |
| `19665e3783f6f51a7337` | 3 | `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` / scene / 1 -> 188 -> 323 |
| `1ce266aebad76b994b0f` | 3 | `base\quest\bugfixing\minor_quests\mq032\mq032_encounter_bugfixes.questphase` / h7 / 9 -> 11 -> 13 |
| `1f24964b77d0d7cf82e2` | 3 | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene` / scene / 51 -> 235 -> 236 |
| `29c7ac4763cf8bc766bd` | 3 | `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` / h0 / 29 -> 27 -> 26 |
| `2fd99f4299806c136bfa` | 3 | `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` / scene / 1 -> 188 -> 4 |
| `400ab17c1f3363cf36e2` | 3 | `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` / h0 / 27 -> 26 -> 28 |
| `44903fec4308710947a9` | 3 | `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` / h0 / 4 -> 24 -> 10 |
| `4c5502cfb80360952883` | 3 | `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` / h0 / 28 -> 31 -> 25 |
| `4fa2901d5baeedde07ac` | 3 | `base\quest\minor_quests\mq032\scenes\mq032_01_hook.scene` / scene / 129 -> 71 -> 4 |
| `570676cffa83a3c52c8e` | 3 | `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 0 -> 3 -> 2 |
| `58c57e3374b8f51c8efb` | 3 | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene` / scene / 105 -> 106 -> 86 |
| `68708e584f27e857dcd1` | 3 | `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` / h0 / 32 -> 28 -> 31 |
| `78ea5703415f3611703c` | 3 | `base\quest\minor_quests\mq032\scenes\mq032_02_maelstrom.scene` / scene / 26 -> 20 -> 37 |
| `7b5b2d18eb5b831df3c4` | 3 | `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` / h0 / 32 -> 31 -> 25 |
| `8c7beb1704f04b204046` | 3 | `base\quest\minor_quests\mq032\phases\mq032_01_hook.questphase` / h0 / 25 -> 29 -> 27 |
| `956a18e11770fe167253` | 3 | `base\quest\minor_quests\mq032\phases\mq032_02_maelstrom.questphase` / h0 / 59 -> 104 -> 121 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
