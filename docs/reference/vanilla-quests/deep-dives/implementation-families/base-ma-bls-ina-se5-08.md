# base-ma-bls-ina-se5-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\community\ma_bls_ina_se5_08_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\community\ma_bls_na_se5_08_com_wraith.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_Kill,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 4 |
| `questCheckpointNodeDefinition` | 1 |
| `questCombatNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 5 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 2 |
| `questLogicalAndNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questDevice_ConditionType,questLogicalCondition,questObjectCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVehicleNodeDefinition[questToggleForceBrake_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `987122e5e2fcd167cf6c` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 1 -> 0 -> 66 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 48 -> 94 -> 49 |
| `0b387b0e0f2538ab6067` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h41 / 4 -> 2 -> 8 |
| `137bcff12e01a164913c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 10 -> 5 -> 2 |
| `1437ef8be826c28f8233` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 66 -> 65 -> 56 |
| `2be56e12eb3d64f26e5a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 104 -> 85 -> 78 |
| `35e8676ac0e5808d43fa` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 51 -> 65 -> 56 |
| `367c2f29f7752b311361` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 81 -> 92 -> 91 |
| `4c86e9d12122e122fabf` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h41 / 2 -> 8 -> 3 |
| `4ceb17253b6ccc6b9061` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 41 -> 88 -> 45 |
| `5d8d196a0a535f75b2b5` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 40 -> 81 -> 92 |
| `65efdd073270a817e59e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 53 -> 54 -> 63 |
| `66e17bf07a534afe17b2` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h41 / 9 -> 4 -> 2 |
| `6ea58e757157e77562cf` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 98 -> 110 -> 108 |
| `736e12da56db0f348c65` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h41 / 3 -> 6 -> 7 |
| `73cae1e39fb2ebead7c5` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 9 -> 51 -> 65 |
| `808c42396a9735fe3a65` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 1 -> 9 -> 51 |
| `83a3757c3e54bd269e2e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 36 -> 12 -> 29 |
| `85f4bdeeacbf141e610a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 36 -> 12 -> 10 |
| `8e1d2b6d16b0384b26b3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_08\ma_bls_ina_se5_08_phase.questphase` / h0 / 0 -> 66 -> 65 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
