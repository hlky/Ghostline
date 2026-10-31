# base-ma-cct-dtn-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\community\ma_cct_dtn_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/city_center/downtown/ma_cct_dtn_01/onscreens/ma_cct_dtn_01_onscreen_02`
- `points_of_interest/minor_activities/ma_cct_dtn_01`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 6 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `e5a365e1a95473e2e5a7` | 3 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 20 -> 21 -> 33 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 47 -> 44 -> 43 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 10 -> 37 -> 27 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 20 -> 21 -> 23 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 1 -> 10 -> 37 |
| `25e95738e237951bd227` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 46 -> 43 -> 20 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 47 -> 46 -> 43 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 17 -> 47 -> 46 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 44 -> 43 -> 12 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 5 -> 3 -> 18 |
| `58cbc3ff47a2570c94cd` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 43 -> 20 -> 21 |
| `66e17bf07a534afe17b2` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 20 -> 21 -> 24 |
| `69ac42d59aa43099e19c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 14 -> 38 -> 28 |
| `6a4895bae96f73e30124` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 45 -> 43 -> 20 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 16 -> 17 -> 47 |
| `71892f49b88f7b8bb8be` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 1 -> 10 -> 16 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 47 -> 45 -> 43 |
| `7ab698c317f00ab32676` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 17 -> 47 -> 45 |
| `7efac81a2bd0fa9801ad` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 44 -> 43 -> 20 |
| `8d10896873df5c62014e` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_01\ma_cct_dtn_01_phase.questphase` / h0 / 0 -> 5 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
