# base-ma-wat-lch-04

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\community\ma_wat_lch_04_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_04/onscreens/ma_wat_lch_04_1`
- `points_of_interest/minor_activities/ma_wat_lch_04`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questPhaseNodeDefinition[questQuestPrefabEntry]` | 1 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 9 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `18be198845c90c6bb3c8` | 4 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h41 / 3 -> 2 -> 5 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 21 -> 44 -> 42 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h41 / 3 -> 2 -> 7 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 50 -> 47 -> 46 |
| `1258cee37e98f0ae14fe` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 28 -> 34 -> 43 |
| `178360ac35259ce804ee` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 1 -> 25 -> 0 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 0 -> 3 -> 16 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 1 -> 21 -> 44 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 21 -> 44 -> 33 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 50 -> 49 -> 46 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 37 -> 50 -> 49 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 47 -> 46 -> 24 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 44 -> 42 -> 33 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 44 -> 33 -> 37 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 42 -> 33 -> 37 |
| `66e17bf07a534afe17b2` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h41 / 3 -> 2 -> 15 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 33 -> 37 -> 50 |
| `6d25f58b6956954efcb3` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h41 / 3 -> 2 -> 14 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 50 -> 48 -> 46 |
| `7ab698c317f00ab32676` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_04\ma_wat_lch_04_phase.questphase` / h0 / 37 -> 50 -> 48 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
