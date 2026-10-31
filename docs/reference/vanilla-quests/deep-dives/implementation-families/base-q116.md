# base-q116

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\part1\q116\q116_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\part1\q116\q116_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\part1\q116\q116_quest_bugfixes.questphase` | repair | 5 / 0 |  |
| `base\quest\main_quests\part1\q116\communities\q116_com_cyberspace_player.community` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase` | content candidate | 11 / 0 | base\quest\main_quests\part1\q113\scenes\q113_13_adam_smasher.scene; base\quest\main_quests\part1\q116\scenes\q116_01_adam_smasher.scene; base\quest\main_quests\part1\q116\scenes\q116_03b_after_bossfight.scene |
| `base\quest\main_quests\part1\q116\phases\q116_cyberspace.questphase` | content candidate | 4 / 0 | base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene; base\quest\main_quests\part1\q116\scenes\q116_05a_ripperdoc_roof.scene |
| `base\quest\main_quests\part1\q116\phases\q116_mikoshi.questphase` | content candidate | 1 / 0 |  |
| `base\quest\main_quests\part1\q116\phases\q116_smasher.questphase` | content candidate | 8 / 0 | base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase; base\quest\main_quests\part1\q116\scenes\q116_01_adam_smasher.scene; base\quest\main_quests\part1\q116\scenes\q116_03b_after_bossfight.scene; base\quest\main_quests\part1\q116\scenes\q116_04_mikoshi_intro.scene |
| `base\quest\main_quests\part1\q116\q116_mikoshi.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\main_quests\part1\q116\q116_mikoshi.quest` | content candidate | 1 / 0 | base\quest\main_quests\part1\q116\q116_mikoshi.questphase; base\quest\main_quests\part1\q116\test\q116_00_chicken_test.scene |
| `base\quest\main_quests\part1\q116\q116_mikoshi.questphase` | content candidate | 8 / 0 | base\quest\main_quests\part1\q116\phases\q116_cyberspace.questphase; base\quest\main_quests\part1\q116\phases\q116_smasher.questphase |
| `base\quest\main_quests\part1\q116\scenes\q116_01_adam_smasher.scene` | content candidate | 0 / 170 |  |
| `base\quest\main_quests\part1\q116\scenes\q116_03b_after_bossfight.scene` | content candidate | 0 / 128 |  |
| `base\quest\main_quests\part1\q116\scenes\q116_04_mikoshi_intro.scene` | content candidate | 0 / 234 |  |
| `base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene` | content candidate | 0 / 1293 |  |
| `base\quest\main_quests\part1\q116\scenes\q116_05a_ripperdoc_roof.scene` | content candidate | 0 / 191 |  |
| `base\quest\main_quests\part1\q116\test\q116_00_chicken_test.scene` | test/debug | 0 / 49 |  |
| `base\quest\main_quests\part1\q116\test\q116_mikoshi_bossfight.gamedef` | test/debug | 0 / 0 |  |
| `base\quest\main_quests\part1\q116\test\q116_mikoshi_bossfight.quest` | test/debug | 2 / 0 | base\quest\main_quests\part1\q116\q116_mikoshi.questphase |
| `base\quest\main_quests\part1\q116\test\q116_smasher_guards_wave_01.community` | test/debug | 0 / 0 |  |
| `base\quest\main_quests\part1\q116\test\q116_smasher_guards_wave_02.community` | test/debug | 0 / 0 |  |

## Journal paths observed in these resources

