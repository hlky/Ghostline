# base-ma-bls-ina-se1-17

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\community\ma_bls_ina_se1_17_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\phases\ma_bls_ina_se1_17_combat.questphase; base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_chicken_test.scene; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` | content candidate | 2 / 0 | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\phases\ma_bls_ina_se1_17_combat.questphase` | content candidate | 5 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_chicken_test.scene` | test/debug | 0 / 4 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene` | content candidate | 0 / 16 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_bls_ina_se1_17`
- `points_of_interest/minor_activities/ma_bls_ina_se1_17`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 12 |
| `questInputNodeDefinition` | 7 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 1 |
| `questMiscAICommandNode` | 5 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 8 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 4 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h0 / 21 -> 22 -> 15 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene` / scene / 96 -> 257 -> 259 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene` / scene / 254 -> 96 -> 90 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene` / scene / 257 -> 259 -> 261 |
| `e6f0d1a9c84e739fc6c0` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17.quest` / h0 / 2 -> 4 -> 5 |
| `02b5b1790eec80cd653e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h0 / 27 -> 77 -> 76 |
| `03997a006fcf1f3b4d06` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h0 / 59 -> 28 -> 66 |
| `07708100a0a35824ab4a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h0 / 79 -> 63 -> 81 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h0 / 61 -> 73 -> 60 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene` / scene / 30 -> 95 -> 97 |
| `12a9b2fa271cb8fd936b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h124 / 6 -> 12 -> 20 |
| `13455132e6fe4cc4bf73` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h124 / 22 -> 6 -> 12 |
| `14a4ae554fd86daf81d6` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h0 / 66 -> 27 -> 77 |
| `14d7f1f2f390b216461a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h0 / 62 -> 79 -> 63 |
| `1520ebe4ea0bf9451321` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h0 / 28 -> 66 -> 62 |
| `18df34190d30ba0599e5` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h0 / 71 -> 21 -> 22 |
| `1d933adb5a617880c93e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene` / scene / 95 -> 97 -> 92 |
| `21769f6b5e5a1e798875` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\ma_bls_ina_se1_17_phase.questphase` / h0 / 22 -> 70 -> 69 |
| `26762f051e7728f090ca` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene` / scene / 91 -> 94 -> 30 |
| `2beeeaa3b4da5300c035` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_17\scenes\ma_bls_ina_se1_17_holocall_brief.scene` / scene / 1 -> 254 -> 96 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
