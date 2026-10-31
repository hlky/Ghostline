# base-mq011

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq011\mq011_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq011\mq011_quest_bugfixes.questphase` | repair | 6 / 0 |  |
| `base\quest\minor_quests\mq011\communities\mq011_com_contestants.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq011\mq011.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq011\mq011.quest` | content candidate | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq011\mq011.questphase; base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene |
| `base\quest\minor_quests\mq011\mq011.questphase` | content candidate | 13 / 0 | base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene |
| `base\quest\minor_quests\mq011\phases\shooting_range.questphase` | content candidate | 6 / 0 | base\quest\minor_quests\mq011\scenes\wilsons_shooting_range.scene |
| `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` | content candidate | 0 / 378 |  |
| `base\quest\minor_quests\mq011\scenes\wilsons_shooting_range.scene` | content candidate | 0 / 12 |  |

## Journal paths observed in these resources

- `contacts/wilson`
- `contacts/wilson/dlc2_gun_sale/01c_wilson_msg_shop_closed_mq011`
- `contacts/wilson/mq011_holocall_hook/00_wilson_start`
- `contacts/wilson/mq011_holocall_hook/01_v_choice`
- `contacts/wilson/mq011_holocall_hook/01_v_choice/01_ch1`
- `contacts/wilson/mq011_holocall_hook/01_v_choice/01_ch2`
- `contacts/wilson/mq011_holocall_hook/02a_wilson_response`
- `contacts/wilson/mq011_holocall_hook/02b_wilson_response`
- `quests/minor_quest/mq011_wilson`
- `quests/minor_quest/mq011_wilson/00_wilson/00_talk_wilson`
- `quests/minor_quest/mq011_wilson/00_wilson/00_talk_wilson/description`
- `quests/minor_quest/mq011_wilson/00_wilson/01_go_to_wilson`
- `quests/minor_quest/mq011_wilson/00_wilson/02_talk_to_wilson`
- `quests/minor_quest/mq011_wilson/00_wilson/03_enter_range`
- `quests/minor_quest/mq011_wilson/00_wilson/04_listen_instructions`
- `quests/minor_quest/mq011_wilson/01_competition/000_wait`
- `quests/minor_quest/mq011_wilson/01_competition/000b_wait`
- `quests/minor_quest/mq011_wilson/01_competition/00_shoot`
- `quests/minor_quest/mq011_wilson/01_competition/00b_ready`
- `quests/minor_quest/mq011_wilson/01_competition/01_go_wilson`
- `quests/minor_quest/mq011_wilson/01_competition/01b_talk_to_wilson`
- `quests/minor_quest/mq011_wilson/01_competition/02_grab_prize`
- `quests/minor_quest/mq011_wilson/description`
- `quests/side_quest/sq_q001_wilson`
- `quests/side_quest/sq_q001_wilson/wilson/meet_wilson`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 3 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetProgressionBuild]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 20 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questConditionNodeDefinition[questPlatform_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 6 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 8 |
| `questEndNodeDefinition` | 1 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 19 |
| `questEventManagerNodeDefinition` | 135 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 42 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 6 |
| `questInputNodeDefinition` | 36 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 26 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questLootTokenManager_NodeType,questLootTokenManager_NodeTypeParams]` | 1 |
| `questItemManagerNodeDefinition[questUniversalRef,questUseWeapon_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 6 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 39 |
| `questJournalNodeDefinition[questJournalQuestObjectiveCounter_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 5 |
| `questLogicalHubNodeDefinition` | 8 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 7 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 5 |
| `questOutputNodeDefinition` | 22 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterEquippedWeapon_ConditionType,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterEquippedWeapon_ConditionType,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterEquippedWeapon_ConditionType,questLogicalCondition,questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarVsVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 11 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 159 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 17 |
| `questPhaseNodeDefinition` | 25 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 8 |
| `questRandomizerNodeDefinition` | 2 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 6 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 5 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 9 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 24 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 7 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Pause]` | 12 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 48 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Reset]` | 36 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 18 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 20 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 17 |
| `scnAndNode[scnNodeId]` | 4 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 8 |
| `scnHubNode[scnNodeId]` | 8 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnRandomizerNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 56 |
| `scnStartNode[scnNodeId]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `f8912595b2e28a1b0d10` | 120 | `base\quest\minor_quests\mq011\mq011.questphase` / h442 / 90 -> 100 -> 91 |
| `afdb7d4950892e5322c8` | 118 | `base\quest\minor_quests\mq011\mq011.questphase` / h442 / 9 -> 10 -> 20 |
| `2ff5242916158ad5e7e8` | 12 | `base\quest\minor_quests\mq011\mq011.questphase` / h1650 / 62 -> 68 -> 74 |
| `e76e3d0e13a19c36585b` | 12 | `base\quest\minor_quests\mq011\mq011.questphase` / h181 / 9 -> 23 -> 17 |
| `f9f595035a979ca87344` | 12 | `base\quest\minor_quests\mq011\mq011.questphase` / h1650 / 47 -> 62 -> 68 |
| `194342d315e851da956f` | 8 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 880 -> 908 -> 873 |
| `9fb543ca59b3f8052ea2` | 8 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 544 -> 924 -> 873 |
| `a6e2c6404cba852cf864` | 8 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 544 -> 924 -> 873 |
| `0b487c56874911c2ea72` | 7 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 326 -> 332 -> 331 |
| `96b144de334c9d792f4b` | 6 | `base\quest\minor_quests\mq011\phases\shooting_range.questphase` / h1198 / 33 -> 41 -> 47 |
| `7d1ea5a44e1df9a39986` | 5 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 119 -> 118 -> 120 |
| `10289f1c50ebdefe71eb` | 4 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 616 -> 562 -> 630 |
| `12cfab2c016adbb2a2c5` | 4 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 98 -> 1178 -> 1189 |
| `17cef4c511c4a3d13db5` | 4 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 562 -> 560 -> 584 |
| `1a84ad264e2e46783cdc` | 4 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 684 -> 758 -> 736 |
| `2fe6b93e78f3a4423efb` | 4 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 924 -> 869 -> 877 |
| `3ac6d8c77268170a54e7` | 4 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 908 -> 877 -> 869 |
| `4926451570204e61a0a3` | 4 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 924 -> 873 -> 871 |
| `4fa2901d5baeedde07ac` | 4 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 544 -> 924 -> 869 |
| `5e979b3177e93431b6db` | 4 | `base\quest\minor_quests\mq011\scenes\mq011_00_gun_range.scene` / scene / 368 -> 370 -> 431 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
