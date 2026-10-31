# base-ma-wat-kab-109

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\community\ma_wat_kab_109_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 2 -> 24 -> 11 |
| `a3e5f861a4b71433135a` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 21 -> 22 -> 19 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 4 -> 8 -> 1 |
| `2252a132cf17333b3476` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 3 -> 4 -> 8 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 2 -> 24 -> 6 |
| `2465cabc5e4b65280bdb` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 19 -> 2 -> 24 |
| `2aa0f3a3b004f071652f` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h58 / 3 -> 9 -> 1 |
| `34b48742c4257a2c4ed9` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 7 -> 3 -> 10 |
| `4947cc5bd61f76664b84` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 22 -> 19 -> 2 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 24 -> 11 -> 6 |
| `4d6a34d4f440a16559f5` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 6 -> 7 -> 3 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 24 -> 6 -> 7 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 11 -> 6 -> 7 |
| `8096bdeebfe3cf375699` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 0 -> 20 -> 21 |
| `8370c76cbc0899b84848` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 7 -> 3 -> 4 |
| `a9350e05126ec08a441f` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 7 -> 3 -> 13 |
| `ea4cb15199b9b3fa8e63` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h58 / 0 -> 4 -> 3 |
| `ff4c8a828496c45d7dfa` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_109\ma_wat_kab_109_phase.questphase` / h0 / 3 -> 13 -> 25 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
