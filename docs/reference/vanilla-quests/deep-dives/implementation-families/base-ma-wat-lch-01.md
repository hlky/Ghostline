# base-ma-wat-lch-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\community\ma_wat_lch_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_ich_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_ich_01.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase; base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\scenes\ma_wat_ich_01_chicken_test.scene |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` | content candidate | 3 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\scenes\ma_wat_lch_01_holocall_brief.scene |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\phases\ma_wat_lch_01.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\scenes\ma_wat_ich_01_chicken_test.scene` | test/debug | 0 / 4 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\scenes\ma_wat_lch_01_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_wat_lch_01`
- `points_of_interest/minor_activities/ma_wat_lch_01`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 13 |
| `questInputNodeDefinition` | 5 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 4 |
| `questMiscAICommandNode` | 7 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questCharacterStatusEffect_CondtionType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 19 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `022b4f9462189fe7c3e1` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h0 / 1 -> 14 -> 22 |
| `4e7757b259f5b870990d` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h0 / 1 -> 21 -> 22 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\scenes\ma_wat_lch_01_holocall_brief.scene` / scene / 67 -> 258 -> 256 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h0 / 65 -> 146 -> 128 |
| `0f374ac8f753ecdc05b1` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h0 / 1 -> 112 -> 113 |
| `4ab99460b939ee484420` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h0 / 1 -> 20 -> 22 |
| `4d841bac909aa5b6b8b6` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h289 / 24 -> 25 -> 20 |
| `66e17bf07a534afe17b2` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h28 / 5 -> 6 -> 10 |
| `74dc076b3f628ca067fc` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h289 / 0 -> 10 -> 35 |
| `8dd134aba6d607d4a590` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h0 / 114 -> 112 -> 113 |
| `94ee6c07a66cf79a95a8` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h289 / 23 -> 25 -> 20 |
| `956a18e11770fe167253` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h0 / 112 -> 113 -> 69 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\scenes\ma_wat_lch_01_holocall_brief.scene` / scene / 254 -> 67 -> 61 |
| `a1e68c9bb5f84b886201` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h0 / 97 -> 143 -> 98 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\scenes\ma_wat_lch_01_holocall_brief.scene` / scene / 258 -> 256 -> 260 |
| `ebf923273db7cf158f68` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h0 / 135 -> 136 -> 137 |
| `09a1b96bd416a1d2a34a` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h0 / 1 -> 25 -> 22 |
| `0bc8f68e59c0b883af0d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h0 / 152 -> 140 -> 144 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\scenes\ma_wat_lch_01_holocall_brief.scene` / scene / 28 -> 66 -> 68 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_01\ma_wat_lch_01_phase.questphase` / h28 / 5 -> 6 -> 2 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
