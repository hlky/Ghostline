# base-ma-std-arr-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\community\ma_std_arr_08_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_08/onscreens/ma_std_arr_08_onscreen_01`
- `points_of_interest/minor_activities/ma_std_arr_08`

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
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
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
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 21 -> 76 -> 77 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 73 -> 109 -> 107 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 109 -> 106 -> 105 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 64 -> 86 -> 74 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 85 -> 109 -> 107 |
| `163b243e32c0bb8c4eb7` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 75 -> 42 -> 36 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 102 -> 101 -> 96 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 55 -> 85 -> 109 |
| `1e253d0fcbd364975401` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 42 -> 21 -> 76 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 109 -> 108 -> 105 |
| `3457629da944eac3b4b2` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 3 -> 75 -> 42 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 106 -> 105 -> 39 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 105 -> 39 -> 65 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 85 -> 73 -> 109 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 76 -> 30 -> 29 |
| `53e1b61b58de584e4473` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 73 -> 109 -> 108 |
| `60a306c2bf9dcf430a17` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 39 -> 65 -> 56 |
| `628937a52a02aa813665` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 87 -> 103 -> 102 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 57 -> 69 -> 87 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_08\ma_std_arr_08_phase.questphase` / h0 / 109 -> 107 -> 105 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
