# base-mq003

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq003\mq003_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq003\mq003_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq003\mq003_quest_bugfixes.questphase` | repair | 4 / 0 |  |
| `base\quest\minor_quests\mq003\communities\mq003_corpo_squad.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq003\communities\mq003_homeless.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq003\mq003_orbitals.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq003\mq003_orbitals.quest` | content candidate | 1 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq003\mq003_orbitals.questphase; base\quest\minor_quests\mq003\scenes\mq003_00_chicken_test.scene |
| `base\quest\minor_quests\mq003\mq003_orbitals.questphase` | content candidate | 4 / 0 | base\quest\minor_quests\mq003\phases\mq003_homeless.questphase; base\quest\minor_quests\mq003\phases\mq003_orbital_pod.questphase |
| `base\quest\minor_quests\mq003\phases\combat\mq003_enemy_intercept.questphase` | content candidate | 2 / 0 | base\quest\minor_quests\mq003\scenes\mq003_03_orbital_pod.scene |
| `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq003\scenes\mq003_01_homeless.scene; base\quest\minor_quests\mq003\scenes\mq003_02_corpse.scene |
| `base\quest\minor_quests\mq003\phases\mq003_homeless.questphase` | content candidate | 3 / 0 | base\quest\minor_quests\mq003\scenes\mq003_01_homeless.scene; base\quest\minor_quests\mq003\scenes\mq003_02_corpse.scene |
| `base\quest\minor_quests\mq003\phases\mq003_orbital_pod.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq003\phases\combat\mq003_enemy_intercept.questphase; base\quest\minor_quests\mq003\scenes\mq003_03_orbital_pod.scene |
| `base\quest\minor_quests\mq003\scenes\mq003_00_chicken_test.scene` | test/debug | 0 / 14 |  |
| `base\quest\minor_quests\mq003\scenes\mq003_01_homeless.scene` | content candidate | 0 / 176 |  |
| `base\quest\minor_quests\mq003\scenes\mq003_02_corpse.scene` | content candidate | 0 / 18 |  |
| `base\quest\minor_quests\mq003\scenes\mq003_03_orbital_pod.scene` | content candidate | 0 / 31 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_quests/mq003_orbitals`
- `quests/minor_quest/mq003_orbitals`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/01_homeless_question`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/01_homeless_question/description`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/01_homeless_question/homeless_mp`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/01b_buy_suitcase`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/03_suitcase_grab`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/05_find_corpse`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/05a_clues`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/05b_examine_corpse`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/05c_take_shard`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/06_suitcase_unlock`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/06a_suitcase_examine`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/07_landing_loc`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/08_eliminate_enemies`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/09_retrieve_pod`
- `quests/minor_quest/mq003_orbitals/mq003_orbitals/10_talk_johnny`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 4 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 14 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 7 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 3 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 8 |
| `questCutControlNodeDefinition` | 8 |
| `questDeletionMarkerNodeDefinition` | 12 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 3 |
| `questEventManagerNodeDefinition` | 22 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 21 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 1 |
| `questInputNodeDefinition` | 24 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 4 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 65 |
| `questJournalNodeDefinition[questJournalQuestObjectiveCounter_NodeType]` | 7 |
| `questLogicalAndNodeDefinition` | 9 |
| `questLogicalHubNodeDefinition` | 18 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMappinManagerNodeDefinition` | 1 |
| `questMinigameNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 10 |
| `questOutputNodeDefinition` | 19 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questCharacterKilled_ConditionType,questCharacterStatusEffect_CondtionType,questComparisonParam,questLogicalCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 6 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 5 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 23 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPhaseNodeDefinition` | 13 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 3 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 9 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 3 |
| `questSceneNodeDefinition[scnWorldMarker]` | 25 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 14 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 2 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 5 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 18 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 44 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 14 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 7 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |
| `scnAndNode[scnNodeId]` | 2 |
| `scnChoiceNode[questBuild_ConditionType,questFactsDBCondition,questLifePath_ConditionType,questStatsCondition,questUniversalRef,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questCharacterCombat_ConditionType,questCharacterCondition,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questPaymentBalanced_ConditionType,questPaymentCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnEndNode[scnNodeId]` | 27 |
| `scnHubNode[scnNodeId]` | 5 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 46 |
| `scnStartNode[scnNodeId]` | 22 |
| `scnXorNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `6fe0547fcc0f7a306282` | 15 | `base\quest\minor_quests\mq003\phases\combat\mq003_enemy_intercept.questphase` / h0 / 30 -> 31 -> 56 |
| `8cd3b647ae3f592ad947` | 10 | `base\quest\minor_quests\mq003\scenes\mq003_01_homeless.scene` / scene / 178 -> 160 -> 179 |
| `2bca83d1511e196ee714` | 7 | `base\quest\minor_quests\mq003\phases\combat\mq003_enemy_intercept.questphase` / h0 / 15 -> 16 -> 14 |
| `b7e863bd58c0072f3308` | 6 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 82 -> 65 -> 66 |
| `258d898cfebab46dfad3` | 4 | `base\quest\minor_quests\mq003\scenes\mq003_01_homeless.scene` / scene / 64 -> 952 -> 910 |
| `2b0401523dc635f02e2c` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 18 -> 20 -> 9 |
| `421d26430670b3176810` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 84 -> 160 -> 157 |
| `48fb4483d28351fc3b43` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 91 -> 7 -> 135 |
| `4c72b4a7256f3776df46` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 67 -> 84 -> 160 |
| `4eef689e92e02371da91` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 7 -> 8 -> 9 |
| `532bca0c304f80fc9687` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 84 -> 160 -> 158 |
| `677ddb1a44cc6446f396` | 4 | `base\quest\minor_quests\mq003\phases\combat\mq003_enemy_intercept.questphase` / h0 / 13 -> 10 -> 9 |
| `80dc5e4d799234ebd745` | 4 | `base\quest\minor_quests\mq003\phases\combat\mq003_enemy_intercept.questphase` / h0 / 21 -> 15 -> 16 |
| `861fabf5a2168cb0534f` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 66 -> 67 -> 84 |
| `8ba1b42b1d96cdcee476` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 20 -> 9 -> 15 |
| `b7cdb7153165986b827a` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 20 -> 10 -> 16 |
| `d151faf9532075d537c4` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 6 -> 7 -> 135 |
| `e6ddbca31de6e613c45a` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 8 -> 92 -> 137 |
| `f23bf56abfb7838dab4a` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 89 -> 91 -> 9 |
| `f4a6ac0fe7f415c3823d` | 4 | `base\quest\minor_quests\mq003\phases\mq003_corpse.questphase` / h0 / 84 -> 160 -> 159 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
