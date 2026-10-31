# base-ma-bls-ina-se1-16

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\community\ma_bls_ina_se1_16_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\community\ma_bls_ina_se1_16_com_fluff.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_16/onscreens/ma_bls_ina_se1_16_nomad`
- `points_of_interest/minor_activities/ma_bls_ina_se1_16`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `ae26d9b3c8043dedb4cc` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 55 -> 50 -> 51 |
| `cba245dc8dd815e4dc63` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 56 -> 55 -> 50 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 35 -> 61 -> 59 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 61 -> 58 -> 57 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 37 -> 46 -> 36 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 58 -> 57 -> 37 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 45 -> 61 -> 59 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 57 -> 37 -> 46 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 41 -> 45 -> 61 |
| `2d61756ead564fdbaa1f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 9 -> 56 -> 55 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 61 -> 60 -> 57 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 58 -> 57 -> 17 |
| `354e0603fdbd00ceb27b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 57 -> 48 -> 47 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 59 -> 57 -> 37 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 60 -> 57 -> 37 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 45 -> 35 -> 61 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 35 -> 61 -> 60 |
| `54ed0f5a452de7226f9b` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 58 -> 57 -> 48 |
| `56fb3f6e9c6b9755b1f3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 60 -> 57 -> 48 |
| `5870e2fba5607932758d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_16\ma_bls_ina_se1_16_phase.questphase` / h0 / 55 -> 16 -> 42 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
