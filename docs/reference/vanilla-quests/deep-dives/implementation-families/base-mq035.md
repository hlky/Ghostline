# base-mq035

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq035\mq035_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq035\mq035_encounter_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq035\mq035_quest_bugfixes.questphase` | repair | 13 / 0 |  |
| `base\quest\minor_quests\mq035\communities\mq035_tyger_claws.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq035\mq035_ozob.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq035\mq035_ozob.quest` | content candidate | 1 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq035\mq035_ozob.questphase; base\quest\minor_quests\mq035\scenes\mq035_chicken_test.scene |
| `base\quest\minor_quests\mq035\mq035_ozob.questphase` | content candidate | 5 / 0 | base\quest\minor_quests\mq035\phases\mq035_01_car_theft.questphase; base\quest\minor_quests\mq035\phases\mq035_02_car_ride.questphase; base\quest\minor_quests\mq035\phases\mq035_03_robbery.questphase; base\quest\minor_quests\mq035\phases\mq035_04_ambush.questphase |
| `base\quest\minor_quests\mq035\phases\mq035_01_car_theft.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq035\scenes\mq035_hook_call.scene |
| `base\quest\minor_quests\mq035\phases\mq035_02_car_ride.questphase` | content candidate | 7 / 0 | base\quest\minor_quests\mq035\scenes\mq035_ozob_dialogues.scene |
| `base\quest\minor_quests\mq035\phases\mq035_03_robbery.questphase` | content candidate | 5 / 0 | base\quest\minor_quests\mq035\scenes\mq035_ozob_dialogues.scene |
| `base\quest\minor_quests\mq035\phases\mq035_04_ambush.questphase` | content candidate | 6 / 0 | base\quest\minor_quests\mq035\phases\mq035_04b_ambush_combat.questphase; base\quest\minor_quests\mq035\scenes\mq035_ozob_dialogues.scene |
| `base\quest\minor_quests\mq035\phases\mq035_04b_ambush_combat.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq035\scenes\mq035_chicken_test.scene` | test/debug | 0 / 5 |  |
| `base\quest\minor_quests\mq035\scenes\mq035_hook_call.scene` | content candidate | 0 / 29 |  |
| `base\quest\minor_quests\mq035\scenes\mq035_ozob_dialogues.scene` | content candidate | 0 / 93 |  |

## Journal paths observed in these resources

