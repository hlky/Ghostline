# ep1-sa-ep1-32

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\sa_ep1_32\communities\sa_ep1_32_av_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_32\communities\sa_ep1_32_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_32\communities\sa_ep1_32_var_01_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_32\communities\sa_ep1_32_var_01b_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_32\communities\sa_ep1_32_var_02_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_32\communities\sa_ep1_32_var_mq304_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.quest` | content candidate | 1 / 0 | ep1\openworld\sandbox_activities\sa_ep1_30\scenes\sa_ep1_30_chicken_test.scene; ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase |
| `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` | content candidate | 7 / 0 |  |

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
| `questCombatNodeDefinition` | 48 |
| `questCombatNodeDefinition[questCombatNodeParams_CombatTarget]` | 1 |
| `questCombatNodeDefinition[questCombatNodeParams_UseCover]` | 4 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 7 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 6 |
| `questCutControlNodeDefinition` | 3 |
| `questDeletionMarkerNodeDefinition` | 3 |
| `questEventManagerNodeDefinition` | 11 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 12 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 25 |
| `questInputNodeDefinition` | 10 |
| `questItemManagerNodeDefinition[questInjectLoot_NodeType,questInjectLoot_NodeTypeParams,questInjectLoot_NodeTypeParams_OperationData,questUniversalRef]` | 1 |
| `questItemManagerNodeDefinition[questReInitContainers_NodeType,questReInitContainers_NodeTypeParams]` | 2 |
| `questLogicalAndNodeDefinition` | 5 |
| `questLogicalHubNodeDefinition` | 11 |
| `questLogicalXorNodeDefinition` | 5 |
| `questMiscAICommandNode` | 9 |
| `questOutputNodeDefinition` | 10 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 6 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam,questLogicalCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 3 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 3 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 2 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 12 |
| `questPauseConditionNodeDefinition[questTickDelay_ConditionType,questTimeCondition]` | 1 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 17 |
| `questPauseConditionNodeDefinition[questVehicleCondition,questVehicleSpawned_ConditionType]` | 2 |
| `questPhaseNodeDefinition` | 7 |
| `questRandomizerNodeDefinition` | 1 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 29 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 12 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 6 |
| `questVehicleNodeDefinition[questToggleDoor_NodeType]` | 3 |
| `questVehicleNodeDefinition[questToggleWindow_NodeType]` | 2 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 6 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 9 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h1455 / 63 -> 46 -> 47 |
| `05c7a2151e0cd17400d5` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h295 / 26 -> 30 -> 3 |
| `3e6653e916afcf7cc2e1` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h295 / 26 -> 30 -> 21 |
| `fc910f43d5ff9aabecc6` | 6 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h295 / 2 -> 26 -> 30 |
| `3d535fe8a50486459d38` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h7 / 27 -> 29 -> 28 |
| `a1cfd83a8f4b572bf513` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h1455 / 50 -> 18 -> 80 |
| `0307c8e1c2bd71322d7d` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h7 / 52 -> 35 -> 80 |
| `0f6060800f34fba21084` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h7 / 54 -> 52 -> 35 |
| `1553ea49805c9d5b4f24` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h7 / 23 -> 21 -> 22 |
| `181f231b641eba46ad3b` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h295 / 30 -> 3 -> 29 |
| `2165c31c38fd80af8cdc` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h295 / 42 -> 43 -> 38 |
| `2765fcbe8f4e745fbc8e` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h295 / 31 -> 36 -> 40 |
| `2c14c6ff67f32d1ff7f0` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h7 / 84 -> 19 -> 15 |
| `2dfa184e3774a4a8c13b` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h7 / 50 -> 5 -> 23 |
| `2f5e3055753dc4c41645` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h295 / 43 -> 38 -> 12 |
| `2fb18be6f0f0cc83eee7` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h295 / 36 -> 40 -> 27 |
| `3e87f6709cd1c631b301` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h7 / 36 -> 50 -> 69 |
| `43614d3e2db5dc5f8e81` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h295 / 31 -> 36 -> 32 |
| `54eef4999910e7f93c1a` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h295 / 36 -> 32 -> 34 |
| `5970ed4a5b4dd61f3ef9` | 3 | `ep1\openworld\sandbox_activities\sa_ep1_32\sa_ep1_32.questphase` / h295 / 26 -> 45 -> 44 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
