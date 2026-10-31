# base-ma-cct-dtn-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\community\ma_cct_dtn_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\community\ma_cct_dtn_02_com_victim.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/city_center/downtown/ma_cct_dtn_02/onscreens/ma_cct_dtn_02_onscreen_01`
- `points_of_interest/minor_activities/ma_cct_dtn_02`

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
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `18be198845c90c6bb3c8` | 3 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 32 -> 33 -> 34 |
| `a3e5f861a4b71433135a` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 32 -> 33 -> 41 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 54 -> 51 -> 50 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 23 -> 47 -> 38 |
| `178ff9eba50354aed786` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 2 -> 0 -> 42 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 2 -> 23 -> 47 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 23 -> 47 -> 27 |
| `25e95738e237951bd227` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 53 -> 50 -> 32 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 54 -> 53 -> 50 |
| `2e1ee5a1324dbeeb9071` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 0 -> 42 -> 1 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 28 -> 54 -> 53 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 51 -> 50 -> 25 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 47 -> 38 -> 27 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 47 -> 27 -> 28 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 1 -> 3 -> 31 |
| `58cbc3ff47a2570c94cd` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 50 -> 32 -> 33 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 38 -> 27 -> 28 |
| `66e17bf07a534afe17b2` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 32 -> 33 -> 35 |
| `69ac42d59aa43099e19c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 26 -> 48 -> 39 |
| `6a4895bae96f73e30124` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_02\ma_cct_dtn_02_phase.questphase` / h0 / 52 -> 50 -> 32 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
