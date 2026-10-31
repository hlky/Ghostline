# base-sts-wat-nid-06

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\communities\sts_wat_nid_06_enemies_inside_ground_floor.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\communities\sts_wat_nid_06_enemies_outside.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_combat.questphase` | content candidate | 6 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_leader_001.scene; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_leader_to_truck.scene; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_truck_scene.scene |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` | content candidate | 4 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_prebrief.scene |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_phase.questphase` | content candidate | 3 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_combat.questphase; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` | content candidate | 0 / 23 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_leader_001.scene` | content candidate | 0 / 8 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_leader_to_truck.scene` | content candidate | 0 / 4 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_truck_scene.scene` | content candidate | 0 / 4 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\sts_wat_nid_06_definition.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\sts_wat_nid_06_quest.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |

## Journal paths observed in these resources

- `contacts/regina_jones/sts_wat_nid_06/sts_wat_nid_05_holocall_debrief`
- `contacts/regina_jones/sts_wat_nid_06/sts_wat_nid_06_brief`
- `points_of_interest/street_stories/sts_wat_nid_06`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/brief`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/deliver_files`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/escape_abandoned_warehouse`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/get_inside`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/locate_data_drive`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/locate_data_drive/area_shard`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/take`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_06/sts_wat_nid_06/take/take_mp`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 1 |
| `questCheckpointNodeDefinition` | 3 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 10 |
| `questEndNodeDefinition` | 1 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 1 |
| `questEventManagerNodeDefinition` | 9 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 23 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 3 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 14 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 4 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 12 |
| `questLogicalAndNodeDefinition` | 5 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMappinManagerNodeDefinition` | 2 |
| `questMiscAICommandNode` | 8 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef,questWithCompanionMoveOnSplineParams]` | 1 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 16 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 3 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPhaseNodeDefinition` | 12 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSendAICommandNodeDefinition[questPatrolParams]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 12 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 5 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 7 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 8 |
| `scnStartNode[scnNodeId]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1141df90534d0bd100ec` | 5 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_combat.questphase` / h12 / 22 -> 7 -> 37 |
| `5a153f4a566c89a7303e` | 5 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_combat.questphase` / h308 / 7 -> 60 -> 20 |
| `5d544a83878871e8ae66` | 5 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_combat.questphase` / h308 / 106 -> 107 -> 20 |
| `6824f5988760343a451a` | 5 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_combat.questphase` / h12 / 4 -> 7 -> 37 |
| `875db287de4c4f2dc8dd` | 5 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_combat.questphase` / h12 / 5 -> 7 -> 37 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 267 -> 259 -> 249 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 283 -> 281 -> 285 |
| `2e362801d31d08a7d108` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 279 -> 62 -> 267 |
| `3b70bb506b872cadfa43` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_leader_001.scene` / scene / 1 -> 32 -> 2 |
| `9fb00f8e8ea036da0a73` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_combat.questphase` / h159 / 65 -> 56 -> 91 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 69 -> 64 -> 65 |
| `101b60945ddf6f25f378` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 17 -> 67 -> 69 |
| `10d2bed67733d8456950` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 259 -> 63 -> 66 |
| `129f2cf1d416edbd0fd1` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 267 -> 259 -> 63 |
| `131b32350d75ba8b8bfe` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_prebrief.scene` / scene / 269 -> 273 -> 279 |
| `1d933adb5a617880c93e` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 67 -> 69 -> 64 |
| `26762f051e7728f090ca` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 63 -> 66 -> 17 |
| `2b8291b6d86672a1ab66` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_leader_001.scene` / scene / 24 -> 22 -> 2 |
| `2beeeaa3b4da5300c035` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\scenes\sts_wat_nid_06_holocall_debrief.scene` / scene / 1 -> 68 -> 279 |
| `3fe0ae98a8cf5496b004` | 2 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_06\phases\sts_wat_nid_06_openworld.questphase` / h126 / 115 -> 113 -> 112 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
