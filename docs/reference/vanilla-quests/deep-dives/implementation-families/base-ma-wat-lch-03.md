# base-ma-wat-lch-03

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\community\ma_wat_lch_03_civ_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\community\ma_wat_lch_03_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\community\ma_wat_lch_03_corpo_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_03/onscreens/ma_wat_lch_03_gps`
- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_03/onscreens/ma_wat_lch_03_urn`
- `points_of_interest/minor_activities/ma_wat_lch_03`
- `quests/minor_activities/watson/little_china/ma_wat_lch_03`
- `quests/minor_activities/watson/little_china/ma_wat_lch_03/description`
- `quests/minor_activities/watson/little_china/ma_wat_lch_03/ma_wat_lch_03/go_to_spot`
- `quests/minor_activities/watson/little_china/ma_wat_lch_03/ma_wat_lch_03/loot`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 9 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questSetItemTags_NodeType,questSetItemTags_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalQuestEntry_NodeType]` | 6 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntryState_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 4 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 10 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 8 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c7feb866b8271d2bea9e` | 4 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h214 / 4 -> 20 -> 7 |
| `12933bc7add8cc0324cd` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h214 / 4 -> 20 -> 9 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 14 -> 105 -> 71 |
| `8b7c7b83f17e24f841e8` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 93 -> 91 -> 28 |
| `0781ef00ea04c05ee418` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 22 -> 23 -> 112 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 112 -> 109 -> 108 |
| `08fabdc4110dabc6ef30` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 17 -> 50 -> 100 |
| `1094980783b061bb3393` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 101 -> 102 -> 93 |
| `138cff49923a75e07348` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 17 -> 21 -> 22 |
| `13e54cc7d319bbafaa58` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 39 -> 41 -> 79 |
| `1666d7526b9bab74f2e2` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 20 -> 17 -> 50 |
| `178ff9eba50354aed786` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 2 -> 104 -> 103 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 28 -> 30 -> 31 |
| `1a3d0ec08c9c011c8d4e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 93 -> 91 -> 0 |
| `1d48bd7cbbaeca8257d2` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 24 -> 26 -> 38 |
| `215ca95d939006973a7d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 38 -> 40 -> 3 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 14 -> 105 -> 39 |
| `25aae51001db85d5b1fb` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 104 -> 103 -> 101 |
| `2994474f402dacd934b6` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 41 -> 79 -> 77 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_03\ma_wat_lch_03_phase.questphase` / h0 / 112 -> 111 -> 108 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
