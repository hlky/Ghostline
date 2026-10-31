# base-ma-bls-ina-se1-19

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\bls_ina_se1_19.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\bls_ina_se1_19.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\community\ma_bls_ina_se1_19_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_19/shards/ma_bls_ina_se1_19`
- `points_of_interest/minor_activities/ma_bls_ina_se1_19`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 22 -> 33 -> 31 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 33 -> 30 -> 29 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 24 -> 28 -> 23 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 30 -> 29 -> 24 |
| `1121a7f146103492ac60` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 31 -> 29 -> 12 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 27 -> 33 -> 31 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 29 -> 24 -> 28 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h38 / 25 -> 4 -> 2 |
| `18df34190d30ba0599e5` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 16 -> 0 -> 21 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 19 -> 27 -> 33 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 17 -> 18 -> 2 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 33 -> 32 -> 29 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 30 -> 29 -> 11 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 31 -> 29 -> 24 |
| `4123636c2b09a02fdc99` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h38 / 6 -> 8 -> 7 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 32 -> 29 -> 24 |
| `4db18aaae4b08d077f4e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h38 / 4 -> 2 -> 21 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 27 -> 22 -> 33 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 21 -> 3 -> 4 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_19\ma_bls_ina_se1_19_phase.questphase` / h0 / 22 -> 33 -> 32 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
