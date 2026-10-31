# base-ma-std-rcr-05

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\community\ma_std_rcr_05_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\community\ma_std_rcr_05_sixthstreet_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` | content candidate | 3 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\phases\ma_std_rcr_05_bugfixing.questphase` | repair | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_05/onscreens/ma_std_rcr_05_onscreen_02`
- `points_of_interest/minor_activities/ma_std_rcr_05`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 6 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 6 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 4 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 8 |
| `questInputNodeDefinition` | 6 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 4 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `a5424d4efba0ea84c008` | 6 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h217 / 0 -> 15 -> 11 |
| `02692ae3a7624f2dd47d` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h217 / 9 -> 10 -> 6 |
| `51d78876d4b7cc3025b7` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 1 -> 2 -> 3 |
| `5506424829d3f5f3a244` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 5 -> 10 -> 21 |
| `66e17bf07a534afe17b2` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h40 / 17 -> 15 -> 12 |
| `8d10896873df5c62014e` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 0 -> 1 -> 2 |
| `a3482bab3b385654b21b` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h217 / 5 -> 10 -> 6 |
| `e5d5e990d5eaa92d5551` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h217 / 8 -> 10 -> 6 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 29 -> 42 -> 40 |
| `022b4f9462189fe7c3e1` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h217 / 0 -> 5 -> 10 |
| `02d878a28a675e881f96` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 40 -> 38 -> 22 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 42 -> 39 -> 38 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 35 -> 42 -> 40 |
| `178360ac35259ce804ee` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 5 -> 15 -> 0 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h40 / 17 -> 15 -> 11 |
| `1ae94ee872986dd79c0d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\phases\ma_std_rcr_05_bugfixing.questphase` / h7 / 0 -> 3 -> 2 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 42 -> 41 -> 38 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 39 -> 38 -> 12 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 38 -> 12 -> 19 |
| `4139243029a8673a5ce0` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_05\ma_std_rcr_05_phase.questphase` / h0 / 5 -> 15 -> 34 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