- `contacts/ozob`
- `contacts/ozob/mq035/hook_message`
- `contacts/ozob/mq035/quest_failed`
- `contacts/player`
- `quests/minor_quest/mq035_ozob`
- `quests/minor_quest/mq035_ozob/mq035_ozob/00_call_ozob`
- `quests/minor_quest/mq035_ozob/mq035_ozob/00_call_ozob/contact`
- `quests/minor_quest/mq035_ozob/mq035_ozob/00_call_ozob/description`
- `quests/minor_quest/mq035_ozob/mq035_ozob/02_meet_ozob`
- `quests/minor_quest/mq035_ozob/mq035_ozob/03_drive_to_casino`
- `quests/minor_quest/mq035_ozob/mq035_ozob/04_wait`
- `quests/minor_quest/mq035_ozob/mq035_ozob/05_drive_to_ambush`
- `quests/minor_quest/mq035_ozob/mq035_ozob/06_kill_enemies`
- `quests/minor_quest/mq035_ozob/mq035_ozob/06_kill_enemies/area_mp`
- `quests/minor_quest/mq035_ozob/mq035_ozob/07_talk_ozob`
- `quests/minor_quest/mq035_ozob/mq035_ozob/honk`
- `quests/minor_quest/mq035_ozob/mq035_ozob/return_to_car`
- `quests/minor_quest/mq035_ozob/mq035_ozob/wait_for_ozob_to_get_in_car`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 18 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_NodeType,questCharacterManagerParameters_SetCombatSpace]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 5 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 15 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 17 |
| `questCombatNodeDefinition` | 10 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_PrimaryWeapon]` | 5 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 4 |
| `questConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questTriggerCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMountedTogether_ConditionType,questMountedObjectInfo]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 1 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 15 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 17 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 2 |
| `questConditionNodeDefinition[questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition,questTriggerCondition]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 5 |
| `questCutControlNodeDefinition` | 16 |
| `questDeletionMarkerNodeDefinition` | 27 |
| `questEndNodeDefinition` | 1 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 3 |
| `questEventManagerNodeDefinition` | 14 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 34 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 16 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 2 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 32 |
| `questInputNodeDefinition` | 52 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 21 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 69 |
| `questLogicalAndNodeDefinition` | 19 |
| `questLogicalHubNodeDefinition` | 33 |
| `questLogicalXorNodeDefinition` | 7 |
| `questMappinManagerNodeDefinition` | 2 |
| `questMiscAICommandNode` | 7 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 10 |
| `questMovePuppetNodeDefinition` | 3 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 5 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 3 |
| `questOutputNodeDefinition` | 50 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questGameTimeDelay_ConditionType,questLogicalCondition,questMenuState_ConditionType,questObjectDistance,questSystemCondition,questTimeCondition,questUICondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 10 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 22 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questCharacterMountedTogether_ConditionType,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questFactsDBCondition,questLogicalCondition,questMountedObjectInfo,questTriggerCondition,questVarComparison_ConditionType,questVehicleCondition,questVehicleSpeed_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 22 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMountedTogether_ConditionType,questMountedObjectInfo]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 15 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition,questTriggerCondition,questVehicleCondition,questVehicleSpeed_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questLogicalCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 29 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questMenuState_ConditionType,questTimeCondition,questUICondition]` | 1 |
| `questPauseConditionNodeDefinition[questInputAction_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questPhone_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 56 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 39 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 4 |
| `questRandomizerNodeDefinition` | 5 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questPlayerLookAt_NodeType]` | 2 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceInterruptConditionParams,scnCheckSpeakersDistanceReturnCondition,scnCheckSpeakersDistanceReturnConditionParams,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnCheckSpeakersDistanceInterruptCondition,scnCheckSpeakersDistanceReturnCondition,scnInterruptionScenarioId,scnOverrideInterruptConditions_InterruptionScenarioOperation,scnOverrideInterruptionScenario_InterruptionOperation,scnOverrideReturnConditions_InterruptionScenarioOperation,scnOverrideTalkOnReturn_InterruptionScenarioOperation,scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 5 |
| `questSceneNodeDefinition[scnWorldMarker]` | 39 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 25 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 19 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 10 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 7 |
| `questUIManagerNodeDefinition[questShowCustomTooltip_NodeType]` | 3 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 10 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 2 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 21 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 8 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 3 |
| `questVehicleNodeDefinition[questRequestVehicleCameraPerspective_NodeType]` | 6 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 2 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 17 |
| `questWorldDataManagerNodeDefinition[questPrefetchStreaming_NodeTypeV2]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 6 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 2 |
| `scnEndNode[scnNodeId]` | 28 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnRandomizerNode[scnNodeId]` | 4 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 39 |
| `scnStartNode[scnNodeId]` | 25 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `8cd3b647ae3f592ad947` | 15 | `base\quest\minor_quests\mq035\scenes\mq035_ozob_dialogues.scene` / scene / 295 -> 115 -> 109 |
| `4ff3abfc2e95448213b9` | 14 | `base\quest\minor_quests\mq035\mq035_ozob.questphase` / h88 / 18 -> 12 -> 13 |
| `8477266677db88dc3069` | 13 | `base\quest\minor_quests\mq035\mq035_ozob.questphase` / h252 / 10 -> 9 -> 12 |
| `eaf5aab427d50e5598b6` | 8 | `base\quest\bugfixing\minor_quests\mq035\mq035_quest_bugfixes.questphase` / h37 / 0 -> 8 -> 2 |
| `02e007a79567f37a7cf3` | 6 | `base\quest\minor_quests\mq035\phases\mq035_04_ambush.questphase` / h748 / 129 -> 130 -> 136 |
| `2c6125d1b1f39755858f` | 6 | `base\quest\minor_quests\mq035\mq035_ozob.questphase` / h252 / 23 -> 19 -> 5 |
| `480a010388ce3a487ffb` | 6 | `base\quest\minor_quests\mq035\phases\mq035_04_ambush.questphase` / h748 / 109 -> 112 -> 75 |
| `4f31d194513a14436360` | 6 | `base\quest\minor_quests\mq035\mq035_ozob.questphase` / h252 / 24 -> 20 -> 2 |
| `7c68bbef82b94a8ad646` | 6 | `base\quest\minor_quests\mq035\phases\mq035_04_ambush.questphase` / h748 / 136 -> 138 -> 1 |
| `a36102ceee6fef729c5f` | 6 | `base\quest\minor_quests\mq035\phases\mq035_04_ambush.questphase` / h748 / 110 -> 112 -> 75 |
| `ae171cffa3dca3159b16` | 6 | `base\quest\minor_quests\mq035\mq035_ozob.questphase` / h671 / 69 -> 62 -> 3 |
| `d8ef39870626a261efb0` | 6 | `base\quest\minor_quests\mq035\phases\mq035_04_ambush.questphase` / h748 / 111 -> 112 -> 75 |
| `2036e2b787ed46b7bfa9` | 5 | `base\quest\minor_quests\mq035\phases\mq035_03_robbery.questphase` / h541 / 103 -> 104 -> 105 |
| `2381992dd64b4bc7968e` | 5 | `base\quest\minor_quests\mq035\phases\mq035_03_robbery.questphase` / h541 / 101 -> 104 -> 105 |
| `28ead5d60e7f9ba5a77e` | 5 | `base\quest\minor_quests\mq035\phases\mq035_03_robbery.questphase` / h541 / 98 -> 101 -> 104 |
| `2efe57311c3afed6b691` | 5 | `base\quest\minor_quests\mq035\phases\mq035_03_robbery.questphase` / h541 / 95 -> 97 -> 99 |
| `31d3bed5ab92ff978d55` | 5 | `base\quest\minor_quests\mq035\phases\mq035_03_robbery.questphase` / h541 / 98 -> 103 -> 104 |
| `6e46493dae3944d7fbf5` | 5 | `base\quest\minor_quests\mq035\phases\mq035_03_robbery.questphase` / h541 / 99 -> 98 -> 102 |
| `7b3dea352ca4005ca166` | 5 | `base\quest\minor_quests\mq035\phases\mq035_03_robbery.questphase` / h541 / 96 -> 95 -> 97 |
| `93383c84868241f1284e` | 5 | `base\quest\minor_quests\mq035\phases\mq035_03_robbery.questphase` / h541 / 106 -> 97 -> 99 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
