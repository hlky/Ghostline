# base-ma-wat-lch-11

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\community\ma_wat_lch_11_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` | content candidate | 2 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_11/onscreens/ma_wat_lch_11_onscreen_02`
- `points_of_interest/minor_activities/ma_wat_lch_11`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 4 |
| `questInputNodeDefinition` | 2 |
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
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 30 -> 27 -> 26 |
| `07baf99c782e2088a11d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 8 -> 23 -> 19 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 27 -> 26 -> 21 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h28 / 2 -> 3 -> 4 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 0 -> 3 -> 6 |
| `1cc591ffbc44f7f46784` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 1 -> 8 -> 23 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 8 -> 23 -> 16 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 30 -> 29 -> 26 |
| `2f1b46b450c03b60561e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 18 -> 30 -> 29 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 27 -> 26 -> 11 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 28 -> 26 -> 21 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 29 -> 26 -> 21 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 23 -> 19 -> 16 |
| `51570397b2f761f6ba4f` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 23 -> 16 -> 18 |
| `598920ee48558917ab4e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 19 -> 16 -> 18 |
| `6b3e5fe15b7a64a01e21` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 16 -> 18 -> 30 |
| `7616062dec0ebe3473b4` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 30 -> 28 -> 26 |
| `7ab698c317f00ab32676` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 18 -> 30 -> 28 |
| `7b136ed9620da85cbac6` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 27 -> 26 -> 4 |
| `87967374dd117813cccb` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_11\ma_wat_lch_11_phase.questphase` / h0 / 1 -> 0 -> 3 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
