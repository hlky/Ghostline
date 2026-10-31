# base-sts-wat-kab-107

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\community\sts_wat_kab_107.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\community\sts_wat_kab_107_combat.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\community\sts_wat_kab_107_crowd.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\community\sts_wat_kab_107_ic_001.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\community\sts_wat_kab_107_ic_002.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_gameplay.questphase; base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_bugfixing.questphase` | repair | 2 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_gameplay.questphase` | content candidate | 4 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase` | content candidate | 4 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_holocall_debrief.scene; base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_prebrief.scene |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_prestate_control.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_holocall_debrief.scene` | content candidate | 0 / 25 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\sts_wat_kab_107.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\sts_wat_kab_107.quest` | content candidate | 2 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107.questphase |

## Journal paths observed in these resources

- `contacts/regina_jones/regina_global_msg/sts_fail_msg_002`
- `contacts/regina_jones/regina_global_msg/sts_fail_warning_001`
- `contacts/regina_jones/regina_global_msg/sts_fail_warning_002`
- `contacts/regina_jones/regina_global_msg/sts_fail_warning_003`
- `contacts/regina_jones/regina_global_msg/sts_warning_fail_002`
- `contacts/regina_jones/sts_wat_kab_107/brief`
- `contacts/regina_jones/sts_wat_kab_107/sts_wat_kab_107_debrief_kill`
- `contacts/regina_jones/sts_wat_kab_107/sts_wat_kab_107_debrief_unconscious`
- `points_of_interest/street_stories/sts_wat_kab_107`
- `quests/street_stories/watson/kabuki/sts_wat_kab_107`
- `quests/street_stories/watson/kabuki/sts_wat_kab_107/brief`
- `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/deliver`
- `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/find_target`
- `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/get_in`
- `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/get_out`
- `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/phone`
- `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/pick_up_unconscious_target`
- `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/pick_up_unconscious_target/pick_up_mp`
- `quests/street_stories/watson/kabuki/sts_wat_kab_107/sts_wat_kab_107/take_down`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 3 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 7 |
| `questDeletionMarkerNodeDefinition` | 16 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 29 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 17 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 8 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 33 |
| `questLogicalAndNodeDefinition` | 3 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMappinManagerNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 15 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition,questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 8 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleTrunk_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 9 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRandomizerNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 3 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 18 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 8 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 3 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 1 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 7 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 3 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `20a77143a898bc753a26` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_gameplay.questphase` / h7 / 52 -> 56 -> 41 |
| `282fd08593d53394f518` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_gameplay.questphase` / h7 / 51 -> 52 -> 56 |
| `a61ecf2b543faa254f2c` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_gameplay.questphase` / h7 / 0 -> 51 -> 54 |
| `ac686eb7c056939b5d16` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase` / h537 / 233 -> 288 -> 290 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_holocall_debrief.scene` / scene / 268 -> 283 -> 271 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_holocall_debrief.scene` / scene / 302 -> 300 -> 304 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_holocall_debrief.scene` / scene / 66 -> 302 -> 300 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_holocall_debrief.scene` / scene / 24 -> 72 -> 73 |
| `5c5e9486af30e2f834ec` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase` / h537 / 233 -> 107 -> 108 |
| `5d6c61989340099b16a6` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase` / h537 / 270 -> 265 -> 264 |
| `a5f6ff0df46f7043f2b5` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase` / h537 / 274 -> 275 -> 276 |
| `07708100a0a35824ab4a` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase` / h139 / 104 -> 49 -> 103 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_holocall_debrief.scene` / scene / 283 -> 64 -> 65 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_holocall_debrief.scene` / scene / 268 -> 283 -> 64 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_prebrief.scene` / scene / 270 -> 273 -> 279 |
| `138cff49923a75e07348` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase` / h537 / 122 -> 125 -> 126 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_holocall_debrief.scene` / scene / 72 -> 73 -> 70 |
| `234254ac7de914caba33` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase` / h537 / 233 -> 289 -> 306 |
| `260a0eeffeaa533b5c20` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\phases\sts_wat_kab_107_openworld.questphase` / h139 / 87 -> 95 -> 102 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_107\scenes\sts_wat_kab_107_holocall_debrief.scene` / scene / 1 -> 298 -> 66 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
