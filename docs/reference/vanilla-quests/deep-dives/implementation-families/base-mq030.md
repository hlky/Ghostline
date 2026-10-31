# base-mq030

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq030\mq030_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq030\mq030_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq030\mq030_quest_bugfixes.questphase` | repair | 3 / 0 |  |
| `base\quest\minor_quests\mq030\communities\mq030_cyberpsycho.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq030\communities\mq030_jinguji_bodyguard.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq030\communities\mq030_max_tac.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq030\communities\mq030_melisa.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq030\communities\mq030_street_crowd.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq030\mq030.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq030\mq030.quest` | content candidate | 2 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq030\mq030.questphase; base\quest\minor_quests\mq030\test\mq030_chicken_test.questphase |
| `base\quest\minor_quests\mq030\mq030.questphase` | content candidate | 4 / 0 | base\quest\minor_quests\mq030\phases\mq030_melisa.questphase; base\quest\minor_quests\mq030\scenes\mq030_02_jinguji_community.scene |
| `base\quest\minor_quests\mq030\phases\mq030_melisa.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene |
| `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` | content candidate | 0 / 623 |  |
| `base\quest\minor_quests\mq030\scenes\mq030_02_jinguji_community.scene` | content candidate | 0 / 6 |  |
| `base\quest\minor_quests\mq030\test\mq030_chicken_test.questphase` | test/debug | 1 / 0 | base\quest\minor_quests\mq030\test\mq030_chicken_test.scene |
| `base\quest\minor_quests\mq030\test\mq030_chicken_test.scene` | test/debug | 0 / 14 |  |

## Journal paths observed in these resources

- `contacts/zane/mq030_follow_up/mq030_01_msg_thanks`
- `contacts/zane/mq030_follow_up/mq030_02_msg_gossip`
- `contacts/zane/mq030_follow_up/mq030_03_ch_gossip`
- `contacts/zane/mq030_follow_up/mq030_03_ch_gossip/mq030_03a_always`
- `contacts/zane/mq030_follow_up/mq030_03_ch_gossip/mq030_03b_nah`
- `contacts/zane/mq030_follow_up/mq030_03b_answer`
- `contacts/zane/mq030_follow_up/mq030_03b_ch_reconsider`
- `contacts/zane/mq030_follow_up/mq030_03b_ch_reconsider/mq030_04b_cynic`
- `contacts/zane/mq030_follow_up/mq030_03b_ch_reconsider/mq030_04b_fine`
- `contacts/zane/mq030_follow_up/mq030_04b_cynic_answer`
- `contacts/zane/mq030_follow_up/mq030_05b_come_again`
- `contacts/zane/mq030_follow_up/mq030_06_news_54`
- `contacts/zane/mq030_follow_up/mq030_07_melisa`
- `contacts/zane/mq030_follow_up/mq030_08_ch_melisa`
- `contacts/zane/mq030_follow_up/mq030_08_ch_melisa/mq030_08a_rage`
- `contacts/zane/mq030_follow_up/mq030_08_ch_melisa/mq030_08b_killing`
- `contacts/zane/mq030_follow_up/mq030_09_see_you`
- `points_of_interest/minor_quests/mq030_melisa`
- `quests/minor_quest/mq030_melisa`
- `quests/minor_quest/mq030_melisa/01_melisa/01_defeat_psycho`
- `quests/minor_quest/mq030_melisa/01_melisa/01_defeat_psycho/description`
- `quests/minor_quest/mq030_melisa/01_melisa/02_approach_max_tac`
- `quests/minor_quest/mq030_melisa/01_melisa/03_sit_down`
- `quests/minor_quest/mq030_melisa/01_melisa/04_talk_to_melisa`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 2 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 7 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 22 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 10 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 13 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 22 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 21 |
| `questCombatNodeDefinition[questCombatNodeParams_PrimaryWeapon]` | 5 |
| `questCombatNodeDefinition[questCombatNodeParams_RestrictMovementToArea]` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 7 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 3 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 8 |
| `questEventManagerNodeDefinition` | 7 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 27 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 4 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 4 |
| `questInputNodeDefinition` | 16 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 11 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 14 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 10 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 5 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 15 |
| `questOutputNodeDefinition` | 14 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterQuickHackUploadBegin_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 27 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 14 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 27 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 19 |
| `questPauseConditionNodeDefinition[questUICondition,questUIElement_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 11 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 6 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 3 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 21 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 11 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 3 |
| `questUIManagerNodeDefinition[questSwitchNameplate_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questVendorPanel_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 35 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 1 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 37 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 20 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 4 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 7 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 10 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 7 |
| `scnAndNode[scnNodeId]` | 19 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeNsTimedParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnCutControlNode[scnNodeId]` | 15 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 5 |
| `scnHubNode[scnNodeId]` | 23 |
| `scnRandomizerNode[scnNodeId]` | 5 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 73 |
| `scnStartNode[scnNodeId]` | 8 |
| `scnXorNode[scnNodeId]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `00895e53badea42e971a` | 22 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 2665 -> 2497 -> 2499 |
| `e7f36a4c3c828f7be85d` | 22 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 2497 -> 2499 -> 3595 |
| `bf93571076914e7a0919` | 16 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 3294 -> 3296 -> 3298 |
| `f0842e4443f5d945587c` | 10 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 2519 -> 2520 -> 2521 |
| `5bad1fe50183293cd1dd` | 9 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 3868 -> 3854 -> 430 |
| `8081b3a10a0beaa086db` | 9 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 3868 -> 3854 -> 430 |
| `189b5e1f0d63ac361dd4` | 8 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 3389 -> 3390 -> 3392 |
| `0384fac21bd89c44f01a` | 6 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 337 -> 340 -> 331 |
| `1b0fdb9a2829108b2482` | 6 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 2809 -> 1440 -> 1442 |
| `3533f40fa23aec648c6b` | 6 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 335 -> 337 -> 340 |
| `694dcc3f01ba46e3e166` | 6 | `base\quest\minor_quests\mq030\mq030.questphase` / h333 / 12 -> 24 -> 26 |
| `a65e40b29d01bc6e4a79` | 6 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 745 -> 1115 -> 1585 |
| `c6360c30becfcd41253a` | 6 | `base\quest\minor_quests\mq030\mq030.questphase` / h333 / 7 -> 12 -> 5 |
| `fbc24cda56fbbb771eab` | 6 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 335 -> 337 -> 340 |
| `0b5a990cfc351a3492ba` | 5 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 2466 -> 2577 -> 233 |
| `0d99ca561498c181e0f0` | 5 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 2466 -> 2577 -> 2298 |
| `11a1b52c9dc108c0de7c` | 5 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 2577 -> 2298 -> 2362 |
| `167dc27908b2f70864b1` | 5 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 233 -> 2362 -> 2333 |
| `35f6c85aff661220bb5c` | 5 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 2467 -> 2577 -> 2298 |
| `3c868842ca6cce55809b` | 5 | `base\quest\minor_quests\mq030\scenes\mq030_01_melisa.scene` / scene / 210 -> 3030 -> 2353 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
