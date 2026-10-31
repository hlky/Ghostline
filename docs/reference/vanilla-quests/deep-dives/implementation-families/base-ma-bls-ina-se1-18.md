# base-ma-bls-ina-se1-18

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\community\ma_bls_ina_se1_18_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase |
| `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/badlands/se1/ma_bls_ina_se1_18/shards/ma_bls_ina_se1_18_a`
- `points_of_interest/minor_activities/ma_bls_ina_se1_18`
- `quests/minor_activities/badlands/se1/ma_bls_ina_se1_18`
- `quests/minor_activities/badlands/se1/ma_bls_ina_se1_18/description`
- `quests/minor_activities/badlands/se1/ma_bls_ina_se1_18/ma_bls_ina_se1_18/go_to_spot`
- `quests/minor_activities/badlands/se1/ma_bls_ina_se1_18/ma_bls_ina_se1_18/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEventManagerNodeDefinition` | 10 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 1 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0781ef00ea04c05ee418` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 16 -> 18 -> 113 |
| `dde3cfc86c1764319bba` | 2 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 0 -> 55 -> 78 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 65 -> 84 -> 63 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 115 -> 114 -> 65 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 122 -> 115 -> 114 |
| `0ea39c90296b8c8c526e` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 62 -> 64 -> 68 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 114 -> 65 -> 84 |
| `159599f19533cfcfe918` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 107 -> 106 -> 51 |
| `1737436a0cc54670e573` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 113 -> 112 -> 42 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 44 -> 45 -> 53 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 53 -> 54 -> 2 |
| `2d47d0d71291822610cc` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 75 -> 85 -> 86 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 119 -> 118 -> 114 |
| `2ea6dc8eef48b1cfc585` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 83 -> 62 -> 64 |
| `380e05c8b76fbf6ccaf7` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 9 -> 16 -> 18 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 118 -> 114 -> 65 |
| `44be803f707bb3e06953` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 112 -> 97 -> 96 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 115 -> 114 -> 44 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 112 -> 42 -> 43 |
| `536dc1d981889e57ea60` | 1 | `base\open_world\minor_activities\badlands\inland_avenue_se1\ma_bls_ina_se1_18\ma_bls_ina_se1_18_phase.questphase` / h0 / 119 -> 122 -> 115 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
