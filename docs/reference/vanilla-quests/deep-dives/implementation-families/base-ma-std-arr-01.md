# base-ma-std-arr-01

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\community\ma_std_arr_01_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_01/onscreens/ma_std_arr_01_onscreen_01`
- `points_of_interest/minor_activities/ma_std_arr_01`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 1 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 21 -> 84 -> 43 |
| `6a23964fa82096d43a98` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 35 -> 74 -> 72 |
| `6b3e5fe15b7a64a01e21` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 42 -> 30 -> 101 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 101 -> 98 -> 97 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 94 -> 92 -> 89 |
| `1e253d0fcbd364975401` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 27 -> 3 -> 35 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 21 -> 84 -> 42 |
| `2465cabc5e4b65280bdb` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 27 -> 21 -> 84 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 101 -> 100 -> 97 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 30 -> 101 -> 100 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 98 -> 97 -> 24 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 97 -> 24 -> 33 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 84 -> 43 -> 42 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 84 -> 42 -> 30 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 43 -> 42 -> 30 |
| `60a306c2bf9dcf430a17` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 24 -> 33 -> 28 |
| `628937a52a02aa813665` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 87 -> 96 -> 94 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 101 -> 99 -> 97 |
| `79f4dddf5c52f6df598a` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 33 -> 28 -> 41 |
| `7ab698c317f00ab32676` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_01\ma_std_arr_01_phase.questphase` / h0 / 30 -> 101 -> 99 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
