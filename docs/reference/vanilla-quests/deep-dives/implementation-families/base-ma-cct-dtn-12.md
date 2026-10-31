# base-ma-cct-dtn-12

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\community\ma_cct_dtn_12_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\community\ma_cct_dtn_12a_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase |
| `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/city_center/downtown/ma_cct_dtn_12/onscreens/ma_cct_dtn_12_onscreen_02`
- `points_of_interest/minor_activities/ma_cct_dtn_12`
- `points_of_interest/minor_activities/ma_cct_dtn_12_b`
- `quests/minor_activities/city_center/downtown/ma_cct_dtn_12`
- `quests/minor_activities/city_center/downtown/ma_cct_dtn_12/description`
- `quests/minor_activities/city_center/downtown/ma_cct_dtn_12/ma_cct_dtn_12/go_to_corporate_parking`
- `quests/minor_activities/city_center/downtown/ma_cct_dtn_12/ma_cct_dtn_12/loot_vehicle`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 7 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 3 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 4 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questSetImmovable_NodeType]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `05204279a5fdb15c9ce0` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h317 / 2 -> 5 -> 4 |
| `808c42396a9735fe3a65` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 1 -> 8 -> 69 |
| `bff957bf33a10413a685` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 8 -> 69 -> 70 |
| `d4eed81f829edcc1a916` | 2 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h317 / 0 -> 8 -> 3 |
| `02c5a983de890662a298` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 73 -> 83 -> 88 |
| `034e4ec70e5e541255d2` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 46 -> 49 -> 2 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 19 -> 74 -> 60 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 34 -> 21 -> 22 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 1 -> 19 -> 74 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 35 -> 26 -> 39 |
| `204ca9b8b94427c1ef81` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 77 -> 75 -> 61 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 19 -> 74 -> 41 |
| `2c3d4d4eb6c82c8f1261` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 50 -> 48 -> 47 |
| `3560b3719769da7fd9fe` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 48 -> 47 -> 46 |
| `380e05c8b76fbf6ccaf7` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 37 -> 27 -> 28 |
| `3e42c30985b959b588d9` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h317 / 8 -> 3 -> 2 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 74 -> 60 -> 41 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 21 -> 22 -> 23 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 74 -> 41 -> 42 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\city_center\downtown\ma_cct_dtn_12\ma_cct_dtn_12_phase.questphase` / h0 / 60 -> 41 -> 42 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
