# ep1-sa-ep1-36

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\sa_ep1_36\communities\sa_ep1_36_av_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_36\communities\sa_ep1_36_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_36\communities\sa_ep1_36_reinforcement.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_36\communities\sa_ep1_36_var_01_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_36\communities\sa_ep1_36_var_01b_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_36\communities\sa_ep1_36_var_02_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.quest` | content candidate | 1 / 0 | ep1\openworld\sandbox_activities\sa_ep1_30\scenes\sa_ep1_30_chicken_test.scene; ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase |
| `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` | content candidate | 8 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 12 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetAttitudeGroupForPuppet]` | 2 |
| `questCharacterManagerNodeDefinition[questCharacterManagerParameters_NodeType,questCharacterManagerParameters_SetMortality]` | 4 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 3 |
| `questCheckpointNodeDefinition` | 3 |
| `questCombatNodeDefinition` | 50 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 10 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 6 |
| `questCutControlNodeDefinition` | 3 |
| `questEntityManagerNodeDefinition[questEntityManagerToggleComponent_NodeType,questEntityManagerToggleComponent_NodeTypeParams]` | 3 |
| `questEventManagerNodeDefinition` | 11 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 13 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 26 |
| `questInputNodeDefinition` | 11 |
| `questItemManagerNodeDefinition[questReInitContainers_NodeType,questReInitContainers_NodeTypeParams]` | 2 |
| `questLogicalAndNodeDefinition` | 5 |
| `questLogicalHubNodeDefinition` | 10 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMiscAICommandNode` | 11 |
| `questOutputNodeDefinition` | 11 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 4 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterKilled_ConditionType,questComparisonParam]` | 3 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterMount_ConditionType]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 11 |
| `questPauseConditionNodeDefinition[questDevice_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 4 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 13 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 3 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 15 |
| `questPhaseNodeDefinition` | 8 |
| `questRandomizerNodeDefinition` | 2 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 35 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questVehicleNodeCommandDefinition[questParamKeepDistance,questParamRubberbanding,questUniversalRef,questVehicleCommandParams,questvehicleChaseParams,questvehicleFollowParams,questvehicleJoinTrafficParams,questvehicleOnSplineParams,questvehiclePanicParams,questvehicleRacingParams,questvehicleToNodeParams]` | 1 |
| `questVehicleNodeDefinition[questAssignCharacter_NodeType]` | 4 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 6 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 4 |
| `questVehicleNodeDefinition[questToggleWindow_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 11 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `05c7a2151e0cd17400d5` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h270 / 26 -> 30 -> 3 |
| `3e6653e916afcf7cc2e1` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h270 / 26 -> 30 -> 21 |
| `fc910f43d5ff9aabecc6` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h270 / 2 -> 26 -> 30 |
| `120c5c4bbfcbfae70bc4` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h7 / 284 -> 283 -> 285 |
| `27d3d4c401ea569d6469` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h1576 / 193 -> 194 -> 209 |
| `7787bd2947640f7916d8` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h1132 / 2 -> 10 -> 8 |
| `cb15f618f342a00de266` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h7 / 298 -> 289 -> 290 |
| `01cc762cd06f16743b1c` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h7 / 202 -> 228 -> 189 |
| `1553ea49805c9d5b4f24` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h7 / 210 -> 208 -> 209 |
| `181f231b641eba46ad3b` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h270 / 30 -> 3 -> 29 |
| `20a77143a898bc753a26` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h7 / 205 -> 245 -> 309 |
| `2165c31c38fd80af8cdc` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h270 / 41 -> 42 -> 38 |
| `2734b8ca598133b05e14` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h7 / 305 -> 308 -> 206 |
| `2765fcbe8f4e745fbc8e` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h270 / 31 -> 36 -> 40 |
| `2f5e3055753dc4c41645` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h270 / 42 -> 38 -> 12 |
| `2fb18be6f0f0cc83eee7` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h270 / 36 -> 40 -> 27 |
| `38a7250852311a112649` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h7 / 225 -> 307 -> 202 |
| `43614d3e2db5dc5f8e81` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h270 / 31 -> 36 -> 32 |
| `4798537ca16e1216226c` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h7 / 245 -> 309 -> 233 |
| `4cfa2ab7900c50b0a71a` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_36\sa_ep1_36.questphase` / h7 / 304 -> 205 -> 245 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
