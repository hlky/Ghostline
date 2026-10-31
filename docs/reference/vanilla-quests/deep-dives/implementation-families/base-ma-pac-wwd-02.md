# base-ma-pac-wwd-02

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\community\ma_pac_wwd_02_scavs_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\community\ma_pac_wwd_02_wraiths_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02.quest` | content candidate | 2 / 0 | base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase; base\quest\holocalls\holocall_initializers.questphase |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` | content candidate | 1 / 0 | base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\scene\ma_pac_wwd_02_holocall_brief.scene |
| `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\scene\ma_pac_wwd_02_holocall_brief.scene` | content candidate | 0 / 15 |  |

## Journal paths observed in these resources

- `contacts/ncpd_dispatcher/outposts/ma_pac_wwd_02`
- `points_of_interest/minor_activities/ma_pac_wwd_02`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAchievementManagerNodeDefinition[questSetProgress_NodeType]` | 1 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 2 |
| `questConditionNodeDefinition[questPhoneMuted_ConditionType,questSystemCondition]` | 1 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 1 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 2 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 13 |
| `questInputNodeDefinition` | 2 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questJournalNodeDefinition[questJournalEntry_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 2 |
| `questMiscAICommandNode` | 2 |
| `questOutputNodeDefinition` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterState_ConditionType,questCharacterState_PlayerSubType,questContentCondition,questContentLock_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questSceneCondition,questSceneNode_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 3 |
| `questPhaseNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 5 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 5 |
| `scnEndNode[scnNodeId]` | 2 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleInterruption_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnInterruptManagerNode[scnInterruptionScenarioId,scnNodeId,scnOverrideInterruptionScenario_InterruptionOperation,scnToggleScenario_InterruptionScenarioOperation]` | 1 |
| `scnSectionNode[scnActorId,scnNodeId,scnSceneTime,scnSectionInternalsActorBehavior]` | 1 |
| `scnStartNode[scnNodeId]` | 1 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `a5f6ff0df46f7043f2b5` | 3 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 35 -> 25 -> 33 |
| `e5742f9794e6583c67cb` | 3 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\scene\ma_pac_wwd_02_holocall_brief.scene` / scene / 64 -> 258 -> 256 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 3 -> 81 -> 64 |
| `22725fd3b57fe8a30b1b` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 8 -> 10 -> 45 |
| `2e1ee5a1324dbeeb9071` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 6 -> 7 -> 8 |
| `3560b3719769da7fd9fe` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 14 -> 6 -> 7 |
| `454f6e0a4529eda7557b` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 9 -> 10 -> 45 |
| `47cc5074c53050699ba3` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 45 -> 46 -> 41 |
| `6824f5988760343a451a` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 8 -> 10 -> 38 |
| `721dd253f632c98c4268` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 76 -> 46 -> 41 |
| `875db287de4c4f2dc8dd` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 9 -> 10 -> 38 |
| `969ec1d50c6e53243f82` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 10 -> 18 -> 89 |
| `9e5e28ecb38ea2a53a15` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\scene\ma_pac_wwd_02_holocall_brief.scene` / scene / 254 -> 64 -> 58 |
| `d6b7c21f5d2d0ab76fc6` | 2 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\scene\ma_pac_wwd_02_holocall_brief.scene` / scene / 258 -> 256 -> 260 |
| `054f38c171189e352254` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 10 -> 45 -> 46 |
| `0bc8f68e59c0b883af0d` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 95 -> 75 -> 78 |
| `0c45bf12915e990be5f2` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 9 -> 10 -> 39 |
| `101b60945ddf6f25f378` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\scene\ma_pac_wwd_02_holocall_brief.scene` / scene / 18 -> 63 -> 65 |
| `12208b60f11caf6d936e` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 62 -> 83 -> 66 |
| `1520ebe4ea0bf9451321` | 1 | `base\open_world\minor_activities\pacifica\west_wind_estate\ma_pac_wwd_02\ma_pac_wwd_02_phase.questphase` / h0 / 76 -> 77 -> 74 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
