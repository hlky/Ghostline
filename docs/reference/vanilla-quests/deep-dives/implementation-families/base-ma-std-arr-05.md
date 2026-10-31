# base-ma-std-arr-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\community\ma_std_arr_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\community\ma_std_arr_05_com_civilians.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/arroyo/ma_std_arr_05/onscreens/ma_std_arr_05_onscreen_01`
- `points_of_interest/minor_activities/ma_std_arr_05`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 2 |
| `questMovePuppetNodeDefinition[questMoveOnSplineAdditionalParams,questMoveOnSplineParams,questSimpleMoveOnSplineParams,questUniversalRef]` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam,questLogicalCondition,questSystemCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterReaction_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 12 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `344a9bb49243e19907c3` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h261 / 2 -> 3 -> 5 |
| `85906da2771a6b983624` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h261 / 3 -> 4 -> 6 |
| `86598e02c77b18e76df0` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h261 / 0 -> 2 -> 3 |
| `da9eef19f71edc11a219` | 4 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h261 / 2 -> 3 -> 4 |
| `ef828624d48b06bf49f2` | 3 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 43 -> 111 -> 48 |
| `fd6abc96d7197725e3e8` | 3 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 64 -> 43 -> 111 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 54 -> 131 -> 116 |
| `6b3e5fe15b7a64a01e21` | 2 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 103 -> 115 -> 153 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 153 -> 150 -> 149 |
| `0c5acabadd2c6d7f6dd6` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 54 -> 137 -> 128 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 147 -> 142 -> 144 |
| `27989a991fbce5b0fc5c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 112 -> 60 -> 109 |
| `2c19d1e1f9a33740cedb` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 43 -> 46 -> 134 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 153 -> 152 -> 149 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 115 -> 153 -> 152 |
| `3473788fa2e021211ee9` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 122 -> 130 -> 120 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 150 -> 149 -> 57 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 149 -> 57 -> 97 |
| `5275557c8b38e629c6aa` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 53 -> 54 -> 131 |
| `60a306c2bf9dcf430a17` | 1 | `base\open_world\minor_activities\santo_domingo\arroyo\ma_std_arr_05\ma_std_arr_05_phase.questphase` / h0 / 57 -> 97 -> 92 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
