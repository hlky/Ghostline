# base-ma-wat-lch-12

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\community\ma_wat_lch_12_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\community\ma_wat_lch_12_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_12/onscreens/ma_wat_lch_12_3`
- `points_of_interest/minor_activities/ma_wat_lch_12`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 2 |
| `questLogicalXorNodeDefinition` | 1 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 8 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 2 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 6 -> 64 -> 49 |
| `6359f1951cb4cbc69ff1` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 0 -> 20 -> 55 |
| `e735e23a5cafaa15e972` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h29 / 5 -> 8 -> 2 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 104 -> 101 -> 100 |
| `0985fc78e580f2f10e14` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h252 / 41 -> 48 -> 47 |
| `0b988ceccf7fcaa3e0e3` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 101 -> 100 -> 51 |
| `15703191a3189e1fd363` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 100 -> 51 -> 65 |
| `1972a0532f20a107c8bb` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 10 -> 2 -> 4 |
| `20e74db83226e46cc202` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 61 -> 63 -> 59 |
| `224ed87e425e330e5d2e` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 20 -> 56 -> 57 |
| `23c83f846beb25d06b1d` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 58 -> 61 -> 63 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 6 -> 64 -> 47 |
| `2465cabc5e4b65280bdb` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 53 -> 6 -> 64 |
| `2cc4f20e16798419f013` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 48 -> 7 -> 104 |
| `2e0e3e918dc6fad6b34c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 104 -> 103 -> 100 |
| `3484262e69bedc0c60ba` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 101 -> 100 -> 9 |
| `3b9c02e635e0f649e86a` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 102 -> 100 -> 51 |
| `423e38da0596af6a3004` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h252 / 48 -> 47 -> 45 |
| `429813b3b7383ae126db` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 103 -> 100 -> 51 |
| `4a1ea25221f47a7c1e8c` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_12\ma_wat_lch_12_phase.questphase` / h0 / 64 -> 49 -> 47 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
