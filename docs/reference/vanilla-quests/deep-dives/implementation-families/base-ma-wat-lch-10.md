# base-ma-wat-lch-10

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\community\ma_wat_lch_10_after_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\community\ma_wat_lch_10_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questEventManagerNodeDefinition` | 2 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_ActionProperty,questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 5 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 7 |
| `questPhaseNodeDefinition` | 2 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `9380dda43f90ecd62efb` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h20 / 8 -> 10 -> 11 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 32 -> 131 -> 33 |
| `0a4e2b5e61acb849c23e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h20 / 11 -> 9 -> 12 |
| `0c5acabadd2c6d7f6dd6` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 65 -> 87 -> 93 |
| `16bd8181563a0ab4b081` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h20 / 4 -> 6 -> 7 |
| `18234e6031e5e28cfa4b` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 65 -> 94 -> 105 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h20 / 2 -> 3 -> 4 |
| `3ba574dfab7ca00c88a8` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 105 -> 95 -> 129 |
| `4123636c2b09a02fdc99` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h20 / 9 -> 12 -> 13 |
| `7f7aef6d600415a71d43` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 104 -> 105 -> 88 |
| `918fa6020952c5f6e22e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 95 -> 129 -> 96 |
| `97747716a7dd75f86a89` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 90 -> 129 -> 96 |
| `978a69b98137186c49a7` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10.quest` / h0 / 2 -> 1 -> 0 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 0 -> 63 -> 77 |
| `9ae2d667c082e0256936` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 94 -> 105 -> 88 |
| `a329860a257b138886c2` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h20 / 3 -> 4 -> 6 |
| `b2a5237925e3bf6d6ce1` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 6 -> 8 -> 32 |
| `bab099eee80b3aa83e38` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 104 -> 105 -> 90 |
| `c19c10b8d44c0ffe1d01` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 63 -> 77 -> 103 |
| `c96df7fdb4914831a6ab` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_10\ma_wat_lch_10_phase.questphase` / h0 / 92 -> 6 -> 8 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
