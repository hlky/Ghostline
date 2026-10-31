# base-ma-wat-nid-08

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\community\ma_wat_nid_08_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_gamedef.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` | content candidate | 1 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_08/onscreens/ma_wat_nid_08_carriage`
- `points_of_interest/minor_activities/ma_wat_nid_08`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMiscAICommandNode` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition,questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `02d878a28a675e881f96` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 68 -> 66 -> 25 |
| `45a0059a97ab5b10fb49` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 67 -> 66 -> 25 |
| `9607ff9432ed294370d1` | 3 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 69 -> 66 -> 25 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 23 -> 57 -> 49 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 70 -> 67 -> 66 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 67 -> 66 -> 51 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 64 -> 52 -> 65 |
| `1121a7f146103492ac60` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 68 -> 66 -> 33 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 66 -> 51 -> 59 |
| `19410088a9f25d58e67e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 65 -> 41 -> 42 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 23 -> 57 -> 31 |
| `255c3064dfbb8efcc440` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 54 -> 42 -> 2 |
| `2a57d66dd4c6f099e6da` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 66 -> 48 -> 63 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 70 -> 69 -> 66 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 30 -> 70 -> 69 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 67 -> 66 -> 24 |
| `354e0603fdbd00ceb27b` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 66 -> 61 -> 64 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 68 -> 66 -> 51 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 69 -> 66 -> 51 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_08\ma_wat_nid_08_phase.questphase` / h0 / 57 -> 49 -> 31 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
