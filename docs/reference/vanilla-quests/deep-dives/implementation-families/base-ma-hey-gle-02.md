# base-ma-hey-gle-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\community\ma_hey_gle_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase; base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\phases\ma_hey_gle_02_combat.questphase; base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_chicken_test.scene; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` | content candidate | 2 / 0 | base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\phases\ma_hey_gle_02_combat.questphase; base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\phases\ma_hey_gle_02_combat.questphase` | content candidate | 2 / 0 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_chicken_test.scene` | test/debug | 0 / 4 |  |
| `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_hey_gle_02`
- `points_of_interest/minor_activities/ma_hey_gle_02`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 12 |
| `questInputNodeDefinition` | 4 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 6 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `scnChoiceNode[scnChoiceNodeNsAdaptiveLookAtParams,scnChoiceNodeNsMappinParams,scnChoiceNodeOption,scnInteractionShapeParams,scnNodeId,scnscreenplayItemId]` | 1 |
| `scnEndNode[scnNodeId]` | 4 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `6359f1951cb4cbc69ff1` | 3 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h0 / 0 -> 38 -> 40 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h0 / 4 -> 56 -> 35 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene` / scene / 256 -> 258 -> 260 |
| `e5742f9794e6583c67cb` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene` / scene / 63 -> 57 -> 58 |
| `e6f0d1a9c84e739fc6c0` | 2 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02.quest` / h0 / 0 -> 2 -> 5 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h59 / 8 -> 3 -> 5 |
| `0672ae8d2fae884916ec` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h59 / 3 -> 5 -> 2 |
| `07708100a0a35824ab4a` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h0 / 60 -> 44 -> 61 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene` / scene / 32 -> 62 -> 64 |
| `14d7f1f2f390b216461a` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h0 / 43 -> 60 -> 44 |
| `1520ebe4ea0bf9451321` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h0 / 5 -> 47 -> 43 |
| `162752495828228ada5e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h59 / 4 -> 7 -> 1 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h0 / 0 -> 4 -> 56 |
| `1d933adb5a617880c93e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene` / scene / 62 -> 64 -> 59 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h0 / 4 -> 56 -> 12 |
| `26762f051e7728f090ca` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene` / scene / 58 -> 61 -> 32 |
| `2beeeaa3b4da5300c035` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\scenes\ma_hey_gle_02_holocall_brief.scene` / scene / 1 -> 254 -> 63 |
| `3a715543ca56d2c2cfcd` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h0 / 5 -> 47 -> 1 |
| `42ca878854c6b758165e` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h59 / 2 -> 4 -> 7 |
| `4365cb473b16f3e76999` | 1 | `base\open_world\minor_activities\heywood\glen\ma_hey_gle_02\ma_hey_gle_02_phase.questphase` / h0 / 60 -> 44 -> 54 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
