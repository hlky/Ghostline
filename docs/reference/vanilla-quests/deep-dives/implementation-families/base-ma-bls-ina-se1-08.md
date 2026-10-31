# base-ma-bls-ina-se1-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase` | repair | 3 / 0 |  |

## Journal paths observed in these resources

- `quests/minor_quest/ma_bls_ina_se1_08/ma_bls_ina_se1_08`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 2 |
| `questInputNodeDefinition` | 3 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questLogicalHubNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `200fadf2365b23aab171` | 1 | `base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase` / h0 / 14 -> 15 -> 16 |
| `2816b0a40335a1393b98` | 1 | `base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase` / h52 / 2 -> 8 -> 4 |
| `382a6bbc3bd5c2ab4724` | 1 | `base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase` / h52 / 8 -> 4 -> 5 |
| `54a967b9c7a9e7781745` | 1 | `base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase` / h52 / 0 -> 2 -> 8 |
| `7e3a3f8d8ab34aac107e` | 1 | `base\quest\bugfixing\minor_quests\ma_bls_ina_se1_08\ma_bls_ina_se1_08_quest_bugfixes.questphase` / h0 / 14 -> 15 -> 12 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
