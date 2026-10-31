# base-ma-wat-nid-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\community\ma_wat_nid_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase; base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_chicken_test.scene |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` | content candidate | 3 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_holocall_brief.scene |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_chicken_test.scene` | test/debug | 0 / 5 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_wat_nid_02`
- `points_of_interest/minor_activities/ma_wat_nid_02`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 8 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 14 |
| `questInputNodeDefinition` | 4 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 5 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `aaf8bd8d6aaaed4808d2` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h0 / 117 -> 64 -> 66 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_holocall_brief.scene` / scene / 254 -> 258 -> 256 |
| `570676cffa83a3c52c8e` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h0 / 0 -> 91 -> 52 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_holocall_brief.scene` / scene / 64 -> 254 -> 58 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_holocall_brief.scene` / scene / 258 -> 256 -> 260 |
| `02b5b1790eec80cd653e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h0 / 11 -> 145 -> 67 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h0 / 117 -> 9 -> 10 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h0 / 110 -> 142 -> 109 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h28 / 11 -> 4 -> 12 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_holocall_brief.scene` / scene / 4 -> 63 -> 65 |
| `14d7f1f2f390b216461a` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h0 / 111 -> 146 -> 113 |
| `1520ebe4ea0bf9451321` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h0 / 117 -> 140 -> 111 |
| `1d933adb5a617880c93e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_holocall_brief.scene` / scene / 63 -> 65 -> 60 |
| `212e4cae08d1d6865934` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h0 / 117 -> 110 -> 142 |
| `26762f051e7728f090ca` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_holocall_brief.scene` / scene / 59 -> 62 -> 4 |
| `2beeeaa3b4da5300c035` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\scenes\ma_wat_nid_02_holocall_brief.scene` / scene / 1 -> 64 -> 254 |
| `344712efef5e632e1bd5` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h28 / 6 -> 7 -> 8 |
| `3de51e6fe8bd91ef54c9` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h153 / 3 -> 5 -> 6 |
| `4365cb473b16f3e76999` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h0 / 146 -> 113 -> 139 |
| `4899e1c5d1a3acedd51b` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_02\ma_wat_nid_02_phase.questphase` / h0 / 111 -> 146 -> 147 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
