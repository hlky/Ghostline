# base-ma-pac-cvi-11

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\community\ma_pac_cvi_11_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` | content candidate | 2 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_sasquatch.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_sasquatch.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/pacifica/coastview/ma_pac_cvi_11/shards/ma_pac_cvi_11`
- `points_of_interest/minor_activities/ma_pac_cvi_11`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEndNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 13 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 7 |
| `questInputNodeDefinition` | 4 |
| `questInteractiveObjectManagerNodeDefinition[questDeviceManager_NodeType,questDeviceManager_NodeTypeParams]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 8 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 2 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c92f06f761368a14f455` | 6 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 2 -> 12 -> 5 |
| `d30dec206567a53c3ede` | 5 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 12 -> 41 -> 42 |
| `ae26d9b3c8043dedb4cc` | 3 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 41 -> 42 -> 45 |
| `0015f21cac33b67104ef` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 38 -> 87 -> 85 |
| `057faf6705431d5dcd46` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 71 -> 72 -> 76 |
| `07a508d9181a1ec44ac6` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_sasquatch.quest` / h0 / 3 -> 4 -> 0 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 87 -> 84 -> 83 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 39 -> 80 -> 40 |
| `114d46d19e809cb7d96b` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 79 -> 87 -> 85 |
| `1ae543dce830cc09ee94` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 55 -> 54 -> 57 |
| `1c8f5db5f76df3ad5f7c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 36 -> 79 -> 87 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 87 -> 86 -> 83 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 84 -> 83 -> 10 |
| `3a3d4ff2ceb6dad82b8e` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_sasquatch.quest` / h0 / 2 -> 3 -> 4 |
| `3a7b7bf9b511613ae356` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 0 -> 55 -> 54 |
| `403d794f01acf7d4e8ce` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 83 -> 10 -> 30 |
| `4365e94e7169e2520841` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 84 -> 83 -> 1 |
| `4516ea8d7bcf8c04ba50` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 85 -> 83 -> 1 |
| `48b34908ac4ded0af324` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 86 -> 83 -> 1 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\pacifica\coastview\ma_pac_cvi_11\ma_pac_cvi_11_phase.questphase` / h0 / 79 -> 38 -> 87 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
