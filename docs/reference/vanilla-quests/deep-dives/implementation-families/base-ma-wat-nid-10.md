# base-ma-wat-nid-10

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\community\ma_wat_nid_10_02.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\community\ma_wat_nid_10_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_10/onscreens/ma_wat_nid_10_help`
- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_10/onscreens/ma_wat_nid_10_ride`
- `points_of_interest/minor_activities/ma_wat_nid_10`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_10`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_10/description`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_10/ma_wat_nid_10/ma_wat_nid_10_blood`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_10/ma_wat_nid_10/ma_wat_nid_10_find`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_10/ma_wat_nid_10/ma_wat_nid_10_loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 6 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 9 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 9 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `6b2e106d948263959099` | 4 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 130 -> 126 -> 22 |
| `bfe95df47bd1ca67330f` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 137 -> 139 -> 138 |
| `0781ef00ea04c05ee418` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 116 -> 117 -> 122 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 11 -> 103 -> 70 |
| `6a23964fa82096d43a98` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 86 -> 91 -> 92 |
| `808c42396a9735fe3a65` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 2 -> 14 -> 16 |
| `8d10896873df5c62014e` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 0 -> 86 -> 3 |
| `bff957bf33a10413a685` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 14 -> 16 -> 19 |
| `f3a269b6a97862bc211c` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 0 -> 86 -> 91 |
| `f9b50df9bd909f351b48` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 126 -> 119 -> 22 |
| `056f65b5401e52f37bc4` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 2 -> 0 -> 137 |
| `05e6009c4d1d8f802e1d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 103 -> 76 -> 102 |
| `08d0cfbab5cb71581bcc` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 25 -> 136 -> 131 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 109 -> 47 -> 110 |
| `0ea39c90296b8c8c526e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 70 -> 76 -> 95 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 22 -> 23 -> 24 |
| `1a9b8893087e174a603f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 118 -> 111 -> 119 |
| `1dc89cfc6ae4d329b522` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 28 -> 73 -> 104 |
| `221bcac503ab6c794bee` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 126 -> 22 -> 23 |
| `235ed1f97cea566186b0` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_10\ma_wat_nid_10_phase.questphase` / h0 / 111 -> 119 -> 22 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
