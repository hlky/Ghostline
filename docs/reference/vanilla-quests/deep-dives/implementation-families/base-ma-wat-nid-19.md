# base-ma-wat-nid-19

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\community\ma_wat_nid_19_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_19/onscreens/ma_wat_nid_19_aldecaldo`
- `points_of_interest/minor_activities/ma_wat_nid_19`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
| `questInputNodeDefinition` | 2 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 51 -> 48 -> 47 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 37 -> 39 -> 36 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 45 -> 28 -> 46 |
| `1489a2df8e7f98f9c78e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 16 -> 1 -> 51 |
| `1495b1d75b7c2987dca3` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 24 -> 30 -> 33 |
| `1a71073485eb34656e41` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 30 -> 33 -> 3 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 51 -> 50 -> 47 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 48 -> 47 -> 12 |
| `3750bdcc2a4bda83d074` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 1 -> 51 -> 50 |
| `3a7f8b9c6d709ceceae1` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 1 -> 51 -> 48 |
| `3c6b36e8c01548f18f31` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 22 -> 26 -> 37 |
| `3de2a161e69ddac9948e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 26 -> 41 -> 45 |
| `51d78876d4b7cc3025b7` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 1 -> 4 -> 6 |
| `5870e2fba5607932758d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 1 -> 11 -> 21 |
| `5d73a2f49ed5d74832e0` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 22 -> 26 -> 41 |
| `75a31805d3e2f9c96e96` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 46 -> 29 -> 24 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 51 -> 49 -> 47 |
| `8d10896873df5c62014e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 16 -> 1 -> 4 |
| `8d45062036af4abbb4bc` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 21 -> 23 -> 38 |
| `8e8dd8bd90cfe26838bf` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_19\ma_wat_nid_19_phase.questphase` / h0 / 34 -> 30 -> 33 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
