# base-mq001

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\mq001\mq001_cinematic_bugfixes.questphase` | repair | 2 / 0 |  |
| `base\quest\bugfixing\minor_quests\mq001\mq001_quest_bugfixes.questphase` | repair | 8 / 0 |  |
| `base\quest\minor_quests\mq001\communities\mq001_com_funeral_nomads.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq001\communities\mq001_com_scorpion_vehicle.community` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq001\mq001.gamedef` | content candidate | 0 / 0 |  |
| `base\quest\minor_quests\mq001\mq001.quest` | content candidate | 3 / 0 | base\quest\additional_game_elements.questphase; base\quest\main_quests\part1\q114\phases\debug\temp_heal_player.questphase; base\quest\minor_quests\mq001\mq001.questphase; base\quest\minor_quests\mq001\phases\mq001_persistent.questphase; base\quest\minor_quests\mq001\scenes\test\mq001_chicken_test.scene |
| `base\quest\minor_quests\mq001\mq001.questphase` | content candidate | 11 / 0 | base\quest\minor_quests\mq001\phases\mq001_camp.questphase; base\quest\minor_quests\mq001\phases\mq001_cleanup.questphase; base\quest\minor_quests\mq001\phases\mq001_cliff.questphase; base\quest\minor_quests\mq001\phases\mq001_setup.questphase |
| `base\quest\minor_quests\mq001\phases\messages\mq001_msg_mitch_bridge_waiting.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq001\phases\messages\mq001_msg_mitch_hook.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq001\phases\messages\mq001_msg_post_quest.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq001\phases\mq001_camp.questphase` | content candidate | 7 / 0 | base\quest\minor_quests\mq001\phases\messages\mq001_msg_mitch_hook.questphase; base\quest\minor_quests\mq001\scenes\mq001_01_funeral_aftermath.scene; base\quest\minor_quests\mq001\scenes\mq001_01_mood_scenes_funeral.scene |
| `base\quest\minor_quests\mq001\phases\mq001_cleanup.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq001\phases\mq001_cliff.questphase` | content candidate | 5 / 0 | base\quest\minor_quests\mq001\phases\messages\mq001_msg_mitch_bridge_waiting.questphase; base\quest\minor_quests\mq001\scenes\mq001_02_drive_to_cliff.scene; base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene |
| `base\quest\minor_quests\mq001\phases\mq001_persistent.questphase` | content candidate | 1 / 0 | base\quest\minor_quests\mq001\phases\messages\mq001_msg_post_quest.questphase |
| `base\quest\minor_quests\mq001\phases\mq001_setup.questphase` | content candidate | 1 / 0 |  |
| `base\quest\minor_quests\mq001\scenes\mq001_01_funeral_aftermath.scene` | content candidate | 0 / 118 |  |
| `base\quest\minor_quests\mq001\scenes\mq001_01_mood_scenes_funeral.scene` | content candidate | 0 / 11 |  |
| `base\quest\minor_quests\mq001\scenes\mq001_02_drive_to_cliff.scene` | content candidate | 0 / 38 |  |
| `base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene` | content candidate | 0 / 329 |  |
| `base\quest\minor_quests\mq001\scenes\test\mq001_chicken_test.scene` | test/debug | 0 / 32 |  |

## Journal paths observed in these resources

