# base-ma-wat-lch-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\community\ma_wat_lch_02_after_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\community\ma_wat_lch_02_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\ma_wat_lch_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\ma_wat_lch_02.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\ma_wat_lch_02_phase.questphase` | content candidate | 1 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_02/onscreens/ma_wat_lch_02_03`
- `points_of_interest/minor_activities/ma_wat_lch_02`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 5 |
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
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 3 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `1972a0532f20a107c8bb` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 14 -> 17 -> 30 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 37 -> 65 -> 60 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h40 / 3 -> 2 -> 5 |
| `66e17bf07a534afe17b2` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h40 / 3 -> 2 -> 15 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h40 / 3 -> 2 -> 10 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 71 -> 68 -> 67 |
| `0c8f031f372a34b54a46` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h40 / 3 -> 2 -> 16 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 15 -> 37 -> 65 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 37 -> 65 -> 52 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 71 -> 70 -> 67 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 54 -> 71 -> 70 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 68 -> 67 -> 40 |
| `3c6b36e8c01548f18f31` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 53 -> 45 -> 62 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 65 -> 60 -> 52 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 65 -> 52 -> 54 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 60 -> 52 -> 54 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 52 -> 54 -> 71 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 71 -> 69 -> 67 |
| `7ab698c317f00ab32676` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 54 -> 71 -> 69 |
| `7b136ed9620da85cbac6` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_02\phases\ma_wat_lch_02.questphase` / h0 / 68 -> 67 -> 18 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
