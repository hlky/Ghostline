# base-ma-std-arr-11

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\community\ma_std_arr_11_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\phases\ma_std_arr_11_bugfixing.questphase` | repair | 4 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_11/onscreens/ma_std_arr_11_onscreen_01`
- `points_of_interest/minor_activities/ma_std_arr_11`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 6 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 8 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 10 |
| `questInputNodeDefinition` | 5 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 3 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 4 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questChangeVoicesetState_NodeType,questChangeVoicesetState_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1e253d0fcbd364975401` | 5 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 36 -> 21 -> 45 |
| `2b12bdfb83488bf5498e` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\phases\ma_std_arr_11_bugfixing.questphase` / h56 / 2 -> 9 -> 8 |
| `95b7458b3ffd83fd4357` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 21 -> 51 -> 50 |
| `a103d4ae3150ecfeb747` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\phases\ma_std_arr_11_bugfixing.questphase` / h56 / 6 -> 2 -> 9 |
| `a514220192c3b5f59537` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 36 -> 21 -> 57 |
| `eaf5aab427d50e5598b6` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\phases\ma_std_arr_11_bugfixing.questphase` / h56 / 0 -> 6 -> 2 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 47 -> 78 -> 76 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 78 -> 75 -> 74 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 64 -> 71 -> 48 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 70 -> 78 -> 76 |
| `163b243e32c0bb8c4eb7` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 49 -> 36 -> 29 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 86 -> 80 -> 81 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 40 -> 70 -> 78 |
| `237687944a84dd96b7b5` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\phases\ma_std_arr_11_bugfixing.questphase` / h114 / 0 -> 9 -> 13 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 78 -> 77 -> 74 |
| `31c826ade07a86b9edf1` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\phases\ma_std_arr_11_bugfixing.questphase` / h7 / 8 -> 2 -> 3 |
| `3457629da944eac3b4b2` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 2 -> 49 -> 36 |
| `3473788fa2e021211ee9` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 69 -> 68 -> 53 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 75 -> 74 -> 32 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_11\ma_std_arr_11_phase.questphase` / h0 / 74 -> 32 -> 42 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