- `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower`
- `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/00_access_mikoshi`
- `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/00b_wait_for_alt`
- `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/01_defeat_adam`
- `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/02_decide_adam`
- `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/03_go_to_access`
- `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/04_talk_to_alt`
- `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/04b_talk_to_panam`
- `quests/main_quest/act_01/q114_03_attack_on_arasaka_tower/09_mikoshi/05_jack_in`
- `quests/main_quest/act_01/q115_rogues_last_flight`
- `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/00_access_mikoshi`
- `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/00b_wait_for_alt`
- `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/01_defeat_adam`
- `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/02_decide_adam`
- `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/02b_rogue_gun`
- `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/03_go_to_access`
- `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/04_talk_to_alt`
- `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/04b_talk_to_weyland`
- `quests/main_quest/act_01/q115_rogues_last_flight/07_mikoshi/05_jack_in`
- `quests/main_quest/act_01/q116_cyberspace`
- `quests/main_quest/act_01/q116_cyberspace/00_roof/01_go_to_roof`
- `quests/main_quest/act_01/q116_cyberspace/00_roof/01_go_to_roof/roof`
- `quests/main_quest/act_01/q116_cyberspace/00_roof/02a_talk_jackie`
- `quests/main_quest/act_01/q116_cyberspace/00_roof/02b_pick_necklace`
- `quests/main_quest/act_01/q116_cyberspace/01_cyberspace/01_explore`
- `quests/main_quest/act_01/q116_cyberspace/01_cyberspace/02a_talk_v`
- `quests/main_quest/act_01/q116_cyberspace/01_cyberspace/02b_talk_johnny`
- `quests/main_quest/act_01/q116_cyberspace/01_cyberspace/02c_talk_johnny_alt`
- `quests/main_quest/act_01/q116_cyberspace/01_cyberspace/02d_talk_v_alt`
- `quests/main_quest/act_01/q116_cyberspace/01_cyberspace/03a_enter_well`
- `quests/main_quest/act_01/q116_cyberspace/01_cyberspace/03a_enter_well_optional`
- `quests/main_quest/act_01/q116_cyberspace/01_cyberspace/03b_cross_bridge`
- `quests/main_quest/act_01/q116_cyberspace/01_cyberspace/03b_cross_bridge_optional`
- `quests/main_quest/act_01/q116_cyberspace/01_cyberspace/03c_touch_alt`
- `quests/main_quest/act_01/q116_cyberspace/01_cyberspace/03c_touch_alt_optional`
- `quests/meta/09_solo`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 55 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 20 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_NodeType,questCharacterManagerParameters_SetCombatSpace]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 7 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 62 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 5 |
| `questCheckpointNodeDefinition` | 7 |
| `questCombatNodeDefinition` | 42 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 46 |
| `questCombatNodeDefinition[questCombatNodeParams_PrimaryWeapon]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_SecondaryWeapon]` | 1 |
| `questConditionNodeDefinition[questBuild_ConditionType,questStatsCondition,questUniversalRef]` | 1 |
| `questConditionNodeDefinition[questCharacterBodyType_CondtionType,questCharacterCondition]` | 6 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 24 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 136 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_ControlCrowd]` | 5 |
| `questCutControlNodeDefinition` | 28 |
| `questDeletionMarkerNodeDefinition` | 62 |
| `questEndNodeDefinition` | 2 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 82 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_NodeType,questPlayEnv_NodeTypeParams]` | 5 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 4 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 23 |
| `questEventManagerNodeDefinition` | 5 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 14 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 132 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 14 |
| `questGameManagerNodeDefinition[questReplacer_NodeType]` | 5 |
| `questInputNodeDefinition` | 48 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 35 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 168 |
| `questInteractiveObjectManagerNodeDefinition[questSetInteractionVisualizerOverride]` | 1 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 6 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 32 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questTransferItem_NodeType,questTransferItems_NodeTypeParams,questTransferItems_NodeTypeParams_OperationData,questTransferItems_NodeTypeParams_TransferAllOperationData,questUniversalRef]` | 3 |
| `questItemManagerNodeDefinition[questTransferItem_NodeType,questTransferItems_NodeTypeParams,questTransferItems_NodeTypeParams_TransferAllOperationData,questUniversalRef]` | 3 |
| `questItemManagerNodeDefinition[questUniversalRef,questUseWeapon_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 82 |
| `questJournalNodeDefinition[questJournalTrackQuest_NodeType]` | 7 |
| `questLogicalAndNodeDefinition` | 10 |
| `questLogicalHubNodeDefinition` | 8 |
| `questLogicalXorNodeDefinition` | 7 |
| `questLookAtDrivenTurnsNode` | 3 |
| `questMappinManagerNodeDefinition` | 1 |
| `questMiscAICommandNode` | 51 |
| `questMovePuppetNodeDefinition[questAnimMoveOnSplineParams,questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questObservableUniversalRef,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questMovePuppetNodeDefinition[questAnimMoveOnSplineParams,questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 50 |
| `questOutputNodeDefinition` | 36 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 40 |
| `questPauseConditionNodeDefinition[questDevice_ConditionFunctionParameter,questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 10 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 25 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 45 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 6 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 142 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSectionNode_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 98 |
| `questPhaseNodeDefinition` | 37 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 12 |
| `questRenderFxManagerNodeDefinition[questSetCyberspacePostFX_NodeType]` | 32 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 19 |
| `questRenderFxManagerNodeDefinition[questSetRenderLayer_NodeType]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 4 |
| `questSceneManagerNodeDefinition[questPlayerLookAt_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetPossesion_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier2Params_NodeType]` | 6 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 14 |
| `questSceneManagerNodeDefinition[questToggleEventExecutionTag_NodeType]` | 14 |
| `questSceneNodeDefinition[scnWorldMarker]` | 19 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 20 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 41 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 33 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 10 |
| `questStartNodeDefinition` | 2 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 12 |
| `questTimeManagerNodeDefinition[questPauseTime_NodeType]` | 6 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 6 |
| `questUIManagerNodeDefinition[questBriefingSequencePlayer_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 3 |
| `questUIManagerNodeDefinition[questSetHUDEntryForcedVisibility_NodeType]` | 12 |
| `questUIManagerNodeDefinition[questSwitchNameplate_NodeType]` | 9 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 6 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1,questUseWorkspotPlayerParams]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 51 |
| `questUseWorkspotNodeDefinition[questUseWorkspotPlayerParams,scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 35 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 186 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 6 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questPrefetchStreaming_NodeTypeV2]` | 10 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 61 |
| `scnAndNode[scnNodeId]` | 33 |
| `scnChoiceNode[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsAttachToScreenParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questTriggerCondition,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[questTriggerCondition,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 5 |
| `scnChoiceNode[questTriggerCondition,scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 5 |
| `scnChoiceNode[questTriggerCondition,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 10 |
| `scnChoiceNode[questTriggerCondition,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAdaptiveLookAtReferencePoint,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsAttachToScreenParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnReferencePointId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAdaptiveLookAtReferencePoint,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnscreenplayItemId]` | 5 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsAttachToScreenParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnReferencePointId,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 9 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 5 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsAttachToPropParams,scnChoiceNodeNsAttachToScreenParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnPropId,scnReferencePointId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 4 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 5 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 6 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 15 |
| `scnCutControlNode[scnNodeId]` | 29 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 13 |
| `scnHubNode[scnNodeId]` | 94 |
| `scnRandomizerNode[scnNodeId]` | 26 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 351 |
| `scnStartNode[scnNodeId]` | 111 |
| `scnXorNode[scnNodeId]` | 20 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `2dd87e6cc4f1584cdfa8` | 40 | `base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase` / h40 / 272 -> 201 -> 186 |
| `6c9e26f1e5a73009543d` | 40 | `base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase` / h40 / 195 -> 272 -> 201 |
| `8dd134aba6d607d4a590` | 36 | `base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase` / h40 / 288 -> 205 -> 289 |
| `956a18e11770fe167253` | 36 | `base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase` / h40 / 206 -> 288 -> 205 |
| `9380dda43f90ecd62efb` | 28 | `base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase` / h40 / 188 -> 189 -> 302 |
| `9832bcd48608fdbe530a` | 28 | `base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase` / h40 / 383 -> 319 -> 318 |
| `43d1a3cdcdcb1d73aed9` | 27 | `base\quest\main_quests\part1\q116\scenes\q116_01_adam_smasher.scene` / scene / 917 -> 912 -> 911 |
| `0e33833754998326d7cf` | 24 | `base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase` / h40 / 198 -> 195 -> 309 |
| `702ebba9defaba1d1043` | 24 | `base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase` / h40 / 198 -> 195 -> 272 |
| `da79d60b032dcba102d6` | 23 | `base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene` / scene / 5946 -> 5950 -> 5949 |
| `c700186a79289568dd51` | 21 | `base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene` / scene / 4062 -> 5946 -> 5950 |
| `53d6c56d20b9427c3dc6` | 20 | `base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase` / h1267 / 293 -> 186 -> 302 |
| `c75a352f3049b561d912` | 20 | `base\quest\main_quests\part1\q116\phases\q116_combat_smasher_bossfight.questphase` / h1267 / 293 -> 186 -> 273 |
| `78a3903e3bfae008d098` | 18 | `base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene` / scene / 3327 -> 4062 -> 4063 |
| `3228aa7a4f8cfbea26a8` | 16 | `base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene` / scene / 3327 -> 4062 -> 5946 |
| `6918eea7c6c5d02643d5` | 16 | `base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene` / scene / 2090 -> 2047 -> 5679 |
| `a964ab6f855446851d67` | 16 | `base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene` / scene / 4062 -> 4063 -> 8072 |
| `ce27958c82560b98f5c9` | 16 | `base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene` / scene / 4062 -> 4063 -> 4094 |
| `ec22e0708eb3fc5fc37f` | 16 | `base\quest\main_quests\part1\q116\scenes\q116_05_mikoshi.scene` / scene / 2958 -> 7629 -> 6397 |
| `41c1642f06c00ab60be1` | 15 | `base\quest\main_quests\part1\q116\scenes\q116_04_mikoshi_intro.scene` / scene / 571 -> 706 -> 698 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
