# base-ma-wat-nid-13

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\community\ma_wat_nid_13_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_13/onscreens/ma_wat_nid_13_delivery`
- `points_of_interest/minor_activities/ma_wat_nid_13`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition,questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 10 -> 37 -> 30 |
| `e7e76532ca5105db2460` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 19 -> 44 -> 24 |
| `02338506bda54552def4` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 0 -> 1 -> 4 |
| `04dd53360cd034415986` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 19 -> 44 -> 23 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 4 -> 6 -> 34 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 49 -> 46 -> 45 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 46 -> 45 -> 32 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 43 -> 19 -> 44 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 45 -> 32 -> 38 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 10 -> 37 -> 15 |
| `24bdc2839a62528ae410` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 44 -> 23 -> 25 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 49 -> 48 -> 45 |
| `33af1be61138ebf59a50` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 33 -> 25 -> 36 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 46 -> 45 -> 11 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 47 -> 45 -> 32 |
| `3c72789334e5ea2c94a5` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 0 -> 1 -> 10 |
| `3de2a161e69ddac9948e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 21 -> 40 -> 43 |
| `3fa1208cc0da990e02e2` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 25 -> 36 -> 3 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 48 -> 45 -> 32 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_13\ma_wat_nid_13.questphase` / h0 / 37 -> 30 -> 15 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
