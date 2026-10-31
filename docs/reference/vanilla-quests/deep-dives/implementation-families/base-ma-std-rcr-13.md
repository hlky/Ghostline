# base-ma-std-rcr-13

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\community\ma_std_rcr_13.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\community\ma_std_rcr_13_stash.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_13/onscreens/ma_std_rcr_13_onscreen_02`
- `points_of_interest/minor_activities/ma_std_rcr_13`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_13`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_13/description`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_13/ma_std_rcr_13/loot_stash`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_13/ma_std_rcr_13/reach_stash`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questStartNodeDefinition` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `02a5265bcccfc8e3cf77` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h42 / 14 -> 12 -> 5 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h42 / 14 -> 12 -> 4 |
| `1d48bd7cbbaeca8257d2` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 32 -> 33 -> 40 |
| `51d78876d4b7cc3025b7` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 5 -> 6 -> 8 |
| `66e17bf07a534afe17b2` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h42 / 14 -> 12 -> 6 |
| `71892f49b88f7b8bb8be` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 0 -> 11 -> 39 |
| `a3e5f861a4b71433135a` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h42 / 14 -> 12 -> 10 |
| `05fe886b74a86bbaffdc` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 10 -> 82 -> 85 |
| `063c0e3538b36ad0971b` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 0 -> 11 -> 10 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 29 -> 30 -> 112 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 112 -> 109 -> 108 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 11 -> 106 -> 101 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 27 -> 28 -> 29 |
| `177509bec033f4e05c92` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 11 -> 10 -> 82 |
| `178ff9eba50354aed786` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 0 -> 4 -> 104 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 0 -> 11 -> 106 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 112 -> 111 -> 108 |
| `380e05c8b76fbf6ccaf7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 13 -> 34 -> 35 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 109 -> 108 -> 32 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_13\ma_std_rcr_13.questphase` / h0 / 28 -> 29 -> 30 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
