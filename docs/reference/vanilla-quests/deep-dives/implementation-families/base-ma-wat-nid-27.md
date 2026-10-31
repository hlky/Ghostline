# base-ma-wat-nid-27

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\community\ma_wat_nid_27_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_27/onscreens/ma_wat_nid_27_sinked_loot`
- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_27/onscreens/ma_wat_nid_27_van`
- `points_of_interest/minor_activities/ma_wat_nid_27`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_27`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_27/description`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_27/ma_wat_nid_27/find`
- `quests/minor_activities/watson/northside_industrial_district/ma_wat_nid_27/ma_wat_nid_27/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 3 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 34 -> 88 -> 64 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 39 -> 40 -> 101 |
| `08d0cfbab5cb71581bcc` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 40 -> 101 -> 97 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 94 -> 61 -> 95 |
| `0ea39c90296b8c8c526e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 64 -> 70 -> 75 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 37 -> 38 -> 39 |
| `178360ac35259ce804ee` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 28 -> 76 -> 26 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 42 -> 43 -> 36 |
| `1e0dcda3e8879c9b8f32` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 97 -> 98 -> 42 |
| `27aa719598304363c84e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 101 -> 97 -> 98 |
| `2802f18cf340a2b946ff` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 34 -> 88 -> 70 |
| `2ea6dc8eef48b1cfc585` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 88 -> 64 -> 70 |
| `380e05c8b76fbf6ccaf7` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 35 -> 45 -> 37 |
| `4139243029a8673a5ce0` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 28 -> 76 -> 81 |
| `438a2213b6e012878ad4` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 100 -> 98 -> 42 |
| `4e9253a72e6b0134b8dd` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 38 -> 39 -> 40 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 27 -> 30 -> 32 |
| `52e256c57c21a40b4b08` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 81 -> 84 -> 82 |
| `53b397a39cc3f9c63a42` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 98 -> 42 -> 43 |
| `5870e2fba5607932758d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_27\ma_wat_nid_27_phase.questphase` / h0 / 27 -> 34 -> 54 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
