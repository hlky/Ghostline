# base-ma-wat-lch-13

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\community\ma_wat_lch_13_civilian_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\community\ma_wat_lch_13_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` | content candidate | 3 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_13/onscreens/ma_wat_lch_13_2`
- `points_of_interest/minor_activities/ma_wat_lch_13`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 1 |
| `questEventManagerNodeDefinition` | 3 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 6 |
| `questFlowControlNodeDefinition` | 1 |
| `questInputNodeDefinition` | 3 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalXorNodeDefinition` | 1 |
| `questMovePuppetNodeDefinition[questMoveToParams,questUniversalRef]` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questDistanceComparison_ConditionType,questDistanceCondition,questLogicalCondition,questObjectDistance,questSystemCondition,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questSystemCondition]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 5 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 6 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 2 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 5 |
| `questPhaseNodeDefinition` | 3 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 15 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 1 |
| `questVoicesetManagerNodeDefinition[questPlayVoiceset_NodeType,questPlayVoiceset_NodeTypeParams]` | 2 |
| `questWorldDataManagerNodeDefinition[questShowWorldNode_NodeType]` | 1 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 3 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `8d10896873df5c62014e` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 0 -> 46 -> 3 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 21 -> 85 -> 41 |
| `178360ac35259ce804ee` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 2 -> 25 -> 0 |
| `18be198845c90c6bb3c8` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h39 / 3 -> 2 -> 4 |
| `2c20201f171f754c99e0` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 91 -> 92 -> 93 |
| `3a201d4eb25e2fb243d0` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 25 -> 52 -> 68 |
| `3ba86c71a70bfb0620a5` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 90 -> 91 -> 92 |
| `543b598a1b2fb7423e72` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 88 -> 92 -> 93 |
| `5466f936f30ed8ee354a` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 87 -> 90 -> 91 |
| `63a3dcfee8c06f13773f` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 72 -> 79 -> 66 |
| `7792fc609dd5a002b7c5` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 56 -> 62 -> 64 |
| `8edf5416ccd8dce9db72` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 87 -> 88 -> 92 |
| `9cbfb93ce558d1c73900` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 88 -> 90 -> 91 |
| `9d63edbfbbd887796b2f` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 68 -> 72 -> 79 |
| `abd13316e0bc0a0da497` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 52 -> 68 -> 72 |
| `c3a8b811b8c7c7ee308f` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 25 -> 0 -> 46 |
| `d1c570f171b188dccaf2` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h39 / 2 -> 6 -> 11 |
| `dcfede577730a0902ef6` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 87 -> 88 -> 90 |
| `02a5265bcccfc8e3cf77` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h39 / 3 -> 2 -> 7 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_13\ma_wat_lch_13_phase.questphase` / h0 / 136 -> 133 -> 132 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
