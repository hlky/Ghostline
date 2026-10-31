# base-ma-pac-cvi-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\community\ma_pac_cvi_09_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\community\ma_pac_cvi_09_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/pacifica/coastview/ma_pac_cvi_09/shards/ma_pac_cvi_09`
- `points_of_interest/minor_activities/ma_pac_cvi_09`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 11 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 4 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 6 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `a7629f14706d6b7addef` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 56 -> 57 -> 61 |
| `c92f06f761368a14f455` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 2 -> 25 -> 46 |
| `c979dc8cc7db14abf187` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 47 -> 49 -> 56 |
| `d30dec206567a53c3ede` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 25 -> 46 -> 50 |
| `d91a9f204f2f2c336b02` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 50 -> 52 -> 53 |
| `e2f47ae0316d4ceab903` | 2 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 54 -> 55 -> 59 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 43 -> 70 -> 68 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 70 -> 67 -> 66 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 44 -> 65 -> 45 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 64 -> 70 -> 68 |
| `1258cee37e98f0ae14fe` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 33 -> 40 -> 44 |
| `12b102391853a0e26cba` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 2 -> 25 -> 42 |
| `178360ac35259ce804ee` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 0 -> 28 -> 2 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 39 -> 64 -> 70 |
| `28db20c91b639a09afae` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 66 -> 36 -> 31 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 70 -> 69 -> 66 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 67 -> 66 -> 23 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 66 -> 23 -> 33 |
| `4365e94e7169e2520841` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 67 -> 66 -> 1 |
| `4516ea8d7bcf8c04ba50` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_09\ma_pac_cvi_09_phase.questphase` / h0 / 68 -> 66 -> 1 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
