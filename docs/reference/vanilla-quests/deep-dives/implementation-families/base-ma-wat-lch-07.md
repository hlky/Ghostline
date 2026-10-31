# base-ma-wat-lch-07

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\community\ma_wat_lch_07_after_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\community\ma_wat_lch_07_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\community\ma_wat_lch_07_police_com.community` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07.gamedef` | content candidate | 0 / 0 |  |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07.quest` | content candidate | 1 / 0 | base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase |
| `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` | content candidate | 9 / 0 |  |

## Journal paths observed in these resources

- `onscreens/emails/quests/minor_activities/watson/little_china/ma_wat_lch_07/onscreens/ma_wat_lch_07_1`
- `points_of_interest/minor_activities/ma_wat_lch_07`

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questCharacterManagerNodeDefinition[questCharacterManagerCombat_ModifyHealth,questCharacterManagerCombat_NodeType]` | 1 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 3 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetGroupsAttitude]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCheckpointNodeDefinition` | 2 |
| `questCombatNodeDefinition` | 15 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 5 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 11 |
| `questConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questConditionNodeDefinition[questSaveLock_ConditionType,questSystemCondition]` | 2 |
| `questConditionNodeDefinition[questTriggerCondition]` | 1 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 2 |
| `questCutControlNodeDefinition` | 2 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 5 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 9 |
| `questInputNodeDefinition` | 9 |
| `questItemManagerNodeDefinition[questAddRemoveItem_NodeType,questAddRemoveItem_NodeTypeParams,questUniversalRef]` | 1 |
| `questJournalNodeDefinition[questJournalChangeMappinPhase_NodeType]` | 1 |
| `questLogicalAndNodeDefinition` | 1 |
| `questLogicalHubNodeDefinition` | 6 |
| `questLogicalXorNodeDefinition` | 6 |
| `questMiscAICommandNode` | 2 |
| `questMiscAICommandNode[questCombatNodeParams_RestrictMovementToArea]` | 1 |
| `questOutputNodeDefinition` | 5 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questRealtimeDelay_ConditionType,questSystemCondition,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questCameraFocus_ConditionType,questLogicalCondition,questSystemCondition,questTriggerCondition]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 9 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 2 |
| `questPauseConditionNodeDefinition[questDistanceComparison_ConditionType,questDistanceCondition,questObjectDistance,questUniversalRef,questValueDistance]` | 1 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questGameTimeDelay_ConditionType,questTimeCondition]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questInventory_ConditionType,questObjectCondition]` | 1 |
| `questPauseConditionNodeDefinition[questJournalCondition,questJournalEntry_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questLogicalCondition,questSensesCondition,questTriggerCondition,questVision_ConditionType]` | 5 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 5 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 6 |
| `questPhaseNodeDefinition` | 9 |
| `questPuppetAIManagerNodeDefinition[questPuppetAIManagerNodeDefinitionEntry]` | 2 |
| `questRandomizerNodeDefinition` | 2 |
| `questRewardManagerNodeDefinition[questGiveReward_NodeType]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 11 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 2 |
| `questStartNodeDefinition` | 1 |
| `questTeleportPuppetNodeDefinition[questPlayerLookAtParams,questTeleportPuppetParamsV1,questUniversalRef]` | 1 |
| `questUseWorkspotNodeDefinition[questUseWorkspotParamsV1]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `25000233cce168c6c80d` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h711 / 23 -> 29 -> 7 |
| `7e1f82a4f2539df5e599` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h711 / 33 -> 4 -> 8 |
| `f0c5cc02984e51b14ad4` | 3 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h711 / 0 -> 19 -> 33 |
| `009ab5ed7e09b336cf99` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h711 / 14 -> 3 -> 2 |
| `07baf99c782e2088a11d` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h0 / 21 -> 190 -> 102 |
| `402359ccd2ed9636b6ff` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h0 / 182 -> 185 -> 187 |
| `66e17bf07a534afe17b2` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h30 / 8 -> 28 -> 33 |
| `736e12da56db0f348c65` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h30 / 25 -> 26 -> 5 |
| `92232569acfea10f426a` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h711 / 0 -> 14 -> 3 |
| `93e3aee8a35caf9e1d3a` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h267 / 4 -> 7 -> 13 |
| `a909c836470d2b0e7fbc` | 2 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h468 / 0 -> 7 -> 1 |
| `011e16259127225fd710` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h30 / 18 -> 15 -> 31 |
| `07ba6ec1c22c01f77949` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h0 / 200 -> 197 -> 196 |
| `07e466f94b0752a568ea` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h0 / 170 -> 171 -> 165 |
| `0d24f215f601552926d6` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h306 / 16 -> 13 -> 25 |
| `1258cee37e98f0ae14fe` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h0 / 35 -> 51 -> 105 |
| `18be198845c90c6bb3c8` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h30 / 8 -> 28 -> 25 |
| `20a77143a898bc753a26` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h30 / 32 -> 12 -> 17 |
| `2409c4dae85a47c39375` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h0 / 21 -> 190 -> 50 |
| `2a074e09ac55462855fd` | 1 | `base\open_world\minor_activities\watson\little_china\ma_wat_lch_07\ma_wat_lch_07_phase.questphase` / h306 / 0 -> 2 -> 24 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
