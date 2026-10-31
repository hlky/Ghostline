# base-ma-wat-kab-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\communities\ma_wat_kab_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `points_of_interest/minor_activities/ma_wat_kab_04`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 4 |
| `questCombatNodeDefinition[questCombatNodeParams_RestrictMovementToArea]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `480a010388ce3a487ffb` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 10 -> 11 -> 12 |
| `82a9643bae17b90ed0b6` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 27 -> 11 -> 12 |
| `a36102ceee6fef729c5f` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 25 -> 11 -> 12 |
| `d8ef39870626a261efb0` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 26 -> 11 -> 12 |
| `fa5824c0efca270073ba` | 4 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 8 -> 9 -> 10 |
| `8d10896873df5c62014e` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 0 -> 6 -> 3 |
| `433b30c57bbf90bfb64b` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 9 -> 27 -> 11 |
| `72456e8dd927fd679172` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 9 -> 10 -> 11 |
| `7ee29249cbf782ce455c` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 6 -> 3 -> 5 |
| `8e1d2b6d16b0384b26b3` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 9 -> 25 -> 11 |
| `987122e5e2fcd167cf6c` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 1 -> 0 -> 6 |
| `999952894b2b547e9107` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 7 -> 8 -> 9 |
| `b7bc8d9b93db78f94b79` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 9 -> 26 -> 11 |
| `c4f8fa0bede88335c941` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 24 -> 7 -> 8 |
| `dc04802f9e0c5b3b29f3` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 6 -> 24 -> 7 |
| `e1d2991c0f5245d8ecd5` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 1 -> 32 -> 36 |
| `fdfd13158b6297073a04` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_04\ma_wat_kab_04_phase.questphase` / h0 / 32 -> 36 -> 37 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
