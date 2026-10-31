# ep1-sa-ep1-31

Depot-family structural inventory. Resources can be shared or belong to test/repair paths. No playable-quest identity or runtime reachability is inferred from the directory.

| Resource | Path role | Quest graphs / scene nodes | Calls and community bindings |
| --- | --- | --- | --- |
| `ep1\openworld\sandbox_activities\sa_ep1_31\community\sa_ep1_31_av_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_31\community\sa_ep1_31_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_31\community\sa_ep1_31_var_01_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_31\community\sa_ep1_31_var_01_mq304_com.community` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.gamedef` | content candidate | 0 / 0 |  |
| `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.quest` | content candidate | 1 / 0 | ep1\openworld\sandbox_activities\sa_ep1_30\scenes\sa_ep1_30_chicken_test.scene; ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase |
| `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` | content candidate | 5 / 0 |  |

## Journal paths observed in these resources

No stored journal path in this family.

## Stored mechanisms

| Type signature | Nodes |
| --- | --- |
| `questAudioNodeDefinition[questAudioEventNodeType]` | 8 |
| `questCharacterManagerNodeDefinition[questCharacterManagerVisuals_ChangeEntityAppearance,questCharacterManagerVisuals_EntityAppearanceOperationBaseEntityAppearanceEntry,questCharacterManagerVisuals_NodeType]` | 2 |
| `questCheckpointNodeDefinition` | 2 |
| `questConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 5 |
| `questCrowdManagerNodeDefinition[questCrowdManagerNodeType_EnableNullArea]` | 4 |
| `questCutControlNodeDefinition` | 2 |
| `questEventManagerNodeDefinition` | 6 |
| `questFXManagerNodeDefinition[questPlayFX_NodeType,questPlayFX_NodeTypeParams]` | 6 |
| `questFactsDBManagerNodeDefinition[questSetVar_NodeType]` | 18 |
| `questInputNodeDefinition` | 7 |
| `questItemManagerNodeDefinition[questReInitContainers_NodeType,questReInitContainers_NodeTypeParams]` | 1 |
| `questLogicalAndNodeDefinition` | 2 |
| `questLogicalHubNodeDefinition` | 2 |
| `questLogicalXorNodeDefinition` | 2 |
| `questMiscAICommandNode` | 8 |
| `questOutputNodeDefinition` | 7 |
| `questPauseConditionNodeDefinition[questCharacterCombat_ConditionType,questCharacterCondition,questLogicalCondition,questTriggerCondition]` | 1 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterHit_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questCharacterCondition,questCharacterSpawned_ConditionType,questComparisonParam]` | 10 |
| `questPauseConditionNodeDefinition[questFactsDBCondition,questVarComparison_ConditionType]` | 2 |
| `questPauseConditionNodeDefinition[questInteraction_ConditionType,questObjectCondition]` | 2 |
| `questPauseConditionNodeDefinition[questNodeLoadingCondition]` | 1 |
| `questPauseConditionNodeDefinition[questRealtimeDelay_ConditionType,questTimeCondition]` | 6 |
| `questPauseConditionNodeDefinition[questTriggerCondition]` | 9 |
| `questPhaseNodeDefinition` | 5 |
| `questSceneNodeDefinition[scnWorldMarker]` | 1 |
| `questSpawnManagerNodeDefinition[questCommunityTemplate_NodeType,questSpawnManagerNodeActionEntry]` | 18 |
| `questSpawnManagerNodeDefinition[questSpawnManagerNodeActionEntry,questSpawner_NodeType]` | 6 |
| `questStartNodeDefinition` | 1 |
| `questSwitchNodeDefinition[questConditionItem,questFactsDBCondition,questVarComparison_ConditionType]` | 1 |
| `questUIManagerNodeDefinition[questDisplayMessageBox_NodeType]` | 1 |
| `questVehicleNodeDefinition[questMoveOnSpline_NodeType]` | 4 |
| `questWorldDataManagerNodeDefinition[questTogglePrefabVariant_NodeType,questTogglePrefabVariant_NodeTypeParams,questVariantState]` | 4 |

## Recurrent connected paths

| Signature | Occurrences in family | Example |
| --- | --- | --- |
| `95b7458b3ffd83fd4357` | 8 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h14 / 37 -> 44 -> 55 |
| `fd6abc96d7197725e3e8` | 5 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h468 / 84 -> 35 -> 81 |
| `05c7a2151e0cd17400d5` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 26 -> 30 -> 3 |
| `3e6653e916afcf7cc2e1` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 26 -> 30 -> 21 |
| `fc910f43d5ff9aabecc6` | 4 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 2 -> 26 -> 30 |
| `1553ea49805c9d5b4f24` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h14 / 51 -> 49 -> 50 |
| `181f231b641eba46ad3b` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 30 -> 3 -> 29 |
| `2165c31c38fd80af8cdc` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 41 -> 42 -> 38 |
| `2765fcbe8f4e745fbc8e` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 31 -> 34 -> 40 |
| `2f5e3055753dc4c41645` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 42 -> 38 -> 12 |
| `2fb18be6f0f0cc83eee7` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 34 -> 40 -> 27 |
| `2fef53694f4256108f17` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h14 / 69 -> 52 -> 47 |
| `43614d3e2db5dc5f8e81` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 31 -> 34 -> 32 |
| `4c7ebd8b4557df747ce3` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h14 / 46 -> 59 -> 63 |
| `54eef4999910e7f93c1a` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 34 -> 32 -> 35 |
| `5970ed4a5b4dd61f3ef9` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 26 -> 44 -> 43 |
| `643565833265bc9c86f6` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 39 -> 41 -> 42 |
| `6791cbbe6b26cff8e34a` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h256 / 2 -> 26 -> 44 |
| `699569630b1f443678c0` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h14 / 75 -> 96 -> 43 |
| `6c0d35667d36d3854c27` | 2 | `ep1\openworld\sandbox_activities\sa_ep1_31\sa_ep1_31.questphase` / h14 / 0 -> 81 -> 49 |

Full source pointers, bindings, facts and graph sockets are in the corresponding compressed evidence shard. See [method](../all-quests-method.md) and [connected patterns](../all-quest-findings.md).
