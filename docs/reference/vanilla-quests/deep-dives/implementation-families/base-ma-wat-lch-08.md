# base-ma-wat-lch-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\community\ma_wat_lch_08_after_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\community\ma_wat_lch_08_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\community\ma_wat_lch_08_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` | content candidate | 6 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\scenes\ma_wat_lch_08_holocall_brief.scene |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\scenes\ma_wat_lch_08_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_wat_lch_08`
- `points_of_interest/minor_activities/ma_wat_lch_08`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 3 |
| `questCutControlNodeDefinition` | 9 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 17 |
| `questFlowControlNodeDefinition` | 2 |
| `questInputNodeDefinition` | 6 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questMiscAICommandNode` | 5 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 15 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 6 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 8 |
| `questPhaseNodeDefinition` | 4 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 22 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `5466f936f30ed8ee354a` | 9 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 105 -> 115 -> 116 |
| `8d10896873df5c62014e` | 9 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 101 -> 105 -> 115 |
| `2c20201f171f754c99e0` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 138 -> 139 -> 140 |
| `3ba86c71a70bfb0620a5` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 137 -> 138 -> 139 |
| `543b598a1b2fb7423e72` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 135 -> 139 -> 140 |
| `8edf5416ccd8dce9db72` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 134 -> 135 -> 139 |
| `9cbfb93ce558d1c73900` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 135 -> 137 -> 138 |
| `dcfede577730a0902ef6` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 134 -> 135 -> 137 |
| `51d78876d4b7cc3025b7` | 5 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 95 -> 26 -> 29 |
| `9ae03849cffc8e91964c` | 5 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 79 -> 80 -> 38 |
| `5a1e5eb45e2acdebe80e` | 4 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 101 -> 105 -> 114 |
| `bd4bb68e151a5a63deb7` | 4 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h14 / 7 -> 6 -> 10 |
| `f3a269b6a97862bc211c` | 4 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 101 -> 104 -> 30 |
| `20e74db83226e46cc202` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 114 -> 116 -> 106 |
| `23c83f846beb25d06b1d` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 105 -> 114 -> 116 |
| `2e1ee5a1324dbeeb9071` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 100 -> 101 -> 104 |
| `58c7e757cd8df0c755d4` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 115 -> 116 -> 107 |
| `5d544a83878871e8ae66` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 114 -> 116 -> 107 |
| `b90715b67cb6f4596277` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 105 -> 107 -> 106 |
| `cce8cd446d174ae41668` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_08\ma_wat_lch_08_phase.questphase` / h0 / 115 -> 116 -> 106 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
