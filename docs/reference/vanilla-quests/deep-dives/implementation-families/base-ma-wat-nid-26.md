# base-ma-wat-nid-26

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\community\ma_wat_nid_26_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_26/onscreens/ma_wat_nid_26_installing`
- `points_of_interest/minor_activities/ma_wat_nid_26`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_26`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_26/description`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_26/ma_wat_nid_26/loot`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_26/ma_wat_nid_26/reach`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 11 -> 67 -> 54 |
| `1972a0532f20a107c8bb` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 0 -> 4 -> 6 |
| `1d48bd7cbbaeca8257d2` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 33 -> 34 -> 27 |
| `05d2345367007644492b` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 66 -> 51 -> 3 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 30 -> 31 -> 79 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 79 -> 76 -> 75 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 73 -> 49 -> 74 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 28 -> 29 -> 30 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 79 -> 78 -> 75 |
| `380e05c8b76fbf6ccaf7` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 12 -> 36 -> 28 |
| `45384fad45d3768a409d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 76 -> 75 -> 33 |
| `4c86e9d12122e122fabf` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 46 -> 53 -> 47 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 29 -> 30 -> 31 |
| `53b397a39cc3f9c63a42` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 75 -> 33 -> 34 |
| `57acaa7093fc730a69e8` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 0 -> 11 -> 67 |
| `624d47eac987aa67b8fb` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 36 -> 28 -> 63 |
| `6b1fcb4c46676ba8a912` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 34 -> 27 -> 43 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 27 -> 43 -> 70 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 79 -> 77 -> 75 |
| `79ff30ab7464b071eda5` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_26\ma_wat_nid_26_phase.questphase` / h0 / 64 -> 65 -> 66 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
