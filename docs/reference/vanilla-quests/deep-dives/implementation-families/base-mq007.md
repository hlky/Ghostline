# base-mq007

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq007\mq007_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq007\mq007_quest_bugfixes.questphase` | repair | 4 / 0 |  |
| `base\quest\minor_quests\mq007\mq007.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq007\mq007.quest` | content candidate | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq007\mq007.questphase; base\quest\minor_quests\mq007\test\mq007_chicken_test.scene |
| `base\quest\minor_quests\mq007\mq007.questphase` | content candidate | 16 / 0 | base\quest\minor_quests\mq007\phases\mq007_expression_facts_reset.questphase; base\quest\minor_quests\mq007\phases\mq007_gameplay_comments.questphase; base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene; base\quest\minor_quests\mq007\scenes\mq007_03_skippy_about_killing.scene; base\quest\minor_quests\mq007\scenes\mq007_04_skippy_return.scene |
| `base\quest\minor_quests\mq007\phases\mq007_expression_facts_reset.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq007\phases\mq007_gameplay_comments.questphase` | content candidate | 5 / 0 | base\quest\minor_quests\mq007\scenes\mq007_02_skippy_reactions.scene; base\quest\minor_quests\mq007\scenes\mq007_04_skippy_return.scene |
| `base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene` | content candidate | 0 / 73 |  |
| `base\quest\minor_quests\mq007\scenes\mq007_02_skippy_reactions.scene` | content candidate | 0 / 111 |  |
| `base\quest\minor_quests\mq007\scenes\mq007_03_skippy_about_killing.scene` | content candidate | 0 / 87 |  |
| `base\quest\minor_quests\mq007\scenes\mq007_04_skippy_return.scene` | content candidate | 0 / 135 |  |
| `base\quest\minor_quests\mq007\test\mq007_chicken_test.scene` | test/debug | 0 / 5 |  |
| `base\quest\minor_quests\mq007\test\mq007_delivery_test.gamedef` | test/debug | 0 / 0 |  |
| `base\quest\minor_quests\mq007\test\mq007_delivery_test.quest` | test/debug | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq007\mq007.questphase |

## Journal paths observed in these resources

- `contacts/regina_jones/mq007_giving_back_skippy/01_about_what_happened`
- `contacts/regina_jones/mq007_giving_back_skippy/02_techie_took_skippy`
- `contacts/regina_jones/mq007_giving_back_skippy/03_want_him_back`
- `points_of_interest/minor_quests/mq007_smartgun`
- `quests/main_quest/act_01/q105_dollhouse/05_leave_dollhouse/take_weapons`
- `quests/minor_quest/mq007_smartgun`
- `quests/minor_quest/mq007_smartgun/mq007_smartgun/01_deliver_skippy`
- `quests/minor_quest/mq007_smartgun/mq007_smartgun/01_deliver_skippy/description`
- `quests/minor_quest/mq007_smartgun/mq007_smartgun/01_deliver_skippy/mq007_mp_mq036_locker`
- `quests/minor_quest/mq007_smartgun/mq007_smartgun/01_deliver_skippy/mq007_mp_q105_locker`
- `quests/minor_quest/mq007_smartgun/mq007_smartgun/01_deliver_skippy/mq007_mp_regina_jones_elevator_panel`
- `quests/minor_quest/mq007_smartgun/mq007_smartgun/01_deliver_skippy/mq007_mp_regina_jones_intercom`
- `quests/minor_quest/mq007_smartgun/mq007_smartgun/01_deliver_skippy/mq007_mp_regina_jones_office`
- `quests/minor_quest/mq007_smartgun/mq007_smartgun/01_deliver_skippy/mq007_mp_skippy_in_stash`
- `quests/minor_quest/mq007_smartgun/mq007_smartgun/01_deliver_skippy/reggie`
- `quests/minor_quest/mq007_smartgun/mq007_smartgun/02_put_skippy_down`
- `quests/minor_quest/mq007_smartgun/mq007_smartgun/03_talk_to_regina`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 11 |
| `questAudioNodeDefinition[questAudioParameterNodeType]` | 1 |
| `questCheckpointNodeDefinition` | 7 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterEquippedItem_ConditionType]` | 8 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 1 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 17 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarVsVarComparison_ConditionType]` | 3 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questLogicalCondition,questSceneCondition,questSectionNode_ConditionType]` | 5 |
| `questConditionNodeDefinition[questSceneCondition,questSceneTier_ConditionType]` | 5 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 16 |
| `questEndNodeDefinition` | 2 |
| `questEntityManagerNodeDefinition[questEntityManagerSetAttachment_NodeType,questEntityManagerSetAttachment_ToActor]` | 2 |
| `questEntityManagerNodeDefinition[questEntityManagerSetAttachment_NodeType,questEntityManagerSetAttachment_ToWorld]` | 2 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 52 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 6 |
| `questEventManagerNodeDefinition` | 80 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 112 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 7 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 14 |
| `questInputNodeDefinition` | 37 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 5 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 7 |
| `questItemManagerNodeDefinition[questUniversalRef,questUseWeapon_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 6 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalHubNodeDefinition` | 19 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMappinManagerNodeDefinition` | 10 |
| `questOutputNodeDefinition` | 29 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterEquippedItem_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentToken_ConditionType,questGameTimeDelay_ConditionType,questInventory_ConditionType,questLogicalCondition,questObjectCondition,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentToken_ConditionType,questInventory_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterStatusEffect_CondtionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionFunctionParameter,questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 28 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 45 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneTalking_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 9 |
| `questPhaseNodeDefinition` | 29 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 6 |
| `questRandomizerNodeDefinition` | 8 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneManagerNodeDefinition[questSetTier2Params_NodeType]` | 3 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 6 |
| `questSceneNodeDefinition[scnWorldMarker]` | 16 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 2 |
| `questStartNodeDefinition` | 2 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 5 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 6 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 7 |
| `questWorldDataManagerNodeDefinition[questPrefetchStreaming_NodeTypeV2]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 10 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questBuild_ConditionType,questStatsCondition,questUniversalRef,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questInventory_ConditionType,questObjectCondition,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToWorldParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 6 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 6 |
| `scnHubNode[scnNodeId]` | 26 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 2 |
| `scnRandomizerNode[scnNodeId]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 75 |
| `scnStartNode[scnNodeId]` | 20 |
| `scnXorNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9af8a87f20a910659fa8` | 13 | `base\quest\minor_quests\mq007\mq007.quest` / h0 / 11 -> 13 -> 4 |
| `13e1c1247187e351cf40` | 10 | `base\quest\minor_quests\mq007\scenes\mq007_02_skippy_reactions.scene` / scene / 67 -> 10 -> 276 |
| `5c18473790c8cdfc785e` | 10 | `base\quest\minor_quests\mq007\scenes\mq007_02_skippy_reactions.scene` / scene / 67 -> 10 -> 146 |
| `5f6ca3c34fa0cfaef79f` | 8 | `base\quest\minor_quests\mq007\scenes\mq007_02_skippy_reactions.scene` / scene / 32 -> 328 -> 219 |
| `83539e257f00f4c1d78c` | 8 | `base\quest\minor_quests\mq007\mq007.questphase` / h293 / 2 -> 12 -> 13 |
| `c5bfb7f330b80f0cec45` | 8 | `base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene` / scene / 26 -> 28 -> 30 |
| `c86438912eaf4306c566` | 8 | `base\quest\minor_quests\mq007\scenes\mq007_02_skippy_reactions.scene` / scene / 32 -> 328 -> 324 |
| `2a2796a758c658c60a67` | 6 | `base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene` / scene / 125 -> 397 -> 393 |
| `2ec03990284c29a11f62` | 6 | `base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene` / scene / 26 -> 28 -> 32 |
| `707ba1d69745205162be` | 6 | `base\quest\minor_quests\mq007\scenes\mq007_03_skippy_about_killing.scene` / scene / 273 -> 344 -> 111 |
| `e591071733a2c9c4f29d` | 5 | `base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene` / scene / 326 -> 324 -> 330 |
| `0940cc9b366036fd47e1` | 4 | `base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene` / scene / 125 -> 397 -> 395 |
| `250e72e71fbe0c0b2106` | 4 | `base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene` / scene / 126 -> 112 -> 186 |
| `2e3e02f88d3445afaa5f` | 4 | `base\quest\minor_quests\mq007\scenes\mq007_03_skippy_about_killing.scene` / scene / 8 -> 48 -> 100 |
| `367353959d7e0d95d90c` | 4 | `base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene` / scene / 28 -> 32 -> 110 |
| `65721fe0e34213a3a57d` | 4 | `base\quest\minor_quests\mq007\phases\mq007_gameplay_comments.questphase` / h302 / 21 -> 11 -> 29 |
| `b0d96c855f870be305d2` | 4 | `base\quest\minor_quests\mq007\mq007.questphase` / h606 / 55 -> 45 -> 44 |
| `b2ab6445a6fa504170b3` | 4 | `base\quest\minor_quests\mq007\scenes\mq007_03_skippy_about_killing.scene` / scene / 255 -> 384 -> 352 |
| `c0d99e0188d9b75228e4` | 4 | `base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene` / scene / 125 -> 397 -> 389 |
| `016828d499c85128303c` | 3 | `base\quest\minor_quests\mq007\scenes\mq007_01_gun_found.scene` / scene / 118 -> 127 -> 125 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
