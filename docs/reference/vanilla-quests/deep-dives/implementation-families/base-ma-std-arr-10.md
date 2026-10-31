# base-ma-std-arr-10

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\community\ma_std_arr_10_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_10/onscreens/ma_std_arr_10_onscreen_02`
- `points_of_interest/minor_activities/ma_std_arr_10`

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
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 66 -> 101 -> 107 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 101 -> 106 -> 105 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 79 -> 85 -> 67 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 84 -> 101 -> 107 |
| `1236b824035f3d3d10f6` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 91 -> 92 -> 93 |
| `163b243e32c0bb8c4eb7` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 68 -> 36 -> 18 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 95 -> 90 -> 91 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 46 -> 84 -> 101 |
| `1e253d0fcbd364975401` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 36 -> 11 -> 73 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 101 -> 100 -> 105 |
| `3457629da944eac3b4b2` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 0 -> 68 -> 36 |
| `3473788fa2e021211ee9` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 81 -> 82 -> 70 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 106 -> 105 -> 22 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 105 -> 22 -> 44 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 84 -> 66 -> 101 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 73 -> 13 -> 12 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 66 -> 101 -> 100 |
| `60a306c2bf9dcf430a17` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 22 -> 44 -> 50 |
| `628937a52a02aa813665` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 86 -> 96 -> 95 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_10\ma_std_arr_10_phase.questphase` / h0 / 47 -> 48 -> 86 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