- `codex/characters/quests/mitch`
- `codex/characters/quests/mitch/mitch_desc`
- `codex/glossary/world/aldecaldos`
- `codex/glossary/world/aldecaldos/aldecaldos_desc`
- `codex/locations/quest/nomads_camps`
- `codex/locations/quest/nomads_camps/nomads_camps_desc`
- `contacts/bob`
- `contacts/carol`
- `contacts/cassidy`
- `contacts/mitch`
- `contacts/mitch/mq001_bridge_waiting/01_msg_mitch_waiting`
- `contacts/mitch/mq001_bridge_waiting/02_msg_mitch_waiting2`
- `contacts/mitch/mq001_hook/01_msg_mitch_greet`
- `contacts/mitch/mq001_hook/02_msg_mitch_funeral`
- `contacts/mitch/mq001_post_quest/01_msg_mitch_greet`
- `contacts/mitch/mq001_post_quest/02_msg_mitch_thanks`
- `contacts/panam`
- `contacts/panam/mq001_quest_blocked/mq001_quest_blocked_text`
- `contacts/player`
- `contacts/teddy`
- `points_of_interest/minor_quests/mq001_scorpion`
- `quests/minor_quest/mq001_scorpion`
- `quests/minor_quest/mq001_scorpion/mq001_scorpion`
- `quests/minor_quest/mq001_scorpion/mq001_scorpion/01_talk_to_mitch`
- `quests/minor_quest/mq001_scorpion/mq001_scorpion/01_talk_to_mitch/description`
- `quests/minor_quest/mq001_scorpion/mq001_scorpion/02_follow_mitch`
- `quests/minor_quest/mq001_scorpion/mq001_scorpion/03_board_mitch_veh`
- `quests/minor_quest/mq001_scorpion/mq001_scorpion/04_drive_mitch`
- `quests/minor_quest/mq001_scorpion/mq001_scorpion/05_open_trunk`
- `quests/minor_quest/mq001_scorpion/mq001_scorpion/06_put_gascan`
- `quests/minor_quest/mq001_scorpion/mq001_scorpion/06_take_gascan`
- `quests/minor_quest/mq001_scorpion/mq001_scorpion/06a_lightup_rag`
- `quests/minor_quest/mq001_scorpion/mq001_scorpion/06b_wait_for_car`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 2 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 13 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_NodeType,questCharacterManagerCombat_SetWeaponState]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAnimset]` | 6 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetLifePath]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 2 |
| `questCheckpointNodeDefinition` | 4 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questSceneCondition,questSceneTier_ConditionType]` | 2 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 18 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 5 |
| `questConditionNodeDefinition[questLifePath_ConditionType,questStatsCondition,questUniversalRef]` | 3 |
| `questCutControlNodeDefinition` | 8 |
| `questDeletionMarkerNodeDefinition` | 16 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerSetAttachment_NodeType,questEntityManagerSetAttachment_ToActor]` | 5 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 5 |
| `questEnvironmentManagerNodeDefinition[questPlayEnv_SetWeather]` | 2 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 2 |
| `questEventManagerNodeDefinition` | 7 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 60 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 7 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 3 |
| `questGameManagerNodeDefinition[questGameplayRestrictions_NodeType]` | 11 |
| `questInputNodeDefinition` | 46 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 4 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 11 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 48 |
| `questLogicalAndNodeDefinition` | 15 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMovePuppetNodeDefinition[questAnimMoveOnSplineParams,questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 4 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 45 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 18 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 15 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questLogicalCondition,questSceneCondition,questSceneTier_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentToken_ConditionType,questLogicalCondition,questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questFactsDBCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 15 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 20 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryVisited_ConditionType,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 47 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 13 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 3 |
| `questPhaseNodeDefinition` | 40 |
| `questPhoneManagerNodeDefinition[questAddRemoveContact_NodeType,questChangeContactList_NodeTypeParams]` | 5 |
| `questPhoneManagerNodeDefinition[questCallContact_NodeType]` | 10 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 3 |
| `questRenderFxManagerNodeDefinition[questSetFadeInOut_NodeType]` | 8 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questPlayerLookAt_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 14 |
| `questSceneNodeDefinition[scnInterruptionScenarioId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 11 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questScene_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 23 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questTimeManagerNodeDefinition[questSetTime_NodeType]` | 1 |
| `questUIManagerNodeDefinition[questSwitchNameplate_NodeType]` | 3 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 18 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 41 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 13 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 3 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 11 |
| `questVehicleNodeDefinition[questStartVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 3 |
| `questVehicleNodeDefinition[questTeleportPuppetParams,questTeleport_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 11 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 10 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questPrefetchStreaming_NodeTypeV2]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 15 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType]` | 2 |
| `scnAndNode[scnNodeId]` | 11 |
| `scnChoiceNode[questFactsDBCondition,questVarComparison_ConditionType,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[questLifePath_ConditionType,questStatsCondition,questUniversalRef,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 6 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAdaptiveLookAtReferencePoint,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnReferencePointId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAttachToGameObjectParams,scnChoiceNodeNsBasicLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 3 |
| `scnCutControlNode[scnNodeId]` | 9 |
| `scnDeletionMarkerNode[scnNodeId]` | 1 |
| `scnEndNode[scnNodeId]` | 20 |
| `scnHubNode[scnNodeId]` | 31 |
| `scnRandomizerNode[scnNodeId]` | 9 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 105 |
| `scnStartNode[scnNodeId]` | 23 |
| `scnXorNode[scnNodeId]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `fbc24cda56fbbb771eab` | 9 | `base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene` / scene / 1480 -> 1484 -> 1490 |
| `eaf5aab427d50e5598b6` | 8 | `base\quest\bugfixing\minor_quests\mq001\mq001_quest_bugfixes.questphase` / h7 / 0 -> 8 -> 9 |
| `276aca4a2dc348a877d5` | 7 | `base\quest\minor_quests\mq001\scenes\mq001_01_funeral_aftermath.scene` / scene / 177 -> 42 -> 245 |
| `c1b6601d2f647c8a694d` | 7 | `base\quest\minor_quests\mq001\scenes\mq001_01_funeral_aftermath.scene` / scene / 80 -> 78 -> 84 |
| `eb8179e91d6143a6eaaf` | 7 | `base\quest\minor_quests\mq001\scenes\mq001_01_funeral_aftermath.scene` / scene / 177 -> 42 -> 51 |
| `0384fac21bd89c44f01a` | 6 | `base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene` / scene / 1484 -> 1490 -> 1472 |
| `1806d8f35ae5ea01c1fb` | 6 | `base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene` / scene / 1619 -> 1553 -> 1557 |
| `1c0072fce06c51316ab2` | 6 | `base\quest\minor_quests\mq001\mq001.questphase` / h57 / 11 -> 5 -> 8 |
| `3533f40fa23aec648c6b` | 6 | `base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene` / scene / 1480 -> 1484 -> 1490 |
| `5bad1fe50183293cd1dd` | 6 | `base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene` / scene / 1619 -> 1553 -> 1596 |
| `f2a37207a30c59bac7f0` | 6 | `base\quest\minor_quests\mq001\mq001.questphase` / h392 / 5 -> 6 -> 7 |
| `43d1a3cdcdcb1d73aed9` | 5 | `base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene` / scene / 2044 -> 2034 -> 2032 |
| `496c523e43b8a17d7751` | 5 | `base\quest\minor_quests\mq001\scenes\mq001_02_drive_to_cliff.scene` / scene / 101 -> 103 -> 102 |
| `b03d99e7db333d8f456f` | 5 | `base\quest\minor_quests\mq001\scenes\mq001_02_drive_to_cliff.scene` / scene / 99 -> 101 -> 103 |
| `e06b04ba23f1d2a682ca` | 5 | `base\quest\minor_quests\mq001\scenes\test\mq001_chicken_test.scene` / scene / 128 -> 130 -> 121 |
| `f42ba76b1fa04f334984` | 5 | `base\quest\minor_quests\mq001\scenes\mq001_02_drive_to_cliff.scene` / scene / 103 -> 102 -> 100 |
| `19665e3783f6f51a7337` | 4 | `base\quest\minor_quests\mq001\scenes\mq001_01_funeral_aftermath.scene` / scene / 103 -> 237 -> 563 |
| `43070478f7d2220e3840` | 4 | `base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene` / scene / 1494 -> 1482 -> 1488 |
| `6161899949641b1322f8` | 4 | `base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene` / scene / 1482 -> 1488 -> 1490 |
| `715597e2ef84d7c2f287` | 4 | `base\quest\minor_quests\mq001\scenes\mq001_03_cliff.scene` / scene / 1494 -> 1482 -> 1484 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
