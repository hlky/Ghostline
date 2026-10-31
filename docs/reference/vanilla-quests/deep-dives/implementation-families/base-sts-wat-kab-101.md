# base-sts-wat-kab-101

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\community\sta_wat_kab_101_reinforcements.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\community\sts_wat_kab_101_drone.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\community\sts_wat_kab_101_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\community\sts_wat_kab_101_residentials.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\community\sts_wat_kab_101_residentials_during.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_combat.questphase; base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_after.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_bugfixing.questphase` | repair | 3 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_combat.questphase` | content candidate | 3 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` | content candidate | 4 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_debrief.scene; base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_prebrief.scene |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_debrief.scene` | content candidate | 0 / 26 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\sts_wat_kab_101.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\sts_wat_kab_101.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101.questphase |

## Journal paths observed in these resources

- `contacts/regina_jones/regina_global_msg/sts_fail_msg_001`
- `contacts/regina_jones/regina_global_msg/sts_fail_warning_001`
- `contacts/regina_jones/regina_global_msg/sts_fail_warning_002`
- `contacts/regina_jones/regina_global_msg/sts_fail_warning_003`
- `contacts/regina_jones/regina_global_msg/sts_warning_fail_001`
- `contacts/regina_jones/regina_global_msg/sts_warning_fail_002`
- `contacts/regina_jones/sts_wat_kab_101/brief`
- `contacts/regina_jones/sts_wat_kab_101/sts_wat_kab_101_debrief_kill`
- `contacts/regina_jones/sts_wat_kab_101/sts_wat_kab_101_debrief_unconscious`
- `points_of_interest/street_stories/sts_wat_kab_101`
- `quests/street_stories/watson/kabuki/sts_wat_kab_101`
- `quests/street_stories/watson/kabuki/sts_wat_kab_101/brief`
- `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/call_transport`
- `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/drop_body`
- `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/find_target`
- `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/get_to_area`
- `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/kill_target`
- `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/leave_area`
- `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/take_body_outside`
- `quests/street_stories/watson/kabuki/sts_wat_kab_101/sts_wat_kab_101/transport_jae_hyun_body`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetStatusEffect,questRecordSelector]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 10 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 7 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 30 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 14 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 35 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 4 |
| `questLogicalXorNodeDefinition` | 4 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questGatherTriggerCondition,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition,questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questGatherTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleTrunk_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 9 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRandomizerNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 8 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 4 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 1 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 1 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 7 |
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
| `92b3cad066674f2a5860` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h90 / 7 -> 172 -> 219 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_debrief.scene` / scene / 249 -> 252 -> 254 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_debrief.scene` / scene / 283 -> 281 -> 285 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_debrief.scene` / scene / 80 -> 283 -> 281 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_debrief.scene` / scene / 24 -> 79 -> 81 |
| `44806a3e994b285e7365` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h90 / 60 -> 191 -> 183 |
| `47cc5074c53050699ba3` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h90 / 100 -> 101 -> 104 |
| `721dd253f632c98c4268` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h90 / 99 -> 101 -> 104 |
| `a5f6ff0df46f7043f2b5` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h90 / 156 -> 157 -> 158 |
| `b4342fd5660f9b85e16a` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h90 / 174 -> 201 -> 66 |
| `b7e863bd58c0072f3308` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h90 / 80 -> 207 -> 211 |
| `e1c15acc1f91be3ed2f0` | 3 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h90 / 172 -> 241 -> 183 |
| `0781ef00ea04c05ee418` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h90 / 171 -> 13 -> 197 |
| `08237f8e0854872f8f98` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h1162 / 75 -> 77 -> 79 |
| `0d9fa3a4b96defe7633b` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h90 / 15 -> 8 -> 215 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_debrief.scene` / scene / 252 -> 75 -> 78 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_debrief.scene` / scene / 249 -> 252 -> 75 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_prebrief.scene` / scene / 270 -> 273 -> 279 |
| `1b27512194d3f275c13e` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\phases\sts_wat_kab_101_openworld.questphase` / h90 / 172 -> 8 -> 215 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\watson\kabuki\sts_wat_kab_101\scenes\sts_wat_kab_101_holocall_debrief.scene` / scene / 79 -> 81 -> 76 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
