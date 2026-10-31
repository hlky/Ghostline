# base-ma-std-rcr-10

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\community\ma_std_rcr_10_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\community\ma_std_rcr_10_com_a.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase |
| `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_10/onscreens/ma_std_rcr_10_onscreen_01`
- `points_of_interest/minor_activities/ma_std_rcr_10`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_10`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_10/ma_description`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_10/ma_std_rcr_10`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_10/ma_std_rcr_10/loot_stash`
- `quests/minor_activities/santo_domingo/rancho_coronado/ma_std_rcr_10/ma_std_rcr_10/reach_stash`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 7 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 2 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 6 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `05e6009c4d1d8f802e1d` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 100 -> 62 -> 93 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h55 / 11 -> 8 -> 2 |
| `380e05c8b76fbf6ccaf7` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 65 -> 73 -> 66 |
| `5506424829d3f5f3a244` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 54 -> 63 -> 76 |
| `7f8d627a8ef91ec53563` | 2 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 90 -> 62 -> 93 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h55 / 11 -> 8 -> 5 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 58 -> 60 -> 96 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 68 -> 69 -> 110 |
| `0d59d5b737ce1451c32f` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 112 -> 107 -> 106 |
| `0ea39c90296b8c8c526e` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 90 -> 62 -> 92 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 66 -> 67 -> 68 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 71 -> 72 -> 77 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 110 -> 109 -> 106 |
| `2ea6dc8eef48b1cfc585` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 100 -> 90 -> 62 |
| `382a6bbc3bd5c2ab4724` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 62 -> 80 -> 81 |
| `3b46faf54cc41c30b40e` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 90 -> 62 -> 56 |
| `414179f27318cfb189d5` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 63 -> 100 -> 90 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 107 -> 106 -> 71 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 67 -> 68 -> 69 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\santo_domingo\rancho_coronado\ma_std_rcr_10\ma_std_rcr_10_phase.questphase` / h0 / 57 -> 58 -> 60 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
