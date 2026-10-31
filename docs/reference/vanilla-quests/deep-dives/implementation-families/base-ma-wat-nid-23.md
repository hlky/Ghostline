# base-ma-wat-nid-23

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\community\ma_wat_nid_23_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_gamedef.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_quest.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/norhside_industrial_district/ma_wat_nid_23/onscreens/ma_wat_nid_23_order`
- `points_of_interest/minor_activities/ma_wat_nid_23`

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
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition,questVehicleCondition,questVehicleSpawned_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
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
| `02338506bda54552def4` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 38 -> 27 -> 3 |
| `04dd53360cd034415986` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 54 -> 62 -> 44 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 51 -> 56 -> 52 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 61 -> 54 -> 62 |
| `27aa719598304363c84e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 66 -> 65 -> 64 |
| `3c6b36e8c01548f18f31` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 42 -> 47 -> 51 |
| `3c72789334e5ea2c94a5` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 38 -> 27 -> 22 |
| `3de2a161e69ddac9948e` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 47 -> 58 -> 61 |
| `4861b1208917398aa185` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 27 -> 22 -> 40 |
| `48ef5781867fbe61b8b0` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 63 -> 64 -> 23 |
| `4bb0ff6439ad8c581aad` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 38 -> 27 -> 66 |
| `5d73a2f49ed5d74832e0` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 42 -> 47 -> 58 |
| `79b539118540b151bff5` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 43 -> 49 -> 2 |
| `8a2391207122dce1edb6` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 27 -> 66 -> 63 |
| `8b11ff41eb479ce97128` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 65 -> 64 -> 23 |
| `8d45062036af4abbb4bc` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 40 -> 41 -> 55 |
| `978a69b98137186c49a7` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_quest.quest` / h0 / 1 -> 0 -> 2 |
| `99c738f69bc472a4bcbf` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 23 -> 25 -> 42 |
| `9af8a87f20a910659fa8` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 25 -> 42 -> 48 |
| `9f3dfa03c86adea5087f` | 1 | `base\open_world\minor_activities\watson\northside\ma_wat_nid_23\ma_wat_nid_23_phase.questphase` / h0 / 64 -> 23 -> 25 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
