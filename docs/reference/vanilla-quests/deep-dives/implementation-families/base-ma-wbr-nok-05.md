# base-ma-wbr-nok-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\community\ma_wbr_nok_05_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\community\ma_wbr_nok_05_netrunner.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\community\ma_wbr_nok_05_reinf.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\community\ma_wbr_nok_05_workers.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` | content candidate | 3 / 0 | base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\scenes\ma_wbr_nok_05_holocall_brief.scene |
| `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\scenes\ma_wbr_nok_05_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_wbr_nok_05`
- `points_of_interest/minor_activities/ma_wbr_nok_05`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 11 |
| `questInputNodeDefinition` | 4 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 3 |
| `questMiscAICommandNode` | 6 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 12 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\scenes\ma_wbr_nok_05_holocall_brief.scene` / scene / 67 -> 258 -> 256 |
| `47cc5074c53050699ba3` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 114 -> 116 -> 117 |
| `721dd253f632c98c4268` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 113 -> 116 -> 117 |
| `79c97502af9fb3eb977e` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 115 -> 116 -> 117 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\scenes\ma_wbr_nok_05_holocall_brief.scene` / scene / 254 -> 67 -> 61 |
| `b507ddedd777cafe9ef4` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 20 -> 10 -> 32 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\scenes\ma_wbr_nok_05_holocall_brief.scene` / scene / 258 -> 256 -> 260 |
| `0e1683196e9d3de4816f` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 112 -> 107 -> 109 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\scenes\ma_wbr_nok_05_holocall_brief.scene` / scene / 26 -> 66 -> 68 |
| `14d7f1f2f390b216461a` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 103 -> 130 -> 104 |
| `1520ebe4ea0bf9451321` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 91 -> 106 -> 103 |
| `178ff9eba50354aed786` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 0 -> 2 -> 20 |
| `1d933adb5a617880c93e` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\scenes\ma_wbr_nok_05_holocall_brief.scene` / scene / 66 -> 68 -> 63 |
| `1ef61236d6443802e900` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 88 -> 91 -> 106 |
| `26762f051e7728f090ca` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\scenes\ma_wbr_nok_05_holocall_brief.scene` / scene / 62 -> 65 -> 26 |
| `27b2de39d77df315d6e2` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 20 -> 10 -> 21 |
| `2beeeaa3b4da5300c035` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\scenes\ma_wbr_nok_05_holocall_brief.scene` / scene / 59 -> 254 -> 67 |
| `4365cb473b16f3e76999` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 130 -> 104 -> 120 |
| `4899e1c5d1a3acedd51b` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 103 -> 130 -> 131 |
| `490f94d7b3e0e9e28605` | 1 | `base\open_world\minor_activities\westbrook\north_oak\ma_wbr_nok_05\ma_wbr_nok_05_phase.questphase` / h0 / 2 -> 20 -> 86 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
