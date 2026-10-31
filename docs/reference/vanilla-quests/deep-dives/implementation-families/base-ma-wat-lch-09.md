# base-ma-wat-lch-09

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\community\ma_wat_lch_09_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_09/onscreens/ma_wat_lch_09`
- `points_of_interest/minor_activities/ma_wat_lch_09`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 20 -> 50 -> 43 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h102 / 2 -> 3 -> 8 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 56 -> 53 -> 52 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 53 -> 52 -> 49 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 52 -> 49 -> 51 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h102 / 2 -> 3 -> 4 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 0 -> 20 -> 50 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 20 -> 50 -> 38 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 56 -> 55 -> 52 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 39 -> 56 -> 55 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 53 -> 52 -> 24 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 54 -> 52 -> 49 |
| `3defb6b5bfe82560078d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 0 -> 27 -> 25 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 55 -> 52 -> 49 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 50 -> 43 -> 38 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 50 -> 38 -> 39 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 43 -> 38 -> 39 |
| `66e17bf07a534afe17b2` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h102 / 2 -> 3 -> 6 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 38 -> 39 -> 56 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_09\ma_wat_lch_09_phase.questphase` / h0 / 56 -> 54 -> 52 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
