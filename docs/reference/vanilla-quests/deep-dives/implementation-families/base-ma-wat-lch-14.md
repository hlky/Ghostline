# base-ma-wat-lch-14

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\communities\ma_wat_lch_14_com_civilians.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\communities\ma_wat_lch_14_com_enemies.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_def.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` | content candidate | 4 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_shooting.scene` | content candidate | 0 / 3 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_14/onscreens/ma_wat_lch_14`
- `points_of_interest/minor_activities/ma_wat_lch_14`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetReactionPreset,questReactionPresetRecordSelector]` | 12 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 5 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEndNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 4 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 9 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 4 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 20 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 1 |
| `questStartNodeDefinition` | 1 |
| `questTriggerManagerNodeDefinition[questSetTriggerState_NodeType,questSetTriggerState_NodeTypeParams]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |
| `scnEndNode[scnNodeId]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `c3a8b811b8c7c7ee308f` | 8 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 24 -> 16 -> 15 |
| `8d10896873df5c62014e` | 7 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 16 -> 15 -> 13 |
| `56b70500e6cbdf46d4ba` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 19 -> 45 -> 57 |
| `a825401f655e476147b4` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 44 -> 45 -> 57 |
| `e2f4a84af8e0c503880f` | 6 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 37 -> 58 -> 46 |
| `2c20201f171f754c99e0` | 5 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 70 -> 71 -> 72 |
| `3ba86c71a70bfb0620a5` | 5 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 69 -> 70 -> 71 |
| `412a193e89b1d10d2e4a` | 5 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h302 / 0 -> 10 -> 15 |
| `543b598a1b2fb7423e72` | 5 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 67 -> 71 -> 72 |
| `5466f936f30ed8ee354a` | 5 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 66 -> 69 -> 70 |
| `8edf5416ccd8dce9db72` | 5 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 66 -> 67 -> 71 |
| `9cbfb93ce558d1c73900` | 4 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 67 -> 69 -> 70 |
| `dcfede577730a0902ef6` | 4 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 66 -> 67 -> 69 |
| `51d78876d4b7cc3025b7` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 15 -> 13 -> 21 |
| `66e17bf07a534afe17b2` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h130 / 2 -> 3 -> 10 |
| `a3e5f861a4b71433135a` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h130 / 2 -> 3 -> 12 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 8 -> 64 -> 38 |
| `178360ac35259ce804ee` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 0 -> 24 -> 16 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h130 / 2 -> 3 -> 4 |
| `5a1e5eb45e2acdebe80e` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_14\ma_wat_lch_14_quest.questphase` / h0 / 16 -> 15 -> 19 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
