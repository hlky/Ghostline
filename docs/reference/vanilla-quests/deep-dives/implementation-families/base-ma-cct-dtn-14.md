# base-ma-cct-dtn-14

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\community\ma_cct_dtn_14_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/city_center/downtown/ma_cct_dtn_14/onscreens/ma_cct_dtn_14_onscreen_02`
- `points_of_interest/minor_activities/ma_cct_dtn_14`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
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
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 31 -> 47 -> 45 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 25 -> 26 -> 35 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 47 -> 44 -> 43 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 40 -> 47 -> 45 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 25 -> 26 -> 24 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 18 -> 40 -> 47 |
| `204ca9b8b94427c1ef81` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 42 -> 41 -> 32 |
| `25e95738e237951bd227` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 46 -> 43 -> 25 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 47 -> 46 -> 43 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 44 -> 43 -> 13 |
| `3de51e6fe8bd91ef54c9` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 1 -> 30 -> 28 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 43 -> 13 -> 14 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 40 -> 31 -> 47 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 1 -> 22 -> 21 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 31 -> 47 -> 46 |
| `58cbc3ff47a2570c94cd` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 43 -> 25 -> 26 |
| `60a306c2bf9dcf430a17` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 13 -> 14 -> 16 |
| `66e17bf07a534afe17b2` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 25 -> 26 -> 23 |
| `6a4895bae96f73e30124` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 45 -> 43 -> 25 |
| `71892f49b88f7b8bb8be` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_14\ma_cct_dtn_14_phase.questphase` / h0 / 2 -> 11 -> 17 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
