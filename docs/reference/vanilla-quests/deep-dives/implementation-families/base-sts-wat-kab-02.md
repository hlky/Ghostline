# base-sts-wat-kab-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\communities\sts_wat_kab_02_backup.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\communities\sts_wat_kab_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\communities\sts_wat_kab_02_com_chester.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\communities\sts_wat_kab_02_flathead.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_bugfixing.questphase` | repair | 12 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_combat.questphase` | content candidate | 5 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_chats.scene |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_openworld.questphase` | content candidate | 9 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_holocall_debriefs.scene; base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_holocall_prebrief.scene; base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_combat.questphase; base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_openworld.questphase |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_chats.scene` | content candidate | 0 / 4 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_holocall_debriefs.scene` | content candidate | 0 / 26 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene` | content candidate | 0 / 155 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\sts_wat_kab_02_def.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\sts_wat_kab_02_quest.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\sts_wat_kab_02_test_def.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/sts_wat_kab_02/sts_wat_kab_02_brief`
- `contacts/regina_jones/sts_wat_kab_02/sts_wat_kab_02_holocall_debrief_fail`
- `contacts/regina_jones/sts_wat_kab_02/sts_wat_kab_02_holocall_debrief_success`
- `contacts/regina_jones/sts_wat_kab_02/transport_request_response`
- `points_of_interest/street_stories/sts_wat_kab_02`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/blood`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/blood/blood`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/blood_inject`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/escor`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/escort_to_car`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/find`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/get_inside`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/get_inside/briefing`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/persuade`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/scan`
- `quests/street_stories/watson/kabuki/sts_wat_kab_02/sts_wat_kab_02/tlk`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 2 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 4 |
| `questCheckpointNodeDefinition` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 16 |
| `questConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition]` | 1 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 6 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questCutControlNodeDefinition` | 4 |
| `questDeletionMarkerNodeDefinition` | 28 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questEquipItemNodeDefinition[questEquipItemParams,questObservableUniversalRef]` | 1 |
| `questEventManagerNodeDefinition` | 18 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 61 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 27 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 5 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 5 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questSetLootInteractionAccess_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 29 |
| `questLogicalAndNodeDefinition` | 5 |
| `questLogicalHubNodeDefinition` | 11 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMappinManagerNodeDefinition` | 2 |
| `questMiscAICommandNode` | 4 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 21 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 11 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questFactsDBCondition,questLogicalCondition,questObjectCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 24 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 19 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 1 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questSensesCondition,questVision_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 18 |
| `questPhaseNodeDefinition` | 17 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 10 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 6 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneManagerNodeDefinition[questSetTier_NodeType]` | 4 |
| `questSceneNodeDefinition[scnWorldMarker]` | 7 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 16 |
| `questSpawnManagerNodeDefinition[questLegacy_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 19 |
| `questUseWorkspotNodeDefinition[scnSceneWorkspotInstanceId,scnUseSceneWorkspotParamsV1]` | 25 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 2 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 8 |
| `questVehicleNodeDefinition[questForbiddenTrigger_NodeType]` | 6 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 1 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 12 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 5 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnAndNode[scnNodeId]` | 1 |
| `scnChoiceNode[questTriggerCondition,scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneEventId,scnSceneTime,scnscreenplayItemId]` | 6 |
| `scnChoiceNode[scnActorId,scnChoiceNodeNsActorReminderParams,scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsAttachToActorParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnSceneTime,scnscreenplayItemId]` | 2 |
| `scnCutControlNode[scnNodeId]` | 5 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 11 |
| `scnHubNode[scnNodeId]` | 3 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnNodeId,scnToggleInterruption_InterruptionOperation]` | 1 |
| `scnRandomizerNode[scnNodeId]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 47 |
| `scnStartNode[scnNodeId]` | 10 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c1b6601d2f647c8a694d` | 9 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene` / scene / 293 -> 308 -> 319 |
| `ef1f1c4d9ff5cba71b71` | 9 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_bugfixing.questphase` / h0 / 7 -> 10 -> 8 |
| `0306ed851cf557ba7848` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_bugfixing.questphase` / h127 / 0 -> 2 -> 5 |
| `0523ee3ed1fe0207d8aa` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene` / scene / 490 -> 461 -> 624 |
| `081b9dbe9528f984ddca` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene` / scene / 494 -> 461 -> 490 |
| `27faccd7b30abbc3add2` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene` / scene / 293 -> 308 -> 317 |
| `2d298b805ff1e7433a38` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_bugfixing.questphase` / h219 / 6 -> 13 -> 12 |
| `56baebc755e8a9b366f5` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene` / scene / 597 -> 859 -> 861 |
| `658debc6d35f485a98ac` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_openworld.questphase` / h893 / 19 -> 2 -> 4 |
| `81118a766b34be07b5e7` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene` / scene / 490 -> 461 -> 494 |
| `a5f6ff0df46f7043f2b5` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_openworld.questphase` / h977 / 105 -> 106 -> 107 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_holocall_debriefs.scene` / scene / 274 -> 262 -> 250 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_holocall_debriefs.scene` / scene / 285 -> 283 -> 287 |
| `ebdaafaddefbc1080fe8` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene` / scene / 308 -> 319 -> 857 |
| `f802ad66d4ceea2d0aff` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_combat.questphase` / h7 / 0 -> 123 -> 129 |
| `fa808c5bfcbd1d7426ca` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_openworld.questphase` / h893 / 19 -> 2 -> 69 |
| `fcc6db629a4300e3949d` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene` / scene / 868 -> 867 -> 879 |
| `057faf6705431d5dcd46` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_combat.questphase` / h311 / 4 -> 6 -> 9 |
| `1fa539921730278ef7fb` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\scenes\sts_wat_kab_02_scene.scene` / scene / 308 -> 319 -> 860 |
| `2919e1a24dfab2855458` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_02\phases\sts_wat_kab_02_bugfixing.questphase` / h127 / 2 -> 5 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
