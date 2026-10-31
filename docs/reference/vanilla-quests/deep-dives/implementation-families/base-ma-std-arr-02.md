# base-ma-std-arr-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\community\ma_std_arr_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_02/onscreens/ma_std_arr_02_onscreen_01`
- `points_of_interest/minor_activities/ma_std_arr_02`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 6 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 5 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 56 -> 88 -> 98 |
| `31813be702f4c1be3421` | 3 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 0 -> 56 -> 61 |
| `a852d679ccc4f4f86414` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 88 -> 59 -> 58 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 123 -> 120 -> 119 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 70 -> 108 -> 92 |
| `1236b824035f3d3d10f6` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 115 -> 113 -> 116 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 117 -> 114 -> 115 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 0 -> 70 -> 108 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 123 -> 122 -> 119 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 89 -> 123 -> 122 |
| `3473788fa2e021211ee9` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 101 -> 104 -> 100 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 120 -> 119 -> 73 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 119 -> 73 -> 82 |
| `54ed0f5a452de7226f9b` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 120 -> 119 -> 110 |
| `56fb3f6e9c6b9755b1f3` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 122 -> 119 -> 110 |
| `60a306c2bf9dcf430a17` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 73 -> 82 -> 77 |
| `628937a52a02aa813665` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 110 -> 118 -> 117 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 81 -> 89 -> 123 |
| `71892f49b88f7b8bb8be` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 0 -> 70 -> 81 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_02\ma_std_arr_02_phase.questphase` / h0 / 123 -> 121 -> 119 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
