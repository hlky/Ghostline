# base-sts-pac-cvi-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\community\sts_pac_cvi_02_combat.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase` | content candidate | 15 / 0 | base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_gangers.scene; base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene; base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_prebrief.scene; base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_johnny.scene |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02_bugfixing.questphase` | repair | 3 / 0 |  |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02_gameplay.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_gangers.scene` | content candidate | 0 / 8 |  |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene` | content candidate | 0 / 46 |  |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_johnny.scene` | content candidate | 0 / 8 |  |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_sasquatch.scene` | content candidate | 0 / 6 |  |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\sts_pac_cvi_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\sts_pac_cvi_02.quest` | content candidate | 1 / 0 | base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\sts_pac_cvi_02_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/mr_hands/sts_pac_cvi_02/brief`
- `contacts/mr_hands/sts_pac_cvi_02/sts_pac_cvi_02_fail`
- `contacts/mr_hands/sts_pac_cvi_02/sts_pac_cvi_02_success`
- `points_of_interest/street_stories/sts_pac_cvi_02`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/brief`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/convey_truck`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/deliver_chased`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/escape_by_van`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/find_truck`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/get_out`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/get_to_metro_station`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/get_to_the_van`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/steal`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 3 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 18 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 3 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 3 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 20 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleDespawn_NodeType]` | 2 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleSpawn_NodeType]` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 12 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 53 |
| `questFlowControlNodeDefinition` | 1 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 5 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 1 |
| `questInputNodeDefinition` | 18 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 38 |
| `questLogicalAndNodeDefinition` | 6 |
| `questLogicalHubNodeDefinition` | 13 |
| `questLogicalXorNodeDefinition` | 8 |
| `questMiscAICommandNode` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 17 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questDestruction_ConditionType,questLogicalCondition,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 18 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questObjectCondition,questScan_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 14 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckAnyoneDistractedInterruptCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 12 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleWater_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 18 |
| `questRandomizerNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnToggleInterruption_InterruptionOperation,scnWorldMarker]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawnSet_NodeType]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 13 |
| `questStartNodeDefinition` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 4 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnCutControlNode[scnNodeId]` | 3 |
| `scnDeletionMarkerNode[scnNodeId]` | 3 |
| `scnEndNode[scnNodeId]` | 11 |
| `scnHubNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 3 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 3 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 8 |
| `scnStartNode[scnNodeId]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `81867a7f03bd3dc79a1f` | 6 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase` / h726 / 56 -> 57 -> 60 |
| `bbf9efd740881cf31a37` | 6 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene` / scene / 318 -> 311 -> 301 |
| `d6b7c21f5d2d0ab76fc6` | 6 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene` / scene / 118 -> 119 -> 2 |
| `2e362801d31d08a7d108` | 5 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene` / scene / 361 -> 116 -> 318 |
| `9f1befbb8473cbc22766` | 5 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase` / h355 / 205 -> 208 -> 221 |
| `e8fc8e5f68ba8e86b8d3` | 5 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase` / h726 / 68 -> 70 -> 50 |
| `10c2ecb8df5575125f58` | 4 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase` / h726 / 43 -> 45 -> 49 |
| `2637d11cc89d07560812` | 4 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase` / h1572 / 2 -> 9 -> 10 |
| `415eb0e0e097f846c0af` | 4 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase` / h726 / 45 -> 49 -> 40 |
| `6deffcdb16038324e882` | 4 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase` / h726 / 56 -> 59 -> 58 |
| `8cd3b647ae3f592ad947` | 4 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_gangers.scene` / scene / 9 -> 13 -> 2 |
| `958362a327cc764f4423` | 4 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene` / scene / 318 -> 311 -> 301 |
| `9ed4b3521844f7918566` | 4 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase` / h726 / 73 -> 74 -> 69 |
| `bed0a8302bb0fc509580` | 4 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase` / h726 / 40 -> 43 -> 45 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene` / scene / 123 -> 118 -> 119 |
| `ebb0bb098dccc13b6987` | 4 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\phases\sts_pac_cvi_02.questphase` / h726 / 49 -> 40 -> 44 |
| `101b60945ddf6f25f378` | 3 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene` / scene / 17 -> 121 -> 123 |
| `10d2bed67733d8456950` | 3 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene` / scene / 311 -> 117 -> 120 |
| `129f2cf1d416edbd0fd1` | 3 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene` / scene / 318 -> 311 -> 117 |
| `1d933adb5a617880c93e` | 3 | `base\open_world\street_stories\pacifica\coastview\sts_pac_cvi_02\scenes\sts_pac_cvi_02_holocall_debriefs.scene` / scene / 121 -> 123 -> 118 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
