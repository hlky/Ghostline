# base-ma-std-arr-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\community\ma_std_arr_09_cars.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\community\ma_std_arr_09_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\phases\ma_std_arr_09_bugfixing.questphase` | repair | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_09/onscreens/ma_std_arr_09_onscreen_01`
- `points_of_interest/minor_activities/ma_std_arr_09`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 3 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 3 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 21 -> 69 -> 70 |
| `72e515c7cbc883d0aba3` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 77 -> 21 -> 38 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 46 -> 91 -> 89 |
| `03d4cdcc208ff1f24d3a` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 48 -> 35 -> 77 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 91 -> 88 -> 87 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 54 -> 74 -> 47 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 73 -> 91 -> 89 |
| `163b243e32c0bb8c4eb7` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 48 -> 35 -> 29 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 85 -> 79 -> 80 |
| `1b6870785e1a3fdbaace` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 77 -> 21 -> 24 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 41 -> 73 -> 91 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 91 -> 90 -> 87 |
| `3457629da944eac3b4b2` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 5 -> 48 -> 35 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 88 -> 87 -> 32 |
| `3508e8ab45a0ac1cbb9b` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\phases\ma_std_arr_09_bugfixing.questphase` / h0 / 5 -> 2 -> 1 |
| `4c7ebd8b4557df747ce3` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 81 -> 82 -> 83 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 73 -> 46 -> 91 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 46 -> 91 -> 90 |
| `628937a52a02aa813665` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 75 -> 86 -> 85 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_09\ma_std_arr_09.questphase` / h0 / 43 -> 45 -> 75 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
