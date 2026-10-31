# base-ma-bls-ina-se5-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\community\ma_bls_ina_se5_09_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 1 |
| `questInputNodeDefinition` | 3 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 21 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `7edf0c9b5edb3c65c003` | 20 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h116 / 0 -> 10 -> 1 |
| `438d71cd5153e6a1a377` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h0 / 47 -> 54 -> 49 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h0 / 43 -> 57 -> 42 |
| `137bcff12e01a164913c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h0 / 16 -> 37 -> 2 |
| `2aa0f3a3b004f071652f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h43 / 3 -> 2 -> 1 |
| `34b48742c4257a2c4ed9` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h0 / 33 -> 16 -> 37 |
| `4046f7e0ed1087267da3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h0 / 14 -> 33 -> 16 |
| `83a3757c3e54bd269e2e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h0 / 35 -> 14 -> 33 |
| `90cf58434e79ce42af1e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h43 / 0 -> 7 -> 6 |
| `a3e5f861a4b71433135a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h43 / 6 -> 3 -> 2 |
| `a9350e05126ec08a441f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h0 / 33 -> 16 -> 43 |
| `d4832a84c1e22dd49d4b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h0 / 1 -> 35 -> 56 |
| `f576caab49a2928ada0b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h0 / 1 -> 35 -> 14 |
| `fee3756653cd083fb28e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h43 / 7 -> 6 -> 3 |
| `ff4c8a828496c45d7dfa` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se5\ma_bls_ina_se5_09\ma_bls_ina_se5_09_phase.questphase` / h0 / 16 -> 43 -> 57 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
