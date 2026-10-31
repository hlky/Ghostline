# base-mq012

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq012\mq012_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq012\mq012_quest_bugfixes.questphase` | repair | 4 / 0 |  |
| `base\quest\minor_quests\mq012\communities\mq012_blockade_01.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq012\communities\mq012_blockade_02.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq012\communities\mq012_ripperdoc.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq012\mq012.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq012\mq012.quest` | content candidate | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\minor_quests\mq012\mq012.questphase |
| `base\quest\minor_quests\mq012\mq012.questphase` | content candidate | 13 / 0 | base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene |
| `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` | content candidate | 0 / 293 |  |

## Journal paths observed in these resources

- `contacts/stud`
- `points_of_interest/minor_quests/mq012_stud`
- `points_of_interest/service_points/wat_nid_ripperdoc_01`
- `quests/minor_quest/mq012_stud`
- `quests/minor_quest/mq012_stud/00_stud/00_find_out`
- `quests/minor_quest/mq012_stud/00_stud/00_find_out/description_new`
- `quests/minor_quest/mq012_stud/00_stud/01_talk_man`
- `quests/minor_quest/mq012_stud/00_stud/01b_help`
- `quests/minor_quest/mq012_stud/00_stud/02_get_car`
- `quests/minor_quest/mq012_stud/00_stud/02b_return_to_car`
- `quests/minor_quest/mq012_stud/00_stud/03_drive_ripperdoc`
- `quests/minor_quest/mq012_stud/00_stud/03_drive_ripperdoc/ripper_gps`
- `quests/minor_quest/mq012_stud/00_stud/04_stop_at_ripper`
- `quests/minor_quest/mq012_stud/00_stud/05_wait_for_call`
- `quests/minor_quest/mq012_stud/00_stud/06_talk_to_stud`
- `quests/minor_quest/mq012_stud/title_post_prologue`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 13 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAnimset]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 2 |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questBuild_ConditionType,questStatsCondition,questUniversalRef]` | 1 |
| `questConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 3 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 18 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questConditionNodeDefinition[questVehicleAvailable_ConditionType,questVehicleCondition]` | 2 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questConditionNodeDefinition[questVehicleCondition,questVehicleSummoned_ConditionType]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 25 |
| `questCutControlNodeDefinition` | 9 |
| `questDeletionMarkerNodeDefinition` | 10 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 48 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 6 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 2 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 6 |
| `questInputNodeDefinition` | 22 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 10 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 7 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 25 |
| `questJournalNodeDefinition[questJournalTrackQuest_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 6 |
| `questLogicalHubNodeDefinition` | 12 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMappinManagerNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition` | 2 |
| `questMovePuppetNodeDefinition[questFollowParams,questUniversalRef]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questObservableUniversalRef,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 38 |
| `questOutputNodeDefinition` | 19 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMountedTogether_ConditionType,questMountedObjectInfo]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questRealtimeDelay_ConditionType,questTimeCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questTriggerCondition,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 18 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questLogicalCondition,questTimeCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questMenuState_ConditionType,questTriggerCondition,questUICondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questRealtimeDelay_ConditionType,questTimeCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition,questVehicleCondition,questVehicleSpeed_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 32 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 20 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleWater_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 11 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 7 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 14 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUIManagerNodeDefinition[questWarningMessage_NodeType]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 19 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 6 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 8 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 25 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 2 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 8 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |
| `scnAndNode[scnNodeId]` | 3 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnCutControlNode[scnNodeId]` | 8 |
| `scnEndNode[scnNodeId]` | 10 |
| `scnHubNode[scnNodeId]` | 32 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnRandomizerNode[scnNodeId]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 42 |
| `scnStartNode[scnNodeId]` | 8 |
| `scnXorNode[scnNodeId]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `31ce8990e6f4ce9ab58d` | 8 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 567 -> 977 -> 932 |
| `420e156967114329d511` | 8 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 132 -> 142 -> 149 |
| `c11cf4b8fc2f0bbc6f96` | 7 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 503 -> 132 -> 142 |
| `391b9296d40f3d5cca3b` | 5 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 172 -> 1669 -> 169 |
| `627eb1907483b119902c` | 5 | `base\quest\minor_quests\mq012\mq012.questphase` / h277 / 61 -> 92 -> 135 |
| `66cb9c4db252e8211d55` | 5 | `base\quest\minor_quests\mq012\mq012.questphase` / h277 / 92 -> 134 -> 136 |
| `a36102ceee6fef729c5f` | 5 | `base\quest\minor_quests\mq012\mq012.questphase` / h277 / 135 -> 136 -> 106 |
| `b50d2df4ab802800c61e` | 5 | `base\quest\minor_quests\mq012\mq012.questphase` / h277 / 134 -> 136 -> 106 |
| `c25631343077baa2819b` | 5 | `base\quest\minor_quests\mq012\mq012.questphase` / h277 / 92 -> 135 -> 136 |
| `f3c8027d977400d19229` | 5 | `base\quest\minor_quests\mq012\mq012.questphase` / h12 / 229 -> 196 -> 197 |
| `3d9b7b29af3679d956a5` | 4 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 398 -> 1140 -> 402 |
| `c2c0aa9278403cc42317` | 4 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 714 -> 487 -> 49 |
| `d04bf3e5e6f3d43e0b07` | 4 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 714 -> 487 -> 49 |
| `fbc24cda56fbbb771eab` | 4 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 977 -> 949 -> 946 |
| `0c91ce99c5758ad6ac7d` | 3 | `base\quest\minor_quests\mq012\mq012.questphase` / h277 / 121 -> 102 -> 99 |
| `101b60945ddf6f25f378` | 3 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 309 -> 1794 -> 1796 |
| `194fb955953a6fbf83e7` | 3 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 149 -> 137 -> 134 |
| `2c4762a122ece48d0e88` | 3 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 149 -> 137 -> 132 |
| `4c19c27e3107f9ae4b13` | 3 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 487 -> 346 -> 398 |
| `5309d8c9bf44c0b3195c` | 3 | `base\quest\minor_quests\mq012\scenes\mq012_00_stud.scene` / scene / 362 -> 1075 -> 1042 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
