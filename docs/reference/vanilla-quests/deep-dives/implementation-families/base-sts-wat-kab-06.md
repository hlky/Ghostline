# base-sts-wat-kab-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\community\sts_wat_kab_06_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\community\sts_wat_kab_06_com_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\community\sts_wat_kab_06_com_shopkeeper.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_bugfixing.questphase` | repair | 8 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_gameplay.questphase` | content candidate | 5 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_scene.scene |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_openworld.questphase` | content candidate | 4 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_halocall_debrief.scene; base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_holocall_prebrief.scene |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_gameplay.questphase; base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_openworld.questphase |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_prestate_control.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_fixer_call.scene` | content candidate | 0 / 3 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_halocall_debrief.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_scene.scene` | content candidate | 0 / 9 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\sts_wat_kab_06_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\sts_wat_kab_06_quest.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_phase.questphase; base\open_world\vendors\watson\kabuki\kabuki_vendors.questphase; base\quest\holocalls\holocall_initializers.questphase |

## Journal paths observed in these resources

- `contacts/regina_jones/regina_global_msg/sts_fail_msg_001`
- `contacts/regina_jones/regina_global_msg/sts_fail_warning_001`
- `contacts/regina_jones/regina_global_msg/sts_fail_warning_002`
- `contacts/regina_jones/regina_global_msg/sts_fail_warning_003`
- `contacts/regina_jones/regina_global_msg/sts_warning_fail_002`
- `contacts/regina_jones/sts_wat_kab_06/sts_wat_kab_06_brief`
- `contacts/regina_jones/sts_wat_kab_06/sts_wat_kab_06_holocall_debrief_kill`
- `contacts/regina_jones/sts_wat_kab_06/sts_wat_kab_06_holocall_debrief_unconscious`
- `points_of_interest/service_points/wat_kab_medicstore_01`
- `points_of_interest/street_stories/sts_wat_kab_06`
- `quests/street_stories/watson/kabuki/sts_wat_kab_06`
- `quests/street_stories/watson/kabuki/sts_wat_kab_06/kab_06_breif`
- `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/call_fixer_for_car`
- `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/drop_trenton_body`
- `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/find_target`
- `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/go_to_shop`
- `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/kill_or_subdue`
- `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/kill_or_subdue/kill_or_subdue`
- `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/leave_area`
- `quests/street_stories/watson/kabuki/sts_wat_kab_06/sts_wat_kab_06/leave_area_with_body`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 3 |
| `questCombatNodeDefinition[questCombatNodeParams_RestrictMovementToArea]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 15 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 3 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 5 |
| `questCutControlNodeDefinition` | 4 |
| `questDeletionMarkerNodeDefinition` | 15 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 15 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 42 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 7 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 21 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 10 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 16 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 5 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 32 |
| `questLogicalAndNodeDefinition` | 5 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 4 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 19 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questJournalCondition,questJournalEntryState_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questGatherTriggerCondition,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 8 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 12 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 9 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleDoor_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleTrunk_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 18 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRandomizerNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 21 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 13 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 7 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 3 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 10 |
| `questVehicleNodeDefinition[questUnassignAll_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 6 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 8 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 7 |
| `scnStartNode[scnNodeId]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `eaf5aab427d50e5598b6` | 7 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_bugfixing.questphase` / h2 / 2 -> 5 -> 6 |
| `8305d8f918998bbbb2ee` | 5 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_openworld.questphase` / h1210 / 48 -> 49 -> 76 |
| `8cd3b647ae3f592ad947` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_fixer_call.scene` / scene / 4 -> 5 -> 6 |
| `ac686eb7c056939b5d16` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_openworld.questphase` / h73 / 233 -> 261 -> 263 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_halocall_debrief.scene` / scene / 249 -> 272 -> 253 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_halocall_debrief.scene` / scene / 288 -> 286 -> 290 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_halocall_debrief.scene` / scene / 74 -> 288 -> 286 |
| `057faf6705431d5dcd46` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_gameplay.questphase` / h255 / 8 -> 13 -> 88 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\scenes\sts_wat_kab_06_halocall_debrief.scene` / scene / 4 -> 73 -> 75 |
| `138cff49923a75e07348` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_openworld.questphase` / h73 / 101 -> 102 -> 103 |
| `1fb1217b6d69ef2494f3` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_gameplay.questphase` / h255 / 132 -> 131 -> 135 |
| `5c5e9486af30e2f834ec` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_openworld.questphase` / h73 / 233 -> 102 -> 103 |
| `5c76d3bf7160f29b884f` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_bugfixing.questphase` / h2 / 5 -> 6 -> 7 |
| `6babc5386a30099b5bdb` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_gameplay.questphase` / h255 / 7 -> 8 -> 153 |
| `7c95935bb7561609101d` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_gameplay.questphase` / h255 / 13 -> 88 -> 113 |
| `9380dda43f90ecd62efb` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_prestate_control.questphase` / h0 / 31 -> 32 -> 33 |
| `999952894b2b547e9107` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_gameplay.questphase` / h255 / 5 -> 6 -> 7 |
| `a5f6ff0df46f7043f2b5` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_openworld.questphase` / h73 / 236 -> 237 -> 238 |
| `aa4581931f52160c0919` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_gameplay.questphase` / h255 / 13 -> 88 -> 97 |
| `b7e863bd58c0072f3308` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_06\phase\sts_wat_kab_06_openworld.questphase` / h73 / 277 -> 224 -> 228 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
