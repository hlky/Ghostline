# base-ma-std-arr-12

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\community\ma_std_arr_12_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_12/onscreens/ma_std_arr_12_onscreen_01`
- `points_of_interest/minor_activities/ma_std_arr_12`

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
| `questMiscAICommandNode` | 3 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUIManagerNodeDefinition[questSwitchNameplate_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 5 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1e253d0fcbd364975401` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 51 -> 37 -> 61 |
| `95b7458b3ffd83fd4357` | 3 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 37 -> 69 -> 70 |
| `bee1f62dab6be5337bda` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 95 -> 96 -> 97 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 64 -> 109 -> 106 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 109 -> 105 -> 104 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 88 -> 91 -> 65 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 90 -> 109 -> 106 |
| `163b243e32c0bb8c4eb7` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 66 -> 51 -> 45 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 102 -> 95 -> 96 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 55 -> 90 -> 109 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 109 -> 108 -> 104 |
| `3457629da944eac3b4b2` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 2 -> 66 -> 51 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 105 -> 104 -> 48 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 104 -> 48 -> 58 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 90 -> 64 -> 109 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 64 -> 109 -> 108 |
| `60a306c2bf9dcf430a17` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 48 -> 58 -> 57 |
| `628937a52a02aa813665` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 92 -> 103 -> 102 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 56 -> 59 -> 92 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_12\ma_std_arr_12_phase.questphase` / h0 / 109 -> 106 -> 104 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
