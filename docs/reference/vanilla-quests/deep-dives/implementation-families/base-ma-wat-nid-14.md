# base-ma-wat-nid-14

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\community\ma_wat_nid_14_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_14/onscreens/ma_wat_nid_14_cop`
- `points_of_interest/minor_activities/ma_wat_nid_14`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 4 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 5 |
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
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c33c9bf9bd58ebcdebf9` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 0 -> 4 -> 19 |
| `e7e76532ca5105db2460` | 2 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 28 -> 51 -> 29 |
| `02338506bda54552def4` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 0 -> 4 -> 2 |
| `04dd53360cd034415986` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 28 -> 51 -> 30 |
| `06e3382349ceff89de6f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 2 -> 5 -> 43 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 56 -> 53 -> 52 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 37 -> 45 -> 36 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 50 -> 28 -> 51 |
| `1ecc1e1f4c4151a3aba0` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 37 -> 45 -> 47 |
| `24bdc2839a62528ae410` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 51 -> 30 -> 31 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 56 -> 55 -> 52 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 53 -> 52 -> 10 |
| `36dddd8add8366cb2443` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 45 -> 47 -> 50 |
| `3c6b36e8c01548f18f31` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 25 -> 26 -> 37 |
| `3c72789334e5ea2c94a5` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 0 -> 4 -> 9 |
| `4861b1208917398aa185` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 4 -> 9 -> 23 |
| `4bb0ff6439ad8c581aad` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 0 -> 4 -> 56 |
| `4e534a24897f81ddee0f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 45 -> 36 -> 47 |
| `6a5da6b827984be4e01a` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 31 -> 34 -> 41 |
| `6af41bd22f4419647524` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_14\ma_wat_nid_14.questphase` / h0 / 51 -> 29 -> 31 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
