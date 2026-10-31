# base-ma-wat-kab-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\community\ma_wat_kab_07_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\community\ma_wat_kab_07_junkie.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/kabuki/ma_wat_kab_07/onscreens/ma_wat_kab_07_onscreen_01`
- `points_of_interest/minor_activities/ma_wat_kab_07`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 1 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questGameManagerNodeDefinition[questLootPurge_NodeType]` | 1 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterWorkspot_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 31 -> 63 -> 58 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h53 / 21 -> 8 -> 3 |
| `51d78876d4b7cc3025b7` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 11 -> 14 -> 12 |
| `7585a7d9dd9f1c5c3f92` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h53 / 3 -> 4 -> 7 |
| `c3a8b811b8c7c7ee308f` | 2 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 49 -> 4 -> 11 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 69 -> 66 -> 65 |
| `178360ac35259ce804ee` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 0 -> 49 -> 4 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 0 -> 31 -> 63 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 31 -> 63 -> 50 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 69 -> 68 -> 65 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 51 -> 69 -> 68 |
| `2f42e8df5c81cf29a5fc` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 0 -> 55 -> 56 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 66 -> 65 -> 30 |
| `3c6b36e8c01548f18f31` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 53 -> 33 -> 60 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 63 -> 58 -> 50 |
| `4c4ed316b40e2958b53f` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h53 / 3 -> 4 -> 18 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 63 -> 50 -> 51 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 58 -> 50 -> 51 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 50 -> 51 -> 69 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\watson\kabuki\ma_wat_kab_07\ma_wat_kab_07_phase.questphase` / h0 / 69 -> 67 -> 65 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
