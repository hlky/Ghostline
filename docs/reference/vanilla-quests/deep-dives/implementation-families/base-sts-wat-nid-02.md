# base-sts-wat-nid-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\community\sts_wat_nid_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\community\sts_wat_nid_02_combat_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_bugfixing.questphase` | repair | 8 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_debriefs.scene |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_gameplay.questphase` | content candidate | 6 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_scene.scene |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` | content candidate | 6 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_debriefs.scene; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_prebrief.scene |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_phase.questphase` | content candidate | 1 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_gameplay.questphase; base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_debriefs.scene` | content candidate | 0 / 26 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_prebrief.scene` | content candidate | 0 / 22 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_scene.scene` | content candidate | 0 / 12 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\sts_wat_nid_02_def.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\sts_wat_nid_02_quest.quest` | content candidate | 1 / 0 | base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\sts_wat_nid_02_test.gamedef` | content candidate | 0 / 0 |  |

## Journal paths observed in these resources

- `contacts/regina_jones/regina_global_msg/sts_optional_failed_on_purpose_after_completion`
- `contacts/regina_jones/sts_wat_nid_02/brief`
- `contacts/regina_jones/sts_wat_nid_02/sts_wat_nid_02_debrief_fail`
- `contacts/regina_jones/sts_wat_nid_02/sts_wat_nid_02_debrief_success`
- `points_of_interest/street_stories/sts_wat_nid_02`
- `quests/street_stories/pacifica/coastview/sts_pac_cvi_02/sts_pac_cvi_02/get_to_the_van`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/brief`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/convey`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/convey/nomads`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/convey/nomads1`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/convey/nomads2`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/get_authorization`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/get_into`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/get_out`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/get_out1`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/inside`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/optional`
- `quests/street_stories/watson/northside_industrial_district/sts_wat_nid_02/sts_wat_nid_02/steal`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 2 |
| `questAudioNodeDefinition[questAudioMixNodeType]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 1 |
| `questCheckpointNodeDefinition` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 3 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questContentCondition,questContentLock_ConditionType]` | 2 |
| `questConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 17 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 4 |
| `questConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 5 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 3 |
| `questConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 2 |
| `questCutControlNodeDefinition` | 6 |
| `questDeletionMarkerNodeDefinition` | 18 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleDespawn_NodeType]` | 3 |
| `questDynamicSpawnSystemNodeDefinition[questDynamicVehicleSpawn_NodeType]` | 5 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 11 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 47 |
| `questFlowControlNodeDefinition` | 1 |
| `questGameManagerNodeDefinition[questBlockTokenActivation_NodeSubType,questContentTokenManager_NodeType]` | 6 |
| `questGameManagerNodeDefinition[questContentTokenManager_NodeType,questSpawnToken_NodeSubType]` | 2 |
| `questInputNodeDefinition` | 25 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 46 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 4 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 6 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 29 |
| `questLogicalAndNodeDefinition` | 7 |
| `questLogicalHubNodeDefinition` | 17 |
| `questLogicalXorNodeDefinition` | 9 |
| `questMappinManagerNodeDefinition` | 19 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 3 |
| `questMovePuppetNodeDefinition[questPatrolParams]` | 4 |
| `questOutputNodeDefinition` | 24 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questCharacterMount_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHealth_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType,questLogicalCondition,questVehicleCondition,questVehicleWater_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questFactsDBCondition,questLogicalCondition,questTriggerCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questContentCondition,questContentLock_ConditionType,questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 27 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneInterrupt_ConditionType,scnCheckSpeakerDistractedInterruptCondition]` | 2 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 20 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpeed_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 22 |
| `questRandomizerNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 5 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 16 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questUIManagerNodeDefinition[questProgressBar_NodeType]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 23 |
| `questVehicleNodeDefinition[questSpawnPlayerVehicle_NodeType,questUniversalRef]` | 2 |
| `questVehicleNodeDefinition[questStopVehicle_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 6 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnCutControlNode[scnNodeId]` | 2 |
| `scnDeletionMarkerNode[scnNodeId]` | 2 |
| `scnEndNode[scnNodeId]` | 6 |
| `scnHubNode[scnNodeId]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 2 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 5 |
| `scnStartNode[scnNodeId]` | 4 |
| `scnXorNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9380dda43f90ecd62efb` | 20 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` / h1459 / 8 -> 10 -> 9 |
| `9f1005d23768724adb43` | 9 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_gameplay.questphase` / h136 / 59 -> 61 -> 62 |
| `2687500265c21d85d3de` | 8 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_gameplay.questphase` / h136 / 58 -> 59 -> 61 |
| `4991ad5f0514af8af7a0` | 8 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_gameplay.questphase` / h136 / 73 -> 58 -> 59 |
| `eaf5aab427d50e5598b6` | 7 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_bugfixing.questphase` / h12 / 0 -> 2 -> 3 |
| `10c2ecb8df5575125f58` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` / h426 / 57 -> 59 -> 62 |
| `1cfa47eb6d677e74c588` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_gameplay.questphase` / h136 / 0 -> 48 -> 15 |
| `2637d11cc89d07560812` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` / h1308 / 2 -> 9 -> 10 |
| `415eb0e0e097f846c0af` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` / h426 / 59 -> 62 -> 55 |
| `5dfe7f97718e5a76c201` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` / h108 / 27 -> 79 -> 26 |
| `74633650611293a65a15` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` / h426 / 105 -> 106 -> 107 |
| `bbf9efd740881cf31a37` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_debriefs.scene` / scene / 84 -> 251 -> 249 |
| `bed0a8302bb0fc509580` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` / h426 / 55 -> 57 -> 59 |
| `bed5a14f2c0a03714fe4` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_bugfixing.questphase` / h283 / 20 -> 11 -> 13 |
| `bf8527305d1d6176d770` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` / h108 / 83 -> 79 -> 26 |
| `d6b7c21f5d2d0ab76fc6` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_debriefs.scene` / scene / 282 -> 284 -> 286 |
| `d8da792a5e5d2849d6fc` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_scene.scene` / scene / 187 -> 251 -> 188 |
| `e5742f9794e6583c67cb` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\scenes\sts_wat_nid_02_holocall_debriefs.scene` / scene / 90 -> 282 -> 284 |
| `ebb0bb098dccc13b6987` | 4 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` / h426 / 62 -> 55 -> 58 |
| `280ad7b1a349d1244221` | 3 | `base\open_world\street_stories\watson\northside_industrial_district\sts_wat_nid_02\phases\sts_wat_nid_02_ow.questphase` / h1308 / 4 -> 11 -> 8 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
