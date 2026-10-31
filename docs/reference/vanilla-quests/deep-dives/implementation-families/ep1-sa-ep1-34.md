# ep1-sa-ep1-34

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\sa_ep1_34\communities\sa_ep1_34_av_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_34\communities\sa_ep1_34_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_34\communities\sa_ep1_34_mq304_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_34\communities\sa_ep1_34_reinforcement_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_34\communities\sa_ep1_34_var_01_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_34\communities\sa_ep1_34_var_02_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.quest` | content candidate | 1 / 0 | ep1\openworld\sandbox_activities\sa_ep1_30\scenes\sa_ep1_30_chicken_test.scene; ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase |
| `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` | content candidate | 7 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 12 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 3 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questLogicalCondition,questVarComparison_ConditionType]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 11 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 6 |
| `questCutControlNodeDefinition` | 3 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 5 |
| `questEventManagerNodeDefinition` | 9 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 15 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 26 |
| `questInputNodeDefinition` | 10 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 2 |
| `questItemManagerNodeDefinition[questReInitContainers_NodeType,questReInitContainers_NodeTypeParams]` | 2 |
| `questLogicalAndNodeDefinition` | 4 |
| `questLogicalHubNodeDefinition` | 3 |
| `questLogicalXorNodeDefinition` | 3 |
| `questMiscAICommandNode` | 10 |
| `questOutputNodeDefinition` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 13 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 4 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPhaseNodeDefinition` | 7 |
| `questRandomizerNodeDefinition` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 35 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questTransformAnimatorNodeDefinition[questTransformAnimatorNode_Action_Play]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 6 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 12 |
| `questVehicleNodeDefinition[questToggleWindow_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 10 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `27d3d4c401ea569d6469` | 10 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 123 -> 124 -> 116 |
| `20a77143a898bc753a26` | 7 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 109 -> 149 -> 186 |
| `05c7a2151e0cd17400d5` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h273 / 26 -> 30 -> 3 |
| `3e6653e916afcf7cc2e1` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h273 / 26 -> 30 -> 21 |
| `fc910f43d5ff9aabecc6` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h273 / 2 -> 26 -> 30 |
| `a5f6ff0df46f7043f2b5` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 101 -> 123 -> 124 |
| `6791cbbe6b26cff8e34a` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 159 -> 172 -> 163 |
| `adbe18e6b3506054cc56` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 96 -> 114 -> 135 |
| `c41e0d15580f011aaf42` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 96 -> 114 -> 112 |
| `cb15f618f342a00de266` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 172 -> 163 -> 164 |
| `d20044f4ad342a7ac284` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 96 -> 114 -> 176 |
| `01cc762cd06f16743b1c` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 106 -> 131 -> 93 |
| `0307c8e1c2bd71322d7d` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 144 -> 120 -> 177 |
| `0f6060800f34fba21084` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 136 -> 144 -> 120 |
| `1553ea49805c9d5b4f24` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h7 / 114 -> 112 -> 113 |
| `181f231b641eba46ad3b` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h273 / 30 -> 3 -> 29 |
| `2165c31c38fd80af8cdc` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h273 / 42 -> 44 -> 38 |
| `2765fcbe8f4e745fbc8e` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h273 / 31 -> 36 -> 43 |
| `2f5e3055753dc4c41645` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h273 / 44 -> 38 -> 12 |
| `2fb18be6f0f0cc83eee7` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_34\sa_ep1_34.questphase` / h273 / 36 -> 43 -> 27 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
